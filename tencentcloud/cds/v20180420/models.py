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
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AppId: 用户AppId
        :type AppId: str
        :param _Uin: 用户Uin
        :type Uin: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _RenewFlag: 续费标识
        :type RenewFlag: int
        :param _Region: 所属地域
        :type Region: str
        :param _PayMode: 付费模式（数据安全审计只支持预付费：1）
        :type PayMode: int
        :param _Status: 实例状态： 0，未生效；1：正常运行； 2：被隔离； 3，已过期
        :type Status: int
        :param _IsolatedTimestamp: 实例被隔离时间，格式：yyyy-mm-dd HH:ii:ss
        :type IsolatedTimestamp: str
        :param _CreateTime: 实例创建时间，格式： yyyy-mm-dd HH:ii:ss
        :type CreateTime: str
        :param _ExpireTime: 实例过期时间，格式：yyyy-mm-dd HH:ii:ss
        :type ExpireTime: str
        :param _InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _PublicIp: 实例公网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param _PrivateIp: 实例私网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _InstanceType: 实例类型（版本）
        :type InstanceType: str
        :param _Pdomain: 实例域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Pdomain: str
        """
        self._InstanceId = None
        self._AppId = None
        self._Uin = None
        self._ProjectId = None
        self._RenewFlag = None
        self._Region = None
        self._PayMode = None
        self._Status = None
        self._IsolatedTimestamp = None
        self._CreateTime = None
        self._ExpireTime = None
        self._InstanceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._InstanceType = None
        self._Pdomain = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsolatedTimestamp(self):
        return self._IsolatedTimestamp

    @IsolatedTimestamp.setter
    def IsolatedTimestamp(self, IsolatedTimestamp):
        self._IsolatedTimestamp = IsolatedTimestamp

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PublicIp(self):
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Pdomain(self):
        return self._Pdomain

    @Pdomain.setter
    def Pdomain(self, Pdomain):
        self._Pdomain = Pdomain


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._ProjectId = params.get("ProjectId")
        self._RenewFlag = params.get("RenewFlag")
        self._Region = params.get("Region")
        self._PayMode = params.get("PayMode")
        self._Status = params.get("Status")
        self._IsolatedTimestamp = params.get("IsolatedTimestamp")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._InstanceName = params.get("InstanceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._InstanceType = params.get("InstanceType")
        self._Pdomain = params.get("Pdomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbauditTypesInfo(AbstractModel):
    """数据安全审计产品规格信息

    """

    def __init__(self):
        r"""
        :param _InstanceVersionName: 规格描述
        :type InstanceVersionName: str
        :param _InstanceVersionKey: 规格名称
        :type InstanceVersionKey: str
        :param _Qps: 最大吞吐量
        :type Qps: int
        :param _MaxInstances: 最大实例数
        :type MaxInstances: int
        :param _InsertSpeed: 入库速率（每小时）
        :type InsertSpeed: int
        :param _OnlineStorageCapacity: 最大在线存储量，单位：条
        :type OnlineStorageCapacity: int
        :param _ArchivingStorageCapacity: 最大归档存储量，单位：条
        :type ArchivingStorageCapacity: int
        """
        self._InstanceVersionName = None
        self._InstanceVersionKey = None
        self._Qps = None
        self._MaxInstances = None
        self._InsertSpeed = None
        self._OnlineStorageCapacity = None
        self._ArchivingStorageCapacity = None

    @property
    def InstanceVersionName(self):
        return self._InstanceVersionName

    @InstanceVersionName.setter
    def InstanceVersionName(self, InstanceVersionName):
        self._InstanceVersionName = InstanceVersionName

    @property
    def InstanceVersionKey(self):
        return self._InstanceVersionKey

    @InstanceVersionKey.setter
    def InstanceVersionKey(self, InstanceVersionKey):
        self._InstanceVersionKey = InstanceVersionKey

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def MaxInstances(self):
        return self._MaxInstances

    @MaxInstances.setter
    def MaxInstances(self, MaxInstances):
        self._MaxInstances = MaxInstances

    @property
    def InsertSpeed(self):
        return self._InsertSpeed

    @InsertSpeed.setter
    def InsertSpeed(self, InsertSpeed):
        self._InsertSpeed = InsertSpeed

    @property
    def OnlineStorageCapacity(self):
        return self._OnlineStorageCapacity

    @OnlineStorageCapacity.setter
    def OnlineStorageCapacity(self, OnlineStorageCapacity):
        self._OnlineStorageCapacity = OnlineStorageCapacity

    @property
    def ArchivingStorageCapacity(self):
        return self._ArchivingStorageCapacity

    @ArchivingStorageCapacity.setter
    def ArchivingStorageCapacity(self, ArchivingStorageCapacity):
        self._ArchivingStorageCapacity = ArchivingStorageCapacity


    def _deserialize(self, params):
        self._InstanceVersionName = params.get("InstanceVersionName")
        self._InstanceVersionKey = params.get("InstanceVersionKey")
        self._Qps = params.get("Qps")
        self._MaxInstances = params.get("MaxInstances")
        self._InsertSpeed = params.get("InsertSpeed")
        self._OnlineStorageCapacity = params.get("OnlineStorageCapacity")
        self._ArchivingStorageCapacity = params.get("ArchivingStorageCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDasbImageIdsRequest(AbstractModel):
    """DescribeDasbImageIds请求参数结构体

    """


class DescribeDasbImageIdsResponse(AbstractModel):
    """DescribeDasbImageIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BaseImageId: 基础镜像ID
        :type BaseImageId: str
        :param _AiImageId: AI镜像ID
        :type AiImageId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BaseImageId = None
        self._AiImageId = None
        self._RequestId = None

    @property
    def BaseImageId(self):
        return self._BaseImageId

    @BaseImageId.setter
    def BaseImageId(self, BaseImageId):
        self._BaseImageId = BaseImageId

    @property
    def AiImageId(self):
        return self._AiImageId

    @AiImageId.setter
    def AiImageId(self, AiImageId):
        self._AiImageId = AiImageId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BaseImageId = params.get("BaseImageId")
        self._AiImageId = params.get("AiImageId")
        self._RequestId = params.get("RequestId")


