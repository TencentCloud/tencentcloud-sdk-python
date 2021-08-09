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
        """
        :param ClientSession: 客户端session信息，从JSSDK请求中获得\n        :type ClientSession: str\n        :param UserId: 游戏用户ID\n        :type UserId: str\n        :param GameId: 游戏ID\n        :type GameId: str\n        :param GameRegion: 【已废弃】只在TrylockWorker时生效\n        :type GameRegion: str\n        :param GameParas: 游戏参数\n        :type GameParas: str\n        :param Resolution: 分辨率,，可设置为1080p或720p或1920x1080格式\n        :type Resolution: str\n        :param ImageUrl: 背景图url，格式为png或jpeg，宽高1920*1080\n        :type ImageUrl: str\n        :param SetNo: 【已废弃】\n        :type SetNo: int\n        :param Bitrate: 单位Mbps，固定码率建议值，有一定浮动范围，后端不动态调整(MaxBitrate和MinBitrate将无效)\n        :type Bitrate: int\n        :param MaxBitrate: 单位Mbps，动态调整最大码率建议值，会按实际情况调整\n        :type MaxBitrate: int\n        :param MinBitrate: 单位Mbps，动态调整最小码率建议值，会按实际情况调整\n        :type MinBitrate: int\n        :param Fps: 帧率，可设置为30、45、60、90、120、144\n        :type Fps: int\n        :param UserIp: 【已废弃】只在TrylockWorker时生效\n        :type UserIp: str\n        :param Optimization: 【已废弃】优化项，便于客户灰度开启新的优化项，默认为0\n        :type Optimization: int\n        :param HostUserId: 【互动云游】游戏主机用户ID\n        :type HostUserId: str\n        :param Role: 【互动云游】角色；Player表示玩家；Viewer表示观察者\n        :type Role: str\n        :param GameContext: 游戏相关参数\n        :type GameContext: str\n        """
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
        """
        :param ServerSession: 服务端session信息，返回给JSSDK\n        :type ServerSession: str\n        :param RoleNumber: 【已废弃】\n        :type RoleNumber: str\n        :param Role: 【互动云游】角色；Player表示玩家；Viewer表示观察者\n        :type Role: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param GameId: 游戏ID\n        :type GameId: str\n        :param GroupId: 实例分组ID\n        :type GroupId: str\n        """
        self.GameId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.GameId = params.get("GameId")
        self.GroupId = params.get("GroupId")
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
        """
        :param Total: 客户的实例总数\n        :type Total: int\n        :param Running: 客户的实例运行数\n        :type Running: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param UserId: 游戏用户ID\n        :type UserId: str\n        :param GameId: 游戏ID\n        :type GameId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopGameRequest(AbstractModel):
    """StopGame请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 游戏用户ID\n        :type UserId: str\n        :param HostUserId: 【多人游戏】游戏主机用户ID\n        :type HostUserId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SwitchGameArchiveRequest(AbstractModel):
    """SwitchGameArchive请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 游戏用户ID\n        :type UserId: str\n        :param GameId: 游戏ID\n        :type GameId: str\n        :param GameArchiveUrl: 游戏存档Url\n        :type GameArchiveUrl: str\n        :param GameContext: 游戏相关参数\n        :type GameContext: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TrylockWorkerRequest(AbstractModel):
    """TrylockWorker请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 游戏用户ID\n        :type UserId: str\n        :param GameId: 游戏ID\n        :type GameId: str\n        :param GameRegion: 游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等，如果不为空，优先按照该区域进行调度分配机器\n        :type GameRegion: str\n        :param SetNo: 【废弃】资源池编号\n        :type SetNo: int\n        :param UserIp: 【必选】用户IP，用于就近调度，不填将严重影响用户体验\n        :type UserIp: str\n        :param GroupId: 分组ID\n        :type GroupId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")