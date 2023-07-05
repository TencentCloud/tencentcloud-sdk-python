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


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称：keewidb。
        :type Product: str
        :param _SecurityGroupId: 要绑定的安全组 ID，类似sg-efil7***。
        :type SecurityGroupId: str
        :param _InstanceIds: 实例 ID，格式如：kee-c1nl9***，支持指定多个实例。
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

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


class BackupInfo(AbstractModel):
    """实例的备份信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 备份开始时间。
        :type StartTime: str
        :param _BackupId: 备份 ID。
        :type BackupId: str
        :param _BackupType: 备份类型。<ul><li>1：手动备份，指根据业务运维排障需求，立即执行备份任务的操作。</li> <li>0：自动备份，指根据自动备份策略定时自动发起的备份任务。</li></ul>
        :type BackupType: str
        :param _Remark: 备份的备注信息.
        :type Remark: str
        :param _Status: 备份状态。  <ul><li>1：备份任务被其它流程锁定。</li><li>2：备份正常，没有被任何流程锁定。</li> <li>-1：备份已过期。</li><li>3：备份正在被导出。</li> <li>4：备份导出成功。</li></ul>
        :type Status: int
        :param _Locked: 备份是否被锁定。<ul><li>0：未被锁定。</li><li>1：已被锁定。</li></ul>
        :type Locked: int
        """
        self._StartTime = None
        self._BackupId = None
        self._BackupType = None
        self._Remark = None
        self._Status = None
        self._Locked = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

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
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Locked(self):
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._BackupId = params.get("BackupId")
        self._BackupType = params.get("BackupType")
        self._Remark = params.get("Remark")
        self._Status = params.get("Status")
        self._Locked = params.get("Locked")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogInfo(AbstractModel):
    """实例增量备份信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 备份开始时间。
        :type StartTime: str
        :param _EndTime: 备份结束时间。
        :type EndTime: str
        :param _BackupId: 备份 ID。
        :type BackupId: str
        :param _Filename: 备份文件名。
        :type Filename: str
        :param _FileSize: 备份文件大小，单位：Byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        """
        self._StartTime = None
        self._EndTime = None
        self._BackupId = None
        self._Filename = None
        self._FileSize = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def Filename(self):
        return self._Filename

    @Filename.setter
    def Filename(self, Filename):
        self._Filename = Filename

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._BackupId = params.get("BackupId")
        self._Filename = params.get("Filename")
        self._FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeInstanceMasterRequest(AbstractModel):
    """ChangeInstanceMaster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param _NodeId: 副本节点 ID。
        :type NodeId: str
        """
        self._InstanceId = None
        self._NodeId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeInstanceMasterResponse(AbstractModel):
    """ChangeInstanceMaster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CleanUpInstanceRequest(AbstractModel):
    """CleanUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CleanUpInstanceResponse(AbstractModel):
    """CleanUpInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ClearInstanceRequest(AbstractModel):
    """ClearInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubhg****。
        :type InstanceId: str
        :param _Password: 实例访问密码。
