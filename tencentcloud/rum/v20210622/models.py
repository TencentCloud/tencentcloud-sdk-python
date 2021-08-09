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
        """
        :param Name: 创建的项目名(不为空且最长为 200)\n        :type Name: str\n        :param InstanceID: 项目对应实例 id\n        :type InstanceID: str\n        :param Rate: 项目抽样率(大于等于 0)\n        :type Rate: str\n        :param EnableURLGroup: 是否开启聚类\n        :type EnableURLGroup: int\n        :param Type: 项目类型("web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")\n        :type Type: str\n        :param Repo: 项目对应仓库地址(可选，最长为 256)\n        :type Repo: str\n        :param URL: 项目对应网页地址(可选，最长为 256)\n        :type URL: str\n        :param Desc: 创建的项目描述(可选，最长为 1000)\n        :type Desc: str\n        """
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
        """
        :param ID: 项目 id\n        :type ID: int\n        :param Key: 项目唯一key\n        :type Key: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ID = None
        self.Key = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Key = params.get("Key")
        self.RequestId = params.get("RequestId")


class DescribeDataPerformancePageRequest(AbstractModel):
    """DescribeDataPerformancePage请求参数结构体

    """

    def __init__(self):
        """
        :param ID: 项目ID\n        :type ID: int\n        :param StartTime: 开始时间\n        :type StartTime: int\n        :param EndTime: 结束时间\n        :type EndTime: int\n        :param Type: ["pagepv", "allcount"]\n        :type Type: str\n        :param Level: 日志等级\n        :type Level: str\n        :param Isp: 运营商\n        :type Isp: str\n        :param Area: 地区\n        :type Area: str\n        :param NetType: 网络类型\n        :type NetType: str\n        :param Platform: 平台\n        :type Platform: str\n        :param Device: 机型\n        :type Device: str\n        :param VersionNum: 版本\n        :type VersionNum: str\n        :param ExtFirst: 自定义1\n        :type ExtFirst: str\n        :param ExtSecond: 自定义2\n        :type ExtSecond: str\n        :param ExtThird: 自定义3\n        :type ExtThird: str\n        :param IsAbroad: 是否海外\n        :type IsAbroad: str\n        :param Browser: 浏览器\n        :type Browser: str\n        :param Os: 操作系统\n        :type Os: str\n        :param Engine: 浏览器引擎\n        :type Engine: str\n        :param Brand: 品牌\n        :type Brand: str\n        :param From: 来源页面\n        :type From: str\n        :param CostType: 耗时计算方式\n        :type CostType: str\n        """
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
        """
        :param Result: 返回值\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")