class DescribeDbauditInstanceTypeRequest(AbstractModel):
    """DescribeDbauditInstanceType请求参数结构体

    """


class DescribeDbauditInstanceTypeResponse(AbstractModel):
    """DescribeDbauditInstanceType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DbauditTypesSet: 数据安全审计产品规格信息列表
        :type DbauditTypesSet: list of DbauditTypesInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DbauditTypesSet = None
        self._RequestId = None

    @property
    def DbauditTypesSet(self):
        return self._DbauditTypesSet

    @DbauditTypesSet.setter
    def DbauditTypesSet(self, DbauditTypesSet):
        self._DbauditTypesSet = DbauditTypesSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DbauditTypesSet") is not None:
            self._DbauditTypesSet = []
            for item in params.get("DbauditTypesSet"):
                obj = DbauditTypesInfo()
                obj._deserialize(item)
                self._DbauditTypesSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDbauditInstancesRequest(AbstractModel):
    """DescribeDbauditInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchRegion: 查询条件地域
        :type SearchRegion: str
        :param _Limit: 限制数目，默认10， 最大50
        :type Limit: int
        :param _Offset: 偏移量，默认1
        :type Offset: int
        """
        self._SearchRegion = None
        self._Limit = None
        self._Offset = None

    @property
    def SearchRegion(self):
        return self._SearchRegion

    @SearchRegion.setter
    def SearchRegion(self, SearchRegion):
        self._SearchRegion = SearchRegion

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._SearchRegion = params.get("SearchRegion")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbauditInstancesResponse(AbstractModel):
    """DescribeDbauditInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总实例数
        :type TotalCount: int
        :param _CdsAuditInstanceSet: 数据安全审计实例信息列表
        :type CdsAuditInstanceSet: list of CdsAuditInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CdsAuditInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CdsAuditInstanceSet(self):
        return self._CdsAuditInstanceSet

    @CdsAuditInstanceSet.setter
    def CdsAuditInstanceSet(self, CdsAuditInstanceSet):
        self._CdsAuditInstanceSet = CdsAuditInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CdsAuditInstanceSet") is not None:
            self._CdsAuditInstanceSet = []
            for item in params.get("CdsAuditInstanceSet"):
                obj = CdsAuditInstance()
                obj._deserialize(item)
                self._CdsAuditInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDbauditUsedRegionsRequest(AbstractModel):
    """DescribeDbauditUsedRegions请求参数结构体

    """


