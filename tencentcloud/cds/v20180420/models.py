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


class CdsAuditInstance(AbstractModel):
    """数据安全产品实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param AppId: 用户AppId\n        :type AppId: str\n        :param Uin: 用户Uin\n        :type Uin: str\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param RenewFlag: 续费标识\n        :type RenewFlag: int\n        :param Region: 所属地域\n        :type Region: str\n        :param PayMode: 付费模式（数据安全审计只支持预付费：1）\n        :type PayMode: int\n        :param Status: 实例状态： 0，未生效；1：正常运行； 2：被隔离； 3，已过期\n        :type Status: int\n        :param IsolatedTimestamp: 实例被隔离时间，格式：yyyy-mm-dd HH:ii:ss\n        :type IsolatedTimestamp: str\n        :param CreateTime: 实例创建时间，格式： yyyy-mm-dd HH:ii:ss\n        :type CreateTime: str\n        :param ExpireTime: 实例过期时间，格式：yyyy-mm-dd HH:ii:ss\n        :type ExpireTime: str\n        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param PublicIp: 实例公网IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type PublicIp: str\n        :param PrivateIp: 实例私网IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateIp: str\n        :param InstanceType: 实例类型（版本）\n        :type InstanceType: str\n        :param Pdomain: 实例域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Pdomain: str\n        """
        self.InstanceId = None
        self.AppId = None
        self.Uin = None
        self.ProjectId = None
        self.RenewFlag = None
        self.Region = None
        self.PayMode = None
        self.Status = None
        self.IsolatedTimestamp = None
        self.CreateTime = None
        self.ExpireTime = None
        self.InstanceName = None
        self.PublicIp = None
        self.PrivateIp = None
        self.InstanceType = None
        self.Pdomain = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.ProjectId = params.get("ProjectId")
        self.RenewFlag = params.get("RenewFlag")
        self.Region = params.get("Region")
        self.PayMode = params.get("PayMode")
        self.Status = params.get("Status")
        self.IsolatedTimestamp = params.get("IsolatedTimestamp")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.InstanceName = params.get("InstanceName")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.InstanceType = params.get("InstanceType")
        self.Pdomain = params.get("Pdomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbauditTypesInfo(AbstractModel):
    """数据安全审计产品规格信息

    """

    def __init__(self):
        """
        :param InstanceVersionName: 规格描述\n        :type InstanceVersionName: str\n        :param InstanceVersionKey: 规格名称\n        :type InstanceVersionKey: str\n        :param Qps: 最大吞吐量\n        :type Qps: int\n        :param MaxInstances: 最大实例数\n        :type MaxInstances: int\n        :param InsertSpeed: 入库速率（每小时）\n        :type InsertSpeed: int\n        :param OnlineStorageCapacity: 最大在线存储量，单位：条\n        :type OnlineStorageCapacity: int\n        :param ArchivingStorageCapacity: 最大归档存储量，单位：条\n        :type ArchivingStorageCapacity: int\n        """
        self.InstanceVersionName = None
        self.InstanceVersionKey = None
        self.Qps = None
        self.MaxInstances = None
        self.InsertSpeed = None
        self.OnlineStorageCapacity = None
        self.ArchivingStorageCapacity = None


    def _deserialize(self, params):
        self.InstanceVersionName = params.get("InstanceVersionName")
        self.InstanceVersionKey = params.get("InstanceVersionKey")
        self.Qps = params.get("Qps")
        self.MaxInstances = params.get("MaxInstances")
        self.InsertSpeed = params.get("InsertSpeed")
        self.OnlineStorageCapacity = params.get("OnlineStorageCapacity")
        self.ArchivingStorageCapacity = params.get("ArchivingStorageCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDasbImageIdsRequest(AbstractModel):
    """DescribeDasbImageIds请求参数结构体

    """


class DescribeDasbImageIdsResponse(AbstractModel):
    """DescribeDasbImageIds返回参数结构体

    """

    def __init__(self):
        """
        :param BaseImageId: 基础镜像ID\n        :type BaseImageId: str\n        :param AiImageId: AI镜像ID\n        :type AiImageId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BaseImageId = None
        self.AiImageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BaseImageId = params.get("BaseImageId")
        self.AiImageId = params.get("AiImageId")
        self.RequestId = params.get("RequestId")


class DescribeDbauditInstanceTypeRequest(AbstractModel):
    """DescribeDbauditInstanceType请求参数结构体

    """


class DescribeDbauditInstanceTypeResponse(AbstractModel):
    """DescribeDbauditInstanceType返回参数结构体

    """

    def __init__(self):
        """
        :param DbauditTypesSet: 数据安全审计产品规格信息列表\n        :type DbauditTypesSet: list of DbauditTypesInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DbauditTypesSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DbauditTypesSet") is not None:
            self.DbauditTypesSet = []
            for item in params.get("DbauditTypesSet"):
                obj = DbauditTypesInfo()
                obj._deserialize(item)
                self.DbauditTypesSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDbauditInstancesRequest(AbstractModel):
    """DescribeDbauditInstances请求参数结构体

    """

    def __init__(self):
        """
        :param SearchRegion: 查询条件地域\n        :type SearchRegion: str\n        :param Limit: 限制数目，默认10， 最大50\n        :type Limit: int\n        :param Offset: 偏移量，默认1\n        :type Offset: int\n        """
        self.SearchRegion = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.SearchRegion = params.get("SearchRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbauditInstancesResponse(AbstractModel):
    """DescribeDbauditInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总实例数\n        :type TotalCount: int\n        :param CdsAuditInstanceSet: 数据安全审计实例信息列表\n        :type CdsAuditInstanceSet: list of CdsAuditInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.CdsAuditInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CdsAuditInstanceSet") is not None:
            self.CdsAuditInstanceSet = []
            for item in params.get("CdsAuditInstanceSet"):
                obj = CdsAuditInstance()
                obj._deserialize(item)
                self.CdsAuditInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDbauditUsedRegionsRequest(AbstractModel):
    """DescribeDbauditUsedRegions请求参数结构体

    """


class DescribeDbauditUsedRegionsResponse(AbstractModel):
    """DescribeDbauditUsedRegions返回参数结构体

    """

    def __init__(self):
        """
        :param RegionSet: 可售卖地域信息列表\n        :type RegionSet: list of RegionInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class InquiryPriceDbauditInstanceRequest(AbstractModel):
    """InquiryPriceDbauditInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceVersion: 实例规格，取值范围： cdsaudit，cdsaudit_adv， cdsaudit_ent 分别为合规版，高级版，企业版\n        :type InstanceVersion: str\n        :param InquiryType: 询价类型： renew，续费；newbuy，新购\n        :type InquiryType: str\n        :param TimeSpan: 购买实例的时长。取值范围：1（y/m），2（y/m）,，3（y/m），4（m）， 5（m），6（m）， 7（m），8（m），9（m）， 10（m）\n        :type TimeSpan: int\n        :param TimeUnit: 购买时长单位，y：年；m：月\n        :type TimeUnit: str\n        :param ServiceRegion: 实例所在地域\n        :type ServiceRegion: str\n        """
        self.InstanceVersion = None
        self.InquiryType = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.ServiceRegion = None


    def _deserialize(self, params):
        self.InstanceVersion = params.get("InstanceVersion")
        self.InquiryType = params.get("InquiryType")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.ServiceRegion = params.get("ServiceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceDbauditInstanceResponse(AbstractModel):
    """InquiryPriceDbauditInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TotalPrice: 总价，单位：元\n        :type TotalPrice: float\n        :param RealTotalCost: 真实价钱，预支费用的折扣价，单位：元\n        :type RealTotalCost: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalPrice = None
        self.RealTotalCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalPrice = params.get("TotalPrice")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RequestId = params.get("RequestId")


class ModifyDbauditInstancesRenewFlagRequest(AbstractModel):
    """ModifyDbauditInstancesRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param AutoRenewFlag: 0，表示默认状态(用户未设置，即初始状态)；1，表示自动续费；2，表示明确不自动续费\n        :type AutoRenewFlag: int\n        """
        self.InstanceId = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDbauditInstancesRenewFlagResponse(AbstractModel):
    """ModifyDbauditInstancesRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """数盾地域信息

    """

    def __init__(self):
        """
        :param RegionId: 地域ID\n        :type RegionId: int\n        :param Region: 地域名称\n        :type Region: str\n        :param RegionName: 地域描述\n        :type RegionName: str\n        :param RegionState: 地域可用状态\n        :type RegionState: int\n        """
        self.RegionId = None
        self.Region = None
        self.RegionName = None
        self.RegionState = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        