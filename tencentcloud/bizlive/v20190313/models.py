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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class CreateSessionRequest(AbstractModel):
    """CreateSession请求参数结构体

    """

    def __init__(self):
        """
        :param ClientSession: 客户端session信息，从JSSDK请求中获得
        :type ClientSession: str
        :param GameId: 游戏ID
        :type GameId: str
        :param UserId: 游戏用户ID
        :type UserId: str
        :param GameParas: 游戏参数
        :type GameParas: str
        :param GameRegion: 游戏区域
        :type GameRegion: str
        :param ImageUrl: 背景图url
        :type ImageUrl: str
        :param Resolution: 分辨率
        :type Resolution: str
        """
        self.ClientSession = None
        self.GameId = None
        self.UserId = None
        self.GameParas = None
        self.GameRegion = None
        self.ImageUrl = None
        self.Resolution = None


    def _deserialize(self, params):
        self.ClientSession = params.get("ClientSession")
        self.GameId = params.get("GameId")
        self.UserId = params.get("UserId")
        self.GameParas = params.get("GameParas")
        self.GameRegion = params.get("GameRegion")
        self.ImageUrl = params.get("ImageUrl")
        self.Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DayStreamPlayInfo(AbstractModel):
    """流播放信息

    """

    def __init__(self):
        """
        :param Bandwidth: 带宽（单位Mbps）。
        :type Bandwidth: float
        :param Flux: 流量 （单位MB）。
        :type Flux: float
        :param Online: 在线人数。
        :type Online: int
        :param Request: 请求数。
        :type Request: int
        :param Time: 数据时间点，格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        """
        self.Bandwidth = None
        self.Flux = None
        self.Online = None
        self.Request = None
        self.Time = None


    def _deserialize(self, params):
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Online = params.get("Online")
        self.Request = params.get("Request")
        self.Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeStreamPlayInfoListRequest(AbstractModel):
    """DescribeStreamPlayInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param EndTime: 结束时间，北京时间，格式：2019-04-28 10:36:00
结束时间 和 开始时间  必须在同一天内。
        :type EndTime: str
        :param PlayDomain: 播放域名。
        :type PlayDomain: str
        :param StartTime: 开始时间，北京时间，格式：2019-04-28 10:36:00
当前时间 和 开始时间 间隔不超过30天。
        :type StartTime: str
        :param StreamName: 流名称，精确匹配。
若不填，则为查询总体播放数据。
        :type StreamName: str
        """
        self.EndTime = None
        self.PlayDomain = None
        self.StartTime = None
        self.StreamName = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.PlayDomain = params.get("PlayDomain")
        self.StartTime = params.get("StartTime")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeStreamPlayInfoListResponse(AbstractModel):
    """DescribeStreamPlayInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 统计信息列表。
        :type DataInfoList: list of DayStreamPlayInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = DayStreamPlayInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeWorkersRequest(AbstractModel):
    """DescribeWorkers请求参数结构体

    """


class DescribeWorkersResponse(AbstractModel):
    """DescribeWorkers返回参数结构体

    """

    def __init__(self):
        """
        :param RegionDetail: 各个区域的机器情况
        :type RegionDetail: list of WorkerRegionInfo
        :param Idle: 空闲机器总数量
        :type Idle: int
        :param RegionNum: 区域个数
        :type RegionNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionDetail = None
        self.Idle = None
        self.RegionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionDetail") is not None:
            self.RegionDetail = []
            for item in params.get("RegionDetail"):
                obj = WorkerRegionInfo()
                obj._deserialize(item)
                self.RegionDetail.append(obj)
        self.Idle = params.get("Idle")
        self.RegionNum = params.get("RegionNum")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的推流域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param ResumeTime: 恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：默认禁播90天，且最长支持禁播90天。
        :type ResumeTime: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.ResumeTime = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.ResumeTime = params.get("ResumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ForbidLiveStreamResponse(AbstractModel):
    """ForbidLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegisterIMRequest(AbstractModel):
    """RegisterIM请求参数结构体

    """

    def __init__(self):
        """
        :param Nickname: 用户昵称
        :type Nickname: str
        :param UserId: 用户唯一ID，建议采用用户小程序OpenID加盐形式
        :type UserId: str
        :param HeadImgUrl: 用户头像URL
        :type HeadImgUrl: str
        :param Level: 用户身份，默认值：0，表示无特殊身份
        :type Level: int
        """
        self.Nickname = None
        self.UserId = None
        self.HeadImgUrl = None
        self.Level = None


    def _deserialize(self, params):
        self.Nickname = params.get("Nickname")
        self.UserId = params.get("UserId")
        self.HeadImgUrl = params.get("HeadImgUrl")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegisterIMResponse(AbstractModel):
    """RegisterIM返回参数结构体

    """

    def __init__(self):
        """
        :param UserKey: 用来传递给插件的关键字段
        :type UserKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserKey = params.get("UserKey")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class WorkerRegionInfo(AbstractModel):
    """worker的区域信息

    """

    def __init__(self):
        """
        :param Idle: 该区域空闲机器数量
        :type Idle: int
        :param Region: 区域
        :type Region: str
        """
        self.Idle = None
        self.Region = None


    def _deserialize(self, params):
        self.Idle = params.get("Idle")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        