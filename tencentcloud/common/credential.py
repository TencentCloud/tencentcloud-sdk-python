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
import time
try:
    # py3
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    # py2
    from urllib import urlencode
    from urllib import urlopen

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

class Credential(object):
    def __init__(self, secretId, secretKey, token=None):
        """Tencent Cloud Credentials.

        Access https://console.cloud.tencent.com/cam/capi to manage your
        credentials.

        :param secretId: The secret id of your credential.
        :type secretId: str
        :param secretKey: The secret key of your credential.
        :type secretKey: str
        :param token: The federation token of your credential, if this field
                      is specified, secretId and secretKey should be set
                      accordingly, see: https://cloud.tencent.com/document/product/598/13896
        """
        if secretId is None or secretId.strip() == "":
            raise TencentCloudSDKException("InvalidCredential", "secret id should not be none or empty")
        if secretId.strip() != secretId:
            raise TencentCloudSDKException("InvalidCredential", "secret id should not contain spaces")
        self.secretId = secretId

        if secretKey is None or secretKey.strip() == "":
            raise TencentCloudSDKException("InvalidCredential", "secret key should not be none or empty")
        if secretKey.strip() != secretKey:
            raise TencentCloudSDKException("InvalidCredential", "secret key should not contain spaces")
        self.secretKey = secretKey

        self.token = token


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
