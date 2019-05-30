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


class DescribeStreamPlayInfoListRequest(AbstractModel):
    """DescribeStreamPlayInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param EndTime: 结束时间，北京时间，
结束时间 和 开始时间  必须在同一天内。
        :type EndTime: str
        :param PlayDomain: 播放域名。
        :type PlayDomain: str
        :param StartTime: 开始时间，北京时间，
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


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的加速域名。
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