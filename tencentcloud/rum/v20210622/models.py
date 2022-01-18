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
        :param InstanceID: 业务系统 ID
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


class DescribeDataEventUrlRequest(AbstractModel):
    """DescribeDataEventUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: 类型
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
        :param Name: 筛选条件
        :type Name: str
        :param Env: 环境
        :type Env: str
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
        self.Name = None
        self.Env = None


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
        self.Name = params.get("Name")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEventUrlResponse(AbstractModel):
    """DescribeDataEventUrl返回参数结构体

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


class DescribeDataFetchUrlInfoRequest(AbstractModel):
    """DescribeDataFetchUrlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: 类型
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
        :param CostType: 耗时计算方式
        :type CostType: str
        :param Url: 来源
        :type Url: str
        :param Env: 环境
        :type Env: str
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
        self.CostType = None
        self.Url = None
        self.Env = None


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
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlInfoResponse(AbstractModel):
    """DescribeDataFetchUrlInfo返回参数结构体

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


class DescribeDataFetchUrlRequest(AbstractModel):
    """DescribeDataFetchUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: 类型
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
        :param CostType: 耗时计算方式
        :type CostType: str
        :param Url: 来源
        :type Url: str
        :param Env: 环境
        :type Env: str
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
        self.CostType = None
        self.Url = None
        self.Env = None


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
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlResponse(AbstractModel):
    """DescribeDataFetchUrl返回参数结构体

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
        :param Env: 环境区分
        :type Env: str
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
        self.Env = None


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
        self.Env = params.get("Env")
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
        :param Env: 环境变量
        :type Env: str
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
        self.Env = None


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
        self.Env = params.get("Env")
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


class DescribeDataPvUrlStatisticsRequest(AbstractModel):
    """DescribeDataPvUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: 类型:"allcount", "falls", "samp", "version", "ext3","nettype", "platform","isp","region","device","browser","ext1","ext2"
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
        :param Env: 环境
        :type Env: str
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
        self.Env = None


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
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlStatisticsResponse(AbstractModel):
    """DescribeDataPvUrlStatistics返回参数结构体

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


