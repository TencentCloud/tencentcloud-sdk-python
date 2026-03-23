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


class AgentAppMcpServerDTO(AbstractModel):
    r"""关联的mcp服务配置

    """

    def __init__(self):
        r"""
        :param _ID: mcp server id
        :type ID: str
        :param _NeedAuth: 是否需要鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type NeedAuth: bool
        :param _AgentCredentialID: 凭据代填的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentCredentialID: str
        :param _SSEResourceIdentifier: 应用为OAuth2认证时，sse模式请求mcp时的资源标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SSEResourceIdentifier: str
        :param _StreamableResourceIdentifier: 应用为OAuth2认证时，streamable模式请求mcp时的资源标识
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamableResourceIdentifier: str
        """
        self._ID = None
        self._NeedAuth = None
        self._AgentCredentialID = None
        self._SSEResourceIdentifier = None
        self._StreamableResourceIdentifier = None

    @property
    def ID(self):
        r"""mcp server id
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def NeedAuth(self):
        r"""是否需要鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._NeedAuth

    @NeedAuth.setter
    def NeedAuth(self, NeedAuth):
        self._NeedAuth = NeedAuth

    @property
    def AgentCredentialID(self):
        r"""凭据代填的ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentCredentialID

    @AgentCredentialID.setter
    def AgentCredentialID(self, AgentCredentialID):
        self._AgentCredentialID = AgentCredentialID

    @property
    def SSEResourceIdentifier(self):
        r"""应用为OAuth2认证时，sse模式请求mcp时的资源标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SSEResourceIdentifier

    @SSEResourceIdentifier.setter
    def SSEResourceIdentifier(self, SSEResourceIdentifier):
        self._SSEResourceIdentifier = SSEResourceIdentifier

    @property
    def StreamableResourceIdentifier(self):
        r"""应用为OAuth2认证时，streamable模式请求mcp时的资源标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StreamableResourceIdentifier

    @StreamableResourceIdentifier.setter
    def StreamableResourceIdentifier(self, StreamableResourceIdentifier):
        self._StreamableResourceIdentifier = StreamableResourceIdentifier


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._NeedAuth = params.get("NeedAuth")
        self._AgentCredentialID = params.get("AgentCredentialID")
        self._SSEResourceIdentifier = params.get("SSEResourceIdentifier")
        self._StreamableResourceIdentifier = params.get("StreamableResourceIdentifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentAppMcpServerVO(AbstractModel):
    r"""应用关联的mcp响应

    """

    def __init__(self):
        r"""
        :param _ID: 绑定ID
        :type ID: str
        :param _NeedAuth: 需要认证
        :type NeedAuth: bool
        :param _AgentCredentialID: 凭据ID
        :type AgentCredentialID: str
        :param _AgentCredentialVO: 凭据详情
        :type AgentCredentialVO: :class:`tencentcloud.apis.v20240801.models.DescribeAgentCredentialResp`
        :param _McpServerVO: mcp详情
        :type McpServerVO: :class:`tencentcloud.apis.v20240801.models.DescribeMcpServerResponseVO`
        :param _RelateTime: 关联时间
        :type RelateTime: str
        :param _SSEResourceIdentifier: 应用为OAuth2认证时，sse模式请求mcp时的资源标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SSEResourceIdentifier: str
        :param _StreamableResourceIdentifier: 应用为OAuth2认证时，streamable模式请求mcp时的资源标识
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamableResourceIdentifier: str
        :param _AgentAppID: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentAppID: str
        :param _McpServerID: mcp ID
