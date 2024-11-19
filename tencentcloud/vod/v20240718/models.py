# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class CreateStorageCredentialsRequest(AbstractModel):
    """CreateStorageCredentials请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubAppId: <b>点播专业版[应用](/document/product/266/14574) ID。</b>
        :type SubAppId: int
        :param _Policy: 按照下方语法组装好策略后，先序列化为字符串，再做 URL Encode，结果作为 Policy 字段入参。服务端会对该字段做 URL Decode，并按解析后的策略授予临时访问凭证权限，请按规范传入参数。
注意： 
1.策略语法参照[访问管理策略](/document/product/598/10603)。
2.策略中不能包含 principal 元素。
3.策略的 action 元素仅支持：<li>name/vod:PutObject;</li><li>name/vod:ListParts;</li><li>name/vod:PostObject;</li><li>name/vod:InitiateMultipartUpload;</li><li>name/vod:UploadPart;</li><li>name/vod:CompleteMultipartUpload;</li><li>name/vod:AbortMultipartUpload;</li><li>name/vod:ListMultipartUploads;</li>4.策略的 resource 元素填写格式为：`qcs::vod:[存储地域]:uid/[账号AppID]:prefix//[点播应用ID]/[存储桶ID]/[存储路径]`，其中存储地域、账号 AppID、点播应用 ID、存储桶 ID 和存储路径要按需填写，其他内容不允许改动，例：`qcs:ap-chongqing:vod::uid/1231456789:prefix//1234567890/2ceds3ew323w3mu/file_path`。

        :type Policy: str
        :param _DurationSeconds: 指定临时证书的有效期，单位：秒。
默认 1800 秒，最大 129600 秒。
        :type DurationSeconds: int
        """
        self._SubAppId = None
        self._Policy = None
        self._DurationSeconds = None

    @property
    def SubAppId(self):
        """<b>点播专业版[应用](/document/product/266/14574) ID。</b>
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def Policy(self):
        """按照下方语法组装好策略后，先序列化为字符串，再做 URL Encode，结果作为 Policy 字段入参。服务端会对该字段做 URL Decode，并按解析后的策略授予临时访问凭证权限，请按规范传入参数。
注意： 
1.策略语法参照[访问管理策略](/document/product/598/10603)。
2.策略中不能包含 principal 元素。
3.策略的 action 元素仅支持：<li>name/vod:PutObject;</li><li>name/vod:ListParts;</li><li>name/vod:PostObject;</li><li>name/vod:InitiateMultipartUpload;</li><li>name/vod:UploadPart;</li><li>name/vod:CompleteMultipartUpload;</li><li>name/vod:AbortMultipartUpload;</li><li>name/vod:ListMultipartUploads;</li>4.策略的 resource 元素填写格式为：`qcs::vod:[存储地域]:uid/[账号AppID]:prefix//[点播应用ID]/[存储桶ID]/[存储路径]`，其中存储地域、账号 AppID、点播应用 ID、存储桶 ID 和存储路径要按需填写，其他内容不允许改动，例：`qcs:ap-chongqing:vod::uid/1231456789:prefix//1234567890/2ceds3ew323w3mu/file_path`。

        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def DurationSeconds(self):
        """指定临时证书的有效期，单位：秒。
默认 1800 秒，最大 129600 秒。
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds


    def _deserialize(self, params):
        self._SubAppId = params.get("SubAppId")
        self._Policy = params.get("Policy")
        self._DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStorageCredentialsResponse(AbstractModel):
    """CreateStorageCredentials返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Credentials: 临时访问凭证。
        :type Credentials: :class:`tencentcloud.vod.v20240718.models.Credentials`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Credentials = None
        self._RequestId = None

    @property
    def Credentials(self):
        """临时访问凭证。
        :rtype: :class:`tencentcloud.vod.v20240718.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """临时访问凭证。

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 访问凭证 ID。
        :type AccessKeyId: str
        :param _SecretAccessKey: 访问凭证 Key。
        :type SecretAccessKey: str
        :param _SessionToken: 访问凭证 Token，长度和绑定的策略有关，最长不超过 4096 字节。
        :type SessionToken: str
        :param _Expiration: 访问凭证的过期时间。
        :type Expiration: str
        """
        self._AccessKeyId = None
        self._SecretAccessKey = None
        self._SessionToken = None
        self._Expiration = None

    @property
    def AccessKeyId(self):
        """访问凭证 ID。
        :rtype: str
        """
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def SecretAccessKey(self):
        """访问凭证 Key。
        :rtype: str
        """
        return self._SecretAccessKey

    @SecretAccessKey.setter
    def SecretAccessKey(self, SecretAccessKey):
        self._SecretAccessKey = SecretAccessKey

    @property
    def SessionToken(self):
        """访问凭证 Token，长度和绑定的策略有关，最长不超过 4096 字节。
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def Expiration(self):
        """访问凭证的过期时间。
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._SecretAccessKey = params.get("SecretAccessKey")
        self._SessionToken = params.get("SessionToken")
        self._Expiration = params.get("Expiration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        