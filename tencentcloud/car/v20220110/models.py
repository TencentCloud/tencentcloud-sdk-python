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


class ApplyConcurrentRequest(AbstractModel):
    r"""ApplyConcurrent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _UserIp: 用户IP，用户客户端的公网IP，用于就近调度
        :type UserIp: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ApplicationVersionId: 应用版本ID。如果请求应用的当前版本，可以不用填写该字段。如果请求应用的其它版本时，才需要通过该字段来指定应用的版本。
        :type ApplicationVersionId: str
        :param _ApplicationId: 应用ID。如果是独享项目，将忽略该参数，使用项目绑定的应用。如果是共享项目，使用该参数来指定应用。
        :type ApplicationId: str
        """
        self._UserId = None
        self._UserIp = None
        self._ProjectId = None
        self._ApplicationVersionId = None
        self._ApplicationId = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserIp(self):
        r"""用户IP，用户客户端的公网IP，用于就近调度
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ApplicationVersionId(self):
        r"""应用版本ID。如果请求应用的当前版本，可以不用填写该字段。如果请求应用的其它版本时，才需要通过该字段来指定应用的版本。
        :rtype: str
        """
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId

    @property
    def ApplicationId(self):
        r"""应用ID。如果是独享项目，将忽略该参数，使用项目绑定的应用。如果是共享项目，使用该参数来指定应用。
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserIp = params.get("UserIp")
        self._ProjectId = params.get("ProjectId")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConcurrentResponse(AbstractModel):
    r"""ApplyConcurrent返回参数结构体

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


class CreateMCPTokenRequest(AbstractModel):
    r"""CreateMCPToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExpireSeconds: <p>Token 过期时间</p><p>取值范围：[0, 2592000]</p><p>单位：秒</p><p>默认值：86400</p><p>不填的话，默认为 1 天超时；过期时间为当前时间 + 超时时间</p>
        :type ExpireSeconds: int
        :param _TokenName: <p>Token 名称（注释）</p><p>参数格式：只支持：中英文、数字、连字符 &quot;-&quot; 的组合</p><p>长度不得超过 16 个字符</p>
        :type TokenName: str
        :param _UserId: <p>用户 Id</p><p>参数格式：只支持：字母（A-Za-z）、数字（0-9）、下划线（_）的组合</p><p>固定使用这个 UserId  来操作云渲染并发资源，长度不能超过 64 个字符</p>
        :type UserId: str
        """
        self._ExpireSeconds = None
        self._TokenName = None
        self._UserId = None

    @property
    def ExpireSeconds(self):
        r"""<p>Token 过期时间</p><p>取值范围：[0, 2592000]</p><p>单位：秒</p><p>默认值：86400</p><p>不填的话，默认为 1 天超时；过期时间为当前时间 + 超时时间</p>
        :rtype: int
        """
        return self._ExpireSeconds

    @ExpireSeconds.setter
    def ExpireSeconds(self, ExpireSeconds):
        self._ExpireSeconds = ExpireSeconds

    @property
    def TokenName(self):
        r"""<p>Token 名称（注释）</p><p>参数格式：只支持：中英文、数字、连字符 &quot;-&quot; 的组合</p><p>长度不得超过 16 个字符</p>
        :rtype: str
        """
        return self._TokenName

    @TokenName.setter
    def TokenName(self, TokenName):
        self._TokenName = TokenName

    @property
    def UserId(self):
        r"""<p>用户 Id</p><p>参数格式：只支持：字母（A-Za-z）、数字（0-9）、下划线（_）的组合</p><p>固定使用这个 UserId  来操作云渲染并发资源，长度不能超过 64 个字符</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ExpireSeconds = params.get("ExpireSeconds")
        self._TokenName = params.get("TokenName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMCPTokenResponse(AbstractModel):
    r"""CreateMCPToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TokenId: <p>TokenId</p>
        :type TokenId: str
        :param _Token: <p>MCP Token </p><p>当前值请妥善保存，后续需要使用该 Token 和 MCP Server 进行通信操作，丢失后无法再查看</p>
        :type Token: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TokenId = None
        self._Token = None
        self._RequestId = None

    @property
    def TokenId(self):
        r"""<p>TokenId</p>
        :rtype: str
        """
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def Token(self):
        r"""<p>MCP Token </p><p>当前值请妥善保存，后续需要使用该 Token 和 MCP Server 进行通信操作，丢失后无法再查看</p>
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

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
        self._TokenId = params.get("TokenId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class CreateSessionRequest(AbstractModel):
    r"""CreateSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _UserIp: 用户IP，用户客户端的公网IP，用于就近调度
        :type UserIp: str
        :param _ClientSession: 客户端session信息，从SDK请求中获得。特殊的，当 RunMode 参数为 RunWithoutClient 时，该字段可以为空
        :type ClientSession: str
        :param _RunMode: 云端运行模式。
RunWithoutClient：允许无客户端连接的情况下仍保持云端 App 运行
默认值（空）：要求必须有客户端连接才会保持云端 App 运行。
        :type RunMode: str
        :param _ApplicationParameters: 应用启动参数。
如果请求的是多应用共享项目，此参数生效；
如果请求的是关闭预启动的单应用独享项目，此参数生效；
如果请求的是开启预启动的单应用独享项目，此参数失效。

注意：在此参数生效的情况下，将会被追加到控制台应用或项目配置的启动参数的后面。
例如，对于某关闭预启动的单应用独享项目，若在控制台中项目配置的启动参数为bar=0，而ApplicationParameters参数为foo=1，则实际应用启动参数为bar=0 foo=1。
        :type ApplicationParameters: str
        :param _HostUserId: 【多人互动】房主用户ID，在多人互动模式下为必填字段。
如果该用户是房主，HostUserId需要和UserId保持一致；
如果该用户非房主，HostUserId需要填写房主的HostUserId。
        :type HostUserId: str
        :param _Role: 【多人互动】角色。
Player：玩家（可通过键鼠等操作应用）
Viewer：观察者（只能观看，无法操作）
        :type Role: str
        """
        self._UserId = None
        self._UserIp = None
        self._ClientSession = None
        self._RunMode = None
        self._ApplicationParameters = None
        self._HostUserId = None
        self._Role = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserIp(self):
        r"""用户IP，用户客户端的公网IP，用于就近调度
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def ClientSession(self):
        r"""客户端session信息，从SDK请求中获得。特殊的，当 RunMode 参数为 RunWithoutClient 时，该字段可以为空
        :rtype: str
        """
        return self._ClientSession

    @ClientSession.setter
    def ClientSession(self, ClientSession):
        self._ClientSession = ClientSession

    @property
    def RunMode(self):
        r"""云端运行模式。
RunWithoutClient：允许无客户端连接的情况下仍保持云端 App 运行
默认值（空）：要求必须有客户端连接才会保持云端 App 运行。
        :rtype: str
        """
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ApplicationParameters(self):
        r"""应用启动参数。
如果请求的是多应用共享项目，此参数生效；
如果请求的是关闭预启动的单应用独享项目，此参数生效；
如果请求的是开启预启动的单应用独享项目，此参数失效。

注意：在此参数生效的情况下，将会被追加到控制台应用或项目配置的启动参数的后面。
例如，对于某关闭预启动的单应用独享项目，若在控制台中项目配置的启动参数为bar=0，而ApplicationParameters参数为foo=1，则实际应用启动参数为bar=0 foo=1。
        :rtype: str
        """
        return self._ApplicationParameters

    @ApplicationParameters.setter
    def ApplicationParameters(self, ApplicationParameters):
        self._ApplicationParameters = ApplicationParameters

    @property
    def HostUserId(self):
        r"""【多人互动】房主用户ID，在多人互动模式下为必填字段。
如果该用户是房主，HostUserId需要和UserId保持一致；
如果该用户非房主，HostUserId需要填写房主的HostUserId。
        :rtype: str
        """
        return self._HostUserId

    @HostUserId.setter
    def HostUserId(self, HostUserId):
        self._HostUserId = HostUserId

    @property
    def Role(self):
        r"""【多人互动】角色。
Player：玩家（可通过键鼠等操作应用）
Viewer：观察者（只能观看，无法操作）
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserIp = params.get("UserIp")
        self._ClientSession = params.get("ClientSession")
        self._RunMode = params.get("RunMode")
        self._ApplicationParameters = params.get("ApplicationParameters")
        self._HostUserId = params.get("HostUserId")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSessionResponse(AbstractModel):
    r"""CreateSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerSession: 服务端session信息，返回给SDK
        :type ServerSession: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServerSession = None
        self._RequestId = None

    @property
    def ServerSession(self):
        r"""服务端session信息，返回给SDK
        :rtype: str
        """
        return self._ServerSession

    @ServerSession.setter
    def ServerSession(self, ServerSession):
        self._ServerSession = ServerSession

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
        self._ServerSession = params.get("ServerSession")
        self._RequestId = params.get("RequestId")


class DescribeConcurrentCountRequest(AbstractModel):
    r"""DescribeConcurrentCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ApplicationCategory: 应用类别（DESKTOP: 桌面端，MOBILE：移动端）
        :type ApplicationCategory: str
        """
        self._ProjectId = None
        self._ApplicationCategory = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ApplicationCategory(self):
        r"""应用类别（DESKTOP: 桌面端，MOBILE：移动端）
        :rtype: str
        """
        return self._ApplicationCategory

    @ApplicationCategory.setter
    def ApplicationCategory(self, ApplicationCategory):
        self._ApplicationCategory = ApplicationCategory


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ApplicationCategory = params.get("ApplicationCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConcurrentCountResponse(AbstractModel):
    r"""DescribeConcurrentCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 并发总数
        :type Total: int
        :param _Running: 并发运行数，包括预启动中的、已连接的、等待重连、清理恢复等所有非空闲的并发数，所以刷新项目或断开并发包的用户连接，都会影响到该值
        :type Running: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Running = None
        self._RequestId = None

    @property
    def Total(self):
        r"""并发总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Running(self):
        r"""并发运行数，包括预启动中的、已连接的、等待重连、清理恢复等所有非空闲的并发数，所以刷新项目或断开并发包的用户连接，都会影响到该值
        :rtype: int
        """
        return self._Running

    @Running.setter
    def Running(self, Running):
        self._Running = Running

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
        self._Total = params.get("Total")
        self._Running = params.get("Running")
        self._RequestId = params.get("RequestId")


class DescribeMCPTokensRequest(AbstractModel):
    r"""DescribeMCPTokens请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: <p>偏移量</p>
        :type Offset: int
        :param _Limit: <p>单页数量</p><p>取值范围：[0, 200]</p><p>默认值：20</p><p>如果传入 0 会使用默认值</p>
        :type Limit: int
        :param _Filters: <p>过滤器列表</p><p>只支持 TokenId 和 TokenName 过滤，Filters 数量不能超过 10、每个 Filter 的 Values 个数不能超过 20、单个 Value 长度不能超过 64 个字符、不允许同名 Filter 出现</p>
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""<p>偏移量</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>单页数量</p><p>取值范围：[0, 200]</p><p>默认值：20</p><p>如果传入 0 会使用默认值</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>过滤器列表</p><p>只支持 TokenId 和 TokenName 过滤，Filters 数量不能超过 10、每个 Filter 的 Values 个数不能超过 20、单个 Value 长度不能超过 64 个字符、不允许同名 Filter 出现</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMCPTokensResponse(AbstractModel):
    r"""DescribeMCPTokens返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tokens: <p>Token 列表</p>
        :type Tokens: list of MCPTokenInfo
        :param _TotalCount: <p>Token 数量</p><p>单位：个</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tokens = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Tokens(self):
        r"""<p>Token 列表</p>
        :rtype: list of MCPTokenInfo
        """
        return self._Tokens

    @Tokens.setter
    def Tokens(self, Tokens):
        self._Tokens = Tokens

    @property
    def TotalCount(self):
        r"""<p>Token 数量</p><p>单位：个</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Tokens") is not None:
            self._Tokens = []
            for item in params.get("Tokens"):
                obj = MCPTokenInfo()
                obj._deserialize(item)
                self._Tokens.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DestroySessionRequest(AbstractModel):
    r"""DestroySession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroySessionResponse(AbstractModel):
    r"""DestroySession返回参数结构体

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


class Filter(AbstractModel):
    r"""查询过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段名（ApplicationId 应用Id、ApplicationName 应用名称、ApplicationRunStatus 运行状态、ApplicationUpdateStatus 更新状态）
        :type Name: str
        :param _Values: 过滤值集合（当过滤 Name 为 ApplicationRunStatus 时，Values 取值为 [ApplicationDeleting 应用删除中、ApplicationCreateFail 应用创建失败、ApplicationCreating 应用创建中、ApplicationRunning 正常运行、ApplicationNoConfigured 主执行程序路径未配置 ]。当过滤 Name 为 ApplicationUpdateStatus 时，Values 取值 [ApplicationUpdateCreating 版本创建中、ApplicationUpdateCreateFail 版本创建失败、ApplicationUpdateNoReleased 版本待发布、ApplicationUpdateReleased 版本发布完成、ApplicationUpdateNormal 无]）
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""过滤字段名（ApplicationId 应用Id、ApplicationName 应用名称、ApplicationRunStatus 运行状态、ApplicationUpdateStatus 更新状态）
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""过滤值集合（当过滤 Name 为 ApplicationRunStatus 时，Values 取值为 [ApplicationDeleting 应用删除中、ApplicationCreateFail 应用创建失败、ApplicationCreating 应用创建中、ApplicationRunning 正常运行、ApplicationNoConfigured 主执行程序路径未配置 ]。当过滤 Name 为 ApplicationUpdateStatus 时，Values 取值 [ApplicationUpdateCreating 版本创建中、ApplicationUpdateCreateFail 版本创建失败、ApplicationUpdateNoReleased 版本待发布、ApplicationUpdateReleased 版本发布完成、ApplicationUpdateNormal 无]）
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MCPTokenInfo(AbstractModel):
    r"""MCP Token 信息

    """

    def __init__(self):
        r"""
        :param _TokenId: <p>TokenId</p><p>用于管理 Token 数据，可用来延长对应 Token 有效时间</p>
        :type TokenId: str
        :param _TokenName: <p>Token 名称（注释）</p>
        :type TokenName: str
        :param _UserId: <p>用户 Id</p><p>固定使用这个 UserId  来操作云渲染并发资源（为空不限制）</p>
        :type UserId: str
        :param _Scopes: <p>权限范围</p><p>默认值：[&quot;*&quot;]</p><p>用于指定操作权限，默认拥有全部权限</p>
        :type Scopes: list of str
        :param _Status: <p>Token 状态</p><p>枚举值：</p><ul><li>ACTIVE： 正常状态，未被吊销。不代表还在有效期内</li><li>REVOKED： 已被吊销，永久失效</li></ul><p>默认值：ACTIVE</p>
        :type Status: str
        :param _CreatedTime: <p>Token 创建时间</p>
        :type CreatedTime: str
        :param _ExpiresTime: <p>Token 过期时间</p>
        :type ExpiresTime: str
        """
        self._TokenId = None
        self._TokenName = None
        self._UserId = None
        self._Scopes = None
        self._Status = None
        self._CreatedTime = None
        self._ExpiresTime = None

    @property
    def TokenId(self):
        r"""<p>TokenId</p><p>用于管理 Token 数据，可用来延长对应 Token 有效时间</p>
        :rtype: str
        """
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def TokenName(self):
        r"""<p>Token 名称（注释）</p>
        :rtype: str
        """
        return self._TokenName

    @TokenName.setter
    def TokenName(self, TokenName):
        self._TokenName = TokenName

    @property
    def UserId(self):
        r"""<p>用户 Id</p><p>固定使用这个 UserId  来操作云渲染并发资源（为空不限制）</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Scopes(self):
        r"""<p>权限范围</p><p>默认值：[&quot;*&quot;]</p><p>用于指定操作权限，默认拥有全部权限</p>
        :rtype: list of str
        """
        return self._Scopes

    @Scopes.setter
    def Scopes(self, Scopes):
        self._Scopes = Scopes

    @property
    def Status(self):
        r"""<p>Token 状态</p><p>枚举值：</p><ul><li>ACTIVE： 正常状态，未被吊销。不代表还在有效期内</li><li>REVOKED： 已被吊销，永久失效</li></ul><p>默认值：ACTIVE</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        r"""<p>Token 创建时间</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiresTime(self):
        r"""<p>Token 过期时间</p>
        :rtype: str
        """
        return self._ExpiresTime

    @ExpiresTime.setter
    def ExpiresTime(self, ExpiresTime):
        self._ExpiresTime = ExpiresTime


    def _deserialize(self, params):
        self._TokenId = params.get("TokenId")
        self._TokenName = params.get("TokenName")
        self._UserId = params.get("UserId")
        self._Scopes = params.get("Scopes")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiresTime = params.get("ExpiresTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewMCPTokenRequest(AbstractModel):
    r"""RenewMCPToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TokenId: <p>TokenId</p>
        :type TokenId: str
        :param _ExpireSeconds: <p>Token 过期时间</p><p>取值范围：[0, 2592000]</p><p>默认值：86400</p><p>单位 秒、不填的话，默认为 1 天；新的超时时间为，当前时刻 + ExpireSeconds</p>
        :type ExpireSeconds: int
        """
        self._TokenId = None
        self._ExpireSeconds = None

    @property
    def TokenId(self):
        r"""<p>TokenId</p>
        :rtype: str
        """
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def ExpireSeconds(self):
        r"""<p>Token 过期时间</p><p>取值范围：[0, 2592000]</p><p>默认值：86400</p><p>单位 秒、不填的话，默认为 1 天；新的超时时间为，当前时刻 + ExpireSeconds</p>
        :rtype: int
        """
        return self._ExpireSeconds

    @ExpireSeconds.setter
    def ExpireSeconds(self, ExpireSeconds):
        self._ExpireSeconds = ExpireSeconds


    def _deserialize(self, params):
        self._TokenId = params.get("TokenId")
        self._ExpireSeconds = params.get("ExpireSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewMCPTokenResponse(AbstractModel):
    r"""RenewMCPToken返回参数结构体

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


class StartPublishStreamRequest(AbstractModel):
    r"""StartPublishStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（UserId将作为StreamId进行推流，比如绑定推流域名为abc.livepush.myqcloud.com，那么推流地址为rtmp://abc.livepush.myqcloud.com/live/UserId?txSecret=xxx&txTime=xxx）
        :type UserId: str
        :param _PublishStreamArgs: 推流参数，推流时携带自定义参数。
        :type PublishStreamArgs: str
        """
        self._UserId = None
        self._PublishStreamArgs = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（UserId将作为StreamId进行推流，比如绑定推流域名为abc.livepush.myqcloud.com，那么推流地址为rtmp://abc.livepush.myqcloud.com/live/UserId?txSecret=xxx&txTime=xxx）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PublishStreamArgs(self):
        r"""推流参数，推流时携带自定义参数。
        :rtype: str
        """
        return self._PublishStreamArgs

    @PublishStreamArgs.setter
    def PublishStreamArgs(self, PublishStreamArgs):
        self._PublishStreamArgs = PublishStreamArgs


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PublishStreamArgs = params.get("PublishStreamArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishStreamResponse(AbstractModel):
    r"""StartPublishStream返回参数结构体

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


class StartPublishStreamWithURLRequest(AbstractModel):
    r"""StartPublishStreamWithURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。
        :type UserId: str
        :param _PublishStreamURL: 推流地址，仅支持rtmp协议。
        :type PublishStreamURL: str
        """
        self._UserId = None
        self._PublishStreamURL = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PublishStreamURL(self):
        r"""推流地址，仅支持rtmp协议。
        :rtype: str
        """
        return self._PublishStreamURL

    @PublishStreamURL.setter
    def PublishStreamURL(self, PublishStreamURL):
        self._PublishStreamURL = PublishStreamURL


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PublishStreamURL = params.get("PublishStreamURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishStreamWithURLResponse(AbstractModel):
    r"""StartPublishStreamWithURL返回参数结构体

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


class StopPublishStreamRequest(AbstractModel):
    r"""StopPublishStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        r"""唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopPublishStreamResponse(AbstractModel):
    r"""StopPublishStream返回参数结构体

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