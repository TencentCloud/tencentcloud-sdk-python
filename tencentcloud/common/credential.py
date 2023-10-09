# -*- coding: utf-8 -*-
# Copyright (c) 2018 Tencent Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os
import time
try:
    # py3
    import configparser
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    # py2
    import ConfigParser as configparser
    from urllib import urlencode
    from urllib import urlopen

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.common_client import CommonClient
from typing import Union

class Credential(object):
    def __init__(self, secret_id, secret_key, token=None):
        """Tencent Cloud Credentials.

        Access https://console.cloud.tencent.com/cam/capi to manage your
        credentials.

        :param secret_id: The secret id of your credential.
        :type secret_id: str
        :param secret_key: The secret key of your credential.
        :type secret_key: str
        :param token: The federation token of your credential, if this field
                      is specified, secret_id and secret_key should be set
                      accordingly, see: https://cloud.tencent.com/document/product/598/13896
        """
        if secret_id is None or secret_id.strip() == "":
            raise TencentCloudSDKException("InvalidCredential", "secret id should not be none or empty")
        if secret_id.strip() != secret_id:
            raise TencentCloudSDKException("InvalidCredential", "secret id should not contain spaces")
        self.secret_id = secret_id

        if secret_key is None or secret_key.strip() == "":
            raise TencentCloudSDKException("InvalidCredential", "secret key should not be none or empty")
        if secret_key.strip() != secret_key:
            raise TencentCloudSDKException("InvalidCredential", "secret key should not contain spaces")
        self.secret_key = secret_key

        self.token = token

    @property
    def secretId(self):
        return self.secret_id

    @property
    def secretKey(self):
        return self.secret_key


class CVMRoleCredential(object):
    _metadata_endpoint = "http://metadata.tencentyun.com/latest/meta-data/"
    _role_endpoint = _metadata_endpoint + "cam/security-credentials/"
    # In seconds.
    # Signatrue will fail if request timestamp gap is larger than 300s,
    # so a strategy to refresh token just before that time is acceptable.
    _expired_timeout = 300

    def __init__(self, role_name=None):
        self.role = role_name
        self._secret_id = None
        self._secret_key = None
        self._token = None
        self._expired_ts = 0

    @property
    def secretId(self):
        return self.secret_id

    @property
    def secret_id(self):
        self.update_credential()
        return self._secret_id

    @property
    def secretKey(self):
        return self.secret_key

    @property
    def secret_key(self):
        self.update_credential()
        return self._secret_key

    @property
    def token(self):
        self.update_credential()
        return self._token

    def get_role_name(self):
        if self.role:
            return self.role
        try:
            resp = urlopen(self._role_endpoint)
            self.role = resp.read().decode("utf8")
        except Exception as e:
            raise TencentCloudSDKException("ClientError.MetadataError", str(e))
        finally:
            return self.role

    def _need_refresh(self):
        ts_remain = self._expired_ts - int(time.time())
        if ts_remain <= self._expired_timeout:
            return True
        else:
            return False

    def update_credential(self):
        if not self._need_refresh():
            return
        role = self.get_role_name()
        try:
            # TODO: what if role has special characters such as space and unicode?
            resp = urlopen(self._role_endpoint + role)
            # py3 requires it to be string rather than byte
            data = resp.read().decode("utf8")
            j = json.loads(data)
            if j.get("Code") != "Success":
                raise Exception("CVM role token data failed: %s" % data)
            self._secret_id = j["TmpSecretId"]
            self._secret_key = j["TmpSecretKey"]
            self._token = j["Token"]
            self._expired_ts = j["ExpiredTime"]
        except Exception as e:
            # we shoud log it
            # maybe we should validate token to None as well
            pass

    def get_credential(self):
        if not self.secret_id or not self.secret_key or not self.token:
            return None
        return self


