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


class AccountVpcInfo(AbstractModel):
    """私有域解析账号Vpc信息

    """

    def __init__(self):
        r"""
        :param UniqVpcId: VpcId： vpc-xadsafsdasd
        :type UniqVpcId: str
        :param Region: Vpc所属地区: ap-guangzhou, ap-shanghai
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Uin: Vpc所属账号: 123456789
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param VpcName: vpc资源名称：testname
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        """
        self.UniqVpcId = None
        self.Region = None
        self.Uin = None
        self.VpcName = None


    def _deserialize(self, params):
        self.UniqVpcId = params.get("UniqVpcId")
        self.Region = params.get("Region")
        self.Uin = params.get("Uin")
        self.VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountVpcInfoOutput(AbstractModel):
    """关联的VPC出参

    """

    def __init__(self):
        r"""
        :param Uin: 关联账户的uin
        :type Uin: str
        :param UniqVpcId: vpcid
        :type UniqVpcId: str
        :param Region: 地域
        :type Region: str
        """
        self.Uin = None
        self.UniqVpcId = None
        self.Region = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLog(AbstractModel):
    """操作日志

    """

    def __init__(self):
        r"""
        :param Resource: 日志类型
        :type Resource: str
        :param Metric: 日志表名
        :type Metric: str
        :param TotalCount: 日志总数
        :type TotalCount: int
        :param DataSet: 日志列表
        :type DataSet: list of AuditLogInfo
        """
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
        r"""
        :param Date: 时间
        :type Date: str
        :param OperatorUin: 操作人uin
        :type OperatorUin: str
        :param Content: 日志内容
        :type Content: str
        """
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
        r"""
        :param ZoneId: 私有域ID
        :type ZoneId: str
        :param RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param SubDomain: 子域名，例如 "www", "m", "@"
        :type SubDomain: str
        :param RecordValue: 记录值，例如 IP：192.168.10.2，CNAME：cname.qcloud.com.，MX：mail.qcloud.com.
        :type RecordValue: str
        :param Weight: 记录权重，值为1-100
        :type Weight: int
        :param MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :type MX: int
        :param TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :type TTL: int
        """
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
        r"""
        :param RecordId: 记录Id
        :type RecordId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class CreatePrivateZoneRequest(AbstractModel):
    """CreatePrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名，格式必须是标准的TLD
        :type Domain: str
        :param TagSet: 创建私有域的同时，为其打上标签
        :type TagSet: list of TagInfo
        :param VpcSet: 创建私有域的同时，将其关联至VPC
        :type VpcSet: list of VpcInfo
        :param Remark: 备注
        :type Remark: str
        :param DnsForwardStatus: 是否开启子域名递归, ENABLED， DISABLED。默认值为DISABLED
        :type DnsForwardStatus: str
        :param Vpcs: 创建私有域的同时，将其关联至VPC
        :type Vpcs: list of VpcInfo
        :param AccountVpcSet: 创建私有域同时绑定关联账号的VPC
        :type AccountVpcSet: list of AccountVpcInfo
        """
        self.Domain = None
        self.TagSet = None
        self.VpcSet = None
        self.Remark = None
        self.DnsForwardStatus = None
        self.Vpcs = None
        self.AccountVpcSet = None


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
        if params.get("AccountVpcSet") is not None:
            self.AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self.AccountVpcSet.append(obj)
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
        r"""
        :param ZoneId: 私有域ID, zone-xxxxxx
        :type ZoneId: str
        :param Domain: 私有域名
        :type Domain: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Date: 时间
        :type Date: str
        :param Value: 值
        :type Value: int
        """
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
        r"""
        :param ZoneId: 私有域ID
        :type ZoneId: str
        :param RecordId: 记录ID
        :type RecordId: str
        :param RecordIdSet: 记录ID数组，RecordId 优先
        :type RecordIdSet: list of str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivateZoneRequest(AbstractModel):
    """DeletePrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 私有域ID
        :type ZoneId: str
        :param ZoneIdSet: 私有域ID数组，ZoneId 优先
        :type ZoneIdSet: list of str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAuditLogRequest(AbstractModel):
    """DescribeAuditLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param TimeRangeBegin: 请求量统计起始时间
        :type TimeRangeBegin: str
        :param Filters: 筛选参数：ZoneId：私有域ID；Domain：私有域；OperatorUin：操作者账号ID
        :type Filters: list of Filter
        :param TimeRangeEnd: 请求量统计结束时间
        :type TimeRangeEnd: str
        :param Offset: 分页偏移量，从0开始
        :type Offset: int
        :param Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        """
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
        r"""
        :param Data: 操作日志列表
        :type Data: list of AuditLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ZoneTotal: 私有域解析总数
        :type ZoneTotal: int
        :param ZoneVpcCount: 私有域关联VPC数量
        :type ZoneVpcCount: int
        :param RequestTotalCount: 历史请求量总数
        :type RequestTotalCount: int
        :param FlowUsage: 流量包用量
        :type FlowUsage: list of FlowUsage
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribePrivateDNSAccountListRequest(AbstractModel):
    """DescribePrivateDNSAccountList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页偏移量，从0开始
        :type Offset: int
        :param Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param Filters: 过滤参数
        :type Filters: list of Filter
        """
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
        


