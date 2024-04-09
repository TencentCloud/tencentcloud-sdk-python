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


class CreateSessionRequest(AbstractModel):
    """CreateSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _GameId: 【已废弃】只在TrylockWorker时生效
        :type GameId: str
        :param _GameRegion: 【已废弃】只在TrylockWorker时生效
        :type GameRegion: str
        :param _GameParas: 游戏参数
        :type GameParas: str
        :param _ClientSession: 客户端session信息，从JSSDK请求中获得。特殊的，当 RunMode 参数为 RunWithoutClient 时，该字段可以为空
        :type ClientSession: str
        :param _Resolution: 分辨率,，可设置为1080p或720p或1920x1080格式
        :type Resolution: str
        :param _ImageUrl: 背景图url，格式为png或jpeg，宽高1920*1080
        :type ImageUrl: str
        :param _SetNo: 【已废弃】
        :type SetNo: int
        :param _Bitrate: 【已废弃】
        :type Bitrate: int
        :param _MaxBitrate: 单位Mbps，动态调整最大码率建议值，会按实际情况调整
        :type MaxBitrate: int
        :param _MinBitrate: 单位Mbps，动态调整最小码率建议值，会按实际情况调整
        :type MinBitrate: int
        :param _Fps: 帧率，可设置为30、45、60、90、120、144
        :type Fps: int
        :param _UserIp: 【必选】用户IP，用户客户端的公网IP，用于就近调度，不填将严重影响用户体验
        :type UserIp: str
        :param _Optimization: 【已废弃】优化项，便于客户灰度开启新的优化项，默认为0
        :type Optimization: int
        :param _HostUserId: 【互动云游】游戏主机用户ID
        :type HostUserId: str
        :param _Role: 【互动云游】角色；Player表示玩家；Viewer表示观察者
        :type Role: str
        :param _GameContext: 游戏相关参数
        :type GameContext: str
        :param _RunMode: 云端运行模式。
RunWithoutClient：允许无客户端连接的情况下仍保持云端 App 运行
默认值（空）：要求必须有客户端连接才会保持云端 App 运行。
        :type RunMode: str
        """
        self._UserId = None
        self._GameId = None
        self._GameRegion = None
        self._GameParas = None
        self._ClientSession = None
        self._Resolution = None
        self._ImageUrl = None
        self._SetNo = None
        self._Bitrate = None
        self._MaxBitrate = None
        self._MinBitrate = None
        self._Fps = None
        self._UserIp = None
        self._Optimization = None
        self._HostUserId = None
        self._Role = None
        self._GameContext = None
        self._RunMode = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GameRegion(self):
        return self._GameRegion

    @GameRegion.setter
    def GameRegion(self, GameRegion):
        self._GameRegion = GameRegion

    @property
    def GameParas(self):
        return self._GameParas

    @GameParas.setter
    def GameParas(self, GameParas):
        self._GameParas = GameParas

    @property
    def ClientSession(self):
        return self._ClientSession

    @ClientSession.setter
    def ClientSession(self, ClientSession):
        self._ClientSession = ClientSession

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def SetNo(self):
        return self._SetNo

    @SetNo.setter
    def SetNo(self, SetNo):
        self._SetNo = SetNo

    @property
    def Bitrate(self):
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def MaxBitrate(self):
        return self._MaxBitrate

    @MaxBitrate.setter
    def MaxBitrate(self, MaxBitrate):
        self._MaxBitrate = MaxBitrate

    @property
    def MinBitrate(self):
        return self._MinBitrate

    @MinBitrate.setter
    def MinBitrate(self, MinBitrate):
        self._MinBitrate = MinBitrate

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Optimization(self):
        return self._Optimization

    @Optimization.setter
    def Optimization(self, Optimization):
        self._Optimization = Optimization

    @property
    def HostUserId(self):
        return self._HostUserId

    @HostUserId.setter
    def HostUserId(self, HostUserId):
        self._HostUserId = HostUserId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def GameContext(self):
        return self._GameContext

    @GameContext.setter
    def GameContext(self, GameContext):
        self._GameContext = GameContext

    @property
    def RunMode(self):
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._GameId = params.get("GameId")
        self._GameRegion = params.get("GameRegion")
        self._GameParas = params.get("GameParas")
        self._ClientSession = params.get("ClientSession")
        self._Resolution = params.get("Resolution")
        self._ImageUrl = params.get("ImageUrl")
        self._SetNo = params.get("SetNo")
        self._Bitrate = params.get("Bitrate")
        self._MaxBitrate = params.get("MaxBitrate")
        self._MinBitrate = params.get("MinBitrate")
        self._Fps = params.get("Fps")
        self._UserIp = params.get("UserIp")
        self._Optimization = params.get("Optimization")
        self._HostUserId = params.get("HostUserId")
        self._Role = params.get("Role")
        self._GameContext = params.get("GameContext")
        self._RunMode = params.get("RunMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSessionResponse(AbstractModel):
    """CreateSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerSession: 服务端session信息，返回给JSSDK
        :type ServerSession: str
        :param _RoleNumber: 【已废弃】
        :type RoleNumber: str
        :param _Role: 【互动云游】角色；Player表示玩家；Viewer表示观察者
        :type Role: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServerSession = None
        self._RoleNumber = None
        self._Role = None
        self._RequestId = None

    @property
    def ServerSession(self):
        return self._ServerSession

    @ServerSession.setter
    def ServerSession(self, ServerSession):
        self._ServerSession = ServerSession

    @property
    def RoleNumber(self):
        return self._RoleNumber

    @RoleNumber.setter
    def RoleNumber(self, RoleNumber):
        self._RoleNumber = RoleNumber

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServerSession = params.get("ServerSession")
        self._RoleNumber = params.get("RoleNumber")
        self._Role = params.get("Role")
        self._RequestId = params.get("RequestId")


class DescribeInstancesCountRequest(AbstractModel):
    """DescribeInstancesCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GameId: 游戏ID
        :type GameId: str
        :param _GroupId: 实例分组ID
        :type GroupId: str
        :param _GameRegion: 游戏区域
        :type GameRegion: str
        :param _GameType: 游戏类型。
MOBILE：手游
PC：默认值，端游
        :type GameType: str
        """
        self._GameId = None
        self._GroupId = None
        self._GameRegion = None
        self._GameType = None

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GameRegion(self):
        return self._GameRegion

    @GameRegion.setter
    def GameRegion(self, GameRegion):
        self._GameRegion = GameRegion

    @property
    def GameType(self):
        return self._GameType

    @GameType.setter
    def GameType(self, GameType):
        self._GameType = GameType


    def _deserialize(self, params):
        self._GameId = params.get("GameId")
        self._GroupId = params.get("GroupId")
        self._GameRegion = params.get("GameRegion")
        self._GameType = params.get("GameType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesCountResponse(AbstractModel):
    """DescribeInstancesCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 客户的实例总数
        :type Total: int
        :param _Running: 客户的实例运行数
        :type Running: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Running = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Running(self):
        return self._Running

    @Running.setter
    def Running(self, Running):
        self._Running = Running

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Running = params.get("Running")
        self._RequestId = params.get("RequestId")


class SaveGameArchiveRequest(AbstractModel):
    """SaveGameArchive请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 游戏用户ID
        :type UserId: str
        :param _GameId: 游戏ID
        :type GameId: str
        """
        self._UserId = None
        self._GameId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._GameId = params.get("GameId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveGameArchiveResponse(AbstractModel):
    """SaveGameArchive返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartPublishStreamRequest(AbstractModel):
    """StartPublishStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _PublishUrl: 推流地址，仅支持rtmp协议
        :type PublishUrl: str
        """
        self._UserId = None
        self._PublishUrl = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PublishUrl(self):
        return self._PublishUrl

    @PublishUrl.setter
    def PublishUrl(self, PublishUrl):
        self._PublishUrl = PublishUrl


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PublishUrl = params.get("PublishUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishStreamResponse(AbstractModel):
    """StartPublishStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartPublishStreamToCSSRequest(AbstractModel):
    """StartPublishStreamToCSS请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _PublishStreamArgs: 推流参数，推流时携带自定义参数。
        :type PublishStreamArgs: str
        """
        self._UserId = None
        self._PublishStreamArgs = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PublishStreamArgs(self):
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
        


class StartPublishStreamToCSSResponse(AbstractModel):
    """StartPublishStreamToCSS返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopGameRequest(AbstractModel):
    """StopGame请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _HostUserId: 【多人游戏】游戏主机用户ID
        :type HostUserId: str
        """
        self._UserId = None
        self._HostUserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def HostUserId(self):
        return self._HostUserId

    @HostUserId.setter
    def HostUserId(self, HostUserId):
        self._HostUserId = HostUserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._HostUserId = params.get("HostUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopGameResponse(AbstractModel):
    """StopGame返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopPublishStreamRequest(AbstractModel):
    """StopPublishStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
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
    """StopPublishStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SwitchGameArchiveRequest(AbstractModel):
    """SwitchGameArchive请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 游戏用户ID
        :type UserId: str
        :param _GameId: 游戏ID
        :type GameId: str
        :param _GameArchiveUrl: 游戏存档Url
        :type GameArchiveUrl: str
        :param _GameContext: 游戏相关参数
        :type GameContext: str
        """
        self._UserId = None
        self._GameId = None
        self._GameArchiveUrl = None
        self._GameContext = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GameArchiveUrl(self):
        return self._GameArchiveUrl

    @GameArchiveUrl.setter
    def GameArchiveUrl(self, GameArchiveUrl):
        self._GameArchiveUrl = GameArchiveUrl

    @property
    def GameContext(self):
        return self._GameContext

    @GameContext.setter
    def GameContext(self, GameContext):
        self._GameContext = GameContext


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._GameId = params.get("GameId")
        self._GameArchiveUrl = params.get("GameArchiveUrl")
        self._GameContext = params.get("GameContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchGameArchiveResponse(AbstractModel):
    """SwitchGameArchive返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TrylockWorkerRequest(AbstractModel):
    """TrylockWorker请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param _GameId: 游戏ID
        :type GameId: str
        :param _GameRegion: 游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等，如果不为空，优先按照该区域进行调度分配机器
        :type GameRegion: str
        :param _SetNo: 【废弃】资源池编号
        :type SetNo: int
        :param _UserIp: 【必选】用户IP，用户客户端的公网IP，用于就近调度，不填将严重影响用户体验
        :type UserIp: str
        :param _GroupId: 分组ID
        :type GroupId: str
        """
        self._UserId = None
        self._GameId = None
        self._GameRegion = None
        self._SetNo = None
        self._UserIp = None
        self._GroupId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameId(self):
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def GameRegion(self):
        return self._GameRegion

    @GameRegion.setter
    def GameRegion(self, GameRegion):
        self._GameRegion = GameRegion

    @property
    def SetNo(self):
        return self._SetNo

    @SetNo.setter
    def SetNo(self, SetNo):
        self._SetNo = SetNo

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._GameId = params.get("GameId")
        self._GameRegion = params.get("GameRegion")
        self._SetNo = params.get("SetNo")
        self._UserIp = params.get("UserIp")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrylockWorkerResponse(AbstractModel):
    """TrylockWorker返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")