class STSAssumeRoleCredential(object):
    """使用STSAssumeRoleCredential，制动role，
    可以自动生成临时凭证，并使用临时凭证调用接口

    """
    _region = "ap-guangzhou"
    _version = '2018-08-13'
    _service = "sts"

    def __init__(self, secret_id, secret_key, role_arn, role_session_name, duration_seconds=7200):
        """
        :param secret_id: 接口调用凭证id
        :type secret_id: str
        :param secret_key: 接口调用凭证key
        :type secret_key: str
        https://cloud.tencent.com/document/api/1312/48197
        :param role_arn: 角色的资源描述，参考官网文档 https://cloud.tencent.com/document/api/1312/48197 中 RoleArn 参数的描述。
        :type role_arn: str
        :param role_session_name: 临时会话名称，由用户自定义名称
        :type role_session_name: str
        :param duration_seconds: 获取临时凭证的有效期，默认7200s
        :type duration_seconds: int
        """
        self._long_secret_id = secret_id
        self._long_secret_key = secret_key
        self._role_arn = role_arn
        self._role_session_name = role_session_name
        self._duration_seconds = duration_seconds

        self._token = None
        self._tmp_secret_id = None
        self._tmp_secret_key = None
        self._expired_time = 0

        self._last_role_arn = None
        self._tmp_credential = None

    @property
    def secretId(self):
        self._need_refresh()
        return self._tmp_secret_id

    @property
    def secretKey(self):
        self._need_refresh()
        return self._tmp_secret_key

    @property
    def secret_id(self):
        self._need_refresh()
        return self._tmp_secret_id

    @property
    def secret_key(self):
        self._need_refresh()
        return self._tmp_secret_key

    @property
    def token(self):
        self._need_refresh()
        return self._token

    def _need_refresh(self):
        """
        https://cloud.tencent.com/document/api/1312/48197
        此函数自动使用初始secret_id和secret_key，自动调用上述链接中获取临时凭证的接口，并返回临时凭证

        :param role_arn: 角色的资源描述，上述链接RoleArn参数中有详细获取方式
        :type role_arn: str
        :param role_session_name: 临时会话名称，由用户自定义名称
        :type role_session_name: str
        :param duration_seconds: 获取临时凭证的有效期，默认7200s
        :type duration_seconds: int

        """

        if None in [self._token, self._tmp_secret_key, self._tmp_secret_id] or self._expired_time < int(time.time()):
            self.get_sts_tmp_role_arn()

    def get_sts_tmp_role_arn(self):
        cred = Credential(self._long_secret_id, self._long_secret_key)

        common_client = CommonClient(credential=cred, region=self._region, version=self._version, service=self._service)
        params = {
            "RoleArn": self._role_arn,
            "RoleSessionName": self._role_session_name,
            "DurationSeconds": self._duration_seconds,
        }

        rsp = common_client.call_json("AssumeRole", params)
        self._token = rsp["Response"]["Credentials"]["Token"]
        self._tmp_secret_id = rsp["Response"]["Credentials"]["TmpSecretId"]
        self._tmp_secret_key = rsp["Response"]["Credentials"]["TmpSecretKey"]
        self._expired_time = rsp["Response"]["ExpiredTime"] - self._duration_seconds * 0.9


class EnvironmentVariableCredential():

    def get_credential(self):
        """Tencent Cloud EnvironmentVariableCredential.

        Access https://console.cloud.tencent.com/cam/capi to manage your
        credentials.

        :param secret_id: The secret id of your credential, get by environment variable TENCENTCLOUD_SECRET_ID
        :type secret_id: str
        :param secret_key: The secret key of your credential. get by environment variable TENCENTCLOUD_SECRET_KEY
        :type secret_key: str
        """
        self.secret_id = os.environ.get('TENCENTCLOUD_SECRET_ID')
        self.secret_key = os.environ.get('TENCENTCLOUD_SECRET_KEY')

        if self.secret_id is None or self.secret_key is None:
            return None
        if len(self.secret_id) == 0 or len(self.secret_key) == 0:
            return None
        return Credential(self.secret_id, self.secret_key)


