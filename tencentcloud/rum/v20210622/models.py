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


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 创建的项目名(不为空且最长为 200)
        :type Name: str
        :param InstanceID: 项目对应实例 id
        :type InstanceID: str
        :param Rate: 项目抽样率(大于等于 0)
        :type Rate: str
        :param EnableURLGroup: 是否开启聚类
        :type EnableURLGroup: int
        :param Type: 项目类型("web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param Repo: 项目对应仓库地址(可选，最长为 256)
        :type Repo: str
        :param URL: 项目对应网页地址(可选，最长为 256)
        :type URL: str
        :param Desc: 创建的项目描述(可选，最长为 1000)
        :type Desc: str
        """
        self.Name = None
        self.InstanceID = None
        self.Rate = None
        self.EnableURLGroup = None
        self.Type = None
        self.Repo = None
        self.URL = None
        self.Desc = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.InstanceID = params.get("InstanceID")
        self.Rate = params.get("Rate")
        self.EnableURLGroup = params.get("EnableURLGroup")
        self.Type = params.get("Type")
        self.Repo = params.get("Repo")
        self.URL = params.get("URL")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 项目 id
        :type ID: int
        :param Key: 项目唯一key
        :type Key: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ID = None
        self.Key = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Key = params.get("Key")
        self.RequestId = params.get("RequestId")


class DescribeDataLogUrlStatisticsRequest(AbstractModel):
    """DescribeDataLogUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: "analysis", "compare", "samp", "version", "ext3","nettype", "platform","isp","region","device","browser","ext1","ext2"
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlStatisticsResponse(AbstractModel):
    """DescribeDataLogUrlStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataPerformancePageRequest(AbstractModel):
    """DescribeDataPerformancePage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 项目ID
        :type ID: int
        :param StartTime: 开始时间
        :type StartTime: int
        :param EndTime: 结束时间
        :type EndTime: int
        :param Type: ["pagepv", "allcount"]
        :type Type: str
        :param Level: 日志等级
        :type Level: str
        :param Isp: 运营商
        :type Isp: str
        :param Area: 地区
        :type Area: str
        :param NetType: 网络类型
        :type NetType: str
        :param Platform: 平台
        :type Platform: str
        :param Device: 机型
        :type Device: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Browser: 浏览器
        :type Browser: str
        :param Os: 操作系统
        :type Os: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Brand: 品牌
        :type Brand: str
        :param From: 来源页面
        :type From: str
        :param CostType: 耗时计算方式
        :type CostType: str
        """
        self.ID = None
        self.StartTime = None
        self.EndTime = None
        self.Type = None
        self.Level = None
        self.Isp = None
        self.Area = None
        self.NetType = None
        self.Platform = None
        self.Device = None
        self.VersionNum = None
        self.ExtFirst = None
        self.ExtSecond = None
        self.ExtThird = None
        self.IsAbroad = None
        self.Browser = None
        self.Os = None
        self.Engine = None
        self.Brand = None
        self.From = None
        self.CostType = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Type = params.get("Type")
        self.Level = params.get("Level")
        self.Isp = params.get("Isp")
        self.Area = params.get("Area")
        self.NetType = params.get("NetType")
        self.Platform = params.get("Platform")
        self.Device = params.get("Device")
        self.VersionNum = params.get("VersionNum")
        self.ExtFirst = params.get("ExtFirst")
        self.ExtSecond = params.get("ExtSecond")
        self.ExtThird = params.get("ExtThird")
        self.IsAbroad = params.get("IsAbroad")
        self.Browser = params.get("Browser")
        self.Os = params.get("Os")
        self.Engine = params.get("Engine")
        self.Brand = params.get("Brand")
        self.From = params.get("From")
        self.CostType = params.get("CostType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPerformancePageResponse(AbstractModel):
    """DescribeDataPerformancePage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeErrorRequest(AbstractModel):
    """DescribeError请求参数结构体

    """

    def __init__(self):
        r"""
        :param Date: 日期
        :type Date: str
        :param ID: 项目ID
        :type ID: int
        """
        self.Date = None
        self.ID = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorResponse(AbstractModel):
    """DescribeError返回参数结构体

    """

    def __init__(self):
        r"""
        :param Content: 内容
        :type Content: str
        :param ID: 项目ID
        :type ID: int
        :param CreateTime: 时间
        :type CreateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.ID = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.ID = params.get("ID")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")