class DescribeDbauditUsedRegionsResponse(AbstractModel):
    """DescribeDbauditUsedRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionSet: 可售卖地域信息列表
        :type RegionSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class InquiryPriceDbauditInstanceRequest(AbstractModel):
    """InquiryPriceDbauditInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceVersion: 实例规格，取值范围： cdsaudit，cdsaudit_adv， cdsaudit_ent 分别为合规版，高级版，企业版
        :type InstanceVersion: str
        :param _InquiryType: 询价类型： renew，续费；newbuy，新购
        :type InquiryType: str
        :param _TimeSpan: 购买实例的时长。取值范围：1（y/m），2（y/m）,，3（y/m），4（m）， 5（m），6（m）， 7（m），8（m），9（m）， 10（m）
        :type TimeSpan: int
        :param _TimeUnit: 购买时长单位，y：年；m：月
        :type TimeUnit: str
        :param _ServiceRegion: 实例所在地域
        :type ServiceRegion: str
        """
        self._InstanceVersion = None
        self._InquiryType = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._ServiceRegion = None

    @property
    def InstanceVersion(self):
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def InquiryType(self):
        return self._InquiryType

    @InquiryType.setter
    def InquiryType(self, InquiryType):
        self._InquiryType = InquiryType

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def ServiceRegion(self):
        return self._ServiceRegion

    @ServiceRegion.setter
    def ServiceRegion(self, ServiceRegion):
        self._ServiceRegion = ServiceRegion


    def _deserialize(self, params):
        self._InstanceVersion = params.get("InstanceVersion")
        self._InquiryType = params.get("InquiryType")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._ServiceRegion = params.get("ServiceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceDbauditInstanceResponse(AbstractModel):
    """InquiryPriceDbauditInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalPrice: 总价，单位：元
        :type TotalPrice: float
        :param _RealTotalCost: 真实价钱，预支费用的折扣价，单位：元
        :type RealTotalCost: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalPrice = None
        self._RealTotalCost = None
        self._RequestId = None

    @property
    def TotalPrice(self):
        return self._TotalPrice

    @TotalPrice.setter
    def TotalPrice(self, TotalPrice):
        self._TotalPrice = TotalPrice

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalPrice = params.get("TotalPrice")
        self._RealTotalCost = params.get("RealTotalCost")
        self._RequestId = params.get("RequestId")


class ModifyDbauditInstancesRenewFlagRequest(AbstractModel):
    """ModifyDbauditInstancesRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AutoRenewFlag: 0，表示默认状态(用户未设置，即初始状态)；1，表示自动续费；2，表示明确不自动续费
        :type AutoRenewFlag: int
        """
        self._InstanceId = None
        self._AutoRenewFlag = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDbauditInstancesRenewFlagResponse(AbstractModel):
    """ModifyDbauditInstancesRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """数盾地域信息

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _Region: 地域名称
        :type Region: str
        :param _RegionName: 地域描述
        :type RegionName: str
        :param _RegionState: 地域可用状态
        :type RegionState: int
        """
        self._RegionId = None
        self._Region = None
        self._RegionName = None
        self._RegionState = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        