class ProfileCredential():

    def __init__(self, profile='default') -> None:
        self.profile = profile
    
    def get_credential(self) -> Union[Credential, STSAssumeRoleCredential]:
        """
        params:
            profile: the profile name
            profile_path: the profile path, deafult path is '~/tencentcloud/credentials'
        des:
            support use profile to auth account and multi-account
        credentials details, such as:
            ```
                [default] (the ak/sk profile')
                secret_id:xxxx
                secret_key:xxxx
                token: xxxx

                [profile] (the role profile)
                role_arn: xxx (required)
                session_name: xxx (default is 'tencentcloud-session')
                duration_seconds: 3600 (default is 3600)
                source_profile: xxx (required, the role'carrier, support 'ak/sk profile' or 'cvm_role')
            ```
        """
        home_path = os.environ.get('HOME') or os.environ.get('HOMEPATH')
        if os.path.exists(home_path + "/.tencentcloud/credentials"):
            file_path = home_path + "/.tencentcloud/credentials"
        elif os.path.exists("/etc/tencentcloud/credentials"):
            file_path = "/etc/tencentcloud/credentials"
        else:
            raise TencentCloudSDKException(
                'not find credentials path, please setting the credentials path!')
        
        return self.parser_credentials_path(file_path)
        
    def parser_credentials(
            self, credentials_path: str) -> Union[Credential, STSAssumeRoleCredential]:
        
        parser = configparser.ConfigParser()
        parser.read(credentials_path)
        profile_obj = parser.get(self.profile)
        if not profile_obj:
            raise TencentCloudSDKException(f'not find profile: {self.profile}, please check the porfile')
        
        # if not find role_arn the profile is ak/sk'profile
        role_arn = profile_obj.get('role_arn', None)
        if role_arn is None:
            secret_id = profile_obj.get('secret_id')
            secret_key = profile_obj.get('secret_key')
            token = profile_obj.get('token')
            return Credential(secret_id, secret_key, token)
        
        session_name = profile_obj.get('session_name', 'tencentcloud-session')
        duration_seconds = profile_obj.get('duration_seconds', 7200)
        source_profile = profile_obj.get('source_profile')

        # if the source_profile == 'cvm_metadata', you need add the role to cvm, 
        # and the role must have assume the the role permmission
        if source_profile == 'cvm_metadata':
            cred = CVMRoleCredential()
            common_client = CommonClient(
                credential=cred, region="ap-guangzhou", version='2018-08-13', service="sts")
            params = {
                "RoleArn": role_arn,
                "RoleSessionName": session_name,
                "DurationSeconds": duration_seconds
            }
            rsp = common_client.call_json("AssumeRole", params)
            token = rsp["Response"]["Credentials"]["Token"]
            secret_id = rsp["Response"]["Credentials"]["TmpSecretId"]
            secret_key = rsp["Response"]["Credentials"]["TmpSecretKey"]

            return Credential(secret_id, secret_key, token=token)
        else:
            sp_obj = parser.get(source_profile, None)
            if sp_obj is None:
                raise TencentCloudSDKException(
                    f'not find source_profile: {source_profile} in credentials, please check the source_profile')
            secret_id = sp_obj.get('secret_id')
            secret_key = sp_obj.get('secret_key')
            token = sp_obj.get('token')

            return STSAssumeRoleCredential(secret_id, secret_key, role_arn, session_name, duration_seconds)


