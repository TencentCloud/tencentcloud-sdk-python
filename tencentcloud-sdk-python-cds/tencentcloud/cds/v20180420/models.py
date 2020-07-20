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


class CdsAuditInstance(AbstractModel):
    """数据安全产品实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param AppId: 用户AppId
        :type AppId: str
        :param Uin: 用户Uin
        :type Uin: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param RenewFlag: 续费标识
        :type RenewFlag: int
        :param Region: 所属地域
        :type Region: str
        :param PayMode: 付费模式（数据安全审计只支持预付费：1）
        :type PayMode: int
        :param Status: 实例状态： 0，未生效；1：正常运行； 2：被隔离； 3，已过期
        :type Status: int
        :param IsolatedTimestamp: 实例被隔离时间，格式：yyyy-mm-dd HH:ii:ss
        :type IsolatedTimestamp: str
        :param CreateTime: 实例创建时间，格式： yyyy-mm-dd HH:ii:ss
        :type CreateTime: str
        :param ExpireTime: 实例过期时间，格式：yyyy-mm-dd HH:ii:ss
        :type ExpireTime: str
        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param PublicIp: 实例公网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param PrivateIp: 实例私网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param InstanceType: 实例类型（版本）
        :type InstanceType: str
        :param Pdomain: 实例域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Pdomain: str
        """
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


class DbauditTypesInfo(AbstractModel):
    """数据安全审计产品规格信息

    """

    def __init__(self):
        """
        :param InstanceVersionName: 规格描述
        :type InstanceVersionName: str
        :param InstanceVersionKey: 规格名称
        :type InstanceVersionKey: str
        :param Qps: 最大吞吐量
        :type Qps: int
        :param MaxInstances: 最大实例数
        :type MaxInstances: int
        :param InsertSpeed: 入库速率（每小时）
        :type InsertSpeed: int
        :param OnlineStorageCapacity: 最大在线存储量，单位：条
        :type OnlineStorageCapacity: int
        :param ArchivingStorageCapacity: 最大归档存储量，单位：条
        :type ArchivingStorageCapacity: int
        """
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


class DescribeDasbImageIdsRequest(AbstractModel):
    """DescribeDasbImageIds请求参数结构体

    """


class DescribeDasbImageIdsResponse(AbstractModel):
    """DescribeDasbImageIds返回参数结构体

    """

    def __init__(self):
        """
        :param BaseImageId: 基础镜像ID
        :type BaseImageId: str
        :param AiImageId: AI镜像ID
        :type AiImageId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param DbauditTypesSet: 数据安全审计产品规格信息列表
        :type DbauditTypesSet: list of DbauditTypesInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param SearchRegion: 查询条件地域
        :type SearchRegion: str
        :param Limit: 限制数目，默认10， 最大50
        :type Limit: int
        :param Offset: 偏移量，默认1
        :type Offset: int
        """
        self.SearchRegion = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.SearchRegion = params.get("SearchRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDbauditInstancesResponse(AbstractModel):
    """DescribeDbauditInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总实例数
        :type TotalCount: int
        :param CdsAuditInstanceSet: 数据安全审计实例信息列表
        :type CdsAuditInstanceSet: list of CdsAuditInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param RegionSet: 可售卖地域信息列表
        :type RegionSet: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param InstanceVersion: 实例规格，取值范围： cdsaudit，cdsaudit_adv， cdsaudit_ent 分别为合规版，高级版，企业版
        :type InstanceVersion: str
        :param InquiryType: 询价类型： renew，续费；newbuy，新购
        :type InquiryType: str
        :param TimeSpan: 购买实例的时长。取值范围：1（y/m），2（y/m）,，3（y/m），4（m）， 5（m），6（m）， 7（m），8（m），9（m）， 10（m）
        :type TimeSpan: int
        :param TimeUnit: 购买时长单位，y：年；m：月
        :type TimeUnit: str
        :param ServiceRegion: 实例所在地域
        :type ServiceRegion: str
        """
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


class InquiryPriceDbauditInstanceResponse(AbstractModel):
    """InquiryPriceDbauditInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TotalPrice: 总价，单位：元
        :type TotalPrice: float
        :param RealTotalCost: 真实价钱，预支费用的折扣价，单位：元
        :type RealTotalCost: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param AutoRenewFlag: 0，表示默认状态(用户未设置，即初始状态)；1，表示自动续费；2，表示明确不自动续费
        :type AutoRenewFlag: int
        """
        self.InstanceId = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")


class ModifyDbauditInstancesRenewFlagResponse(AbstractModel):
    """ModifyDbauditInstancesRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """数盾地域信息

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
        :type RegionId: int
        :param Region: 地域名称
        :type Region: str
        :param RegionName: 地域描述
        :type RegionName: str
        :param RegionState: 地域可用状态
        :type RegionState: int
        """
        self.RegionId = None
        self.Region = None
        self.RegionName = None
        self.RegionState = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionState = params.get("RegionState")