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
        :param ClientSession: 客户端session信息，从JSSDK请求中获得
        :type ClientSession: str
        :param UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param GameId: 游戏ID
        :type GameId: str
        :param GameRegion: 【已废弃】只在TrylockWorker时生效
        :type GameRegion: str
        :param GameParas: 游戏参数
        :type GameParas: str
        :param Resolution: 分辨率,，可设置为1080p或720p或1920x1080格式
        :type Resolution: str
        :param ImageUrl: 背景图url，格式为png或jpeg，宽高1920*1080
        :type ImageUrl: str
        :param SetNo: 【已废弃】
        :type SetNo: int
        :param Bitrate: 单位Mbps，固定码率建议值，有一定浮动范围，后端不动态调整(MaxBitrate和MinBitrate将无效)
        :type Bitrate: int
        :param MaxBitrate: 单位Mbps，动态调整最大码率建议值，会按实际情况调整
        :type MaxBitrate: int
        :param MinBitrate: 单位Mbps，动态调整最小码率建议值，会按实际情况调整
        :type MinBitrate: int
        :param Fps: 帧率，可设置为30、45、60、90、120、144
        :type Fps: int
        :param UserIp: 【必选】用户IP，用户客户端的公网IP，用于就近调度，不填将严重影响用户体验
        :type UserIp: str
        :param Optimization: 【已废弃】优化项，便于客户灰度开启新的优化项，默认为0
        :type Optimization: int
        :param HostUserId: 【互动云游】游戏主机用户ID
        :type HostUserId: str
        :param Role: 【互动云游】角色；Player表示玩家；Viewer表示观察者
        :type Role: str
        :param GameContext: 游戏相关参数
        :type GameContext: str
        :param RunMode: 云端运行模式。
RunWithoutClient：允许无客户端连接的情况下仍保持云端 App 运行
默认值（空）：要求必须有客户端连接才会保持云端 App 运行。
        :type RunMode: str
        """
        self.ClientSession = None
        self.UserId = None
        self.GameId = None
        self.GameRegion = None
        self.GameParas = None
        self.Resolution = None
        self.ImageUrl = None
        self.SetNo = None
        self.Bitrate = None
        self.MaxBitrate = None
        self.MinBitrate = None
        self.Fps = None
        self.UserIp = None
        self.Optimization = None
        self.HostUserId = None
        self.Role = None
        self.GameContext = None
        self.RunMode = None


    def _deserialize(self, params):
        self.ClientSession = params.get("ClientSession")
        self.UserId = params.get("UserId")
        self.GameId = params.get("GameId")
        self.GameRegion = params.get("GameRegion")
        self.GameParas = params.get("GameParas")
        self.Resolution = params.get("Resolution")
        self.ImageUrl = params.get("ImageUrl")
        self.SetNo = params.get("SetNo")
        self.Bitrate = params.get("Bitrate")
        self.MaxBitrate = params.get("MaxBitrate")
        self.MinBitrate = params.get("MinBitrate")
        self.Fps = params.get("Fps")
        self.UserIp = params.get("UserIp")
        self.Optimization = params.get("Optimization")
        self.HostUserId = params.get("HostUserId")
        self.Role = params.get("Role")
        self.GameContext = params.get("GameContext")
        self.RunMode = params.get("RunMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSessionResponse(AbstractModel):
    """CreateSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServerSession: 服务端session信息，返回给JSSDK
        :type ServerSession: str
        :param RoleNumber: 【已废弃】
        :type RoleNumber: str
        :param Role: 【互动云游】角色；Player表示玩家；Viewer表示观察者
        :type Role: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServerSession = None
        self.RoleNumber = None
        self.Role = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServerSession = params.get("ServerSession")
        self.RoleNumber = params.get("RoleNumber")
        self.Role = params.get("Role")
        self.RequestId = params.get("RequestId")


class DescribeInstancesCountRequest(AbstractModel):
    """DescribeInstancesCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param GameId: 游戏ID
        :type GameId: str
        :param GroupId: 实例分组ID
        :type GroupId: str
        :param GameRegion: 游戏区域
        :type GameRegion: str
        :param GameType: 游戏类型。
MOBILE：手游
PC：默认值，端游
        :type GameType: str
        """
        self.GameId = None
        self.GroupId = None
        self.GameRegion = None
        self.GameType = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.GroupId = params.get("GroupId")
        self.GameRegion = params.get("GameRegion")
        self.GameType = params.get("GameType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesCountResponse(AbstractModel):
    """DescribeInstancesCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 客户的实例总数
        :type Total: int
        :param Running: 客户的实例运行数
        :type Running: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Running = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Running = params.get("Running")
        self.RequestId = params.get("RequestId")


class SaveGameArchiveRequest(AbstractModel):
    """SaveGameArchive请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 游戏用户ID
        :type UserId: str
        :param GameId: 游戏ID
        :type GameId: str
        """
        self.UserId = None
        self.GameId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.GameId = params.get("GameId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveGameArchiveResponse(AbstractModel):
    """SaveGameArchive返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartPublishStreamRequest(AbstractModel):
    """StartPublishStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param PublishUrl: 推流地址，仅支持rtmp协议
        :type PublishUrl: str
        """
        self.UserId = None
        self.PublishUrl = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.PublishUrl = params.get("PublishUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishStreamResponse(AbstractModel):
    """StartPublishStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopGameRequest(AbstractModel):
    """StopGame请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param HostUserId: 【多人游戏】游戏主机用户ID
        :type HostUserId: str
        """
        self.UserId = None
        self.HostUserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.HostUserId = params.get("HostUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopGameResponse(AbstractModel):
    """StopGame返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopPublishStreamRequest(AbstractModel):
    """StopPublishStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopPublishStreamResponse(AbstractModel):
    """StopPublishStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SwitchGameArchiveRequest(AbstractModel):
    """SwitchGameArchive请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 游戏用户ID
        :type UserId: str
        :param GameId: 游戏ID
        :type GameId: str
        :param GameArchiveUrl: 游戏存档Url
        :type GameArchiveUrl: str
        :param GameContext: 游戏相关参数
        :type GameContext: str
        """
        self.UserId = None
        self.GameId = None
        self.GameArchiveUrl = None
        self.GameContext = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.GameId = params.get("GameId")
        self.GameArchiveUrl = params.get("GameArchiveUrl")
        self.GameContext = params.get("GameContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchGameArchiveResponse(AbstractModel):
    """SwitchGameArchive返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TrylockWorkerRequest(AbstractModel):
    """TrylockWorker请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 唯一用户身份标识，由业务方自定义，平台不予理解。（可根据业务需要决定使用用户的唯一身份标识或是使用时间戳随机生成；在用户重连时应保持UserId不变）
        :type UserId: str
        :param GameId: 游戏ID
        :type GameId: str
        :param GameRegion: 游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等，如果不为空，优先按照该区域进行调度分配机器
        :type GameRegion: str
        :param SetNo: 【废弃】资源池编号
        :type SetNo: int
        :param UserIp: 【必选】用户IP，用户客户端的公网IP，用于就近调度，不填将严重影响用户体验
        :type UserIp: str
        :param GroupId: 分组ID
        :type GroupId: str
        """
        self.UserId = None
        self.GameId = None
        self.GameRegion = None
        self.SetNo = None
        self.UserIp = None
        self.GroupId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.GameId = params.get("GameId")
        self.GameRegion = params.get("GameRegion")
        self.SetNo = params.get("SetNo")
        self.UserIp = params.get("UserIp")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrylockWorkerResponse(AbstractModel):
    """TrylockWorker返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")