class DefaultCredentialProvider(object):
    """Tencent Cloud DefaultCredentialProvider.

    DefaultCredentialProvider will search credential by order EnvironmentVariableCredential ProfileCredential
    and CVMRoleCredential.
    """

    def __init__(self):
        self.cred = None

    def get_credential(self):
        return self.get_credentials()

    def get_credentials(self):
        if self.cred is not None:
            return self.cred

        self.cred = EnvironmentVariableCredential().get_credential()
        if self.cred is not None:
            return self.cred

        self.cred = ProfileCredential().get_credential()
        if self.cred is not None:
            return self.cred

        self.cred = CVMRoleCredential().get_credential()
        if self.cred is not None:
            return self.cred

        self.cred = DefaultTkeOIDCRoleArnProvider().get_credential()
        if self.cred is not None:
            return self.cred

        raise TencentCloudSDKException("ClientSideError", "no valid credentail.")


class DefaultTkeOIDCRoleArnProvider(object):
    default_session_name = 'tencentcloud-python-sdk-'

    def __init__(self):
        self.region = os.getenv('TKE_REGION')
        if not self.region:
            raise EnvironmentError("TKE_REGION not exist")

        self.provider_id = os.getenv('TKE_PROVIDER_ID')
        if not self.provider_id:
            raise EnvironmentError("TKE_PROVIDER_ID not exist")

        token_file = os.getenv('TKE_WEB_IDENTITY_TOKEN_FILE')
        if not token_file:
            raise EnvironmentError("TKE_WEB_IDENTITY_TOKEN_FILE not exist")

        with open(token_file) as f:
            self.web_identity_token = f.read()

        self.role_arn = os.getenv('TKE_ROLE_ARN')
        if not self.role_arn:
            raise EnvironmentError("TKE_ROLE_ARN not exist")

        self.role_session_name = self.default_session_name + str(time.time() * 1e6)  # time in microseconds

    def get_credential(self):
        return self.get_credentials()

    def get_credentials(self):
        return OIDCRoleArnCredential(self.region, self.provider_id, self.web_identity_token, self.role_arn,
                                     self.role_session_name)


class OIDCRoleArnCredential(object):
    _version = '2018-08-13'
    _service = "sts"
    _action = 'AssumeRoleWithWebIdentity'

    def __init__(self, region, provider_id, web_identity_token, role_arn, role_session_name, duration_seconds=7200):
        self._region = region
        self._provider_id = provider_id
        self._web_identity_token = web_identity_token
        self._role_arn = role_arn
        self._role_session_name = role_session_name
        self._duration_seconds = duration_seconds

        self._token = None
        self._tmp_secret_id = None
        self._tmp_secret_key = None
        self._expired_time = 0

        self._last_role_arn = None
        self._tmp_credential = None

    @property
    def secretId(self):
        self._keep_fresh()
        return self._tmp_secret_id

    @property
    def secretKey(self):
        self._keep_fresh()
        return self._tmp_secret_key

    @property
    def secret_id(self):
        self._keep_fresh()
        return self._tmp_secret_id

    @property
    def secret_key(self):
        self._keep_fresh()
        return self._tmp_secret_key

    @property
    def token(self):
        self._keep_fresh()
        return self._token

    def _keep_fresh(self):
        if None in [self._token, self._tmp_secret_key, self._tmp_secret_id] or self._expired_time < int(time.time()):
            self.refresh()

    def refresh(self):
        common_client = CommonClient(credential=None, region=self._region, version=self._version, service=self._service)
        params = {
            "ProviderId": self._provider_id,
            "WebIdentityToken": self._web_identity_token,
            "RoleArn": self._role_arn,
            "RoleSessionName": self._role_session_name,
            "DurationSeconds": self._duration_seconds,
        }

        options = {'SkipSign': True}

        rsp = common_client.call_json(self._action, params, options=options)
        self._token = rsp["Response"]["Credentials"]["Token"]
        self._tmp_secret_id = rsp["Response"]["Credentials"]["TmpSecretId"]
        self._tmp_secret_key = rsp["Response"]["Credentials"]["TmpSecretKey"]
        self._expired_time = rsp["Response"]["ExpiredTime"] - self._duration_seconds * 0.9
