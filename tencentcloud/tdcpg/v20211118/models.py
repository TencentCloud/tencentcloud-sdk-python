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


class Account(AbstractModel):
    """数据库账户信息

    """

    def __init__(self):
        r"""
        :param _AccountName: 数据库账号名
        :type AccountName: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _AccountDescription: 数据库账号描述
        :type AccountDescription: str
        :param _CreateTime: 数据库账号创建时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type CreateTime: str
        :param _UpdateTime: 数据库账号信息更新时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type UpdateTime: str
        """
        self._AccountName = None
        self._ClusterId = None
        self._AccountDescription = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AccountDescription(self):
        return self._AccountDescription

    @AccountDescription.setter
    def AccountDescription(self, AccountDescription):
        self._AccountDescription = AccountDescription

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._AccountName = params.get("AccountName")
        self._ClusterId = params.get("ClusterId")
        self._AccountDescription = params.get("AccountDescription")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableRecoveryTimeRange(AbstractModel):
    """可以回档时间范围

    """

    def __init__(self):
        r"""
        :param _AvailableBeginTime: 可回档起始时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type AvailableBeginTime: str
        :param _AvailableEndTime: 可回档结束时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type AvailableEndTime: str
        """
        self._AvailableBeginTime = None
        self._AvailableEndTime = None

    @property
    def AvailableBeginTime(self):
        return self._AvailableBeginTime

    @AvailableBeginTime.setter
    def AvailableBeginTime(self, AvailableBeginTime):
        self._AvailableBeginTime = AvailableBeginTime

    @property
    def AvailableEndTime(self):
        return self._AvailableEndTime

    @AvailableEndTime.setter
    def AvailableEndTime(self, AvailableEndTime):
        self._AvailableEndTime = AvailableEndTime


    def _deserialize(self, params):
        self._AvailableBeginTime = params.get("AvailableBeginTime")
        self._AvailableEndTime = params.get("AvailableEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Backup(AbstractModel):
    """集群备份集信息

    """

    def __init__(self):
        r"""
        :param _BackupId: 备份集ID，集群内唯一
        :type BackupId: int
        :param _BackupType: 备份集类型，目前只支持 SNAPSHOT：快照
        :type BackupType: str
        :param _BackupMethod: 备份集产生的方案，目前只支持 AUTO：自动
        :type BackupMethod: str
        :param _BackupDataTime: 备份集对应的数据时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type BackupDataTime: str
        :param _BackupDataSize: 备份集数据大小，单位GiB
        :type BackupDataSize: int
        :param _BackupTaskStartTime: 备份集对应的任务开始时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type BackupTaskStartTime: str
        :param _BackupTaskEndTime: 备份集对应的任务结束时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type BackupTaskEndTime: str
        :param _BackupTaskStatus: 备份集对应的任务状态  SUCCESS：成功
        :type BackupTaskStatus: str
        """
        self._BackupId = None
        self._BackupType = None
        self._BackupMethod = None
        self._BackupDataTime = None
        self._BackupDataSize = None
        self._BackupTaskStartTime = None
        self._BackupTaskEndTime = None
        self._BackupTaskStatus = None

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupMethod(self):
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupDataTime(self):
        return self._BackupDataTime

    @BackupDataTime.setter
    def BackupDataTime(self, BackupDataTime):
        self._BackupDataTime = BackupDataTime

    @property
    def BackupDataSize(self):
        return self._BackupDataSize

    @BackupDataSize.setter
    def BackupDataSize(self, BackupDataSize):
        self._BackupDataSize = BackupDataSize

    @property
    def BackupTaskStartTime(self):
        return self._BackupTaskStartTime

    @BackupTaskStartTime.setter
    def BackupTaskStartTime(self, BackupTaskStartTime):
        self._BackupTaskStartTime = BackupTaskStartTime

    @property
    def BackupTaskEndTime(self):
        return self._BackupTaskEndTime

    @BackupTaskEndTime.setter
    def BackupTaskEndTime(self, BackupTaskEndTime):
        self._BackupTaskEndTime = BackupTaskEndTime

    @property
    def BackupTaskStatus(self):
        return self._BackupTaskStatus

    @BackupTaskStatus.setter
    def BackupTaskStatus(self, BackupTaskStatus):
        self._BackupTaskStatus = BackupTaskStatus


    def _deserialize(self, params):
        self._BackupId = params.get("BackupId")
        self._BackupType = params.get("BackupType")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupDataTime = params.get("BackupDataTime")
        self._BackupDataSize = params.get("BackupDataSize")
        self._BackupTaskStartTime = params.get("BackupTaskStartTime")
        self._BackupTaskEndTime = params.get("BackupTaskEndTime")
        self._BackupTaskStatus = params.get("BackupTaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneClusterToPointInTimeRequest(AbstractModel):
    """CloneClusterToPointInTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _DBVersion: 数据库版本，目前仅支持 10.17
        :type DBVersion: str
        :param _CPU: CPU核数。取值参考文档【购买指南】
        :type CPU: int
        :param _Memory: 内存大小，单位GiB。取值参考文档【购买指南】
        :type Memory: int
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 已配置的私有网络中的子网ID
        :type SubnetId: str
        :param _PayMode: 集群付费模式
- PREPAID：预付费，即包年包月
- POSTPAID_BY_HOUR：按小时后付费
        :type PayMode: str
        :param _SourceClusterId: 对应的备份数据来源集群ID
        :type SourceClusterId: str
        :param _SourceDataPoint: 对应的备份数据时间点。按照RFC3339标准表示，并且使用东八区时区时间。格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type SourceDataPoint: str
        :param _ClusterName: 集群名，1-60个字符，可以包含中文、英文、数字和符号"-"、"_"、"."。不输入此参数时默认与ClusterId保持一致。
        :type ClusterName: str
        :param _ProjectId: 项目Id，默认为0表示默认项目
        :type ProjectId: int
        :param _Port: 连接数据库时，Endpoint使用的端口。取值范围为[1,65534]，默认值为5432
        :type Port: int
        :param _InstanceCount: 集群下实例数量。取值范围为[1,4]，默认值为1
        :type InstanceCount: int
        :param _Period: 购买时长，单位：月。取值范围为[1,60]，默认值为1。
只有当PayMode为PREPAID时生效。
        :type Period: int
        :param _AutoRenewFlag: 是否自动续费，0-不 1-是。默认为0，只有当PayMode为PREPAID时生效。
        :type AutoRenewFlag: int
        :param _StoragePayMode: 存储付费模式
 - PREPAID：预付费，即包年包月
 - POSTPAID_BY_HOUR：按小时后付费
默认为POSTPAID_BY_HOUR，实例付费模式为按小时付费时，存储付费模式不支持包年包月
        :type StoragePayMode: str
        :param _Storage: 存储最大使用量，单位GB。取值参考文档【购买指南】。存储使用预付费模式时必须设置，存储使用按小时后付费时不可设置
        :type Storage: int
        """
        self._Zone = None
        self._DBVersion = None
        self._CPU = None
        self._Memory = None
        self._VpcId = None
        self._SubnetId = None
        self._PayMode = None
        self._SourceClusterId = None
        self._SourceDataPoint = None
        self._ClusterName = None
        self._ProjectId = None
        self._Port = None
        self._InstanceCount = None
        self._Period = None
        self._AutoRenewFlag = None
        self._StoragePayMode = None
        self._Storage = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

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
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SourceClusterId(self):
        return self._SourceClusterId

    @SourceClusterId.setter
    def SourceClusterId(self, SourceClusterId):
        self._SourceClusterId = SourceClusterId

    @property
    def SourceDataPoint(self):
        return self._SourceDataPoint

    @SourceDataPoint.setter
    def SourceDataPoint(self, SourceDataPoint):
        self._SourceDataPoint = SourceDataPoint

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._DBVersion = params.get("DBVersion")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PayMode = params.get("PayMode")
        self._SourceClusterId = params.get("SourceClusterId")
        self._SourceDataPoint = params.get("SourceDataPoint")
        self._ClusterName = params.get("ClusterName")
        self._ProjectId = params.get("ProjectId")
        self._Port = params.get("Port")
        self._InstanceCount = params.get("InstanceCount")
        self._Period = params.get("Period")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._StoragePayMode = params.get("StoragePayMode")
        self._Storage = params.get("Storage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneClusterToPointInTimeResponse(AbstractModel):
    """CloneClusterToPointInTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNameSet: 订单号
        :type DealNameSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealNameSet = None
        self._RequestId = None

    @property
    def DealNameSet(self):
        return self._DealNameSet

    @DealNameSet.setter
    def DealNameSet(self, DealNameSet):
        self._DealNameSet = DealNameSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealNameSet = params.get("DealNameSet")
        self._RequestId = params.get("RequestId")


class Cluster(AbstractModel):
    """集群信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID，集群的唯一标识
        :type ClusterId: str
        :param _ClusterName: 集群名字，不修改时默认和集群ID相同
        :type ClusterName: str
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _DBVersion: TDSQL-C PostgreSQL 合入的社区版本号
        :type DBVersion: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Status: 集群状态。目前包括
 - creating ：创建中
 - running : 运行中
 - isolating : 隔离中
 - isolated : 已隔离
 - recovering : 恢复中
 - deleting : 删除中
 - deleted : 已删除
        :type Status: str
        :param _StatusDesc: 集群状态中文含义
        :type StatusDesc: str
        :param _CreateTime: 集群创建时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type CreateTime: str
        :param _StorageUsed: 存储当前使用量，单位GiB
        :type StorageUsed: float
        :param _StorageLimit: 存储最大使用量，单位GiB
        :type StorageLimit: int
        :param _PayMode: 付费模式：
 - PREPAID : 预付费，即包年包月
 - POSTPAID_BY_HOUR : 按小时结算后付费
        :type PayMode: str
        :param _PayPeriodEndTime: 预付费集群到期时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type PayPeriodEndTime: str
        :param _AutoRenewFlag: 预付费集群自动续费标签
 - 0 : 到期不自动续费
 - 1 : 到期自动续费
        :type AutoRenewFlag: int
        :param _DBCharset: 数据库字符集
        :type DBCharset: str
        :param _InstanceCount: 集群内实例的数量
        :type InstanceCount: int
        :param _EndpointSet: 集群内访问点信息
        :type EndpointSet: list of Endpoint
        :param _DBMajorVersion: TDSQL-C PostgreSQL 合入的社区主要版本号
        :type DBMajorVersion: str
        :param _DBKernelVersion: TDSQL-C PostgreSQL 内核版本号
        :type DBKernelVersion: str
        :param _StoragePayMode: 存储付费模式
 - PREPAID：预付费，即包年包月
 - POSTPAID_BY_HOUR：按小时后付费
注意：此字段可能返回 null，表示取不到有效值。
        :type StoragePayMode: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Region = None
        self._Zone = None
        self._DBVersion = None
        self._ProjectId = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._StorageUsed = None
        self._StorageLimit = None
        self._PayMode = None
        self._PayPeriodEndTime = None
        self._AutoRenewFlag = None
        self._DBCharset = None
        self._InstanceCount = None
        self._EndpointSet = None
        self._DBMajorVersion = None
        self._DBKernelVersion = None
        self._StoragePayMode = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

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
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StorageUsed(self):
        return self._StorageUsed

    @StorageUsed.setter
    def StorageUsed(self, StorageUsed):
        self._StorageUsed = StorageUsed

    @property
    def StorageLimit(self):
        return self._StorageLimit

    @StorageLimit.setter
    def StorageLimit(self, StorageLimit):
        self._StorageLimit = StorageLimit

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayPeriodEndTime(self):
        return self._PayPeriodEndTime

    @PayPeriodEndTime.setter
    def PayPeriodEndTime(self, PayPeriodEndTime):
        self._PayPeriodEndTime = PayPeriodEndTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def DBCharset(self):
        return self._DBCharset

    @DBCharset.setter
    def DBCharset(self, DBCharset):
        self._DBCharset = DBCharset

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def EndpointSet(self):
        return self._EndpointSet

    @EndpointSet.setter
    def EndpointSet(self, EndpointSet):
        self._EndpointSet = EndpointSet

    @property
    def DBMajorVersion(self):
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBKernelVersion(self):
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._DBVersion = params.get("DBVersion")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._StorageUsed = params.get("StorageUsed")
        self._StorageLimit = params.get("StorageLimit")
        self._PayMode = params.get("PayMode")
        self._PayPeriodEndTime = params.get("PayPeriodEndTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._DBCharset = params.get("DBCharset")
        self._InstanceCount = params.get("InstanceCount")
        if params.get("EndpointSet") is not None:
            self._EndpointSet = []
            for item in params.get("EndpointSet"):
                obj = Endpoint()
                obj._deserialize(item)
                self._EndpointSet.append(obj)
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._StoragePayMode = params.get("StoragePayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterInstancesRequest(AbstractModel):
    """CreateClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _CPU: CPU核数。取值参考文档【购买指南】
        :type CPU: int
        :param _Memory: 内存大小，单位GiB。取值参考文档【购买指南】
        :type Memory: int
        :param _InstanceName: 实例名，1-60个字符，可以包含中文、英文、数字和符号"-"、"_"、"."。不输入此参数时默认与InstanceId一致。
        :type InstanceName: str
        :param _InstanceCount: 新建实例的数量，默认为1。单集群下实例数量目前不能超过4个。
        :type InstanceCount: int
        """
        self._ClusterId = None
        self._CPU = None
        self._Memory = None
        self._InstanceName = None
        self._InstanceCount = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._InstanceName = params.get("InstanceName")
        self._InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterInstancesResponse(AbstractModel):
    """CreateClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNameSet: 订单号
        :type DealNameSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealNameSet = None
        self._RequestId = None

    @property
    def DealNameSet(self):
        return self._DealNameSet

    @DealNameSet.setter
    def DealNameSet(self, DealNameSet):
        self._DealNameSet = DealNameSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealNameSet = params.get("DealNameSet")
        self._RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _MasterUserPassword: 数据库用户密码，必须满足 8-64个字符，至少包含 大写字母、小写字母、数字和符号~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/中的任意三种
        :type MasterUserPassword: str
        :param _CPU: CPU核数。取值参考文档【购买指南】
        :type CPU: int
        :param _Memory: 内存大小，单位GiB。取值参考文档【购买指南】
        :type Memory: int
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 已配置的私有网络中的子网ID
        :type SubnetId: str
        :param _PayMode: 实例付费模式
 - PREPAID：预付费，即包年包月
 - POSTPAID_BY_HOUR：按小时后付费
        :type PayMode: str
        :param _ClusterName: 集群名，1-60个字符，可以包含中文、英文、数字和符号"-"、"_"、"."。不输入此参数时默认与ClusterId保持一致
        :type ClusterName: str
        :param _DBVersion: TDSQL-C PostgreSQL 合入的社区版本号。
支持入参值为：10.17。当输入该参数时，会基于此版本号创建对应的最新DBKernelVersion数据库内核。
注：该参数与DBMajorVersion、DBKernelVersion只能传递一个，且需要传递一个。
        :type DBVersion: str
        :param _ProjectId: 项目Id，默认为0表示默认项目
        :type ProjectId: int
        :param _Port: 连接数据库时，Endpoint使用的端口。取值范围为[1,65534]，默认值为5432
        :type Port: int
        :param _InstanceCount: 集群下实例数量。取值范围为[1,4]，默认值为1
        :type InstanceCount: int
        :param _Period: 购买时长，单位：月。取值范围为[1,60]，默认值为1。
只有当PayMode为PREPAID时生效。
        :type Period: int
        :param _AutoRenewFlag: 是否自动续费，0-不 1-是。默认值为0，只有当PayMode为PREPAID时生效。
        :type AutoRenewFlag: int
        :param _DBMajorVersion: TDSQL-C PostgreSQL 合入的社区主要版本号。
支持入参值为：10。当输入该参数时，会基于此版本号创建对应的最新DBKernelVersion数据库内核。
注：该参数和DBVersion、DBKernelVersion只能传递一个，且需要传递一个。
        :type DBMajorVersion: str
        :param _DBKernelVersion: TDSQL-C PostgreSQL 内核版本号。
支持入参值为：v10.17_r1.4。当输入该参数时，会创建此版本号对应的数据库内核。
注：该参数和DBVersion、DBMajorVersion只能传递一个，且需要传递一个。
        :type DBKernelVersion: str
        :param _StoragePayMode: 存储付费模式
 - PREPAID：预付费，即包年包月
 - POSTPAID_BY_HOUR：按小时后付费
默认为POSTPAID_BY_HOUR，实例付费模式为按小时付费时，存储付费模式不支持包年包月
        :type StoragePayMode: str
        :param _Storage: 存储最大使用量，单位GB。取值参考文档【购买指南】。存储使用预付费模式时必须设置，存储使用按小时后付费时不可设置
        :type Storage: int
        """
        self._Zone = None
        self._MasterUserPassword = None
        self._CPU = None
        self._Memory = None
        self._VpcId = None
        self._SubnetId = None
        self._PayMode = None
        self._ClusterName = None
        self._DBVersion = None
        self._ProjectId = None
        self._Port = None
        self._InstanceCount = None
        self._Period = None
        self._AutoRenewFlag = None
        self._DBMajorVersion = None
        self._DBKernelVersion = None
        self._StoragePayMode = None
        self._Storage = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def MasterUserPassword(self):
        return self._MasterUserPassword

    @MasterUserPassword.setter
    def MasterUserPassword(self, MasterUserPassword):
        self._MasterUserPassword = MasterUserPassword

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

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
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def DBMajorVersion(self):
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBKernelVersion(self):
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion

    @property
    def StoragePayMode(self):
        return self._StoragePayMode

    @StoragePayMode.setter
    def StoragePayMode(self, StoragePayMode):
        self._StoragePayMode = StoragePayMode

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._MasterUserPassword = params.get("MasterUserPassword")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PayMode = params.get("PayMode")
        self._ClusterName = params.get("ClusterName")
        self._DBVersion = params.get("DBVersion")
        self._ProjectId = params.get("ProjectId")
        self._Port = params.get("Port")
        self._InstanceCount = params.get("InstanceCount")
        self._Period = params.get("Period")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBKernelVersion = params.get("DBKernelVersion")
        self._StoragePayMode = params.get("StoragePayMode")
        self._Storage = params.get("Storage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealNameSet: 订单号
        :type DealNameSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealNameSet = None
        self._RequestId = None

    @property
    def DealNameSet(self):
        return self._DealNameSet

    @DealNameSet.setter
    def DealNameSet(self, DealNameSet):
        self._DealNameSet = DealNameSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealNameSet = params.get("DealNameSet")
        self._RequestId = params.get("RequestId")


class DeleteClusterInstancesRequest(AbstractModel):
    """DeleteClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        """
        self._ClusterId = None
        self._InstanceIdSet = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterInstancesResponse(AbstractModel):
    """DeleteClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _AccountSet: 账号信息列表
        :type AccountSet: list of Account
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccountSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountSet(self):
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccountSet") is not None:
            self._AccountSet = []
            for item in params.get("AccountSet"):
                obj = Account()
                obj._deserialize(item)
                self._AccountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterBackupsRequest(AbstractModel):
    """DescribeClusterBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _PageNumber: 页码，取值范围为[1,INF)，默认值为1
        :type PageNumber: int
        :param _PageSize: 每页个数，取值范围为默认为[1,100]，默认值为20
        :type PageSize: int
        """
        self._ClusterId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterBackupsResponse(AbstractModel):
    """DescribeClusterBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _BackupSet: 备份列表信息
        :type BackupSet: list of Backup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupSet(self):
        return self._BackupSet

    @BackupSet.setter
    def BackupSet(self, BackupSet):
        self._BackupSet = BackupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BackupSet") is not None:
            self._BackupSet = []
            for item in params.get("BackupSet"):
                obj = Backup()
                obj._deserialize(item)
                self._BackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterEndpointsRequest(AbstractModel):
    """DescribeClusterEndpoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterEndpointsResponse(AbstractModel):
    """DescribeClusterEndpoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _EndpointSet: 接入点列表
        :type EndpointSet: list of Endpoint
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._EndpointSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EndpointSet(self):
        return self._EndpointSet

    @EndpointSet.setter
    def EndpointSet(self, EndpointSet):
        self._EndpointSet = EndpointSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EndpointSet") is not None:
            self._EndpointSet = []
            for item in params.get("EndpointSet"):
                obj = Endpoint()
                obj._deserialize(item)
                self._EndpointSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _PageNumber: 页码，取值范围为[1,INF)，默认值为1
        :type PageNumber: int
        :param _PageSize: 每页个数，取值范围为默认为[1,100]，默认值为20
        :type PageSize: int
        :param _Filters: 目前支持查询条件包括：
 - InstanceId : 实例ID
 - InstanceName : 实例名
 - EndpointId : 接入点ID
 - Status : 实例状态
 - InstanceType : 实例类型
        :type Filters: list of Filter
        :param _OrderBy: 排序字段，可选字段：
- CreateTime : 实例创建时间(默认值)
- PayPeriodEndTime : 实例过期时间
        :type OrderBy: str
        :param _OrderByType: 排序方式，可选字段：
- DESC : 降序(默认值)
- ASC : 升序
        :type OrderByType: str
        """
        self._ClusterId = None
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _InstanceSet: 实例列表信息
        :type InstanceSet: list of Instance
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterRecoveryTimeRangeRequest(AbstractModel):
    """DescribeClusterRecoveryTimeRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _DataPoint: 期望的回档时间点，传入从集群创建时间到当前时间之间的时间点。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type DataPoint: str
        """
        self._ClusterId = None
        self._DataPoint = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DataPoint(self):
        return self._DataPoint

    @DataPoint.setter
    def DataPoint(self, DataPoint):
        self._DataPoint = DataPoint


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DataPoint = params.get("DataPoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterRecoveryTimeRangeResponse(AbstractModel):
    """DescribeClusterRecoveryTimeRange返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AvailableRecoveryTimeRangeSet: 可回档时间范围列表
        :type AvailableRecoveryTimeRangeSet: list of AvailableRecoveryTimeRange
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AvailableRecoveryTimeRangeSet = None
        self._RequestId = None

    @property
    def AvailableRecoveryTimeRangeSet(self):
        return self._AvailableRecoveryTimeRangeSet

    @AvailableRecoveryTimeRangeSet.setter
    def AvailableRecoveryTimeRangeSet(self, AvailableRecoveryTimeRangeSet):
        self._AvailableRecoveryTimeRangeSet = AvailableRecoveryTimeRangeSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AvailableRecoveryTimeRangeSet") is not None:
            self._AvailableRecoveryTimeRangeSet = []
            for item in params.get("AvailableRecoveryTimeRangeSet"):
                obj = AvailableRecoveryTimeRange()
                obj._deserialize(item)
                self._AvailableRecoveryTimeRangeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码，取值范围为[1,INF)，默认值为1
        :type PageNumber: int
        :param _PageSize: 每页条数，取值范围为默认为[1,100]，默认值为20
        :type PageSize: int
        :param _Filters: 目前支持查询条件包括：
 - ClusterId : 集群ID
 - ClusterName : 集群名
 - ProjectId : 项目ID
 - Status : 集群状态
 - PayMode : 付费模式
        :type Filters: list of Filter
        :param _OrderBy: 排序字段，可选字段：
 - CreateTime : 集群创建时间(默认值)
 - PayPeriodEndTime : 集群过期时间
        :type OrderBy: str
        :param _OrderByType: 排序方式，可选字段：
 - DESC : 降序(默认值)
 - ASC : 升序
        :type OrderByType: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _ClusterSet: 集群列表信息
        :type ClusterSet: list of Cluster
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterSet(self):
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = Cluster()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcesByDealNameRequest(AbstractModel):
    """DescribeResourcesByDealName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 计费订单id（如果计费还没回调业务发货，可能出现错误码InvalidParameterValue.DealNameNotFound，这种情况需要业务重试DescribeResourcesByDealName接口直到成功）
        :type DealName: str
        """
        self._DealName = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByDealNameResponse(AbstractModel):
    """DescribeResourcesByDealName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceIdInfoSet: 资源ID信息列表
        :type ResourceIdInfoSet: list of ResourceIdInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceIdInfoSet = None
        self._RequestId = None

    @property
    def ResourceIdInfoSet(self):
        return self._ResourceIdInfoSet

    @ResourceIdInfoSet.setter
    def ResourceIdInfoSet(self, ResourceIdInfoSet):
        self._ResourceIdInfoSet = ResourceIdInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResourceIdInfoSet") is not None:
            self._ResourceIdInfoSet = []
            for item in params.get("ResourceIdInfoSet"):
                obj = ResourceIdInfo()
                obj._deserialize(item)
                self._ResourceIdInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class Endpoint(AbstractModel):
    """集群的连接点信息，包含访问数据库的相关网络信息

    """

    def __init__(self):
        r"""
        :param _EndpointId: 连接点ID，集群内唯一
        :type EndpointId: str
        :param _ClusterId: 连接点所属的集群ID
        :type ClusterId: str
        :param _EndpointName: 连接点名字，默认和连接点ID一致
        :type EndpointName: str
        :param _EndpointType: 连接点类型
 - RW : 读写
 - RO : 只读
        :type EndpointType: str
        :param _VpcId: 私有网络VPC实例ID
        :type VpcId: str
        :param _SubnetId: 私有网络VPC下子网实例ID
        :type SubnetId: str
        :param _PrivateIp: 私有网络VPC下用于访问数据库的IP
        :type PrivateIp: str
        :param _PrivatePort: 私有网络VPC下用于访问数据库的端口
        :type PrivatePort: int
        :param _WanIp: 公共网络用户访问数据库的IP
        :type WanIp: str
        :param _WanPort: 公共网络用户访问数据库的端口
        :type WanPort: int
        :param _WanDomain: 公共网络用户访问数据库的域名
        :type WanDomain: str
        """
        self._EndpointId = None
        self._ClusterId = None
        self._EndpointName = None
        self._EndpointType = None
        self._VpcId = None
        self._SubnetId = None
        self._PrivateIp = None
        self._PrivatePort = None
        self._WanIp = None
        self._WanPort = None
        self._WanDomain = None

    @property
    def EndpointId(self):
        return self._EndpointId

    @EndpointId.setter
    def EndpointId(self, EndpointId):
        self._EndpointId = EndpointId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EndpointName(self):
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

    @property
    def EndpointType(self):
        return self._EndpointType

    @EndpointType.setter
    def EndpointType(self, EndpointType):
        self._EndpointType = EndpointType

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
    def PrivateIp(self):
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PrivatePort(self):
        return self._PrivatePort

    @PrivatePort.setter
    def PrivatePort(self, PrivatePort):
        self._PrivatePort = PrivatePort

    @property
    def WanIp(self):
        return self._WanIp

    @WanIp.setter
    def WanIp(self, WanIp):
        self._WanIp = WanIp

    @property
    def WanPort(self):
        return self._WanPort

    @WanPort.setter
    def WanPort(self, WanPort):
        self._WanPort = WanPort

    @property
    def WanDomain(self):
        return self._WanDomain

    @WanDomain.setter
    def WanDomain(self, WanDomain):
        self._WanDomain = WanDomain


    def _deserialize(self, params):
        self._EndpointId = params.get("EndpointId")
        self._ClusterId = params.get("ClusterId")
        self._EndpointName = params.get("EndpointName")
        self._EndpointType = params.get("EndpointType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PrivateIp = params.get("PrivateIp")
        self._PrivatePort = params.get("PrivatePort")
        self._WanIp = params.get("WanIp")
        self._WanPort = params.get("WanPort")
        self._WanDomain = params.get("WanDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤条件名
        :type Name: str
        :param _Values: 过滤条件值数组
        :type Values: list of str
        :param _ExactMatch: true:精确匹配(默认值) false:(模糊匹配)
        :type ExactMatch: bool
        """
        self._Name = None
        self._Values = None
        self._ExactMatch = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """集群下的实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，集群下唯一
        :type InstanceId: str
        :param _InstanceName: 实例名字，默认和实例ID一致
        :type InstanceName: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _EndpointId: 实例所在的访问点ID
        :type EndpointId: str
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _DBVersion: 数据库版本
        :type DBVersion: str
        :param _Status: 实例状态
        :type Status: str
        :param _StatusDesc: 实例状态中文含义
        :type StatusDesc: str
        :param _CreateTime: 实例创建时间。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type CreateTime: str
        :param _PayMode: 付费模式：
- PREPAID : 预付费
- POSTPAID_BY_HOUR : 按小时结算后付费

同一集群下付费模式需要保持一致。
        :type PayMode: str
        :param _PayPeriodEndTime: 实例到期时间。同一集群下到期时间需要保持一致。按照RFC3339标准表示，并且使用东八区时区时间，格式为：YYYY-MM-DDThh:mm:ss+08:00。
        :type PayPeriodEndTime: str
        :param _CPU: CPU核数
        :type CPU: int
        :param _Memory: 内存大小，单位GiB
        :type Memory: int
        :param _InstanceType: 实例类型
 - RW：读写实例
 - RO：只读实例
        :type InstanceType: str
        :param _DBMajorVersion: TDSQL-C PostgreSQL 合入的社区主要版本号
        :type DBMajorVersion: str
        :param _DBKernelVersion: TDSQL-C PostgreSQL 内核版本号
        :type DBKernelVersion: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._ClusterId = None
        self._EndpointId = None
        self._Region = None
        self._Zone = None
        self._DBVersion = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._PayMode = None
        self._PayPeriodEndTime = None
        self._CPU = None
        self._Memory = None
        self._InstanceType = None
        self._DBMajorVersion = None
        self._DBKernelVersion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EndpointId(self):
        return self._EndpointId

    @EndpointId.setter
    def EndpointId(self, EndpointId):
        self._EndpointId = EndpointId

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
    def DBVersion(self):
        return self._DBVersion

    @DBVersion.setter
    def DBVersion(self, DBVersion):
        self._DBVersion = DBVersion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayPeriodEndTime(self):
        return self._PayPeriodEndTime

    @PayPeriodEndTime.setter
    def PayPeriodEndTime(self, PayPeriodEndTime):
        self._PayPeriodEndTime = PayPeriodEndTime

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DBMajorVersion(self):
        return self._DBMajorVersion

    @DBMajorVersion.setter
    def DBMajorVersion(self, DBMajorVersion):
        self._DBMajorVersion = DBMajorVersion

    @property
    def DBKernelVersion(self):
        return self._DBKernelVersion

    @DBKernelVersion.setter
    def DBKernelVersion(self, DBKernelVersion):
        self._DBKernelVersion = DBKernelVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ClusterId = params.get("ClusterId")
        self._EndpointId = params.get("EndpointId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._DBVersion = params.get("DBVersion")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._PayMode = params.get("PayMode")
        self._PayPeriodEndTime = params.get("PayPeriodEndTime")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._InstanceType = params.get("InstanceType")
        self._DBMajorVersion = params.get("DBMajorVersion")
        self._DBKernelVersion = params.get("DBKernelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterInstancesRequest(AbstractModel):
    """IsolateClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        """
        self._ClusterId = None
        self._InstanceIdSet = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterInstancesResponse(AbstractModel):
    """IsolateClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class IsolateClusterRequest(AbstractModel):
    """IsolateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterResponse(AbstractModel):
    """IsolateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _AccountName: 账号名字
        :type AccountName: str
        :param _AccountDescription: 账号描述，0-256个字符
        :type AccountDescription: str
        """
        self._ClusterId = None
        self._AccountName = None
        self._AccountDescription = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountDescription(self):
        return self._AccountDescription

    @AccountDescription.setter
    def AccountDescription(self, AccountDescription):
        self._AccountDescription = AccountDescription


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._AccountName = params.get("AccountName")
        self._AccountDescription = params.get("AccountDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyClusterEndpointWanStatusRequest(AbstractModel):
    """ModifyClusterEndpointWanStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _EndpointId: 接入点ID
        :type EndpointId: str
        :param _WanStatus: 取值为： 
 - OPEN：开启外网 
 - CLOSE：关闭外网
        :type WanStatus: str
        """
        self._ClusterId = None
        self._EndpointId = None
        self._WanStatus = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EndpointId(self):
        return self._EndpointId

    @EndpointId.setter
    def EndpointId(self, EndpointId):
        self._EndpointId = EndpointId

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._EndpointId = params.get("EndpointId")
        self._WanStatus = params.get("WanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterEndpointWanStatusResponse(AbstractModel):
    """ModifyClusterEndpointWanStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyClusterInstancesSpecRequest(AbstractModel):
    """ModifyClusterInstancesSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIdSet: 实例ID列表，目前只支持单个实例修改
        :type InstanceIdSet: list of str
        :param _CPU: 修改后的CPU核数。取值参考文档【购买指南】
        :type CPU: int
        :param _Memory: 修改后的内存大小，单位GiB。取值参考文档【购买指南】
        :type Memory: int
        :param _OperationTiming: 操作时机
 - IMMEDIATE：立即执行 
 - MAINTAIN_PERIOD：维护窗口期执行
        :type OperationTiming: str
        """
        self._ClusterId = None
        self._InstanceIdSet = None
        self._CPU = None
        self._Memory = None
        self._OperationTiming = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def OperationTiming(self):
        return self._OperationTiming

    @OperationTiming.setter
    def OperationTiming(self, OperationTiming):
        self._OperationTiming = OperationTiming


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._OperationTiming = params.get("OperationTiming")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterInstancesSpecResponse(AbstractModel):
    """ModifyClusterInstancesSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ClusterName: 集群名，1-60个字符，可以包含中文、英文、数字和符号"-"、"_"、"."
        :type ClusterName: str
        """
        self._ClusterId = None
        self._ClusterName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyClustersAutoRenewFlagRequest(AbstractModel):
    """ModifyClustersAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterIdSet: 集群ID列表
        :type ClusterIdSet: list of str
        :param _AutoRenewFlag: 是否自动续费，0-不 1-是。默认为0，只有当集群的PayMode为PREPAID时生效。
        :type AutoRenewFlag: int
        """
        self._ClusterIdSet = None
        self._AutoRenewFlag = None

    @property
    def ClusterIdSet(self):
        return self._ClusterIdSet

    @ClusterIdSet.setter
    def ClusterIdSet(self, ClusterIdSet):
        self._ClusterIdSet = ClusterIdSet

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._ClusterIdSet = params.get("ClusterIdSet")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClustersAutoRenewFlagResponse(AbstractModel):
    """ModifyClustersAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class RecoverClusterInstancesRequest(AbstractModel):
    """RecoverClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        :param _Period: 购买时长，单位：月。取值范围为[1,60]，默认值为1。
只有当PayMode为PREPAID时生效。
        :type Period: int
        """
        self._ClusterId = None
        self._InstanceIdSet = None
        self._Period = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverClusterInstancesResponse(AbstractModel):
    """RecoverClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class RecoverClusterRequest(AbstractModel):
    """RecoverCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Period: 购买时长，单位：月。取值范围为[1,60]，默认值为1。
只有当PayMode为PREPAID时生效。
        :type Period: int
        """
        self._ClusterId = None
        self._Period = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverClusterResponse(AbstractModel):
    """RecoverCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class RenewClusterRequest(AbstractModel):
    """RenewCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Period: 续费时间，单位：月。取值范围为[1,60]，默认值为1。
        :type Period: int
        """
        self._ClusterId = None
        self._Period = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewClusterResponse(AbstractModel):
    """RenewCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _AccountName: 账号名字
        :type AccountName: str
        :param _AccountPassword: 数据库用户密码，必须满足 8-64个字符，至少包含 大写字母、小写字母、数字和符号~!@#$%^&*_-+=`|(){}[]:;'<>,.?/中的任意三种
        :type AccountPassword: str
        """
        self._ClusterId = None
        self._AccountName = None
        self._AccountPassword = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ResourceIdInfo(AbstractModel):
    """资源ID信息，包括ClusterID和InstanceID

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        """
        self._ClusterId = None
        self._InstanceIdSet = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterInstancesRequest(AbstractModel):
    """RestartClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _InstanceIdSet: 实例ID列表，目前只支持单个实例重启
        :type InstanceIdSet: list of str
        """
        self._ClusterId = None
        self._InstanceIdSet = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceIdSet(self):
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartClusterInstancesResponse(AbstractModel):
    """RestartClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class TransformClusterPayModeRequest(AbstractModel):
    """TransformClusterPayMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _CurrentPayMode: 当前付费模式，目前只支持：POSTPAID_BY_HOUR(按小时后付费)
        :type CurrentPayMode: str
        :param _TargetPayMode: 目标付费模式，目前只支持：PREPAID(预付费)
        :type TargetPayMode: str
        :param _Period: 购买时长，单位：月。取值范围为[1,60]，默认值为1。
        :type Period: int
        """
        self._ClusterId = None
        self._CurrentPayMode = None
        self._TargetPayMode = None
        self._Period = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CurrentPayMode(self):
        return self._CurrentPayMode

    @CurrentPayMode.setter
    def CurrentPayMode(self, CurrentPayMode):
        self._CurrentPayMode = CurrentPayMode

    @property
    def TargetPayMode(self):
        return self._TargetPayMode

    @TargetPayMode.setter
    def TargetPayMode(self, TargetPayMode):
        self._TargetPayMode = TargetPayMode

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._CurrentPayMode = params.get("CurrentPayMode")
        self._TargetPayMode = params.get("TargetPayMode")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransformClusterPayModeResponse(AbstractModel):
    """TransformClusterPayMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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