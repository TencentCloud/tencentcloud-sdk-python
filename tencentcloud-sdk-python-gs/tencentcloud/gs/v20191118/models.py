# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class CreateSessionRequest(AbstractModel):
    """CreateSession请求参数结构体

    """

    def __init__(self):
        """
        :param ClientSession: 客户端session信息，从JSSDK请求中获得
        :type ClientSession: str
        :param UserId: 游戏用户ID
        :type UserId: str
        :param GameId: 游戏ID
        :type GameId: str
        :param GameRegion: 游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等
        :type GameRegion: str
        :param GameParas: 游戏参数
        :type GameParas: str
        :param Resolution: 分辨率,，可设置为1080p或720p
        :type Resolution: str
        :param ImageUrl: 背景图url，格式为png或jpeg，宽高1920*1080
        :type ImageUrl: str
        :param SetNo: 资源池编号，1表示正式，2表示测试
        :type SetNo: int
        :param Bitrate: 单位Mbps，固定码率，后端不动态调整(MaxBitrate和MinBitrate将无效)
        :type Bitrate: int
        :param MaxBitrate: 单位Mbps，动态调整最大码率
        :type MaxBitrate: int
        :param MinBitrate: 单位Mbps，动态调整最小码率
        :type MinBitrate: int
        :param Fps: 帧率，可设置为30、45或60
        :type Fps: int
        :param UserIp: 游戏用户IP，用于就近调度，例如125.127.178.228
        :type UserIp: str
        :param Optimization: 优化项，便于客户灰度开启新的优化项，默认为0
        :type Optimization: int
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


class CreateSessionResponse(AbstractModel):
    """CreateSession返回参数结构体

    """

    def __init__(self):
        """
        :param ServerSession: 服务端session信息，返回给JSSDK
        :type ServerSession: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServerSession = params.get("ServerSession")
        self.RequestId = params.get("RequestId")


class StopGameRequest(AbstractModel):
    """StopGame请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 游戏用户ID
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")


class StopGameResponse(AbstractModel):
    """StopGame返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param UserId: 游戏用户ID
        :type UserId: str
        :param GameId: 游戏ID
        :type GameId: str
        :param GameRegion: 游戏区域，ap-guangzhou、ap-shanghai、ap-beijing等
        :type GameRegion: str
        :param SetNo: 资源池编号，1表示共用，2表示测试
        :type SetNo: int
        :param UserIp: 游戏用户IP，用于就近调度，例如125.127.178.228
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


class TrylockWorkerResponse(AbstractModel):
    """TrylockWorker返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")