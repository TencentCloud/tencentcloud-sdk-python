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


class CreateIAPUserOIDCConfigRequest(AbstractModel):
    """CreateIAPUserOIDCConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: 身份提供商URL。OpenID Connect身份提供商标识。对应企业IdP提供的Openid-configuration中"issuer"字段的值。
        :type IdentityUrl: str
        :param _ClientId: 客户端ID，在OpenID Connect身份提供商注册的客户端ID。
        :type ClientId: str
        :param _AuthorizationEndpoint: 授权请求Endpoint，OpenID Connect身份提供商授权地址。对应企业IdP提供的Openid-configuration中"authorization_endpoint"字段的值。
        :type AuthorizationEndpoint: str
        :param _ResponseType: 授权请求Response type，固定值id_token
        :type ResponseType: str
        :param _ResponseMode: 授权请求Response mode。授权请求返回模式，form_post和fragment两种可选模式，推荐选择form_post模式。
        :type ResponseMode: str
        :param _MappingFiled: 映射字段名称。IdP的id_token中哪一个字段映射到子用户的用户名，通常是sub或者name字段
        :type MappingFiled: str
        :param _IdentityKey: 签名公钥，需要base64_encode。验证OpenID Connect身份提供商ID Token签名的公钥。为了您的账号安全，建议您定期轮换签名公钥。
        :type IdentityKey: str
        :param _Scope: 授权请求Scope。openid; email;profile。授权请求信息范围。默认必选openid。
        :type Scope: list of str
        :param _Description: 描述
        :type Description: str
        """
        self._IdentityUrl = None
        self._ClientId = None
        self._AuthorizationEndpoint = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._IdentityKey = None
        self._Scope = None
        self._Description = None

    @property
    def IdentityUrl(self):
        """身份提供商URL。OpenID Connect身份提供商标识。对应企业IdP提供的Openid-configuration中"issuer"字段的值。
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def ClientId(self):
        """客户端ID，在OpenID Connect身份提供商注册的客户端ID。
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def AuthorizationEndpoint(self):
        """授权请求Endpoint，OpenID Connect身份提供商授权地址。对应企业IdP提供的Openid-configuration中"authorization_endpoint"字段的值。
        :rtype: str
        """
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def ResponseType(self):
        """授权请求Response type，固定值id_token
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        """授权请求Response mode。授权请求返回模式，form_post和fragment两种可选模式，推荐选择form_post模式。
        :rtype: str
        """
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        """映射字段名称。IdP的id_token中哪一个字段映射到子用户的用户名，通常是sub或者name字段
        :rtype: str
        """
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def IdentityKey(self):
        """签名公钥，需要base64_encode。验证OpenID Connect身份提供商ID Token签名的公钥。为了您的账号安全，建议您定期轮换签名公钥。
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def Scope(self):
        """授权请求Scope。openid; email;profile。授权请求信息范围。默认必选openid。
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._ClientId = params.get("ClientId")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._IdentityKey = params.get("IdentityKey")
        self._Scope = params.get("Scope")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIAPUserOIDCConfigResponse(AbstractModel):
    """CreateIAPUserOIDCConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeIAPLoginSessionDurationRequest(AbstractModel):
    """DescribeIAPLoginSessionDuration请求参数结构体

    """


class DescribeIAPLoginSessionDurationResponse(AbstractModel):
    """DescribeIAPLoginSessionDuration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Duration: 登录会话时长
        :type Duration: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Duration = None
        self._RequestId = None

    @property
    def Duration(self):
        """登录会话时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

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
        self._Duration = params.get("Duration")
        self._RequestId = params.get("RequestId")


class DescribeIAPUserOIDCConfigRequest(AbstractModel):
    """DescribeIAPUserOIDCConfig请求参数结构体

    """


