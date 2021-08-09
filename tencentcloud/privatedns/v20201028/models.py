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


class AuditLog(AbstractModel):
    """操作日志

    """

    def __init__(self):
        """
        :param Resource: 日志类型\n        :type Resource: str\n        :param Metric: 日志表名\n        :type Metric: str\n        :param TotalCount: 日志总数\n        :type TotalCount: int\n        :param DataSet: 日志列表\n        :type DataSet: list of AuditLogInfo\n        """
        self.Resource = None
        self.Metric = None
        self.TotalCount = None
        self.DataSet = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        self.Metric = params.get("Metric")
        self.TotalCount = params.get("TotalCount")
        if params.get("DataSet") is not None:
            self.DataSet = []
            for item in params.get("DataSet"):
                obj = AuditLogInfo()
                obj._deserialize(item)
                self.DataSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogInfo(AbstractModel):
    """日志详情

    """

    def __init__(self):
        """
        :param Date: 时间\n        :type Date: str\n        :param OperatorUin: 操作人uin\n        :type OperatorUin: str\n        :param Content: 日志内容\n        :type Content: str\n        """
        self.Date = None
        self.OperatorUin = None
        self.Content = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.OperatorUin = params.get("OperatorUin")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneRecordRequest(AbstractModel):
    """CreatePrivateZoneRecord请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 私有域ID\n        :type ZoneId: str\n        :param RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"\n        :type RecordType: str\n        :param SubDomain: 子域名，例如 "www", "m", "@"\n        :type SubDomain: str\n        :param RecordValue: 记录值，例如 IP：192.168.10.2，CNAME：cname.qcloud.com.，MX：mail.qcloud.com.\n        :type RecordValue: str\n        :param Weight: 记录权重，值为1-100\n        :type Weight: int\n        :param MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50\n        :type MX: int\n        :param TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600\n        :type TTL: int\n        """
        self.ZoneId = None
        self.RecordType = None
        self.SubDomain = None
        self.RecordValue = None
        self.Weight = None
        self.MX = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RecordType = params.get("RecordType")
        self.SubDomain = params.get("SubDomain")
        self.RecordValue = params.get("RecordValue")
        self.Weight = params.get("Weight")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneRecordResponse(AbstractModel):
    """CreatePrivateZoneRecord返回参数结构体

    """

    def __init__(self):
        """
        :param RecordId: 记录Id\n        :type RecordId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class CreatePrivateZoneRequest(AbstractModel):
    """CreatePrivateZone请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名，格式必须是标准的TLD\n        :type Domain: str\n        :param TagSet: 创建私有域的同时，为其打上标签\n        :type TagSet: list of TagInfo\n        :param VpcSet: 创建私有域的同时，将其关联至VPC\n        :type VpcSet: list of VpcInfo\n        :param Remark: 备注\n        :type Remark: str\n        :param DnsForwardStatus: 是否开启子域名递归, ENABLED， DISABLED。默认值为DISABLED\n        :type DnsForwardStatus: str\n        :param Vpcs: 创建私有域的同时，将其关联至VPC\n        :type Vpcs: list of VpcInfo\n        """
        self.Domain = None
        self.TagSet = None
        self.VpcSet = None
        self.Remark = None
        self.DnsForwardStatus = None
        self.Vpcs = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.Remark = params.get("Remark")
        self.DnsForwardStatus = params.get("DnsForwardStatus")
        if params.get("Vpcs") is not None:
            self.Vpcs = []
            for item in params.get("Vpcs"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.Vpcs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneResponse(AbstractModel):
    """CreatePrivateZone返回参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 私有域ID, zone-xxxxxx\n        :type ZoneId: str\n        :param Domain: 私有域名\n        :type Domain: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ZoneId = None
        self.Domain = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Domain = params.get("Domain")
        self.RequestId = params.get("RequestId")