注意：此字段可能返回 null，表示取不到有效值。
        :type McpServerID: str
        """
        self._ID = None
        self._NeedAuth = None
        self._AgentCredentialID = None
        self._AgentCredentialVO = None
        self._McpServerVO = None
        self._RelateTime = None
        self._SSEResourceIdentifier = None
        self._StreamableResourceIdentifier = None
        self._AgentAppID = None
        self._McpServerID = None

    @property
    def ID(self):
        r"""绑定ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def NeedAuth(self):
        r"""需要认证
        :rtype: bool
        """
        return self._NeedAuth

    @NeedAuth.setter
    def NeedAuth(self, NeedAuth):
        self._NeedAuth = NeedAuth

    @property
    def AgentCredentialID(self):
        r"""凭据ID
        :rtype: str
        """
        return self._AgentCredentialID

    @AgentCredentialID.setter
    def AgentCredentialID(self, AgentCredentialID):
        self._AgentCredentialID = AgentCredentialID

    @property
    def AgentCredentialVO(self):
        r"""凭据详情
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentCredentialResp`
        """
        return self._AgentCredentialVO

    @AgentCredentialVO.setter
    def AgentCredentialVO(self, AgentCredentialVO):
        self._AgentCredentialVO = AgentCredentialVO

    @property
    def McpServerVO(self):
        r"""mcp详情
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeMcpServerResponseVO`
        """
        return self._McpServerVO

    @McpServerVO.setter
    def McpServerVO(self, McpServerVO):
        self._McpServerVO = McpServerVO

    @property
    def RelateTime(self):
        r"""关联时间
        :rtype: str
        """
        return self._RelateTime

    @RelateTime.setter
    def RelateTime(self, RelateTime):
        self._RelateTime = RelateTime

    @property
    def SSEResourceIdentifier(self):
        r"""应用为OAuth2认证时，sse模式请求mcp时的资源标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SSEResourceIdentifier

    @SSEResourceIdentifier.setter
    def SSEResourceIdentifier(self, SSEResourceIdentifier):
        self._SSEResourceIdentifier = SSEResourceIdentifier

    @property
    def StreamableResourceIdentifier(self):
        r"""应用为OAuth2认证时，streamable模式请求mcp时的资源标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StreamableResourceIdentifier

    @StreamableResourceIdentifier.setter
    def StreamableResourceIdentifier(self, StreamableResourceIdentifier):
        self._StreamableResourceIdentifier = StreamableResourceIdentifier

    @property
    def AgentAppID(self):
        r"""应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentAppID

    @AgentAppID.setter
    def AgentAppID(self, AgentAppID):
        self._AgentAppID = AgentAppID

    @property
    def McpServerID(self):
        r"""mcp ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._McpServerID

    @McpServerID.setter
    def McpServerID(self, McpServerID):
        self._McpServerID = McpServerID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._NeedAuth = params.get("NeedAuth")
        self._AgentCredentialID = params.get("AgentCredentialID")
        if params.get("AgentCredentialVO") is not None:
            self._AgentCredentialVO = DescribeAgentCredentialResp()
            self._AgentCredentialVO._deserialize(params.get("AgentCredentialVO"))
        if params.get("McpServerVO") is not None:
            self._McpServerVO = DescribeMcpServerResponseVO()
            self._McpServerVO._deserialize(params.get("McpServerVO"))
        self._RelateTime = params.get("RelateTime")
        self._SSEResourceIdentifier = params.get("SSEResourceIdentifier")
        self._StreamableResourceIdentifier = params.get("StreamableResourceIdentifier")
        self._AgentAppID = params.get("AgentAppID")
        self._McpServerID = params.get("McpServerID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentAppModelServiceDTO(AbstractModel):
    r"""应用绑定模型服务入参

    """

    def __init__(self):
        r"""
        :param _ID: 模型服务ID
        :type ID: str
        :param _InvokeLimitConfigStatus: 是否开启流量控制
        :type InvokeLimitConfigStatus: bool
        :param _InvokeLimitConfig: 流量控制
        :type InvokeLimitConfig: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        :param _TokenLimitStatus: 是否开启token控制
        :type TokenLimitStatus: bool
        :param _TokenLimitConfig: token控制
        :type TokenLimitConfig: :class:`tencentcloud.apis.v20240801.models.TokenLimitConfigDTO`
        """
        self._ID = None
        self._InvokeLimitConfigStatus = None
        self._InvokeLimitConfig = None
        self._TokenLimitStatus = None
        self._TokenLimitConfig = None

    @property
    def ID(self):
        r"""模型服务ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InvokeLimitConfigStatus(self):
        r"""是否开启流量控制
        :rtype: bool
        """
        return self._InvokeLimitConfigStatus

    @InvokeLimitConfigStatus.setter
    def InvokeLimitConfigStatus(self, InvokeLimitConfigStatus):
        self._InvokeLimitConfigStatus = InvokeLimitConfigStatus

    @property
    def InvokeLimitConfig(self):
        r"""流量控制
        :rtype: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        """
        return self._InvokeLimitConfig

    @InvokeLimitConfig.setter
    def InvokeLimitConfig(self, InvokeLimitConfig):
        self._InvokeLimitConfig = InvokeLimitConfig

    @property
    def TokenLimitStatus(self):
        r"""是否开启token控制
        :rtype: bool
        """
        return self._TokenLimitStatus

    @TokenLimitStatus.setter
    def TokenLimitStatus(self, TokenLimitStatus):
        self._TokenLimitStatus = TokenLimitStatus

    @property
    def TokenLimitConfig(self):
        r"""token控制
        :rtype: :class:`tencentcloud.apis.v20240801.models.TokenLimitConfigDTO`
        """
        return self._TokenLimitConfig

    @TokenLimitConfig.setter
    def TokenLimitConfig(self, TokenLimitConfig):
        self._TokenLimitConfig = TokenLimitConfig


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InvokeLimitConfigStatus = params.get("InvokeLimitConfigStatus")
        if params.get("InvokeLimitConfig") is not None:
            self._InvokeLimitConfig = InvokeLimitConfigDTO()
            self._InvokeLimitConfig._deserialize(params.get("InvokeLimitConfig"))
        self._TokenLimitStatus = params.get("TokenLimitStatus")
        if params.get("TokenLimitConfig") is not None:
            self._TokenLimitConfig = TokenLimitConfigDTO()
            self._TokenLimitConfig._deserialize(params.get("TokenLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentAppSecretKeyVO(AbstractModel):
    r"""secretKey的出参

    """

    def __init__(self):
        r"""
        :param _SecretID: secret id
        :type SecretID: str
        :param _SecretKey: secret key
        :type SecretKey: str
        """
        self._SecretID = None
        self._SecretKey = None

    @property
    def SecretID(self):
        r"""secret id
        :rtype: str
        """
        return self._SecretID

    @SecretID.setter
    def SecretID(self, SecretID):
        self._SecretID = SecretID

    @property
    def SecretKey(self):
        r"""secret key
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey


    def _deserialize(self, params):
        self._SecretID = params.get("SecretID")
        self._SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentCredentialContentDTO(AbstractModel):
    r"""凭证内容

    """

    def __init__(self):
        r"""
        :param _STSSystem: 如果认证类型为sts时，该项必填
        :type STSSystem: str
        :param _STSService: 如果认证类型为sts时，该项必填
        :type STSService: str
        :param _Headers: 如果认证类型为reqKey时，该项必填
        :type Headers: list of AgentCredentialContentHeaderDTO
        """
        self._STSSystem = None
        self._STSService = None
        self._Headers = None

    @property
    def STSSystem(self):
        r"""如果认证类型为sts时，该项必填
        :rtype: str
        """
        return self._STSSystem

    @STSSystem.setter
    def STSSystem(self, STSSystem):
        self._STSSystem = STSSystem

    @property
    def STSService(self):
        r"""如果认证类型为sts时，该项必填
        :rtype: str
        """
        return self._STSService

    @STSService.setter
    def STSService(self, STSService):
        self._STSService = STSService

    @property
    def Headers(self):
        r"""如果认证类型为reqKey时，该项必填
        :rtype: list of AgentCredentialContentHeaderDTO
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._STSSystem = params.get("STSSystem")
        self._STSService = params.get("STSService")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = AgentCredentialContentHeaderDTO()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentCredentialContentHeaderDTO(AbstractModel):
    r"""凭证内容头

    """

    def __init__(self):
        r"""
        :param _Key: 凭据header key
        :type Key: str
        :param _Value: 凭据header value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""凭据header key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""凭据header value
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
        


class BindMcpSecurityRuleDTO(AbstractModel):
    r"""BindMcpSecurityRuleDTO，替换之前的McpSecurityRule

    """

    def __init__(self):
        r"""
        :param _ID: 规则ID
        :type ID: str
        :param _Act: 处置动作
        :type Act: str
        """
        self._ID = None
        self._Act = None

    @property
    def ID(self):
        r"""规则ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Act(self):
        r"""处置动作
        :rtype: str
        """
        return self._Act

    @Act.setter
    def Act(self, Act):
        self._Act = Act


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Act = params.get("Act")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindMcpSecurityRuleVO(AbstractModel):
    r"""BindMcpSecurityRuleVO，重新定义了之前的McpSecurityRulesVO

    """

    def __init__(self):
        r"""
        :param _ID: 规则ID
        :type ID: str
        :param _Type: 规则类型
        :type Type: str
        :param _Name: 规则名称
        :type Name: str
        :param _Description: 规则描述
        :type Description: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: str
        :param _VersionNumber: 版本号
        :type VersionNumber: str
        :param _Act: 当前选择的处置动作
        :type Act: str
        :param _SupportActs: 支持的处置动作
        :type SupportActs: list of str
        :param _BodyType: 内容类型
        :type BodyType: str
        :param _IconType: icon类型
        :type IconType: str
        """
        self._ID = None
        self._Type = None
        self._Name = None
        self._Description = None
        self._RiskLevel = None
        self._VersionNumber = None
        self._Act = None
        self._SupportActs = None
        self._BodyType = None
        self._IconType = None

    @property
    def ID(self):
        r"""规则ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Type(self):
        r"""规则类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""规则名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def VersionNumber(self):
        r"""版本号
        :rtype: str
        """
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        self._VersionNumber = VersionNumber

    @property
    def Act(self):
        r"""当前选择的处置动作
        :rtype: str
        """
        return self._Act

    @Act.setter
    def Act(self, Act):
        self._Act = Act

    @property
    def SupportActs(self):
        r"""支持的处置动作
        :rtype: list of str
        """
        return self._SupportActs

    @SupportActs.setter
    def SupportActs(self, SupportActs):
        self._SupportActs = SupportActs

    @property
    def BodyType(self):
        r"""内容类型
        :rtype: str
        """
        return self._BodyType

    @BodyType.setter
    def BodyType(self, BodyType):
        self._BodyType = BodyType

    @property
    def IconType(self):
        r"""icon类型
        :rtype: str
        """
        return self._IconType

    @IconType.setter
    def IconType(self, IconType):
        self._IconType = IconType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._RiskLevel = params.get("RiskLevel")
        self._VersionNumber = params.get("VersionNumber")
        self._Act = params.get("Act")
        self._SupportActs = params.get("SupportActs")
        self._BodyType = params.get("BodyType")
        self._IconType = params.get("IconType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentAppMcpServersRequest(AbstractModel):
    r"""CreateAgentAppMcpServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 应用ID
        :type ID: str
        :param _McpServers: 关联的mcp server
        :type McpServers: list of AgentAppMcpServerDTO
        """
        self._InstanceID = None
        self._ID = None
        self._McpServers = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""应用ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def McpServers(self):
        r"""关联的mcp server
        :rtype: list of AgentAppMcpServerDTO
        """
        return self._McpServers

    @McpServers.setter
    def McpServers(self, McpServers):
        self._McpServers = McpServers


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        if params.get("McpServers") is not None:
            self._McpServers = []
            for item in params.get("McpServers"):
                obj = AgentAppMcpServerDTO()
                obj._deserialize(item)
                self._McpServers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentAppMcpServersResponse(AbstractModel):
    r"""CreateAgentAppMcpServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: app id
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""app id
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateAgentAppModelServicesRequest(AbstractModel):
    r"""CreateAgentAppModelServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 应用ID
        :type ID: str
        :param _ModelServices: 关联的model service
        :type ModelServices: list of AgentAppModelServiceDTO
        """
        self._InstanceID = None
        self._ID = None
        self._ModelServices = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""应用ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ModelServices(self):
        r"""关联的model service
        :rtype: list of AgentAppModelServiceDTO
        """
        return self._ModelServices

    @ModelServices.setter
    def ModelServices(self, ModelServices):
        self._ModelServices = ModelServices


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        if params.get("ModelServices") is not None:
            self._ModelServices = []
            for item in params.get("ModelServices"):
                obj = AgentAppModelServiceDTO()
                obj._deserialize(item)
                self._ModelServices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentAppModelServicesResponse(AbstractModel):
    r"""CreateAgentAppModelServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: app id
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""app id
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateAgentAppRequest(AbstractModel):
    r"""CreateAgentApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _Name: 名称
        :type Name: str
        :param _AuthType: 认证类型
        :type AuthType: str
        :param _OAuth2ResourceServerID: OAuth2资源服务器ID
        :type OAuth2ResourceServerID: str
        :param _Description: 描述
        :type Description: str
        """
        self._InstanceID = None
        self._Name = None
        self._AuthType = None
        self._OAuth2ResourceServerID = None
        self._Description = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AuthType(self):
        r"""认证类型
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def OAuth2ResourceServerID(self):
        r"""OAuth2资源服务器ID
        :rtype: str
        """
        return self._OAuth2ResourceServerID

    @OAuth2ResourceServerID.setter
    def OAuth2ResourceServerID(self, OAuth2ResourceServerID):
        self._OAuth2ResourceServerID = OAuth2ResourceServerID

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Name = params.get("Name")
        self._AuthType = params.get("AuthType")
        self._OAuth2ResourceServerID = params.get("OAuth2ResourceServerID")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentAppResp(AbstractModel):
    r"""创建Agent应用的返回值，根据创建的AuthType，返回ApiKey或者SecretKey

    """

    def __init__(self):
        r"""
        :param _ID: app id 
        :type ID: str
        :param _ApiKey: 如果authType为apiKey时，返回该字段
        :type ApiKey: str
        :param _SecretKey: 如果authType为secretKey时，返回该字段
        :type SecretKey: str
        :param _SecretID: 如果authType为secretKey时，返回该字段
        :type SecretID: str
        """
        self._ID = None
        self._ApiKey = None
        self._SecretKey = None
        self._SecretID = None

    @property
    def ID(self):
        r"""app id 
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ApiKey(self):
        r"""如果authType为apiKey时，返回该字段
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def SecretKey(self):
        r"""如果authType为secretKey时，返回该字段
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SecretID(self):
        r"""如果authType为secretKey时，返回该字段
        :rtype: str
        """
        return self._SecretID

    @SecretID.setter
    def SecretID(self, SecretID):
        self._SecretID = SecretID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._ApiKey = params.get("ApiKey")
        self._SecretKey = params.get("SecretKey")
        self._SecretID = params.get("SecretID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentAppResponse(AbstractModel):
    r"""CreateAgentApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: app id
        :type Data: :class:`tencentcloud.apis.v20240801.models.CreateAgentAppResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""app id
        :rtype: :class:`tencentcloud.apis.v20240801.models.CreateAgentAppResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CreateAgentAppResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateAgentCredentialRequest(AbstractModel):
    r"""CreateAgentCredential请求参数结构体

    """


class CreateAgentCredentialResponse(AbstractModel):
    r"""CreateAgentCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateMcpServerRequest(AbstractModel):
    r"""CreateMcpServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mode: 模式：proxy代理模式； wrap封装模式；
        :type Mode: str
        :param _McpVersion: 版本号：2024-11-05 2025-03-26
        :type McpVersion: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _Name: 名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _WrapServices: 封装服务列表
        :type WrapServices: list of str
        :param _TargetSelect: 负载方式，robin random consistentHash
        :type TargetSelect: str
        :param _TargetHosts: 目标服务器
        :type TargetHosts: list of TargetHostDTO
        :param _HttpProtocolType: 后端协议：http https
        :type HttpProtocolType: str
        :param _CheckTargetCertsError: 证书检查
        :type CheckTargetCertsError: bool
        :param _TargetPath: 目标路径
        :type TargetPath: str
        :param _InvokeLimitConfigStatus: 流量控制开启状态
        :type InvokeLimitConfigStatus: bool
        :param _InvokeLimitConfig: 流量控制配置
        :type InvokeLimitConfig: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        :param _IpWhiteStatus: IP白名单开启状态
        :type IpWhiteStatus: bool
        :param _IpWhiteConfig: IP白名单配置
        :type IpWhiteConfig: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        :param _IpBlackStatus: IP黑名单开启状态
        :type IpBlackStatus: bool
        :param _IpBlackConfig: IP黑名单配置
        :type IpBlackConfig: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        :param _CustomHttpHost: 自定义host
        :type CustomHttpHost: str
        :param _HttpHostType: Http 请求host类型：useRequestHost 保持源请求；host targetHost 修正为源站host；  customHost 自定义host
        :type HttpHostType: str
        :param _Timeout: 请求的超时时间
        :type Timeout: int
        :param _McpSecurityRules: 安全规则集
        :type McpSecurityRules: list of McpSecurityRule
        :param _ToolConfigs: 工具集配置（openapi时或许用的是）
        :type ToolConfigs: list of ToolConfigDTO
        :param _WrapPaasID: 封装的API分组ID
        :type WrapPaasID: str
        :param _PluginConfigs: 插件配置
        :type PluginConfigs: list of PluginConfigDTO
        """
        self._Mode = None
        self._McpVersion = None
        self._InstanceID = None
        self._Name = None
        self._Description = None
        self._WrapServices = None
        self._TargetSelect = None
        self._TargetHosts = None
        self._HttpProtocolType = None
        self._CheckTargetCertsError = None
        self._TargetPath = None
        self._InvokeLimitConfigStatus = None
        self._InvokeLimitConfig = None
        self._IpWhiteStatus = None
        self._IpWhiteConfig = None
        self._IpBlackStatus = None
        self._IpBlackConfig = None
        self._CustomHttpHost = None
        self._HttpHostType = None
        self._Timeout = None
        self._McpSecurityRules = None
        self._ToolConfigs = None
        self._WrapPaasID = None
        self._PluginConfigs = None

    @property
    def Mode(self):
        r"""模式：proxy代理模式； wrap封装模式；
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def McpVersion(self):
        r"""版本号：2024-11-05 2025-03-26
        :rtype: str
        """
        return self._McpVersion

    @McpVersion.setter
    def McpVersion(self, McpVersion):
        self._McpVersion = McpVersion

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WrapServices(self):
        r"""封装服务列表
        :rtype: list of str
        """
        return self._WrapServices

    @WrapServices.setter
    def WrapServices(self, WrapServices):
        self._WrapServices = WrapServices

    @property
    def TargetSelect(self):
        r"""负载方式，robin random consistentHash
        :rtype: str
        """
        return self._TargetSelect

    @TargetSelect.setter
    def TargetSelect(self, TargetSelect):
        self._TargetSelect = TargetSelect

    @property
    def TargetHosts(self):
        r"""目标服务器
        :rtype: list of TargetHostDTO
        """
        return self._TargetHosts

    @TargetHosts.setter
    def TargetHosts(self, TargetHosts):
        self._TargetHosts = TargetHosts

    @property
    def HttpProtocolType(self):
        r"""后端协议：http https
        :rtype: str
        """
        return self._HttpProtocolType

    @HttpProtocolType.setter
    def HttpProtocolType(self, HttpProtocolType):
        self._HttpProtocolType = HttpProtocolType

    @property
    def CheckTargetCertsError(self):
        r"""证书检查
        :rtype: bool
        """
        return self._CheckTargetCertsError

    @CheckTargetCertsError.setter
    def CheckTargetCertsError(self, CheckTargetCertsError):
        self._CheckTargetCertsError = CheckTargetCertsError

    @property
    def TargetPath(self):
        r"""目标路径
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath

    @property
    def InvokeLimitConfigStatus(self):
        r"""流量控制开启状态
        :rtype: bool
        """
        return self._InvokeLimitConfigStatus

    @InvokeLimitConfigStatus.setter
    def InvokeLimitConfigStatus(self, InvokeLimitConfigStatus):
        self._InvokeLimitConfigStatus = InvokeLimitConfigStatus

    @property
    def InvokeLimitConfig(self):
        r"""流量控制配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        """
        return self._InvokeLimitConfig

    @InvokeLimitConfig.setter
    def InvokeLimitConfig(self, InvokeLimitConfig):
        self._InvokeLimitConfig = InvokeLimitConfig

    @property
    def IpWhiteStatus(self):
        r"""IP白名单开启状态
        :rtype: bool
        """
        return self._IpWhiteStatus

    @IpWhiteStatus.setter
    def IpWhiteStatus(self, IpWhiteStatus):
        self._IpWhiteStatus = IpWhiteStatus

    @property
    def IpWhiteConfig(self):
        r"""IP白名单配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        """
        return self._IpWhiteConfig

    @IpWhiteConfig.setter
    def IpWhiteConfig(self, IpWhiteConfig):
        self._IpWhiteConfig = IpWhiteConfig

    @property
    def IpBlackStatus(self):
        r"""IP黑名单开启状态
        :rtype: bool
        """
        return self._IpBlackStatus

    @IpBlackStatus.setter
    def IpBlackStatus(self, IpBlackStatus):
        self._IpBlackStatus = IpBlackStatus

    @property
    def IpBlackConfig(self):
        r"""IP黑名单配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        """
        return self._IpBlackConfig

    @IpBlackConfig.setter
    def IpBlackConfig(self, IpBlackConfig):
        self._IpBlackConfig = IpBlackConfig

    @property
    def CustomHttpHost(self):
        r"""自定义host
        :rtype: str
        """
        return self._CustomHttpHost

    @CustomHttpHost.setter
    def CustomHttpHost(self, CustomHttpHost):
        self._CustomHttpHost = CustomHttpHost

    @property
    def HttpHostType(self):
        r"""Http 请求host类型：useRequestHost 保持源请求；host targetHost 修正为源站host；  customHost 自定义host
        :rtype: str
        """
        return self._HttpHostType

    @HttpHostType.setter
    def HttpHostType(self, HttpHostType):
        self._HttpHostType = HttpHostType

    @property
    def Timeout(self):
        r"""请求的超时时间
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def McpSecurityRules(self):
        r"""安全规则集
        :rtype: list of McpSecurityRule
        """
        return self._McpSecurityRules

    @McpSecurityRules.setter
    def McpSecurityRules(self, McpSecurityRules):
        self._McpSecurityRules = McpSecurityRules

    @property
    def ToolConfigs(self):
        r"""工具集配置（openapi时或许用的是）
        :rtype: list of ToolConfigDTO
        """
        return self._ToolConfigs

    @ToolConfigs.setter
    def ToolConfigs(self, ToolConfigs):
        self._ToolConfigs = ToolConfigs

    @property
    def WrapPaasID(self):
        r"""封装的API分组ID
        :rtype: str
        """
        return self._WrapPaasID

    @WrapPaasID.setter
    def WrapPaasID(self, WrapPaasID):
        self._WrapPaasID = WrapPaasID

    @property
    def PluginConfigs(self):
        r"""插件配置
        :rtype: list of PluginConfigDTO
        """
        return self._PluginConfigs

    @PluginConfigs.setter
    def PluginConfigs(self, PluginConfigs):
        self._PluginConfigs = PluginConfigs


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._McpVersion = params.get("McpVersion")
        self._InstanceID = params.get("InstanceID")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._WrapServices = params.get("WrapServices")
        self._TargetSelect = params.get("TargetSelect")
        if params.get("TargetHosts") is not None:
            self._TargetHosts = []
            for item in params.get("TargetHosts"):
                obj = TargetHostDTO()
                obj._deserialize(item)
                self._TargetHosts.append(obj)
        self._HttpProtocolType = params.get("HttpProtocolType")
        self._CheckTargetCertsError = params.get("CheckTargetCertsError")
        self._TargetPath = params.get("TargetPath")
        self._InvokeLimitConfigStatus = params.get("InvokeLimitConfigStatus")
        if params.get("InvokeLimitConfig") is not None:
            self._InvokeLimitConfig = InvokeLimitConfigDTO()
            self._InvokeLimitConfig._deserialize(params.get("InvokeLimitConfig"))
        self._IpWhiteStatus = params.get("IpWhiteStatus")
        if params.get("IpWhiteConfig") is not None:
            self._IpWhiteConfig = IpConfig()
            self._IpWhiteConfig._deserialize(params.get("IpWhiteConfig"))
        self._IpBlackStatus = params.get("IpBlackStatus")
        if params.get("IpBlackConfig") is not None:
            self._IpBlackConfig = IpConfig()
            self._IpBlackConfig._deserialize(params.get("IpBlackConfig"))
        self._CustomHttpHost = params.get("CustomHttpHost")
        self._HttpHostType = params.get("HttpHostType")
        self._Timeout = params.get("Timeout")
        if params.get("McpSecurityRules") is not None:
            self._McpSecurityRules = []
            for item in params.get("McpSecurityRules"):
                obj = McpSecurityRule()
                obj._deserialize(item)
                self._McpSecurityRules.append(obj)
        if params.get("ToolConfigs") is not None:
            self._ToolConfigs = []
            for item in params.get("ToolConfigs"):
                obj = ToolConfigDTO()
                obj._deserialize(item)
                self._ToolConfigs.append(obj)
        self._WrapPaasID = params.get("WrapPaasID")
        if params.get("PluginConfigs") is not None:
            self._PluginConfigs = []
            for item in params.get("PluginConfigs"):
                obj = PluginConfigDTO()
                obj._deserialize(item)
                self._PluginConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMcpServerResponse(AbstractModel):
    r"""CreateMcpServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: mcp server ID
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""mcp server ID
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateModelRequest(AbstractModel):
    r"""CreateModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例
        :type InstanceID: str
        :param _Name: 模型名称
        :type Name: str
        :param _HttpProtocolType: 协议类型：http/https
        :type HttpProtocolType: str
        :param _TargetPath: 目标路径
        :type TargetPath: str
        :param _TargetHosts: 目标服务器
        :type TargetHosts: list of TargetHostDTO
        :param _CredentialID: 凭据ID
        :type CredentialID: str
        :param _CheckTargetCertsError: https时，是否检查证书合法
        :type CheckTargetCertsError: bool
        :param _HttpProtocolVersion: http协议版本：1.1/2.0
        :type HttpProtocolVersion: str
        """
        self._InstanceID = None
        self._Name = None
        self._HttpProtocolType = None
        self._TargetPath = None
        self._TargetHosts = None
        self._CredentialID = None
        self._CheckTargetCertsError = None
        self._HttpProtocolVersion = None

    @property
    def InstanceID(self):
        r"""实例
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Name(self):
        r"""模型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def HttpProtocolType(self):
        r"""协议类型：http/https
        :rtype: str
        """
        return self._HttpProtocolType

    @HttpProtocolType.setter
    def HttpProtocolType(self, HttpProtocolType):
        self._HttpProtocolType = HttpProtocolType

    @property
    def TargetPath(self):
        r"""目标路径
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath

    @property
    def TargetHosts(self):
        r"""目标服务器
        :rtype: list of TargetHostDTO
        """
        return self._TargetHosts

    @TargetHosts.setter
    def TargetHosts(self, TargetHosts):
        self._TargetHosts = TargetHosts

    @property
    def CredentialID(self):
        r"""凭据ID
        :rtype: str
        """
        return self._CredentialID

    @CredentialID.setter
    def CredentialID(self, CredentialID):
        self._CredentialID = CredentialID

    @property
    def CheckTargetCertsError(self):
        r"""https时，是否检查证书合法
        :rtype: bool
        """
        return self._CheckTargetCertsError

    @CheckTargetCertsError.setter
    def CheckTargetCertsError(self, CheckTargetCertsError):
        self._CheckTargetCertsError = CheckTargetCertsError

    @property
    def HttpProtocolVersion(self):
        r"""http协议版本：1.1/2.0
        :rtype: str
        """
        return self._HttpProtocolVersion

    @HttpProtocolVersion.setter
    def HttpProtocolVersion(self, HttpProtocolVersion):
        self._HttpProtocolVersion = HttpProtocolVersion


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Name = params.get("Name")
        self._HttpProtocolType = params.get("HttpProtocolType")
        self._TargetPath = params.get("TargetPath")
        if params.get("TargetHosts") is not None:
            self._TargetHosts = []
            for item in params.get("TargetHosts"):
                obj = TargetHostDTO()
                obj._deserialize(item)
                self._TargetHosts.append(obj)
        self._CredentialID = params.get("CredentialID")
        self._CheckTargetCertsError = params.get("CheckTargetCertsError")
        self._HttpProtocolVersion = params.get("HttpProtocolVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModelResponse(AbstractModel):
    r"""CreateModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateModelServiceRequest(AbstractModel):
    r"""CreateModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例
        :type InstanceID: str
        :param _Name: 模型服务名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _PubPath: 访问路径
        :type PubPath: str
        :param _TargetModels: 模型ID列表
        :type TargetModels: list of TargetModelDTO
        :param _PathMatchType: 路径匹配类型: prefix 前缀匹配(不送默认); absolute 绝对匹配; regex正则匹配;
        :type PathMatchType: str
        :param _InvokeLimitConfigStatus: 是否开启限流
        :type InvokeLimitConfigStatus: bool
        :param _InvokeLimitConfig: 限流配置
        :type InvokeLimitConfig: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        :param _TokenLimitStatus: 是否开启token控制
        :type TokenLimitStatus: bool
        :param _TokenLimitConfig: token控制
        :type TokenLimitConfig: :class:`tencentcloud.apis.v20240801.models.TokenLimitConfigDTO`
        :param _TmsStatus: 是否开启内容安全
        :type TmsStatus: bool
        :param _TmsConfig: 内容安全配置
        :type TmsConfig: :class:`tencentcloud.apis.v20240801.models.TmsConfigDTO`
        :param _IpWhiteStatus: 是否开启IP白名单
        :type IpWhiteStatus: bool
        :param _IpWhiteList: IP白名单
        :type IpWhiteList: list of str
        :param _IpBlackList: IP黑名单
        :type IpBlackList: list of str
        :param _PluginConfigs: 插件配置
        :type PluginConfigs: list of PluginConfigDTO
        :param _Timeout: 超时配置，秒
        :type Timeout: int
        """
        self._InstanceID = None
        self._Name = None
        self._Description = None
        self._PubPath = None
        self._TargetModels = None
        self._PathMatchType = None
        self._InvokeLimitConfigStatus = None
        self._InvokeLimitConfig = None
        self._TokenLimitStatus = None
        self._TokenLimitConfig = None
        self._TmsStatus = None
        self._TmsConfig = None
        self._IpWhiteStatus = None
        self._IpWhiteList = None
        self._IpBlackList = None
        self._PluginConfigs = None
        self._Timeout = None

    @property
    def InstanceID(self):
        r"""实例
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Name(self):
        r"""模型服务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PubPath(self):
        r"""访问路径
        :rtype: str
        """
        return self._PubPath

    @PubPath.setter
    def PubPath(self, PubPath):
        self._PubPath = PubPath

    @property
    def TargetModels(self):
        r"""模型ID列表
        :rtype: list of TargetModelDTO
        """
        return self._TargetModels

    @TargetModels.setter
    def TargetModels(self, TargetModels):
        self._TargetModels = TargetModels

    @property
    def PathMatchType(self):
        r"""路径匹配类型: prefix 前缀匹配(不送默认); absolute 绝对匹配; regex正则匹配;
        :rtype: str
        """
        return self._PathMatchType

    @PathMatchType.setter
    def PathMatchType(self, PathMatchType):
        self._PathMatchType = PathMatchType

    @property
    def InvokeLimitConfigStatus(self):
        r"""是否开启限流
        :rtype: bool
        """
        return self._InvokeLimitConfigStatus

    @InvokeLimitConfigStatus.setter
    def InvokeLimitConfigStatus(self, InvokeLimitConfigStatus):
        self._InvokeLimitConfigStatus = InvokeLimitConfigStatus

    @property
    def InvokeLimitConfig(self):
        r"""限流配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        """
        return self._InvokeLimitConfig

    @InvokeLimitConfig.setter
    def InvokeLimitConfig(self, InvokeLimitConfig):
        self._InvokeLimitConfig = InvokeLimitConfig

    @property
    def TokenLimitStatus(self):
        r"""是否开启token控制
        :rtype: bool
        """
        return self._TokenLimitStatus

    @TokenLimitStatus.setter
    def TokenLimitStatus(self, TokenLimitStatus):
        self._TokenLimitStatus = TokenLimitStatus

    @property
    def TokenLimitConfig(self):
        r"""token控制
        :rtype: :class:`tencentcloud.apis.v20240801.models.TokenLimitConfigDTO`
        """
        return self._TokenLimitConfig

    @TokenLimitConfig.setter
    def TokenLimitConfig(self, TokenLimitConfig):
        self._TokenLimitConfig = TokenLimitConfig

    @property
    def TmsStatus(self):
        r"""是否开启内容安全
        :rtype: bool
        """
        return self._TmsStatus

    @TmsStatus.setter
    def TmsStatus(self, TmsStatus):
        self._TmsStatus = TmsStatus

    @property
    def TmsConfig(self):
        r"""内容安全配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.TmsConfigDTO`
        """
        return self._TmsConfig

    @TmsConfig.setter
    def TmsConfig(self, TmsConfig):
        self._TmsConfig = TmsConfig

    @property
    def IpWhiteStatus(self):
        r"""是否开启IP白名单
        :rtype: bool
        """
        return self._IpWhiteStatus

    @IpWhiteStatus.setter
    def IpWhiteStatus(self, IpWhiteStatus):
        self._IpWhiteStatus = IpWhiteStatus

    @property
    def IpWhiteList(self):
        r"""IP白名单
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def IpBlackList(self):
        r"""IP黑名单
        :rtype: list of str
        """
        return self._IpBlackList

    @IpBlackList.setter
    def IpBlackList(self, IpBlackList):
        self._IpBlackList = IpBlackList

    @property
    def PluginConfigs(self):
        r"""插件配置
        :rtype: list of PluginConfigDTO
        """
        return self._PluginConfigs

    @PluginConfigs.setter
    def PluginConfigs(self, PluginConfigs):
        self._PluginConfigs = PluginConfigs

    @property
    def Timeout(self):
        r"""超时配置，秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._PubPath = params.get("PubPath")
        if params.get("TargetModels") is not None:
            self._TargetModels = []
            for item in params.get("TargetModels"):
                obj = TargetModelDTO()
                obj._deserialize(item)
                self._TargetModels.append(obj)
        self._PathMatchType = params.get("PathMatchType")
        self._InvokeLimitConfigStatus = params.get("InvokeLimitConfigStatus")
        if params.get("InvokeLimitConfig") is not None:
            self._InvokeLimitConfig = InvokeLimitConfigDTO()
            self._InvokeLimitConfig._deserialize(params.get("InvokeLimitConfig"))
        self._TokenLimitStatus = params.get("TokenLimitStatus")
        if params.get("TokenLimitConfig") is not None:
            self._TokenLimitConfig = TokenLimitConfigDTO()
            self._TokenLimitConfig._deserialize(params.get("TokenLimitConfig"))
        self._TmsStatus = params.get("TmsStatus")
        if params.get("TmsConfig") is not None:
            self._TmsConfig = TmsConfigDTO()
            self._TmsConfig._deserialize(params.get("TmsConfig"))
        self._IpWhiteStatus = params.get("IpWhiteStatus")
        self._IpWhiteList = params.get("IpWhiteList")
        self._IpBlackList = params.get("IpBlackList")
        if params.get("PluginConfigs") is not None:
            self._PluginConfigs = []
            for item in params.get("PluginConfigs"):
                obj = PluginConfigDTO()
                obj._deserialize(item)
                self._PluginConfigs.append(obj)
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModelServiceResponse(AbstractModel):
    r"""CreateModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteAgentAppMcpServersRequest(AbstractModel):
    r"""DeleteAgentAppMcpServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 应用ID
        :type ID: str
        :param _McpServerIDs: mcp server id数组
        :type McpServerIDs: list of str
        """
        self._InstanceID = None
        self._ID = None
        self._McpServerIDs = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""应用ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def McpServerIDs(self):
        r"""mcp server id数组
        :rtype: list of str
        """
        return self._McpServerIDs

    @McpServerIDs.setter
    def McpServerIDs(self, McpServerIDs):
        self._McpServerIDs = McpServerIDs


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        self._McpServerIDs = params.get("McpServerIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentAppMcpServersResponse(AbstractModel):
    r"""DeleteAgentAppMcpServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: app id
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""app id
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteAgentAppModelServicesRequest(AbstractModel):
    r"""DeleteAgentAppModelServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 应用ID
        :type ID: str
        :param _ModelServiceIDs: 关联的model service id
        :type ModelServiceIDs: list of str
        """
        self._InstanceID = None
        self._ID = None
        self._ModelServiceIDs = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""应用ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ModelServiceIDs(self):
        r"""关联的model service id
        :rtype: list of str
        """
        return self._ModelServiceIDs

    @ModelServiceIDs.setter
    def ModelServiceIDs(self, ModelServiceIDs):
        self._ModelServiceIDs = ModelServiceIDs


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        self._ModelServiceIDs = params.get("ModelServiceIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentAppModelServicesResponse(AbstractModel):
    r"""DeleteAgentAppModelServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: app id
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""app id
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteAgentAppRequest(AbstractModel):
    r"""DeleteAgentApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 应用ID
        :type ID: str
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""应用ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentAppResponse(AbstractModel):
    r"""DeleteAgentApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: app id
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""app id
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteAgentCredentialRequest(AbstractModel):
    r"""DeleteAgentCredential请求参数结构体

    """


class DeleteAgentCredentialResponse(AbstractModel):
    r"""DeleteAgentCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteMcpServerRequest(AbstractModel):
    r"""DeleteMcpServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: mcp server ID
        :type ID: str
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""mcp server ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMcpServerResponse(AbstractModel):
    r"""DeleteMcpServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: mcp server ID
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""mcp server ID
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteModelRequest(AbstractModel):
    r"""DeleteModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例
        :type InstanceID: str
        :param _IDs: 模型ID数组
        :type IDs: list of str
        """
        self._InstanceID = None
        self._IDs = None

    @property
    def InstanceID(self):
        r"""实例
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def IDs(self):
        r"""模型ID数组
        :rtype: list of str
        """
        return self._IDs

    @IDs.setter
    def IDs(self, IDs):
        self._IDs = IDs


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._IDs = params.get("IDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelResponse(AbstractModel):
    r"""DeleteModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDsVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDsVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDsVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteModelServiceRequest(AbstractModel):
    r"""DeleteModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例
        :type InstanceID: str
        :param _ID: 模型服务ID
        :type ID: str
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""实例
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""模型服务ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelServiceResponse(AbstractModel):
    r"""DeleteModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAgentAppMcpServersRequest(AbstractModel):
    r"""DescribeAgentAppMcpServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _AgentAppIDs: 应用ID
        :type AgentAppIDs: list of str
        :param _McpServerIDs: 关联的mcp
        :type McpServerIDs: list of str
        :param _AgentCredentialIDs: 凭据ID
        :type AgentCredentialIDs: list of str
        :param _Keyword: 关键词
        :type Keyword: str
        """
        self._Limit = None
        self._Offset = None
        self._InstanceID = None
        self._AgentAppIDs = None
        self._McpServerIDs = None
        self._AgentCredentialIDs = None
        self._Keyword = None

    @property
    def Limit(self):
        r"""分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def AgentAppIDs(self):
        r"""应用ID
        :rtype: list of str
        """
        return self._AgentAppIDs

    @AgentAppIDs.setter
    def AgentAppIDs(self, AgentAppIDs):
        self._AgentAppIDs = AgentAppIDs

    @property
    def McpServerIDs(self):
        r"""关联的mcp
        :rtype: list of str
        """
        return self._McpServerIDs

    @McpServerIDs.setter
    def McpServerIDs(self, McpServerIDs):
        self._McpServerIDs = McpServerIDs

    @property
    def AgentCredentialIDs(self):
        r"""凭据ID
        :rtype: list of str
        """
        return self._AgentCredentialIDs

    @AgentCredentialIDs.setter
    def AgentCredentialIDs(self, AgentCredentialIDs):
        self._AgentCredentialIDs = AgentCredentialIDs

    @property
    def Keyword(self):
        r"""关键词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceID = params.get("InstanceID")
        self._AgentAppIDs = params.get("AgentAppIDs")
        self._McpServerIDs = params.get("McpServerIDs")
        self._AgentCredentialIDs = params.get("AgentCredentialIDs")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentAppMcpServersResp(AbstractModel):
    r"""查询App mcpServer绑定列表响应

    """

    def __init__(self):
        r"""
        :param _Total: 条目总数
        :type Total: int
        :param _Items: 具体条目
        :type Items: list of AgentAppMcpServerVO
        """
        self._Total = None
        self._Items = None

    @property
    def Total(self):
        r"""条目总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""具体条目
        :rtype: list of AgentAppMcpServerVO
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AgentAppMcpServerVO()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentAppMcpServersResponse(AbstractModel):
    r"""DescribeAgentAppMcpServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表
        :type Data: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppMcpServersResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""列表
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppMcpServersResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeAgentAppMcpServersResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAgentAppModelServicesRequest(AbstractModel):
    r"""DescribeAgentAppModelServices请求参数结构体

    """


class DescribeAgentAppModelServicesResponse(AbstractModel):
    r"""DescribeAgentAppModelServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeAgentAppRequest(AbstractModel):
    r"""DescribeAgentApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: app id
        :type ID: str
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""app id
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentAppResp(AbstractModel):
    r"""查询app详情响应

    """

    def __init__(self):
        r"""
        :param _AppID: 租户appID
        :type AppID: int
        :param _Uin: 租户ID
        :type Uin: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 应用ID
        :type ID: str
        :param _Name: 名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _Status: 状态
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        :param _AuthType: 认证类型
        :type AuthType: str
        :param _ApiKeys: apiKeys列表，脱敏
        :type ApiKeys: list of str
        :param _SecretKeys: secretKey列表，脱敏
        :type SecretKeys: list of AgentAppSecretKeyVO
        :param _OAuth2ResourceServerID: OAuth2 Resource Server ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OAuth2ResourceServerID: str
        :param _McpServersNum: 绑定mcpServer数量
        :type McpServersNum: int
        :param _ModelServicesNum: 绑定的模型服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelServicesNum: int
        """
        self._AppID = None
        self._Uin = None
        self._InstanceID = None
        self._ID = None
        self._Name = None
        self._Description = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AuthType = None
        self._ApiKeys = None
        self._SecretKeys = None
        self._OAuth2ResourceServerID = None
        self._McpServersNum = None
        self._ModelServicesNum = None

    @property
    def AppID(self):
        r"""租户appID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        r"""租户ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""应用ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AuthType(self):
        r"""认证类型
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ApiKeys(self):
        r"""apiKeys列表，脱敏
        :rtype: list of str
        """
        return self._ApiKeys

    @ApiKeys.setter
    def ApiKeys(self, ApiKeys):
        self._ApiKeys = ApiKeys

    @property
    def SecretKeys(self):
        r"""secretKey列表，脱敏
        :rtype: list of AgentAppSecretKeyVO
        """
        return self._SecretKeys

    @SecretKeys.setter
    def SecretKeys(self, SecretKeys):
        self._SecretKeys = SecretKeys

    @property
    def OAuth2ResourceServerID(self):
        r"""OAuth2 Resource Server ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OAuth2ResourceServerID

    @OAuth2ResourceServerID.setter
    def OAuth2ResourceServerID(self, OAuth2ResourceServerID):
        self._OAuth2ResourceServerID = OAuth2ResourceServerID

    @property
    def McpServersNum(self):
        r"""绑定mcpServer数量
        :rtype: int
        """
        return self._McpServersNum

    @McpServersNum.setter
    def McpServersNum(self, McpServersNum):
        self._McpServersNum = McpServersNum

    @property
    def ModelServicesNum(self):
        r"""绑定的模型服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ModelServicesNum

    @ModelServicesNum.setter
    def ModelServicesNum(self, ModelServicesNum):
        self._ModelServicesNum = ModelServicesNum


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AuthType = params.get("AuthType")
        self._ApiKeys = params.get("ApiKeys")
        if params.get("SecretKeys") is not None:
            self._SecretKeys = []
            for item in params.get("SecretKeys"):
                obj = AgentAppSecretKeyVO()
                obj._deserialize(item)
                self._SecretKeys.append(obj)
        self._OAuth2ResourceServerID = params.get("OAuth2ResourceServerID")
        self._McpServersNum = params.get("McpServersNum")
        self._ModelServicesNum = params.get("ModelServicesNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentAppResponse(AbstractModel):
    r"""DescribeAgentApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: app详情
        :type Data: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""app详情
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeAgentAppResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAgentAppsRequest(AbstractModel):
    r"""DescribeAgentApps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _IDs: 服务ID数组
        :type IDs: list of str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _NotIDs: notID列表
        :type NotIDs: list of str
        :param _Status: 状态：normal正常状态，disabled下线状态
        :type Status: str
        :param _Keyword: 关键词
        :type Keyword: str
        :param _AuthType: 认证类型：apiKey，secretKey
        :type AuthType: str
        :param _Sort: 排序
        :type Sort: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppsSortDTO`
        :param _AgentCredentialID: 凭据ID
        :type AgentCredentialID: str
        """
        self._Limit = None
        self._Offset = None
        self._IDs = None
        self._InstanceID = None
        self._NotIDs = None
        self._Status = None
        self._Keyword = None
        self._AuthType = None
        self._Sort = None
        self._AgentCredentialID = None

    @property
    def Limit(self):
        r"""分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def IDs(self):
        r"""服务ID数组
        :rtype: list of str
        """
        return self._IDs

    @IDs.setter
    def IDs(self, IDs):
        self._IDs = IDs

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def NotIDs(self):
        r"""notID列表
        :rtype: list of str
        """
        return self._NotIDs

    @NotIDs.setter
    def NotIDs(self, NotIDs):
        self._NotIDs = NotIDs

    @property
    def Status(self):
        r"""状态：normal正常状态，disabled下线状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Keyword(self):
        r"""关键词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def AuthType(self):
        r"""认证类型：apiKey，secretKey
        :rtype: str
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def Sort(self):
        r"""排序
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppsSortDTO`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def AgentCredentialID(self):
        r"""凭据ID
        :rtype: str
        """
        return self._AgentCredentialID

    @AgentCredentialID.setter
    def AgentCredentialID(self, AgentCredentialID):
        self._AgentCredentialID = AgentCredentialID


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._IDs = params.get("IDs")
        self._InstanceID = params.get("InstanceID")
        self._NotIDs = params.get("NotIDs")
        self._Status = params.get("Status")
        self._Keyword = params.get("Keyword")
        self._AuthType = params.get("AuthType")
        if params.get("Sort") is not None:
            self._Sort = DescribeAgentAppsSortDTO()
            self._Sort._deserialize(params.get("Sort"))
        self._AgentCredentialID = params.get("AgentCredentialID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentAppsResp(AbstractModel):
    r"""查询App列表响应

    """

    def __init__(self):
        r"""
        :param _Total: 条目总数
        :type Total: int
        :param _Items: 具体条目
        :type Items: list of DescribeAgentAppResp
        """
        self._Total = None
        self._Items = None

    @property
    def Total(self):
        r"""条目总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""具体条目
        :rtype: list of DescribeAgentAppResp
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeAgentAppResp()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentAppsResponse(AbstractModel):
    r"""DescribeAgentApps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: app列表
        :type Data: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppsResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""app列表
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppsResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeAgentAppsResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAgentAppsSortDTO(AbstractModel):
    r"""agentApp查询排序

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _UpdateTime: 修改时间
        :type UpdateTime: int
        :param _Name: 名称
        :type Name: int
        :param _Status: 状态
        :type Status: int
        """
        self._CreateTime = None
        self._UpdateTime = None
        self._Name = None
        self._Status = None

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""修改时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Name(self):
        r"""名称
        :rtype: int
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentCredentialRequest(AbstractModel):
    r"""DescribeAgentCredential请求参数结构体

    """


class DescribeAgentCredentialResp(AbstractModel):
    r"""凭据详情响应

    """

    def __init__(self):
        r"""
        :param _AppID: 租户应用ID
        :type AppID: int
        :param _Uin: 租户ID
        :type Uin: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 凭据ID
        :type ID: str
        :param _Name: 凭据名称
        :type Name: str
        :param _Status: 状态
        :type Status: str
        :param _RelateAgentAppNum: 关联应用数
        :type RelateAgentAppNum: int
        :param _RelateMcpServerNum: 关联mcp数
        :type RelateMcpServerNum: int
        :param _RelateModelNum: 关联模型数
注意：此字段可能返回 null，表示取不到有效值。
        :type RelateModelNum: int
        :param _Content: 凭据内容
        :type Content: :class:`tencentcloud.apis.v20240801.models.AgentCredentialContentDTO`
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _LastUpdateTime: 修改时间
        :type LastUpdateTime: str
        :param _Type: 类型
        :type Type: str
        """
        self._AppID = None
        self._Uin = None
        self._InstanceID = None
        self._ID = None
        self._Name = None
        self._Status = None
        self._RelateAgentAppNum = None
        self._RelateMcpServerNum = None
        self._RelateModelNum = None
        self._Content = None
        self._CreateTime = None
        self._LastUpdateTime = None
        self._Type = None

    @property
    def AppID(self):
        r"""租户应用ID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        r"""租户ID
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""凭据ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""凭据名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RelateAgentAppNum(self):
        r"""关联应用数
        :rtype: int
        """
        return self._RelateAgentAppNum

    @RelateAgentAppNum.setter
    def RelateAgentAppNum(self, RelateAgentAppNum):
        self._RelateAgentAppNum = RelateAgentAppNum

    @property
    def RelateMcpServerNum(self):
        r"""关联mcp数
        :rtype: int
        """
        return self._RelateMcpServerNum

    @RelateMcpServerNum.setter
    def RelateMcpServerNum(self, RelateMcpServerNum):
        self._RelateMcpServerNum = RelateMcpServerNum

    @property
    def RelateModelNum(self):
        r"""关联模型数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RelateModelNum

    @RelateModelNum.setter
    def RelateModelNum(self, RelateModelNum):
        self._RelateModelNum = RelateModelNum

    @property
    def Content(self):
        r"""凭据内容
        :rtype: :class:`tencentcloud.apis.v20240801.models.AgentCredentialContentDTO`
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""修改时间
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Type(self):
        r"""类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._RelateAgentAppNum = params.get("RelateAgentAppNum")
        self._RelateMcpServerNum = params.get("RelateMcpServerNum")
        self._RelateModelNum = params.get("RelateModelNum")
        if params.get("Content") is not None:
            self._Content = AgentCredentialContentDTO()
            self._Content._deserialize(params.get("Content"))
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentCredentialResponse(AbstractModel):
    r"""DescribeAgentCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeAgentCredentialsRequest(AbstractModel):
    r"""DescribeAgentCredentials请求参数结构体

    """


class DescribeAgentCredentialsResponse(AbstractModel):
    r"""DescribeAgentCredentials返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeMcpServerRequest(AbstractModel):
    r"""DescribeMcpServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: mcp server ID
        :type ID: str
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""mcp server ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMcpServerResponse(AbstractModel):
    r"""DescribeMcpServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: mcp server详情
        :type Data: :class:`tencentcloud.apis.v20240801.models.DescribeMcpServerResponseVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""mcp server详情
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeMcpServerResponseVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeMcpServerResponseVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMcpServerResponseVO(AbstractModel):
    r"""DescribeMcpServerResponseVO

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceID: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _LabelIDs: 标签ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelIDs: list of str
        :param _CategoryIDs: 目录ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryIDs: list of str
        :param _TargetSelect: 负载方式，robin random consistentHash
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetSelect: str
        :param _TargetHosts: 目标服务器
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetHosts: list of TargetHostDTO
        :param _HttpProtocolType: 后端协议：http https
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpProtocolType: str
        :param _CheckTargetCertsError: 证书检查
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckTargetCertsError: bool
        :param _TargetPath: 目标路径
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetPath: str
        :param _InvokeLimitConfigStatus: 流量控制状态
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeLimitConfigStatus: bool
        :param _InvokeLimitConfig: 流量控制配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeLimitConfig: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        :param _IpWhiteStatus: IP白名单开启状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IpWhiteStatus: bool
        :param _IpWhiteConfig: IP白名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :type IpWhiteConfig: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        :param _IpBlackStatus: IP黑名单开启状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IpBlackStatus: bool
        :param _IpBlackConfig: IP黑名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :type IpBlackConfig: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        :param _ID: mcp server ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Url: 预览地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _App: 应用
注意：此字段可能返回 null，表示取不到有效值。
        :type App: :class:`tencentcloud.apis.v20240801.models.IDNameVO`
        :param _Catalogs: 目录
注意：此字段可能返回 null，表示取不到有效值。
        :type Catalogs: list of IDNameVO
        :param _Labels: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of IDNameVO
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _LastUpdateTime: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param _AppID: 用户appID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppID: int
        :param _Uin: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _CustomHttpHost: 自定义host
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomHttpHost: str
        :param _HttpHostType:  Http 请求host类型 useRequestHost 保持源请求host targetHost 修正为源站host  customHost 自定义host
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpHostType: str
        :param _Timeout: 请求的超时时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param _Mode: mcp server模式
        :type Mode: str
        :param _McpVersion: mcp version
        :type McpVersion: str
        :param _WrapServices: 封装模式下绑定的服务ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type WrapServices: list of str
        :param _ToolNum: 工具数量
        :type ToolNum: int
        :param _McpSecurityRulesVO: 安全规则集响应
        :type McpSecurityRulesVO: list of McpSecurityRulesVO
        :param _ToolConfigs: 真实工具级别配置，实时拉取了tool/list做渲染的，如果tool/list不通，就拉不到。
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolConfigs: list of ToolConfigVO
        :param _UrlObj: 访问URL
        :type UrlObj: :class:`tencentcloud.apis.v20240801.models.McpUrlObj`
        :param _ToolMessage: 后端mcp服务是否正常
        :type ToolMessage: str
        :param _Tools: 后端mcp服务的工具列表
        :type Tools: list of McpTool
        :param _WrapPaasID: 封装的API分组ID
        :type WrapPaasID: str
        :param _RelateAgentAppNum: 关联的agentApp数量
        :type RelateAgentAppNum: int
        :param _PluginConfigs: 插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PluginConfigs: list of PluginConfigDTO
        """
        self._InstanceID = None
        self._Name = None
        self._Description = None
        self._LabelIDs = None
        self._CategoryIDs = None
        self._TargetSelect = None
        self._TargetHosts = None
        self._HttpProtocolType = None
        self._CheckTargetCertsError = None
        self._TargetPath = None
        self._InvokeLimitConfigStatus = None
        self._InvokeLimitConfig = None
        self._IpWhiteStatus = None
        self._IpWhiteConfig = None
        self._IpBlackStatus = None
        self._IpBlackConfig = None
        self._ID = None
        self._Status = None
        self._Url = None
        self._App = None
        self._Catalogs = None
        self._Labels = None
        self._CreateTime = None
        self._LastUpdateTime = None
        self._AppID = None
        self._Uin = None
        self._CustomHttpHost = None
        self._HttpHostType = None
        self._Timeout = None
        self._Mode = None
        self._McpVersion = None
        self._WrapServices = None
        self._ToolNum = None
        self._McpSecurityRulesVO = None
        self._ToolConfigs = None
        self._UrlObj = None
        self._ToolMessage = None
        self._Tools = None
        self._WrapPaasID = None
        self._RelateAgentAppNum = None
        self._PluginConfigs = None

    @property
    def InstanceID(self):
        r"""实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Name(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def LabelIDs(self):
        r"""标签ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LabelIDs

    @LabelIDs.setter
    def LabelIDs(self, LabelIDs):
        self._LabelIDs = LabelIDs

    @property
    def CategoryIDs(self):
        r"""目录ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CategoryIDs

    @CategoryIDs.setter
    def CategoryIDs(self, CategoryIDs):
        self._CategoryIDs = CategoryIDs

    @property
    def TargetSelect(self):
        r"""负载方式，robin random consistentHash
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetSelect

    @TargetSelect.setter
    def TargetSelect(self, TargetSelect):
        self._TargetSelect = TargetSelect

    @property
    def TargetHosts(self):
        r"""目标服务器
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TargetHostDTO
        """
        return self._TargetHosts

    @TargetHosts.setter
    def TargetHosts(self, TargetHosts):
        self._TargetHosts = TargetHosts

    @property
    def HttpProtocolType(self):
        r"""后端协议：http https
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HttpProtocolType

    @HttpProtocolType.setter
    def HttpProtocolType(self, HttpProtocolType):
        self._HttpProtocolType = HttpProtocolType

    @property
    def CheckTargetCertsError(self):
        r"""证书检查
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CheckTargetCertsError

    @CheckTargetCertsError.setter
    def CheckTargetCertsError(self, CheckTargetCertsError):
        self._CheckTargetCertsError = CheckTargetCertsError

    @property
    def TargetPath(self):
        r"""目标路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath

    @property
    def InvokeLimitConfigStatus(self):
        r"""流量控制状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._InvokeLimitConfigStatus

    @InvokeLimitConfigStatus.setter
    def InvokeLimitConfigStatus(self, InvokeLimitConfigStatus):
        self._InvokeLimitConfigStatus = InvokeLimitConfigStatus

    @property
    def InvokeLimitConfig(self):
        r"""流量控制配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        """
        return self._InvokeLimitConfig

    @InvokeLimitConfig.setter
    def InvokeLimitConfig(self, InvokeLimitConfig):
        self._InvokeLimitConfig = InvokeLimitConfig

    @property
    def IpWhiteStatus(self):
        r"""IP白名单开启状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IpWhiteStatus

    @IpWhiteStatus.setter
    def IpWhiteStatus(self, IpWhiteStatus):
        self._IpWhiteStatus = IpWhiteStatus

    @property
    def IpWhiteConfig(self):
        r"""IP白名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        """
        return self._IpWhiteConfig

    @IpWhiteConfig.setter
    def IpWhiteConfig(self, IpWhiteConfig):
        self._IpWhiteConfig = IpWhiteConfig

    @property
    def IpBlackStatus(self):
        r"""IP黑名单开启状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IpBlackStatus

    @IpBlackStatus.setter
    def IpBlackStatus(self, IpBlackStatus):
        self._IpBlackStatus = IpBlackStatus

    @property
    def IpBlackConfig(self):
        r"""IP黑名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        """
        return self._IpBlackConfig

    @IpBlackConfig.setter
    def IpBlackConfig(self, IpBlackConfig):
        self._IpBlackConfig = IpBlackConfig

    @property
    def ID(self):
        r"""mcp server ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Status(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Url(self):
        r"""预览地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def App(self):
        r"""应用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apis.v20240801.models.IDNameVO`
        """
        return self._App

    @App.setter
    def App(self, App):
        self._App = App

    @property
    def Catalogs(self):
        r"""目录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IDNameVO
        """
        return self._Catalogs

    @Catalogs.setter
    def Catalogs(self, Catalogs):
        self._Catalogs = Catalogs

    @property
    def Labels(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IDNameVO
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def AppID(self):
        r"""用户appID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        r"""用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CustomHttpHost(self):
        r"""自定义host
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CustomHttpHost

    @CustomHttpHost.setter
    def CustomHttpHost(self, CustomHttpHost):
        self._CustomHttpHost = CustomHttpHost

    @property
    def HttpHostType(self):
        r""" Http 请求host类型 useRequestHost 保持源请求host targetHost 修正为源站host  customHost 自定义host
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HttpHostType

    @HttpHostType.setter
    def HttpHostType(self, HttpHostType):
        self._HttpHostType = HttpHostType

    @property
    def Timeout(self):
        r"""请求的超时时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Mode(self):
        r"""mcp server模式
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def McpVersion(self):
        r"""mcp version
        :rtype: str
        """
        return self._McpVersion

    @McpVersion.setter
    def McpVersion(self, McpVersion):
        self._McpVersion = McpVersion

    @property
    def WrapServices(self):
        r"""封装模式下绑定的服务ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._WrapServices

    @WrapServices.setter
    def WrapServices(self, WrapServices):
        self._WrapServices = WrapServices

    @property
    def ToolNum(self):
        r"""工具数量
        :rtype: int
        """
        return self._ToolNum

    @ToolNum.setter
    def ToolNum(self, ToolNum):
        self._ToolNum = ToolNum

    @property
    def McpSecurityRulesVO(self):
        r"""安全规则集响应
        :rtype: list of McpSecurityRulesVO
        """
        return self._McpSecurityRulesVO

    @McpSecurityRulesVO.setter
    def McpSecurityRulesVO(self, McpSecurityRulesVO):
        self._McpSecurityRulesVO = McpSecurityRulesVO

    @property
    def ToolConfigs(self):
        r"""真实工具级别配置，实时拉取了tool/list做渲染的，如果tool/list不通，就拉不到。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ToolConfigVO
        """
        return self._ToolConfigs

    @ToolConfigs.setter
    def ToolConfigs(self, ToolConfigs):
        self._ToolConfigs = ToolConfigs

    @property
    def UrlObj(self):
        r"""访问URL
        :rtype: :class:`tencentcloud.apis.v20240801.models.McpUrlObj`
        """
        return self._UrlObj

    @UrlObj.setter
    def UrlObj(self, UrlObj):
        self._UrlObj = UrlObj

    @property
    def ToolMessage(self):
        r"""后端mcp服务是否正常
        :rtype: str
        """
        return self._ToolMessage

    @ToolMessage.setter
    def ToolMessage(self, ToolMessage):
        self._ToolMessage = ToolMessage

    @property
    def Tools(self):
        r"""后端mcp服务的工具列表
        :rtype: list of McpTool
        """
        return self._Tools

    @Tools.setter
    def Tools(self, Tools):
        self._Tools = Tools

    @property
    def WrapPaasID(self):
        r"""封装的API分组ID
        :rtype: str
        """
        return self._WrapPaasID

    @WrapPaasID.setter
    def WrapPaasID(self, WrapPaasID):
        self._WrapPaasID = WrapPaasID

    @property
    def RelateAgentAppNum(self):
        r"""关联的agentApp数量
        :rtype: int
        """
        return self._RelateAgentAppNum

    @RelateAgentAppNum.setter
    def RelateAgentAppNum(self, RelateAgentAppNum):
        self._RelateAgentAppNum = RelateAgentAppNum

    @property
    def PluginConfigs(self):
        r"""插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PluginConfigDTO
        """
        return self._PluginConfigs

    @PluginConfigs.setter
    def PluginConfigs(self, PluginConfigs):
        self._PluginConfigs = PluginConfigs


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._LabelIDs = params.get("LabelIDs")
        self._CategoryIDs = params.get("CategoryIDs")
        self._TargetSelect = params.get("TargetSelect")
        if params.get("TargetHosts") is not None:
            self._TargetHosts = []
            for item in params.get("TargetHosts"):
                obj = TargetHostDTO()
                obj._deserialize(item)
                self._TargetHosts.append(obj)
        self._HttpProtocolType = params.get("HttpProtocolType")
        self._CheckTargetCertsError = params.get("CheckTargetCertsError")
        self._TargetPath = params.get("TargetPath")
        self._InvokeLimitConfigStatus = params.get("InvokeLimitConfigStatus")
        if params.get("InvokeLimitConfig") is not None:
            self._InvokeLimitConfig = InvokeLimitConfigDTO()
            self._InvokeLimitConfig._deserialize(params.get("InvokeLimitConfig"))
        self._IpWhiteStatus = params.get("IpWhiteStatus")
        if params.get("IpWhiteConfig") is not None:
            self._IpWhiteConfig = IpConfig()
            self._IpWhiteConfig._deserialize(params.get("IpWhiteConfig"))
        self._IpBlackStatus = params.get("IpBlackStatus")
        if params.get("IpBlackConfig") is not None:
            self._IpBlackConfig = IpConfig()
            self._IpBlackConfig._deserialize(params.get("IpBlackConfig"))
        self._ID = params.get("ID")
        self._Status = params.get("Status")
        self._Url = params.get("Url")
        if params.get("App") is not None:
            self._App = IDNameVO()
            self._App._deserialize(params.get("App"))
        if params.get("Catalogs") is not None:
            self._Catalogs = []
            for item in params.get("Catalogs"):
                obj = IDNameVO()
                obj._deserialize(item)
                self._Catalogs.append(obj)
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = IDNameVO()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        self._CustomHttpHost = params.get("CustomHttpHost")
        self._HttpHostType = params.get("HttpHostType")
        self._Timeout = params.get("Timeout")
        self._Mode = params.get("Mode")
        self._McpVersion = params.get("McpVersion")
        self._WrapServices = params.get("WrapServices")
        self._ToolNum = params.get("ToolNum")
        if params.get("McpSecurityRulesVO") is not None:
            self._McpSecurityRulesVO = []
            for item in params.get("McpSecurityRulesVO"):
                obj = McpSecurityRulesVO()
                obj._deserialize(item)
                self._McpSecurityRulesVO.append(obj)
        if params.get("ToolConfigs") is not None:
            self._ToolConfigs = []
            for item in params.get("ToolConfigs"):
                obj = ToolConfigVO()
                obj._deserialize(item)
                self._ToolConfigs.append(obj)
        if params.get("UrlObj") is not None:
            self._UrlObj = McpUrlObj()
            self._UrlObj._deserialize(params.get("UrlObj"))
        self._ToolMessage = params.get("ToolMessage")
        if params.get("Tools") is not None:
            self._Tools = []
            for item in params.get("Tools"):
                obj = McpTool()
                obj._deserialize(item)
                self._Tools.append(obj)
        self._WrapPaasID = params.get("WrapPaasID")
        self._RelateAgentAppNum = params.get("RelateAgentAppNum")
        if params.get("PluginConfigs") is not None:
            self._PluginConfigs = []
            for item in params.get("PluginConfigs"):
                obj = PluginConfigDTO()
                obj._deserialize(item)
                self._PluginConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMcpServersRequest(AbstractModel):
    r"""DescribeMcpServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _Statuses: 状态数组：normal正常状态，disabled下线状态
        :type Statuses: list of str
        :param _Keyword: 关键词
        :type Keyword: str
        :param _IDs: 服务ID数组
        :type IDs: list of str
        :param _Modes: 模式：proxy代理模式； wrap封装模式；
        :type Modes: list of str
        :param _McpSecurityRuleID: 绑定的安全规则ID
        :type McpSecurityRuleID: str
        :param _McpSecurityRuleAct: 绑定安全规则的处置动作（填写时McpSecurityRuleID得必填）
        :type McpSecurityRuleAct: str
        :param _PluginID: 已绑定插件id
        :type PluginID: str
        """
        self._Limit = None
        self._Offset = None
        self._InstanceID = None
        self._Statuses = None
        self._Keyword = None
        self._IDs = None
        self._Modes = None
        self._McpSecurityRuleID = None
        self._McpSecurityRuleAct = None
        self._PluginID = None

    @property
    def Limit(self):
        r"""分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Statuses(self):
        r"""状态数组：normal正常状态，disabled下线状态
        :rtype: list of str
        """
        return self._Statuses

    @Statuses.setter
    def Statuses(self, Statuses):
        self._Statuses = Statuses

    @property
    def Keyword(self):
        r"""关键词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def IDs(self):
        r"""服务ID数组
        :rtype: list of str
        """
        return self._IDs

    @IDs.setter
    def IDs(self, IDs):
        self._IDs = IDs

    @property
    def Modes(self):
        r"""模式：proxy代理模式； wrap封装模式；
        :rtype: list of str
        """
        return self._Modes

    @Modes.setter
    def Modes(self, Modes):
        self._Modes = Modes

    @property
    def McpSecurityRuleID(self):
        r"""绑定的安全规则ID
        :rtype: str
        """
        return self._McpSecurityRuleID

    @McpSecurityRuleID.setter
    def McpSecurityRuleID(self, McpSecurityRuleID):
        self._McpSecurityRuleID = McpSecurityRuleID

    @property
    def McpSecurityRuleAct(self):
        r"""绑定安全规则的处置动作（填写时McpSecurityRuleID得必填）
        :rtype: str
        """
        return self._McpSecurityRuleAct

    @McpSecurityRuleAct.setter
    def McpSecurityRuleAct(self, McpSecurityRuleAct):
        self._McpSecurityRuleAct = McpSecurityRuleAct

    @property
    def PluginID(self):
        r"""已绑定插件id
        :rtype: str
        """
        return self._PluginID

    @PluginID.setter
    def PluginID(self, PluginID):
        self._PluginID = PluginID


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceID = params.get("InstanceID")
        self._Statuses = params.get("Statuses")
        self._Keyword = params.get("Keyword")
        self._IDs = params.get("IDs")
        self._Modes = params.get("Modes")
        self._McpSecurityRuleID = params.get("McpSecurityRuleID")
        self._McpSecurityRuleAct = params.get("McpSecurityRuleAct")
        self._PluginID = params.get("PluginID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMcpServersResponse(AbstractModel):
    r"""DescribeMcpServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: mcp server列表
        :type Data: :class:`tencentcloud.apis.v20240801.models.DescribeMcpServersResponseVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""mcp server列表
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeMcpServersResponseVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeMcpServersResponseVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMcpServersResponseVO(AbstractModel):
    r"""ServicesVO

    """

    def __init__(self):
        r"""
        :param _Total: 条目
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Items: 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DescribeMcpServerResponseVO
        """
        self._Total = None
        self._Items = None

    @property
    def Total(self):
        r"""条目
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DescribeMcpServerResponseVO
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeMcpServerResponseVO()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelRequest(AbstractModel):
    r"""DescribeModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例
        :type InstanceID: str
        :param _ID: 模型ID
        :type ID: str
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""实例
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""模型ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelResponse(AbstractModel):
    r"""DescribeModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: :class:`tencentcloud.apis.v20240801.models.DescribeModelResponseVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeModelResponseVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeModelResponseVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeModelResponseVO(AbstractModel):
    r"""查询模型详情的响应

    """

    def __init__(self):
        r"""
        :param _AppID: 腾讯云AppID
        :type AppID: int
        :param _Uin: 腾讯云Uin
        :type Uin: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 模型ID
        :type ID: str
        :param _Name: 模型名称
        :type Name: str
        :param _CredentialID: 凭据ID
        :type CredentialID: str
        :param _CredentialName: 凭据名称
        :type CredentialName: str
        :param _HttpProtocolType: http协议类型
        :type HttpProtocolType: str
        :param _CheckTargetCertsError: https时，是否校验目标证书
        :type CheckTargetCertsError: bool
        :param _HttpProtocolVersion: http协议版本：1.1/2.0
        :type HttpProtocolVersion: str
        :param _TargetPath: 目标路径
        :type TargetPath: str
        :param _TargetHosts: 目标器列表
        :type TargetHosts: list of TargetHostDTO
        :param _ModelServiceCount: 被模型服务使用的个数
        :type ModelServiceCount: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _LastUpdateTime: 最后修改时间
        :type LastUpdateTime: str
        """
        self._AppID = None
        self._Uin = None
        self._InstanceID = None
        self._ID = None
        self._Name = None
        self._CredentialID = None
        self._CredentialName = None
        self._HttpProtocolType = None
        self._CheckTargetCertsError = None
        self._HttpProtocolVersion = None
        self._TargetPath = None
        self._TargetHosts = None
        self._ModelServiceCount = None
        self._CreateTime = None
        self._LastUpdateTime = None

    @property
    def AppID(self):
        r"""腾讯云AppID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        r"""腾讯云Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""模型ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""模型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CredentialID(self):
        r"""凭据ID
        :rtype: str
        """
        return self._CredentialID

    @CredentialID.setter
    def CredentialID(self, CredentialID):
        self._CredentialID = CredentialID

    @property
    def CredentialName(self):
        r"""凭据名称
        :rtype: str
        """
        return self._CredentialName

    @CredentialName.setter
    def CredentialName(self, CredentialName):
        self._CredentialName = CredentialName

    @property
    def HttpProtocolType(self):
        r"""http协议类型
        :rtype: str
        """
        return self._HttpProtocolType

    @HttpProtocolType.setter
    def HttpProtocolType(self, HttpProtocolType):
        self._HttpProtocolType = HttpProtocolType

    @property
    def CheckTargetCertsError(self):
        r"""https时，是否校验目标证书
        :rtype: bool
        """
        return self._CheckTargetCertsError

    @CheckTargetCertsError.setter
    def CheckTargetCertsError(self, CheckTargetCertsError):
        self._CheckTargetCertsError = CheckTargetCertsError

    @property
    def HttpProtocolVersion(self):
        r"""http协议版本：1.1/2.0
        :rtype: str
        """
        return self._HttpProtocolVersion

    @HttpProtocolVersion.setter
    def HttpProtocolVersion(self, HttpProtocolVersion):
        self._HttpProtocolVersion = HttpProtocolVersion

    @property
    def TargetPath(self):
        r"""目标路径
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath

    @property
    def TargetHosts(self):
        r"""目标器列表
        :rtype: list of TargetHostDTO
        """
        return self._TargetHosts

    @TargetHosts.setter
    def TargetHosts(self, TargetHosts):
        self._TargetHosts = TargetHosts

    @property
    def ModelServiceCount(self):
        r"""被模型服务使用的个数
        :rtype: int
        """
        return self._ModelServiceCount

    @ModelServiceCount.setter
    def ModelServiceCount(self, ModelServiceCount):
        self._ModelServiceCount = ModelServiceCount

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""最后修改时间
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._CredentialID = params.get("CredentialID")
        self._CredentialName = params.get("CredentialName")
        self._HttpProtocolType = params.get("HttpProtocolType")
        self._CheckTargetCertsError = params.get("CheckTargetCertsError")
        self._HttpProtocolVersion = params.get("HttpProtocolVersion")
        self._TargetPath = params.get("TargetPath")
        if params.get("TargetHosts") is not None:
            self._TargetHosts = []
            for item in params.get("TargetHosts"):
                obj = TargetHostDTO()
                obj._deserialize(item)
                self._TargetHosts.append(obj)
        self._ModelServiceCount = params.get("ModelServiceCount")
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceRequest(AbstractModel):
    r"""DescribeModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例
        :type InstanceID: str
        :param _ID: 模型服务ID
        :type ID: str
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""实例
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""模型服务ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceResponse(AbstractModel):
    r"""DescribeModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: :class:`tencentcloud.apis.v20240801.models.DescribeModelServiceResponseVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeModelServiceResponseVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeModelServiceResponseVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeModelServiceResponseVO(AbstractModel):
    r"""查询模型服务详情的响应

    """

    def __init__(self):
        r"""
        :param _AppID: 腾讯云AppID
        :type AppID: int
        :param _Uin: 腾讯云Uin
        :type Uin: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 模型ID
        :type ID: str
        :param _Name: 模型名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _PubPath: 访问路径
        :type PubPath: str
        :param _PathMatchType: 路径匹配方式：absolute，prefix，regex
        :type PathMatchType: str
        :param _TargetModels: 目标模型列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetModels: list of TargetModelDTO
        :param _ModelNames: 模板模型的名称列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelNames: list of str
        :param _InvokeLimitConfigStatus: 是否开启限流
        :type InvokeLimitConfigStatus: bool
        :param _InvokeLimitConfig: 限流配置
        :type InvokeLimitConfig: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _LastUpdateTime: 最后修改时间
        :type LastUpdateTime: str
        :param _TokenLimitStatus: 是否开启token控制
        :type TokenLimitStatus: bool
        :param _TokenLimitConfig: token控制
        :type TokenLimitConfig: :class:`tencentcloud.apis.v20240801.models.TokenLimitConfigDTO`
        :param _TmsStatus: 是否开启tms配置
        :type TmsStatus: bool
        :param _TmsConfig: tms配置
        :type TmsConfig: :class:`tencentcloud.apis.v20240801.models.TmsConfigDTO`
        :param _IpWhiteStatus: 是否开启IP白名单
        :type IpWhiteStatus: bool
        :param _IpWhiteList: IP白名单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IpWhiteList: list of str
        :param _IpBlackStatus: 是否开启IP黑名单
        :type IpBlackStatus: bool
        :param _IpBlackList: IP黑名单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IpBlackList: list of str
        :param _PluginConfigs: 插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PluginConfigs: list of PluginConfigDTO
        :param _Timeout: 超时配置，单位秒
        :type Timeout: int
        :param _Status: 状态：normal，disabled
        :type Status: str
        :param _RelateAgentAppNum: 关联应用数
        :type RelateAgentAppNum: int
        :param _Url: 请求路径
        :type Url: str
        """
        self._AppID = None
        self._Uin = None
        self._InstanceID = None
        self._ID = None
        self._Name = None
        self._Description = None
        self._PubPath = None
        self._PathMatchType = None
        self._TargetModels = None
        self._ModelNames = None
        self._InvokeLimitConfigStatus = None
        self._InvokeLimitConfig = None
        self._CreateTime = None
        self._LastUpdateTime = None
        self._TokenLimitStatus = None
        self._TokenLimitConfig = None
        self._TmsStatus = None
        self._TmsConfig = None
        self._IpWhiteStatus = None
        self._IpWhiteList = None
        self._IpBlackStatus = None
        self._IpBlackList = None
        self._PluginConfigs = None
        self._Timeout = None
        self._Status = None
        self._RelateAgentAppNum = None
        self._Url = None

    @property
    def AppID(self):
        r"""腾讯云AppID
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        r"""腾讯云Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""模型ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""模型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PubPath(self):
        r"""访问路径
        :rtype: str
        """
        return self._PubPath

    @PubPath.setter
    def PubPath(self, PubPath):
        self._PubPath = PubPath

    @property
    def PathMatchType(self):
        r"""路径匹配方式：absolute，prefix，regex
        :rtype: str
        """
        return self._PathMatchType

    @PathMatchType.setter
    def PathMatchType(self, PathMatchType):
        self._PathMatchType = PathMatchType

    @property
    def TargetModels(self):
        r"""目标模型列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TargetModelDTO
        """
        return self._TargetModels

    @TargetModels.setter
    def TargetModels(self, TargetModels):
        self._TargetModels = TargetModels

    @property
    def ModelNames(self):
        r"""模板模型的名称列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ModelNames

    @ModelNames.setter
    def ModelNames(self, ModelNames):
        self._ModelNames = ModelNames

    @property
    def InvokeLimitConfigStatus(self):
        r"""是否开启限流
        :rtype: bool
        """
        return self._InvokeLimitConfigStatus

    @InvokeLimitConfigStatus.setter
    def InvokeLimitConfigStatus(self, InvokeLimitConfigStatus):
        self._InvokeLimitConfigStatus = InvokeLimitConfigStatus

    @property
    def InvokeLimitConfig(self):
        r"""限流配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        """
        return self._InvokeLimitConfig

    @InvokeLimitConfig.setter
    def InvokeLimitConfig(self, InvokeLimitConfig):
        self._InvokeLimitConfig = InvokeLimitConfig

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""最后修改时间
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def TokenLimitStatus(self):
        r"""是否开启token控制
        :rtype: bool
        """
        return self._TokenLimitStatus

    @TokenLimitStatus.setter
    def TokenLimitStatus(self, TokenLimitStatus):
        self._TokenLimitStatus = TokenLimitStatus

    @property
    def TokenLimitConfig(self):
        r"""token控制
        :rtype: :class:`tencentcloud.apis.v20240801.models.TokenLimitConfigDTO`
        """
        return self._TokenLimitConfig

    @TokenLimitConfig.setter
    def TokenLimitConfig(self, TokenLimitConfig):
        self._TokenLimitConfig = TokenLimitConfig

    @property
    def TmsStatus(self):
        r"""是否开启tms配置
        :rtype: bool
        """
        return self._TmsStatus

    @TmsStatus.setter
    def TmsStatus(self, TmsStatus):
        self._TmsStatus = TmsStatus

    @property
    def TmsConfig(self):
        r"""tms配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.TmsConfigDTO`
        """
        return self._TmsConfig

    @TmsConfig.setter
    def TmsConfig(self, TmsConfig):
        self._TmsConfig = TmsConfig

    @property
    def IpWhiteStatus(self):
        r"""是否开启IP白名单
        :rtype: bool
        """
        return self._IpWhiteStatus

    @IpWhiteStatus.setter
    def IpWhiteStatus(self, IpWhiteStatus):
        self._IpWhiteStatus = IpWhiteStatus

    @property
    def IpWhiteList(self):
        r"""IP白名单列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def IpBlackStatus(self):
        r"""是否开启IP黑名单
        :rtype: bool
        """
        return self._IpBlackStatus

    @IpBlackStatus.setter
    def IpBlackStatus(self, IpBlackStatus):
        self._IpBlackStatus = IpBlackStatus

    @property
    def IpBlackList(self):
        r"""IP黑名单列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._IpBlackList

    @IpBlackList.setter
    def IpBlackList(self, IpBlackList):
        self._IpBlackList = IpBlackList

    @property
    def PluginConfigs(self):
        r"""插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PluginConfigDTO
        """
        return self._PluginConfigs

    @PluginConfigs.setter
    def PluginConfigs(self, PluginConfigs):
        self._PluginConfigs = PluginConfigs

    @property
    def Timeout(self):
        r"""超时配置，单位秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Status(self):
        r"""状态：normal，disabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RelateAgentAppNum(self):
        r"""关联应用数
        :rtype: int
        """
        return self._RelateAgentAppNum

    @RelateAgentAppNum.setter
    def RelateAgentAppNum(self, RelateAgentAppNum):
        self._RelateAgentAppNum = RelateAgentAppNum

    @property
    def Url(self):
        r"""请求路径
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._PubPath = params.get("PubPath")
        self._PathMatchType = params.get("PathMatchType")
        if params.get("TargetModels") is not None:
            self._TargetModels = []
            for item in params.get("TargetModels"):
                obj = TargetModelDTO()
                obj._deserialize(item)
                self._TargetModels.append(obj)
        self._ModelNames = params.get("ModelNames")
        self._InvokeLimitConfigStatus = params.get("InvokeLimitConfigStatus")
        if params.get("InvokeLimitConfig") is not None:
            self._InvokeLimitConfig = InvokeLimitConfigDTO()
            self._InvokeLimitConfig._deserialize(params.get("InvokeLimitConfig"))
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._TokenLimitStatus = params.get("TokenLimitStatus")
        if params.get("TokenLimitConfig") is not None:
            self._TokenLimitConfig = TokenLimitConfigDTO()
            self._TokenLimitConfig._deserialize(params.get("TokenLimitConfig"))
        self._TmsStatus = params.get("TmsStatus")
        if params.get("TmsConfig") is not None:
            self._TmsConfig = TmsConfigDTO()
            self._TmsConfig._deserialize(params.get("TmsConfig"))
        self._IpWhiteStatus = params.get("IpWhiteStatus")
        self._IpWhiteList = params.get("IpWhiteList")
        self._IpBlackStatus = params.get("IpBlackStatus")
        self._IpBlackList = params.get("IpBlackList")
        if params.get("PluginConfigs") is not None:
            self._PluginConfigs = []
            for item in params.get("PluginConfigs"):
                obj = PluginConfigDTO()
                obj._deserialize(item)
                self._PluginConfigs.append(obj)
        self._Timeout = params.get("Timeout")
        self._Status = params.get("Status")
        self._RelateAgentAppNum = params.get("RelateAgentAppNum")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServicesRequest(AbstractModel):
    r"""DescribeModelServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例
        :type InstanceID: str
        :param _Offset: 分页参数
        :type Offset: int
        :param _Limit: 分页限制
        :type Limit: int
        :param _IDs: ID列表
        :type IDs: list of str
        :param _NotIDs: 排除的ID列表
        :type NotIDs: list of str
        :param _Status: 状态：normal，disabled
        :type Status: str
        :param _Keyword: 关键词
        :type Keyword: str
        :param _ModelID: 模型ID
        :type ModelID: str
        :param _Sort: 排序
        :type Sort: :class:`tencentcloud.apis.v20240801.models.DescribeModelServicesSort`
        """
        self._InstanceID = None
        self._Offset = None
        self._Limit = None
        self._IDs = None
        self._NotIDs = None
        self._Status = None
        self._Keyword = None
        self._ModelID = None
        self._Sort = None

    @property
    def InstanceID(self):
        r"""实例
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Offset(self):
        r"""分页参数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def IDs(self):
        r"""ID列表
        :rtype: list of str
        """
        return self._IDs

    @IDs.setter
    def IDs(self, IDs):
        self._IDs = IDs

    @property
    def NotIDs(self):
        r"""排除的ID列表
        :rtype: list of str
        """
        return self._NotIDs

    @NotIDs.setter
    def NotIDs(self, NotIDs):
        self._NotIDs = NotIDs

    @property
    def Status(self):
        r"""状态：normal，disabled
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Keyword(self):
        r"""关键词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def ModelID(self):
        r"""模型ID
        :rtype: str
        """
        return self._ModelID

    @ModelID.setter
    def ModelID(self, ModelID):
        self._ModelID = ModelID

    @property
    def Sort(self):
        r"""排序
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeModelServicesSort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IDs = params.get("IDs")
        self._NotIDs = params.get("NotIDs")
        self._Status = params.get("Status")
        self._Keyword = params.get("Keyword")
        self._ModelID = params.get("ModelID")
        if params.get("Sort") is not None:
            self._Sort = DescribeModelServicesSort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServicesResponse(AbstractModel):
    r"""DescribeModelServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: :class:`tencentcloud.apis.v20240801.models.DescribeModelServicesResponseVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeModelServicesResponseVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeModelServicesResponseVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeModelServicesResponseVO(AbstractModel):
    r"""查询模型列表的响应

    """

    def __init__(self):
        r"""
        :param _Total: 条目
        :type Total: int
        :param _Items: 列表
        :type Items: list of DescribeModelServiceResponseVO
        """
        self._Total = None
        self._Items = None

    @property
    def Total(self):
        r"""条目
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""列表
        :rtype: list of DescribeModelServiceResponseVO
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeModelServiceResponseVO()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServicesSort(AbstractModel):
    r"""查询模型服务列表的排序

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _LastUpdateTime: 最后修改时间
        :type LastUpdateTime: int
        :param _Name: 模型名称
        :type Name: int
        :param _Status: 状态
        :type Status: int
        """
        self._CreateTime = None
        self._LastUpdateTime = None
        self._Name = None
        self._Status = None

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""最后修改时间
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Name(self):
        r"""模型名称
        :rtype: int
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelsRequest(AbstractModel):
    r"""DescribeModels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例
        :type InstanceID: str
        :param _Offset: 分页参数
        :type Offset: int
        :param _Limit: 分页限制
        :type Limit: int
        :param _IDs: ID列表
        :type IDs: list of str
        :param _NotIDs: 排除的ID列表
        :type NotIDs: list of str
        :param _CredentialID: 凭据ID
        :type CredentialID: str
        :param _Keyword: 关键词
        :type Keyword: str
        :param _Sort: 排序
        :type Sort: :class:`tencentcloud.apis.v20240801.models.DescribeModelsSort`
        """
        self._InstanceID = None
        self._Offset = None
        self._Limit = None
        self._IDs = None
        self._NotIDs = None
        self._CredentialID = None
        self._Keyword = None
        self._Sort = None

    @property
    def InstanceID(self):
        r"""实例
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Offset(self):
        r"""分页参数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def IDs(self):
        r"""ID列表
        :rtype: list of str
        """
        return self._IDs

    @IDs.setter
    def IDs(self, IDs):
        self._IDs = IDs

    @property
    def NotIDs(self):
        r"""排除的ID列表
        :rtype: list of str
        """
        return self._NotIDs

    @NotIDs.setter
    def NotIDs(self, NotIDs):
        self._NotIDs = NotIDs

    @property
    def CredentialID(self):
        r"""凭据ID
        :rtype: str
        """
        return self._CredentialID

    @CredentialID.setter
    def CredentialID(self, CredentialID):
        self._CredentialID = CredentialID

    @property
    def Keyword(self):
        r"""关键词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Sort(self):
        r"""排序
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeModelsSort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IDs = params.get("IDs")
        self._NotIDs = params.get("NotIDs")
        self._CredentialID = params.get("CredentialID")
        self._Keyword = params.get("Keyword")
        if params.get("Sort") is not None:
            self._Sort = DescribeModelsSort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelsResponse(AbstractModel):
    r"""DescribeModels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: :class:`tencentcloud.apis.v20240801.models.DescribeModelsResponseVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeModelsResponseVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeModelsResponseVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeModelsResponseVO(AbstractModel):
    r"""查询模型列表的响应

    """

    def __init__(self):
        r"""
        :param _Total: 条目
        :type Total: int
        :param _Items: 列表
        :type Items: list of DescribeModelResponseVO
        """
        self._Total = None
        self._Items = None

    @property
    def Total(self):
        r"""条目
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""列表
        :rtype: list of DescribeModelResponseVO
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DescribeModelResponseVO()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelsSort(AbstractModel):
    r"""DescribeModelsSort

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _LastUpdateTime: 最后修改时间
        :type LastUpdateTime: int
        :param _Name: 模型名称
        :type Name: int
        """
        self._CreateTime = None
        self._LastUpdateTime = None
        self._Name = None

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""最后修改时间
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Name(self):
        r"""模型名称
        :rtype: int
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IDNameVO(AbstractModel):
    r"""IDNameVO

    """

    def __init__(self):
        r"""
        :param _ID: 业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._ID = None
        self._Name = None

    @property
    def ID(self):
        r"""业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeLimitConfigDTO(AbstractModel):
    r"""InvokeLimitConfigDTO

    """

    def __init__(self):
        r"""
        :param _Type: Type类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _TokenBucketMaxNum: 令牌桶最大容量

注意：此字段可能返回 null，表示取不到有效值。
        :type TokenBucketMaxNum: int
        :param _TokenBucketRate: 令牌生成速率
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenBucketRate: int
        :param _FunnelMaxNum: 漏斗容量
注意：此字段可能返回 null，表示取不到有效值。
        :type FunnelMaxNum: int
        :param _FunnelRate: 漏嘴流速
注意：此字段可能返回 null，表示取不到有效值。
        :type FunnelRate: int
        :param _SlidingWindowMaxNum: 滑动窗口最大请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type SlidingWindowMaxNum: int
        :param _SlidingWindowSize: 滑动窗口长度
注意：此字段可能返回 null，表示取不到有效值。
        :type SlidingWindowSize: int
        :param _TimeWindow: 时间窗口最大请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeWindow: int
        :param _TimeWindowInterval: 时间窗口长度
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeWindowInterval: int
        :param _Timeout: 请求的超时时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        """
        self._Type = None
        self._TokenBucketMaxNum = None
        self._TokenBucketRate = None
        self._FunnelMaxNum = None
        self._FunnelRate = None
        self._SlidingWindowMaxNum = None
        self._SlidingWindowSize = None
        self._TimeWindow = None
        self._TimeWindowInterval = None
        self._Timeout = None

    @property
    def Type(self):
        r"""Type类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TokenBucketMaxNum(self):
        r"""令牌桶最大容量

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TokenBucketMaxNum

    @TokenBucketMaxNum.setter
    def TokenBucketMaxNum(self, TokenBucketMaxNum):
        self._TokenBucketMaxNum = TokenBucketMaxNum

    @property
    def TokenBucketRate(self):
        r"""令牌生成速率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TokenBucketRate

    @TokenBucketRate.setter
    def TokenBucketRate(self, TokenBucketRate):
        self._TokenBucketRate = TokenBucketRate

    @property
    def FunnelMaxNum(self):
        r"""漏斗容量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FunnelMaxNum

    @FunnelMaxNum.setter
    def FunnelMaxNum(self, FunnelMaxNum):
        self._FunnelMaxNum = FunnelMaxNum

    @property
    def FunnelRate(self):
        r"""漏嘴流速
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FunnelRate

    @FunnelRate.setter
    def FunnelRate(self, FunnelRate):
        self._FunnelRate = FunnelRate

    @property
    def SlidingWindowMaxNum(self):
        r"""滑动窗口最大请求数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SlidingWindowMaxNum

    @SlidingWindowMaxNum.setter
    def SlidingWindowMaxNum(self, SlidingWindowMaxNum):
        self._SlidingWindowMaxNum = SlidingWindowMaxNum

    @property
    def SlidingWindowSize(self):
        r"""滑动窗口长度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SlidingWindowSize

    @SlidingWindowSize.setter
    def SlidingWindowSize(self, SlidingWindowSize):
        self._SlidingWindowSize = SlidingWindowSize

    @property
    def TimeWindow(self):
        r"""时间窗口最大请求数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimeWindow

    @TimeWindow.setter
    def TimeWindow(self, TimeWindow):
        self._TimeWindow = TimeWindow

    @property
    def TimeWindowInterval(self):
        r"""时间窗口长度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimeWindowInterval

    @TimeWindowInterval.setter
    def TimeWindowInterval(self, TimeWindowInterval):
        self._TimeWindowInterval = TimeWindowInterval

    @property
    def Timeout(self):
        r"""请求的超时时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TokenBucketMaxNum = params.get("TokenBucketMaxNum")
        self._TokenBucketRate = params.get("TokenBucketRate")
        self._FunnelMaxNum = params.get("FunnelMaxNum")
        self._FunnelRate = params.get("FunnelRate")
        self._SlidingWindowMaxNum = params.get("SlidingWindowMaxNum")
        self._SlidingWindowSize = params.get("SlidingWindowSize")
        self._TimeWindow = params.get("TimeWindow")
        self._TimeWindowInterval = params.get("TimeWindowInterval")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpConfig(AbstractModel):
    r"""ip黑白名单配置

    """

    def __init__(self):
        r"""
        :param _Ips: ip数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Ips: list of str
        :param _EffectType: 生效类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectType: str
        :param _EffectTimes: 生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectTimes: list of StartEndTime
        :param _Comment: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        """
        self._Ips = None
        self._EffectType = None
        self._EffectTimes = None
        self._Comment = None

    @property
    def Ips(self):
        r"""ip数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def EffectType(self):
        r"""生效类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EffectType

    @EffectType.setter
    def EffectType(self, EffectType):
        self._EffectType = EffectType

    @property
    def EffectTimes(self):
        r"""生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StartEndTime
        """
        return self._EffectTimes

    @EffectTimes.setter
    def EffectTimes(self, EffectTimes):
        self._EffectTimes = EffectTimes

    @property
    def Comment(self):
        r"""备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Ips = params.get("Ips")
        self._EffectType = params.get("EffectType")
        if params.get("EffectTimes") is not None:
            self._EffectTimes = []
            for item in params.get("EffectTimes"):
                obj = StartEndTime()
                obj._deserialize(item)
                self._EffectTimes.append(obj)
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LimitWindowsDTO(AbstractModel):
    r"""限流窗口配置

    """

    def __init__(self):
        r"""
        :param _Interval: 时间窗口，分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type Interval: int
        :param _Limit: 累计上限，k
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        """
        self._Interval = None
        self._Limit = None

    @property
    def Interval(self):
        r"""时间窗口，分钟
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Limit(self):
        r"""累计上限，k
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McpInputOutSchema(AbstractModel):
    r"""出入参说明

    """

    def __init__(self):
        r"""
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Properties: 属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: str
        :param _Required: 必填字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Required: list of str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._Type = None
        self._Properties = None
        self._Required = None
        self._Description = None

    @property
    def Type(self):
        r"""类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Properties(self):
        r"""属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def Required(self):
        r"""必填字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Properties = params.get("Properties")
        self._Required = params.get("Required")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McpSecurityRule(AbstractModel):
    r"""mcp安全规则

    """

    def __init__(self):
        r"""
        :param _ID: 规则ID
        :type ID: str
        :param _Status: 状态
        :type Status: str
        :param _Act: 处置动作
        :type Act: str
        """
        self._ID = None
        self._Status = None
        self._Act = None

    @property
    def ID(self):
        r"""规则ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Status(self):
        r"""状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Act(self):
        r"""处置动作
        :rtype: str
        """
        return self._Act

    @Act.setter
    def Act(self, Act):
        self._Act = Act


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Status = params.get("Status")
        self._Act = params.get("Act")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McpSecurityRulesVO(AbstractModel):
    r"""绑定的安全规则列表

    """

    def __init__(self):
        r"""
        :param _ID: 规则ID
        :type ID: str
        :param _Type: 规则类型
        :type Type: str
        :param _Name: 规则名称
        :type Name: str
        :param _Description: 规则描述
        :type Description: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: str
        :param _VersionNumber: 版本号
        :type VersionNumber: str
        :param _Status: 状态开关
        :type Status: str
        :param _Act: 当前选择的处置动作
        :type Act: str
        :param _SupportActs: 支持的处置动作
        :type SupportActs: list of str
        :param _BodyType: 内容类型
        :type BodyType: str
        :param _IconType: icon类型
        :type IconType: str
        """
        self._ID = None
        self._Type = None
        self._Name = None
        self._Description = None
        self._RiskLevel = None
        self._VersionNumber = None
        self._Status = None
        self._Act = None
        self._SupportActs = None
        self._BodyType = None
        self._IconType = None

    @property
    def ID(self):
        r"""规则ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Type(self):
        r"""规则类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""规则名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def VersionNumber(self):
        r"""版本号
        :rtype: str
        """
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        self._VersionNumber = VersionNumber

    @property
    def Status(self):
        r"""状态开关
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Act(self):
        r"""当前选择的处置动作
        :rtype: str
        """
        return self._Act

    @Act.setter
    def Act(self, Act):
        self._Act = Act

    @property
    def SupportActs(self):
        r"""支持的处置动作
        :rtype: list of str
        """
        return self._SupportActs

    @SupportActs.setter
    def SupportActs(self, SupportActs):
        self._SupportActs = SupportActs

    @property
    def BodyType(self):
        r"""内容类型
        :rtype: str
        """
        return self._BodyType

    @BodyType.setter
    def BodyType(self, BodyType):
        self._BodyType = BodyType

    @property
    def IconType(self):
        r"""icon类型
        :rtype: str
        """
        return self._IconType

    @IconType.setter
    def IconType(self, IconType):
        self._IconType = IconType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._RiskLevel = params.get("RiskLevel")
        self._VersionNumber = params.get("VersionNumber")
        self._Status = params.get("Status")
        self._Act = params.get("Act")
        self._SupportActs = params.get("SupportActs")
        self._BodyType = params.get("BodyType")
        self._IconType = params.get("IconType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McpTool(AbstractModel):
    r"""mcp工具

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _InputSchema: 入参参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InputSchema: :class:`tencentcloud.apis.v20240801.models.McpInputOutSchema`
        :param _Annotations: 注释
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotations: :class:`tencentcloud.apis.v20240801.models.McpToolAnnotation`
        :param _OutputSchema: 出参参数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputSchema: :class:`tencentcloud.apis.v20240801.models.McpInputOutSchema`
        """
        self._Name = None
        self._Description = None
        self._InputSchema = None
        self._Annotations = None
        self._OutputSchema = None

    @property
    def Name(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InputSchema(self):
        r"""入参参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apis.v20240801.models.McpInputOutSchema`
        """
        return self._InputSchema

    @InputSchema.setter
    def InputSchema(self, InputSchema):
        self._InputSchema = InputSchema

    @property
    def Annotations(self):
        r"""注释
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apis.v20240801.models.McpToolAnnotation`
        """
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def OutputSchema(self):
        r"""出参参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apis.v20240801.models.McpInputOutSchema`
        """
        return self._OutputSchema

    @OutputSchema.setter
    def OutputSchema(self, OutputSchema):
        self._OutputSchema = OutputSchema


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("InputSchema") is not None:
            self._InputSchema = McpInputOutSchema()
            self._InputSchema._deserialize(params.get("InputSchema"))
        if params.get("Annotations") is not None:
            self._Annotations = McpToolAnnotation()
            self._Annotations._deserialize(params.get("Annotations"))
        if params.get("OutputSchema") is not None:
            self._OutputSchema = McpInputOutSchema()
            self._OutputSchema._deserialize(params.get("OutputSchema"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McpToolAnnotation(AbstractModel):
    r"""mcp工具注解

    """

    def __init__(self):
        r"""
        :param _Title: title for the tool
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _ReadOnlyHint: If true, the tool does not modify its environment
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnlyHint: bool
        :param _DestructiveHint: If true, the tool may perform destructive updates
注意：此字段可能返回 null，表示取不到有效值。
        :type DestructiveHint: bool
        :param _IdempotentHint: If true, repeated calls with same args have no additional effect
注意：此字段可能返回 null，表示取不到有效值。
        :type IdempotentHint: bool
        :param _OpenWorldHint: If true, tool interacts with external entities
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenWorldHint: bool
        """
        self._Title = None
        self._ReadOnlyHint = None
        self._DestructiveHint = None
        self._IdempotentHint = None
        self._OpenWorldHint = None

    @property
    def Title(self):
        r"""title for the tool
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def ReadOnlyHint(self):
        r"""If true, the tool does not modify its environment
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ReadOnlyHint

    @ReadOnlyHint.setter
    def ReadOnlyHint(self, ReadOnlyHint):
        self._ReadOnlyHint = ReadOnlyHint

    @property
    def DestructiveHint(self):
        r"""If true, the tool may perform destructive updates
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._DestructiveHint

    @DestructiveHint.setter
    def DestructiveHint(self, DestructiveHint):
        self._DestructiveHint = DestructiveHint

    @property
    def IdempotentHint(self):
        r"""If true, repeated calls with same args have no additional effect
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IdempotentHint

    @IdempotentHint.setter
    def IdempotentHint(self, IdempotentHint):
        self._IdempotentHint = IdempotentHint

    @property
    def OpenWorldHint(self):
        r"""If true, tool interacts with external entities
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._OpenWorldHint

    @OpenWorldHint.setter
    def OpenWorldHint(self, OpenWorldHint):
        self._OpenWorldHint = OpenWorldHint


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._ReadOnlyHint = params.get("ReadOnlyHint")
        self._DestructiveHint = params.get("DestructiveHint")
        self._IdempotentHint = params.get("IdempotentHint")
        self._OpenWorldHint = params.get("OpenWorldHint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McpUrlObj(AbstractModel):
    r"""Mcp的访问URL

    """

    def __init__(self):
        r"""
        :param _SSEUrl: sse访问URL
        :type SSEUrl: str
        :param _StreamAbleUrl: streamable访问URL
        :type StreamAbleUrl: str
        """
        self._SSEUrl = None
        self._StreamAbleUrl = None

    @property
    def SSEUrl(self):
        r"""sse访问URL
        :rtype: str
        """
        return self._SSEUrl

    @SSEUrl.setter
    def SSEUrl(self, SSEUrl):
        self._SSEUrl = SSEUrl

    @property
    def StreamAbleUrl(self):
        r"""streamable访问URL
        :rtype: str
        """
        return self._StreamAbleUrl

    @StreamAbleUrl.setter
    def StreamAbleUrl(self, StreamAbleUrl):
        self._StreamAbleUrl = StreamAbleUrl


    def _deserialize(self, params):
        self._SSEUrl = params.get("SSEUrl")
        self._StreamAbleUrl = params.get("StreamAbleUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentAppModelServicesRequest(AbstractModel):
    r"""ModifyAgentAppModelServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 应用ID
        :type ID: str
        :param _ModelServices: 关联的model service
        :type ModelServices: list of AgentAppModelServiceDTO
        """
        self._InstanceID = None
        self._ID = None
        self._ModelServices = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""应用ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ModelServices(self):
        r"""关联的model service
        :rtype: list of AgentAppModelServiceDTO
        """
        return self._ModelServices

    @ModelServices.setter
    def ModelServices(self, ModelServices):
        self._ModelServices = ModelServices


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        if params.get("ModelServices") is not None:
            self._ModelServices = []
            for item in params.get("ModelServices"):
                obj = AgentAppModelServiceDTO()
                obj._deserialize(item)
                self._ModelServices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentAppModelServicesResponse(AbstractModel):
    r"""ModifyAgentAppModelServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: app id
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""app id
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyAgentAppRequest(AbstractModel):
    r"""ModifyAgentApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 应用ID
        :type ID: str
        :param _Name: 名称
        :type Name: str
        :param _OAuth2ResourceServerID: OAuth2资源服务器ID
        :type OAuth2ResourceServerID: str
        :param _Description: 描述
        :type Description: str
        """
        self._InstanceID = None
        self._ID = None
        self._Name = None
        self._OAuth2ResourceServerID = None
        self._Description = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""应用ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OAuth2ResourceServerID(self):
        r"""OAuth2资源服务器ID
        :rtype: str
        """
        return self._OAuth2ResourceServerID

    @OAuth2ResourceServerID.setter
    def OAuth2ResourceServerID(self, OAuth2ResourceServerID):
        self._OAuth2ResourceServerID = OAuth2ResourceServerID

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._OAuth2ResourceServerID = params.get("OAuth2ResourceServerID")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentAppResponse(AbstractModel):
    r"""ModifyAgentApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: app id
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""app id
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyAgentCredentialRequest(AbstractModel):
    r"""ModifyAgentCredential请求参数结构体

    """


class ModifyAgentCredentialResponse(AbstractModel):
    r"""ModifyAgentCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyMcpServerRequest(AbstractModel):
    r"""ModifyMcpServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: mcp server ID
        :type ID: str
        :param _Mode: 模式：proxy代理模式； wrap封装模式；
        :type Mode: str
        :param _McpVersion: 版本号：2024-11-05 2025-03-26
        :type McpVersion: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _Name: 名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _WrapServices: 封装服务列表
        :type WrapServices: list of str
        :param _TargetSelect: 负载方式，robin random consistentHash
        :type TargetSelect: str
        :param _TargetHosts: 目标服务器
        :type TargetHosts: list of TargetHostDTO
        :param _HttpProtocolType: 后端协议：http https
        :type HttpProtocolType: str
        :param _CheckTargetCertsError: 证书检查
        :type CheckTargetCertsError: bool
        :param _TargetPath: 目标路径
        :type TargetPath: str
        :param _InvokeLimitConfigStatus: 流量控制开启状态
        :type InvokeLimitConfigStatus: bool
        :param _InvokeLimitConfig: 流量控制配置
        :type InvokeLimitConfig: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        :param _IpWhiteStatus: IP白名单开启状态
        :type IpWhiteStatus: bool
        :param _IpWhiteConfig: IP白名单配置
        :type IpWhiteConfig: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        :param _IpBlackStatus: IP黑名单开启状态
        :type IpBlackStatus: bool
        :param _IpBlackConfig: IP黑名单配置
        :type IpBlackConfig: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        :param _TargetHostType: 目标Host类型 0 默认 1 vpc
        :type TargetHostType: int
        :param _CustomHttpHost: 自定义host
        :type CustomHttpHost: str
        :param _HttpHostType: Http 请求host类型：useRequestHost 保持源请求；host targetHost 修正为源站host； customHost 自定义host
        :type HttpHostType: str
        :param _Timeout: 请求的超时时间
        :type Timeout: int
        :param _McpSecurityRules: 安全规则集
        :type McpSecurityRules: list of McpSecurityRule
        :param _ToolConfigs: 工具集配置（openapi可能会用到）
        :type ToolConfigs: list of ToolConfigDTO
        :param _WrapPaasID: 封装的API分组ID
        :type WrapPaasID: str
        :param _PluginConfigs: 插件配置
        :type PluginConfigs: list of PluginConfigDTO
        """
        self._ID = None
        self._Mode = None
        self._McpVersion = None
        self._InstanceID = None
        self._Name = None
        self._Description = None
        self._WrapServices = None
        self._TargetSelect = None
        self._TargetHosts = None
        self._HttpProtocolType = None
        self._CheckTargetCertsError = None
        self._TargetPath = None
        self._InvokeLimitConfigStatus = None
        self._InvokeLimitConfig = None
        self._IpWhiteStatus = None
        self._IpWhiteConfig = None
        self._IpBlackStatus = None
        self._IpBlackConfig = None
        self._TargetHostType = None
        self._CustomHttpHost = None
        self._HttpHostType = None
        self._Timeout = None
        self._McpSecurityRules = None
        self._ToolConfigs = None
        self._WrapPaasID = None
        self._PluginConfigs = None

    @property
    def ID(self):
        r"""mcp server ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Mode(self):
        r"""模式：proxy代理模式； wrap封装模式；
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def McpVersion(self):
        r"""版本号：2024-11-05 2025-03-26
        :rtype: str
        """
        return self._McpVersion

    @McpVersion.setter
    def McpVersion(self, McpVersion):
        self._McpVersion = McpVersion

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WrapServices(self):
        r"""封装服务列表
        :rtype: list of str
        """
        return self._WrapServices

    @WrapServices.setter
    def WrapServices(self, WrapServices):
        self._WrapServices = WrapServices

    @property
    def TargetSelect(self):
        r"""负载方式，robin random consistentHash
        :rtype: str
        """
        return self._TargetSelect

    @TargetSelect.setter
    def TargetSelect(self, TargetSelect):
        self._TargetSelect = TargetSelect

    @property
    def TargetHosts(self):
        r"""目标服务器
        :rtype: list of TargetHostDTO
        """
        return self._TargetHosts

    @TargetHosts.setter
    def TargetHosts(self, TargetHosts):
        self._TargetHosts = TargetHosts

    @property
    def HttpProtocolType(self):
        r"""后端协议：http https
        :rtype: str
        """
        return self._HttpProtocolType

    @HttpProtocolType.setter
    def HttpProtocolType(self, HttpProtocolType):
        self._HttpProtocolType = HttpProtocolType

    @property
    def CheckTargetCertsError(self):
        r"""证书检查
        :rtype: bool
        """
        return self._CheckTargetCertsError

    @CheckTargetCertsError.setter
    def CheckTargetCertsError(self, CheckTargetCertsError):
        self._CheckTargetCertsError = CheckTargetCertsError

    @property
    def TargetPath(self):
        r"""目标路径
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath

    @property
    def InvokeLimitConfigStatus(self):
        r"""流量控制开启状态
        :rtype: bool
        """
        return self._InvokeLimitConfigStatus

    @InvokeLimitConfigStatus.setter
    def InvokeLimitConfigStatus(self, InvokeLimitConfigStatus):
        self._InvokeLimitConfigStatus = InvokeLimitConfigStatus

    @property
    def InvokeLimitConfig(self):
        r"""流量控制配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        """
        return self._InvokeLimitConfig

    @InvokeLimitConfig.setter
    def InvokeLimitConfig(self, InvokeLimitConfig):
        self._InvokeLimitConfig = InvokeLimitConfig

    @property
    def IpWhiteStatus(self):
        r"""IP白名单开启状态
        :rtype: bool
        """
        return self._IpWhiteStatus

    @IpWhiteStatus.setter
    def IpWhiteStatus(self, IpWhiteStatus):
        self._IpWhiteStatus = IpWhiteStatus

    @property
    def IpWhiteConfig(self):
        r"""IP白名单配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        """
        return self._IpWhiteConfig

    @IpWhiteConfig.setter
    def IpWhiteConfig(self, IpWhiteConfig):
        self._IpWhiteConfig = IpWhiteConfig

    @property
    def IpBlackStatus(self):
        r"""IP黑名单开启状态
        :rtype: bool
        """
        return self._IpBlackStatus

    @IpBlackStatus.setter
    def IpBlackStatus(self, IpBlackStatus):
        self._IpBlackStatus = IpBlackStatus

    @property
    def IpBlackConfig(self):
        r"""IP黑名单配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.IpConfig`
        """
        return self._IpBlackConfig

    @IpBlackConfig.setter
    def IpBlackConfig(self, IpBlackConfig):
        self._IpBlackConfig = IpBlackConfig

    @property
    def TargetHostType(self):
        r"""目标Host类型 0 默认 1 vpc
        :rtype: int
        """
        return self._TargetHostType

    @TargetHostType.setter
    def TargetHostType(self, TargetHostType):
        self._TargetHostType = TargetHostType

    @property
    def CustomHttpHost(self):
        r"""自定义host
        :rtype: str
        """
        return self._CustomHttpHost

    @CustomHttpHost.setter
    def CustomHttpHost(self, CustomHttpHost):
        self._CustomHttpHost = CustomHttpHost

    @property
    def HttpHostType(self):
        r"""Http 请求host类型：useRequestHost 保持源请求；host targetHost 修正为源站host； customHost 自定义host
        :rtype: str
        """
        return self._HttpHostType

    @HttpHostType.setter
    def HttpHostType(self, HttpHostType):
        self._HttpHostType = HttpHostType

    @property
    def Timeout(self):
        r"""请求的超时时间
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def McpSecurityRules(self):
        r"""安全规则集
        :rtype: list of McpSecurityRule
        """
        return self._McpSecurityRules

    @McpSecurityRules.setter
    def McpSecurityRules(self, McpSecurityRules):
        self._McpSecurityRules = McpSecurityRules

    @property
    def ToolConfigs(self):
        r"""工具集配置（openapi可能会用到）
        :rtype: list of ToolConfigDTO
        """
        return self._ToolConfigs

    @ToolConfigs.setter
    def ToolConfigs(self, ToolConfigs):
        self._ToolConfigs = ToolConfigs

    @property
    def WrapPaasID(self):
        r"""封装的API分组ID
        :rtype: str
        """
        return self._WrapPaasID

    @WrapPaasID.setter
    def WrapPaasID(self, WrapPaasID):
        self._WrapPaasID = WrapPaasID

    @property
    def PluginConfigs(self):
        r"""插件配置
        :rtype: list of PluginConfigDTO
        """
        return self._PluginConfigs

    @PluginConfigs.setter
    def PluginConfigs(self, PluginConfigs):
        self._PluginConfigs = PluginConfigs


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Mode = params.get("Mode")
        self._McpVersion = params.get("McpVersion")
        self._InstanceID = params.get("InstanceID")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._WrapServices = params.get("WrapServices")
        self._TargetSelect = params.get("TargetSelect")
        if params.get("TargetHosts") is not None:
            self._TargetHosts = []
            for item in params.get("TargetHosts"):
                obj = TargetHostDTO()
                obj._deserialize(item)
                self._TargetHosts.append(obj)
        self._HttpProtocolType = params.get("HttpProtocolType")
        self._CheckTargetCertsError = params.get("CheckTargetCertsError")
        self._TargetPath = params.get("TargetPath")
        self._InvokeLimitConfigStatus = params.get("InvokeLimitConfigStatus")
        if params.get("InvokeLimitConfig") is not None:
            self._InvokeLimitConfig = InvokeLimitConfigDTO()
            self._InvokeLimitConfig._deserialize(params.get("InvokeLimitConfig"))
        self._IpWhiteStatus = params.get("IpWhiteStatus")
        if params.get("IpWhiteConfig") is not None:
            self._IpWhiteConfig = IpConfig()
            self._IpWhiteConfig._deserialize(params.get("IpWhiteConfig"))
        self._IpBlackStatus = params.get("IpBlackStatus")
        if params.get("IpBlackConfig") is not None:
            self._IpBlackConfig = IpConfig()
            self._IpBlackConfig._deserialize(params.get("IpBlackConfig"))
        self._TargetHostType = params.get("TargetHostType")
        self._CustomHttpHost = params.get("CustomHttpHost")
        self._HttpHostType = params.get("HttpHostType")
        self._Timeout = params.get("Timeout")
        if params.get("McpSecurityRules") is not None:
            self._McpSecurityRules = []
            for item in params.get("McpSecurityRules"):
                obj = McpSecurityRule()
                obj._deserialize(item)
                self._McpSecurityRules.append(obj)
        if params.get("ToolConfigs") is not None:
            self._ToolConfigs = []
            for item in params.get("ToolConfigs"):
                obj = ToolConfigDTO()
                obj._deserialize(item)
                self._ToolConfigs.append(obj)
        self._WrapPaasID = params.get("WrapPaasID")
        if params.get("PluginConfigs") is not None:
            self._PluginConfigs = []
            for item in params.get("PluginConfigs"):
                obj = PluginConfigDTO()
                obj._deserialize(item)
                self._PluginConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMcpServerResponse(AbstractModel):
    r"""ModifyMcpServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: mcp server ID
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""mcp server ID
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyModelRequest(AbstractModel):
    r"""ModifyModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例
        :type InstanceID: str
        :param _ID: 模型ID
        :type ID: str
        :param _Name: 模型名称
        :type Name: str
        :param _HttpProtocolType: 协议类型：http/https
        :type HttpProtocolType: str
        :param _TargetPath: 目标路径
        :type TargetPath: str
        :param _TargetHosts: 目标服务器
        :type TargetHosts: list of TargetHostDTO
        :param _CredentialID: 凭据ID
        :type CredentialID: str
        :param _CheckTargetCertsError: https时，是否检查证书合法
        :type CheckTargetCertsError: bool
        :param _HttpProtocolVersion: http协议版本：1.1/2.0
        :type HttpProtocolVersion: str
        """
        self._InstanceID = None
        self._ID = None
        self._Name = None
        self._HttpProtocolType = None
        self._TargetPath = None
        self._TargetHosts = None
        self._CredentialID = None
        self._CheckTargetCertsError = None
        self._HttpProtocolVersion = None

    @property
    def InstanceID(self):
        r"""实例
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""模型ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""模型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def HttpProtocolType(self):
        r"""协议类型：http/https
        :rtype: str
        """
        return self._HttpProtocolType

    @HttpProtocolType.setter
    def HttpProtocolType(self, HttpProtocolType):
        self._HttpProtocolType = HttpProtocolType

    @property
    def TargetPath(self):
        r"""目标路径
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath

    @property
    def TargetHosts(self):
        r"""目标服务器
        :rtype: list of TargetHostDTO
        """
        return self._TargetHosts

    @TargetHosts.setter
    def TargetHosts(self, TargetHosts):
        self._TargetHosts = TargetHosts

    @property
    def CredentialID(self):
        r"""凭据ID
        :rtype: str
        """
        return self._CredentialID

    @CredentialID.setter
    def CredentialID(self, CredentialID):
        self._CredentialID = CredentialID

    @property
    def CheckTargetCertsError(self):
        r"""https时，是否检查证书合法
        :rtype: bool
        """
        return self._CheckTargetCertsError

    @CheckTargetCertsError.setter
    def CheckTargetCertsError(self, CheckTargetCertsError):
        self._CheckTargetCertsError = CheckTargetCertsError

    @property
    def HttpProtocolVersion(self):
        r"""http协议版本：1.1/2.0
        :rtype: str
        """
        return self._HttpProtocolVersion

    @HttpProtocolVersion.setter
    def HttpProtocolVersion(self, HttpProtocolVersion):
        self._HttpProtocolVersion = HttpProtocolVersion


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._HttpProtocolType = params.get("HttpProtocolType")
        self._TargetPath = params.get("TargetPath")
        if params.get("TargetHosts") is not None:
            self._TargetHosts = []
            for item in params.get("TargetHosts"):
                obj = TargetHostDTO()
                obj._deserialize(item)
                self._TargetHosts.append(obj)
        self._CredentialID = params.get("CredentialID")
        self._CheckTargetCertsError = params.get("CheckTargetCertsError")
        self._HttpProtocolVersion = params.get("HttpProtocolVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelResponse(AbstractModel):
    r"""ModifyModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyModelServiceRequest(AbstractModel):
    r"""ModifyModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例
        :type InstanceID: str
        :param _ID: 模型服务ID
        :type ID: str
        :param _Name: 模型服务名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _TargetModels: 模板模型列表
        :type TargetModels: list of TargetModelDTO
        :param _InvokeLimitConfigStatus: 是否开启限流
        :type InvokeLimitConfigStatus: bool
        :param _InvokeLimitConfig: 限流配置
        :type InvokeLimitConfig: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        :param _TokenLimitStatus: 是否开启token控制
        :type TokenLimitStatus: bool
        :param _TokenLimitConfig: token控制
        :type TokenLimitConfig: :class:`tencentcloud.apis.v20240801.models.TokenLimitConfigDTO`
        :param _TmsStatus: 是否开启内容安全
        :type TmsStatus: bool
        :param _TmsConfig: 内容安全配置
        :type TmsConfig: :class:`tencentcloud.apis.v20240801.models.TmsConfigDTO`
        :param _IpWhiteStatus: 是否开启IP白名单
        :type IpWhiteStatus: bool
        :param _IpWhiteList: IP白名单
        :type IpWhiteList: list of str
        :param _IpBlackStatus: 是否开启IP黑名单
        :type IpBlackStatus: bool
        :param _IpBlackList: IP黑名单
        :type IpBlackList: list of str
        :param _PluginConfigs: 插件配置
        :type PluginConfigs: list of PluginConfigDTO
        :param _Timeout: 超时配置，秒
        :type Timeout: int
        """
        self._InstanceID = None
        self._ID = None
        self._Name = None
        self._Description = None
        self._TargetModels = None
        self._InvokeLimitConfigStatus = None
        self._InvokeLimitConfig = None
        self._TokenLimitStatus = None
        self._TokenLimitConfig = None
        self._TmsStatus = None
        self._TmsConfig = None
        self._IpWhiteStatus = None
        self._IpWhiteList = None
        self._IpBlackStatus = None
        self._IpBlackList = None
        self._PluginConfigs = None
        self._Timeout = None

    @property
    def InstanceID(self):
        r"""实例
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""模型服务ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""模型服务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TargetModels(self):
        r"""模板模型列表
        :rtype: list of TargetModelDTO
        """
        return self._TargetModels

    @TargetModels.setter
    def TargetModels(self, TargetModels):
        self._TargetModels = TargetModels

    @property
    def InvokeLimitConfigStatus(self):
        r"""是否开启限流
        :rtype: bool
        """
        return self._InvokeLimitConfigStatus

    @InvokeLimitConfigStatus.setter
    def InvokeLimitConfigStatus(self, InvokeLimitConfigStatus):
        self._InvokeLimitConfigStatus = InvokeLimitConfigStatus

    @property
    def InvokeLimitConfig(self):
        r"""限流配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        """
        return self._InvokeLimitConfig

    @InvokeLimitConfig.setter
    def InvokeLimitConfig(self, InvokeLimitConfig):
        self._InvokeLimitConfig = InvokeLimitConfig

    @property
    def TokenLimitStatus(self):
        r"""是否开启token控制
        :rtype: bool
        """
        return self._TokenLimitStatus

    @TokenLimitStatus.setter
    def TokenLimitStatus(self, TokenLimitStatus):
        self._TokenLimitStatus = TokenLimitStatus

    @property
    def TokenLimitConfig(self):
        r"""token控制
        :rtype: :class:`tencentcloud.apis.v20240801.models.TokenLimitConfigDTO`
        """
        return self._TokenLimitConfig

    @TokenLimitConfig.setter
    def TokenLimitConfig(self, TokenLimitConfig):
        self._TokenLimitConfig = TokenLimitConfig

    @property
    def TmsStatus(self):
        r"""是否开启内容安全
        :rtype: bool
        """
        return self._TmsStatus

    @TmsStatus.setter
    def TmsStatus(self, TmsStatus):
        self._TmsStatus = TmsStatus

    @property
    def TmsConfig(self):
        r"""内容安全配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.TmsConfigDTO`
        """
        return self._TmsConfig

    @TmsConfig.setter
    def TmsConfig(self, TmsConfig):
        self._TmsConfig = TmsConfig

    @property
    def IpWhiteStatus(self):
        r"""是否开启IP白名单
        :rtype: bool
        """
        return self._IpWhiteStatus

    @IpWhiteStatus.setter
    def IpWhiteStatus(self, IpWhiteStatus):
        self._IpWhiteStatus = IpWhiteStatus

    @property
    def IpWhiteList(self):
        r"""IP白名单
        :rtype: list of str
        """
        return self._IpWhiteList

    @IpWhiteList.setter
    def IpWhiteList(self, IpWhiteList):
        self._IpWhiteList = IpWhiteList

    @property
    def IpBlackStatus(self):
        r"""是否开启IP黑名单
        :rtype: bool
        """
        return self._IpBlackStatus

    @IpBlackStatus.setter
    def IpBlackStatus(self, IpBlackStatus):
        self._IpBlackStatus = IpBlackStatus

    @property
    def IpBlackList(self):
        r"""IP黑名单
        :rtype: list of str
        """
        return self._IpBlackList

    @IpBlackList.setter
    def IpBlackList(self, IpBlackList):
        self._IpBlackList = IpBlackList

    @property
    def PluginConfigs(self):
        r"""插件配置
        :rtype: list of PluginConfigDTO
        """
        return self._PluginConfigs

    @PluginConfigs.setter
    def PluginConfigs(self, PluginConfigs):
        self._PluginConfigs = PluginConfigs

    @property
    def Timeout(self):
        r"""超时配置，秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("TargetModels") is not None:
            self._TargetModels = []
            for item in params.get("TargetModels"):
                obj = TargetModelDTO()
                obj._deserialize(item)
                self._TargetModels.append(obj)
        self._InvokeLimitConfigStatus = params.get("InvokeLimitConfigStatus")
        if params.get("InvokeLimitConfig") is not None:
            self._InvokeLimitConfig = InvokeLimitConfigDTO()
            self._InvokeLimitConfig._deserialize(params.get("InvokeLimitConfig"))
        self._TokenLimitStatus = params.get("TokenLimitStatus")
        if params.get("TokenLimitConfig") is not None:
            self._TokenLimitConfig = TokenLimitConfigDTO()
            self._TokenLimitConfig._deserialize(params.get("TokenLimitConfig"))
        self._TmsStatus = params.get("TmsStatus")
        if params.get("TmsConfig") is not None:
            self._TmsConfig = TmsConfigDTO()
            self._TmsConfig._deserialize(params.get("TmsConfig"))
        self._IpWhiteStatus = params.get("IpWhiteStatus")
        self._IpWhiteList = params.get("IpWhiteList")
        self._IpBlackStatus = params.get("IpBlackStatus")
        self._IpBlackList = params.get("IpBlackList")
        if params.get("PluginConfigs") is not None:
            self._PluginConfigs = []
            for item in params.get("PluginConfigs"):
                obj = PluginConfigDTO()
                obj._deserialize(item)
                self._PluginConfigs.append(obj)
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelServiceResponse(AbstractModel):
    r"""ModifyModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: :class:`tencentcloud.apis.v20240801.models.ResultIDVO`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ResultIDVO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class PluginConfigDTO(AbstractModel):
    r"""PluginConfigDTO

    """

    def __init__(self):
        r"""
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: bool
        :param _PluginName: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PluginName: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _PluginID: ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PluginID: str
        :param _Level: 优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _PluginFormValues: 表单配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PluginFormValues: list of PluginFormValueDTO
        """
        self._Status = None
        self._PluginName = None
        self._Description = None
        self._PluginID = None
        self._Level = None
        self._PluginFormValues = None

    @property
    def Status(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PluginName(self):
        r"""名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PluginID(self):
        r"""ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PluginID

    @PluginID.setter
    def PluginID(self, PluginID):
        self._PluginID = PluginID

    @property
    def Level(self):
        r"""优先级
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def PluginFormValues(self):
        r"""表单配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PluginFormValueDTO
        """
        return self._PluginFormValues

    @PluginFormValues.setter
    def PluginFormValues(self, PluginFormValues):
        self._PluginFormValues = PluginFormValues


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._PluginName = params.get("PluginName")
        self._Description = params.get("Description")
        self._PluginID = params.get("PluginID")
        self._Level = params.get("Level")
        if params.get("PluginFormValues") is not None:
            self._PluginFormValues = []
            for item in params.get("PluginFormValues"):
                obj = PluginFormValueDTO()
                obj._deserialize(item)
                self._PluginFormValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginFormValueDTO(AbstractModel):
    r"""PluginFormValueDTO

    """

    def __init__(self):
        r"""
        :param _Field: 字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Field: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Field = None
        self._Value = None

    @property
    def Field(self):
        r"""字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Value(self):
        r"""值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultIDVO(AbstractModel):
    r"""ResultIDVO

    """

    def __init__(self):
        r"""
        :param _ID: 对象ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        """
        self._ID = None

    @property
    def ID(self):
        r"""对象ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultIDsVO(AbstractModel):
    r"""结果ID数组

    """

    def __init__(self):
        r"""
        :param _IDs: 结果ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :type IDs: list of str
        """
        self._IDs = None

    @property
    def IDs(self):
        r"""结果ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._IDs

    @IDs.setter
    def IDs(self, IDs):
        self._IDs = IDs


    def _deserialize(self, params):
        self._IDs = params.get("IDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartEndTime(AbstractModel):
    r"""开始结束时间结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        r"""开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetHostDTO(AbstractModel):
    r"""TargetHostDTO

    """

    def __init__(self):
        r"""
        :param _Host: 服务器
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _Rank: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Rank: int
        """
        self._Host = None
        self._Rank = None

    @property
    def Host(self):
        r"""服务器
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Rank(self):
        r"""权重
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Rank

    @Rank.setter
    def Rank(self, Rank):
        self._Rank = Rank


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Rank = params.get("Rank")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetModelDTO(AbstractModel):
    r"""模板模型

    """

    def __init__(self):
        r"""
        :param _ID: 模型ID
        :type ID: str
        :param _Name: 匹配名称
        :type Name: str
        :param _Rank: 权重
        :type Rank: int
        """
        self._ID = None
        self._Name = None
        self._Rank = None

    @property
    def ID(self):
        r"""模型ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""匹配名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rank(self):
        r"""权重
        :rtype: int
        """
        return self._Rank

    @Rank.setter
    def Rank(self, Rank):
        self._Rank = Rank


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Rank = params.get("Rank")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TmsConfigDTO(AbstractModel):
    r"""内容安全配置

    """

    def __init__(self):
        r"""
        :param _Scope: 检测范围,请求/响应
注意：此字段可能返回 null，表示取不到有效值。
        :type Scope: list of str
        :param _Mode: 检测形式
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param _Action: 执行动作
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _MergeCount: 合并请求检测event数，联动Mode字段sync
注意：此字段可能返回 null，表示取不到有效值。
        :type MergeCount: int
        :param _BizType: 风控策略
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param _InterceptMessage: 响应拦截内容
注意：此字段可能返回 null，表示取不到有效值。
        :type InterceptMessage: str
        """
        self._Scope = None
        self._Mode = None
        self._Action = None
        self._MergeCount = None
        self._BizType = None
        self._InterceptMessage = None

    @property
    def Scope(self):
        r"""检测范围,请求/响应
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Mode(self):
        r"""检测形式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Action(self):
        r"""执行动作
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def MergeCount(self):
        r"""合并请求检测event数，联动Mode字段sync
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MergeCount

    @MergeCount.setter
    def MergeCount(self, MergeCount):
        self._MergeCount = MergeCount

    @property
    def BizType(self):
        r"""风控策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def InterceptMessage(self):
        r"""响应拦截内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InterceptMessage

    @InterceptMessage.setter
    def InterceptMessage(self, InterceptMessage):
        self._InterceptMessage = InterceptMessage


    def _deserialize(self, params):
        self._Scope = params.get("Scope")
        self._Mode = params.get("Mode")
        self._Action = params.get("Action")
        self._MergeCount = params.get("MergeCount")
        self._BizType = params.get("BizType")
        self._InterceptMessage = params.get("InterceptMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenLimitConfigDTO(AbstractModel):
    r"""Token限流配置

    """

    def __init__(self):
        r"""
        :param _LimitRequestBody: 单次请求上限，k
注意：此字段可能返回 null，表示取不到有效值。
        :type LimitRequestBody: int
        :param _LimitWindows: 累次token总量消耗上限
注意：此字段可能返回 null，表示取不到有效值。
        :type LimitWindows: list of LimitWindowsDTO
        """
        self._LimitRequestBody = None
        self._LimitWindows = None

    @property
    def LimitRequestBody(self):
        r"""单次请求上限，k
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LimitRequestBody

    @LimitRequestBody.setter
    def LimitRequestBody(self, LimitRequestBody):
        self._LimitRequestBody = LimitRequestBody

    @property
    def LimitWindows(self):
        r"""累次token总量消耗上限
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LimitWindowsDTO
        """
        return self._LimitWindows

    @LimitWindows.setter
    def LimitWindows(self, LimitWindows):
        self._LimitWindows = LimitWindows


    def _deserialize(self, params):
        self._LimitRequestBody = params.get("LimitRequestBody")
        if params.get("LimitWindows") is not None:
            self._LimitWindows = []
            for item in params.get("LimitWindows"):
                obj = LimitWindowsDTO()
                obj._deserialize(item)
                self._LimitWindows.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolConfigDTO(AbstractModel):
    r"""工具级别配置

    """

    def __init__(self):
        r"""
        :param _ToolName: 工具名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolName: str
        :param _InvokeLimitConfigStatus: 是否开启限流配置
        :type InvokeLimitConfigStatus: bool
        :param _InvokeLimitConfig: 限流配置
        :type InvokeLimitConfig: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        :param _McpSecurityRules: 绑定安全规则
        :type McpSecurityRules: list of BindMcpSecurityRuleDTO
        """
        self._ToolName = None
        self._InvokeLimitConfigStatus = None
        self._InvokeLimitConfig = None
        self._McpSecurityRules = None

    @property
    def ToolName(self):
        r"""工具名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def InvokeLimitConfigStatus(self):
        r"""是否开启限流配置
        :rtype: bool
        """
        return self._InvokeLimitConfigStatus

    @InvokeLimitConfigStatus.setter
    def InvokeLimitConfigStatus(self, InvokeLimitConfigStatus):
        self._InvokeLimitConfigStatus = InvokeLimitConfigStatus

    @property
    def InvokeLimitConfig(self):
        r"""限流配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        """
        return self._InvokeLimitConfig

    @InvokeLimitConfig.setter
    def InvokeLimitConfig(self, InvokeLimitConfig):
        self._InvokeLimitConfig = InvokeLimitConfig

    @property
    def McpSecurityRules(self):
        r"""绑定安全规则
        :rtype: list of BindMcpSecurityRuleDTO
        """
        return self._McpSecurityRules

    @McpSecurityRules.setter
    def McpSecurityRules(self, McpSecurityRules):
        self._McpSecurityRules = McpSecurityRules


    def _deserialize(self, params):
        self._ToolName = params.get("ToolName")
        self._InvokeLimitConfigStatus = params.get("InvokeLimitConfigStatus")
        if params.get("InvokeLimitConfig") is not None:
            self._InvokeLimitConfig = InvokeLimitConfigDTO()
            self._InvokeLimitConfig._deserialize(params.get("InvokeLimitConfig"))
        if params.get("McpSecurityRules") is not None:
            self._McpSecurityRules = []
            for item in params.get("McpSecurityRules"):
                obj = BindMcpSecurityRuleDTO()
                obj._deserialize(item)
                self._McpSecurityRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolConfigVO(AbstractModel):
    r"""工具配置响应

    """

    def __init__(self):
        r"""
        :param _ToolName: 工具名称
        :type ToolName: str
        :param _InvokeLimitConfigStatus: 是否开启限流配置
        :type InvokeLimitConfigStatus: bool
        :param _InvokeLimitConfig: 限流配置
        :type InvokeLimitConfig: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        :param _McpSecurityRules: 绑定安全规则（响应）
        :type McpSecurityRules: list of BindMcpSecurityRuleVO
        """
        self._ToolName = None
        self._InvokeLimitConfigStatus = None
        self._InvokeLimitConfig = None
        self._McpSecurityRules = None

    @property
    def ToolName(self):
        r"""工具名称
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def InvokeLimitConfigStatus(self):
        r"""是否开启限流配置
        :rtype: bool
        """
        return self._InvokeLimitConfigStatus

    @InvokeLimitConfigStatus.setter
    def InvokeLimitConfigStatus(self, InvokeLimitConfigStatus):
        self._InvokeLimitConfigStatus = InvokeLimitConfigStatus

    @property
    def InvokeLimitConfig(self):
        r"""限流配置
        :rtype: :class:`tencentcloud.apis.v20240801.models.InvokeLimitConfigDTO`
        """
        return self._InvokeLimitConfig

    @InvokeLimitConfig.setter
    def InvokeLimitConfig(self, InvokeLimitConfig):
        self._InvokeLimitConfig = InvokeLimitConfig

    @property
    def McpSecurityRules(self):
        r"""绑定安全规则（响应）
        :rtype: list of BindMcpSecurityRuleVO
        """
        return self._McpSecurityRules

    @McpSecurityRules.setter
    def McpSecurityRules(self, McpSecurityRules):
        self._McpSecurityRules = McpSecurityRules


    def _deserialize(self, params):
        self._ToolName = params.get("ToolName")
        self._InvokeLimitConfigStatus = params.get("InvokeLimitConfigStatus")
        if params.get("InvokeLimitConfig") is not None:
            self._InvokeLimitConfig = InvokeLimitConfigDTO()
            self._InvokeLimitConfig._deserialize(params.get("InvokeLimitConfig"))
        if params.get("McpSecurityRules") is not None:
            self._McpSecurityRules = []
            for item in params.get("McpSecurityRules"):
                obj = BindMcpSecurityRuleVO()
                obj._deserialize(item)
                self._McpSecurityRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        