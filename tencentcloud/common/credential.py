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
import threading

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
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile


class Credential(object):
    """Tencent Cloud Credentials.

    Access https://console.cloud.tencent.com/cam/capi to manage your credentials.

    :param secret_id: The secret id of your credential.
    :type secret_id: str
    :param secret_key: The secret key of your credential.
    :type secret_key: str
    :param token: The federation token of your credential, if this field
                  is specified, secret_id and secret_key should be set
                  accordingly, see: https://cloud.tencent.com/document/product/598/13896
    """

    def __init__(self, secret_id, secret_key, token=None):
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
    
    def get_credential_info(self):
        return self.secret_id, self.secret_key, self.token


class CVMRoleCredential(object):
    """Tencent Cloud Credential via CVM role

    Automatically generates temporary credentials when binding a service role to instance.
    See https://cloud.tencent.com/document/product/598/85616 for more information.
    """
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
        self._lock = threading.Lock()

    @property
    def secretId(self):
        return self.secret_id

    @property
    def secret_id(self):
        with self._lock:
            self.update_credential()
            return self._secret_id

    @property
    def secretKey(self):
        return self.secret_key

    @property
    def secret_key(self):
        with self._lock:
            self.update_credential()
            return self._secret_key

    @property
    def token(self):
        with self._lock:
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

    def get_credential_info(self):
        with self._lock:
            self.update_credential()
            return self._secret_id, self._secret_key, self._token