class DescribeIAPUserOIDCConfigResponse(AbstractModel):
    """DescribeIAPUserOIDCConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProviderType: 身份提供商类型。 13：IAP用户OIDC身份提供商
        :type ProviderType: int
        :param _IdentityUrl: 身份提供商URL
        :type IdentityUrl: str
        :param _IdentityKey: 签名公钥
        :type IdentityKey: str
        :param _ClientId: 客户端id
        :type ClientId: str
        :param _Status: 状态：0:未设置，11:已开启，2:已禁用
        :type Status: int
        :param _Fingerprints: HTTPS CA证书的验证指纹，允许英文字母和数字，每个指纹长度为40个字符，最多5个指纹。
        :type Fingerprints: list of str
        :param _EnableAutoPublicKey: 是否需要开启自动使用OIDC签名公钥，1:需要，2:不需要，默认不需要
        :type EnableAutoPublicKey: int
        :param _AuthorizationEndpoint: 授权请求Endpoint
        :type AuthorizationEndpoint: str
        :param _Scope: 授权请求Scope
        :type Scope: list of str
        :param _ResponseType: 授权请求Response type
        :type ResponseType: str
        :param _ResponseMode: 授权请求Response mode
        :type ResponseMode: str
        :param _MappingFiled: 映射字段名称
        :type MappingFiled: str
        :param _Description: 描述
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProviderType = None
        self._IdentityUrl = None
        self._IdentityKey = None
        self._ClientId = None
        self._Status = None
        self._Fingerprints = None
        self._EnableAutoPublicKey = None
        self._AuthorizationEndpoint = None
        self._Scope = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._Description = None
        self._RequestId = None

    @property
    def ProviderType(self):
        """身份提供商类型。 13：IAP用户OIDC身份提供商
        :rtype: int
        """
        return self._ProviderType

    @ProviderType.setter
    def ProviderType(self, ProviderType):
        self._ProviderType = ProviderType

    @property
    def IdentityUrl(self):
        """身份提供商URL
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def IdentityKey(self):
        """签名公钥
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def ClientId(self):
        """客户端id
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Status(self):
        """状态：0:未设置，11:已开启，2:已禁用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Fingerprints(self):
        """HTTPS CA证书的验证指纹，允许英文字母和数字，每个指纹长度为40个字符，最多5个指纹。
        :rtype: list of str
        """
        return self._Fingerprints

    @Fingerprints.setter
    def Fingerprints(self, Fingerprints):
        self._Fingerprints = Fingerprints

    @property
    def EnableAutoPublicKey(self):
        """是否需要开启自动使用OIDC签名公钥，1:需要，2:不需要，默认不需要
        :rtype: int
        """
        return self._EnableAutoPublicKey

    @EnableAutoPublicKey.setter
    def EnableAutoPublicKey(self, EnableAutoPublicKey):
        self._EnableAutoPublicKey = EnableAutoPublicKey

    @property
    def AuthorizationEndpoint(self):
        """授权请求Endpoint
        :rtype: str
        """
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def Scope(self):
        """授权请求Scope
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ResponseType(self):
        """授权请求Response type
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        """授权请求Response mode
        :rtype: str
        """
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        """映射字段名称
        :rtype: str
        """
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
        self._ProviderType = params.get("ProviderType")
        self._IdentityUrl = params.get("IdentityUrl")
        self._IdentityKey = params.get("IdentityKey")
        self._ClientId = params.get("ClientId")
        self._Status = params.get("Status")
        self._Fingerprints = params.get("Fingerprints")
        self._EnableAutoPublicKey = params.get("EnableAutoPublicKey")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._Scope = params.get("Scope")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DisableIAPUserSSORequest(AbstractModel):
    """DisableIAPUserSSO请求参数结构体

    """


class DisableIAPUserSSOResponse(AbstractModel):
    """DisableIAPUserSSO返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyIAPLoginSessionDurationRequest(AbstractModel):
    """ModifyIAPLoginSessionDuration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Duration: 登录会话时长
        :type Duration: int
        """
        self._Duration = None

    @property
    def Duration(self):
        """登录会话时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIAPLoginSessionDurationResponse(AbstractModel):
    """ModifyIAPLoginSessionDuration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateIAPUserOIDCConfigRequest(AbstractModel):
    """UpdateIAPUserOIDCConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: 身份提供商URL。OpenID Connect身份提供商标识。对应企业IdP提供的Openid-configuration中"issuer"字段的值。
        :type IdentityUrl: str
        :param _ClientId: 客户端ID，在OpenID Connect身份提供商注册的客户端ID。
        :type ClientId: str
        :param _AuthorizationEndpoint: 授权请求Endpoint，OpenID Connect身份提供商授权地址。对应企业IdP提供的Openid-configuration中"authorization_endpoint"字段的值。
        :type AuthorizationEndpoint: str
        :param _ResponseType: 授权请求Response type，固定值id_token
        :type ResponseType: str
        :param _ResponseMode: 授权请求Response mode。授权请求返回模式，form_post和fragment两种可选模式，推荐选择form_post模式。
        :type ResponseMode: str
        :param _MappingFiled: 映射字段名称。IdP的id_token中哪一个字段映射到子用户的用户名，通常是sub或者name字段
        :type MappingFiled: str
        :param _IdentityKey: RSA签名公钥，JWKS格式，需要进行base64_encode。验证OpenID Connect身份提供商ID Token签名的公钥。为了您的账号安全，建议您定期轮换签名公钥。
        :type IdentityKey: str
        :param _Scope: 授权请求Scope。openid; email;profile。授权请求信息范围。默认必选openid。
        :type Scope: list of str
        :param _Description: 描述，长度为1~255个英文或中文字符，默认值为空。
        :type Description: str
        """
        self._IdentityUrl = None
        self._ClientId = None
        self._AuthorizationEndpoint = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._IdentityKey = None
        self._Scope = None
        self._Description = None

    @property
    def IdentityUrl(self):
        """身份提供商URL。OpenID Connect身份提供商标识。对应企业IdP提供的Openid-configuration中"issuer"字段的值。
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def ClientId(self):
        """客户端ID，在OpenID Connect身份提供商注册的客户端ID。
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def AuthorizationEndpoint(self):
        """授权请求Endpoint，OpenID Connect身份提供商授权地址。对应企业IdP提供的Openid-configuration中"authorization_endpoint"字段的值。
        :rtype: str
        """
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def ResponseType(self):
        """授权请求Response type，固定值id_token
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        """授权请求Response mode。授权请求返回模式，form_post和fragment两种可选模式，推荐选择form_post模式。
        :rtype: str
        """
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        """映射字段名称。IdP的id_token中哪一个字段映射到子用户的用户名，通常是sub或者name字段
        :rtype: str
        """
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def IdentityKey(self):
        """RSA签名公钥，JWKS格式，需要进行base64_encode。验证OpenID Connect身份提供商ID Token签名的公钥。为了您的账号安全，建议您定期轮换签名公钥。
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def Scope(self):
        """授权请求Scope。openid; email;profile。授权请求信息范围。默认必选openid。
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Description(self):
        """描述，长度为1~255个英文或中文字符，默认值为空。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._ClientId = params.get("ClientId")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._IdentityKey = params.get("IdentityKey")
        self._Scope = params.get("Scope")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateIAPUserOIDCConfigResponse(AbstractModel):
    """UpdateIAPUserOIDCConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")