class DescribeLogListRequest(AbstractModel):
    """DescribeLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sort: 排序方式  desc  asc
        :type Sort: str
        :param ActionType: searchlog  histogram
        :type ActionType: str
        :param ID: 项目ID
        :type ID: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param Limit: 单次查询返回的原始日志条数，最大值为100
        :type Limit: int
        :param Context: 上下文，加载更多日志时使用，透传上次返回的 Context 值，获取后续的日志内容，总计最多可获取1万条原始日志。过期时间1小时
        :type Context: str
        :param Query: 查询语句，语句长度最大为4096
        :type Query: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.Sort = None
        self.ActionType = None
        self.ID = None
        self.StartTime = None
        self.Limit = None
        self.Context = None
        self.Query = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Sort = params.get("Sort")
        self.ActionType = params.get("ActionType")
        self.ID = params.get("ID")
        self.StartTime = params.get("StartTime")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Query = params.get("Query")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogListResponse(AbstractModel):
    """DescribeLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回字符串
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页每页数目，整型
        :type Limit: int
        :param Offset: 分页页码，整型
        :type Offset: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 列表总数
        :type TotalCount: int
        :param ProjectSet: 项目列表
        :type ProjectSet: list of RumProject
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProjectSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProjectSet") is not None:
            self.ProjectSet = []
            for item in params.get("ProjectSet"):
                obj = RumProject()
                obj._deserialize(item)
                self.ProjectSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScoresRequest(AbstractModel):
    """DescribeScores请求参数结构体

    """

    def __init__(self):
        r"""
        :param EndTime: 结束时间
        :type EndTime: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param ID: 项目ID
        :type ID: int
        """
        self.EndTime = None
        self.StartTime = None
        self.ID = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScoresResponse(AbstractModel):
    """DescribeScores返回参数结构体

    """

    def __init__(self):
        r"""
        :param ScoreSet: 数组
        :type ScoreSet: list of ScoreInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScoreSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScoreSet") is not None:
            self.ScoreSet = []
            for item in params.get("ScoreSet"):
                obj = ScoreInfo()
                obj._deserialize(item)
                self.ScoreSet.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    · 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    · 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param Name: 过滤键的名称。
        :type Name: str
        """
        self.Values = None
        self.Name = None


    def _deserialize(self, params):
        self.Values = params.get("Values")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumProject(AbstractModel):
    """Rum 项目信息

    """

    def __init__(self):
        r"""
        :param Name: 项目名
        :type Name: str
        :param Creator: 创建者 id
        :type Creator: str
        :param InstanceID: 实例 id
        :type InstanceID: str
        :param Type: 项目类型
        :type Type: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Repo: 项目仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Repo: str
        :param URL: 项目网址地址
注意：此字段可能返回 null，表示取不到有效值。
        :type URL: str
        :param Rate: 项目采样频率
        :type Rate: str
        :param Key: 项目唯一key（长度 12 位）
        :type Key: str
        :param EnableURLGroup: 是否开启url聚类
        :type EnableURLGroup: int
        :param InstanceName: 实例名
        :type InstanceName: str
        :param ID: 项目 ID
        :type ID: int
        :param InstanceKey: 实例 key
        :type InstanceKey: str
        :param Desc: 项目描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param IsStar: 是否星标  1:是 0:否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsStar: int
        """
        self.Name = None
        self.Creator = None
        self.InstanceID = None
        self.Type = None
        self.CreateTime = None
        self.Repo = None
        self.URL = None
        self.Rate = None
        self.Key = None
        self.EnableURLGroup = None
        self.InstanceName = None
        self.ID = None
        self.InstanceKey = None
        self.Desc = None
        self.IsStar = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Creator = params.get("Creator")
        self.InstanceID = params.get("InstanceID")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.Repo = params.get("Repo")
        self.URL = params.get("URL")
        self.Rate = params.get("Rate")
        self.Key = params.get("Key")
        self.EnableURLGroup = params.get("EnableURLGroup")
        self.InstanceName = params.get("InstanceName")
        self.ID = params.get("ID")
        self.InstanceKey = params.get("InstanceKey")
        self.Desc = params.get("Desc")
        self.IsStar = params.get("IsStar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreInfo(AbstractModel):
    """project Score分数实体

    """

    def __init__(self):
        r"""
        :param StaticDuration: duration
        :type StaticDuration: str
        :param PagePv: pv
        :type PagePv: str
        :param ApiFail: 失败
        :type ApiFail: str
        :param ApiNum: 请求
        :type ApiNum: str
        :param StaticFail: fail
        :type StaticFail: str
        :param ProjectID: 项目id
        :type ProjectID: int
        :param PageUv: uv
        :type PageUv: str
        :param ApiDuration: 请求次数
        :type ApiDuration: str
        :param Score: 分数
        :type Score: str
        :param PageError: error
        :type PageError: str
        :param StaticNum: num
        :type StaticNum: str
        :param RecordNum: num
        :type RecordNum: int
        :param PageDuration: Duration
        :type PageDuration: str
        """
        self.StaticDuration = None
        self.PagePv = None
        self.ApiFail = None
        self.ApiNum = None
        self.StaticFail = None
        self.ProjectID = None
        self.PageUv = None
        self.ApiDuration = None
        self.Score = None
        self.PageError = None
        self.StaticNum = None
        self.RecordNum = None
        self.PageDuration = None


    def _deserialize(self, params):
        self.StaticDuration = params.get("StaticDuration")
        self.PagePv = params.get("PagePv")
        self.ApiFail = params.get("ApiFail")
        self.ApiNum = params.get("ApiNum")
        self.StaticFail = params.get("StaticFail")
        self.ProjectID = params.get("ProjectID")
        self.PageUv = params.get("PageUv")
        self.ApiDuration = params.get("ApiDuration")
        self.Score = params.get("Score")
        self.PageError = params.get("PageError")
        self.StaticNum = params.get("StaticNum")
        self.RecordNum = params.get("RecordNum")
        self.PageDuration = params.get("PageDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        