class DescribePrivateDNSAccountListResponse(AbstractModel):
    """DescribePrivateDNSAccountList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 私有域解析账号数量
        :type TotalCount: int
        :param AccountSet: 私有域解析账号列表
        :type AccountSet: list of PrivateDNSAccount
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccountSet") is not None:
            self.AccountSet = []
            for item in params.get("AccountSet"):
                obj = PrivateDNSAccount()
                obj._deserialize(item)
                self.AccountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateZoneListRequest(AbstractModel):
    """DescribePrivateZoneList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页偏移量，从0开始
        :type Offset: int
        :param Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param Filters: 过滤参数
        :type Filters: list of Filter
        """
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
        r"""
        :param TotalCount: 私有域数量
        :type TotalCount: int
        :param PrivateZoneSet: 私有域列表
        :type PrivateZoneSet: list of PrivateZone
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ZoneId: 私有域ID: zone-xxxxxx
        :type ZoneId: str
        :param Filters: 过滤参数
        :type Filters: list of Filter
        :param Offset: 分页偏移量，从0开始
        :type Offset: int
        :param Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        """
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
        r"""
        :param TotalCount: 解析记录数量
        :type TotalCount: int
        :param RecordSet: 解析记录列表
        :type RecordSet: list of PrivateZoneRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ZoneId: 域名，格式必须是标准的TLD
        :type ZoneId: str
        """
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
        r"""
        :param PrivateZone: 私有域详情
        :type PrivateZone: :class:`tencentcloud.privatedns.v20201028.models.PrivateZone`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ServiceStatus: 私有域解析服务开通状态。ENABLED已开通，DISABLED未开通
        :type ServiceStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceStatus = params.get("ServiceStatus")
        self.RequestId = params.get("RequestId")


