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


class CreateSessionRequest(AbstractModel):
    r"""CreateSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientSession: 客户端session信息，从JSSDK请求中获得
        :type ClientSession: str
        :param _GameId: 游戏ID
        :type GameId: str
        :param _UserId: 游戏用户ID
        :type UserId: str
        :param _GameParas: 游戏参数
        :type GameParas: str
        :param _GameRegion: 游戏区域
        :type GameRegion: str
        :param _ImageUrl: 背景图url
        :type ImageUrl: str
        :param _Resolution: 分辨率
        :type Resolution: str
        """
        self._ClientSession = None
        self._GameId = None
        self._UserId = None
        self._GameParas = None
        self._GameRegion = None
        self._ImageUrl = None
        self._Resolution = None

    @property
    def ClientSession(self):
        r"""客户端session信息，从JSSDK请求中获得
        :rtype: str
        """
        return self._ClientSession

    @ClientSession.setter
    def ClientSession(self, ClientSession):
        self._ClientSession = ClientSession

    @property
    def GameId(self):
        r"""游戏ID
        :rtype: str
        """
        return self._GameId

    @GameId.setter
    def GameId(self, GameId):
        self._GameId = GameId

    @property
    def UserId(self):
        r"""游戏用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GameParas(self):
        r"""游戏参数
        :rtype: str
        """
        return self._GameParas

    @GameParas.setter
    def GameParas(self, GameParas):
        self._GameParas = GameParas

    @property
    def GameRegion(self):
        r"""游戏区域
        :rtype: str
        """
        return self._GameRegion

    @GameRegion.setter
    def GameRegion(self, GameRegion):
        self._GameRegion = GameRegion

    @property
    def ImageUrl(self):
        r"""背景图url
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Resolution(self):
        r"""分辨率
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution


    def _deserialize(self, params):
        self._ClientSession = params.get("ClientSession")
        self._GameId = params.get("GameId")
        self._UserId = params.get("UserId")
        self._GameParas = params.get("GameParas")
        self._GameRegion = params.get("GameRegion")
        self._ImageUrl = params.get("ImageUrl")
        self._Resolution = params.get("Resolution")
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
        :param _ServerSession: 服务端session信息，返回给JSSDK
        :type ServerSession: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServerSession = None
        self._RequestId = None

    @property
    def ServerSession(self):
        r"""服务端session信息，返回给JSSDK
        :rtype: str
        """
        return self._ServerSession

    @ServerSession.setter
    def ServerSession(self, ServerSession):
        self._ServerSession = ServerSession

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServerSession = params.get("ServerSession")
        self._RequestId = params.get("RequestId")


class DayStreamPlayInfo(AbstractModel):
    r"""流播放信息

    """

    def __init__(self):
        r"""
        :param _Bandwidth: 带宽（单位Mbps）。
        :type Bandwidth: float
        :param _Flux: 流量 （单位MB）。
        :type Flux: float
        :param _Online: 在线人数。
        :type Online: int
        :param _Request: 请求数。
        :type Request: int
        :param _Time: 数据时间点，格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        """
        self._Bandwidth = None
        self._Flux = None
        self._Online = None
        self._Request = None
        self._Time = None

    @property
    def Bandwidth(self):
        r"""带宽（单位Mbps）。
        :rtype: float
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Flux(self):
        r"""流量 （单位MB）。
        :rtype: float
        """
        return self._Flux

    @Flux.setter
    def Flux(self, Flux):
        self._Flux = Flux

    @property
    def Online(self):
        r"""在线人数。
        :rtype: int
        """
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def Request(self):
        r"""请求数。
        :rtype: int
        """
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request

    @property
    def Time(self):
        r"""数据时间点，格式：yyyy-mm-dd HH:MM:SS。
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Bandwidth = params.get("Bandwidth")
        self._Flux = params.get("Flux")
        self._Online = params.get("Online")
        self._Request = params.get("Request")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPlayInfoListRequest(AbstractModel):
    r"""DescribeStreamPlayInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndTime: 结束时间，北京时间，格式：2019-04-28 10:36:00
结束时间 和 开始时间  必须在同一天内。
        :type EndTime: str
        :param _PlayDomain: 播放域名。
        :type PlayDomain: str
        :param _StartTime: 开始时间，北京时间，格式：2019-04-28 10:36:00
当前时间 和 开始时间 间隔不超过30天。
        :type StartTime: str
        :param _StreamName: 流名称，精确匹配。
若不填，则为查询总体播放数据。
        :type StreamName: str
        """
        self._EndTime = None
        self._PlayDomain = None
        self._StartTime = None
        self._StreamName = None

    @property
    def EndTime(self):
        r"""结束时间，北京时间，格式：2019-04-28 10:36:00
结束时间 和 开始时间  必须在同一天内。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PlayDomain(self):
        r"""播放域名。
        :rtype: str
        """
        return self._PlayDomain

    @PlayDomain.setter
    def PlayDomain(self, PlayDomain):
        self._PlayDomain = PlayDomain

    @property
    def StartTime(self):
        r"""开始时间，北京时间，格式：2019-04-28 10:36:00
当前时间 和 开始时间 间隔不超过30天。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StreamName(self):
        r"""流名称，精确匹配。