实例为免密访问，则无需设置该参数。
        :type Password: str
        """
        self._InstanceId = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearInstanceResponse(AbstractModel):
    """ClearInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateBackupManuallyRequest(AbstractModel):
    """CreateBackupManually请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待操作的实例 ID，可通过 DescribeInstance接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _Remark: 本次备份的备注信息。
        :type Remark: str
        :param _StorageDays: 备份文件保存天数。0代表指定默认保留时间
        :type StorageDays: int
        """
        self._InstanceId = None
        self._Remark = None
        self._StorageDays = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def StorageDays(self):
        return self._StorageDays

    @StorageDays.setter
    def StorageDays(self, StorageDays):
        self._StorageDays = StorageDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Remark = params.get("Remark")
        self._StorageDays = params.get("StorageDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupManuallyResponse(AbstractModel):
    """CreateBackupManually返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    """CreateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TypeId: 产品版本。
14：当前仅支持混合存储版。
        :type TypeId: int
        :param _UniqVpcId: 私有网络唯一ID。
请登录控制台在私有网络列表查询，如：vpc-azlk3***。
        :type UniqVpcId: str
        :param _UniqSubnetId: 私有网络所属子网唯一ID。
请登录控制台在私有网络列表查询，如：subnet-8abje***。
        :type UniqSubnetId: str
        :param _BillingMode: 计费模式。<ul><li>0：按量计费。</li><li>1：包年包月。</li></ul>
        :type BillingMode: int
        :param _GoodsNum: 实例数量，单次最大购买数量以查询产品售卖规格返回的数量为准。
        :type GoodsNum: int
        :param _Period: 选择包年包月计费模式（BillingMode 设置为1）时，您需要选择购买实例的时长。单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。按量计费（BillingMode 设置为0）实例该参数设置为1即可。
        :type Period: int
        :param _ShardNum: 分片数量，支持选择3、5、6、8、9、10、12、15、16、18、20、21、24、25、27、30、32、33、35、36、39、40、42、45、48、50、51、54、55、56、57、60、63、64分片。
        :type ShardNum: int
        :param _ReplicasNum: 副本数。当前仅支持设置1个副本节点，即每一个分片仅包含1个主节点与1个副本节点，数据主从实时热备。
        :type ReplicasNum: int
        :param _MachineCpu: 计算cpu核心数。
        :type MachineCpu: int
        :param _MachineMemory: 实例内存容量，单位：GB。
KeeWiDB 内存容量<b>MachineMemory</b>与持久内存容量<b>MemSize</b>为固定搭配，即2GB内存，固定分配8GB的持久内存，不可选择。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。
        :type MachineMemory: int
        :param _ZoneId: 实例所属的可用区ID。<ul><li>具体取值，请参见[地域和可用区](https://cloud.tencent.com/document/product/239/4106)获取。</li><li>参数<b>ZoneId</b>和<b>ZoneName</b>至少配置其中一个。</li></u>
        :type ZoneId: int
        :param _ZoneName: 实例所属的可用区名称。<ul><li>具体取值，请参见[地域和可用区](https://cloud.tencent.com/document/product/239/4106)获取。</li><li>参数<b>ZoneId</b>和<b>ZoneName</b>至少配置其中一个。</li></u>
        :type ZoneName: str
        :param _InstanceName: 创建实例的名称。
仅支持长度小于60的中文、英文或者数字，短划线"-"、下划线"_"。
        :type InstanceName: str
        :param _NoAuth: 指明创建的实例是否需要支持免密访问。<ul><li>true：免密实例。</li><li>false：非免密实例，默认为非免密实例。此时，需要设置访问密码。</li></ul>
        :type NoAuth: bool
        :param _Password: 实例访问密码。<ul><li>当参数<b>NoAuth</b>为<b>true</b>时，Password为无需设置，否则Password为必填参数。</li>
<li>密码复杂度要求：<ul><li>8-30个字符。</li><li>至少包含小写字母、大写字母、数字和字符 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的2种。</li><li>不能以"/"开头。</li></ul></li></ul>
        :type Password: str
        :param _VPort: 自定义端口。默认为6379，范围[1024,65535]。
        :type VPort: int
        :param _AutoRenew: 包年包月计费的续费模式。<ul><li>0：默认状态，指手动续费。</li><li>1：自动续费。</li><li>2：到期不再续费。</ul>
        :type AutoRenew: int
        :param _SecurityGroupIdList: 给实例设置安全组 ID 数组。
        :type SecurityGroupIdList: list of str
        :param _ResourceTags: 给实例绑定标签。
        :type ResourceTags: list of ResourceTag
        :param _MemSize: 混合存储版，单分片持久化内存容量，单位：GB。
KeeWiDB 内存容量<b>MachineMemory</b>与持久内存容量<b>MemSize</b>为固定搭配，即2GB内存，固定分配8GB的持久内存，不可选择。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。
        :type MemSize: int
        :param _DiskSize: 每个分片硬盘的容量。单位：GB。
每一缓存分片容量，对应的磁盘容量范围不同。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。
        :type DiskSize: int
        :param _ProjectId: 项目id，取值以用户账户>用户账户相关接口查询>项目列表返回的projectId为准。
        :type ProjectId: int
        """
        self._TypeId = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._BillingMode = None
        self._GoodsNum = None
        self._Period = None
        self._ShardNum = None
        self._ReplicasNum = None
        self._MachineCpu = None
        self._MachineMemory = None
        self._ZoneId = None
        self._ZoneName = None
        self._InstanceName = None
        self._NoAuth = None
        self._Password = None
        self._VPort = None
        self._AutoRenew = None
        self._SecurityGroupIdList = None
        self._ResourceTags = None
        self._MemSize = None
        self._DiskSize = None
        self._ProjectId = None

    @property
    def TypeId(self):
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ShardNum(self):
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def ReplicasNum(self):
        return self._ReplicasNum

    @ReplicasNum.setter
    def ReplicasNum(self, ReplicasNum):
        self._ReplicasNum = ReplicasNum

    @property
    def MachineCpu(self):
        return self._MachineCpu

    @MachineCpu.setter
    def MachineCpu(self, MachineCpu):
        self._MachineCpu = MachineCpu

    @property
    def MachineMemory(self):
        return self._MachineMemory

    @MachineMemory.setter
    def MachineMemory(self, MachineMemory):
        self._MachineMemory = MachineMemory

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def SecurityGroupIdList(self):
        return self._SecurityGroupIdList

    @SecurityGroupIdList.setter
    def SecurityGroupIdList(self, SecurityGroupIdList):
        self._SecurityGroupIdList = SecurityGroupIdList

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._TypeId = params.get("TypeId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._BillingMode = params.get("BillingMode")
        self._GoodsNum = params.get("GoodsNum")
        self._Period = params.get("Period")
        self._ShardNum = params.get("ShardNum")
        self._ReplicasNum = params.get("ReplicasNum")
        self._MachineCpu = params.get("MachineCpu")
        self._MachineMemory = params.get("MachineMemory")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._InstanceName = params.get("InstanceName")
        self._NoAuth = params.get("NoAuth")
        self._Password = params.get("Password")
        self._VPort = params.get("VPort")
        self._AutoRenew = params.get("AutoRenew")
        self._SecurityGroupIdList = params.get("SecurityGroupIdList")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._MemSize = params.get("MemSize")
        self._DiskSize = params.get("DiskSize")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    """CreateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 交易 ID。
        :type DealId: str
        :param _InstanceIds: 实例 ID 。
        :type InstanceIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class DescribeAutoBackupConfigRequest(AbstractModel):
    """DescribeAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoBackupConfigResponse(AbstractModel):
    """DescribeAutoBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WeekDays: 自动备份的周期。包括：Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :type WeekDays: list of str
        :param _TimePeriod: 自动备份时间段。
        :type TimePeriod: str
        :param _BackupStorageDays: 全量备份文件保存天数。
        :type BackupStorageDays: int
        :param _BinlogStorageDays: 增量备份文件保存天数。
        :type BinlogStorageDays: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WeekDays = None
        self._TimePeriod = None
        self._BackupStorageDays = None
        self._BinlogStorageDays = None
        self._RequestId = None

    @property
    def WeekDays(self):
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def BackupStorageDays(self):
        return self._BackupStorageDays

    @BackupStorageDays.setter
    def BackupStorageDays(self, BackupStorageDays):
        self._BackupStorageDays = BackupStorageDays

    @property
    def BinlogStorageDays(self):
        return self._BinlogStorageDays

    @BinlogStorageDays.setter
    def BinlogStorageDays(self, BinlogStorageDays):
        self._BinlogStorageDays = BinlogStorageDays

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WeekDays = params.get("WeekDays")
        self._TimePeriod = params.get("TimePeriod")
        self._BackupStorageDays = params.get("BackupStorageDays")
        self._BinlogStorageDays = params.get("BinlogStorageDays")
        self._RequestId = params.get("RequestId")


class DescribeConnectionConfigRequest(AbstractModel):
    """DescribeConnectionConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConnectionConfigResponse(AbstractModel):
    """DescribeConnectionConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InNetLimit: 单分片入流量带宽限制，单位：MB。
        :type InNetLimit: int
        :param _OutNetLimit: 单分片出流量带宽限制，单位：MB。
        :type OutNetLimit: int
        :param _ClientLimit: 单分片连接数限制。
        :type ClientLimit: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InNetLimit = None
        self._OutNetLimit = None
        self._ClientLimit = None
        self._RequestId = None

    @property
    def InNetLimit(self):
        return self._InNetLimit

    @InNetLimit.setter
    def InNetLimit(self, InNetLimit):
        self._InNetLimit = InNetLimit

    @property
    def OutNetLimit(self):
        return self._OutNetLimit

    @OutNetLimit.setter
    def OutNetLimit(self, OutNetLimit):
        self._OutNetLimit = OutNetLimit

    @property
    def ClientLimit(self):
        return self._ClientLimit

    @ClientLimit.setter
    def ClientLimit(self, ClientLimit):
        self._ClientLimit = ClientLimit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InNetLimit = params.get("InNetLimit")
        self._OutNetLimit = params.get("OutNetLimit")
        self._ClientLimit = params.get("ClientLimit")
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称：keewidb。
        :type Product: str
        :param _InstanceId: 实例ID，格式如：kee-c1nl9***。
        :type InstanceId: str
        """
        self._Product = None
        self._InstanceId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组规则。
        :type Groups: list of SecurityGroup
        :param _VIP: 安全组生效内网地址。
        :type VIP: str
        :param _VPort: 安全组生效内网端口。
        :type VPort: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._VIP = None
        self._VPort = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def VIP(self):
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._VIP = params.get("VIP")
        self._VPort = params.get("VPort")
        self._RequestId = params.get("RequestId")


class DescribeInstanceBackupsRequest(AbstractModel):
    """DescribeInstanceBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 待操作的实例ID，可通过 DescribeInstance 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param _Limit: 每页输出的备份列表大小，即每页输出的备份文件的数量，默认值20，取值范围为[1,100]。
        :type Limit: int
        :param _Offset: 备份列表分页偏移量，取Limit整数倍。
计算公式为offset=limit*(页码-1)。例如 limit=10，第1页offset就为0，第2页offset就为10，依次类推。
        :type Offset: int
        :param _BeginTime: 查询备份文件的开始时间，格式如：2017-02-08 16:46:34。查询实例在 [BeginTime, EndTime] 时间段内的备份列表。
        :type BeginTime: str
        :param _EndTime: 查询备份文件的结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内的备份列表。
        :type EndTime: str
        :param _Status: 备份任务状态。<ul><li>1：备份在流程中。</li><li>2：备份正常。</li><li>3：备份转RDB文件处理中。</li><li>4：已完成RDB转换。</li><li>-1：备份已过期。</li><li>-2：备份已删除。</li></ul>
        :type Status: list of int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._BeginTime = None
        self._EndTime = None
        self._Status = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceBackupsResponse(AbstractModel):
    """DescribeInstanceBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 备份文件总数。
        :type TotalCount: int
        :param _BackupSet: 废弃字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSet: list of BinlogInfo
        :param _BackupRecord: 实例备份信息列表。
        :type BackupRecord: list of BackupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupSet = None
        self._BackupRecord = None
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
    def BackupRecord(self):
        return self._BackupRecord

    @BackupRecord.setter
    def BackupRecord(self, BackupRecord):
        self._BackupRecord = BackupRecord

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
                obj = BinlogInfo()
                obj._deserialize(item)
                self._BackupSet.append(obj)
        if params.get("BackupRecord") is not None:
            self._BackupRecord = []
            for item in params.get("BackupRecord"):
                obj = BackupInfo()
                obj._deserialize(item)
                self._BackupRecord.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceBinlogsRequest(AbstractModel):
    """DescribeInstanceBinlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _Limit: 每页输出备份列表大小，默认大小20。
        :type Limit: int
        :param _Offset: 分页偏移量，取Limit整数倍。
        :type Offset: int
        :param _BeginTime: 开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。
        :type BeginTime: str
        :param _EndTime: 结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。
        :type EndTime: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceBinlogsResponse(AbstractModel):
    """DescribeInstanceBinlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 备份总数
        :type TotalCount: int
        :param _BackupSet: 实例的备份信息数组
        :type BackupSet: list of BinlogInfo
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
                obj = BinlogInfo()
                obj._deserialize(item)
                self._BackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceDealDetailRequest(AbstractModel):
    """DescribeInstanceDealDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealIds: 订单交易ID数组，即 [CreateInstances](https://cloud.tencent.com/document/api/1520/86207) 的输出参数DealId。
        :type DealIds: list of str
        """
        self._DealIds = None

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDealDetailResponse(AbstractModel):
    """DescribeInstanceDealDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealDetails: 订单详细信息
        :type DealDetails: list of TradeDealDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealDetails = None
        self._RequestId = None

    @property
    def DealDetails(self):
        return self._DealDetails

    @DealDetails.setter
    def DealDetails(self, DealDetails):
        self._DealDetails = DealDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DealDetails") is not None:
            self._DealDetails = []
            for item in params.get("DealDetails"):
                obj = TradeDealDetail()
                obj._deserialize(item)
                self._DealDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodeInfoRequest(AbstractModel):
    """DescribeInstanceNodeInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param _Limit: 每页输出的节点信息大小。默认为 20。
        :type Limit: int
        :param _Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodeInfoResponse(AbstractModel):
    """DescribeInstanceNodeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyCount: Proxy 节点数量。
        :type ProxyCount: int
        :param _Proxy: Proxy 节点信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Proxy: list of ProxyNodeInfo
        :param _RedisCount: Redis 节点数量。该参数仅为产品兼容性而保留，并不具有实际意义，可忽略。
        :type RedisCount: int
        :param _Redis: Redis 节点信息。该参数仅为产品兼容性而保留，并不具有实际意义，可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Redis: list of RedisNodeInfo
        :param _TendisCount: Tendis 节点数量。该参数仅为产品兼容性而保留，并不具有实际意义，可忽略。
        :type TendisCount: int
        :param _Tendis: Tendis 节点信息。该参数仅为产品兼容性而保留，并不具有实际意义，可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tendis: list of InstanceNodeInfo
        :param _KeeWiDBCount: KeewiDB 节点数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeeWiDBCount: int
        :param _KeeWiDB: KeewiDB 节点信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeeWiDB: list of InstanceNodeInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxyCount = None
        self._Proxy = None
        self._RedisCount = None
        self._Redis = None
        self._TendisCount = None
        self._Tendis = None
        self._KeeWiDBCount = None
        self._KeeWiDB = None
        self._RequestId = None

    @property
    def ProxyCount(self):
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def Proxy(self):
        return self._Proxy

    @Proxy.setter
    def Proxy(self, Proxy):
        self._Proxy = Proxy

    @property
    def RedisCount(self):
        return self._RedisCount

    @RedisCount.setter
    def RedisCount(self, RedisCount):
        self._RedisCount = RedisCount

    @property
    def Redis(self):
        return self._Redis

    @Redis.setter
    def Redis(self, Redis):
        self._Redis = Redis

    @property
    def TendisCount(self):
        return self._TendisCount

    @TendisCount.setter
    def TendisCount(self, TendisCount):
        self._TendisCount = TendisCount

    @property
    def Tendis(self):
        return self._Tendis

    @Tendis.setter
    def Tendis(self, Tendis):
        self._Tendis = Tendis

    @property
    def KeeWiDBCount(self):
        return self._KeeWiDBCount

    @KeeWiDBCount.setter
    def KeeWiDBCount(self, KeeWiDBCount):
        self._KeeWiDBCount = KeeWiDBCount

    @property
    def KeeWiDB(self):
        return self._KeeWiDB

    @KeeWiDB.setter
    def KeeWiDB(self, KeeWiDB):
        self._KeeWiDB = KeeWiDB

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyCount = params.get("ProxyCount")
        if params.get("Proxy") is not None:
            self._Proxy = []
            for item in params.get("Proxy"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self._Proxy.append(obj)
        self._RedisCount = params.get("RedisCount")
        if params.get("Redis") is not None:
            self._Redis = []
            for item in params.get("Redis"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self._Redis.append(obj)
        self._TendisCount = params.get("TendisCount")
        if params.get("Tendis") is not None:
            self._Tendis = []
            for item in params.get("Tendis"):
                obj = InstanceNodeInfo()
                obj._deserialize(item)
                self._Tendis.append(obj)
        self._KeeWiDBCount = params.get("KeeWiDBCount")
        if params.get("KeeWiDB") is not None:
            self._KeeWiDB = []
            for item in params.get("KeeWiDB"):
                obj = InstanceNodeInfo()
                obj._deserialize(item)
                self._KeeWiDB.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param _Limit: 每页输出的参数列表大小。默认为 20，最多输出100条。
        :type Limit: int
        :param _Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 修改历史记录总数。
        :type TotalCount: int
        :param _InstanceParamHistory: 修改历史记录信息。
        :type InstanceParamHistory: list of InstanceParamHistory
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceParamHistory = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceParamHistory(self):
        return self._InstanceParamHistory

    @InstanceParamHistory.setter
    def InstanceParamHistory(self, InstanceParamHistory):
        self._InstanceParamHistory = InstanceParamHistory

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceParamHistory") is not None:
            self._InstanceParamHistory = []
            for item in params.get("InstanceParamHistory"):
                obj = InstanceParamHistory()
                obj._deserialize(item)
                self._InstanceParamHistory.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例参数总数量。
        :type TotalCount: int
        :param _InstanceEnumParam: 实例枚举类型参数数组。
        :type InstanceEnumParam: list of InstanceEnumParam
        :param _InstanceIntegerParam: 实例整型参数数组。
        :type InstanceIntegerParam: list of InstanceIntegerParam
        :param _InstanceTextParam: 实例字符型参数数组。
        :type InstanceTextParam: list of InstanceTextParam
        :param _InstanceMultiParam: 实例多选项型参数数组。
        :type InstanceMultiParam: list of InstanceMultiParam
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceEnumParam = None
        self._InstanceIntegerParam = None
        self._InstanceTextParam = None
        self._InstanceMultiParam = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceEnumParam(self):
        return self._InstanceEnumParam

    @InstanceEnumParam.setter
    def InstanceEnumParam(self, InstanceEnumParam):
        self._InstanceEnumParam = InstanceEnumParam

    @property
    def InstanceIntegerParam(self):
        return self._InstanceIntegerParam

    @InstanceIntegerParam.setter
    def InstanceIntegerParam(self, InstanceIntegerParam):
        self._InstanceIntegerParam = InstanceIntegerParam

    @property
    def InstanceTextParam(self):
        return self._InstanceTextParam

    @InstanceTextParam.setter
    def InstanceTextParam(self, InstanceTextParam):
        self._InstanceTextParam = InstanceTextParam

    @property
    def InstanceMultiParam(self):
        return self._InstanceMultiParam

    @InstanceMultiParam.setter
    def InstanceMultiParam(self, InstanceMultiParam):
        self._InstanceMultiParam = InstanceMultiParam

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceEnumParam") is not None:
            self._InstanceEnumParam = []
            for item in params.get("InstanceEnumParam"):
                obj = InstanceEnumParam()
                obj._deserialize(item)
                self._InstanceEnumParam.append(obj)
        if params.get("InstanceIntegerParam") is not None:
            self._InstanceIntegerParam = []
            for item in params.get("InstanceIntegerParam"):
                obj = InstanceIntegerParam()
                obj._deserialize(item)
                self._InstanceIntegerParam.append(obj)
        if params.get("InstanceTextParam") is not None:
            self._InstanceTextParam = []
            for item in params.get("InstanceTextParam"):
                obj = InstanceTextParam()
                obj._deserialize(item)
                self._InstanceTextParam.append(obj)
        if params.get("InstanceMultiParam") is not None:
            self._InstanceMultiParam = []
            for item in params.get("InstanceMultiParam"):
                obj = InstanceMultiParam()
                obj._deserialize(item)
                self._InstanceMultiParam.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceReplicasRequest(AbstractModel):
    """DescribeInstanceReplicas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceReplicasResponse(AbstractModel):
    """DescribeInstanceReplicas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例所有节点数量，包括主节点、副本节点。
        :type TotalCount: int
        :param _ReplicaGroups: 实例节点信息。
        :type ReplicaGroups: list of ReplicaGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ReplicaGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReplicaGroups(self):
        return self._ReplicaGroups

    @ReplicaGroups.setter
    def ReplicaGroups(self, ReplicaGroups):
        self._ReplicaGroups = ReplicaGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ReplicaGroups") is not None:
            self._ReplicaGroups = []
            for item in params.get("ReplicaGroups"):
                obj = ReplicaGroup()
                obj._deserialize(item)
                self._ReplicaGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页输出的实例列表的大小，即每页输出的实例数量，默认值20，取值范围为[1,1000]。
        :type Limit: int
        :param _Offset: 分页偏移量，取Limit整数倍。
计算公式为offset=limit*(页码-1)。例如 limit=10，第1页offset就为0，第2页offset就为10，依次类推。
        :type Offset: int
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param _OrderBy: 排序依据。枚举范围如下所示。 <ul><li>projectId：实例按照项目ID排序。</li><li>createtime：实例按照创建时间排序。</li><li>instancename：实例按照实例名称排序。</li><li>type：实例按照类型排序。</li><li>curDeadline：实例按照到期时间排序。</li></ul>
        :type OrderBy: str
        :param _OrderType: 排序方式。<ul><li>1：倒序。默认为倒序。</li><li>0：顺序。</li></ul>
        :type OrderType: int
        :param _VpcIds: 私有网络ID数组。数组下标从0开始，如果不传则默认选择基础网络，如：47525
        :type VpcIds: list of str
        :param _SubnetIds: 子网ID数组，数组下标从0开始，如：56854
        :type SubnetIds: list of str
        :param _ProjectIds: 项目ID 组成的数组，数组下标从0开始
        :type ProjectIds: list of int
        :param _SearchKey: 查找关键字，可输入实例的ID或者实例名称。
        :type SearchKey: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _UniqVpcIds: 私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络，如：vpc-sad23jfdfk
        :type UniqVpcIds: list of str
        :param _UniqSubnetIds: 子网ID数组，数组下标从0开始，如：subnet-fdj24n34j2
        :type UniqSubnetIds: list of str
        :param _Status: 实例状态。<ul><li>0：待初始化。</li><li>1：流程中。</li><li>2：运行中。</li><li>-2：已隔离。</li><li>-3：待删除。</li></ul>
        :type Status: list of int
        :param _AutoRenew: 包年包月计费的续费模式。<ul><li>0：默认状态，指手动续费。</li><li>1：自动续费。</li><li>2：到期不再续费。</ul>
        :type AutoRenew: list of int
        :param _BillingMode: 计费模式。<ul><li>postpaid：按量计费。</li><li>prepaid：包年包月。</li></ul>
        :type BillingMode: str
        :param _Type: 实例类型。<ul><li>13：标准版。</li><li>14：集群版。</li></ul>
        :type Type: int
        :param _SearchKeys: 搜索关键词：支持实例 ID、实例名称、私有网络IP地址。
        :type SearchKeys: list of str
        :param _TypeList: 内部参数，用户可忽略。
        :type TypeList: list of int
        :param _MonitorVersion: 内部参数，用户可忽略。
        :type MonitorVersion: str
        :param _InstanceTags: 根据标签的 Key 和 Value 筛选资源。该参数不配置或者数组设置为空值，则不根据标签进行过滤。
        :type InstanceTags: :class:`tencentcloud.keewidb.v20220308.models.InstanceTagInfo`
        :param _TagKeys: 根据标签的 Key 筛选资源，该参数不配置或者数组设置为空值，则不根据标签Key进行过滤。
        :type TagKeys: list of str
        """
        self._Limit = None
        self._Offset = None
        self._InstanceId = None
        self._OrderBy = None
        self._OrderType = None
        self._VpcIds = None
        self._SubnetIds = None
        self._ProjectIds = None
        self._SearchKey = None
        self._InstanceName = None
        self._UniqVpcIds = None
        self._UniqSubnetIds = None
        self._Status = None
        self._AutoRenew = None
        self._BillingMode = None
        self._Type = None
        self._SearchKeys = None
        self._TypeList = None
        self._MonitorVersion = None
        self._InstanceTags = None
        self._TagKeys = None

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

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def VpcIds(self):
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def UniqVpcIds(self):
        return self._UniqVpcIds

    @UniqVpcIds.setter
    def UniqVpcIds(self, UniqVpcIds):
        self._UniqVpcIds = UniqVpcIds

    @property
    def UniqSubnetIds(self):
        return self._UniqSubnetIds

    @UniqSubnetIds.setter
    def UniqSubnetIds(self, UniqSubnetIds):
        self._UniqSubnetIds = UniqSubnetIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SearchKeys(self):
        return self._SearchKeys

    @SearchKeys.setter
    def SearchKeys(self, SearchKeys):
        self._SearchKeys = SearchKeys

    @property
    def TypeList(self):
        return self._TypeList

    @TypeList.setter
    def TypeList(self, TypeList):
        self._TypeList = TypeList

    @property
    def MonitorVersion(self):
        return self._MonitorVersion

    @MonitorVersion.setter
    def MonitorVersion(self, MonitorVersion):
        self._MonitorVersion = MonitorVersion

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceId = params.get("InstanceId")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._VpcIds = params.get("VpcIds")
        self._SubnetIds = params.get("SubnetIds")
        self._ProjectIds = params.get("ProjectIds")
        self._SearchKey = params.get("SearchKey")
        self._InstanceName = params.get("InstanceName")
        self._UniqVpcIds = params.get("UniqVpcIds")
        self._UniqSubnetIds = params.get("UniqSubnetIds")
        self._Status = params.get("Status")
        self._AutoRenew = params.get("AutoRenew")
        self._BillingMode = params.get("BillingMode")
        self._Type = params.get("Type")
        self._SearchKeys = params.get("SearchKeys")
        self._TypeList = params.get("TypeList")
        self._MonitorVersion = params.get("MonitorVersion")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = InstanceTagInfo()
            self._InstanceTags._deserialize(params.get("InstanceTags"))
        self._TagKeys = params.get("TagKeys")
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
        :param _TotalCount: 实例数
        :type TotalCount: int
        :param _InstanceSet: 实例详细信息列表
        :type InstanceSet: list of InstanceInfo
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
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMaintenanceWindowRequest(AbstractModel):
    """DescribeMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubhg***。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaintenanceWindowResponse(AbstractModel):
    """DescribeMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 维护时间窗起始时间，如：03:00。
        :type StartTime: str
        :param _EndTime: 维护时间窗结束时间，如：06:00。
        :type EndTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._RequestId = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeProductInfoRequest(AbstractModel):
    """DescribeProductInfo请求参数结构体

    """


class DescribeProductInfoResponse(AbstractModel):
    """DescribeProductInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionSet: 地域售卖信息
        :type RegionSet: list of RegionConf
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = RegionConf()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称。该产品固定为 keewidb。
        :type Product: str
        :param _ProjectId: 项目 ID。
登录 [账号中心](https://console.cloud.tencent.com/developer)，在<b>项目管理</b>中可获取项目 ID。
        :type ProjectId: int
        :param _Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param _Limit: 每页安全组的数量限制。默认为 20，最多输出100条。
        :type Limit: int
        :param _SearchKey: 搜索关键词，支持根据安全组 ID 或者安全组名称搜索。
        :type SearchKey: str
        """
        self._Product = None
        self._ProjectId = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ProjectId = params.get("ProjectId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 安全组规则。
        :type Groups: list of SecurityGroup
        :param _Total: 符合条件的安全组总数量。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._Total = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProxySlowLogRequest(AbstractModel):
    """DescribeProxySlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubhgouj
        :type InstanceId: str
        :param _BeginTime: 开始时间。
        :type BeginTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _MinQueryTime: 慢查询平均执行时间阈值。<ul><li>单位：毫秒。</li><li>取值范围：10、20、30、40、50。</li></ul>
        :type MinQueryTime: int
        :param _Limit: 每个页面大小，即每个页面输出慢日志的数量。取值范围为：10、20、30、40、50，默认为 20。
        :type Limit: int
        :param _Offset: 页面偏移量，取Limit整数倍，计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self._InstanceId = None
        self._BeginTime = None
        self._EndTime = None
        self._MinQueryTime = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

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
        self._InstanceId = params.get("InstanceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._MinQueryTime = params.get("MinQueryTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySlowLogResponse(AbstractModel):
    """DescribeProxySlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 慢查询总数。
        :type TotalCount: int
        :param _InstanceProxySlowLogDetail: 慢查询详情。
        :type InstanceProxySlowLogDetail: list of InstanceProxySlowlogDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceProxySlowLogDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceProxySlowLogDetail(self):
        return self._InstanceProxySlowLogDetail

    @InstanceProxySlowLogDetail.setter
    def InstanceProxySlowLogDetail(self, InstanceProxySlowLogDetail):
        self._InstanceProxySlowLogDetail = InstanceProxySlowLogDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceProxySlowLogDetail") is not None:
            self._InstanceProxySlowLogDetail = []
            for item in params.get("InstanceProxySlowLogDetail"):
                obj = InstanceProxySlowlogDetail()
                obj._deserialize(item)
                self._InstanceProxySlowLogDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。<ul><li>preparing：待执行。</li><li>running：执行中。</li><li>succeed：成功。</li><li>failed：失败。</li><li>error：执行出错。</li></ul>
        :type Status: str
        :param _StartTime: 任务开始时间。
        :type StartTime: str
        :param _TaskType: 任务类型。
        :type TaskType: str
        :param _InstanceId: 实例的ID。
        :type InstanceId: str
        :param _TaskMessage: 任务信息，错误时显示错误信息。执行中与成功则为空值。
        :type TaskMessage: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._StartTime = None
        self._TaskType = None
        self._InstanceId = None
        self._TaskMessage = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskMessage(self):
        return self._TaskMessage

    @TaskMessage.setter
    def TaskMessage(self, TaskMessage):
        self._TaskMessage = TaskMessage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._TaskType = params.get("TaskType")
        self._InstanceId = params.get("InstanceId")
        self._TaskMessage = params.get("TaskMessage")
        self._RequestId = params.get("RequestId")


class DescribeTaskListRequest(AbstractModel):
    """DescribeTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _Limit: 每页输出的任务列表大小。默认为 20，最多输出100条。
        :type Limit: int
        :param _Offset: Offset：分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param _ProjectIds: 项目ID。
        :type ProjectIds: list of int
        :param _TaskTypes: 任务类型。可设置为：FLOW_CREATE、FLOW_SETPWD、FLOW_CLOSE等。
        :type TaskTypes: list of str
        :param _BeginTime: 起始时间。
        :type BeginTime: str
        :param _EndTime: 终止时间。
        :type EndTime: str
        :param _TaskStatus: 任务状态。
        :type TaskStatus: list of int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Limit = None
        self._Offset = None
        self._ProjectIds = None
        self._TaskTypes = None
        self._BeginTime = None
        self._EndTime = None
        self._TaskStatus = None

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

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def TaskTypes(self):
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ProjectIds = params.get("ProjectIds")
        self._TaskTypes = params.get("TaskTypes")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskListResponse(AbstractModel):
    """DescribeTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务总数。
        :type TotalCount: int
        :param _Tasks: 任务详细信息列表。
        :type Tasks: list of TaskInfoDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfoDetail()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTendisSlowLogRequest(AbstractModel):
    """DescribeTendisSlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param _BeginTime: 开始时间。
        :type BeginTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _MinQueryTime: 慢查询平均执行时间阈值。<ul><li>单位：毫秒。</li><li>取值范围：10、20、30、40、50。</li></ul>
        :type MinQueryTime: int
        :param _Limit: 每个页面大小，即每个页面输出慢日志的数量。取值范围为：10、20、30、40、50。默认为 20。
        :type Limit: int
        :param _Offset: 页面偏移量，取Limit整数倍，计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self._InstanceId = None
        self._BeginTime = None
        self._EndTime = None
        self._MinQueryTime = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

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
        self._InstanceId = params.get("InstanceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._MinQueryTime = params.get("MinQueryTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTendisSlowLogResponse(AbstractModel):
    """DescribeTendisSlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TendisSlowLogDetail: 慢查询详情。
        :type TendisSlowLogDetail: list of TendisSlowLogDetail
        :param _TotalCount: 慢查询总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TendisSlowLogDetail = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TendisSlowLogDetail(self):
        return self._TendisSlowLogDetail

    @TendisSlowLogDetail.setter
    def TendisSlowLogDetail(self, TendisSlowLogDetail):
        self._TendisSlowLogDetail = TendisSlowLogDetail

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
        if params.get("TendisSlowLogDetail") is not None:
            self._TendisSlowLogDetail = []
            for item in params.get("TendisSlowLogDetail"):
                obj = TendisSlowLogDetail()
                obj._deserialize(item)
                self._TendisSlowLogDetail.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DestroyPostpaidInstanceRequest(AbstractModel):
    """DestroyPostpaidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyPostpaidInstanceResponse(AbstractModel):
    """DestroyPostpaidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DestroyPrepaidInstanceRequest(AbstractModel):
    """DestroyPrepaidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyPrepaidInstanceResponse(AbstractModel):
    """DestroyPrepaidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 交易ID。
        :type DealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称：keewidb。
        :type Product: str
        :param _SecurityGroupId: 要绑定的安全组 ID，类似sg-efil****。
        :type SecurityGroupId: str
        :param _InstanceIds: 实例 ID，格式如：kee-c1nl****，支持指定多个实例。
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

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


class Inbound(AbstractModel):
    """安全组入站规则

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT或者DROP。
        :type Action: str
        :param _AddressModule: 地址组id代表的地址集合。
        :type AddressModule: str
        :param _CidrIp: 来源Ip或Ip段，例如192.168.0.0/16。
        :type CidrIp: str
        :param _Desc: 描述。
        :type Desc: str
        :param _IpProtocol: 网络协议，支持udp、tcp等。
        :type IpProtocol: str
        :param _PortRange: 端口。
        :type PortRange: str
        :param _ServiceModule: 服务组id代表的协议和端口集合。
        :type ServiceModule: str
        :param _Id: 安全组id代表的地址集合。
        :type Id: str
        """
        self._Action = None
        self._AddressModule = None
        self._CidrIp = None
        self._Desc = None
        self._IpProtocol = None
        self._PortRange = None
        self._ServiceModule = None
        self._Id = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def ServiceModule(self):
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._AddressModule = params.get("AddressModule")
        self._CidrIp = params.get("CidrIp")
        self._Desc = params.get("Desc")
        self._IpProtocol = params.get("IpProtocol")
        self._PortRange = params.get("PortRange")
        self._ServiceModule = params.get("ServiceModule")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnumParam(AbstractModel):
    """实例枚举类型参数描述

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名
        :type ParamName: str
        :param _ValueType: 参数类型：enum
        :type ValueType: str
        :param _NeedRestart: 修改后是否需要重启：true，false
        :type NeedRestart: str
        :param _DefaultValue: 参数默认值
        :type DefaultValue: str
        :param _CurrentValue: 当前运行参数值
        :type CurrentValue: str
        :param _Tips: 参数说明
        :type Tips: str
        :param _EnumValue: 参数可取值
        :type EnumValue: list of str
        :param _Status: 参数状态, 1: 修改中， 2：修改完成
        :type Status: int
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._EnumValue = None
        self._Status = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._EnumValue = params.get("EnumValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名称。
        :type InstanceName: str
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _Appid: 用户的Appid。
        :type Appid: int
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        :param _RegionId: 地域ID。<ul><li>1：广州。</li><li>4：上海。</li><li>8：北京。</li></ul>
        :type RegionId: int
        :param _ZoneId: 可用区 ID。
        :type ZoneId: int
        :param _VpcId: VPC 网络 ID， 如：75101。该参数当前暂保留，可忽略。
        :type VpcId: int
        :param _Status: 实例当前状态。<ul><li>0：待初始化。</li><li>1：实例在流程中。</li><li>2：实例运行中。</li><li>-2：实例已隔离。</li><li>-3：实例待删除。</li></ul>
        :type Status: int
        :param _SubnetId: VPC 网络下子网 ID， 如：46315。该参数当前暂保留，可忽略。
        :type SubnetId: int
        :param _WanIp: 实例 VIP。
        :type WanIp: str
        :param _Port: 实例端口号。
        :type Port: int
        :param _Createtime: 实例创建时间。
        :type Createtime: str
        :param _Size: 实例持久内存总容量大小，单位：MB。
        :type Size: float
        :param _Type: 实例类型。<ul><li>13：标准版。</li><li>14：集群版。</li></ul>
        :type Type: int
        :param _AutoRenewFlag: 实例是否设置自动续费标识。<ul><li>1：设置自动续费。</li><li>0：未设置自动续费。</li></ul>
        :type AutoRenewFlag: int
        :param _DeadlineTime: 实例到期时间。
        :type DeadlineTime: str
        :param _Engine: 存储引擎。
        :type Engine: str
        :param _ProductType: 产品类型。<ul><li>standalone ：标准版。</li><li>cluster ：集群版。</li></ul>
        :type ProductType: str
        :param _UniqVpcId: VPC 网络 ID， 如：vpc-fk33jsf4****。
        :type UniqVpcId: str
        :param _UniqSubnetId: VPC 网络下子网 ID，如：subnet-fd3j6l3****。
        :type UniqSubnetId: str
        :param _BillingMode: 计费模式。<ul><li>0：按量计费。</li><li>1：包年包月。</li></ul>
        :type BillingMode: int
        :param _InstanceTitle: 实例运行状态描述：如”实例运行中“。
        :type InstanceTitle: str
        :param _OfflineTime: 计划下线时间。
        :type OfflineTime: str
        :param _SubStatus: 流程中的实例，返回子状态。
        :type SubStatus: int
        :param _Tags: 反亲和性标签
        :type Tags: list of str
        :param _RedisShardSize: 分片大小。
        :type RedisShardSize: int
        :param _RedisShardNum: 分片数量。
        :type RedisShardNum: int
        :param _RedisReplicasNum: 副本数量。
        :type RedisReplicasNum: int
        :param _PriceId: 计费 ID。
        :type PriceId: int
        :param _CloseTime: 隔离时间。
        :type CloseTime: str
        :param _SlaveReadWeight: 从节点读取权重。
        :type SlaveReadWeight: int
        :param _InstanceTags: 实例关联的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTags: list of InstanceTagInfo
        :param _ProjectName: 项目名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _NoAuth: 是否为免密实例；<ul><li>true：免密实例。</li><li>false：非免密实例。</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type NoAuth: bool
        :param _ClientLimit: 客户端连接数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientLimit: int
        :param _DtsStatus: DTS状态（内部参数，用户可忽略）。
注意：此字段可能返回 null，表示取不到有效值。
        :type DtsStatus: int
        :param _NetLimit: 分片带宽上限，单位 MB。
注意：此字段可能返回 null，表示取不到有效值。
        :type NetLimit: int
        :param _PasswordFree: 免密实例标识（内部参数，用户可忽略）。
注意：此字段可能返回 null，表示取不到有效值。
        :type PasswordFree: int
        :param _ReadOnly: 实例只读标识（内部参数，用户可忽略）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnly: int
        :param _Vip6: 内部参数，用户可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip6: str
        :param _RemainBandwidthDuration: 内部参数，用户可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainBandwidthDuration: str
        :param _DiskSize: 实例的磁盘容量大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _MonitorVersion: 监控版本。<ul><li>1m：分钟粒度监控。</li><li>5s：5秒粒度监控。</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorVersion: str
        :param _ClientLimitMin: 客户端最大连接数可设置的最小值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientLimitMin: int
        :param _ClientLimitMax: 客户端最大连接数可设置的最大值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientLimitMax: int
        :param _NodeSet: 实例的节点详细信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of NodeInfo
        :param _Region: 实例所在的地域信息，比如ap-guangzhou。
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _MachineMemory: 实例内存容量，单位：GB。KeeWiDB 内存容量
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineMemory: int
        :param _DiskShardSize: 单分片磁盘大小，单位：MB
        :type DiskShardSize: int
        :param _DiskShardNum: 3
        :type DiskShardNum: int
        :param _DiskReplicasNum: 1
        :type DiskReplicasNum: int
        """
        self._InstanceName = None
        self._InstanceId = None
        self._Appid = None
        self._ProjectId = None
        self._RegionId = None
        self._ZoneId = None
        self._VpcId = None
        self._Status = None
        self._SubnetId = None
        self._WanIp = None
        self._Port = None
        self._Createtime = None
        self._Size = None
        self._Type = None
        self._AutoRenewFlag = None
        self._DeadlineTime = None
        self._Engine = None
        self._ProductType = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._BillingMode = None
        self._InstanceTitle = None
        self._OfflineTime = None
        self._SubStatus = None
        self._Tags = None
        self._RedisShardSize = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None
        self._PriceId = None
        self._CloseTime = None
        self._SlaveReadWeight = None
        self._InstanceTags = None
        self._ProjectName = None
        self._NoAuth = None
        self._ClientLimit = None
        self._DtsStatus = None
        self._NetLimit = None
        self._PasswordFree = None
        self._ReadOnly = None
        self._Vip6 = None
        self._RemainBandwidthDuration = None
        self._DiskSize = None
        self._MonitorVersion = None
        self._ClientLimitMin = None
        self._ClientLimitMax = None
        self._NodeSet = None
        self._Region = None
        self._MachineMemory = None
        self._DiskShardSize = None
        self._DiskShardNum = None
        self._DiskReplicasNum = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def WanIp(self):
        return self._WanIp

    @WanIp.setter
    def WanIp(self, WanIp):
        self._WanIp = WanIp

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Createtime(self):
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def InstanceTitle(self):
        return self._InstanceTitle

    @InstanceTitle.setter
    def InstanceTitle(self, InstanceTitle):
        self._InstanceTitle = InstanceTitle

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def SubStatus(self):
        return self._SubStatus

    @SubStatus.setter
    def SubStatus(self, SubStatus):
        self._SubStatus = SubStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RedisShardSize(self):
        return self._RedisShardSize

    @RedisShardSize.setter
    def RedisShardSize(self, RedisShardSize):
        self._RedisShardSize = RedisShardSize

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def PriceId(self):
        return self._PriceId

    @PriceId.setter
    def PriceId(self, PriceId):
        self._PriceId = PriceId

    @property
    def CloseTime(self):
        return self._CloseTime

    @CloseTime.setter
    def CloseTime(self, CloseTime):
        self._CloseTime = CloseTime

    @property
    def SlaveReadWeight(self):
        return self._SlaveReadWeight

    @SlaveReadWeight.setter
    def SlaveReadWeight(self, SlaveReadWeight):
        self._SlaveReadWeight = SlaveReadWeight

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def ClientLimit(self):
        return self._ClientLimit

    @ClientLimit.setter
    def ClientLimit(self, ClientLimit):
        self._ClientLimit = ClientLimit

    @property
    def DtsStatus(self):
        return self._DtsStatus

    @DtsStatus.setter
    def DtsStatus(self, DtsStatus):
        self._DtsStatus = DtsStatus

    @property
    def NetLimit(self):
        return self._NetLimit

    @NetLimit.setter
    def NetLimit(self, NetLimit):
        self._NetLimit = NetLimit

    @property
    def PasswordFree(self):
        return self._PasswordFree

    @PasswordFree.setter
    def PasswordFree(self, PasswordFree):
        self._PasswordFree = PasswordFree

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def Vip6(self):
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def RemainBandwidthDuration(self):
        return self._RemainBandwidthDuration

    @RemainBandwidthDuration.setter
    def RemainBandwidthDuration(self, RemainBandwidthDuration):
        self._RemainBandwidthDuration = RemainBandwidthDuration

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MonitorVersion(self):
        return self._MonitorVersion

    @MonitorVersion.setter
    def MonitorVersion(self, MonitorVersion):
        self._MonitorVersion = MonitorVersion

    @property
    def ClientLimitMin(self):
        return self._ClientLimitMin

    @ClientLimitMin.setter
    def ClientLimitMin(self, ClientLimitMin):
        self._ClientLimitMin = ClientLimitMin

    @property
    def ClientLimitMax(self):
        return self._ClientLimitMax

    @ClientLimitMax.setter
    def ClientLimitMax(self, ClientLimitMax):
        self._ClientLimitMax = ClientLimitMax

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def MachineMemory(self):
        return self._MachineMemory

    @MachineMemory.setter
    def MachineMemory(self, MachineMemory):
        self._MachineMemory = MachineMemory

    @property
    def DiskShardSize(self):
        return self._DiskShardSize

    @DiskShardSize.setter
    def DiskShardSize(self, DiskShardSize):
        self._DiskShardSize = DiskShardSize

    @property
    def DiskShardNum(self):
        return self._DiskShardNum

    @DiskShardNum.setter
    def DiskShardNum(self, DiskShardNum):
        self._DiskShardNum = DiskShardNum

    @property
    def DiskReplicasNum(self):
        return self._DiskReplicasNum

    @DiskReplicasNum.setter
    def DiskReplicasNum(self, DiskReplicasNum):
        self._DiskReplicasNum = DiskReplicasNum


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._Appid = params.get("Appid")
        self._ProjectId = params.get("ProjectId")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._Status = params.get("Status")
        self._SubnetId = params.get("SubnetId")
        self._WanIp = params.get("WanIp")
        self._Port = params.get("Port")
        self._Createtime = params.get("Createtime")
        self._Size = params.get("Size")
        self._Type = params.get("Type")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._DeadlineTime = params.get("DeadlineTime")
        self._Engine = params.get("Engine")
        self._ProductType = params.get("ProductType")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._BillingMode = params.get("BillingMode")
        self._InstanceTitle = params.get("InstanceTitle")
        self._OfflineTime = params.get("OfflineTime")
        self._SubStatus = params.get("SubStatus")
        self._Tags = params.get("Tags")
        self._RedisShardSize = params.get("RedisShardSize")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        self._PriceId = params.get("PriceId")
        self._CloseTime = params.get("CloseTime")
        self._SlaveReadWeight = params.get("SlaveReadWeight")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        self._ProjectName = params.get("ProjectName")
        self._NoAuth = params.get("NoAuth")
        self._ClientLimit = params.get("ClientLimit")
        self._DtsStatus = params.get("DtsStatus")
        self._NetLimit = params.get("NetLimit")
        self._PasswordFree = params.get("PasswordFree")
        self._ReadOnly = params.get("ReadOnly")
        self._Vip6 = params.get("Vip6")
        self._RemainBandwidthDuration = params.get("RemainBandwidthDuration")
        self._DiskSize = params.get("DiskSize")
        self._MonitorVersion = params.get("MonitorVersion")
        self._ClientLimitMin = params.get("ClientLimitMin")
        self._ClientLimitMax = params.get("ClientLimitMax")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._Region = params.get("Region")
        self._MachineMemory = params.get("MachineMemory")
        self._DiskShardSize = params.get("DiskShardSize")
        self._DiskShardNum = params.get("DiskShardNum")
        self._DiskReplicasNum = params.get("DiskReplicasNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceIntegerParam(AbstractModel):
    """实例整型参数描述

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名
        :type ParamName: str
        :param _ValueType: 参数类型：integer
        :type ValueType: str
        :param _NeedRestart: 修改后是否需要重启：true，false
        :type NeedRestart: str
        :param _DefaultValue: 参数默认值
        :type DefaultValue: str
        :param _CurrentValue: 当前运行参数值
        :type CurrentValue: str
        :param _Tips: 参数说明
        :type Tips: str
        :param _Min: 参数最小值
        :type Min: str
        :param _Max: 参数最大值
        :type Max: str
        :param _Status: 参数状态, 1: 修改中， 2：修改完成
        :type Status: int
        :param _Unit: 参数单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._Min = None
        self._Max = None
        self._Status = None
        self._Unit = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        self._Status = params.get("Status")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMultiParam(AbstractModel):
    """实例多选项类型参数描述

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名
        :type ParamName: str
        :param _ValueType: 参数类型：multi
        :type ValueType: str
        :param _NeedRestart: 修改后是否需要重启：true，false
        :type NeedRestart: str
        :param _DefaultValue: 参数默认值
        :type DefaultValue: str
        :param _CurrentValue: 当前运行参数值
        :type CurrentValue: str
        :param _Tips: 参数说明
        :type Tips: str
        :param _EnumValue: 参数说明
        :type EnumValue: list of str
        :param _Status: 参数状态, 1: 修改中， 2：修改完成
        :type Status: int
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._EnumValue = None
        self._Status = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._EnumValue = params.get("EnumValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNodeInfo(AbstractModel):
    """实例节点信息

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID
        :type NodeId: str
        :param _NodeRole: 节点角色
        :type NodeRole: str
        """
        self._NodeId = None
        self._NodeRole = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeRole = params.get("NodeRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParam(AbstractModel):
    """实例参数

    """

    def __init__(self):
        r"""
        :param _Key: 设置参数的名字
        :type Key: str
        :param _Value: 设置参数的值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParamHistory(AbstractModel):
    """实例参数修改历史

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名称
        :type ParamName: str
        :param _PreValue: 修改前值
        :type PreValue: str
        :param _NewValue: 修改后值
        :type NewValue: str
        :param _Status: 状态：1-参数配置修改中；2-参数配置修改成功；3-参数配置修改失败
        :type Status: int
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._ParamName = None
        self._PreValue = None
        self._NewValue = None
        self._Status = None
        self._ModifyTime = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def PreValue(self):
        return self._PreValue

    @PreValue.setter
    def PreValue(self, PreValue):
        self._PreValue = PreValue

    @property
    def NewValue(self):
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._PreValue = params.get("PreValue")
        self._NewValue = params.get("NewValue")
        self._Status = params.get("Status")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceProxySlowlogDetail(AbstractModel):
    """代理慢查询详情

    """

    def __init__(self):
        r"""
        :param _Duration: 慢查询耗时
        :type Duration: int
        :param _Client: 客户端地址
        :type Client: str
        :param _Command: 命令
        :type Command: str
        :param _CommandLine: 详细命令行信息
        :type CommandLine: str
        :param _ExecuteTime: 执行时间
        :type ExecuteTime: str
        """
        self._Duration = None
        self._Client = None
        self._Command = None
        self._CommandLine = None
        self._ExecuteTime = None

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Client(self):
        return self._Client

    @Client.setter
    def Client(self, Client):
        self._Client = Client

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def ExecuteTime(self):
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._Client = params.get("Client")
        self._Command = params.get("Command")
        self._CommandLine = params.get("CommandLine")
        self._ExecuteTime = params.get("ExecuteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTagInfo(AbstractModel):
    """实例标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
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
        


class InstanceTextParam(AbstractModel):
    """实例字符型参数描述

    """

    def __init__(self):
        r"""
        :param _ParamName: 参数名
        :type ParamName: str
        :param _ValueType: 参数类型：text
        :type ValueType: str
        :param _NeedRestart: 修改后是否需要重启：true，false
        :type NeedRestart: str
        :param _DefaultValue: 参数默认值
        :type DefaultValue: str
        :param _CurrentValue: 当前运行参数值
        :type CurrentValue: str
        :param _Tips: 参数说明
        :type Tips: str
        :param _TextValue: 参数可取值
        :type TextValue: list of str
        :param _Status: 参数状态, 1: 修改中， 2：修改完成
        :type Status: int
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._TextValue = None
        self._Status = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def TextValue(self):
        return self._TextValue

    @TextValue.setter
    def TextValue(self, TextValue):
        self._TextValue = TextValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._TextValue = params.get("TextValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeeWiDBNode(AbstractModel):
    """KeeWiDB节点的运行信息

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点的序列ID。
        :type NodeId: str
        :param _Status: 节点的状态。
        :type Status: str
        :param _Role: 节点角色。
        :type Role: str
        """
        self._NodeId = None
        self._Status = None
        self._Role = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Status = params.get("Status")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoBackupConfigRequest(AbstractModel):
    """ModifyAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _WeekDays: 备份周期。可设置为 Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday，该参数暂不支持修改、
        :type WeekDays: list of str
        :param _TimePeriod: 备份任务执行时间段。
可设置的格式为一个整点到下一个整点。例如：00:00-01:00、01:00-02:00、21:00-22:00、23:00-00:00等。
        :type TimePeriod: str
        """
        self._InstanceId = None
        self._WeekDays = None
        self._TimePeriod = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WeekDays(self):
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._WeekDays = params.get("WeekDays")
        self._TimePeriod = params.get("TimePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoBackupConfigResponse(AbstractModel):
    """ModifyAutoBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BackupStorageDays: 增量备份文件保存天数。
        :type BackupStorageDays: int
        :param _BinlogStorageDays: 全量备份文件保存天数。
        :type BinlogStorageDays: int
        :param _TimePeriod: 备份时间段。
        :type TimePeriod: str
        :param _WeekDays: 备份周期。Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :type WeekDays: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BackupStorageDays = None
        self._BinlogStorageDays = None
        self._TimePeriod = None
        self._WeekDays = None
        self._RequestId = None

    @property
    def BackupStorageDays(self):
        return self._BackupStorageDays

    @BackupStorageDays.setter
    def BackupStorageDays(self, BackupStorageDays):
        self._BackupStorageDays = BackupStorageDays

    @property
    def BinlogStorageDays(self):
        return self._BinlogStorageDays

    @BinlogStorageDays.setter
    def BinlogStorageDays(self, BinlogStorageDays):
        self._BinlogStorageDays = BinlogStorageDays

    @property
    def TimePeriod(self):
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def WeekDays(self):
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupStorageDays = params.get("BackupStorageDays")
        self._BinlogStorageDays = params.get("BinlogStorageDays")
        self._TimePeriod = params.get("TimePeriod")
        self._WeekDays = params.get("WeekDays")
        self._RequestId = params.get("RequestId")


class ModifyConnectionConfigRequest(AbstractModel):
    """ModifyConnectionConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param _Bandwidth: 单分片附加带宽，取值范围[0,512]，单位：MB。
<ul><li>开启副本只读时，实例总带宽  = 单分片附加带宽 * 分片数 + 标准带宽 * 分片数 * Max ([只读副本数量, 1])，标准架构的分片数 = 1。</li><li>没有开启副本只读时，实例总带宽 = 单分片附加带宽 * 分片数 + 标准带宽 * 分片数，标准架构的分片数 = 1。</li></ul>
        :type Bandwidth: int
        :param _ClientLimit: 单分片的总连接数。
<ul>默认为10000，整个实例的最大连接数为单个分片的最大连接数 x 分片数量。标准架构分片数量为1。
<li>关闭副本只读：每个分片的最大连接数的取值范围为[10000,40000]。</li><li>开启副本只读：每个分片的最大连接数的取值范围为 [10000,10000 x (副本数 + 3)]。</li></ul>
        :type ClientLimit: int
        """
        self._InstanceId = None
        self._Bandwidth = None
        self._ClientLimit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def ClientLimit(self):
        return self._ClientLimit

    @ClientLimit.setter
    def ClientLimit(self, ClientLimit):
        self._ClientLimit = ClientLimit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Bandwidth = params.get("Bandwidth")
        self._ClientLimit = params.get("ClientLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConnectionConfigResponse(AbstractModel):
    """ModifyConnectionConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 数据库引擎名称：keewidb。
        :type Product: str
        :param _SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIds: list of str
        :param _InstanceId: 实例ID，格式如：kee-c1nl****。
        :type InstanceId: str
        """
        self._Product = None
        self._SecurityGroupIds = None
        self._InstanceId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

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


class ModifyInstanceParamsRequest(AbstractModel):
    """ModifyInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param _InstanceParams: 实例修改的参数列表。
        :type InstanceParams: list of InstanceParam
        """
        self._InstanceId = None
        self._InstanceParams = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceParams(self):
        return self._InstanceParams

    @InstanceParams.setter
    def InstanceParams(self, InstanceParams):
        self._InstanceParams = InstanceParams


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("InstanceParams") is not None:
            self._InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._InstanceParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamsResponse(AbstractModel):
    """ModifyInstanceParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Changed: 修改是否成功。<ul><li>true：修改成功。</li><li>false：修改失败。</li></ul>
        :type Changed: bool
        :param _TaskId: 任务 ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Changed = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Changed(self):
        return self._Changed

    @Changed.setter
    def Changed(self, Changed):
        self._Changed = Changed

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Changed = params.get("Changed")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operation: 修改实例操作。<ul><li>rename：表示实例重命名。</li><li>modifyProject：修改实例所属项目。</li><li>modifyAutoRenew：修改实例续费模式。</li></ul>
        :type Operation: str
        :param _InstanceIds: 实例 ID 数组。
        :type InstanceIds: list of str
        :param _InstanceNames: 实例的新名称。
        :type InstanceNames: list of str
        :param _ProjectId: 实例新的项目 ID。
        :type ProjectId: int
        :param _AutoRenews: 包年包月计费的续费模式。<b>InstanceIds</b>数组和<b>AutoRenews</b>数组中的修改值对应。<ul><li>0：默认状态，指手动续费。</li><li>1：自动续费。</li><li>2：到期不再续费。</ul>
        :type AutoRenews: list of int
        """
        self._Operation = None
        self._InstanceIds = None
        self._InstanceNames = None
        self._ProjectId = None
        self._AutoRenews = None

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AutoRenews(self):
        return self._AutoRenews

    @AutoRenews.setter
    def AutoRenews(self, AutoRenews):
        self._AutoRenews = AutoRenews


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._ProjectId = params.get("ProjectId")
        self._AutoRenews = params.get("AutoRenews")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回参数结构体

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


class ModifyMaintenanceWindowRequest(AbstractModel):
    """ModifyMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param _StartTime: 维护时间窗起始时间，如：03:00。
        :type StartTime: str
        :param _EndTime: 维护时间窗结束时间，如：06:00。
        :type EndTime: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintenanceWindowResponse(AbstractModel):
    """ModifyMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 执行结果。<ul><li>success：修改成功。 </li> <li>failed：修改失败。</li></ul>
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyNetworkConfigRequest(AbstractModel):
    """ModifyNetworkConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param _Operation: 操作类型。<ul><li>changeVip：修改实例私有网络。</li><li>changeVpc：修改实例私有网络所属子网。</li><li>changeBaseToVpc：基础网络转为私有网络。</li></ul>
        :type Operation: str
        :param _Vip: 修改后的 VIP 地址。
当参数<b>Operation</b>为<b>changeVip</b>时，需设置实例修改后的 VIP 地址。该参数不配置，则自动分配。
        :type Vip: str
        :param _VpcId: 修改后的私有网络 ID。
当参数<b>Operation</b>为<b>changeVip</b>或者为<b>changeBaseToVpc</b>时，务必设置实例修改后的私有网络 ID。
        :type VpcId: str
        :param _SubnetId: 修改后的所属子网 ID。
当参数<b>Operation</b>为<b>changeVpc</b>或者为<b>changeBaseToVpc</b>时，务必设置实例修改后的子网 ID。
        :type SubnetId: str
        :param _Recycle: 原 VIP 保留时长。
单位：天。取值范围：0、1、2、3、7、15。
        :type Recycle: int
        """
        self._InstanceId = None
        self._Operation = None
        self._Vip = None
        self._VpcId = None
        self._SubnetId = None
        self._Recycle = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

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
    def Recycle(self):
        return self._Recycle

    @Recycle.setter
    def Recycle(self, Recycle):
        self._Recycle = Recycle


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Operation = params.get("Operation")
        self._Vip = params.get("Vip")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Recycle = params.get("Recycle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkConfigResponse(AbstractModel):
    """ModifyNetworkConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 执行状态。<ul><li>true：执行成功。</li><li>false：执行失败。</li></ul>
        :type Status: bool
        :param _SubnetId: 修改后的子网 ID。
        :type SubnetId: str
        :param _VpcId: 修改后的私有网络 ID。
        :type VpcId: str
        :param _Vip: 修改后的 VIP 地址。
        :type Vip: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._SubnetId = None
        self._VpcId = None
        self._Vip = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Vip = params.get("Vip")
        self._RequestId = params.get("RequestId")


class NodeInfo(AbstractModel):
    """描述实例的主节点或者副本节点信息

    """

    def __init__(self):
        r"""
        :param _NodeType: 节点类型，0 为主节点，1 为副本节点
        :type NodeType: int
        :param _NodeId: 主节点或者副本节点的ID，创建时不需要传递此参数。
        :type NodeId: int
        :param _ZoneId: 主节点或者副本节点的可用区ID
        :type ZoneId: int
        :param _ZoneName: 主节点或者副本节点的可用区名称
        :type ZoneName: str
        """
        self._NodeType = None
        self._NodeId = None
        self._ZoneId = None
        self._ZoneName = None

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._NodeId = params.get("NodeId")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Outbound(AbstractModel):
    """安全组出站规则

    """

    def __init__(self):
        r"""
        :param _Action: 策略，ACCEPT或者DROP。
        :type Action: str
        :param _AddressModule: 地址组id代表的地址集合。
        :type AddressModule: str
        :param _CidrIp: 来源Ip或Ip段，例如192.168.0.0/16。
        :type CidrIp: str
        :param _Desc: 描述。
        :type Desc: str
        :param _IpProtocol: 网络协议，支持udp、tcp等。
        :type IpProtocol: str
        :param _PortRange: 端口。
        :type PortRange: str
        :param _ServiceModule: 服务组id代表的协议和端口集合。
        :type ServiceModule: str
        :param _Id: 安全组id代表的地址集合。
        :type Id: str
        """
        self._Action = None
        self._AddressModule = None
        self._CidrIp = None
        self._Desc = None
        self._IpProtocol = None
        self._PortRange = None
        self._ServiceModule = None
        self._Id = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def ServiceModule(self):
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._AddressModule = params.get("AddressModule")
        self._CidrIp = params.get("CidrIp")
        self._Desc = params.get("Desc")
        self._IpProtocol = params.get("IpProtocol")
        self._PortRange = params.get("PortRange")
        self._ServiceModule = params.get("ServiceModule")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductConf(AbstractModel):
    """产品规格信息

    """

    def __init__(self):
        r"""
        :param _Type: 产品类型，13-KeewiDB标准架构，14-KeewiDB集群架构
        :type Type: int
        :param _TypeName: KeewiDB标准架构，KeewiDB集群架构
        :type TypeName: str
        :param _MinBuyNum: 购买时的最小数量
        :type MinBuyNum: int
        :param _MaxBuyNum: 购买时的最大数量
        :type MaxBuyNum: int
        :param _Saleout: 产品是否售罄
        :type Saleout: bool
        :param _Engine: 产品引擎，keewidb
        :type Engine: str
        :param _Version: 兼容版本，Redis-2.8，Redis-3.2，Redis-4.0
        :type Version: str
        :param _ReplicaNum: 副本数量
        :type ReplicaNum: list of str
        :param _PayMode: 支持的计费模式，1-包年包月，0-按量计费
        :type PayMode: str
        """
        self._Type = None
        self._TypeName = None
        self._MinBuyNum = None
        self._MaxBuyNum = None
        self._Saleout = None
        self._Engine = None
        self._Version = None
        self._ReplicaNum = None
        self._PayMode = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def MinBuyNum(self):
        return self._MinBuyNum

    @MinBuyNum.setter
    def MinBuyNum(self, MinBuyNum):
        self._MinBuyNum = MinBuyNum

    @property
    def MaxBuyNum(self):
        return self._MaxBuyNum

    @MaxBuyNum.setter
    def MaxBuyNum(self, MaxBuyNum):
        self._MaxBuyNum = MaxBuyNum

    @property
    def Saleout(self):
        return self._Saleout

    @Saleout.setter
    def Saleout(self, Saleout):
        self._Saleout = Saleout

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ReplicaNum(self):
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TypeName = params.get("TypeName")
        self._MinBuyNum = params.get("MinBuyNum")
        self._MaxBuyNum = params.get("MaxBuyNum")
        self._Saleout = params.get("Saleout")
        self._Engine = params.get("Engine")
        self._Version = params.get("Version")
        self._ReplicaNum = params.get("ReplicaNum")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodeInfo(AbstractModel):
    """Proxy节点信息

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        """
        self._NodeId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNodeInfo(AbstractModel):
    """Redis节点信息

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID
        :type NodeId: str
        :param _NodeRole: 节点角色
        :type NodeRole: str
        :param _ClusterId: 分片ID
        :type ClusterId: int
        :param _ZoneId: 可用区ID
        :type ZoneId: int
        """
        self._NodeId = None
        self._NodeRole = None
        self._ClusterId = None
        self._ZoneId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeRole = params.get("NodeRole")
        self._ClusterId = params.get("ClusterId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionConf(AbstractModel):
    """地域售卖信息

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: str
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _RegionShortName: 地域简称
        :type RegionShortName: str
        :param _Area: 地域所在大区名称
        :type Area: str
        :param _ZoneSet: 可用区信息
        :type ZoneSet: list of ZoneCapacityConf
        """
        self._RegionId = None
        self._RegionName = None
        self._RegionShortName = None
        self._Area = None
        self._ZoneSet = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionShortName(self):
        return self._RegionShortName

    @RegionShortName.setter
    def RegionShortName(self, RegionShortName):
        self._RegionShortName = RegionShortName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._RegionShortName = params.get("RegionShortName")
        self._Area = params.get("Area")
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneCapacityConf()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceRequest(AbstractModel):
    """RenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _Period: 购买时长。单位：月。取值为 [1,2,3,4,5,6,7,8,9,10,11,12,24,36,48,60]。
        :type Period: int
        """
        self._InstanceId = None
        self._Period = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    """RenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 交易 ID。
        :type DealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class ReplicaGroup(AbstractModel):
    """实例副本组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 节点 ID。
        :type GroupId: int
        :param _GroupName: 节点组的名称，主节点为空。
        :type GroupName: str
        :param _ZoneId: 节点的可用区ID，比如ap-guangzhou-1。
        :type ZoneId: str
        :param _Role: 节点组角色。<ul><li>master：为主节点。</li><li>replica：为副本节点。</li></ul>
        :type Role: str
        :param _KeeWiDBNodes: 节点组节点列表。
        :type KeeWiDBNodes: list of KeeWiDBNode
        """
        self._GroupId = None
        self._GroupName = None
        self._ZoneId = None
        self._Role = None
        self._KeeWiDBNodes = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def KeeWiDBNodes(self):
        return self._KeeWiDBNodes

    @KeeWiDBNodes.setter
    def KeeWiDBNodes(self, KeeWiDBNodes):
        self._KeeWiDBNodes = KeeWiDBNodes


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._ZoneId = params.get("ZoneId")
        self._Role = params.get("Role")
        if params.get("KeeWiDBNodes") is not None:
            self._KeeWiDBNodes = []
            for item in params.get("KeeWiDBNodes"):
                obj = KeeWiDBNode()
                obj._deserialize(item)
                self._KeeWiDBNodes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordRequest(AbstractModel):
    """ResetPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _Password: 设置新密码。<ul><li>当参数<b>NoAuth</b>设置为<b>true</b>，切换为免密实例时，可不设置该参数。</li><li>密码复杂度要求：<ul><li>长度8 - 30位, 推荐使用12位以上的密码。</li><li>不能以"/"开头。</li>
<li>至少包含以下两项：<ul><li>小写字母a - z</li><li>大写字母A - Z</li><li>数字0 - 9</li><li>()~!@#$%^&*-+=_|{}[]:;<>,.?/</li></ul></li></ul></li></ul>
        :type Password: str
        :param _NoAuth: 标识实例是否切换免密认证。<ul><li>false：由免密码认证方式切换为密码认证实例。默认为false。</li><li>true：由密码认证方式切换为免密码认证的方式。</li></ul>
        :type NoAuth: bool
        """
        self._InstanceId = None
        self._Password = None
        self._NoAuth = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        self._NoAuth = params.get("NoAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordResponse(AbstractModel):
    """ResetPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID。
<b>说明：</b>修改密码时的任务ID，如果切换免密访问或者非免密码实例，则无需关注此返回值。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """实例绑定标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签 Key。
        :type TagKey: str
        :param _TagValue: 标签 Value。
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
        


class SecurityGroup(AbstractModel):
    """安全组规则

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss。
        :type CreateTime: str
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        :param _SecurityGroupId: 安全组ID。
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称。
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: 安全组备注。
        :type SecurityGroupRemark: str
        :param _Outbound: 出站规则。
        :type Outbound: list of Outbound
        :param _Inbound: 入站规则。
        :type Inbound: list of Inbound
        """
        self._CreateTime = None
        self._ProjectId = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._Outbound = None
        self._Inbound = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def Outbound(self):
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def Inbound(self):
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._ProjectId = params.get("ProjectId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartUpInstanceRequest(AbstractModel):
    """StartUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartUpInstanceResponse(AbstractModel):
    """StartUpInstance返回参数结构体

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


class TaskInfoDetail(AbstractModel):
    """任务信息详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: str
        :param _InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _InstanceId: 实例Id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ProjectId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _Progress: 任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: float
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Result: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: int
        :param _OperatorUin: 操作者用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUin: str
        """
        self._TaskId = None
        self._StartTime = None
        self._TaskType = None
        self._InstanceName = None
        self._InstanceId = None
        self._ProjectId = None
        self._Progress = None
        self._EndTime = None
        self._Result = None
        self._OperatorUin = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def OperatorUin(self):
        return self._OperatorUin

    @OperatorUin.setter
    def OperatorUin(self, OperatorUin):
        self._OperatorUin = OperatorUin


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._StartTime = params.get("StartTime")
        self._TaskType = params.get("TaskType")
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._ProjectId = params.get("ProjectId")
        self._Progress = params.get("Progress")
        self._EndTime = params.get("EndTime")
        self._Result = params.get("Result")
        self._OperatorUin = params.get("OperatorUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TendisSlowLogDetail(AbstractModel):
    """实例慢查询详情

    """

    def __init__(self):
        r"""
        :param _ExecuteTime: 执行时间
        :type ExecuteTime: str
        :param _Duration: 慢查询耗时（毫秒）
        :type Duration: int
        :param _Command: 命令
        :type Command: str
        :param _CommandLine: 详细命令行信息
        :type CommandLine: str
        :param _Node: 节点ID
        :type Node: str
        """
        self._ExecuteTime = None
        self._Duration = None
        self._Command = None
        self._CommandLine = None
        self._Node = None

    @property
    def ExecuteTime(self):
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def Node(self):
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node


    def _deserialize(self, params):
        self._ExecuteTime = params.get("ExecuteTime")
        self._Duration = params.get("Duration")
        self._Command = params.get("Command")
        self._CommandLine = params.get("CommandLine")
        self._Node = params.get("Node")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradeDealDetail(AbstractModel):
    """订单交易信息

    """

    def __init__(self):
        r"""
        :param _DealId: 订单号ID，调用云API时使用此ID	
        :type DealId: str
        :param _DealName: 长订单ID，反馈订单问题给官方客服使用此ID	
        :type DealName: str
        :param _ZoneId: 可用区id
        :type ZoneId: int
        :param _GoodsNum: 订单关联的实例数
        :type GoodsNum: int
        :param _Creater: 创建用户uin
        :type Creater: str
        :param _CreatTime: 订单创建时间
        :type CreatTime: str
        :param _OverdueTime: 订单超时时间
        :type OverdueTime: str
        :param _EndTime: 订单完成时间
        :type EndTime: str
        :param _Status: 订单状态 1：未支付 2:已支付，未发货 3:发货中 4:发货成功 5:发货失败 6:已退款 7:已关闭订单 8:订单过期 9:订单已失效 10:产品已失效 11:代付拒绝 12:支付中
        :type Status: int
        :param _Description: 订单状态描述
        :type Description: str
        :param _Price: 订单实际总价，单位：分
        :type Price: float
        :param _InstanceIds: 实例ID
        :type InstanceIds: list of str
        """
        self._DealId = None
        self._DealName = None
        self._ZoneId = None
        self._GoodsNum = None
        self._Creater = None
        self._CreatTime = None
        self._OverdueTime = None
        self._EndTime = None
        self._Status = None
        self._Description = None
        self._Price = None
        self._InstanceIds = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Creater(self):
        return self._Creater

    @Creater.setter
    def Creater(self, Creater):
        self._Creater = Creater

    @property
    def CreatTime(self):
        return self._CreatTime

    @CreatTime.setter
    def CreatTime(self, CreatTime):
        self._CreatTime = CreatTime

    @property
    def OverdueTime(self):
        return self._OverdueTime

    @OverdueTime.setter
    def OverdueTime(self, OverdueTime):
        self._OverdueTime = OverdueTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._DealName = params.get("DealName")
        self._ZoneId = params.get("ZoneId")
        self._GoodsNum = params.get("GoodsNum")
        self._Creater = params.get("Creater")
        self._CreatTime = params.get("CreatTime")
        self._OverdueTime = params.get("OverdueTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._Price = params.get("Price")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _MemSize: 配置变更后，每个分片持久化内存容量，单位：GB。
<ul><li>KeeWiDB 内存容量<b>MachineMemory</b>与持久内存容量<b>MemSize</b>为固定搭配，即2GB内存，固定分配8GB的持久内存，不可选择。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。</li><li>变更实例内存、持久化内存与磁盘、变更实例的分片数量，每次只能变更一项。</li></ul>
        :type MemSize: int
        :param _MachineCpu: CPU 核数。
        :type MachineCpu: int
        :param _MachineMemory: 实例内存容量，单位：GB。
<ul><li>KeeWiDB 内存容量<b>MachineMemory</b>与持久内存容量<b>MemSize</b>为固定搭配，即2GB内存，固定分配8GB的持久内存，不可选择。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。</li><li>变更实例内存、持久化内存与磁盘、变更实例的分片数量，每次只能变更一项。</li></ul>
        :type MachineMemory: int
        :param _ShardNum: 配置变更后，分片数量。
<ul><li>增加后分片的数量务必为增加之前数量的整数倍。分片数量支持选择3、5、6、8、9、10、12、15、16、18、20、21、24、25、27、30、32、33、35、36、39、40、42、45、48、50、51、54、55、56、57、60、63、64分片。</li><li>变更实例内存、持久化内存与磁盘、变更实例的分片数量，每次只能变更一项。</li></ul>
        :type ShardNum: int
        :param _DiskSize: 配置变更后，每个分片硬盘的容量。单位：GB。
<ul><li>每一缓存分片容量，对应的磁盘容量范围不同。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。</li><li>变更实例内存、持久化内存与磁盘、变更实例的分片数量，每次只能变更一项。</li></ul>
        :type DiskSize: int
        """
        self._InstanceId = None
        self._MemSize = None
        self._MachineCpu = None
        self._MachineMemory = None
        self._ShardNum = None
        self._DiskSize = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def MachineCpu(self):
        return self._MachineCpu

    @MachineCpu.setter
    def MachineCpu(self, MachineCpu):
        self._MachineCpu = MachineCpu

    @property
    def MachineMemory(self):
        return self._MachineMemory

    @MachineMemory.setter
    def MachineMemory(self, MachineMemory):
        self._MachineMemory = MachineMemory

    @property
    def ShardNum(self):
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MemSize = params.get("MemSize")
        self._MachineCpu = params.get("MachineCpu")
        self._MachineMemory = params.get("MachineMemory")
        self._ShardNum = params.get("ShardNum")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealId: 交易ID。
        :type DealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class ZoneCapacityConf(AbstractModel):
    """可用区内产品售卖信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区ID
        :type ZoneId: str
        :param _ZoneName: 可用区名称
        :type ZoneName: str
        :param _IsSaleout: 可用区是否售罄
        :type IsSaleout: bool
        :param _IsDefault: 是否为默认可用区
        :type IsDefault: bool
        :param _NetWorkType: 网络类型：basenet -- 基础网络；vpcnet -- VPC网络
        :type NetWorkType: list of str
        :param _ProductSet: 产品规格等信息
        :type ProductSet: list of ProductConf
        :param _OldZoneId: Int类型可用区ID
        :type OldZoneId: int
        """
        self._ZoneId = None
        self._ZoneName = None
        self._IsSaleout = None
        self._IsDefault = None
        self._NetWorkType = None
        self._ProductSet = None
        self._OldZoneId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def IsSaleout(self):
        return self._IsSaleout

    @IsSaleout.setter
    def IsSaleout(self, IsSaleout):
        self._IsSaleout = IsSaleout

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def NetWorkType(self):
        return self._NetWorkType

    @NetWorkType.setter
    def NetWorkType(self, NetWorkType):
        self._NetWorkType = NetWorkType

    @property
    def ProductSet(self):
        return self._ProductSet

    @ProductSet.setter
    def ProductSet(self, ProductSet):
        self._ProductSet = ProductSet

    @property
    def OldZoneId(self):
        return self._OldZoneId

    @OldZoneId.setter
    def OldZoneId(self, OldZoneId):
        self._OldZoneId = OldZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._IsSaleout = params.get("IsSaleout")
        self._IsDefault = params.get("IsDefault")
        self._NetWorkType = params.get("NetWorkType")
        if params.get("ProductSet") is not None:
            self._ProductSet = []
            for item in params.get("ProductSet"):
                obj = ProductConf()
                obj._deserialize(item)
                self._ProductSet.append(obj)
        self._OldZoneId = params.get("OldZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        