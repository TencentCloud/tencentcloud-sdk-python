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


class DescribeStatusRequest(AbstractModel):
    """DescribeStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Pk: 购买服务后获得的授权帐号，用于保证请求有效性
        :type Pk: str
        :param Md5: 需要获取分析结果的样本md5
        :type Md5: str
        """
        self.Pk = None
        self.Md5 = None


    def _deserialize(self, params):
        self.Pk = params.get("Pk")
        self.Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStatusResponse(AbstractModel):
    """DescribeStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 接口调用状态，1表示成功，非1表示失败
        :type Status: int
        :param Info: 成功时返回success，失败时返回具体的失败原因，如样本分析未完成
        :type Info: str
        :param Data: 成功时返回样本日志下载地址，该地址10分钟内有效
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class StartAnalyseRequest(AbstractModel):
    """StartAnalyse请求参数结构体

    """

    def __init__(self):
        r"""
        :param Pk: 购买服务后获得的授权帐号，用于保证请求有效性
        :type Pk: str
        :param Md5: 样本md5，用于对下载获得的样本完整性进行校验
        :type Md5: str
        :param DlUrl: 待分析样本下载地址
        :type DlUrl: str
        """
        self.Pk = None
        self.Md5 = None
        self.DlUrl = None


    def _deserialize(self, params):
        self.Pk = params.get("Pk")
        self.Md5 = params.get("Md5")
        self.DlUrl = params.get("DlUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAnalyseResponse(AbstractModel):
    """StartAnalyse返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 接口调用状态，1表示成功，非1表示失败
        :type Status: int
        :param Info: 成功时返回success，失败时返回具体的失败原因
        :type Info: str
        :param Data: 保留字段
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")