若不填，则为查询总体播放数据。
        :rtype: str
        """
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._PlayDomain = params.get("PlayDomain")
        self._StartTime = params.get("StartTime")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPlayInfoListResponse(AbstractModel):
    r"""DescribeStreamPlayInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataInfoList: 统计信息列表。
        :type DataInfoList: list of DayStreamPlayInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataInfoList = None
        self._RequestId = None

    @property
    def DataInfoList(self):
        r"""统计信息列表。
        :rtype: list of DayStreamPlayInfo
        """
        return self._DataInfoList

    @DataInfoList.setter
    def DataInfoList(self, DataInfoList):
        self._DataInfoList = DataInfoList

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self._DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = DayStreamPlayInfo()
                obj._deserialize(item)
                self._DataInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWorkersRequest(AbstractModel):
    r"""DescribeWorkers请求参数结构体

    """


class DescribeWorkersResponse(AbstractModel):
    r"""DescribeWorkers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionDetail: 各个区域的机器情况
        :type RegionDetail: list of WorkerRegionInfo
        :param _Idle: 空闲机器总数量
        :type Idle: int
        :param _RegionNum: 区域个数
        :type RegionNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionDetail = None
        self._Idle = None
        self._RegionNum = None
        self._RequestId = None

    @property
    def RegionDetail(self):
        r"""各个区域的机器情况
        :rtype: list of WorkerRegionInfo
        """
        return self._RegionDetail

    @RegionDetail.setter
    def RegionDetail(self, RegionDetail):
        self._RegionDetail = RegionDetail

    @property
    def Idle(self):
        r"""空闲机器总数量
        :rtype: int
        """
        return self._Idle

    @Idle.setter
    def Idle(self, Idle):
        self._Idle = Idle

    @property
    def RegionNum(self):
        r"""区域个数
        :rtype: int
        """
        return self._RegionNum

    @RegionNum.setter
    def RegionNum(self, RegionNum):
        self._RegionNum = RegionNum

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionDetail") is not None:
            self._RegionDetail = []
            for item in params.get("RegionDetail"):
                obj = WorkerRegionInfo()
                obj._deserialize(item)
                self._RegionDetail.append(obj)
        self._Idle = params.get("Idle")
        self._RegionNum = params.get("RegionNum")
        self._RequestId = params.get("RequestId")


class ForbidLiveStreamRequest(AbstractModel):
    r"""ForbidLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称。
        :type AppName: str
        :param _DomainName: 您的推流域名。
        :type DomainName: str
        :param _StreamName: 流名称。
        :type StreamName: str
        :param _ResumeTime: 恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：默认禁播90天，且最长支持禁播90天。
        :type ResumeTime: str
        """
        self._AppName = None
        self._DomainName = None
        self._StreamName = None
        self._ResumeTime = None

    @property
    def AppName(self):
        r"""应用名称。
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def DomainName(self):
        r"""您的推流域名。
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def StreamName(self):
        r"""流名称。
        :rtype: str
        """
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def ResumeTime(self):
        r"""恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：默认禁播90天，且最长支持禁播90天。
        :rtype: str
        """
        return self._ResumeTime

    @ResumeTime.setter
    def ResumeTime(self, ResumeTime):
        self._ResumeTime = ResumeTime


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._DomainName = params.get("DomainName")
        self._StreamName = params.get("StreamName")
        self._ResumeTime = params.get("ResumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidLiveStreamResponse(AbstractModel):
    r"""ForbidLiveStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RegisterIMRequest(AbstractModel):
    r"""RegisterIM请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Nickname: 用户昵称
        :type Nickname: str
        :param _UserId: 用户唯一ID，建议采用用户小程序OpenID加盐形式
        :type UserId: str
        :param _HeadImgUrl: 用户头像URL
        :type HeadImgUrl: str
        :param _Level: 用户身份，默认值：0，表示无特殊身份
        :type Level: int
        """
        self._Nickname = None
        self._UserId = None
        self._HeadImgUrl = None
        self._Level = None

    @property
    def Nickname(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def UserId(self):
        r"""用户唯一ID，建议采用用户小程序OpenID加盐形式
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def HeadImgUrl(self):
        r"""用户头像URL
        :rtype: str
        """
        return self._HeadImgUrl

    @HeadImgUrl.setter
    def HeadImgUrl(self, HeadImgUrl):
        self._HeadImgUrl = HeadImgUrl

    @property
    def Level(self):
        r"""用户身份，默认值：0，表示无特殊身份
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Nickname = params.get("Nickname")
        self._UserId = params.get("UserId")
        self._HeadImgUrl = params.get("HeadImgUrl")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterIMResponse(AbstractModel):
    r"""RegisterIM返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserKey: 用来传递给插件的关键字段
        :type UserKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserKey = None
        self._RequestId = None

    @property
    def UserKey(self):
        r"""用来传递给插件的关键字段
        :rtype: str
        """
        return self._UserKey

    @UserKey.setter
    def UserKey(self, UserKey):
        self._UserKey = UserKey

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserKey = params.get("UserKey")
        self._RequestId = params.get("RequestId")


class StopGameRequest(AbstractModel):
    r"""StopGame请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 游戏用户ID
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        r"""游戏用户ID
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
        


class StopGameResponse(AbstractModel):
    r"""StopGame返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class WorkerRegionInfo(AbstractModel):
    r"""worker的区域信息

    """

    def __init__(self):
        r"""
        :param _Idle: 该区域空闲机器数量
        :type Idle: int
        :param _Region: 区域
        :type Region: str
        """
        self._Idle = None
        self._Region = None

    @property
    def Idle(self):
        r"""该区域空闲机器数量
        :rtype: int
        """
        return self._Idle

    @Idle.setter
    def Idle(self, Idle):
        self._Idle = Idle

    @property
    def Region(self):
        r"""区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Idle = params.get("Idle")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        