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


class DescribeResourceListRequest(AbstractModel):
    """DescribeResourceList请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版；shield表示棋牌）
        :type Business: str
        :param RegionList: 地域码搜索，可选，当不指定地域时空数组，当指定地域时，填地域码。例如：["gz", "sh"]
        :type RegionList: list of str
        :param Line: 线路搜索，可选，只有当获取高防IP资源列表是可以选填，取值为[1（BGP线路），2（南京电信），3（南京联通），99（第三方合作线路）]，当获取其他产品时请填空数组；
        :type Line: list of int non-negative
        :param IdList: 资源ID搜索，可选，当不为空数组时表示获取指定资源的资源列表；
        :type IdList: list of str
        :param Name: 资源名称搜索，可选，当不为空字符串时表示按名称搜索资源；
        :type Name: str
        :param IpList: IP搜索列表，可选，当不为空时表示安装IP搜索资源；
        :type IpList: list of str
        :param Status: 资源状态搜索列表，可选，取值为[0（运行中）, 1（清洗中）, 2（封堵中）]，当填空数组时不进行状态搜索；
        :type Status: list of int non-negative
        :param Expire: 即将到期搜索；可选，取值为[0（不搜索），1（搜索即将到期的资源）]
        :type Expire: int
        :param OderBy: 排序字段，可选
        :type OderBy: list of OrderBy
        :param Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param CName: 高防IP专业版资源的CNAME，可选，只对高防IP专业版资源列表有效；
        :type CName: str
        :param Domain: 高防IP专业版资源的域名，可选，只对高防IP专业版资源列表有效；
        :type Domain: str
        """
        self.Business = None
        self.RegionList = None
        self.Line = None
        self.IdList = None
        self.Name = None
        self.IpList = None
        self.Status = None
        self.Expire = None
        self.OderBy = None
        self.Limit = None
        self.Offset = None
        self.CName = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RegionList = params.get("RegionList")
        self.Line = params.get("Line")
        self.IdList = params.get("IdList")
        self.Name = params.get("Name")
        self.IpList = params.get("IpList")
        self.Status = params.get("Status")
        self.Expire = params.get("Expire")
        if params.get("OderBy") is not None:
            self.OderBy = []
            for item in params.get("OderBy"):
                obj = OrderBy()
                obj._deserialize(item)
                self.OderBy.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.CName = params.get("CName")
        self.Domain = params.get("Domain")


class DescribeResourceListResponse(AbstractModel):
    """DescribeResourceList返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 总记录数
        :type Total: int
        :param ServicePacks: 资源记录列表
        :type ServicePacks: list of KeyValueRecord
        :param Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版；shield表示棋牌）
        :type Business: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ServicePacks = None
        self.Business = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ServicePacks") is not None:
            self.ServicePacks = []
            for item in params.get("ServicePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.ServicePacks.append(obj)
        self.Business = params.get("Business")
        self.RequestId = params.get("RequestId")


class KeyValue(AbstractModel):
    """字段值，K-V形式

    """

    def __init__(self):
        """
        :param Key: 字段名称
        :type Key: str
        :param Value: 字段取值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class KeyValueRecord(AbstractModel):
    """KeyValue记录

    """

    def __init__(self):
        """
        :param Record: 一条记录的Key-Value数组
        :type Record: list of KeyValue
        """
        self.Record = None


    def _deserialize(self, params):
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Record.append(obj)


class OrderBy(AbstractModel):
    """排序字段

    """

    def __init__(self):
        """
        :param Field: 排序字段名称，取值[
bandwidth（带宽），
overloadCount（超峰值次数）
]
        :type Field: str
        :param Order: 升降序，取值为[asc（升序），（升序），desc（降序）， DESC（降序）]
        :type Order: str
        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")