class DescribeRequestDataRequest(AbstractModel):
    """DescribeRequestData请求参数结构体

    """

    def __init__(self):
        r"""
        :param TimeRangeBegin: 请求量统计起始时间，格式：2020-11-22 00:00:00
        :type TimeRangeBegin: str
        :param Filters: 筛选参数：
        :type Filters: list of Filter
        :param TimeRangeEnd: 请求量统计结束时间，格式：2020-11-22 23:59:59
        :type TimeRangeEnd: str
        """
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
        r"""
        :param Data: 请求量统计表
        :type Data: list of MetricData
        :param Interval: 请求量单位时间: Day：天，Hour：小时
        :type Interval: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Name: 参数名
        :type Name: str
        :param Values: 参数值数组
        :type Values: list of str
        """
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
        r"""
        :param FlowType: 流量包类型：ZONE 私有域；TRAFFIC 解析流量包
        :type FlowType: str
        :param TotalQuantity: 流量包总额度
        :type TotalQuantity: int
        :param AvailableQuantity: 流量包可用额度
        :type AvailableQuantity: int
        """
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
        r"""
        :param Resource: 资源描述
        :type Resource: str
        :param Metric: 表名
        :type Metric: str
        :param DataSet: 表数据
        :type DataSet: list of DatePoint
        """
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
        r"""
        :param ZoneId: 私有域ID
        :type ZoneId: str
        :param RecordId: 记录ID
        :type RecordId: str
        :param RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param SubDomain: 子域名，例如 "www", "m", "@"
        :type SubDomain: str
        :param RecordValue: 记录值，例如 IP：192.168.10.2，CNAME：cname.qcloud.com.，MX：mail.qcloud.com.
        :type RecordValue: str
        :param Weight: 记录权重，值为1-100
        :type Weight: int
        :param MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :type MX: int
        :param TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :type TTL: int
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateZoneRequest(AbstractModel):
    """ModifyPrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 私有域ID
        :type ZoneId: str
        :param Remark: 备注
        :type Remark: str
        :param DnsForwardStatus: 是否开启子域名递归, ENABLED， DISABLED
        :type DnsForwardStatus: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateZoneVpcRequest(AbstractModel):
    """ModifyPrivateZoneVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 私有域ID
        :type ZoneId: str
        :param VpcSet: 私有域关联的全部VPC列表
        :type VpcSet: list of VpcInfo
        :param AccountVpcSet: 私有域账号关联的全部VPC列表
        :type AccountVpcSet: list of AccountVpcInfo
        """
        self.ZoneId = None
        self.VpcSet = None
        self.AccountVpcSet = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self.AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self.AccountVpcSet.append(obj)
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
        r"""
        :param ZoneId: 私有域ID, zone-xxxxxx
        :type ZoneId: str
        :param VpcSet: 解析域关联的VPC列表
        :type VpcSet: list of VpcInfo
        :param AccountVpcSet: 私有域账号关联的全部VPC列表
        :type AccountVpcSet: list of AccountVpcInfoOutput
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ZoneId = None
        self.VpcSet = None
        self.AccountVpcSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self.AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfoOutput()
                obj._deserialize(item)
                self.AccountVpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class PrivateDNSAccount(AbstractModel):
    """私有域解析账号

    """

    def __init__(self):
        r"""
        :param Uin: 主账号Uin
        :type Uin: str
        :param Account: 主账号名称
        :type Account: str
        :param Nickname: 用户昵称
        :type Nickname: str
        """
        self.Uin = None
        self.Account = None
        self.Nickname = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Account = params.get("Account")
        self.Nickname = params.get("Nickname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateZone(AbstractModel):
    """私有域信息

    """

    def __init__(self):
        r"""
        :param ZoneId: 私有域id: zone-xxxxxxxx
        :type ZoneId: str
        :param OwnerUin: 域名所有者uin
        :type OwnerUin: int
        :param Domain: 私有域名
        :type Domain: str
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param UpdatedOn: 修改时间
        :type UpdatedOn: str
        :param RecordCount: 记录数
        :type RecordCount: int
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param VpcSet: 绑定的Vpc列表
        :type VpcSet: list of VpcInfo
        :param Status: 私有域状态：正常解析：ENABLED, 暂停解析：SUSPEND, 锁定：FROZEN
        :type Status: str
        :param DnsForwardStatus: 域名递归解析状态：开通：ENABLED, 关闭，DISABLED
        :type DnsForwardStatus: str
        :param Tags: 标签键值对集合
        :type Tags: list of TagInfo
        :param AccountVpcSet: 绑定的关联账号的vpc列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountVpcSet: list of AccountVpcInfoOutput
        """
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
        self.AccountVpcSet = None


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
        if params.get("AccountVpcSet") is not None:
            self.AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfoOutput()
                obj._deserialize(item)
                self.AccountVpcSet.append(obj)
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
        r"""
        :param RecordId: 记录id
        :type RecordId: str
        :param ZoneId: 私有域id: zone-xxxxxxxx
        :type ZoneId: str
        :param SubDomain: 子域名
        :type SubDomain: str
        :param RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param RecordValue: 记录值
        :type RecordValue: str
        :param TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :type TTL: int
        :param MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
注意：此字段可能返回 null，表示取不到有效值。
        :type MX: int
        :param Status: 记录状态：ENABLED
        :type Status: str
        :param Weight: 记录权重，值为1-100
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param CreatedOn: 记录创建时间
        :type CreatedOn: str
        :param UpdatedOn: 记录更新时间
        :type UpdatedOn: str
        :param Extra: 附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        """
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
        r"""
        :param ServiceStatus: 私有域解析服务开通状态
        :type ServiceStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceStatus = params.get("ServiceStatus")
        self.RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
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
        r"""
        :param UniqVpcId: VpcId： vpc-xadsafsdasd
        :type UniqVpcId: str
        :param Region: Vpc所属地区: ap-guangzhou, ap-shanghai
        :type Region: str
        """
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
        