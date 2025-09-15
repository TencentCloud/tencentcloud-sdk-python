# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class ApiKey(AbstractModel):
    r"""API密钥数据列表

    """

    def __init__(self):
        r"""
        :param _SecretId: 密钥ID
        :type SecretId: str
        :param _CreateTime: 创建时间(时间戳)
        :type CreateTime: int
        :param _Status: 状态(2:有效, 3:禁用, 4:已删除)
        :type Status: int
        """
        self._SecretId = None
        self._CreateTime = None
        self._Status = None

    @property
    def SecretId(self):
        r"""密钥ID
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def CreateTime(self):
        r"""创建时间(时间戳)
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        r"""状态(2:有效, 3:禁用, 4:已删除)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._SecretId = params.get("SecretId")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleRequest(AbstractModel):
    r"""AssumeRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleArn: 角色的资源描述，可在[访问管理](https://console.cloud.tencent.com/cam/role)，点击角色名获取。
普通角色：
qcs::cam::uin/12345678:role/4611686018427397919、qcs::cam::uin/12345678:roleName/testRoleName
服务角色：
qcs::cam::uin/12345678:role/tencentcloudServiceRole/4611686018427397920、qcs::cam::uin/12345678:role/tencentcloudServiceRoleName/testServiceRoleName
        :type RoleArn: str
        :param _RoleSessionName: 临时会话名称，由用户自定义名称。
长度在2到128之间，可包含大小写字符，数字以及特殊字符：=,.@_-。 正则为：[\w+=,.@_-]*
        :type RoleSessionName: str
        :param _DurationSeconds: 指定临时访问凭证的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 43200 秒
        :type DurationSeconds: int
        :param _Policy: 策略描述
注意：
1、该参数需要做urlencode，服务端会对该字段做urldecode， 并按处理后Policy授予临时访问凭证权限，请按规范传入参数。（如果通过 GET 方法请求云 API，发送请求前，所有参数都需要按照[云 API 规范](https://cloud.tencent.com/document/api/598/33159#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2)再 urlencode 一次）。
2、策略语法参照[ CAM 策略语法](https://cloud.tencent.com/document/product/598/10603)。
3、策略中不能包含 principal 元素。
        :type Policy: str
        :param _ExternalId: 角色外部ID，可在[访问管理](https://console.cloud.tencent.com/cam/role)，点击角色名获取。
长度在2到128之间，可包含大小写字符，数字以及特殊字符：=,.@:/-。 正则为：[\w+=,.@:\/-]*
        :type ExternalId: str
        :param _Tags: 会话标签列表。最多可以传递 50 个会话标签，不支持包含相同标签键。
        :type Tags: list of Tag
        :param _SourceIdentity: 调用者身份uin
        :type SourceIdentity: str
        :param _SerialNumber: MFA序列号，与进行调用的CAM用户关联的MFA设备的标识号。格式qcs::cam:uin/${ownerUin}::mfa/${mfaType}。mfaType支持softToken（软token）
        :type SerialNumber: str
        :param _TokenCode: mfa身份验证码。
        :type TokenCode: str
        """
        self._RoleArn = None
        self._RoleSessionName = None
        self._DurationSeconds = None
        self._Policy = None
        self._ExternalId = None
        self._Tags = None
        self._SourceIdentity = None
        self._SerialNumber = None
        self._TokenCode = None

    @property
    def RoleArn(self):
        r"""角色的资源描述，可在[访问管理](https://console.cloud.tencent.com/cam/role)，点击角色名获取。
普通角色：
qcs::cam::uin/12345678:role/4611686018427397919、qcs::cam::uin/12345678:roleName/testRoleName
服务角色：
qcs::cam::uin/12345678:role/tencentcloudServiceRole/4611686018427397920、qcs::cam::uin/12345678:role/tencentcloudServiceRoleName/testServiceRoleName
        :rtype: str
        """
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def RoleSessionName(self):
        r"""临时会话名称，由用户自定义名称。
长度在2到128之间，可包含大小写字符，数字以及特殊字符：=,.@_-。 正则为：[\w+=,.@_-]*
        :rtype: str
        """
        return self._RoleSessionName

    @RoleSessionName.setter
    def RoleSessionName(self, RoleSessionName):
        self._RoleSessionName = RoleSessionName

    @property
    def DurationSeconds(self):
        r"""指定临时访问凭证的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 43200 秒
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds

    @property
    def Policy(self):
        r"""策略描述
注意：
1、该参数需要做urlencode，服务端会对该字段做urldecode， 并按处理后Policy授予临时访问凭证权限，请按规范传入参数。（如果通过 GET 方法请求云 API，发送请求前，所有参数都需要按照[云 API 规范](https://cloud.tencent.com/document/api/598/33159#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2)再 urlencode 一次）。
2、策略语法参照[ CAM 策略语法](https://cloud.tencent.com/document/product/598/10603)。
3、策略中不能包含 principal 元素。
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def ExternalId(self):
        r"""角色外部ID，可在[访问管理](https://console.cloud.tencent.com/cam/role)，点击角色名获取。
长度在2到128之间，可包含大小写字符，数字以及特殊字符：=,.@:/-。 正则为：[\w+=,.@:\/-]*
        :rtype: str
        """
        return self._ExternalId

    @ExternalId.setter
    def ExternalId(self, ExternalId):
        self._ExternalId = ExternalId

    @property
    def Tags(self):
        r"""会话标签列表。最多可以传递 50 个会话标签，不支持包含相同标签键。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SourceIdentity(self):
        r"""调用者身份uin
        :rtype: str
        """
        return self._SourceIdentity

    @SourceIdentity.setter
    def SourceIdentity(self, SourceIdentity):
        self._SourceIdentity = SourceIdentity

    @property
    def SerialNumber(self):
        r"""MFA序列号，与进行调用的CAM用户关联的MFA设备的标识号。格式qcs::cam:uin/${ownerUin}::mfa/${mfaType}。mfaType支持softToken（软token）
        :rtype: str
        """
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def TokenCode(self):
        r"""mfa身份验证码。
        :rtype: str
        """
        return self._TokenCode

    @TokenCode.setter
    def TokenCode(self, TokenCode):
        self._TokenCode = TokenCode


    def _deserialize(self, params):
        self._RoleArn = params.get("RoleArn")
        self._RoleSessionName = params.get("RoleSessionName")
        self._DurationSeconds = params.get("DurationSeconds")
        self._Policy = params.get("Policy")
        self._ExternalId = params.get("ExternalId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SourceIdentity = params.get("SourceIdentity")
        self._SerialNumber = params.get("SerialNumber")
        self._TokenCode = params.get("TokenCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleResponse(AbstractModel):
    r"""AssumeRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Credentials: 临时访问凭证
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param _ExpiredTime: 临时访问凭证的过期时间，返回 Unix 时间戳，精确到秒
        :type ExpiredTime: int
        :param _Expiration: 临时访问凭证的过期时间，以 iso8601 格式的 UTC 时间表示
        :type Expiration: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Credentials = None
        self._ExpiredTime = None
        self._Expiration = None
        self._RequestId = None

    @property
    def Credentials(self):
        r"""临时访问凭证
        :rtype: :class:`tencentcloud.sts.v20180813.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def ExpiredTime(self):
        r"""临时访问凭证的过期时间，返回 Unix 时间戳，精确到秒
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        r"""临时访问凭证的过期时间，以 iso8601 格式的 UTC 时间表示
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        self._RequestId = params.get("RequestId")


class AssumeRoleWithSAMLRequest(AbstractModel):
    r"""AssumeRoleWithSAML请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SAMLAssertion: base64 编码的 SAML 断言信息
        :type SAMLAssertion: str
        :param _PrincipalArn: 扮演者访问描述名
        :type PrincipalArn: str
        :param _RoleArn: 角色访问描述名
        :type RoleArn: str
        :param _RoleSessionName: 会话名称
        :type RoleSessionName: str
        :param _DurationSeconds: 指定临时访问凭证的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 43200 秒
        :type DurationSeconds: int
        """
        self._SAMLAssertion = None
        self._PrincipalArn = None
        self._RoleArn = None
        self._RoleSessionName = None
        self._DurationSeconds = None

    @property
    def SAMLAssertion(self):
        r"""base64 编码的 SAML 断言信息
        :rtype: str
        """
        return self._SAMLAssertion

    @SAMLAssertion.setter
    def SAMLAssertion(self, SAMLAssertion):
        self._SAMLAssertion = SAMLAssertion

    @property
    def PrincipalArn(self):
        r"""扮演者访问描述名
        :rtype: str
        """
        return self._PrincipalArn

    @PrincipalArn.setter
    def PrincipalArn(self, PrincipalArn):
        self._PrincipalArn = PrincipalArn

    @property
    def RoleArn(self):
        r"""角色访问描述名
        :rtype: str
        """
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def RoleSessionName(self):
        r"""会话名称
        :rtype: str
        """
        return self._RoleSessionName

    @RoleSessionName.setter
    def RoleSessionName(self, RoleSessionName):
        self._RoleSessionName = RoleSessionName

    @property
    def DurationSeconds(self):
        r"""指定临时访问凭证的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 43200 秒
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds


    def _deserialize(self, params):
        self._SAMLAssertion = params.get("SAMLAssertion")
        self._PrincipalArn = params.get("PrincipalArn")
        self._RoleArn = params.get("RoleArn")
        self._RoleSessionName = params.get("RoleSessionName")
        self._DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleWithSAMLResponse(AbstractModel):
    r"""AssumeRoleWithSAML返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Credentials: 对象里面包含 Token，TmpSecretId，TmpSecretKey 三元组
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param _ExpiredTime: 临时访问凭证的过期时间，返回 Unix 时间戳，精确到秒
        :type ExpiredTime: int
        :param _Expiration: 临时访问凭证的过期时间，以 ISO8601 格式的 UTC 时间表示
        :type Expiration: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Credentials = None
        self._ExpiredTime = None
        self._Expiration = None
        self._RequestId = None

    @property
    def Credentials(self):
        r"""对象里面包含 Token，TmpSecretId，TmpSecretKey 三元组
        :rtype: :class:`tencentcloud.sts.v20180813.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def ExpiredTime(self):
        r"""临时访问凭证的过期时间，返回 Unix 时间戳，精确到秒
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        r"""临时访问凭证的过期时间，以 ISO8601 格式的 UTC 时间表示
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        self._RequestId = params.get("RequestId")


class AssumeRoleWithWebIdentityRequest(AbstractModel):
    r"""AssumeRoleWithWebIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProviderId: 身份提供商名称
        :type ProviderId: str
        :param _WebIdentityToken: IdP签发的OIDC令牌
        :type WebIdentityToken: str
        :param _RoleArn: 角色访问描述名
        :type RoleArn: str
        :param _RoleSessionName: 会话名称
        :type RoleSessionName: str
        :param _DurationSeconds: 指定临时访问凭证的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 43200 秒
        :type DurationSeconds: int
        """
        self._ProviderId = None
        self._WebIdentityToken = None
        self._RoleArn = None
        self._RoleSessionName = None
        self._DurationSeconds = None

    @property
    def ProviderId(self):
        r"""身份提供商名称
        :rtype: str
        """
        return self._ProviderId

    @ProviderId.setter
    def ProviderId(self, ProviderId):
        self._ProviderId = ProviderId

    @property
    def WebIdentityToken(self):
        r"""IdP签发的OIDC令牌
        :rtype: str
        """
        return self._WebIdentityToken

    @WebIdentityToken.setter
    def WebIdentityToken(self, WebIdentityToken):
        self._WebIdentityToken = WebIdentityToken

    @property
    def RoleArn(self):
        r"""角色访问描述名
        :rtype: str
        """
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def RoleSessionName(self):
        r"""会话名称
        :rtype: str
        """
        return self._RoleSessionName

    @RoleSessionName.setter
    def RoleSessionName(self, RoleSessionName):
        self._RoleSessionName = RoleSessionName

    @property
    def DurationSeconds(self):
        r"""指定临时访问凭证的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 43200 秒
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds


    def _deserialize(self, params):
        self._ProviderId = params.get("ProviderId")
        self._WebIdentityToken = params.get("WebIdentityToken")
        self._RoleArn = params.get("RoleArn")
        self._RoleSessionName = params.get("RoleSessionName")
        self._DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleWithWebIdentityResponse(AbstractModel):
    r"""AssumeRoleWithWebIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExpiredTime: 临时访问凭证过期时间(时间戳)
        :type ExpiredTime: int
        :param _Expiration: 临时访问凭证过期时间
        :type Expiration: str
        :param _Credentials: 临时访问凭证
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExpiredTime = None
        self._Expiration = None
        self._Credentials = None
        self._RequestId = None

    @property
    def ExpiredTime(self):
        r"""临时访问凭证过期时间(时间戳)
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        r"""临时访问凭证过期时间
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Credentials(self):
        r"""临时访问凭证
        :rtype: :class:`tencentcloud.sts.v20180813.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    r"""临时证书

    """

    def __init__(self):
        r"""
        :param _Token: token。token长度和绑定的策略有关，最长不超过4096字节。
        :type Token: str
        :param _TmpSecretId: 临时证书密钥ID。最长不超过1024字节。
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时证书密钥Key。最长不超过1024字节。
        :type TmpSecretKey: str
        """
        self._Token = None
        self._TmpSecretId = None
        self._TmpSecretKey = None

    @property
    def Token(self):
        r"""token。token长度和绑定的策略有关，最长不超过4096字节。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def TmpSecretId(self):
        r"""临时证书密钥ID。最长不超过1024字节。
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        r"""临时证书密钥Key。最长不超过1024字节。
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCallerIdentityRequest(AbstractModel):
    r"""GetCallerIdentity请求参数结构体

    """


class GetCallerIdentityResponse(AbstractModel):
    r"""GetCallerIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Arn: 当前调用者ARN。
        :type Arn: str
        :param _AccountId: 当前调用者所属主账号Uin。
        :type AccountId: str
        :param _UserId: 身份标识。
1. 调用者是云账号时，返回的是当前账号Uin
2. 调用者是角色时，返回的是roleId:roleSessionName
3. 调用者是联合身份时，返回的是uin:federatedUserName
        :type UserId: str
        :param _PrincipalId: 密钥所属账号Uin。
1. 调用者是云账号，返回的当前账号Uin
2, 调用者是角色，返回的申请角色密钥的账号Uin
        :type PrincipalId: str
        :param _Type: 身份类型。
        :type Type: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Arn = None
        self._AccountId = None
        self._UserId = None
        self._PrincipalId = None
        self._Type = None
        self._RequestId = None

    @property
    def Arn(self):
        r"""当前调用者ARN。
        :rtype: str
        """
        return self._Arn

    @Arn.setter
    def Arn(self, Arn):
        self._Arn = Arn

    @property
    def AccountId(self):
        r"""当前调用者所属主账号Uin。
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def UserId(self):
        r"""身份标识。
1. 调用者是云账号时，返回的是当前账号Uin
2. 调用者是角色时，返回的是roleId:roleSessionName
3. 调用者是联合身份时，返回的是uin:federatedUserName
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PrincipalId(self):
        r"""密钥所属账号Uin。
1. 调用者是云账号，返回的当前账号Uin
2, 调用者是角色，返回的申请角色密钥的账号Uin
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def Type(self):
        r"""身份类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Arn = params.get("Arn")
        self._AccountId = params.get("AccountId")
        self._UserId = params.get("UserId")
        self._PrincipalId = params.get("PrincipalId")
        self._Type = params.get("Type")
        self._RequestId = params.get("RequestId")


class GetFederationTokenRequest(AbstractModel):
    r"""GetFederationToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 您可以自定义调用方英文名称，由字母组成。
        :type Name: str
        :param _Policy: 注意：
1、策略语法参照[ CAM 策略语法](https://cloud.tencent.com/document/product/598/10603)。
2、策略中不能包含 principal 元素。
3、该参数需要做urlencode，服务端会对该字段做urldecode， 并按处理后Policy授予临时访问凭证权限，请按规范传入参数。
        :type Policy: str
        :param _DurationSeconds: 指定临时证书的有效期，单位：秒，默认1800秒，主账号最长可设定有效期为7200秒，子账号最长可设定有效期为129600秒。
        :type DurationSeconds: int
        """
        self._Name = None
        self._Policy = None
        self._DurationSeconds = None

    @property
    def Name(self):
        r"""您可以自定义调用方英文名称，由字母组成。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Policy(self):
        r"""注意：
1、策略语法参照[ CAM 策略语法](https://cloud.tencent.com/document/product/598/10603)。
2、策略中不能包含 principal 元素。
3、该参数需要做urlencode，服务端会对该字段做urldecode， 并按处理后Policy授予临时访问凭证权限，请按规范传入参数。
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def DurationSeconds(self):
        r"""指定临时证书的有效期，单位：秒，默认1800秒，主账号最长可设定有效期为7200秒，子账号最长可设定有效期为129600秒。
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Policy = params.get("Policy")
        self._DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFederationTokenResponse(AbstractModel):
    r"""GetFederationToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Credentials: 临时访问凭证
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param _ExpiredTime: 临时访问凭证有效的时间，返回 Unix 时间戳，精确到秒
        :type ExpiredTime: int
        :param _Expiration: 临时访问凭证有效的时间，以 iso8601 格式的 UTC 时间表示
注意：此字段可能返回 null，表示取不到有效值。
        :type Expiration: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Credentials = None
        self._ExpiredTime = None
        self._Expiration = None
        self._RequestId = None

    @property
    def Credentials(self):
        r"""临时访问凭证
        :rtype: :class:`tencentcloud.sts.v20180813.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def ExpiredTime(self):
        r"""临时访问凭证有效的时间，返回 Unix 时间戳，精确到秒
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        r"""临时访问凭证有效的时间，以 iso8601 格式的 UTC 时间表示
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        self._RequestId = params.get("RequestId")


class GetSessionTokenRequest(AbstractModel):
    r"""GetSessionToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SerialNumber: MFA序列号，与进行调用的CAM用户关联的MFA设备的标识号。格式qcs::cam:uin/${ownerUin}::mfa/${mfaType}。mfaType支持softToken（软token）
        :type SerialNumber: str
        :param _TokenCode: mfa身份验证码。
        :type TokenCode: str
        :param _DurationSeconds: 指定临时证书的有效期，单位：秒，默认1800秒，主账号最长可设定有效期为7200秒，子账号最长可设定有效期为129600秒。
        :type DurationSeconds: int
        """
        self._SerialNumber = None
        self._TokenCode = None
        self._DurationSeconds = None

    @property
    def SerialNumber(self):
        r"""MFA序列号，与进行调用的CAM用户关联的MFA设备的标识号。格式qcs::cam:uin/${ownerUin}::mfa/${mfaType}。mfaType支持softToken（软token）
        :rtype: str
        """
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def TokenCode(self):
        r"""mfa身份验证码。
        :rtype: str
        """
        return self._TokenCode

    @TokenCode.setter
    def TokenCode(self, TokenCode):
        self._TokenCode = TokenCode

    @property
    def DurationSeconds(self):
        r"""指定临时证书的有效期，单位：秒，默认1800秒，主账号最长可设定有效期为7200秒，子账号最长可设定有效期为129600秒。
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds


    def _deserialize(self, params):
        self._SerialNumber = params.get("SerialNumber")
        self._TokenCode = params.get("TokenCode")
        self._DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSessionTokenResponse(AbstractModel):
    r"""GetSessionToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Credentials: 临时访问凭证
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param _ExpiredTime: 证书无效的时间，返回 Unix 时间戳，精确到秒
        :type ExpiredTime: int
        :param _Expiration: 临时访问凭证的过期时间，以 iso8601 格式的 UTC 时间表示
        :type Expiration: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Credentials = None
        self._ExpiredTime = None
        self._Expiration = None
        self._RequestId = None

    @property
    def Credentials(self):
        r"""临时访问凭证
        :rtype: :class:`tencentcloud.sts.v20180813.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def ExpiredTime(self):
        r"""证书无效的时间，返回 Unix 时间戳，精确到秒
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        r"""临时访问凭证的过期时间，以 iso8601 格式的 UTC 时间表示
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        self._RequestId = params.get("RequestId")


class QueryApiKeyRequest(AbstractModel):
    r"""QueryApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetUin: 待查询的账号uin(不填默认查当前账号uin)
        :type TargetUin: int
        """
        self._TargetUin = None

    @property
    def TargetUin(self):
        r"""待查询的账号uin(不填默认查当前账号uin)
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryApiKeyResponse(AbstractModel):
    r"""QueryApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdKeys: 密钥ID列表。
        :type IdKeys: list of ApiKey
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdKeys = None
        self._RequestId = None

    @property
    def IdKeys(self):
        r"""密钥ID列表。
        :rtype: list of ApiKey
        """
        return self._IdKeys

    @IdKeys.setter
    def IdKeys(self, IdKeys):
        self._IdKeys = IdKeys

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IdKeys") is not None:
            self._IdKeys = []
            for item in params.get("IdKeys"):
                obj = ApiKey()
                obj._deserialize(item)
                self._IdKeys.append(obj)
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    r"""标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签键，最长128个字符，区分大小写。
        :type Key: str
        :param _Value: 标签值，最长256个字符，区分大小写。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""标签键，最长128个字符，区分大小写。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值，最长256个字符，区分大小写。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        