class DatePoint(AbstractModel):
    """时间统计值

    """

    def __init__(self):
        """
        :param Date: 时间\n        :type Date: str\n        :param Value: 值\n        :type Value: int\n        """
        self.Date = None
        self.Value = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneRecordRequest(AbstractModel):
    """DeletePrivateZoneRecord请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 私有域ID\n        :type ZoneId: str\n        :param RecordId: 记录ID\n        :type RecordId: str\n        :param RecordIdSet: 记录ID数组，RecordId 优先\n        :type RecordIdSet: list of str\n        """
        self.ZoneId = None
        self.RecordId = None
        self.RecordIdSet = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RecordId = params.get("RecordId")
        self.RecordIdSet = params.get("RecordIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneRecordResponse(AbstractModel):
    """DeletePrivateZoneRecord返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivateZoneRequest(AbstractModel):
    """DeletePrivateZone请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 私有域ID\n        :type ZoneId: str\n        :param ZoneIdSet: 私有域ID数组，ZoneId 优先\n        :type ZoneIdSet: list of str\n        """
        self.ZoneId = None
        self.ZoneIdSet = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneIdSet = params.get("ZoneIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneResponse(AbstractModel):
    """DeletePrivateZone返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAuditLogRequest(AbstractModel):
    """DescribeAuditLog请求参数结构体

    """

    def __init__(self):
        """
        :param TimeRangeBegin: 请求量统计起始时间\n        :type TimeRangeBegin: str\n        :param Filters: 筛选参数：ZoneId：私有域ID；Domain：私有域；OperatorUin：操作者账号ID\n        :type Filters: list of Filter\n        :param TimeRangeEnd: 请求量统计结束时间\n        :type TimeRangeEnd: str\n        :param Offset: 分页偏移量，从0开始\n        :type Offset: int\n        :param Limit: 分页限制数目， 最大100，默认20\n        :type Limit: int\n        """
        self.TimeRangeBegin = None
        self.Filters = None
        self.TimeRangeEnd = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TimeRangeBegin = params.get("TimeRangeBegin")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogResponse(AbstractModel):
    """DescribeAuditLog返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 操作日志列表\n        :type Data: list of AuditLog\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AuditLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDashboardRequest(AbstractModel):
    """DescribeDashboard请求参数结构体

    """


class DescribeDashboardResponse(AbstractModel):
    """DescribeDashboard返回参数结构体

    """

    def __init__(self):
        """
        :param ZoneTotal: 私有域解析总数\n        :type ZoneTotal: int\n        :param ZoneVpcCount: 私有域关联VPC数量\n        :type ZoneVpcCount: int\n        :param RequestTotalCount: 历史请求量总数\n        :type RequestTotalCount: int\n        :param FlowUsage: 流量包用量\n        :type FlowUsage: list of FlowUsage\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ZoneTotal = None
        self.ZoneVpcCount = None
        self.RequestTotalCount = None
        self.FlowUsage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneTotal = params.get("ZoneTotal")
        self.ZoneVpcCount = params.get("ZoneVpcCount")
        self.RequestTotalCount = params.get("RequestTotalCount")
        if params.get("FlowUsage") is not None:
            self.FlowUsage = []
            for item in params.get("FlowUsage"):
                obj = FlowUsage()
                obj._deserialize(item)
                self.FlowUsage.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateZoneListRequest(AbstractModel):
    """DescribePrivateZoneList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页偏移量，从0开始\n        :type Offset: int\n        :param Limit: 分页限制数目， 最大100，默认20\n        :type Limit: int\n        :param Filters: 过滤参数\n        :type Filters: list of Filter\n        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        


class DescribePrivateZoneListResponse(AbstractModel):
    """DescribePrivateZoneList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 私有域数量\n        :type TotalCount: int\n        :param PrivateZoneSet: 私有域列表\n        :type PrivateZoneSet: list of PrivateZone\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.PrivateZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PrivateZoneSet") is not None:
            self.PrivateZoneSet = []
            for item in params.get("PrivateZoneSet"):
                obj = PrivateZone()
                obj._deserialize(item)
                self.PrivateZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateZoneRecordListRequest(AbstractModel):
    """DescribePrivateZoneRecordList请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 私有域ID: zone-xxxxxx\n        :type ZoneId: str\n        :param Filters: 过滤参数\n        :type Filters: list of Filter\n        :param Offset: 分页偏移量，从0开始\n        :type Offset: int\n        :param Limit: 分页限制数目， 最大100，默认20\n        :type Limit: int\n        """
        self.ZoneId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateZoneRecordListResponse(AbstractModel):
    """DescribePrivateZoneRecordList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 解析记录数量\n        :type TotalCount: int\n        :param RecordSet: 解析记录列表\n        :type RecordSet: list of PrivateZoneRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.RecordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RecordSet") is not None:
            self.RecordSet = []
            for item in params.get("RecordSet"):
                obj = PrivateZoneRecord()
                obj._deserialize(item)
                self.RecordSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateZoneRequest(AbstractModel):
    """DescribePrivateZone请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 域名，格式必须是标准的TLD\n        :type ZoneId: str\n        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateZoneResponse(AbstractModel):
    """DescribePrivateZone返回参数结构体

    """

    def __init__(self):
        """
        :param PrivateZone: 私有域详情\n        :type PrivateZone: :class:`tencentcloud.privatedns.v20201028.models.PrivateZone`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PrivateZone = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PrivateZone") is not None:
            self.PrivateZone = PrivateZone()
            self.PrivateZone._deserialize(params.get("PrivateZone"))
        self.RequestId = params.get("RequestId")


class DescribePrivateZoneServiceRequest(AbstractModel):
    """DescribePrivateZoneService请求参数结构体

    """


class DescribePrivateZoneServiceResponse(AbstractModel):
    """DescribePrivateZoneService返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceStatus: 私有域解析服务开通状态。ENABLED已开通，DISABLED未开通\n        :type ServiceStatus: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceStatus = params.get("ServiceStatus")
        self.RequestId = params.get("RequestId")


class DescribeRequestDataRequest(AbstractModel):
    """DescribeRequestData请求参数结构体

    """

    def __init__(self):
        """
        :param TimeRangeBegin: 请求量统计起始时间，格式：2020-11-22 00:00:00\n        :type TimeRangeBegin: str\n        :param Filters: 筛选参数：\n        :type Filters: list of Filter\n        :param TimeRangeEnd: 请求量统计结束时间，格式：2020-11-22 23:59:59\n        :type TimeRangeEnd: str\n        """
        self.TimeRangeBegin = None
        self.Filters = None
        self.TimeRangeEnd = None


    def _deserialize(self, params):
        self.TimeRangeBegin = params.get("TimeRangeBegin")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRequestDataResponse(AbstractModel):
    """DescribeRequestData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 请求量统计表\n        :type Data: list of MetricData\n        :param Interval: 请求量单位时间: Day：天，Hour：小时\n        :type Interval: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = MetricData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """筛选参数

    """

    def __init__(self):
        """
        :param Name: 参数名\n        :type Name: str\n        :param Values: 参数值数组\n        :type Values: list of str\n        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowUsage(AbstractModel):
    """流量包用量

    """

    def __init__(self):
        """
        :param FlowType: 流量包类型：ZONE 私有域；TRAFFIC 解析流量包\n        :type FlowType: str\n        :param TotalQuantity: 流量包总额度\n        :type TotalQuantity: int\n        :param AvailableQuantity: 流量包可用额度\n        :type AvailableQuantity: int\n        """
        self.FlowType = None
        self.TotalQuantity = None
        self.AvailableQuantity = None


    def _deserialize(self, params):
        self.FlowType = params.get("FlowType")
        self.TotalQuantity = params.get("TotalQuantity")
        self.AvailableQuantity = params.get("AvailableQuantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    """统计数据表

    """

    def __init__(self):
        """
        :param Resource: 资源描述\n        :type Resource: str\n        :param Metric: 表名\n        :type Metric: str\n        :param DataSet: 表数据\n        :type DataSet: list of DatePoint\n        """
        self.Resource = None
        self.Metric = None
        self.DataSet = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        self.Metric = params.get("Metric")
        if params.get("DataSet") is not None:
            self.DataSet = []
            for item in params.get("DataSet"):
                obj = DatePoint()
                obj._deserialize(item)
                self.DataSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneRecordRequest(AbstractModel):
    """ModifyPrivateZoneRecord请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 私有域ID\n        :type ZoneId: str\n        :param RecordId: 记录ID\n        :type RecordId: str\n        :param RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"\n        :type RecordType: str\n        :param SubDomain: 子域名，例如 "www", "m", "@"\n        :type SubDomain: str\n        :param RecordValue: 记录值，例如 IP：192.168.10.2，CNAME：cname.qcloud.com.，MX：mail.qcloud.com.\n        :type RecordValue: str\n        :param Weight: 记录权重，值为1-100\n        :type Weight: int\n        :param MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50\n        :type MX: int\n        :param TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600\n        :type TTL: int\n        """
        self.ZoneId = None
        self.RecordId = None
        self.RecordType = None
        self.SubDomain = None
        self.RecordValue = None
        self.Weight = None
        self.MX = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RecordId = params.get("RecordId")
        self.RecordType = params.get("RecordType")
        self.SubDomain = params.get("SubDomain")
        self.RecordValue = params.get("RecordValue")
        self.Weight = params.get("Weight")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneRecordResponse(AbstractModel):
    """ModifyPrivateZoneRecord返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateZoneRequest(AbstractModel):
    """ModifyPrivateZone请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 私有域ID\n        :type ZoneId: str\n        :param Remark: 备注\n        :type Remark: str\n        :param DnsForwardStatus: 是否开启子域名递归, ENABLED， DISABLED\n        :type DnsForwardStatus: str\n        """
        self.ZoneId = None
        self.Remark = None
        self.DnsForwardStatus = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Remark = params.get("Remark")
        self.DnsForwardStatus = params.get("DnsForwardStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneResponse(AbstractModel):
    """ModifyPrivateZone返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateZoneVpcRequest(AbstractModel):
    """ModifyPrivateZoneVpc请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 私有域ID\n        :type ZoneId: str\n        :param VpcSet: 私有域关联的全部VPC列表\n        :type VpcSet: list of VpcInfo\n        """
        self.ZoneId = None
        self.VpcSet = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneVpcResponse(AbstractModel):
    """ModifyPrivateZoneVpc返回参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 私有域ID, zone-xxxxxx\n        :type ZoneId: str\n        :param VpcSet: 解析域关联的VPC列表\n        :type VpcSet: list of VpcInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ZoneId = None
        self.VpcSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class PrivateZone(AbstractModel):
    """私有域信息

    """

    def __init__(self):
        """
        :param ZoneId: 私有域id: zone-xxxxxxxx\n        :type ZoneId: str\n        :param OwnerUin: 域名所有者uin\n        :type OwnerUin: int\n        :param Domain: 私有域名\n        :type Domain: str\n        :param CreatedOn: 创建时间\n        :type CreatedOn: str\n        :param UpdatedOn: 修改时间\n        :type UpdatedOn: str\n        :param RecordCount: 记录数\n        :type RecordCount: int\n        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param VpcSet: 绑定的Vpc列表\n        :type VpcSet: list of VpcInfo\n        :param Status: 私有域状态：正常解析：ENABLED, 暂停解析：SUSPEND, 锁定：FROZEN\n        :type Status: str\n        :param DnsForwardStatus: 域名递归解析状态：开通：ENABLED, 关闭，DISABLED\n        :type DnsForwardStatus: str\n        :param Tags: 标签键值对集合\n        :type Tags: list of TagInfo\n        """
        self.ZoneId = None
        self.OwnerUin = None
        self.Domain = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.RecordCount = None
        self.Remark = None
        self.VpcSet = None
        self.Status = None
        self.DnsForwardStatus = None
        self.Tags = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.OwnerUin = params.get("OwnerUin")
        self.Domain = params.get("Domain")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.RecordCount = params.get("RecordCount")
        self.Remark = params.get("Remark")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.Status = params.get("Status")
        self.DnsForwardStatus = params.get("DnsForwardStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateZoneRecord(AbstractModel):
    """私有域信息

    """

    def __init__(self):
        """
        :param RecordId: 记录id\n        :type RecordId: str\n        :param ZoneId: 私有域id: zone-xxxxxxxx\n        :type ZoneId: str\n        :param SubDomain: 子域名\n        :type SubDomain: str\n        :param RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"\n        :type RecordType: str\n        :param RecordValue: 记录值\n        :type RecordValue: str\n        :param TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600\n        :type TTL: int\n        :param MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
注意：此字段可能返回 null，表示取不到有效值。\n        :type MX: int\n        :param Status: 记录状态：ENABLED\n        :type Status: str\n        :param Weight: 记录权重，值为1-100
注意：此字段可能返回 null，表示取不到有效值。\n        :type Weight: int\n        :param CreatedOn: 记录创建时间\n        :type CreatedOn: str\n        :param UpdatedOn: 记录更新时间\n        :type UpdatedOn: str\n        :param Extra: 附加信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Extra: str\n        """
        self.RecordId = None
        self.ZoneId = None
        self.SubDomain = None
        self.RecordType = None
        self.RecordValue = None
        self.TTL = None
        self.MX = None
        self.Status = None
        self.Weight = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.Extra = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.ZoneId = params.get("ZoneId")
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        self.TTL = params.get("TTL")
        self.MX = params.get("MX")
        self.Status = params.get("Status")
        self.Weight = params.get("Weight")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribePrivateZoneServiceRequest(AbstractModel):
    """SubscribePrivateZoneService请求参数结构体

    """


class SubscribePrivateZoneServiceResponse(AbstractModel):
    """SubscribePrivateZoneService返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceStatus: 私有域解析服务开通状态\n        :type ServiceStatus: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceStatus = params.get("ServiceStatus")
        self.RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """标签

    """

    def __init__(self):
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """Vpc信息

    """

    def __init__(self):
        """
        :param UniqVpcId: VpcId： vpc-xadsafsdasd\n        :type UniqVpcId: str\n        :param Region: Vpc所属地区: ap-guangzhou, ap-shanghai\n        :type Region: str\n        """
        self.UniqVpcId = None
        self.Region = None


    def _deserialize(self, params):
        self.UniqVpcId = params.get("UniqVpcId")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        