class STSAssumeRoleCredential(object):
    """Tencent Cloud Credential via STS service

    Automatically generates temporary credentials for API calls.

    :param secret_id: The secret id of your credential.
    :type secret_id: str
    :param secret_key: The secret key of your credential.
    :type secret_key: str
    :param role_arn: Resource descriptions of a role，see https://cloud.tencent.com/document/api/1312/48197
    :type role_arn: str
    :param role_session_name: User-defined temporary session name
    :type role_session_name: str
    :param duration_seconds: Specifies the validity period of credentials in seconds. Default value: 7200. Maximum value: 43200
    :type duration_seconds: int
    """
    _region = "ap-guangzhou"
    _version = '2018-08-13'
    _service = "sts"
    _endpoint = "sts.tencentcloudapi.com"

    def __init__(self, secret_id, secret_key, role_arn, role_session_name, duration_seconds=7200, endpoint=None):
        """

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
        if endpoint:
            self._endpoint = endpoint
        self._lock = threading.Lock()

    @property
    def secretId(self):
        with self._lock:
            self._need_refresh()
            return self._tmp_secret_id

    @property
    def secretKey(self):
        with self._lock:
            self._need_refresh()
            return self._tmp_secret_key

    @property
    def secret_id(self):
        with self._lock:
            self._need_refresh()
            return self._tmp_secret_id

    @property
    def secret_key(self):
        with self._lock:
            self._need_refresh()
            return self._tmp_secret_key

    @property
    def token(self):
        with self._lock:
            self._need_refresh()
            return self._token
    
    def get_credential_info(self):
        with self._lock:
            self._need_refresh()
            return self._tmp_secret_id, self._tmp_secret_key, self._token

    def _need_refresh(self):
        if None in [self._token, self._tmp_secret_key, self._tmp_secret_id] or self._expired_time < int(time.time()):
            self.get_sts_tmp_role_arn()

    def get_sts_tmp_role_arn(self):
        cred = Credential(self._long_secret_id, self._long_secret_key)
        http_profile = HttpProfile()
        http_profile.endpoint = self._endpoint
        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile

        common_client = CommonClient(credential=cred, region=self._region, version=self._version,
                                     service=self._service, profile=client_profile)
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


class EnvironmentVariableCredential(object):
    """Tencent Cloud EnvironmentVariableCredential.

    Acquire credential from environment variables.
    Access https://console.cloud.tencent.com/cam/capi to manage your credentials.
    Set secret id and secret key as `TENCENTCLOUD_SECRET_ID` and `TENCENTCLOUD_SECRET_KEY `in environment variables.
    """

    def get_credential(self):
        self.secret_id = os.environ.get('TENCENTCLOUD_SECRET_ID')
        self.secret_key = os.environ.get('TENCENTCLOUD_SECRET_KEY')

        if self.secret_id is None or self.secret_key is None:
            return None
        if len(self.secret_id) == 0 or len(self.secret_key) == 0:
            return None
        return Credential(self.secret_id, self.secret_key)


class ProfileCredential(object):
    """Tencent Cloud ProfileCredential.

    Access https://console.cloud.tencent.com/cam/capi to manage your credentials.
    default file position is "~/.tencentcloud/credentials" or "/etc/tencentcloud/credentials", it is ini format.
    such as:
    [default]
    secret_id=""
    secret_key=""
    """

    def get_credential(self):
        if os.path.exists(os.path.expanduser("~/.tencentcloud/credentials")):
            file_path = os.path.expanduser("~/.tencentcloud/credentials")
        elif os.path.exists("/etc/tencentcloud/credentials"):
            file_path = "/etc/tencentcloud/credentials"
        else:
            file_path = ""
        if file_path:
            # loads config
            conf = configparser.ConfigParser()
            conf.read(file_path)
            ini_map = dict(conf._sections)
            for k in dict(conf._sections):
                option = dict(ini_map[k])
                for key, value in dict(ini_map[k]).items():
                    option[key] = value.strip()
                ini_map[k] = option
            if "default" in ini_map:
                client_config = ini_map.get("default")
                self.secret_id = client_config.get('secret_id', None)
                self.secret_key = client_config.get('secret_key', None)
                self.role_arn = client_config.get('role_arn', None)
        else:
            self.secret_id = None
            self.secret_key = None
            self.role_arn = None

        if self.secret_id is None or self.secret_key is None:
            return None
        if len(self.secret_id) == 0 or len(self.secret_key) == 0:
            return None
        return Credential(self.secret_id, self.secret_key)


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
    """Acquire credential via TKE IdP automatically."""
    def get_credential(self):
        return self.get_credentials()

    def get_credentials(self):
        cred = OIDCRoleArnCredential('', '', '', '', '', 7200)
        cred._is_tke = True
        cred._init_from_tke()
        return cred


class OIDCRoleArnCredential(object):
    """TencentCloud OIDC Credential

    OIDC is an authentication protocol built on OAuth 2.0. Tencent Cloud CAM supports OIDC role-based SSO.
    See https://cloud.tencent.com/document/product/598/96013 for more information.
    This will apply for an OIDC role credential automatically.

    :param region: Region for AssumeRoleWithWebIdentity call. See https://cloud.tencent.com/document/product/1312/73070
    :type region: str
    :param provider_id: Identity provider name
    :type provider_id: str
    :param web_identity_token: OIDC token issued by the IdP
    :type web_identity_token: str
    :param role_arn: Role access description name
    :type role_arn: str
    :param role_session_name: Session name
    :type role_session_name: str
    :param duration_seconds: The validity period of the temporary credential in seconds. Default value: 7200s. Maximum value: 43200s.
    :type duration_seconds: int
    """
    _version = '2018-08-13'
    _service = "sts"
    _action = 'AssumeRoleWithWebIdentity'
    _default_session_name = 'tencentcloud-python-sdk-'
    _endpoint = "sts.tencentcloudapi.com"

    def __init__(self, region, provider_id, web_identity_token, role_arn, role_session_name, duration_seconds=7200, endpoint=None):
        self._region = region
        self._provider_id = provider_id
        self._web_identity_token = web_identity_token
        self._role_arn = role_arn
        self._role_session_name = role_session_name
        self._duration_seconds = duration_seconds
        if endpoint:
            self._endpoint = endpoint

        self._token = None
        self._tmp_secret_id = None
        self._tmp_secret_key = None
        self._expired_time = 0
        self._is_tke = False
        self._lock = threading.Lock()

    @property
    def secretId(self):
        with self._lock:
            self._keep_fresh()
            return self._tmp_secret_id

    @property
    def secretKey(self):
        with self._lock:
            self._keep_fresh()
            return self._tmp_secret_key

    @property
    def secret_id(self):
        with self._lock:
            self._keep_fresh()
            return self._tmp_secret_id

    @property
    def secret_key(self):
        with self._lock:
            self._keep_fresh()
            return self._tmp_secret_key

    @property
    def token(self):
        with self._lock:
            self._keep_fresh()
            return self._token
        
    def get_credential_info(self):
        with self._lock:
            self._keep_fresh()
            return self._tmp_secret_id, self._tmp_secret_key, self._token

    @property
    def endpoint(self):
        return self._endpoint
    
    @endpoint.setter
    def endpoint(self, endpoint):
        self._endpoint = endpoint

    def _keep_fresh(self):
        if None in [self._token, self._tmp_secret_key, self._tmp_secret_id] or self._expired_time < int(time.time()):
            self.refresh()

    def refresh(self):
        if self._is_tke:
            self._init_from_tke()
            
        http_profile = HttpProfile()
        http_profile.endpoint = self._endpoint
        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        
        common_client = CommonClient(credential=None, region=self._region, version=self._version, 
                                     service=self._service, profile=client_profile)
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
        self._expired_time = rsp["Response"]["ExpiredTime"] - self._duration_seconds * 0.1

    def _init_from_tke(self):
        self._region = os.getenv('TKE_REGION')
        if not self._region:
            raise EnvironmentError("TKE_REGION not exist")

        self._provider_id = os.getenv('TKE_PROVIDER_ID')
        if not self._provider_id:
            raise EnvironmentError("TKE_PROVIDER_ID not exist")

        token_file = os.getenv('TKE_WEB_IDENTITY_TOKEN_FILE')
        if not token_file:
            raise EnvironmentError("TKE_WEB_IDENTITY_TOKEN_FILE not exist")

        with open(token_file) as f:
            self._web_identity_token = f.read()

        self._role_arn = os.getenv('TKE_ROLE_ARN')
        if not self._role_arn:
            raise EnvironmentError("TKE_ROLE_ARN not exist")

        self._role_session_name = self._default_session_name + str(time.time() * 1e6)  # time in microsecond
