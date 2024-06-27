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


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID数组。
        :type InstanceIds: list of str
        :param _InstanceNames: 实例名称，支持模糊搜索。
        :type InstanceNames: list of str
        :param _InstanceKeys: 实例模糊搜索字段。
        :type InstanceKeys: list of str
        :param _Status: 根据状态获取实例， 为空则获取全部非隔离和非下线的实例。
        :type Status: list of str
        :param _EngineNames: 按照引擎筛选实例。
        :type EngineNames: list of str
        :param _EngineVersions: 按照版本筛选实例。
        :type EngineVersions: list of str
        :param _CreateAt: 按照创建时间筛选实例。
        :type CreateAt: str
        :param _Zones: 按照可用区筛选实例。
        :type Zones: list of str
        :param _OrderBy: 排序字段。
        :type OrderBy: str
        :param _OrderDirection: 排序方式。
        :type OrderDirection: str
        :param _Offset: 查询开始位置。
        :type Offset: int
        :param _Limit: 列表查询数量。
        :type Limit: int
        :param _ResourceTags: 按照标签筛选实例
        :type ResourceTags: list of Tag
        """
        self._InstanceIds = None
        self._InstanceNames = None
        self._InstanceKeys = None
        self._Status = None
        self._EngineNames = None
        self._EngineVersions = None
        self._CreateAt = None
        self._Zones = None
        self._OrderBy = None
        self._OrderDirection = None
        self._Offset = None
        self._Limit = None
        self._ResourceTags = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def InstanceKeys(self):
        return self._InstanceKeys

    @InstanceKeys.setter
    def InstanceKeys(self, InstanceKeys):
        self._InstanceKeys = InstanceKeys

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EngineNames(self):
        return self._EngineNames

    @EngineNames.setter
    def EngineNames(self, EngineNames):
        self._EngineNames = EngineNames

    @property
    def EngineVersions(self):
        return self._EngineVersions

    @EngineVersions.setter
    def EngineVersions(self, EngineVersions):
        self._EngineVersions = EngineVersions

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._InstanceKeys = params.get("InstanceKeys")
        self._Status = params.get("Status")
        self._EngineNames = params.get("EngineNames")
        self._EngineVersions = params.get("EngineVersions")
        self._CreateAt = params.get("CreateAt")
        self._Zones = params.get("Zones")
        self._OrderBy = params.get("OrderBy")
        self._OrderDirection = params.get("OrderDirection")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 实例列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of InstanceInfo
        :param _TotalCount: 实例总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """实例信息，用于实例列表

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Name: 实例自定义名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _AppId: 用户APPID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Region: 地域。
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Zone: 可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _Product: 产品。
注意：此字段可能返回 null，表示取不到有效值。
        :type Product: str
        :param _Networks: 网络信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Networks: list of Network
        :param _ShardNum: 分片信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardNum: int
        :param _ReplicaNum: 副本数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplicaNum: int
        :param _Cpu: CPU.
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: float
        :param _Memory: 内存。
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: float
        :param _Disk: 磁盘。
注意：此字段可能返回 null，表示取不到有效值。
        :type Disk: int
        :param _HealthScore: 健康得分。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthScore: float
        :param _Warning: 异常告警。
注意：此字段可能返回 null，表示取不到有效值。
        :type Warning: int
        :param _Project: 所属项目。
注意：此字段可能返回 null，表示取不到有效值。
        :type Project: str
        :param _ResourceTags: 所属标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTags: list of Tag
        :param _CreatedAt: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _Status: 资源状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _EngineName: 引擎名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineName: str
        :param _EngineVersion: 引擎版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineVersion: str
        :param _PayMode: 计费模式。
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param _Extend: 差异化扩展信息, json格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Extend: str
        :param _ExpiredAt: 过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredAt: str
        :param _IsNoExpired: 是否不过期(永久)。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNoExpired: bool
        :param _WanAddress: 外网地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type WanAddress: str
        :param _IsolateAt: 隔离时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateAt: str
        :param _AutoRenew: 是否自动续费。0: 不自动续费(可以支持特权不停服)；1:自动续费；2:到期不续费.
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenew: int
        """
        self._InstanceId = None
        self._Name = None
        self._AppId = None
        self._Region = None
        self._Zone = None
        self._Product = None
        self._Networks = None
        self._ShardNum = None
        self._ReplicaNum = None
        self._Cpu = None
        self._Memory = None
        self._Disk = None
        self._HealthScore = None
        self._Warning = None
        self._Project = None
        self._ResourceTags = None
        self._CreatedAt = None
        self._Status = None
        self._EngineName = None
        self._EngineVersion = None
        self._PayMode = None
        self._Extend = None
        self._ExpiredAt = None
        self._IsNoExpired = None
        self._WanAddress = None
        self._IsolateAt = None
        self._AutoRenew = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Networks(self):
        return self._Networks

    @Networks.setter
    def Networks(self, Networks):
        self._Networks = Networks

    @property
    def ShardNum(self):
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def ReplicaNum(self):
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Disk(self):
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def HealthScore(self):
        return self._HealthScore

    @HealthScore.setter
    def HealthScore(self, HealthScore):
        self._HealthScore = HealthScore

    @property
    def Warning(self):
        return self._Warning

    @Warning.setter
    def Warning(self, Warning):
        self._Warning = Warning

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EngineName(self):
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Extend(self):
        return self._Extend

    @Extend.setter
    def Extend(self, Extend):
        self._Extend = Extend

    @property
    def ExpiredAt(self):
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def IsNoExpired(self):
        return self._IsNoExpired

    @IsNoExpired.setter
    def IsNoExpired(self, IsNoExpired):
        self._IsNoExpired = IsNoExpired

    @property
    def WanAddress(self):
        return self._WanAddress

    @WanAddress.setter
    def WanAddress(self, WanAddress):
        self._WanAddress = WanAddress

    @property
    def IsolateAt(self):
        return self._IsolateAt

    @IsolateAt.setter
    def IsolateAt(self, IsolateAt):
        self._IsolateAt = IsolateAt

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Product = params.get("Product")
        if params.get("Networks") is not None:
            self._Networks = []
            for item in params.get("Networks"):
                obj = Network()
                obj._deserialize(item)
                self._Networks.append(obj)
        self._ShardNum = params.get("ShardNum")
        self._ReplicaNum = params.get("ReplicaNum")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Disk = params.get("Disk")
        self._HealthScore = params.get("HealthScore")
        self._Warning = params.get("Warning")
        self._Project = params.get("Project")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._CreatedAt = params.get("CreatedAt")
        self._Status = params.get("Status")
        self._EngineName = params.get("EngineName")
        self._EngineVersion = params.get("EngineVersion")
        self._PayMode = params.get("PayMode")
        self._Extend = params.get("Extend")
        self._ExpiredAt = params.get("ExpiredAt")
        self._IsNoExpired = params.get("IsNoExpired")
        self._WanAddress = params.get("WanAddress")
        self._IsolateAt = params.get("IsolateAt")
        self._AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Network(AbstractModel):
    """网络信息

    """

    def __init__(self):
        r"""
        :param _VpcId: VpcId(VPC网络下有效)
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网Id(VPC网络下有效)。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Vip: 内网访问IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _Port: 内网访问Port。
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._Vip = None
        self._Port = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vip = params.get("Vip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        