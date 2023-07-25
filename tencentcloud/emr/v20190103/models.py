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


class AddUsersForUserManagerRequest(AbstractModel):
    """AddUsersForUserManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群字符串ID
        :type InstanceId: str
        :param _UserManagerUserList: 用户信息列表
        :type UserManagerUserList: list of UserInfoForUserManager
        """
        self._InstanceId = None
        self._UserManagerUserList = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserManagerUserList(self):
        return self._UserManagerUserList

    @UserManagerUserList.setter
    def UserManagerUserList(self, UserManagerUserList):
        self._UserManagerUserList = UserManagerUserList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("UserManagerUserList") is not None:
            self._UserManagerUserList = []
            for item in params.get("UserManagerUserList"):
                obj = UserInfoForUserManager()
                obj._deserialize(item)
                self._UserManagerUserList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUsersForUserManagerResponse(AbstractModel):
    """AddUsersForUserManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessUserList: 添加成功的用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessUserList: list of str
        :param _FailedUserList: 添加失败的用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedUserList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessUserList = None
        self._FailedUserList = None
        self._RequestId = None

    @property
    def SuccessUserList(self):
        return self._SuccessUserList

    @SuccessUserList.setter
    def SuccessUserList(self, SuccessUserList):
        self._SuccessUserList = SuccessUserList

    @property
    def FailedUserList(self):
        return self._FailedUserList

    @FailedUserList.setter
    def FailedUserList(self, FailedUserList):
        self._FailedUserList = FailedUserList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessUserList = params.get("SuccessUserList")
        self._FailedUserList = params.get("FailedUserList")
        self._RequestId = params.get("RequestId")


class AllNodeResourceSpec(AbstractModel):
    """资源描述

    """

    def __init__(self):
        r"""
        :param _MasterResourceSpec: 描述Master节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _CoreResourceSpec: 描述Core节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _TaskResourceSpec: 描述Taskr节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _CommonResourceSpec: 描述Common节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _MasterCount: Master节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterCount: int
        :param _CoreCount: Corer节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreCount: int
        :param _TaskCount: Task节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCount: int
        :param _CommonCount: Common节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonCount: int
        """
        self._MasterResourceSpec = None
        self._CoreResourceSpec = None
        self._TaskResourceSpec = None
        self._CommonResourceSpec = None
        self._MasterCount = None
        self._CoreCount = None
        self._TaskCount = None
        self._CommonCount = None

    @property
    def MasterResourceSpec(self):
        return self._MasterResourceSpec

    @MasterResourceSpec.setter
    def MasterResourceSpec(self, MasterResourceSpec):
        self._MasterResourceSpec = MasterResourceSpec

    @property
    def CoreResourceSpec(self):
        return self._CoreResourceSpec

    @CoreResourceSpec.setter
    def CoreResourceSpec(self, CoreResourceSpec):
        self._CoreResourceSpec = CoreResourceSpec

    @property
    def TaskResourceSpec(self):
        return self._TaskResourceSpec

    @TaskResourceSpec.setter
    def TaskResourceSpec(self, TaskResourceSpec):
        self._TaskResourceSpec = TaskResourceSpec

    @property
    def CommonResourceSpec(self):
        return self._CommonResourceSpec

    @CommonResourceSpec.setter
    def CommonResourceSpec(self, CommonResourceSpec):
        self._CommonResourceSpec = CommonResourceSpec

    @property
    def MasterCount(self):
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def TaskCount(self):
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CommonCount(self):
        return self._CommonCount

    @CommonCount.setter
    def CommonCount(self, CommonCount):
        self._CommonCount = CommonCount


    def _deserialize(self, params):
        if params.get("MasterResourceSpec") is not None:
            self._MasterResourceSpec = NodeResourceSpec()
            self._MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self._CoreResourceSpec = NodeResourceSpec()
            self._CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self._TaskResourceSpec = NodeResourceSpec()
            self._TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        if params.get("CommonResourceSpec") is not None:
            self._CommonResourceSpec = NodeResourceSpec()
            self._CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self._MasterCount = params.get("MasterCount")
        self._CoreCount = params.get("CoreCount")
        self._TaskCount = params.get("TaskCount")
        self._CommonCount = params.get("CommonCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationStatics(AbstractModel):
    """yarn application 统计信息

    """

    def __init__(self):
        r"""
        :param _Queue: 队列名
        :type Queue: str
        :param _User: 用户名
        :type User: str
        :param _ApplicationType: 作业类型
        :type ApplicationType: str
        :param _SumMemorySeconds: SumMemorySeconds含义
        :type SumMemorySeconds: int
        :param _SumVCoreSeconds: SumVCoreSeconds含义
        :type SumVCoreSeconds: int
        :param _SumHDFSBytesWritten: SumHDFSBytesWritten（带单位）
        :type SumHDFSBytesWritten: str
        :param _SumHDFSBytesRead: SumHDFSBytesRead（待单位）
        :type SumHDFSBytesRead: str
        :param _CountApps: 作业数
        :type CountApps: int
        """
        self._Queue = None
        self._User = None
        self._ApplicationType = None
        self._SumMemorySeconds = None
        self._SumVCoreSeconds = None
        self._SumHDFSBytesWritten = None
        self._SumHDFSBytesRead = None
        self._CountApps = None

    @property
    def Queue(self):
        return self._Queue

    @Queue.setter
    def Queue(self, Queue):
        self._Queue = Queue

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def SumMemorySeconds(self):
        return self._SumMemorySeconds

    @SumMemorySeconds.setter
    def SumMemorySeconds(self, SumMemorySeconds):
        self._SumMemorySeconds = SumMemorySeconds

    @property
    def SumVCoreSeconds(self):
        return self._SumVCoreSeconds

    @SumVCoreSeconds.setter
    def SumVCoreSeconds(self, SumVCoreSeconds):
        self._SumVCoreSeconds = SumVCoreSeconds

    @property
    def SumHDFSBytesWritten(self):
        return self._SumHDFSBytesWritten

    @SumHDFSBytesWritten.setter
    def SumHDFSBytesWritten(self, SumHDFSBytesWritten):
        self._SumHDFSBytesWritten = SumHDFSBytesWritten

    @property
    def SumHDFSBytesRead(self):
        return self._SumHDFSBytesRead

    @SumHDFSBytesRead.setter
    def SumHDFSBytesRead(self, SumHDFSBytesRead):
        self._SumHDFSBytesRead = SumHDFSBytesRead

    @property
    def CountApps(self):
        return self._CountApps

    @CountApps.setter
    def CountApps(self, CountApps):
        self._CountApps = CountApps


    def _deserialize(self, params):
        self._Queue = params.get("Queue")
        self._User = params.get("User")
        self._ApplicationType = params.get("ApplicationType")
        self._SumMemorySeconds = params.get("SumMemorySeconds")
        self._SumVCoreSeconds = params.get("SumVCoreSeconds")
        self._SumHDFSBytesWritten = params.get("SumHDFSBytesWritten")
        self._SumHDFSBytesRead = params.get("SumHDFSBytesRead")
        self._CountApps = params.get("CountApps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BootstrapAction(AbstractModel):
    """引导脚本

    """

    def __init__(self):
        r"""
        :param _Path: 脚本位置，支持cos上的文件，且只支持https协议。
        :type Path: str
        :param _WhenRun: 执行时间。
resourceAfter 表示在机器资源申请成功后执行。
clusterBefore 表示在集群初始化前执行。
clusterAfter 表示在集群初始化后执行。
        :type WhenRun: str
        :param _Args: 脚本参数
        :type Args: list of str
        """
        self._Path = None
        self._WhenRun = None
        self._Args = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def WhenRun(self):
        return self._WhenRun

    @WhenRun.setter
    def WhenRun(self, WhenRun):
        self._WhenRun = WhenRun

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._WhenRun = params.get("WhenRun")
        self._Args = params.get("Args")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class COSSettings(AbstractModel):
    """COS 相关配置

    """

    def __init__(self):
        r"""
        :param _CosSecretId: COS SecretId
        :type CosSecretId: str
        :param _CosSecretKey: COS SecrectKey
        :type CosSecretKey: str
        :param _LogOnCosPath: 日志存储在COS上的路径
        :type LogOnCosPath: str
        """
        self._CosSecretId = None
        self._CosSecretKey = None
        self._LogOnCosPath = None

    @property
    def CosSecretId(self):
        return self._CosSecretId

    @CosSecretId.setter
    def CosSecretId(self, CosSecretId):
        self._CosSecretId = CosSecretId

    @property
    def CosSecretKey(self):
        return self._CosSecretKey

    @CosSecretKey.setter
    def CosSecretKey(self, CosSecretKey):
        self._CosSecretKey = CosSecretKey

    @property
    def LogOnCosPath(self):
        return self._LogOnCosPath

    @LogOnCosPath.setter
    def LogOnCosPath(self, LogOnCosPath):
        self._LogOnCosPath = LogOnCosPath


    def _deserialize(self, params):
        self._CosSecretId = params.get("CosSecretId")
        self._CosSecretKey = params.get("CosSecretKey")
        self._LogOnCosPath = params.get("LogOnCosPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbInfo(AbstractModel):
    """出参

    """

    def __init__(self):
        r"""
        :param _InstanceName: 数据库实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Ip: 数据库IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: 数据库端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _MemSize: 数据库内存规格
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _Volume: 数据库磁盘规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Volume: int
        :param _Service: 服务标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyTime: str
        :param _PayType: 付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PayType: int
        :param _ExpireFlag: 过期标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireFlag: bool
        :param _Status: 数据库状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _IsAutoRenew: 续费标识
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoRenew: int
        :param _SerialNo: 数据库字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialNo: str
        :param _ZoneId: ZoneId
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _RegionId: RegionId
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        """
        self._InstanceName = None
        self._Ip = None
        self._Port = None
        self._MemSize = None
        self._Volume = None
        self._Service = None
        self._ExpireTime = None
        self._ApplyTime = None
        self._PayType = None
        self._ExpireFlag = None
        self._Status = None
        self._IsAutoRenew = None
        self._SerialNo = None
        self._ZoneId = None
        self._RegionId = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ApplyTime(self):
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def ExpireFlag(self):
        return self._ExpireFlag

    @ExpireFlag.setter
    def ExpireFlag(self, ExpireFlag):
        self._ExpireFlag = ExpireFlag

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsAutoRenew(self):
        return self._IsAutoRenew

    @IsAutoRenew.setter
    def IsAutoRenew(self, IsAutoRenew):
        self._IsAutoRenew = IsAutoRenew

    @property
    def SerialNo(self):
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._MemSize = params.get("MemSize")
        self._Volume = params.get("Volume")
        self._Service = params.get("Service")
        self._ExpireTime = params.get("ExpireTime")
        self._ApplyTime = params.get("ApplyTime")
        self._PayType = params.get("PayType")
        self._ExpireFlag = params.get("ExpireFlag")
        self._Status = params.get("Status")
        self._IsAutoRenew = params.get("IsAutoRenew")
        self._SerialNo = params.get("SerialNo")
        self._ZoneId = params.get("ZoneId")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterExternalServiceInfo(AbstractModel):
    """当前集群共用组件与集群对应关系

    """

    def __init__(self):
        r"""
        :param _DependType: 依赖关系，0:被其他集群依赖，1:依赖其他集群
注意：此字段可能返回 null，表示取不到有效值。
        :type DependType: int
        :param _Service: 共用组件
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param _ClusterId: 共用集群
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterStatus: 共用集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStatus: int
        """
        self._DependType = None
        self._Service = None
        self._ClusterId = None
        self._ClusterStatus = None

    @property
    def DependType(self):
        return self._DependType

    @DependType.setter
    def DependType(self, DependType):
        self._DependType = DependType

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus


    def _deserialize(self, params):
        self._DependType = params.get("DependType")
        self._Service = params.get("Service")
        self._ClusterId = params.get("ClusterId")
        self._ClusterStatus = params.get("ClusterStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInstancesInfo(AbstractModel):
    """集群实例信息

    """

    def __init__(self):
        r"""
        :param _Id: ID号
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _Ftitle: 标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Ftitle: str
        :param _ClusterName: 集群名
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _ZoneId: 地区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _AppId: 用户APPID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 用户UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _ProjectId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _VpcId: 集群VPCID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: int
        :param _Status: 实例的状态码。取值范围：
<li>2：表示集群运行中。</li>
<li>3：表示集群创建中。</li>
<li>4：表示集群扩容中。</li>
<li>5：表示集群增加router节点中。</li>
<li>6：表示集群安装组件中。</li>
<li>7：表示集群执行命令中。</li>
<li>8：表示重启服务中。</li>
<li>9：表示进入维护中。</li>
<li>10：表示服务暂停中。</li>
<li>11：表示退出维护中。</li>
<li>12：表示退出暂停中。</li>
<li>13：表示配置下发中。</li>
<li>14：表示销毁集群中。</li>
<li>15：表示销毁core节点中。</li>
<li>16：销毁task节点中。</li>
<li>17：表示销毁router节点中。</li>
<li>18：表示更改webproxy密码中。</li>
<li>19：表示集群隔离中。</li>
<li>20：表示集群冲正中。</li>
<li>21：表示集群回收中。</li>
<li>22：表示变配等待中。</li>
<li>23：表示集群已隔离。</li>
<li>24：表示缩容节点中。</li>
<li>33：表示集群等待退费中。</li>
<li>34：表示集群已退费。</li>
<li>301：表示创建失败。</li>
<li>302：表示扩容失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _AddTime: 添加时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param _RunTime: 已经运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RunTime: str
        :param _Config: 集群产品配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.emr.v20190103.models.EmrProductConfigOutter`
        :param _MasterIp: 主节点外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterIp: str
        :param _EmrVersion: EMR版本
注意：此字段可能返回 null，表示取不到有效值。
        :type EmrVersion: str
        :param _ChargeType: 收费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param _TradeVersion: 交易版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeVersion: int
        :param _ResourceOrderId: 资源订单ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceOrderId: int
        :param _IsTradeCluster: 是否计费集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTradeCluster: int
        :param _AlarmInfo: 集群错误状态告警信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmInfo: str
        :param _IsWoodpeckerCluster: 是否采用新架构
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWoodpeckerCluster: int
        :param _MetaDb: 元数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaDb: str
        :param _Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _HiveMetaDb: Hive元数据信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HiveMetaDb: str
        :param _ServiceClass: 集群类型:EMR,CLICKHOUSE,DRUID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceClass: str
        :param _AliasInfo: 集群所有节点的别名序列化
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasInfo: str
        :param _ProductId: 集群版本Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: int
        :param _Zone: 地区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _SceneName: 场景名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneName: str
        :param _SceneServiceClass: 场景化集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneServiceClass: str
        :param _SceneEmrVersion: 场景化EMR版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneEmrVersion: str
        :param _DisplayName: 场景化集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _VpcName: vpc name
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _SubnetName: subnet name
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param _ClusterExternalServiceInfo: 集群依赖关系
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterExternalServiceInfo: list of ClusterExternalServiceInfo
        :param _UniqVpcId: 集群vpcid 字符串类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UniqSubnetId: 子网id 字符串类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param _TopologyInfoList: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TopologyInfoList: list of TopologyInfo
        :param _IsMultiZoneCluster: 是否是跨AZ集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMultiZoneCluster: bool
        :param _IsCvmReplace: 是否开通异常节点自动补偿
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCvmReplace: bool
        """
        self._Id = None
        self._ClusterId = None
        self._Ftitle = None
        self._ClusterName = None
        self._RegionId = None
        self._ZoneId = None
        self._AppId = None
        self._Uin = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._AddTime = None
        self._RunTime = None
        self._Config = None
        self._MasterIp = None
        self._EmrVersion = None
        self._ChargeType = None
        self._TradeVersion = None
        self._ResourceOrderId = None
        self._IsTradeCluster = None
        self._AlarmInfo = None
        self._IsWoodpeckerCluster = None
        self._MetaDb = None
        self._Tags = None
        self._HiveMetaDb = None
        self._ServiceClass = None
        self._AliasInfo = None
        self._ProductId = None
        self._Zone = None
        self._SceneName = None
        self._SceneServiceClass = None
        self._SceneEmrVersion = None
        self._DisplayName = None
        self._VpcName = None
        self._SubnetName = None
        self._ClusterExternalServiceInfo = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._TopologyInfoList = None
        self._IsMultiZoneCluster = None
        self._IsCvmReplace = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Ftitle(self):
        return self._Ftitle

    @Ftitle.setter
    def Ftitle(self, Ftitle):
        self._Ftitle = Ftitle

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def RunTime(self):
        return self._RunTime

    @RunTime.setter
    def RunTime(self, RunTime):
        self._RunTime = RunTime

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def MasterIp(self):
        return self._MasterIp

    @MasterIp.setter
    def MasterIp(self, MasterIp):
        self._MasterIp = MasterIp

    @property
    def EmrVersion(self):
        return self._EmrVersion

    @EmrVersion.setter
    def EmrVersion(self, EmrVersion):
        self._EmrVersion = EmrVersion

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def TradeVersion(self):
        return self._TradeVersion

    @TradeVersion.setter
    def TradeVersion(self, TradeVersion):
        self._TradeVersion = TradeVersion

    @property
    def ResourceOrderId(self):
        return self._ResourceOrderId

    @ResourceOrderId.setter
    def ResourceOrderId(self, ResourceOrderId):
        self._ResourceOrderId = ResourceOrderId

    @property
    def IsTradeCluster(self):
        return self._IsTradeCluster

    @IsTradeCluster.setter
    def IsTradeCluster(self, IsTradeCluster):
        self._IsTradeCluster = IsTradeCluster

    @property
    def AlarmInfo(self):
        return self._AlarmInfo

    @AlarmInfo.setter
    def AlarmInfo(self, AlarmInfo):
        self._AlarmInfo = AlarmInfo

    @property
    def IsWoodpeckerCluster(self):
        return self._IsWoodpeckerCluster

    @IsWoodpeckerCluster.setter
    def IsWoodpeckerCluster(self, IsWoodpeckerCluster):
        self._IsWoodpeckerCluster = IsWoodpeckerCluster

    @property
    def MetaDb(self):
        return self._MetaDb

    @MetaDb.setter
    def MetaDb(self, MetaDb):
        self._MetaDb = MetaDb

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HiveMetaDb(self):
        return self._HiveMetaDb

    @HiveMetaDb.setter
    def HiveMetaDb(self, HiveMetaDb):
        self._HiveMetaDb = HiveMetaDb

    @property
    def ServiceClass(self):
        return self._ServiceClass

    @ServiceClass.setter
    def ServiceClass(self, ServiceClass):
        self._ServiceClass = ServiceClass

    @property
    def AliasInfo(self):
        return self._AliasInfo

    @AliasInfo.setter
    def AliasInfo(self, AliasInfo):
        self._AliasInfo = AliasInfo

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SceneName(self):
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def SceneServiceClass(self):
        return self._SceneServiceClass

    @SceneServiceClass.setter
    def SceneServiceClass(self, SceneServiceClass):
        self._SceneServiceClass = SceneServiceClass

    @property
    def SceneEmrVersion(self):
        return self._SceneEmrVersion

    @SceneEmrVersion.setter
    def SceneEmrVersion(self, SceneEmrVersion):
        self._SceneEmrVersion = SceneEmrVersion

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def ClusterExternalServiceInfo(self):
        return self._ClusterExternalServiceInfo

    @ClusterExternalServiceInfo.setter
    def ClusterExternalServiceInfo(self, ClusterExternalServiceInfo):
        self._ClusterExternalServiceInfo = ClusterExternalServiceInfo

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
    def TopologyInfoList(self):
        return self._TopologyInfoList

    @TopologyInfoList.setter
    def TopologyInfoList(self, TopologyInfoList):
        self._TopologyInfoList = TopologyInfoList

    @property
    def IsMultiZoneCluster(self):
        return self._IsMultiZoneCluster

    @IsMultiZoneCluster.setter
    def IsMultiZoneCluster(self, IsMultiZoneCluster):
        self._IsMultiZoneCluster = IsMultiZoneCluster

    @property
    def IsCvmReplace(self):
        return self._IsCvmReplace

    @IsCvmReplace.setter
    def IsCvmReplace(self, IsCvmReplace):
        self._IsCvmReplace = IsCvmReplace


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ClusterId = params.get("ClusterId")
        self._Ftitle = params.get("Ftitle")
        self._ClusterName = params.get("ClusterName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._AddTime = params.get("AddTime")
        self._RunTime = params.get("RunTime")
        if params.get("Config") is not None:
            self._Config = EmrProductConfigOutter()
            self._Config._deserialize(params.get("Config"))
        self._MasterIp = params.get("MasterIp")
        self._EmrVersion = params.get("EmrVersion")
        self._ChargeType = params.get("ChargeType")
        self._TradeVersion = params.get("TradeVersion")
        self._ResourceOrderId = params.get("ResourceOrderId")
        self._IsTradeCluster = params.get("IsTradeCluster")
        self._AlarmInfo = params.get("AlarmInfo")
        self._IsWoodpeckerCluster = params.get("IsWoodpeckerCluster")
        self._MetaDb = params.get("MetaDb")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HiveMetaDb = params.get("HiveMetaDb")
        self._ServiceClass = params.get("ServiceClass")
        self._AliasInfo = params.get("AliasInfo")
        self._ProductId = params.get("ProductId")
        self._Zone = params.get("Zone")
        self._SceneName = params.get("SceneName")
        self._SceneServiceClass = params.get("SceneServiceClass")
        self._SceneEmrVersion = params.get("SceneEmrVersion")
        self._DisplayName = params.get("DisplayName")
        self._VpcName = params.get("VpcName")
        self._SubnetName = params.get("SubnetName")
        if params.get("ClusterExternalServiceInfo") is not None:
            self._ClusterExternalServiceInfo = []
            for item in params.get("ClusterExternalServiceInfo"):
                obj = ClusterExternalServiceInfo()
                obj._deserialize(item)
                self._ClusterExternalServiceInfo.append(obj)
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        if params.get("TopologyInfoList") is not None:
            self._TopologyInfoList = []
            for item in params.get("TopologyInfoList"):
                obj = TopologyInfo()
                obj._deserialize(item)
                self._TopologyInfoList.append(obj)
        self._IsMultiZoneCluster = params.get("IsMultiZoneCluster")
        self._IsCvmReplace = params.get("IsCvmReplace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterSetting(AbstractModel):
    """集群配置。

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 付费方式。
PREPAID 包年包月。
POSTPAID_BY_HOUR 按量计费，默认方式。
        :type InstanceChargeType: str
        :param _SupportHA: 是否为HA集群。
        :type SupportHA: bool
        :param _SecurityGroupIds: 集群所使用的安全组，目前仅支持一个。
        :type SecurityGroupIds: list of str
        :param _Placement: 实例位置。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _VPCSettings: 实例所在VPC。
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _LoginSettings: 实例登录配置。
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param _TagSpecification: 实例标签，示例：["{\"TagKey\":\"test-tag1\",\"TagValue\":\"001\"}","{\"TagKey\":\"test-tag2\",\"TagValue\":\"002\"}"]。
        :type TagSpecification: list of str
        :param _MetaDB: 元数据库配置。
        :type MetaDB: :class:`tencentcloud.emr.v20190103.models.MetaDbInfo`
        :param _ResourceSpec: 实例硬件配置。
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResourceSpec`
        :param _PublicIpAssigned: 是否申请公网IP，默认为false。
        :type PublicIpAssigned: bool
        :param _InstanceChargePrepaid: 包年包月配置，只对包年包月集群生效。
        :type InstanceChargePrepaid: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`
        :param _DisasterRecoverGroupIds: 集群置放群组。
        :type DisasterRecoverGroupIds: str
        :param _CbsEncryptFlag: 是否使用cbs加密。
        :type CbsEncryptFlag: bool
        :param _RemoteTcpDefaultPort: 是否使用远程登录，默认为false。
        :type RemoteTcpDefaultPort: bool
        """
        self._InstanceChargeType = None
        self._SupportHA = None
        self._SecurityGroupIds = None
        self._Placement = None
        self._VPCSettings = None
        self._LoginSettings = None
        self._TagSpecification = None
        self._MetaDB = None
        self._ResourceSpec = None
        self._PublicIpAssigned = None
        self._InstanceChargePrepaid = None
        self._DisasterRecoverGroupIds = None
        self._CbsEncryptFlag = None
        self._RemoteTcpDefaultPort = None

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SupportHA(self):
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def VPCSettings(self):
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def MetaDB(self):
        return self._MetaDB

    @MetaDB.setter
    def MetaDB(self, MetaDB):
        self._MetaDB = MetaDB

    @property
    def ResourceSpec(self):
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def PublicIpAssigned(self):
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def CbsEncryptFlag(self):
        return self._CbsEncryptFlag

    @CbsEncryptFlag.setter
    def CbsEncryptFlag(self, CbsEncryptFlag):
        self._CbsEncryptFlag = CbsEncryptFlag

    @property
    def RemoteTcpDefaultPort(self):
        return self._RemoteTcpDefaultPort

    @RemoteTcpDefaultPort.setter
    def RemoteTcpDefaultPort(self, RemoteTcpDefaultPort):
        self._RemoteTcpDefaultPort = RemoteTcpDefaultPort


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._SupportHA = params.get("SupportHA")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._TagSpecification = params.get("TagSpecification")
        if params.get("MetaDB") is not None:
            self._MetaDB = MetaDbInfo()
            self._MetaDB._deserialize(params.get("MetaDB"))
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = JobFlowResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        self._PublicIpAssigned = params.get("PublicIpAssigned")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._CbsEncryptFlag = params.get("CbsEncryptFlag")
        self._RemoteTcpDefaultPort = params.get("RemoteTcpDefaultPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentBasicRestartInfo(AbstractModel):
    """操作的进程范围

    """

    def __init__(self):
        r"""
        :param _ComponentName: 进程名，必填，如NameNode
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentName: str
        :param _IpList: 操作的IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IpList: list of str
        """
        self._ComponentName = None
        self._IpList = None

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._ComponentName = params.get("ComponentName")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Configuration(AbstractModel):
    """自定义配置参数

    """

    def __init__(self):
        r"""
        :param _Classification: 配置文件名，支持SPARK、HIVE、HDFS、YARN的部分配置文件自定义。
        :type Classification: str
        :param _Properties: 配置参数通过KV的形式传入，部分文件支持自定义，可以通过特殊的键"content"传入所有内容。
        :type Properties: str
        """
        self._Classification = None
        self._Properties = None

    @property
    def Classification(self):
        return self._Classification

    @Classification.setter
    def Classification(self, Classification):
        self._Classification = Classification

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties


    def _deserialize(self, params):
        self._Classification = params.get("Classification")
        self._Properties = params.get("Properties")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductVersion: EMR产品版本名称如EMR-V2.3.0 表示2.3.0版本的EMR， 当前支持产品版本名称查询：[产品版本名称](https://cloud.tencent.com/document/product/589/66338)
        :type ProductVersion: str
        :param _EnableSupportHAFlag: 是否开启节点高可用。取值范围：
<li>true：表示开启节点高可用。</li>
<li>false：表示不开启节点高可用。</li>
        :type EnableSupportHAFlag: bool
        :param _InstanceName: 实例名称。
<li>长度限制为6-36个字符。</li>
<li>只允许包含中文、字母、数字、-、_。</li>
        :type InstanceName: str
        :param _InstanceChargeType: 实例计费模式。取值范围：
<li>PREPAID：预付费，即包年包月。</li>
<li>POSTPAID_BY_HOUR：按小时后付费。</li>
        :type InstanceChargeType: str
        :param _LoginSettings: 实例登录设置。通过该参数可以设置所购买节点的登录方式密码或者密钥。
<li>设置密钥时，密码仅用于组件原生WebUI快捷入口登录。</li>
<li>未设置密钥时，密码用于登录所购节点以及组件原生WebUI快捷入口登录。</li>
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param _SceneSoftwareConfig: 集群应用场景以及支持部署组件配置
        :type SceneSoftwareConfig: :class:`tencentcloud.emr.v20190103.models.SceneSoftwareConfig`
        :param _InstanceChargePrepaid: 即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`
        :param _SecurityGroupIds: 实例所属安全组的ID，形如sg-xxxxxxxx。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的SecurityGroupId字段来获取。
        :type SecurityGroupIds: list of str
        :param _ScriptBootstrapActionConfig: [引导操作](https://cloud.tencent.com/document/product/589/35656)脚本设置。
        :type ScriptBootstrapActionConfig: list of ScriptBootstrapActionConfig
        :param _ClientToken: 唯一随机标识，时效性为5分钟，需要调用者指定 防止客户端重复创建资源，例如 a9a90aa6-751a-41b6-aad6-fae360632808
        :type ClientToken: str
        :param _NeedMasterWan: 是否开启集群Master节点公网。取值范围：
<li>NEED_MASTER_WAN：表示开启集群Master节点公网。</li>
<li>NOT_NEED_MASTER_WAN：表示不开启。</li>默认开启集群Master节点公网。
        :type NeedMasterWan: str
        :param _EnableRemoteLoginFlag: 是否开启外网远程登录。（在SecurityGroupId不为空时，该参数无效）不填默认为不开启 取值范围：
<li>true：表示开启</li>
<li>false：表示不开启</li>
        :type EnableRemoteLoginFlag: bool
        :param _EnableKerberosFlag: 是否开启Kerberos认证。默认不开启 取值范围：
<li>true：表示开启</li>
<li>false：表示不开启</li>
        :type EnableKerberosFlag: bool
        :param _CustomConf: [自定义软件配置](https://cloud.tencent.com/document/product/589/35655?from_cn_redirect=1)
        :type CustomConf: str
        :param _Tags: 标签描述列表。通过指定该参数可以同时绑定标签到相应的实例。
        :type Tags: list of Tag
        :param _DisasterRecoverGroupIds: 分散置放群组ID列表，当前只支持指定一个。
该参数可以通过调用 [DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/product/213/17810)的返回值中的DisasterRecoverGroupId字段来获取。
        :type DisasterRecoverGroupIds: list of str
        :param _EnableCbsEncryptFlag: 是否开启集群维度CBS加密。默认不加密 取值范围：
<li>true：表示加密</li>
<li>false：表示不加密</li>
        :type EnableCbsEncryptFlag: bool
        :param _MetaDBInfo: MetaDB信息，当MetaType选择EMR_NEW_META时，MetaDataJdbcUrl MetaDataUser MetaDataPass UnifyMetaInstanceId不用填
当MetaType选择EMR_EXIT_META时，填写UnifyMetaInstanceId
当MetaType选择USER_CUSTOM_META时，填写MetaDataJdbcUrl MetaDataUser MetaDataPass
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaDBInfo`
        :param _DependService: 共享组件信息
        :type DependService: list of DependService
        :param _ZoneResourceConfiguration: 节点资源的规格，有几个可用区，就填几个，按顺序第一个为主可用区，第二个为备可用区，第三个为仲裁可用区。如果没有开启跨AZ，则长度为1即可。
        :type ZoneResourceConfiguration: list of ZoneResourceConfiguration
        """
        self._ProductVersion = None
        self._EnableSupportHAFlag = None
        self._InstanceName = None
        self._InstanceChargeType = None
        self._LoginSettings = None
        self._SceneSoftwareConfig = None
        self._InstanceChargePrepaid = None
        self._SecurityGroupIds = None
        self._ScriptBootstrapActionConfig = None
        self._ClientToken = None
        self._NeedMasterWan = None
        self._EnableRemoteLoginFlag = None
        self._EnableKerberosFlag = None
        self._CustomConf = None
        self._Tags = None
        self._DisasterRecoverGroupIds = None
        self._EnableCbsEncryptFlag = None
        self._MetaDBInfo = None
        self._DependService = None
        self._ZoneResourceConfiguration = None

    @property
    def ProductVersion(self):
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def EnableSupportHAFlag(self):
        return self._EnableSupportHAFlag

    @EnableSupportHAFlag.setter
    def EnableSupportHAFlag(self, EnableSupportHAFlag):
        self._EnableSupportHAFlag = EnableSupportHAFlag

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SceneSoftwareConfig(self):
        return self._SceneSoftwareConfig

    @SceneSoftwareConfig.setter
    def SceneSoftwareConfig(self, SceneSoftwareConfig):
        self._SceneSoftwareConfig = SceneSoftwareConfig

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ScriptBootstrapActionConfig(self):
        return self._ScriptBootstrapActionConfig

    @ScriptBootstrapActionConfig.setter
    def ScriptBootstrapActionConfig(self, ScriptBootstrapActionConfig):
        self._ScriptBootstrapActionConfig = ScriptBootstrapActionConfig

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def NeedMasterWan(self):
        return self._NeedMasterWan

    @NeedMasterWan.setter
    def NeedMasterWan(self, NeedMasterWan):
        self._NeedMasterWan = NeedMasterWan

    @property
    def EnableRemoteLoginFlag(self):
        return self._EnableRemoteLoginFlag

    @EnableRemoteLoginFlag.setter
    def EnableRemoteLoginFlag(self, EnableRemoteLoginFlag):
        self._EnableRemoteLoginFlag = EnableRemoteLoginFlag

    @property
    def EnableKerberosFlag(self):
        return self._EnableKerberosFlag

    @EnableKerberosFlag.setter
    def EnableKerberosFlag(self, EnableKerberosFlag):
        self._EnableKerberosFlag = EnableKerberosFlag

    @property
    def CustomConf(self):
        return self._CustomConf

    @CustomConf.setter
    def CustomConf(self, CustomConf):
        self._CustomConf = CustomConf

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def EnableCbsEncryptFlag(self):
        return self._EnableCbsEncryptFlag

    @EnableCbsEncryptFlag.setter
    def EnableCbsEncryptFlag(self, EnableCbsEncryptFlag):
        self._EnableCbsEncryptFlag = EnableCbsEncryptFlag

    @property
    def MetaDBInfo(self):
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo

    @property
    def DependService(self):
        return self._DependService

    @DependService.setter
    def DependService(self, DependService):
        self._DependService = DependService

    @property
    def ZoneResourceConfiguration(self):
        return self._ZoneResourceConfiguration

    @ZoneResourceConfiguration.setter
    def ZoneResourceConfiguration(self, ZoneResourceConfiguration):
        self._ZoneResourceConfiguration = ZoneResourceConfiguration


    def _deserialize(self, params):
        self._ProductVersion = params.get("ProductVersion")
        self._EnableSupportHAFlag = params.get("EnableSupportHAFlag")
        self._InstanceName = params.get("InstanceName")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("SceneSoftwareConfig") is not None:
            self._SceneSoftwareConfig = SceneSoftwareConfig()
            self._SceneSoftwareConfig._deserialize(params.get("SceneSoftwareConfig"))
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("ScriptBootstrapActionConfig") is not None:
            self._ScriptBootstrapActionConfig = []
            for item in params.get("ScriptBootstrapActionConfig"):
                obj = ScriptBootstrapActionConfig()
                obj._deserialize(item)
                self._ScriptBootstrapActionConfig.append(obj)
        self._ClientToken = params.get("ClientToken")
        self._NeedMasterWan = params.get("NeedMasterWan")
        self._EnableRemoteLoginFlag = params.get("EnableRemoteLoginFlag")
        self._EnableKerberosFlag = params.get("EnableKerberosFlag")
        self._CustomConf = params.get("CustomConf")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._EnableCbsEncryptFlag = params.get("EnableCbsEncryptFlag")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaDBInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        if params.get("DependService") is not None:
            self._DependService = []
            for item in params.get("DependService"):
                obj = DependService()
                obj._deserialize(item)
                self._DependService.append(obj)
        if params.get("ZoneResourceConfiguration") is not None:
            self._ZoneResourceConfiguration = []
            for item in params.get("ZoneResourceConfiguration"):
                obj = ZoneResourceConfiguration()
                obj._deserialize(item)
                self._ZoneResourceConfiguration.append(obj)
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
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID，不同产品ID表示不同的EMR产品版本。取值范围：
<li>16：表示EMR-V2.3.0。</li>
<li>20：表示EMR-V2.5.0。</li>
<li>25：表示EMR-V3.1.0。</li>
<li>27：表示KAFKA-V1.0.0。</li>
<li>30：表示EMR-V2.6.0。</li>
<li>33 :   表示EMR-V3.2.1。</li>
<li>34 :   表示EMR-V3.3.0。</li>
<li>36 :   表示STARROCKS-V1.0.0。</li>
<li>37 :   表示EMR-V3.4.0。</li>
<li>38 :   表示EMR-V2.7.0。</li>
<li>39 :   表示STARROCKS-V1.1.0。</li>
<li>41 :   表示DRUID-V1.1.0。</li>
        :type ProductId: int
        :param _Software: 部署的组件列表。不同的EMR产品ID（ProductId：具体含义参考入参ProductId字段）对应不同可选组件列表，不同产品版本可选组件列表查询：[组件版本](https://cloud.tencent.com/document/product/589/20279) ；
填写实例值：hive、flink。
        :type Software: list of str
        :param _SupportHA: 是否开启节点高可用。取值范围：
<li>0：表示不开启节点高可用。</li>
<li>1：表示开启节点高可用。</li>
        :type SupportHA: int
        :param _InstanceName: 实例名称。
<li>长度限制为6-36个字符。</li>
<li>只允许包含中文、字母、数字、-、_。</li>
        :type InstanceName: str
        :param _PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param _TimeSpan: 购买实例的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param _TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param _LoginSettings: 实例登录设置。通过该参数可以设置所购买节点的登录方式密码或者密钥。
<li>设置密钥时，密码仅用于组件原生WebUI快捷入口登录。</li>
<li>未设置密钥时，密码用于登录所购节点以及组件原生WebUI快捷入口登录。</li>
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param _VPCSettings: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _ResourceSpec: 节点资源的规格。
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        :param _COSSettings: 开启COS访问需要设置的参数。
        :type COSSettings: :class:`tencentcloud.emr.v20190103.models.COSSettings`
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _SgId: 实例所属安全组的ID，形如sg-xxxxxxxx。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的SecurityGroupId字段来获取。
        :type SgId: str
        :param _PreExecutedFileSettings: [引导操作](https://cloud.tencent.com/document/product/589/35656)脚本设置。
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param _AutoRenew: 包年包月实例是否自动续费。取值范围：
<li>0：表示不自动续费。</li>
<li>1：表示自动续费。</li>
        :type AutoRenew: int
        :param _ClientToken: 客户端Token。
        :type ClientToken: str
        :param _NeedMasterWan: 是否开启集群Master节点公网。取值范围：
<li>NEED_MASTER_WAN：表示开启集群Master节点公网。</li>
<li>NOT_NEED_MASTER_WAN：表示不开启。</li>默认开启集群Master节点公网。
        :type NeedMasterWan: str
        :param _RemoteLoginAtCreate: 是否需要开启外网远程登录，即22号端口。在SgId不为空时，该参数无效。
        :type RemoteLoginAtCreate: int
        :param _CheckSecurity: 是否开启安全集群。0表示不开启，非0表示开启。
        :type CheckSecurity: int
        :param _ExtendFsField: 访问外部文件系统。
        :type ExtendFsField: str
        :param _Tags: 标签描述列表。通过指定该参数可以同时绑定标签到相应的实例。
        :type Tags: list of Tag
        :param _DisasterRecoverGroupIds: 分散置放群组ID列表，当前只支持指定一个。
该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/product/213/15486 ) 的返回值中的SecurityGroupId字段来获取。
        :type DisasterRecoverGroupIds: list of str
        :param _CbsEncrypt: 集群维度CBS加密盘，默认0表示不加密，1表示加密
        :type CbsEncrypt: int
        :param _MetaType: hive共享元数据库类型。取值范围：
<li>EMR_NEW_META：表示集群默认创建</li>
<li>EMR_EXIT_META：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>
        :type MetaType: str
        :param _UnifyMetaInstanceId: EMR-MetaDB实例
        :type UnifyMetaInstanceId: str
        :param _MetaDBInfo: 自定义MetaDB信息
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        :param _ApplicationRole: 自定义应用角色。
        :type ApplicationRole: str
        :param _SceneName: 场景化取值：
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
        :type SceneName: str
        :param _ExternalService: 共享组件信息
        :type ExternalService: list of ExternalService
        :param _VersionID: 如果为0，则MultiZone、MultiDeployStrategy、MultiZoneSettings是disable的状态，如果为1，则废弃ResourceSpec，使用MultiZoneSettings。
        :type VersionID: int
        :param _MultiZone: true表示开启跨AZ部署；仅为新建集群时的用户参数，后续不支持调整。
        :type MultiZone: bool
        :param _MultiZoneSettings: 节点资源的规格，有几个可用区，就填几个，按顺序第一个为主可用区，第二个为备可用区，第三个为仲裁可用区。如果没有开启跨AZ，则长度为1即可。
        :type MultiZoneSettings: list of MultiZoneSetting
        """
        self._ProductId = None
        self._Software = None
        self._SupportHA = None
        self._InstanceName = None
        self._PayMode = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._LoginSettings = None
        self._VPCSettings = None
        self._ResourceSpec = None
        self._COSSettings = None
        self._Placement = None
        self._SgId = None
        self._PreExecutedFileSettings = None
        self._AutoRenew = None
        self._ClientToken = None
        self._NeedMasterWan = None
        self._RemoteLoginAtCreate = None
        self._CheckSecurity = None
        self._ExtendFsField = None
        self._Tags = None
        self._DisasterRecoverGroupIds = None
        self._CbsEncrypt = None
        self._MetaType = None
        self._UnifyMetaInstanceId = None
        self._MetaDBInfo = None
        self._ApplicationRole = None
        self._SceneName = None
        self._ExternalService = None
        self._VersionID = None
        self._MultiZone = None
        self._MultiZoneSettings = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Software(self):
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def SupportHA(self):
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

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
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def VPCSettings(self):
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def ResourceSpec(self):
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def COSSettings(self):
        return self._COSSettings

    @COSSettings.setter
    def COSSettings(self, COSSettings):
        self._COSSettings = COSSettings

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def SgId(self):
        return self._SgId

    @SgId.setter
    def SgId(self, SgId):
        self._SgId = SgId

    @property
    def PreExecutedFileSettings(self):
        return self._PreExecutedFileSettings

    @PreExecutedFileSettings.setter
    def PreExecutedFileSettings(self, PreExecutedFileSettings):
        self._PreExecutedFileSettings = PreExecutedFileSettings

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def NeedMasterWan(self):
        return self._NeedMasterWan

    @NeedMasterWan.setter
    def NeedMasterWan(self, NeedMasterWan):
        self._NeedMasterWan = NeedMasterWan

    @property
    def RemoteLoginAtCreate(self):
        return self._RemoteLoginAtCreate

    @RemoteLoginAtCreate.setter
    def RemoteLoginAtCreate(self, RemoteLoginAtCreate):
        self._RemoteLoginAtCreate = RemoteLoginAtCreate

    @property
    def CheckSecurity(self):
        return self._CheckSecurity

    @CheckSecurity.setter
    def CheckSecurity(self, CheckSecurity):
        self._CheckSecurity = CheckSecurity

    @property
    def ExtendFsField(self):
        return self._ExtendFsField

    @ExtendFsField.setter
    def ExtendFsField(self, ExtendFsField):
        self._ExtendFsField = ExtendFsField

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def CbsEncrypt(self):
        return self._CbsEncrypt

    @CbsEncrypt.setter
    def CbsEncrypt(self, CbsEncrypt):
        self._CbsEncrypt = CbsEncrypt

    @property
    def MetaType(self):
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId

    @property
    def MetaDBInfo(self):
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo

    @property
    def ApplicationRole(self):
        return self._ApplicationRole

    @ApplicationRole.setter
    def ApplicationRole(self, ApplicationRole):
        self._ApplicationRole = ApplicationRole

    @property
    def SceneName(self):
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def ExternalService(self):
        return self._ExternalService

    @ExternalService.setter
    def ExternalService(self, ExternalService):
        self._ExternalService = ExternalService

    @property
    def VersionID(self):
        return self._VersionID

    @VersionID.setter
    def VersionID(self, VersionID):
        self._VersionID = VersionID

    @property
    def MultiZone(self):
        return self._MultiZone

    @MultiZone.setter
    def MultiZone(self, MultiZone):
        self._MultiZone = MultiZone

    @property
    def MultiZoneSettings(self):
        return self._MultiZoneSettings

    @MultiZoneSettings.setter
    def MultiZoneSettings(self, MultiZoneSettings):
        self._MultiZoneSettings = MultiZoneSettings


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Software = params.get("Software")
        self._SupportHA = params.get("SupportHA")
        self._InstanceName = params.get("InstanceName")
        self._PayMode = params.get("PayMode")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NewResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        if params.get("COSSettings") is not None:
            self._COSSettings = COSSettings()
            self._COSSettings._deserialize(params.get("COSSettings"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._SgId = params.get("SgId")
        if params.get("PreExecutedFileSettings") is not None:
            self._PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self._PreExecutedFileSettings.append(obj)
        self._AutoRenew = params.get("AutoRenew")
        self._ClientToken = params.get("ClientToken")
        self._NeedMasterWan = params.get("NeedMasterWan")
        self._RemoteLoginAtCreate = params.get("RemoteLoginAtCreate")
        self._CheckSecurity = params.get("CheckSecurity")
        self._ExtendFsField = params.get("ExtendFsField")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self._CbsEncrypt = params.get("CbsEncrypt")
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self._ApplicationRole = params.get("ApplicationRole")
        self._SceneName = params.get("SceneName")
        if params.get("ExternalService") is not None:
            self._ExternalService = []
            for item in params.get("ExternalService"):
                obj = ExternalService()
                obj._deserialize(item)
                self._ExternalService.append(obj)
        self._VersionID = params.get("VersionID")
        self._MultiZone = params.get("MultiZone")
        if params.get("MultiZoneSettings") is not None:
            self._MultiZoneSettings = []
            for item in params.get("MultiZoneSettings"):
                obj = MultiZoneSetting()
                obj._deserialize(item)
                self._MultiZoneSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CustomMetaDBInfo(AbstractModel):
    """用户Hive-MetaDB信息

    """

    def __init__(self):
        r"""
        :param _MetaDataJdbcUrl: 自定义MetaDB的JDBC连接，示例: jdbc:mysql://10.10.10.10:3306/dbname
        :type MetaDataJdbcUrl: str
        :param _MetaDataUser: 自定义MetaDB用户名
        :type MetaDataUser: str
        :param _MetaDataPass: 自定义MetaDB密码
        :type MetaDataPass: str
        :param _MetaType: hive共享元数据库类型。取值范围：
<li>EMR_DEFAULT_META：表示集群默认创建</li>
<li>EMR_EXIST_META：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>
        :type MetaType: str
        :param _UnifyMetaInstanceId: EMR-MetaDB实例
        :type UnifyMetaInstanceId: str
        """
        self._MetaDataJdbcUrl = None
        self._MetaDataUser = None
        self._MetaDataPass = None
        self._MetaType = None
        self._UnifyMetaInstanceId = None

    @property
    def MetaDataJdbcUrl(self):
        return self._MetaDataJdbcUrl

    @MetaDataJdbcUrl.setter
    def MetaDataJdbcUrl(self, MetaDataJdbcUrl):
        self._MetaDataJdbcUrl = MetaDataJdbcUrl

    @property
    def MetaDataUser(self):
        return self._MetaDataUser

    @MetaDataUser.setter
    def MetaDataUser(self, MetaDataUser):
        self._MetaDataUser = MetaDataUser

    @property
    def MetaDataPass(self):
        return self._MetaDataPass

    @MetaDataPass.setter
    def MetaDataPass(self, MetaDataPass):
        self._MetaDataPass = MetaDataPass

    @property
    def MetaType(self):
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId


    def _deserialize(self, params):
        self._MetaDataJdbcUrl = params.get("MetaDataJdbcUrl")
        self._MetaDataUser = params.get("MetaDataUser")
        self._MetaDataPass = params.get("MetaDataPass")
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomMetaInfo(AbstractModel):
    """用户自建Hive-MetaDB信息

    """

    def __init__(self):
        r"""
        :param _MetaDataJdbcUrl: 自定义MetaDB的JDBC连接，请以 jdbc:mysql:// 开头
        :type MetaDataJdbcUrl: str
        :param _MetaDataUser: 自定义MetaDB用户名
        :type MetaDataUser: str
        :param _MetaDataPass: 自定义MetaDB密码
        :type MetaDataPass: str
        """
        self._MetaDataJdbcUrl = None
        self._MetaDataUser = None
        self._MetaDataPass = None

    @property
    def MetaDataJdbcUrl(self):
        return self._MetaDataJdbcUrl

    @MetaDataJdbcUrl.setter
    def MetaDataJdbcUrl(self, MetaDataJdbcUrl):
        self._MetaDataJdbcUrl = MetaDataJdbcUrl

    @property
    def MetaDataUser(self):
        return self._MetaDataUser

    @MetaDataUser.setter
    def MetaDataUser(self, MetaDataUser):
        self._MetaDataUser = MetaDataUser

    @property
    def MetaDataPass(self):
        return self._MetaDataPass

    @MetaDataPass.setter
    def MetaDataPass(self, MetaDataPass):
        self._MetaDataPass = MetaDataPass


    def _deserialize(self, params):
        self._MetaDataJdbcUrl = params.get("MetaDataJdbcUrl")
        self._MetaDataUser = params.get("MetaDataUser")
        self._MetaDataPass = params.get("MetaDataPass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomServiceDefine(AbstractModel):
    """共用自建组件参数

    """

    def __init__(self):
        r"""
        :param _Name: 自定义参数key
        :type Name: str
        :param _Value: 自定义参数value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserManagerUserListRequest(AbstractModel):
    """DeleteUserManagerUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _UserNameList: 集群用户名列表
        :type UserNameList: list of str
        :param _TkeClusterId: tke/eks集群id，容器集群传
        :type TkeClusterId: str
        :param _DisplayStrategy: 默认空，容器版传"native"
        :type DisplayStrategy: str
        :param _UserGroupList: 用户组
        :type UserGroupList: list of UserAndGroup
        """
        self._InstanceId = None
        self._UserNameList = None
        self._TkeClusterId = None
        self._DisplayStrategy = None
        self._UserGroupList = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserNameList(self):
        return self._UserNameList

    @UserNameList.setter
    def UserNameList(self, UserNameList):
        self._UserNameList = UserNameList

    @property
    def TkeClusterId(self):
        return self._TkeClusterId

    @TkeClusterId.setter
    def TkeClusterId(self, TkeClusterId):
        self._TkeClusterId = TkeClusterId

    @property
    def DisplayStrategy(self):
        return self._DisplayStrategy

    @DisplayStrategy.setter
    def DisplayStrategy(self, DisplayStrategy):
        self._DisplayStrategy = DisplayStrategy

    @property
    def UserGroupList(self):
        return self._UserGroupList

    @UserGroupList.setter
    def UserGroupList(self, UserGroupList):
        self._UserGroupList = UserGroupList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserNameList = params.get("UserNameList")
        self._TkeClusterId = params.get("TkeClusterId")
        self._DisplayStrategy = params.get("DisplayStrategy")
        if params.get("UserGroupList") is not None:
            self._UserGroupList = []
            for item in params.get("UserGroupList"):
                obj = UserAndGroup()
                obj._deserialize(item)
                self._UserGroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserManagerUserListResponse(AbstractModel):
    """DeleteUserManagerUserList返回参数结构体

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


class DependService(AbstractModel):
    """共用组件信息

    """

    def __init__(self):
        r"""
        :param _ServiceName: 共用组件名
        :type ServiceName: str
        :param _InstanceId: 共用组件集群
        :type InstanceId: str
        """
        self._ServiceName = None
        self._InstanceId = None

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodesRequest(AbstractModel):
    """DescribeClusterNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID,实例ID形如: emr-xxxxxxxx
        :type InstanceId: str
        :param _NodeFlag: 节点标识，取值为：
<li>all：表示获取全部类型节点，cdb信息除外。</li>
<li>master：表示获取master节点信息。</li>
<li>core：表示获取core节点信息。</li>
<li>task：表示获取task节点信息。</li>
<li>common：表示获取common节点信息。</li>
<li>router：表示获取router节点信息。</li>
<li>db：表示获取正常状态的cdb信息。</li>
<li>recyle：表示获取回收站隔离中的节点信息，包括cdb信息。</li>
<li>renew：表示获取所有待续费的节点信息，包括cdb信息，自动续费节点不会返回。</li>
注意：现在只支持以上取值，输入其他值会导致错误。
        :type NodeFlag: str
        :param _Offset: 页编号，默认值为0，表示第一页。
        :type Offset: int
        :param _Limit: 每页返回数量，默认值为100，最大值为100。
        :type Limit: int
        :param _HardwareResourceType: 资源类型:支持all/host/pod，默认为all
        :type HardwareResourceType: str
        :param _SearchFields: 支持搜索的字段
        :type SearchFields: list of SearchItem
        :param _OrderField: 无
        :type OrderField: str
        :param _Asc: 无
        :type Asc: int
        """
        self._InstanceId = None
        self._NodeFlag = None
        self._Offset = None
        self._Limit = None
        self._HardwareResourceType = None
        self._SearchFields = None
        self._OrderField = None
        self._Asc = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeFlag(self):
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

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
    def HardwareResourceType(self):
        return self._HardwareResourceType

    @HardwareResourceType.setter
    def HardwareResourceType(self, HardwareResourceType):
        self._HardwareResourceType = HardwareResourceType

    @property
    def SearchFields(self):
        return self._SearchFields

    @SearchFields.setter
    def SearchFields(self, SearchFields):
        self._SearchFields = SearchFields

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeFlag = params.get("NodeFlag")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._HardwareResourceType = params.get("HardwareResourceType")
        if params.get("SearchFields") is not None:
            self._SearchFields = []
            for item in params.get("SearchFields"):
                obj = SearchItem()
                obj._deserialize(item)
                self._SearchFields.append(obj)
        self._OrderField = params.get("OrderField")
        self._Asc = params.get("Asc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodesResponse(AbstractModel):
    """DescribeClusterNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 查询到的节点总数
        :type TotalCnt: int
        :param _NodeList: 节点详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeList: list of NodeHardwareInfo
        :param _TagKeys: 用户所有的标签键列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKeys: list of str
        :param _HardwareResourceTypeList: 资源类型列表
注意：此字段可能返回 null，表示取不到有效值。
        :type HardwareResourceTypeList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._NodeList = None
        self._TagKeys = None
        self._HardwareResourceTypeList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def HardwareResourceTypeList(self):
        return self._HardwareResourceTypeList

    @HardwareResourceTypeList.setter
    def HardwareResourceTypeList(self, HardwareResourceTypeList):
        self._HardwareResourceTypeList = HardwareResourceTypeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = NodeHardwareInfo()
                obj._deserialize(item)
                self._NodeList.append(obj)
        self._TagKeys = params.get("TagKeys")
        self._HardwareResourceTypeList = params.get("HardwareResourceTypeList")
        self._RequestId = params.get("RequestId")


class DescribeCvmQuotaRequest(AbstractModel):
    """DescribeCvmQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: EMR集群ID
        :type ClusterId: str
        :param _ZoneId: 区ID
        :type ZoneId: int
        """
        self._ClusterId = None
        self._ZoneId = None

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
        self._ClusterId = params.get("ClusterId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCvmQuotaResponse(AbstractModel):
    """DescribeCvmQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PostPaidQuotaSet: 后付费配额列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PostPaidQuotaSet: list of QuotaEntity
        :param _SpotPaidQuotaSet: 竞价实例配额列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SpotPaidQuotaSet: list of QuotaEntity
        :param _EksQuotaSet: eks配额
注意：此字段可能返回 null，表示取不到有效值。
        :type EksQuotaSet: list of PodSaleSpec
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PostPaidQuotaSet = None
        self._SpotPaidQuotaSet = None
        self._EksQuotaSet = None
        self._RequestId = None

    @property
    def PostPaidQuotaSet(self):
        return self._PostPaidQuotaSet

    @PostPaidQuotaSet.setter
    def PostPaidQuotaSet(self, PostPaidQuotaSet):
        self._PostPaidQuotaSet = PostPaidQuotaSet

    @property
    def SpotPaidQuotaSet(self):
        return self._SpotPaidQuotaSet

    @SpotPaidQuotaSet.setter
    def SpotPaidQuotaSet(self, SpotPaidQuotaSet):
        self._SpotPaidQuotaSet = SpotPaidQuotaSet

    @property
    def EksQuotaSet(self):
        return self._EksQuotaSet

    @EksQuotaSet.setter
    def EksQuotaSet(self, EksQuotaSet):
        self._EksQuotaSet = EksQuotaSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PostPaidQuotaSet") is not None:
            self._PostPaidQuotaSet = []
            for item in params.get("PostPaidQuotaSet"):
                obj = QuotaEntity()
                obj._deserialize(item)
                self._PostPaidQuotaSet.append(obj)
        if params.get("SpotPaidQuotaSet") is not None:
            self._SpotPaidQuotaSet = []
            for item in params.get("SpotPaidQuotaSet"):
                obj = QuotaEntity()
                obj._deserialize(item)
                self._SpotPaidQuotaSet.append(obj)
        if params.get("EksQuotaSet") is not None:
            self._EksQuotaSet = []
            for item in params.get("EksQuotaSet"):
                obj = PodSaleSpec()
                obj._deserialize(item)
                self._EksQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEmrApplicationStaticsRequest(AbstractModel):
    """DescribeEmrApplicationStatics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _StartTime: 起始时间，时间戳（秒）
        :type StartTime: int
        :param _EndTime: 结束时间，时间戳（秒）
        :type EndTime: int
        :param _Queues: 过滤的队列名
        :type Queues: list of str
        :param _Users: 过滤的用户名
        :type Users: list of str
        :param _ApplicationTypes: 过滤的作业类型
        :type ApplicationTypes: list of str
        :param _GroupBy: 分组字段，可选：queue, user, applicationType
        :type GroupBy: list of str
        :param _OrderBy: 排序字段，可选：sumMemorySeconds, sumVCoreSeconds, sumHDFSBytesWritten, sumHDFSBytesRead
        :type OrderBy: str
        :param _IsAsc: 是否顺序排序，0-逆序，1-正序
        :type IsAsc: int
        :param _Offset: 页号
        :type Offset: int
        :param _Limit: 页容量
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Queues = None
        self._Users = None
        self._ApplicationTypes = None
        self._GroupBy = None
        self._OrderBy = None
        self._IsAsc = None
        self._Offset = None
        self._Limit = None

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

    @property
    def Queues(self):
        return self._Queues

    @Queues.setter
    def Queues(self, Queues):
        self._Queues = Queues

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def ApplicationTypes(self):
        return self._ApplicationTypes

    @ApplicationTypes.setter
    def ApplicationTypes(self, ApplicationTypes):
        self._ApplicationTypes = ApplicationTypes

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def IsAsc(self):
        return self._IsAsc

    @IsAsc.setter
    def IsAsc(self, IsAsc):
        self._IsAsc = IsAsc

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Queues = params.get("Queues")
        self._Users = params.get("Users")
        self._ApplicationTypes = params.get("ApplicationTypes")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._IsAsc = params.get("IsAsc")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEmrApplicationStaticsResponse(AbstractModel):
    """DescribeEmrApplicationStatics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Statics: 作业统计信息
        :type Statics: list of ApplicationStatics
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Queues: 可选择的队列名
        :type Queues: list of str
        :param _Users: 可选择的用户名
        :type Users: list of str
        :param _ApplicationTypes: 可选择的作业类型
        :type ApplicationTypes: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Statics = None
        self._TotalCount = None
        self._Queues = None
        self._Users = None
        self._ApplicationTypes = None
        self._RequestId = None

    @property
    def Statics(self):
        return self._Statics

    @Statics.setter
    def Statics(self, Statics):
        self._Statics = Statics

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Queues(self):
        return self._Queues

    @Queues.setter
    def Queues(self, Queues):
        self._Queues = Queues

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def ApplicationTypes(self):
        return self._ApplicationTypes

    @ApplicationTypes.setter
    def ApplicationTypes(self, ApplicationTypes):
        self._ApplicationTypes = ApplicationTypes

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Statics") is not None:
            self._Statics = []
            for item in params.get("Statics"):
                obj = ApplicationStatics()
                obj._deserialize(item)
                self._Statics.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Queues = params.get("Queues")
        self._Users = params.get("Users")
        self._ApplicationTypes = params.get("ApplicationTypes")
        self._RequestId = params.get("RequestId")


class DescribeHiveQueriesRequest(AbstractModel):
    """DescribeHiveQueries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 起始时间秒
        :type StartTime: int
        :param _EndTime: 结束时间秒，EndTime-StartTime不得超过1天秒数86400
        :type EndTime: int
        :param _Offset: 分页起始偏移，从0开始
        :type Offset: int
        :param _Limit: 分页大小，合法范围[1,100]
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHiveQueriesResponse(AbstractModel):
    """DescribeHiveQueries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总条数
        :type Total: int
        :param _Results: 结果列表
        :type Results: list of HiveQuery
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = HiveQuery()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImpalaQueriesRequest(AbstractModel):
    """DescribeImpalaQueries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 起始时间秒
        :type StartTime: int
        :param _EndTime: 结束时间秒，EndTime-StartTime不得超过1天秒数86400
        :type EndTime: int
        :param _Offset: 分页起始偏移，从0开始
        :type Offset: int
        :param _Limit: 分页大小，合法范围[1,100]
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImpalaQueriesResponse(AbstractModel):
    """DescribeImpalaQueries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Results: 结果列表
        :type Results: list of ImpalaQuery
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ImpalaQuery()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRenewNodesRequest(AbstractModel):
    """DescribeInstanceRenewNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID,实例ID形如: emr-xxxxxxxx
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
        


class DescribeInstanceRenewNodesResponse(AbstractModel):
    """DescribeInstanceRenewNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 查询到的节点总数
        :type TotalCnt: int
        :param _NodeList: 节点详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeList: list of RenewInstancesInfo
        :param _MetaInfo: 用户所有的标签键列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaInfo: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._NodeList = None
        self._MetaInfo = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def MetaInfo(self):
        return self._MetaInfo

    @MetaInfo.setter
    def MetaInfo(self, MetaInfo):
        self._MetaInfo = MetaInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = RenewInstancesInfo()
                obj._deserialize(item)
                self._NodeList.append(obj)
        self._MetaInfo = params.get("MetaInfo")
        self._RequestId = params.get("RequestId")


class DescribeInstancesListRequest(AbstractModel):
    """DescribeInstancesList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayStrategy: 集群筛选策略。取值范围：<li>clusterList：表示查询除了已销毁集群之外的集群列表。</li><li>monitorManage：表示查询除了已销毁、创建中以及创建失败的集群之外的集群列表。</li><li>cloudHardwareManage/componentManage：目前这两个取值为预留取值，暂时和monitorManage表示同样的含义。</li>
        :type DisplayStrategy: str
        :param _Offset: 页编号，默认值为0，表示第一页。
        :type Offset: int
        :param _Limit: 每页返回数量，默认值为10，最大值为100。
        :type Limit: int
        :param _OrderField: 排序字段。取值范围：<li>clusterId：表示按照实例ID排序。</li><li>addTime：表示按照实例创建时间排序。</li><li>status：表示按照实例的状态码排序。</li>
        :type OrderField: str
        :param _Asc: 按照OrderField升序或者降序进行排序。取值范围：<li>0：表示降序。</li><li>1：表示升序。</li>默认值为0。
        :type Asc: int
        :param _Filters: 自定义查询
        :type Filters: list of Filters
        """
        self._DisplayStrategy = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Asc = None
        self._Filters = None

    @property
    def DisplayStrategy(self):
        return self._DisplayStrategy

    @DisplayStrategy.setter
    def DisplayStrategy(self, DisplayStrategy):
        self._DisplayStrategy = DisplayStrategy

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
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DisplayStrategy = params.get("DisplayStrategy")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Asc = params.get("Asc")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesListResponse(AbstractModel):
    """DescribeInstancesList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 符合条件的实例总数。
        :type TotalCnt: int
        :param _InstancesList: 集群实例列表
        :type InstancesList: list of EmrListInstance
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._InstancesList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def InstancesList(self):
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = EmrListInstance()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DisplayStrategy: 集群筛选策略。取值范围：
<li>clusterList：表示查询除了已销毁集群之外的集群列表。</li>
<li>monitorManage：表示查询除了已销毁、创建中以及创建失败的集群之外的集群列表。</li>
<li>cloudHardwareManage/componentManage：目前这两个取值为预留取值，暂时和monitorManage表示同样的含义。</li>
        :type DisplayStrategy: str
        :param _InstanceIds: 按照一个或者多个实例ID查询。实例ID形如: emr-xxxxxxxx 。(此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的 Ids.N 一节)。如果不填写实例ID，返回该APPID下所有实例列表。
        :type InstanceIds: list of str
        :param _Offset: 页编号，默认值为0，表示第一页。
        :type Offset: int
        :param _Limit: 每页返回数量，默认值为10，最大值为100。
        :type Limit: int
        :param _ProjectId: 建议必填-1，表示拉取所有项目下的集群。
不填默认值为0，表示拉取默认项目下的集群。
实例所属项目ID。该参数可以通过调用 [DescribeProjects](https://cloud.tencent.com/document/product/651/78725) 的返回值中的 projectId 字段来获取。
        :type ProjectId: int
        :param _OrderField: 排序字段。取值范围：
<li>clusterId：表示按照实例ID排序。</li>
<li>addTime：表示按照实例创建时间排序。</li>
<li>status：表示按照实例的状态码排序。</li>
        :type OrderField: str
        :param _Asc: 按照OrderField升序或者降序进行排序。取值范围：
<li>0：表示降序。</li>
<li>1：表示升序。</li>默认值为0。
        :type Asc: int
        """
        self._DisplayStrategy = None
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None
        self._ProjectId = None
        self._OrderField = None
        self._Asc = None

    @property
    def DisplayStrategy(self):
        return self._DisplayStrategy

    @DisplayStrategy.setter
    def DisplayStrategy(self, DisplayStrategy):
        self._DisplayStrategy = DisplayStrategy

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Asc(self):
        return self._Asc

    @Asc.setter
    def Asc(self, Asc):
        self._Asc = Asc


    def _deserialize(self, params):
        self._DisplayStrategy = params.get("DisplayStrategy")
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProjectId = params.get("ProjectId")
        self._OrderField = params.get("OrderField")
        self._Asc = params.get("Asc")
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
        :param _TotalCnt: 符合条件的实例总数。
        :type TotalCnt: int
        :param _ClusterList: EMR实例详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterList: list of ClusterInstancesInfo
        :param _TagKeys: 实例关联的标签键列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKeys: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._ClusterList = None
        self._TagKeys = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def ClusterList(self):
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = ClusterInstancesInfo()
                obj._deserialize(item)
                self._ClusterList.append(obj)
        self._TagKeys = params.get("TagKeys")
        self._RequestId = params.get("RequestId")


class DescribeJobFlowRequest(AbstractModel):
    """DescribeJobFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobFlowId: 流程任务Id，RunJobFlow接口返回的值。
        :type JobFlowId: int
        """
        self._JobFlowId = None

    @property
    def JobFlowId(self):
        return self._JobFlowId

    @JobFlowId.setter
    def JobFlowId(self, JobFlowId):
        self._JobFlowId = JobFlowId


    def _deserialize(self, params):
        self._JobFlowId = params.get("JobFlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobFlowResponse(AbstractModel):
    """DescribeJobFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _State: 流程任务状态，可以为以下值：
JobFlowInit，流程任务初始化。
JobFlowResourceApplied，资源申请中，通常为JobFlow需要新建集群时的状态。
JobFlowResourceReady，执行流程任务的资源就绪。
JobFlowStepsRunning，流程任务步骤已提交。
JobFlowStepsComplete，流程任务步骤已完成。
JobFlowTerminating，流程任务所需资源销毁中。
JobFlowFinish，流程任务已完成。
        :type State: str
        :param _Details: 流程任务步骤结果。
        :type Details: list of JobResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._State = None
        self._Details = None
        self._RequestId = None

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._State = params.get("State")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = JobResult()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceScheduleRequest(AbstractModel):
    """DescribeResourceSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
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
        


class DescribeResourceScheduleResponse(AbstractModel):
    """DescribeResourceSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OpenSwitch: 资源调度功能是否开启
        :type OpenSwitch: bool
        :param _Scheduler: 正在使用的资源调度器
        :type Scheduler: str
        :param _FSInfo: 公平调度器的信息
        :type FSInfo: str
        :param _CSInfo: 容量调度器的信息
        :type CSInfo: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OpenSwitch = None
        self._Scheduler = None
        self._FSInfo = None
        self._CSInfo = None
        self._RequestId = None

    @property
    def OpenSwitch(self):
        return self._OpenSwitch

    @OpenSwitch.setter
    def OpenSwitch(self, OpenSwitch):
        self._OpenSwitch = OpenSwitch

    @property
    def Scheduler(self):
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def FSInfo(self):
        return self._FSInfo

    @FSInfo.setter
    def FSInfo(self, FSInfo):
        self._FSInfo = FSInfo

    @property
    def CSInfo(self):
        return self._CSInfo

    @CSInfo.setter
    def CSInfo(self, CSInfo):
        self._CSInfo = CSInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OpenSwitch = params.get("OpenSwitch")
        self._Scheduler = params.get("Scheduler")
        self._FSInfo = params.get("FSInfo")
        self._CSInfo = params.get("CSInfo")
        self._RequestId = params.get("RequestId")


class DescribeUsersForUserManagerRequest(AbstractModel):
    """DescribeUsersForUserManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 分页的大小
        :type PageSize: int
        :param _UserManagerFilter: 查询用户列表过滤器
        :type UserManagerFilter: :class:`tencentcloud.emr.v20190103.models.UserManagerFilter`
        :param _NeedKeytabInfo: 是否需要keytab文件的信息，仅对开启kerberos的集群有效，默认为false
        :type NeedKeytabInfo: bool
        """
        self._InstanceId = None
        self._PageNo = None
        self._PageSize = None
        self._UserManagerFilter = None
        self._NeedKeytabInfo = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def UserManagerFilter(self):
        return self._UserManagerFilter

    @UserManagerFilter.setter
    def UserManagerFilter(self, UserManagerFilter):
        self._UserManagerFilter = UserManagerFilter

    @property
    def NeedKeytabInfo(self):
        return self._NeedKeytabInfo

    @NeedKeytabInfo.setter
    def NeedKeytabInfo(self, NeedKeytabInfo):
        self._NeedKeytabInfo = NeedKeytabInfo


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        if params.get("UserManagerFilter") is not None:
            self._UserManagerFilter = UserManagerFilter()
            self._UserManagerFilter._deserialize(params.get("UserManagerFilter"))
        self._NeedKeytabInfo = params.get("NeedKeytabInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersForUserManagerResponse(AbstractModel):
    """DescribeUsersForUserManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCnt: 总数
        :type TotalCnt: int
        :param _UserManagerUserList: 用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserManagerUserList: list of UserManagerUserBriefInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCnt = None
        self._UserManagerUserList = None
        self._RequestId = None

    @property
    def TotalCnt(self):
        return self._TotalCnt

    @TotalCnt.setter
    def TotalCnt(self, TotalCnt):
        self._TotalCnt = TotalCnt

    @property
    def UserManagerUserList(self):
        return self._UserManagerUserList

    @UserManagerUserList.setter
    def UserManagerUserList(self, UserManagerUserList):
        self._UserManagerUserList = UserManagerUserList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCnt = params.get("TotalCnt")
        if params.get("UserManagerUserList") is not None:
            self._UserManagerUserList = []
            for item in params.get("UserManagerUserList"):
                obj = UserManagerUserBriefInfo()
                obj._deserialize(item)
                self._UserManagerUserList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeYarnApplicationsRequest(AbstractModel):
    """DescribeYarnApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _StartTime: 起始时间秒
        :type StartTime: int
        :param _EndTime: 结束时间秒，EndTime-StartTime不得超过1天秒数86400
        :type EndTime: int
        :param _Offset: 分页起始偏移，从0开始
        :type Offset: int
        :param _Limit: 分页大小，合法范围[1,100]
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeYarnApplicationsResponse(AbstractModel):
    """DescribeYarnApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Results: 结果列表
        :type Results: list of YarnApplication
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = YarnApplication()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DiskGroup(AbstractModel):
    """磁盘组。

    """

    def __init__(self):
        r"""
        :param _Spec: 磁盘规格。
        :type Spec: :class:`tencentcloud.emr.v20190103.models.DiskSpec`
        :param _Count: 同类型磁盘数量。
        :type Count: int
        """
        self._Spec = None
        self._Count = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        if params.get("Spec") is not None:
            self._Spec = DiskSpec()
            self._Spec._deserialize(params.get("Spec"))
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskSpec(AbstractModel):
    """磁盘描述。

    """

    def __init__(self):
        r"""
        :param _DiskType: 磁盘类型。
LOCAL_BASIC  本地盘。
CLOUD_BASIC 云硬盘。
LOCAL_SSD 本地SSD。
CLOUD_SSD 云SSD。
CLOUD_PREMIUM 高效云盘。
CLOUD_HSSD 增强型云SSD。
        :type DiskType: str
        :param _DiskSize: 磁盘大小，单位GB。
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskSpecInfo(AbstractModel):
    """节点磁盘信息

    """

    def __init__(self):
        r"""
        :param _Count: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _DiskType: 系统盘类型 取值范围：
<li>CLOUD_SSD：表示云SSD。</li>
<li>CLOUD_PREMIUM：表示高效云盘。</li>
<li>CLOUD_BASIC：表示云硬盘。</li>
<li>LOCAL_BASIC：表示本地盘。</li>
<li>LOCAL_SSD：表示本地SSD。</li>

数据盘类型 取值范围：
<li>CLOUD_SSD：表示云SSD。</li>
<li>CLOUD_PREMIUM：表示高效云盘。</li>
<li>CLOUD_BASIC：表示云硬盘。</li>
<li>LOCAL_BASIC：表示本地盘。</li>
<li>LOCAL_SSD：表示本地SSD。</li>
<li>CLOUD_HSSD：表示增强型SSD云硬盘。</li>
<li>CLOUD_THROUGHPUT：表示吞吐型云硬盘。</li>
<li>CLOUD_TSSD：表示极速型SSD云硬盘。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskSize: 数据容量，单位为GB
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        """
        self._Count = None
        self._DiskType = None
        self._DiskSize = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicPodSpec(AbstractModel):
    """POD浮动规格

    """

    def __init__(self):
        r"""
        :param _RequestCpu: 需求最小cpu核数
        :type RequestCpu: float
        :param _LimitCpu: 需求最大cpu核数
        :type LimitCpu: float
        :param _RequestMemory: 需求最小memory，单位MB
        :type RequestMemory: float
        :param _LimitMemory: 需求最大memory，单位MB
        :type LimitMemory: float
        """
        self._RequestCpu = None
        self._LimitCpu = None
        self._RequestMemory = None
        self._LimitMemory = None

    @property
    def RequestCpu(self):
        return self._RequestCpu

    @RequestCpu.setter
    def RequestCpu(self, RequestCpu):
        self._RequestCpu = RequestCpu

    @property
    def LimitCpu(self):
        return self._LimitCpu

    @LimitCpu.setter
    def LimitCpu(self, LimitCpu):
        self._LimitCpu = LimitCpu

    @property
    def RequestMemory(self):
        return self._RequestMemory

    @RequestMemory.setter
    def RequestMemory(self, RequestMemory):
        self._RequestMemory = RequestMemory

    @property
    def LimitMemory(self):
        return self._LimitMemory

    @LimitMemory.setter
    def LimitMemory(self, LimitMemory):
        self._LimitMemory = LimitMemory


    def _deserialize(self, params):
        self._RequestCpu = params.get("RequestCpu")
        self._LimitCpu = params.get("LimitCpu")
        self._RequestMemory = params.get("RequestMemory")
        self._LimitMemory = params.get("LimitMemory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrListInstance(AbstractModel):
    """集群列表返回示例

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _StatusDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _ClusterName: 集群名字
        :type ClusterName: str
        :param _ZoneId: 集群地域
        :type ZoneId: int
        :param _AppId: 用户APPID
        :type AppId: int
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _RunTime: 运行时间
        :type RunTime: str
        :param _MasterIp: 集群IP
        :type MasterIp: str
        :param _EmrVersion: 集群版本
        :type EmrVersion: str
        :param _ChargeType: 集群计费类型
        :type ChargeType: int
        :param _Id: emr ID
        :type Id: int
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: int
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _RegionId: 区域
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: int
        :param _VpcId: 网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param _Zone: 地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _Status: 状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Tags: 实例标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _AlarmInfo: 告警信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmInfo: str
        :param _IsWoodpeckerCluster: 是否是woodpecker集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWoodpeckerCluster: int
        :param _VpcName: Vpc中文
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param _SubnetName: 子网中文
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param _UniqVpcId: 字符串VpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _UniqSubnetId: 字符串子网
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param _ClusterClass: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterClass: str
        :param _IsMultiZoneCluster: 是否为跨AZ集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMultiZoneCluster: bool
        :param _IsHandsCluster: 是否手戳集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsHandsCluster: bool
        :param _OutSideSoftInfo: 体外客户端组件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OutSideSoftInfo: list of SoftDependInfo
        :param _IsSupportOutsideCluster: 当前集群的应用场景是否支持体外客户端
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportOutsideCluster: bool
        """
        self._ClusterId = None
        self._StatusDesc = None
        self._ClusterName = None
        self._ZoneId = None
        self._AppId = None
        self._AddTime = None
        self._RunTime = None
        self._MasterIp = None
        self._EmrVersion = None
        self._ChargeType = None
        self._Id = None
        self._ProductId = None
        self._ProjectId = None
        self._RegionId = None
        self._SubnetId = None
        self._VpcId = None
        self._Zone = None
        self._Status = None
        self._Tags = None
        self._AlarmInfo = None
        self._IsWoodpeckerCluster = None
        self._VpcName = None
        self._SubnetName = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._ClusterClass = None
        self._IsMultiZoneCluster = None
        self._IsHandsCluster = None
        self._OutSideSoftInfo = None
        self._IsSupportOutsideCluster = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def RunTime(self):
        return self._RunTime

    @RunTime.setter
    def RunTime(self, RunTime):
        self._RunTime = RunTime

    @property
    def MasterIp(self):
        return self._MasterIp

    @MasterIp.setter
    def MasterIp(self, MasterIp):
        self._MasterIp = MasterIp

    @property
    def EmrVersion(self):
        return self._EmrVersion

    @EmrVersion.setter
    def EmrVersion(self, EmrVersion):
        self._EmrVersion = EmrVersion

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AlarmInfo(self):
        return self._AlarmInfo

    @AlarmInfo.setter
    def AlarmInfo(self, AlarmInfo):
        self._AlarmInfo = AlarmInfo

    @property
    def IsWoodpeckerCluster(self):
        return self._IsWoodpeckerCluster

    @IsWoodpeckerCluster.setter
    def IsWoodpeckerCluster(self, IsWoodpeckerCluster):
        self._IsWoodpeckerCluster = IsWoodpeckerCluster

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

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
    def ClusterClass(self):
        return self._ClusterClass

    @ClusterClass.setter
    def ClusterClass(self, ClusterClass):
        self._ClusterClass = ClusterClass

    @property
    def IsMultiZoneCluster(self):
        return self._IsMultiZoneCluster

    @IsMultiZoneCluster.setter
    def IsMultiZoneCluster(self, IsMultiZoneCluster):
        self._IsMultiZoneCluster = IsMultiZoneCluster

    @property
    def IsHandsCluster(self):
        return self._IsHandsCluster

    @IsHandsCluster.setter
    def IsHandsCluster(self, IsHandsCluster):
        self._IsHandsCluster = IsHandsCluster

    @property
    def OutSideSoftInfo(self):
        return self._OutSideSoftInfo

    @OutSideSoftInfo.setter
    def OutSideSoftInfo(self, OutSideSoftInfo):
        self._OutSideSoftInfo = OutSideSoftInfo

    @property
    def IsSupportOutsideCluster(self):
        return self._IsSupportOutsideCluster

    @IsSupportOutsideCluster.setter
    def IsSupportOutsideCluster(self, IsSupportOutsideCluster):
        self._IsSupportOutsideCluster = IsSupportOutsideCluster


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._StatusDesc = params.get("StatusDesc")
        self._ClusterName = params.get("ClusterName")
        self._ZoneId = params.get("ZoneId")
        self._AppId = params.get("AppId")
        self._AddTime = params.get("AddTime")
        self._RunTime = params.get("RunTime")
        self._MasterIp = params.get("MasterIp")
        self._EmrVersion = params.get("EmrVersion")
        self._ChargeType = params.get("ChargeType")
        self._Id = params.get("Id")
        self._ProductId = params.get("ProductId")
        self._ProjectId = params.get("ProjectId")
        self._RegionId = params.get("RegionId")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AlarmInfo = params.get("AlarmInfo")
        self._IsWoodpeckerCluster = params.get("IsWoodpeckerCluster")
        self._VpcName = params.get("VpcName")
        self._SubnetName = params.get("SubnetName")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._ClusterClass = params.get("ClusterClass")
        self._IsMultiZoneCluster = params.get("IsMultiZoneCluster")
        self._IsHandsCluster = params.get("IsHandsCluster")
        if params.get("OutSideSoftInfo") is not None:
            self._OutSideSoftInfo = []
            for item in params.get("OutSideSoftInfo"):
                obj = SoftDependInfo()
                obj._deserialize(item)
                self._OutSideSoftInfo.append(obj)
        self._IsSupportOutsideCluster = params.get("IsSupportOutsideCluster")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrPrice(AbstractModel):
    """Emr询价描述

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 刊例价格
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: str
        :param _DiscountCost: 折扣价格
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: str
        :param _Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _PriceSpec: 询价配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceSpec: :class:`tencentcloud.emr.v20190103.models.PriceResource`
        :param _SupportSpotPaid: 是否支持竞价实例
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportSpotPaid: bool
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._Unit = None
        self._PriceSpec = None
        self._SupportSpotPaid = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def PriceSpec(self):
        return self._PriceSpec

    @PriceSpec.setter
    def PriceSpec(self, PriceSpec):
        self._PriceSpec = PriceSpec

    @property
    def SupportSpotPaid(self):
        return self._SupportSpotPaid

    @SupportSpotPaid.setter
    def SupportSpotPaid(self, SupportSpotPaid):
        self._SupportSpotPaid = SupportSpotPaid


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._Unit = params.get("Unit")
        if params.get("PriceSpec") is not None:
            self._PriceSpec = PriceResource()
            self._PriceSpec._deserialize(params.get("PriceSpec"))
        self._SupportSpotPaid = params.get("SupportSpotPaid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrProductConfigOutter(AbstractModel):
    """EMR产品配置

    """

    def __init__(self):
        r"""
        :param _SoftInfo: 软件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftInfo: list of str
        :param _MasterNodeSize: Master节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterNodeSize: int
        :param _CoreNodeSize: Core节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreNodeSize: int
        :param _TaskNodeSize: Task节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNodeSize: int
        :param _ComNodeSize: Common节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ComNodeSize: int
        :param _MasterResource: Master节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _CoreResource: Core节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _TaskResource: Task节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _ComResource: Common节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type ComResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param _OnCos: 是否使用COS
注意：此字段可能返回 null，表示取不到有效值。
        :type OnCos: bool
        :param _ChargeType: 收费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param _RouterNodeSize: Router节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RouterNodeSize: int
        :param _SupportHA: 是否支持HA
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportHA: bool
        :param _SecurityOn: 是否支持安全模式
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityOn: bool
        :param _SecurityGroup: 安全组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroup: str
        :param _CbsEncrypt: 是否开启Cbs加密
注意：此字段可能返回 null，表示取不到有效值。
        :type CbsEncrypt: int
        :param _ApplicationRole: 自定义应用角色。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationRole: str
        :param _SecurityGroups: 安全组
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroups: list of str
        :param _PublicKeyId: SSH密钥Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicKeyId: str
        """
        self._SoftInfo = None
        self._MasterNodeSize = None
        self._CoreNodeSize = None
        self._TaskNodeSize = None
        self._ComNodeSize = None
        self._MasterResource = None
        self._CoreResource = None
        self._TaskResource = None
        self._ComResource = None
        self._OnCos = None
        self._ChargeType = None
        self._RouterNodeSize = None
        self._SupportHA = None
        self._SecurityOn = None
        self._SecurityGroup = None
        self._CbsEncrypt = None
        self._ApplicationRole = None
        self._SecurityGroups = None
        self._PublicKeyId = None

    @property
    def SoftInfo(self):
        return self._SoftInfo

    @SoftInfo.setter
    def SoftInfo(self, SoftInfo):
        self._SoftInfo = SoftInfo

    @property
    def MasterNodeSize(self):
        return self._MasterNodeSize

    @MasterNodeSize.setter
    def MasterNodeSize(self, MasterNodeSize):
        self._MasterNodeSize = MasterNodeSize

    @property
    def CoreNodeSize(self):
        return self._CoreNodeSize

    @CoreNodeSize.setter
    def CoreNodeSize(self, CoreNodeSize):
        self._CoreNodeSize = CoreNodeSize

    @property
    def TaskNodeSize(self):
        return self._TaskNodeSize

    @TaskNodeSize.setter
    def TaskNodeSize(self, TaskNodeSize):
        self._TaskNodeSize = TaskNodeSize

    @property
    def ComNodeSize(self):
        return self._ComNodeSize

    @ComNodeSize.setter
    def ComNodeSize(self, ComNodeSize):
        self._ComNodeSize = ComNodeSize

    @property
    def MasterResource(self):
        return self._MasterResource

    @MasterResource.setter
    def MasterResource(self, MasterResource):
        self._MasterResource = MasterResource

    @property
    def CoreResource(self):
        return self._CoreResource

    @CoreResource.setter
    def CoreResource(self, CoreResource):
        self._CoreResource = CoreResource

    @property
    def TaskResource(self):
        return self._TaskResource

    @TaskResource.setter
    def TaskResource(self, TaskResource):
        self._TaskResource = TaskResource

    @property
    def ComResource(self):
        return self._ComResource

    @ComResource.setter
    def ComResource(self, ComResource):
        self._ComResource = ComResource

    @property
    def OnCos(self):
        return self._OnCos

    @OnCos.setter
    def OnCos(self, OnCos):
        self._OnCos = OnCos

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def RouterNodeSize(self):
        return self._RouterNodeSize

    @RouterNodeSize.setter
    def RouterNodeSize(self, RouterNodeSize):
        self._RouterNodeSize = RouterNodeSize

    @property
    def SupportHA(self):
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def SecurityOn(self):
        return self._SecurityOn

    @SecurityOn.setter
    def SecurityOn(self, SecurityOn):
        self._SecurityOn = SecurityOn

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def CbsEncrypt(self):
        return self._CbsEncrypt

    @CbsEncrypt.setter
    def CbsEncrypt(self, CbsEncrypt):
        self._CbsEncrypt = CbsEncrypt

    @property
    def ApplicationRole(self):
        return self._ApplicationRole

    @ApplicationRole.setter
    def ApplicationRole(self, ApplicationRole):
        self._ApplicationRole = ApplicationRole

    @property
    def SecurityGroups(self):
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def PublicKeyId(self):
        return self._PublicKeyId

    @PublicKeyId.setter
    def PublicKeyId(self, PublicKeyId):
        self._PublicKeyId = PublicKeyId


    def _deserialize(self, params):
        self._SoftInfo = params.get("SoftInfo")
        self._MasterNodeSize = params.get("MasterNodeSize")
        self._CoreNodeSize = params.get("CoreNodeSize")
        self._TaskNodeSize = params.get("TaskNodeSize")
        self._ComNodeSize = params.get("ComNodeSize")
        if params.get("MasterResource") is not None:
            self._MasterResource = OutterResource()
            self._MasterResource._deserialize(params.get("MasterResource"))
        if params.get("CoreResource") is not None:
            self._CoreResource = OutterResource()
            self._CoreResource._deserialize(params.get("CoreResource"))
        if params.get("TaskResource") is not None:
            self._TaskResource = OutterResource()
            self._TaskResource._deserialize(params.get("TaskResource"))
        if params.get("ComResource") is not None:
            self._ComResource = OutterResource()
            self._ComResource._deserialize(params.get("ComResource"))
        self._OnCos = params.get("OnCos")
        self._ChargeType = params.get("ChargeType")
        self._RouterNodeSize = params.get("RouterNodeSize")
        self._SupportHA = params.get("SupportHA")
        self._SecurityOn = params.get("SecurityOn")
        self._SecurityGroup = params.get("SecurityGroup")
        self._CbsEncrypt = params.get("CbsEncrypt")
        self._ApplicationRole = params.get("ApplicationRole")
        self._SecurityGroups = params.get("SecurityGroups")
        self._PublicKeyId = params.get("PublicKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Execution(AbstractModel):
    """执行动作。

    """

    def __init__(self):
        r"""
        :param _JobType: 任务类型，目前支持以下类型。
1. “MR”，将通过hadoop jar的方式提交。
2. "HIVE"，将通过hive -f的方式提交。
3. "SPARK"，将通过spark-submit的方式提交。
        :type JobType: str
        :param _Args: 任务参数，提供除提交指令以外的参数。
        :type Args: list of str
        """
        self._JobType = None
        self._Args = None

    @property
    def JobType(self):
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args


    def _deserialize(self, params):
        self._JobType = params.get("JobType")
        self._Args = params.get("Args")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalService(AbstractModel):
    """共用组件信息

    """

    def __init__(self):
        r"""
        :param _ShareType: 共用组件类型，EMR/CUSTOM
        :type ShareType: str
        :param _CustomServiceDefineList: 自定义参数集合
        :type CustomServiceDefineList: list of CustomServiceDefine
        :param _Service: 共用组件名
        :type Service: str
        :param _InstanceId: 共用组件集群
        :type InstanceId: str
        """
        self._ShareType = None
        self._CustomServiceDefineList = None
        self._Service = None
        self._InstanceId = None

    @property
    def ShareType(self):
        return self._ShareType

    @ShareType.setter
    def ShareType(self, ShareType):
        self._ShareType = ShareType

    @property
    def CustomServiceDefineList(self):
        return self._CustomServiceDefineList

    @CustomServiceDefineList.setter
    def CustomServiceDefineList(self, CustomServiceDefineList):
        self._CustomServiceDefineList = CustomServiceDefineList

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ShareType = params.get("ShareType")
        if params.get("CustomServiceDefineList") is not None:
            self._CustomServiceDefineList = []
            for item in params.get("CustomServiceDefineList"):
                obj = CustomServiceDefine()
                obj._deserialize(item)
                self._CustomServiceDefineList.append(obj)
        self._Service = params.get("Service")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """Emr集群列表实例自定义查询过滤

    """

    def __init__(self):
        r"""
        :param _Name: 字段名称
        :type Name: str
        :param _Values: 过滤字段值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

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


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HiveQuery(AbstractModel):
    """Hive查询详情

    """

    def __init__(self):
        r"""
        :param _Statement: 查询语句
注意：此字段可能返回 null，表示取不到有效值。
        :type Statement: str
        :param _Duration: 执行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _StartTime: 开始时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _EndTime: 结束时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _User: 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _JobIds: appId列表
注意：此字段可能返回 null，表示取不到有效值。
        :type JobIds: list of str
        :param _ExecutionEngine: 执行引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecutionEngine: str
        :param _Id: 查询ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        """
        self._Statement = None
        self._Duration = None
        self._StartTime = None
        self._EndTime = None
        self._State = None
        self._User = None
        self._JobIds = None
        self._ExecutionEngine = None
        self._Id = None

    @property
    def Statement(self):
        return self._Statement

    @Statement.setter
    def Statement(self, Statement):
        self._Statement = Statement

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

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
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def ExecutionEngine(self):
        return self._ExecutionEngine

    @ExecutionEngine.setter
    def ExecutionEngine(self, ExecutionEngine):
        self._ExecutionEngine = ExecutionEngine

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Statement = params.get("Statement")
        self._Duration = params.get("Duration")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._State = params.get("State")
        self._User = params.get("User")
        self._JobIds = params.get("JobIds")
        self._ExecutionEngine = params.get("ExecutionEngine")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostVolumeContext(AbstractModel):
    """Pod HostPath挂载方式描述

    """

    def __init__(self):
        r"""
        :param _VolumePath: Pod挂载宿主机的目录。资源对宿主机的挂载点，指定的挂载点对应了宿主机的路径，该挂载点在Pod中作为数据存储目录使用
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumePath: str
        """
        self._VolumePath = None

    @property
    def VolumePath(self):
        return self._VolumePath

    @VolumePath.setter
    def VolumePath(self, VolumePath):
        self._VolumePath = VolumePath


    def _deserialize(self, params):
        self._VolumePath = params.get("VolumePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImpalaQuery(AbstractModel):
    """Impala查询详情

    """

    def __init__(self):
        r"""
        :param _Statement: 执行语句
注意：此字段可能返回 null，表示取不到有效值。
        :type Statement: str
        :param _Id: 查询ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _Duration: 运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _State: 执行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _RowsFetched: 获取行数
注意：此字段可能返回 null，表示取不到有效值。
        :type RowsFetched: int
        :param _User: 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _DefaultDB: 默认DB
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultDB: str
        :param _Coordinator: 执行的Coordinator节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Coordinator: str
        :param _MaxNodePeakMemoryUsage: 单节点内存峰值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNodePeakMemoryUsage: str
        :param _QueryType: 查询类型
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryType: str
        :param _ScanHDFSRows: 扫描的HDFS行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanHDFSRows: int
        :param _ScanKUDURows: 扫描的Kudu行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanKUDURows: int
        :param _ScanRowsTotal: 扫描的总行数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRowsTotal: int
        :param _TotalBytesRead: 读取的总字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalBytesRead: int
        :param _TotalBytesSent: 发送的总字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalBytesSent: int
        :param _TotalCpuTime: CPU总时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCpuTime: int
        :param _TotalInnerBytesSent: 内部数据发送总量(Bytes)
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalInnerBytesSent: int
        :param _TotalScanBytesSent: 内部扫描数据发送总量(Bytes)
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalScanBytesSent: int
        :param _EstimatedPerHostMemBytes: 预估单节点内存
注意：此字段可能返回 null，表示取不到有效值。
        :type EstimatedPerHostMemBytes: int
        :param _NumRowsFetchedFromCache: 从缓存中获取的数据行数
注意：此字段可能返回 null，表示取不到有效值。
        :type NumRowsFetchedFromCache: int
        """
        self._Statement = None
        self._Id = None
        self._StartTime = None
        self._Duration = None
        self._EndTime = None
        self._State = None
        self._RowsFetched = None
        self._User = None
        self._DefaultDB = None
        self._Coordinator = None
        self._MaxNodePeakMemoryUsage = None
        self._QueryType = None
        self._ScanHDFSRows = None
        self._ScanKUDURows = None
        self._ScanRowsTotal = None
        self._TotalBytesRead = None
        self._TotalBytesSent = None
        self._TotalCpuTime = None
        self._TotalInnerBytesSent = None
        self._TotalScanBytesSent = None
        self._EstimatedPerHostMemBytes = None
        self._NumRowsFetchedFromCache = None

    @property
    def Statement(self):
        return self._Statement

    @Statement.setter
    def Statement(self, Statement):
        self._Statement = Statement

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def RowsFetched(self):
        return self._RowsFetched

    @RowsFetched.setter
    def RowsFetched(self, RowsFetched):
        self._RowsFetched = RowsFetched

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def DefaultDB(self):
        return self._DefaultDB

    @DefaultDB.setter
    def DefaultDB(self, DefaultDB):
        self._DefaultDB = DefaultDB

    @property
    def Coordinator(self):
        return self._Coordinator

    @Coordinator.setter
    def Coordinator(self, Coordinator):
        self._Coordinator = Coordinator

    @property
    def MaxNodePeakMemoryUsage(self):
        return self._MaxNodePeakMemoryUsage

    @MaxNodePeakMemoryUsage.setter
    def MaxNodePeakMemoryUsage(self, MaxNodePeakMemoryUsage):
        self._MaxNodePeakMemoryUsage = MaxNodePeakMemoryUsage

    @property
    def QueryType(self):
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def ScanHDFSRows(self):
        return self._ScanHDFSRows

    @ScanHDFSRows.setter
    def ScanHDFSRows(self, ScanHDFSRows):
        self._ScanHDFSRows = ScanHDFSRows

    @property
    def ScanKUDURows(self):
        return self._ScanKUDURows

    @ScanKUDURows.setter
    def ScanKUDURows(self, ScanKUDURows):
        self._ScanKUDURows = ScanKUDURows

    @property
    def ScanRowsTotal(self):
        return self._ScanRowsTotal

    @ScanRowsTotal.setter
    def ScanRowsTotal(self, ScanRowsTotal):
        self._ScanRowsTotal = ScanRowsTotal

    @property
    def TotalBytesRead(self):
        return self._TotalBytesRead

    @TotalBytesRead.setter
    def TotalBytesRead(self, TotalBytesRead):
        self._TotalBytesRead = TotalBytesRead

    @property
    def TotalBytesSent(self):
        return self._TotalBytesSent

    @TotalBytesSent.setter
    def TotalBytesSent(self, TotalBytesSent):
        self._TotalBytesSent = TotalBytesSent

    @property
    def TotalCpuTime(self):
        return self._TotalCpuTime

    @TotalCpuTime.setter
    def TotalCpuTime(self, TotalCpuTime):
        self._TotalCpuTime = TotalCpuTime

    @property
    def TotalInnerBytesSent(self):
        return self._TotalInnerBytesSent

    @TotalInnerBytesSent.setter
    def TotalInnerBytesSent(self, TotalInnerBytesSent):
        self._TotalInnerBytesSent = TotalInnerBytesSent

    @property
    def TotalScanBytesSent(self):
        return self._TotalScanBytesSent

    @TotalScanBytesSent.setter
    def TotalScanBytesSent(self, TotalScanBytesSent):
        self._TotalScanBytesSent = TotalScanBytesSent

    @property
    def EstimatedPerHostMemBytes(self):
        return self._EstimatedPerHostMemBytes

    @EstimatedPerHostMemBytes.setter
    def EstimatedPerHostMemBytes(self, EstimatedPerHostMemBytes):
        self._EstimatedPerHostMemBytes = EstimatedPerHostMemBytes

    @property
    def NumRowsFetchedFromCache(self):
        return self._NumRowsFetchedFromCache

    @NumRowsFetchedFromCache.setter
    def NumRowsFetchedFromCache(self, NumRowsFetchedFromCache):
        self._NumRowsFetchedFromCache = NumRowsFetchedFromCache


    def _deserialize(self, params):
        self._Statement = params.get("Statement")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        self._EndTime = params.get("EndTime")
        self._State = params.get("State")
        self._RowsFetched = params.get("RowsFetched")
        self._User = params.get("User")
        self._DefaultDB = params.get("DefaultDB")
        self._Coordinator = params.get("Coordinator")
        self._MaxNodePeakMemoryUsage = params.get("MaxNodePeakMemoryUsage")
        self._QueryType = params.get("QueryType")
        self._ScanHDFSRows = params.get("ScanHDFSRows")
        self._ScanKUDURows = params.get("ScanKUDURows")
        self._ScanRowsTotal = params.get("ScanRowsTotal")
        self._TotalBytesRead = params.get("TotalBytesRead")
        self._TotalBytesSent = params.get("TotalBytesSent")
        self._TotalCpuTime = params.get("TotalCpuTime")
        self._TotalInnerBytesSent = params.get("TotalInnerBytesSent")
        self._TotalScanBytesSent = params.get("TotalScanBytesSent")
        self._EstimatedPerHostMemBytes = params.get("EstimatedPerHostMemBytes")
        self._NumRowsFetchedFromCache = params.get("NumRowsFetchedFromCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewEmrRequest(AbstractModel):
    """InquirePriceRenewEmr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeSpan: 实例续费的时长。需要结合TimeUnit一起使用。1表示续费一个月
        :type TimeSpan: int
        :param _InstanceId: 待续费集群ID列表。
        :type InstanceId: str
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _PayMode: 实例计费模式。此处只支持取值为1，表示包年包月。
        :type PayMode: int
        :param _TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
        :type TimeUnit: str
        :param _Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        """
        self._TimeSpan = None
        self._InstanceId = None
        self._Placement = None
        self._PayMode = None
        self._TimeUnit = None
        self._Currency = None

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency


    def _deserialize(self, params):
        self._TimeSpan = params.get("TimeSpan")
        self._InstanceId = params.get("InstanceId")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._PayMode = params.get("PayMode")
        self._TimeUnit = params.get("TimeUnit")
        self._Currency = params.get("Currency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewEmrResponse(AbstractModel):
    """InquirePriceRenewEmr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param _DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param _TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _TimeSpan: 实例续费的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._RequestId = params.get("RequestId")


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param _TimeSpan: 购买实例的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param _Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param _PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param _SupportHA: 是否开启节点高可用。取值范围：
<li>0：表示不开启节点高可用。</li>
<li>1：表示开启节点高可用。</li>
        :type SupportHA: int
        :param _Software: 部署的组件列表。不同的EMR产品ID（ProductId：具体含义参考入参ProductId字段）需要选择不同的必选组件：
<li>ProductId为1的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为2的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为4的时候，必选组件包括：hadoop-2.8.4、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为7的时候，必选组件包括：hadoop-3.1.2、knox-1.2.0、zookeeper-3.4.9</li>
        :type Software: list of str
        :param _ResourceSpec: 询价的节点规格。
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _VPCSettings: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _MetaType: hive共享元数据库类型。取值范围：
<li>EMR_NEW_META：表示集群默认创建</li>
<li>EMR_EXIT_METE：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>
        :type MetaType: str
        :param _UnifyMetaInstanceId: EMR-MetaDB实例
        :type UnifyMetaInstanceId: str
        :param _MetaDBInfo: 自定义MetaDB信息
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        :param _ProductId: 产品ID，不同产品ID表示不同的EMR产品版本。取值范围：
<li>1：表示EMR-V1.3.1。</li>
<li>2：表示EMR-V2.0.1。</li>
<li>4：表示EMR-V2.1.0。</li>
<li>7：表示EMR-V3.0.0。</li>
        :type ProductId: int
        :param _SceneName: 场景化取值：
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
        :type SceneName: str
        :param _ExternalService: 共用组件信息
        :type ExternalService: list of ExternalService
        :param _VersionID: 当前默认值为0，跨AZ特性支持后为1
        :type VersionID: int
        :param _MultiZoneSettings: 可用区的规格信息
        :type MultiZoneSettings: list of MultiZoneSetting
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._Currency = None
        self._PayMode = None
        self._SupportHA = None
        self._Software = None
        self._ResourceSpec = None
        self._Placement = None
        self._VPCSettings = None
        self._MetaType = None
        self._UnifyMetaInstanceId = None
        self._MetaDBInfo = None
        self._ProductId = None
        self._SceneName = None
        self._ExternalService = None
        self._VersionID = None
        self._MultiZoneSettings = None

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SupportHA(self):
        return self._SupportHA

    @SupportHA.setter
    def SupportHA(self, SupportHA):
        self._SupportHA = SupportHA

    @property
    def Software(self):
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def ResourceSpec(self):
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def VPCSettings(self):
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def MetaType(self):
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId

    @property
    def MetaDBInfo(self):
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def SceneName(self):
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def ExternalService(self):
        return self._ExternalService

    @ExternalService.setter
    def ExternalService(self, ExternalService):
        self._ExternalService = ExternalService

    @property
    def VersionID(self):
        return self._VersionID

    @VersionID.setter
    def VersionID(self, VersionID):
        self._VersionID = VersionID

    @property
    def MultiZoneSettings(self):
        return self._MultiZoneSettings

    @MultiZoneSettings.setter
    def MultiZoneSettings(self, MultiZoneSettings):
        self._MultiZoneSettings = MultiZoneSettings


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._Currency = params.get("Currency")
        self._PayMode = params.get("PayMode")
        self._SupportHA = params.get("SupportHA")
        self._Software = params.get("Software")
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NewResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self._ProductId = params.get("ProductId")
        self._SceneName = params.get("SceneName")
        if params.get("ExternalService") is not None:
            self._ExternalService = []
            for item in params.get("ExternalService"):
                obj = ExternalService()
                obj._deserialize(item)
                self._ExternalService.append(obj)
        self._VersionID = params.get("VersionID")
        if params.get("MultiZoneSettings") is not None:
            self._MultiZoneSettings = []
            for item in params.get("MultiZoneSettings"):
                obj = MultiZoneSetting()
                obj._deserialize(item)
                self._MultiZoneSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param _DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param _TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _TimeSpan: 购买实例的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _PriceList: 价格清单
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceList: list of ZoneDetailPriceResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._PriceList = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def PriceList(self):
        return self._PriceList

    @PriceList.setter
    def PriceList(self, PriceList):
        self._PriceList = PriceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        if params.get("PriceList") is not None:
            self._PriceList = []
            for item in params.get("PriceList"):
                obj = ZoneDetailPriceResult()
                obj._deserialize(item)
                self._PriceList.append(obj)
        self._RequestId = params.get("RequestId")


class InquiryPriceRenewInstanceRequest(AbstractModel):
    """InquiryPriceRenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeSpan: 实例续费的时长。需要结合TimeUnit一起使用。1表示续费一个月
        :type TimeSpan: int
        :param _ResourceIds: 待续费节点的资源ID列表。资源ID形如：emr-vm-xxxxxxxx。有效的资源ID可通过登录[控制台](https://console.cloud.tencent.com/emr)查询。
        :type ResourceIds: list of str
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _PayMode: 实例计费模式。此处只支持取值为1，表示包年包月。
        :type PayMode: int
        :param _TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
        :type TimeUnit: str
        :param _Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param _ModifyPayMode: 是否按量转包年包月。0：否，1：是。
        :type ModifyPayMode: int
        """
        self._TimeSpan = None
        self._ResourceIds = None
        self._Placement = None
        self._PayMode = None
        self._TimeUnit = None
        self._Currency = None
        self._ModifyPayMode = None

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def ModifyPayMode(self):
        return self._ModifyPayMode

    @ModifyPayMode.setter
    def ModifyPayMode(self, ModifyPayMode):
        self._ModifyPayMode = ModifyPayMode


    def _deserialize(self, params):
        self._TimeSpan = params.get("TimeSpan")
        self._ResourceIds = params.get("ResourceIds")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._PayMode = params.get("PayMode")
        self._TimeUnit = params.get("TimeUnit")
        self._Currency = params.get("Currency")
        self._ModifyPayMode = params.get("ModifyPayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewInstanceResponse(AbstractModel):
    """InquiryPriceRenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param _DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param _TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _TimeSpan: 实例续费的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._RequestId = params.get("RequestId")


class InquiryPriceScaleOutInstanceRequest(AbstractModel):
    """InquiryPriceScaleOutInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeUnit: 扩容的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param _TimeSpan: 扩容的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param _ZoneId: 实例所属的可用区ID，例如100003。该参数可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/213/15707) 的返回值中的ZoneId字段来获取。
        :type ZoneId: int
        :param _PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _CoreCount: 扩容的Core节点数量。
        :type CoreCount: int
        :param _TaskCount: 扩容的Task节点数量。
        :type TaskCount: int
        :param _Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param _RouterCount: 扩容的Router节点数量。
        :type RouterCount: int
        :param _MasterCount: 扩容的Master节点数量。
        :type MasterCount: int
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._ZoneId = None
        self._PayMode = None
        self._InstanceId = None
        self._CoreCount = None
        self._TaskCount = None
        self._Currency = None
        self._RouterCount = None
        self._MasterCount = None

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def TaskCount(self):
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def RouterCount(self):
        return self._RouterCount

    @RouterCount.setter
    def RouterCount(self, RouterCount):
        self._RouterCount = RouterCount

    @property
    def MasterCount(self):
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._ZoneId = params.get("ZoneId")
        self._PayMode = params.get("PayMode")
        self._InstanceId = params.get("InstanceId")
        self._CoreCount = params.get("CoreCount")
        self._TaskCount = params.get("TaskCount")
        self._Currency = params.get("Currency")
        self._RouterCount = params.get("RouterCount")
        self._MasterCount = params.get("MasterCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceScaleOutInstanceResponse(AbstractModel):
    """InquiryPriceScaleOutInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: str
        :param _DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: str
        :param _Unit: 扩容的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _PriceSpec: 询价的节点规格。
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceSpec: :class:`tencentcloud.emr.v20190103.models.PriceResource`
        :param _MultipleEmrPrice: 对应入参MultipleResources中多个规格的询价结果，其它出参返回的是第一个规格的询价结果
注意：此字段可能返回 null，表示取不到有效值。
        :type MultipleEmrPrice: list of EmrPrice
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._Unit = None
        self._PriceSpec = None
        self._MultipleEmrPrice = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def PriceSpec(self):
        return self._PriceSpec

    @PriceSpec.setter
    def PriceSpec(self, PriceSpec):
        self._PriceSpec = PriceSpec

    @property
    def MultipleEmrPrice(self):
        return self._MultipleEmrPrice

    @MultipleEmrPrice.setter
    def MultipleEmrPrice(self, MultipleEmrPrice):
        self._MultipleEmrPrice = MultipleEmrPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._Unit = params.get("Unit")
        if params.get("PriceSpec") is not None:
            self._PriceSpec = PriceResource()
            self._PriceSpec._deserialize(params.get("PriceSpec"))
        if params.get("MultipleEmrPrice") is not None:
            self._MultipleEmrPrice = []
            for item in params.get("MultipleEmrPrice"):
                obj = EmrPrice()
                obj._deserialize(item)
                self._MultipleEmrPrice.append(obj)
        self._RequestId = params.get("RequestId")


class InquiryPriceUpdateInstanceRequest(AbstractModel):
    """InquiryPriceUpdateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeUnit: 变配的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param _TimeSpan: 变配的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param _UpdateSpec: 节点变配的目标配置。
        :type UpdateSpec: :class:`tencentcloud.emr.v20190103.models.UpdateInstanceSettings`
        :param _PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param _ResourceIdList: 批量变配资源ID列表
        :type ResourceIdList: list of str
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._UpdateSpec = None
        self._PayMode = None
        self._Placement = None
        self._Currency = None
        self._ResourceIdList = None

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def UpdateSpec(self):
        return self._UpdateSpec

    @UpdateSpec.setter
    def UpdateSpec(self, UpdateSpec):
        self._UpdateSpec = UpdateSpec

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def ResourceIdList(self):
        return self._ResourceIdList

    @ResourceIdList.setter
    def ResourceIdList(self, ResourceIdList):
        self._ResourceIdList = ResourceIdList


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        if params.get("UpdateSpec") is not None:
            self._UpdateSpec = UpdateInstanceSettings()
            self._UpdateSpec._deserialize(params.get("UpdateSpec"))
        self._PayMode = params.get("PayMode")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._Currency = params.get("Currency")
        self._ResourceIdList = params.get("ResourceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpdateInstanceResponse(AbstractModel):
    """InquiryPriceUpdateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param _DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param _TimeUnit: 变配的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _TimeSpan: 变配的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _PriceDetail: 价格详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceDetail: list of PriceDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalCost = None
        self._DiscountCost = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._PriceDetail = None
        self._RequestId = None

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def PriceDetail(self):
        return self._PriceDetail

    @PriceDetail.setter
    def PriceDetail(self, PriceDetail):
        self._PriceDetail = PriceDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        if params.get("PriceDetail") is not None:
            self._PriceDetail = []
            for item in params.get("PriceDetail"):
                obj = PriceDetail()
                obj._deserialize(item)
                self._PriceDetail.append(obj)
        self._RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """实例预付费参数，只有在付费类型为PREPAID时生效。

    """

    def __init__(self):
        r"""
        :param _Period: 包年包月时间，默认为1，单位：月。
取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 24, 36, 48, 60。
        :type Period: int
        :param _RenewFlag: 是否自动续费，默认为否。
<li>true：是</li>
<li>false：否</li>
        :type RenewFlag: bool
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobFlowResource(AbstractModel):
    """机器资源描述。

    """

    def __init__(self):
        r"""
        :param _Spec: 机器类型描述。
        :type Spec: str
        :param _InstanceType: 机器类型描述，可参考CVM的该含义。
        :type InstanceType: str
        :param _Tags: 标签KV对。
        :type Tags: list of Tag
        :param _DiskGroups: 磁盘描述列表。
        :type DiskGroups: list of DiskGroup
        """
        self._Spec = None
        self._InstanceType = None
        self._Tags = None
        self._DiskGroups = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DiskGroups(self):
        return self._DiskGroups

    @DiskGroups.setter
    def DiskGroups(self, DiskGroups):
        self._DiskGroups = DiskGroups


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._InstanceType = params.get("InstanceType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("DiskGroups") is not None:
            self._DiskGroups = []
            for item in params.get("DiskGroups"):
                obj = DiskGroup()
                obj._deserialize(item)
                self._DiskGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobFlowResourceSpec(AbstractModel):
    """流程作业资源描述

    """

    def __init__(self):
        r"""
        :param _MasterCount: 主节点数量。
        :type MasterCount: int
        :param _MasterResourceSpec: 主节点配置。
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`
        :param _CoreCount: Core节点数量
        :type CoreCount: int
        :param _CoreResourceSpec: Core节点配置。
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`
        :param _TaskCount: Task节点数量。
        :type TaskCount: int
        :param _CommonCount: Common节点数量。
        :type CommonCount: int
        :param _TaskResourceSpec: Task节点配置。
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`
        :param _CommonResourceSpec: Common节点配置。
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`
        """
        self._MasterCount = None
        self._MasterResourceSpec = None
        self._CoreCount = None
        self._CoreResourceSpec = None
        self._TaskCount = None
        self._CommonCount = None
        self._TaskResourceSpec = None
        self._CommonResourceSpec = None

    @property
    def MasterCount(self):
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def MasterResourceSpec(self):
        return self._MasterResourceSpec

    @MasterResourceSpec.setter
    def MasterResourceSpec(self, MasterResourceSpec):
        self._MasterResourceSpec = MasterResourceSpec

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def CoreResourceSpec(self):
        return self._CoreResourceSpec

    @CoreResourceSpec.setter
    def CoreResourceSpec(self, CoreResourceSpec):
        self._CoreResourceSpec = CoreResourceSpec

    @property
    def TaskCount(self):
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CommonCount(self):
        return self._CommonCount

    @CommonCount.setter
    def CommonCount(self, CommonCount):
        self._CommonCount = CommonCount

    @property
    def TaskResourceSpec(self):
        return self._TaskResourceSpec

    @TaskResourceSpec.setter
    def TaskResourceSpec(self, TaskResourceSpec):
        self._TaskResourceSpec = TaskResourceSpec

    @property
    def CommonResourceSpec(self):
        return self._CommonResourceSpec

    @CommonResourceSpec.setter
    def CommonResourceSpec(self, CommonResourceSpec):
        self._CommonResourceSpec = CommonResourceSpec


    def _deserialize(self, params):
        self._MasterCount = params.get("MasterCount")
        if params.get("MasterResourceSpec") is not None:
            self._MasterResourceSpec = JobFlowResource()
            self._MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        self._CoreCount = params.get("CoreCount")
        if params.get("CoreResourceSpec") is not None:
            self._CoreResourceSpec = JobFlowResource()
            self._CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        self._TaskCount = params.get("TaskCount")
        self._CommonCount = params.get("CommonCount")
        if params.get("TaskResourceSpec") is not None:
            self._TaskResourceSpec = JobFlowResource()
            self._TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        if params.get("CommonResourceSpec") is not None:
            self._CommonResourceSpec = JobFlowResource()
            self._CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobResult(AbstractModel):
    """任务步骤结果描述

    """

    def __init__(self):
        r"""
        :param _Name: 任务步骤名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ActionOnFailure: 任务步骤失败时的处理策略，可以为以下值：
"CONTINUE"，跳过当前失败步骤，继续后续步骤。
“TERMINATE_CLUSTER”，终止当前及后续步骤，并销毁集群。
“CANCEL_AND_WAIT”，取消当前步骤并阻塞等待处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionOnFailure: str
        :param _JobState: 当前步骤的状态，可以为以下值：
“JobFlowStepStatusInit”，初始化状态，等待执行。
“JobFlowStepStatusRunning”，任务步骤正在执行。
“JobFlowStepStatusFailed”，任务步骤执行失败。
“JobFlowStepStatusSucceed”，任务步骤执行成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type JobState: str
        :param _ApplicationId: YARN任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        """
        self._Name = None
        self._ActionOnFailure = None
        self._JobState = None
        self._ApplicationId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionOnFailure(self):
        return self._ActionOnFailure

    @ActionOnFailure.setter
    def ActionOnFailure(self, ActionOnFailure):
        self._ActionOnFailure = ActionOnFailure

    @property
    def JobState(self):
        return self._JobState

    @JobState.setter
    def JobState(self, JobState):
        self._JobState = JobState

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ActionOnFailure = params.get("ActionOnFailure")
        self._JobState = params.get("JobState")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """登录设置

    """

    def __init__(self):
        r"""
        :param _Password: 实例登录密码，8-16个字符，包含大写字母、小写字母、数字和特殊字符四种，特殊符号仅支持!@%^*，密码第一位不能为特殊字符
        :type Password: str
        :param _PublicKeyId: 密钥ID。关联密钥后，就可以通过对应的私钥来访问实例；PublicKeyId可通过接口[DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699)获取
        :type PublicKeyId: str
        """
        self._Password = None
        self._PublicKeyId = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PublicKeyId(self):
        return self._PublicKeyId

    @PublicKeyId.setter
    def PublicKeyId(self, PublicKeyId):
        self._PublicKeyId = PublicKeyId


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._PublicKeyId = params.get("PublicKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetaDbInfo(AbstractModel):
    """元数据库信息

    """

    def __init__(self):
        r"""
        :param _MetaType: 元数据类型。
        :type MetaType: str
        :param _UnifyMetaInstanceId: 统一元数据库实例ID。
        :type UnifyMetaInstanceId: str
        :param _MetaDBInfo: 自建元数据库信息。
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        """
        self._MetaType = None
        self._UnifyMetaInstanceId = None
        self._MetaDBInfo = None

    @property
    def MetaType(self):
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def UnifyMetaInstanceId(self):
        return self._UnifyMetaInstanceId

    @UnifyMetaInstanceId.setter
    def UnifyMetaInstanceId(self, UnifyMetaInstanceId):
        self._UnifyMetaInstanceId = UnifyMetaInstanceId

    @property
    def MetaDBInfo(self):
        return self._MetaDBInfo

    @MetaDBInfo.setter
    def MetaDBInfo(self, MetaDBInfo):
        self._MetaDBInfo = MetaDBInfo


    def _deserialize(self, params):
        self._MetaType = params.get("MetaType")
        self._UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self._MetaDBInfo = CustomMetaInfo()
            self._MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcePoolsRequest(AbstractModel):
    """ModifyResourcePools请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群id
        :type InstanceId: str
        :param _Key: 取值范围：
<li>fair:代表公平调度标识</li>
<li>capacity:代表容量调度标识</li>
        :type Key: str
        """
        self._InstanceId = None
        self._Key = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcePoolsResponse(AbstractModel):
    """ModifyResourcePools返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsDraft: false表示不是草稿，提交刷新请求成功
        :type IsDraft: bool
        :param _ErrorMsg: 扩展字段，暂时没用
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsDraft = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def IsDraft(self):
        return self._IsDraft

    @IsDraft.setter
    def IsDraft(self, IsDraft):
        self._IsDraft = IsDraft

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsDraft = params.get("IsDraft")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ModifyResourceScheduleConfigRequest(AbstractModel):
    """ModifyResourceScheduleConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
        :type InstanceId: str
        :param _Key: 业务标识，fair表示编辑公平的配置项，fairPlan表示编辑执行计划，capacity表示编辑容量的配置项
        :type Key: str
        :param _Value: 修改后的模块消息
        :type Value: str
        """
        self._InstanceId = None
        self._Key = None
        self._Value = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceScheduleConfigResponse(AbstractModel):
    """ModifyResourceScheduleConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsDraft: true为草稿，表示还没有刷新资源池
        :type IsDraft: bool
        :param _ErrorMsg: 校验错误信息，如果不为空，则说明校验失败，配置没有成功
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _Data: 返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsDraft = None
        self._ErrorMsg = None
        self._Data = None
        self._RequestId = None

    @property
    def IsDraft(self):
        return self._IsDraft

    @IsDraft.setter
    def IsDraft(self, IsDraft):
        self._IsDraft = IsDraft

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsDraft = params.get("IsDraft")
        self._ErrorMsg = params.get("ErrorMsg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class ModifyResourceSchedulerRequest(AbstractModel):
    """ModifyResourceScheduler请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: emr集群的英文id
        :type InstanceId: str
        :param _OldValue: 老的调度器:fair
        :type OldValue: str
        :param _NewValue: 新的调度器:capacity
        :type NewValue: str
        """
        self._InstanceId = None
        self._OldValue = None
        self._NewValue = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldValue(self):
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceSchedulerResponse(AbstractModel):
    """ModifyResourceScheduler返回参数结构体

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


class MultiDisk(AbstractModel):
    """多云盘参数

    """

    def __init__(self):
        r"""
        :param _DiskType: 云盘类型
<li>CLOUD_SSD：表示云SSD。</li>
<li>CLOUD_PREMIUM：表示高效云盘。</li>
<li>CLOUD_HSSD：表示增强型SSD云硬盘。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _Volume: 云盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Volume: int
        :param _Count: 该类型云盘个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._DiskType = None
        self._Volume = None
        self._Count = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._Volume = params.get("Volume")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiDiskMC(AbstractModel):
    """多云盘参数

    """

    def __init__(self):
        r"""
        :param _Count: 该类型云盘个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Type: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _Volume: 云盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Volume: int
        """
        self._Count = None
        self._Type = None
        self._Volume = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Type = params.get("Type")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiZoneSetting(AbstractModel):
    """各个可用区的参数信息

    """

    def __init__(self):
        r"""
        :param _ZoneTag: "master"、"standby"、"third-party"
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneTag: str
        :param _VPCSettings: 无
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param _Placement: 无
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _ResourceSpec: 无
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        """
        self._ZoneTag = None
        self._VPCSettings = None
        self._Placement = None
        self._ResourceSpec = None

    @property
    def ZoneTag(self):
        return self._ZoneTag

    @ZoneTag.setter
    def ZoneTag(self, ZoneTag):
        self._ZoneTag = ZoneTag

    @property
    def VPCSettings(self):
        return self._VPCSettings

    @VPCSettings.setter
    def VPCSettings(self, VPCSettings):
        self._VPCSettings = VPCSettings

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ResourceSpec(self):
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec


    def _deserialize(self, params):
        self._ZoneTag = params.get("ZoneTag")
        if params.get("VPCSettings") is not None:
            self._VPCSettings = VPCSettings()
            self._VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NewResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewResourceSpec(AbstractModel):
    """资源描述

    """

    def __init__(self):
        r"""
        :param _MasterResourceSpec: 描述Master节点资源
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _CoreResourceSpec: 描述Core节点资源
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _TaskResourceSpec: 描述Task节点资源
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _MasterCount: Master节点数量
        :type MasterCount: int
        :param _CoreCount: Core节点数量
        :type CoreCount: int
        :param _TaskCount: Task节点数量
        :type TaskCount: int
        :param _CommonResourceSpec: 描述Common节点资源
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param _CommonCount: Common节点数量
        :type CommonCount: int
        """
        self._MasterResourceSpec = None
        self._CoreResourceSpec = None
        self._TaskResourceSpec = None
        self._MasterCount = None
        self._CoreCount = None
        self._TaskCount = None
        self._CommonResourceSpec = None
        self._CommonCount = None

    @property
    def MasterResourceSpec(self):
        return self._MasterResourceSpec

    @MasterResourceSpec.setter
    def MasterResourceSpec(self, MasterResourceSpec):
        self._MasterResourceSpec = MasterResourceSpec

    @property
    def CoreResourceSpec(self):
        return self._CoreResourceSpec

    @CoreResourceSpec.setter
    def CoreResourceSpec(self, CoreResourceSpec):
        self._CoreResourceSpec = CoreResourceSpec

    @property
    def TaskResourceSpec(self):
        return self._TaskResourceSpec

    @TaskResourceSpec.setter
    def TaskResourceSpec(self, TaskResourceSpec):
        self._TaskResourceSpec = TaskResourceSpec

    @property
    def MasterCount(self):
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def TaskCount(self):
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CommonResourceSpec(self):
        return self._CommonResourceSpec

    @CommonResourceSpec.setter
    def CommonResourceSpec(self, CommonResourceSpec):
        self._CommonResourceSpec = CommonResourceSpec

    @property
    def CommonCount(self):
        return self._CommonCount

    @CommonCount.setter
    def CommonCount(self, CommonCount):
        self._CommonCount = CommonCount


    def _deserialize(self, params):
        if params.get("MasterResourceSpec") is not None:
            self._MasterResourceSpec = Resource()
            self._MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self._CoreResourceSpec = Resource()
            self._CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self._TaskResourceSpec = Resource()
            self._TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        self._MasterCount = params.get("MasterCount")
        self._CoreCount = params.get("CoreCount")
        self._TaskCount = params.get("TaskCount")
        if params.get("CommonResourceSpec") is not None:
            self._CommonResourceSpec = Resource()
            self._CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self._CommonCount = params.get("CommonCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeDetailPriceResult(AbstractModel):
    """用于创建集群价格清单 节点价格详情

    """

    def __init__(self):
        r"""
        :param _NodeType: 节点类型 master core task common router mysql
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param _PartDetailPrice: 节点组成部分价格详情
        :type PartDetailPrice: list of PartDetailPriceItem
        """
        self._NodeType = None
        self._PartDetailPrice = None

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def PartDetailPrice(self):
        return self._PartDetailPrice

    @PartDetailPrice.setter
    def PartDetailPrice(self, PartDetailPrice):
        self._PartDetailPrice = PartDetailPrice


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        if params.get("PartDetailPrice") is not None:
            self._PartDetailPrice = []
            for item in params.get("PartDetailPrice"):
                obj = PartDetailPriceItem()
                obj._deserialize(item)
                self._PartDetailPrice.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeHardwareInfo(AbstractModel):
    """节点硬件信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户APPID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _SerialNo: 序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialNo: str
        :param _OrderNo: 机器实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderNo: str
        :param _WanIp: master节点绑定外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type WanIp: str
        :param _Flag: 节点类型。0:common节点；1:master节点
；2:core节点；3:task节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Flag: int
        :param _Spec: 节点规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param _CpuNum: 节点核数
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuNum: int
        :param _MemSize: 节点内存
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _MemDesc: 节点内存描述
注意：此字段可能返回 null，表示取不到有效值。
        :type MemDesc: str
        :param _RegionId: 节点所在region
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _ZoneId: 节点所在Zone
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyTime: str
        :param _FreeTime: 释放时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeTime: str
        :param _DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: str
        :param _NameTag: 节点描述
注意：此字段可能返回 null，表示取不到有效值。
        :type NameTag: str
        :param _Services: 节点部署服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: str
        :param _StorageType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param _RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param _ChargeType: 付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param _CdbIp: 数据库IP
注意：此字段可能返回 null，表示取不到有效值。
        :type CdbIp: str
        :param _CdbPort: 数据库端口
注意：此字段可能返回 null，表示取不到有效值。
        :type CdbPort: int
        :param _HwDiskSize: 硬盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type HwDiskSize: int
        :param _HwDiskSizeDesc: 硬盘容量描述
注意：此字段可能返回 null，表示取不到有效值。
        :type HwDiskSizeDesc: str
        :param _HwMemSize: 内存容量
注意：此字段可能返回 null，表示取不到有效值。
        :type HwMemSize: int
        :param _HwMemSizeDesc: 内存容量描述
注意：此字段可能返回 null，表示取不到有效值。
        :type HwMemSizeDesc: str
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _EmrResourceId: 节点资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EmrResourceId: str
        :param _IsAutoRenew: 续费标志
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoRenew: int
        :param _DeviceClass: 设备标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceClass: str
        :param _Mutable: 支持变配
注意：此字段可能返回 null，表示取不到有效值。
        :type Mutable: int
        :param _MCMultiDisk: 多云盘
注意：此字段可能返回 null，表示取不到有效值。
        :type MCMultiDisk: list of MultiDiskMC
        :param _CdbNodeInfo: 数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CdbNodeInfo: :class:`tencentcloud.emr.v20190103.models.CdbInfo`
        :param _Ip: 内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Destroyable: 此节点是否可销毁，1可销毁，0不可销毁
注意：此字段可能返回 null，表示取不到有效值。
        :type Destroyable: int
        :param _Tags: 节点绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _AutoFlag: 是否是自动扩缩容节点，0为普通节点，1为自动扩缩容节点。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoFlag: int
        :param _HardwareResourceType: 资源类型, host/pod
注意：此字段可能返回 null，表示取不到有效值。
        :type HardwareResourceType: str
        :param _IsDynamicSpec: 是否浮动规格，1是，0否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDynamicSpec: int
        :param _DynamicPodSpec: 浮动规格值json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicPodSpec: str
        :param _SupportModifyPayMode: 是否支持变更计费类型 1是，0否
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportModifyPayMode: int
        :param _RootStorageType: 系统盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RootStorageType: int
        :param _Zone: 可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _SubnetInfo: 子网
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetInfo: :class:`tencentcloud.emr.v20190103.models.SubnetInfo`
        :param _Clients: 客户端
注意：此字段可能返回 null，表示取不到有效值。
        :type Clients: str
        :param _CurrentTime: 系统当前时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentTime: str
        :param _IsFederation: 是否用于联邦 ,1是，0否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFederation: int
        :param _DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _ServiceClient: 服务
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceClient: str
        :param _DisableApiTermination: 该实例是否开启实例保护，true为开启 false为关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type DisableApiTermination: bool
        :param _TradeVersion: 0表示老计费，1表示新计费
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeVersion: int
        """
        self._AppId = None
        self._SerialNo = None
        self._OrderNo = None
        self._WanIp = None
        self._Flag = None
        self._Spec = None
        self._CpuNum = None
        self._MemSize = None
        self._MemDesc = None
        self._RegionId = None
        self._ZoneId = None
        self._ApplyTime = None
        self._FreeTime = None
        self._DiskSize = None
        self._NameTag = None
        self._Services = None
        self._StorageType = None
        self._RootSize = None
        self._ChargeType = None
        self._CdbIp = None
        self._CdbPort = None
        self._HwDiskSize = None
        self._HwDiskSizeDesc = None
        self._HwMemSize = None
        self._HwMemSizeDesc = None
        self._ExpireTime = None
        self._EmrResourceId = None
        self._IsAutoRenew = None
        self._DeviceClass = None
        self._Mutable = None
        self._MCMultiDisk = None
        self._CdbNodeInfo = None
        self._Ip = None
        self._Destroyable = None
        self._Tags = None
        self._AutoFlag = None
        self._HardwareResourceType = None
        self._IsDynamicSpec = None
        self._DynamicPodSpec = None
        self._SupportModifyPayMode = None
        self._RootStorageType = None
        self._Zone = None
        self._SubnetInfo = None
        self._Clients = None
        self._CurrentTime = None
        self._IsFederation = None
        self._DeviceName = None
        self._ServiceClient = None
        self._DisableApiTermination = None
        self._TradeVersion = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def SerialNo(self):
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def OrderNo(self):
        return self._OrderNo

    @OrderNo.setter
    def OrderNo(self, OrderNo):
        self._OrderNo = OrderNo

    @property
    def WanIp(self):
        return self._WanIp

    @WanIp.setter
    def WanIp(self, WanIp):
        self._WanIp = WanIp

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def CpuNum(self):
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def MemDesc(self):
        return self._MemDesc

    @MemDesc.setter
    def MemDesc(self, MemDesc):
        self._MemDesc = MemDesc

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
    def ApplyTime(self):
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def FreeTime(self):
        return self._FreeTime

    @FreeTime.setter
    def FreeTime(self, FreeTime):
        self._FreeTime = FreeTime

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def NameTag(self):
        return self._NameTag

    @NameTag.setter
    def NameTag(self, NameTag):
        self._NameTag = NameTag

    @property
    def Services(self):
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def RootSize(self):
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def CdbIp(self):
        return self._CdbIp

    @CdbIp.setter
    def CdbIp(self, CdbIp):
        self._CdbIp = CdbIp

    @property
    def CdbPort(self):
        return self._CdbPort

    @CdbPort.setter
    def CdbPort(self, CdbPort):
        self._CdbPort = CdbPort

    @property
    def HwDiskSize(self):
        return self._HwDiskSize

    @HwDiskSize.setter
    def HwDiskSize(self, HwDiskSize):
        self._HwDiskSize = HwDiskSize

    @property
    def HwDiskSizeDesc(self):
        return self._HwDiskSizeDesc

    @HwDiskSizeDesc.setter
    def HwDiskSizeDesc(self, HwDiskSizeDesc):
        self._HwDiskSizeDesc = HwDiskSizeDesc

    @property
    def HwMemSize(self):
        return self._HwMemSize

    @HwMemSize.setter
    def HwMemSize(self, HwMemSize):
        self._HwMemSize = HwMemSize

    @property
    def HwMemSizeDesc(self):
        return self._HwMemSizeDesc

    @HwMemSizeDesc.setter
    def HwMemSizeDesc(self, HwMemSizeDesc):
        self._HwMemSizeDesc = HwMemSizeDesc

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def EmrResourceId(self):
        return self._EmrResourceId

    @EmrResourceId.setter
    def EmrResourceId(self, EmrResourceId):
        self._EmrResourceId = EmrResourceId

    @property
    def IsAutoRenew(self):
        return self._IsAutoRenew

    @IsAutoRenew.setter
    def IsAutoRenew(self, IsAutoRenew):
        self._IsAutoRenew = IsAutoRenew

    @property
    def DeviceClass(self):
        return self._DeviceClass

    @DeviceClass.setter
    def DeviceClass(self, DeviceClass):
        self._DeviceClass = DeviceClass

    @property
    def Mutable(self):
        return self._Mutable

    @Mutable.setter
    def Mutable(self, Mutable):
        self._Mutable = Mutable

    @property
    def MCMultiDisk(self):
        return self._MCMultiDisk

    @MCMultiDisk.setter
    def MCMultiDisk(self, MCMultiDisk):
        self._MCMultiDisk = MCMultiDisk

    @property
    def CdbNodeInfo(self):
        return self._CdbNodeInfo

    @CdbNodeInfo.setter
    def CdbNodeInfo(self, CdbNodeInfo):
        self._CdbNodeInfo = CdbNodeInfo

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Destroyable(self):
        return self._Destroyable

    @Destroyable.setter
    def Destroyable(self, Destroyable):
        self._Destroyable = Destroyable

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoFlag(self):
        return self._AutoFlag

    @AutoFlag.setter
    def AutoFlag(self, AutoFlag):
        self._AutoFlag = AutoFlag

    @property
    def HardwareResourceType(self):
        return self._HardwareResourceType

    @HardwareResourceType.setter
    def HardwareResourceType(self, HardwareResourceType):
        self._HardwareResourceType = HardwareResourceType

    @property
    def IsDynamicSpec(self):
        return self._IsDynamicSpec

    @IsDynamicSpec.setter
    def IsDynamicSpec(self, IsDynamicSpec):
        self._IsDynamicSpec = IsDynamicSpec

    @property
    def DynamicPodSpec(self):
        return self._DynamicPodSpec

    @DynamicPodSpec.setter
    def DynamicPodSpec(self, DynamicPodSpec):
        self._DynamicPodSpec = DynamicPodSpec

    @property
    def SupportModifyPayMode(self):
        return self._SupportModifyPayMode

    @SupportModifyPayMode.setter
    def SupportModifyPayMode(self, SupportModifyPayMode):
        self._SupportModifyPayMode = SupportModifyPayMode

    @property
    def RootStorageType(self):
        return self._RootStorageType

    @RootStorageType.setter
    def RootStorageType(self, RootStorageType):
        self._RootStorageType = RootStorageType

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetInfo(self):
        return self._SubnetInfo

    @SubnetInfo.setter
    def SubnetInfo(self, SubnetInfo):
        self._SubnetInfo = SubnetInfo

    @property
    def Clients(self):
        return self._Clients

    @Clients.setter
    def Clients(self, Clients):
        self._Clients = Clients

    @property
    def CurrentTime(self):
        return self._CurrentTime

    @CurrentTime.setter
    def CurrentTime(self, CurrentTime):
        self._CurrentTime = CurrentTime

    @property
    def IsFederation(self):
        return self._IsFederation

    @IsFederation.setter
    def IsFederation(self, IsFederation):
        self._IsFederation = IsFederation

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ServiceClient(self):
        return self._ServiceClient

    @ServiceClient.setter
    def ServiceClient(self, ServiceClient):
        self._ServiceClient = ServiceClient

    @property
    def DisableApiTermination(self):
        return self._DisableApiTermination

    @DisableApiTermination.setter
    def DisableApiTermination(self, DisableApiTermination):
        self._DisableApiTermination = DisableApiTermination

    @property
    def TradeVersion(self):
        return self._TradeVersion

    @TradeVersion.setter
    def TradeVersion(self, TradeVersion):
        self._TradeVersion = TradeVersion


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._SerialNo = params.get("SerialNo")
        self._OrderNo = params.get("OrderNo")
        self._WanIp = params.get("WanIp")
        self._Flag = params.get("Flag")
        self._Spec = params.get("Spec")
        self._CpuNum = params.get("CpuNum")
        self._MemSize = params.get("MemSize")
        self._MemDesc = params.get("MemDesc")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._ApplyTime = params.get("ApplyTime")
        self._FreeTime = params.get("FreeTime")
        self._DiskSize = params.get("DiskSize")
        self._NameTag = params.get("NameTag")
        self._Services = params.get("Services")
        self._StorageType = params.get("StorageType")
        self._RootSize = params.get("RootSize")
        self._ChargeType = params.get("ChargeType")
        self._CdbIp = params.get("CdbIp")
        self._CdbPort = params.get("CdbPort")
        self._HwDiskSize = params.get("HwDiskSize")
        self._HwDiskSizeDesc = params.get("HwDiskSizeDesc")
        self._HwMemSize = params.get("HwMemSize")
        self._HwMemSizeDesc = params.get("HwMemSizeDesc")
        self._ExpireTime = params.get("ExpireTime")
        self._EmrResourceId = params.get("EmrResourceId")
        self._IsAutoRenew = params.get("IsAutoRenew")
        self._DeviceClass = params.get("DeviceClass")
        self._Mutable = params.get("Mutable")
        if params.get("MCMultiDisk") is not None:
            self._MCMultiDisk = []
            for item in params.get("MCMultiDisk"):
                obj = MultiDiskMC()
                obj._deserialize(item)
                self._MCMultiDisk.append(obj)
        if params.get("CdbNodeInfo") is not None:
            self._CdbNodeInfo = CdbInfo()
            self._CdbNodeInfo._deserialize(params.get("CdbNodeInfo"))
        self._Ip = params.get("Ip")
        self._Destroyable = params.get("Destroyable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoFlag = params.get("AutoFlag")
        self._HardwareResourceType = params.get("HardwareResourceType")
        self._IsDynamicSpec = params.get("IsDynamicSpec")
        self._DynamicPodSpec = params.get("DynamicPodSpec")
        self._SupportModifyPayMode = params.get("SupportModifyPayMode")
        self._RootStorageType = params.get("RootStorageType")
        self._Zone = params.get("Zone")
        if params.get("SubnetInfo") is not None:
            self._SubnetInfo = SubnetInfo()
            self._SubnetInfo._deserialize(params.get("SubnetInfo"))
        self._Clients = params.get("Clients")
        self._CurrentTime = params.get("CurrentTime")
        self._IsFederation = params.get("IsFederation")
        self._DeviceName = params.get("DeviceName")
        self._ServiceClient = params.get("ServiceClient")
        self._DisableApiTermination = params.get("DisableApiTermination")
        self._TradeVersion = params.get("TradeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeResourceSpec(AbstractModel):
    """资源详情

    """

    def __init__(self):
        r"""
        :param _InstanceType: 规格类型，如S2.MEDIUM8
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _SystemDisk: 系统盘，系统盘个数不超过1块
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDisk: list of DiskSpecInfo
        :param _Tags: 需要绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _DataDisk: 云数据盘，云数据盘总个数不超过15块
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisk: list of DiskSpecInfo
        :param _LocalDataDisk: 本地数据盘
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDataDisk: list of DiskSpecInfo
        """
        self._InstanceType = None
        self._SystemDisk = None
        self._Tags = None
        self._DataDisk = None
        self._LocalDataDisk = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DataDisk(self):
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def LocalDataDisk(self):
        return self._LocalDataDisk

    @LocalDataDisk.setter
    def LocalDataDisk(self, LocalDataDisk):
        self._LocalDataDisk = LocalDataDisk


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = []
            for item in params.get("SystemDisk"):
                obj = DiskSpecInfo()
                obj._deserialize(item)
                self._SystemDisk.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("DataDisk") is not None:
            self._DataDisk = []
            for item in params.get("DataDisk"):
                obj = DiskSpecInfo()
                obj._deserialize(item)
                self._DataDisk.append(obj)
        if params.get("LocalDataDisk") is not None:
            self._LocalDataDisk = []
            for item in params.get("LocalDataDisk"):
                obj = DiskSpecInfo()
                obj._deserialize(item)
                self._LocalDataDisk.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpScope(AbstractModel):
    """操作范围

    """

    def __init__(self):
        r"""
        :param _ServiceInfoList: 操作范围，要操作的服务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceInfoList: list of ServiceBasicRestartInfo
        """
        self._ServiceInfoList = None

    @property
    def ServiceInfoList(self):
        return self._ServiceInfoList

    @ServiceInfoList.setter
    def ServiceInfoList(self, ServiceInfoList):
        self._ServiceInfoList = ServiceInfoList


    def _deserialize(self, params):
        if params.get("ServiceInfoList") is not None:
            self._ServiceInfoList = []
            for item in params.get("ServiceInfoList"):
                obj = ServiceBasicRestartInfo()
                obj._deserialize(item)
                self._ServiceInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutterResource(AbstractModel):
    """资源详情

    """

    def __init__(self):
        r"""
        :param _Spec: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param _SpecName: 规格名
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param _StorageType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param _DiskType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param _MemSize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _Cpu: CPU个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _InstanceType: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        """
        self._Spec = None
        self._SpecName = None
        self._StorageType = None
        self._DiskType = None
        self._RootSize = None
        self._MemSize = None
        self._Cpu = None
        self._DiskSize = None
        self._InstanceType = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def RootSize(self):
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._SpecName = params.get("SpecName")
        self._StorageType = params.get("StorageType")
        self._DiskType = params.get("DiskType")
        self._RootSize = params.get("RootSize")
        self._MemSize = params.get("MemSize")
        self._Cpu = params.get("Cpu")
        self._DiskSize = params.get("DiskSize")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartDetailPriceItem(AbstractModel):
    """用于创建集群价格清单-节点组成部分价格

    """

    def __init__(self):
        r"""
        :param _InstanceType: 类型包括：节点->node、系统盘->rootDisk、云数据盘->dataDisk、metaDB
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _Price: 单价（原价）
注意：此字段可能返回 null，表示取不到有效值。
        :type Price: float
        :param _RealCost: 单价（折扣价）
注意：此字段可能返回 null，表示取不到有效值。
        :type RealCost: float
        :param _RealTotalCost: 总价（折扣价）
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTotalCost: float
        :param _Policy: 折扣
注意：此字段可能返回 null，表示取不到有效值。
        :type Policy: float
        :param _GoodsNum: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsNum: int
        """
        self._InstanceType = None
        self._Price = None
        self._RealCost = None
        self._RealTotalCost = None
        self._Policy = None
        self._GoodsNum = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RealCost(self):
        return self._RealCost

    @RealCost.setter
    def RealCost(self, RealCost):
        self._RealCost = RealCost

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._Price = params.get("Price")
        self._RealCost = params.get("RealCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._Policy = params.get("Policy")
        self._GoodsNum = params.get("GoodsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersistentVolumeContext(AbstractModel):
    """Pod PVC存储方式描述

    """

    def __init__(self):
        r"""
        :param _DiskSize: 磁盘大小，单位为GB。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _DiskType: 磁盘类型。CLOUD_PREMIUM;CLOUD_SSD
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskNum: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskNum: int
        """
        self._DiskSize = None
        self._DiskType = None
        self._DiskNum = None

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskNum(self):
        return self._DiskNum

    @DiskNum.setter
    def DiskNum(self, DiskNum):
        self._DiskNum = DiskNum


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        self._DiskNum = params.get("DiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """描述集群实例位置信息

    """

    def __init__(self):
        r"""
        :param _Zone: 实例所属的可用区，例如ap-guangzhou-1。该参数也可以通过调用[DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用[DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        """
        self._Zone = None
        self._ProjectId = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodNewParameter(AbstractModel):
    """POD自定义权限和自定义参数

    """

    def __init__(self):
        r"""
        :param _InstanceId: TKE或EKS集群ID
        :type InstanceId: str
        :param _Config: 自定义权限
如：
{
  "apiVersion": "v1",
  "clusters": [
    {
      "cluster": {
        "certificate-authority-data": "xxxxxx==",
        "server": "https://xxxxx.com"
      },
      "name": "cls-xxxxx"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "cls-xxxxx",
        "user": "100014xxxxx"
      },
      "name": "cls-a44yhcxxxxxxxxxx"
    }
  ],
  "current-context": "cls-a4xxxx-context-default",
  "kind": "Config",
  "preferences": {},
  "users": [
    {
      "name": "100014xxxxx",
      "user": {
        "client-certificate-data": "xxxxxx",
        "client-key-data": "xxxxxx"
      }
    }
  ]
}
        :type Config: str
        :param _Parameter: 自定义参数
如：
{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "test-deployment",
      "labels": {
        "app": "test"
      }
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": {
          "app": "test-app"
        }
      },
      "template": {
        "metadata": {
          "annotations": {
            "your-organization.com/department-v1": "test-example-v1",
            "your-organization.com/department-v2": "test-example-v2"
          },
          "labels": {
            "app": "test-app",
            "environment": "production"
          }
        },
        "spec": {
          "nodeSelector": {
            "your-organization/node-test": "test-node"
          },
          "containers": [
            {
              "name": "nginx",
              "image": "nginx:1.14.2",
              "ports": [
                {
                  "containerPort": 80
                }
              ]
            }
          ],
          "affinity": {
            "nodeAffinity": {
              "requiredDuringSchedulingIgnoredDuringExecution": {
                "nodeSelectorTerms": [
                  {
                    "matchExpressions": [
                      {
                        "key": "disk-type",
                        "operator": "In",
                        "values": [
                          "ssd",
                          "sas"
                        ]
                      },
                      {
                        "key": "cpu-num",
                        "operator": "Gt",
                        "values": [
                          "6"
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
        :type Parameter: str
        """
        self._InstanceId = None
        self._Config = None
        self._Parameter = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Parameter(self):
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Config = params.get("Config")
        self._Parameter = params.get("Parameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodNewSpec(AbstractModel):
    """扩容容器资源时的资源描述

    """

    def __init__(self):
        r"""
        :param _ResourceProviderIdentifier: 外部资源提供者的标识符，例如"cls-a1cd23fa"。
        :type ResourceProviderIdentifier: str
        :param _ResourceProviderType: 外部资源提供者类型，例如"tke",当前仅支持"tke"。
        :type ResourceProviderType: str
        :param _NodeFlag: 资源的用途，即节点类型，当前仅支持"TASK"。
        :type NodeFlag: str
        :param _Cpu: CPU核数。
        :type Cpu: int
        :param _Memory: 内存大小，单位为GB。
        :type Memory: int
        :param _CpuType: Eks集群-CPU类型，当前支持"intel"和"amd"
        :type CpuType: str
        :param _PodVolumes: Pod节点数据目录挂载信息。
        :type PodVolumes: list of PodVolume
        :param _EnableDynamicSpecFlag: 是否浮动规格，默认否
<li>true：代表是</li>
<li>false：代表否</li>
        :type EnableDynamicSpecFlag: bool
        :param _DynamicPodSpec: 浮动规格
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicPodSpec: :class:`tencentcloud.emr.v20190103.models.DynamicPodSpec`
        :param _VpcId: 代表vpc网络唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 代表vpc子网唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _PodName: pod name
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        """
        self._ResourceProviderIdentifier = None
        self._ResourceProviderType = None
        self._NodeFlag = None
        self._Cpu = None
        self._Memory = None
        self._CpuType = None
        self._PodVolumes = None
        self._EnableDynamicSpecFlag = None
        self._DynamicPodSpec = None
        self._VpcId = None
        self._SubnetId = None
        self._PodName = None

    @property
    def ResourceProviderIdentifier(self):
        return self._ResourceProviderIdentifier

    @ResourceProviderIdentifier.setter
    def ResourceProviderIdentifier(self, ResourceProviderIdentifier):
        self._ResourceProviderIdentifier = ResourceProviderIdentifier

    @property
    def ResourceProviderType(self):
        return self._ResourceProviderType

    @ResourceProviderType.setter
    def ResourceProviderType(self, ResourceProviderType):
        self._ResourceProviderType = ResourceProviderType

    @property
    def NodeFlag(self):
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

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
    def CpuType(self):
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def PodVolumes(self):
        return self._PodVolumes

    @PodVolumes.setter
    def PodVolumes(self, PodVolumes):
        self._PodVolumes = PodVolumes

    @property
    def EnableDynamicSpecFlag(self):
        return self._EnableDynamicSpecFlag

    @EnableDynamicSpecFlag.setter
    def EnableDynamicSpecFlag(self, EnableDynamicSpecFlag):
        self._EnableDynamicSpecFlag = EnableDynamicSpecFlag

    @property
    def DynamicPodSpec(self):
        return self._DynamicPodSpec

    @DynamicPodSpec.setter
    def DynamicPodSpec(self, DynamicPodSpec):
        self._DynamicPodSpec = DynamicPodSpec

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
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName


    def _deserialize(self, params):
        self._ResourceProviderIdentifier = params.get("ResourceProviderIdentifier")
        self._ResourceProviderType = params.get("ResourceProviderType")
        self._NodeFlag = params.get("NodeFlag")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._CpuType = params.get("CpuType")
        if params.get("PodVolumes") is not None:
            self._PodVolumes = []
            for item in params.get("PodVolumes"):
                obj = PodVolume()
                obj._deserialize(item)
                self._PodVolumes.append(obj)
        self._EnableDynamicSpecFlag = params.get("EnableDynamicSpecFlag")
        if params.get("DynamicPodSpec") is not None:
            self._DynamicPodSpec = DynamicPodSpec()
            self._DynamicPodSpec._deserialize(params.get("DynamicPodSpec"))
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodParameter(AbstractModel):
    """POD自定义权限和自定义参数

    """

    def __init__(self):
        r"""
        :param _ClusterId: TKE或EKS集群ID
        :type ClusterId: str
        :param _Config: 自定义权限
如：
{
  "apiVersion": "v1",
  "clusters": [
    {
      "cluster": {
        "certificate-authority-data": "xxxxxx==",
        "server": "https://xxxxx.com"
      },
      "name": "cls-xxxxx"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "cls-xxxxx",
        "user": "100014xxxxx"
      },
      "name": "cls-a44yhcxxxxxxxxxx"
    }
  ],
  "current-context": "cls-a4xxxx-context-default",
  "kind": "Config",
  "preferences": {},
  "users": [
    {
      "name": "100014xxxxx",
      "user": {
        "client-certificate-data": "xxxxxx",
        "client-key-data": "xxxxxx"
      }
    }
  ]
}
        :type Config: str
        :param _Parameter: 自定义参数
如：
{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "test-deployment",
      "labels": {
        "app": "test"
      }
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": {
          "app": "test-app"
        }
      },
      "template": {
        "metadata": {
          "annotations": {
            "your-organization.com/department-v1": "test-example-v1",
            "your-organization.com/department-v2": "test-example-v2"
          },
          "labels": {
            "app": "test-app",
            "environment": "production"
          }
        },
        "spec": {
          "nodeSelector": {
            "your-organization/node-test": "test-node"
          },
          "containers": [
            {
              "name": "nginx",
              "image": "nginx:1.14.2",
              "ports": [
                {
                  "containerPort": 80
                }
              ]
            }
          ],
          "affinity": {
            "nodeAffinity": {
              "requiredDuringSchedulingIgnoredDuringExecution": {
                "nodeSelectorTerms": [
                  {
                    "matchExpressions": [
                      {
                        "key": "disk-type",
                        "operator": "In",
                        "values": [
                          "ssd",
                          "sas"
                        ]
                      },
                      {
                        "key": "cpu-num",
                        "operator": "Gt",
                        "values": [
                          "6"
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
        :type Parameter: str
        """
        self._ClusterId = None
        self._Config = None
        self._Parameter = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Parameter(self):
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Config = params.get("Config")
        self._Parameter = params.get("Parameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSaleSpec(AbstractModel):
    """Pod资源售卖规格

    """

    def __init__(self):
        r"""
        :param _NodeType: 可售卖的资源规格，仅为以下值:"TASK","CORE","MASTER","ROUTER"。
        :type NodeType: str
        :param _Cpu: Cpu核数。
        :type Cpu: int
        :param _Memory: 内存数量，单位为GB。
        :type Memory: int
        :param _Number: 该规格资源可申请的最大数量。
        :type Number: int
        """
        self._NodeType = None
        self._Cpu = None
        self._Memory = None
        self._Number = None

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

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
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSpec(AbstractModel):
    """扩容容器资源时的资源描述

    """

    def __init__(self):
        r"""
        :param _ResourceProviderIdentifier: 外部资源提供者的标识符，例如"cls-a1cd23fa"。
        :type ResourceProviderIdentifier: str
        :param _ResourceProviderType: 外部资源提供者类型，例如"tke",当前仅支持"tke"。
        :type ResourceProviderType: str
        :param _NodeType: 资源的用途，即节点类型，当前仅支持"TASK"。
        :type NodeType: str
        :param _Cpu: CPU核数。
        :type Cpu: int
        :param _Memory: 内存大小，单位为GB。
        :type Memory: int
        :param _DataVolumes: 资源对宿主机的挂载点，指定的挂载点对应了宿主机的路径，该挂载点在Pod中作为数据存储目录使用。弃用
        :type DataVolumes: list of str
        :param _CpuType: Eks集群-CPU类型，当前支持"intel"和"amd"
        :type CpuType: str
        :param _PodVolumes: Pod节点数据目录挂载信息。
        :type PodVolumes: list of PodVolume
        :param _IsDynamicSpec: 是否浮动规格，1是，0否
        :type IsDynamicSpec: int
        :param _DynamicPodSpec: 浮动规格
注意：此字段可能返回 null，表示取不到有效值。
        :type DynamicPodSpec: :class:`tencentcloud.emr.v20190103.models.DynamicPodSpec`
        :param _VpcId: 代表vpc网络唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 代表vpc子网唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _PodName: pod name
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        """
        self._ResourceProviderIdentifier = None
        self._ResourceProviderType = None
        self._NodeType = None
        self._Cpu = None
        self._Memory = None
        self._DataVolumes = None
        self._CpuType = None
        self._PodVolumes = None
        self._IsDynamicSpec = None
        self._DynamicPodSpec = None
        self._VpcId = None
        self._SubnetId = None
        self._PodName = None

    @property
    def ResourceProviderIdentifier(self):
        return self._ResourceProviderIdentifier

    @ResourceProviderIdentifier.setter
    def ResourceProviderIdentifier(self, ResourceProviderIdentifier):
        self._ResourceProviderIdentifier = ResourceProviderIdentifier

    @property
    def ResourceProviderType(self):
        return self._ResourceProviderType

    @ResourceProviderType.setter
    def ResourceProviderType(self, ResourceProviderType):
        self._ResourceProviderType = ResourceProviderType

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

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
    def DataVolumes(self):
        return self._DataVolumes

    @DataVolumes.setter
    def DataVolumes(self, DataVolumes):
        self._DataVolumes = DataVolumes

    @property
    def CpuType(self):
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def PodVolumes(self):
        return self._PodVolumes

    @PodVolumes.setter
    def PodVolumes(self, PodVolumes):
        self._PodVolumes = PodVolumes

    @property
    def IsDynamicSpec(self):
        return self._IsDynamicSpec

    @IsDynamicSpec.setter
    def IsDynamicSpec(self, IsDynamicSpec):
        self._IsDynamicSpec = IsDynamicSpec

    @property
    def DynamicPodSpec(self):
        return self._DynamicPodSpec

    @DynamicPodSpec.setter
    def DynamicPodSpec(self, DynamicPodSpec):
        self._DynamicPodSpec = DynamicPodSpec

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
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName


    def _deserialize(self, params):
        self._ResourceProviderIdentifier = params.get("ResourceProviderIdentifier")
        self._ResourceProviderType = params.get("ResourceProviderType")
        self._NodeType = params.get("NodeType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._DataVolumes = params.get("DataVolumes")
        self._CpuType = params.get("CpuType")
        if params.get("PodVolumes") is not None:
            self._PodVolumes = []
            for item in params.get("PodVolumes"):
                obj = PodVolume()
                obj._deserialize(item)
                self._PodVolumes.append(obj)
        self._IsDynamicSpec = params.get("IsDynamicSpec")
        if params.get("DynamicPodSpec") is not None:
            self._DynamicPodSpec = DynamicPodSpec()
            self._DynamicPodSpec._deserialize(params.get("DynamicPodSpec"))
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSpecInfo(AbstractModel):
    """Pod相关信息

    """

    def __init__(self):
        r"""
        :param _PodSpec: 使用Pod资源扩容时，指定的Pod规格以及来源等信息
        :type PodSpec: :class:`tencentcloud.emr.v20190103.models.PodNewSpec`
        :param _PodParameter: POD自定义权限和自定义参数
        :type PodParameter: :class:`tencentcloud.emr.v20190103.models.PodNewParameter`
        """
        self._PodSpec = None
        self._PodParameter = None

    @property
    def PodSpec(self):
        return self._PodSpec

    @PodSpec.setter
    def PodSpec(self, PodSpec):
        self._PodSpec = PodSpec

    @property
    def PodParameter(self):
        return self._PodParameter

    @PodParameter.setter
    def PodParameter(self, PodParameter):
        self._PodParameter = PodParameter


    def _deserialize(self, params):
        if params.get("PodSpec") is not None:
            self._PodSpec = PodNewSpec()
            self._PodSpec._deserialize(params.get("PodSpec"))
        if params.get("PodParameter") is not None:
            self._PodParameter = PodNewParameter()
            self._PodParameter._deserialize(params.get("PodParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodState(AbstractModel):
    """单个pod状态

    """

    def __init__(self):
        r"""
        :param _Name: pod的名称
        :type Name: str
        :param _Uuid: pod uuid
        :type Uuid: str
        :param _State: pod的状态
        :type State: str
        :param _Reason: pod处于该状态原因
        :type Reason: str
        :param _OwnerCluster: pod所属集群
        :type OwnerCluster: str
        :param _Memory: pod内存大小
        :type Memory: int
        """
        self._Name = None
        self._Uuid = None
        self._State = None
        self._Reason = None
        self._OwnerCluster = None
        self._Memory = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uuid(self):
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def OwnerCluster(self):
        return self._OwnerCluster

    @OwnerCluster.setter
    def OwnerCluster(self, OwnerCluster):
        self._OwnerCluster = OwnerCluster

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Uuid = params.get("Uuid")
        self._State = params.get("State")
        self._Reason = params.get("Reason")
        self._OwnerCluster = params.get("OwnerCluster")
        self._Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodVolume(AbstractModel):
    """Pod的存储设备描述信息。

    """

    def __init__(self):
        r"""
        :param _VolumeType: 存储类型，可为"pvc"，"hostpath"。
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeType: str
        :param _PVCVolume: 当VolumeType为"pvc"时，该字段生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PVCVolume: :class:`tencentcloud.emr.v20190103.models.PersistentVolumeContext`
        :param _HostVolume: 当VolumeType为"hostpath"时，该字段生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type HostVolume: :class:`tencentcloud.emr.v20190103.models.HostVolumeContext`
        """
        self._VolumeType = None
        self._PVCVolume = None
        self._HostVolume = None

    @property
    def VolumeType(self):
        return self._VolumeType

    @VolumeType.setter
    def VolumeType(self, VolumeType):
        self._VolumeType = VolumeType

    @property
    def PVCVolume(self):
        return self._PVCVolume

    @PVCVolume.setter
    def PVCVolume(self, PVCVolume):
        self._PVCVolume = PVCVolume

    @property
    def HostVolume(self):
        return self._HostVolume

    @HostVolume.setter
    def HostVolume(self, HostVolume):
        self._HostVolume = HostVolume


    def _deserialize(self, params):
        self._VolumeType = params.get("VolumeType")
        if params.get("PVCVolume") is not None:
            self._PVCVolume = PersistentVolumeContext()
            self._PVCVolume._deserialize(params.get("PVCVolume"))
        if params.get("HostVolume") is not None:
            self._HostVolume = HostVolumeContext()
            self._HostVolume._deserialize(params.get("HostVolume"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreExecuteFileSettings(AbstractModel):
    """预执行脚本配置

    """

    def __init__(self):
        r"""
        :param _Path: 脚本在COS上路径，已废弃
        :type Path: str
        :param _Args: 执行脚本参数
        :type Args: list of str
        :param _Bucket: COS的Bucket名称，已废弃
        :type Bucket: str
        :param _Region: COS的Region名称，已废弃
        :type Region: str
        :param _Domain: COS的Domain数据，已废弃
        :type Domain: str
        :param _RunOrder: 执行顺序
        :type RunOrder: int
        :param _WhenRun: resourceAfter 或 clusterAfter
        :type WhenRun: str
        :param _CosFileName: 脚本文件名，已废弃
        :type CosFileName: str
        :param _CosFileURI: 脚本的cos地址
        :type CosFileURI: str
        :param _CosSecretId: cos的SecretId
        :type CosSecretId: str
        :param _CosSecretKey: Cos的SecretKey
        :type CosSecretKey: str
        :param _AppId: cos的appid，已废弃
        :type AppId: str
        """
        self._Path = None
        self._Args = None
        self._Bucket = None
        self._Region = None
        self._Domain = None
        self._RunOrder = None
        self._WhenRun = None
        self._CosFileName = None
        self._CosFileURI = None
        self._CosSecretId = None
        self._CosSecretKey = None
        self._AppId = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RunOrder(self):
        return self._RunOrder

    @RunOrder.setter
    def RunOrder(self, RunOrder):
        self._RunOrder = RunOrder

    @property
    def WhenRun(self):
        return self._WhenRun

    @WhenRun.setter
    def WhenRun(self, WhenRun):
        self._WhenRun = WhenRun

    @property
    def CosFileName(self):
        return self._CosFileName

    @CosFileName.setter
    def CosFileName(self, CosFileName):
        self._CosFileName = CosFileName

    @property
    def CosFileURI(self):
        return self._CosFileURI

    @CosFileURI.setter
    def CosFileURI(self, CosFileURI):
        self._CosFileURI = CosFileURI

    @property
    def CosSecretId(self):
        return self._CosSecretId

    @CosSecretId.setter
    def CosSecretId(self, CosSecretId):
        self._CosSecretId = CosSecretId

    @property
    def CosSecretKey(self):
        return self._CosSecretKey

    @CosSecretKey.setter
    def CosSecretKey(self, CosSecretKey):
        self._CosSecretKey = CosSecretKey

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Args = params.get("Args")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._Domain = params.get("Domain")
        self._RunOrder = params.get("RunOrder")
        self._WhenRun = params.get("WhenRun")
        self._CosFileName = params.get("CosFileName")
        self._CosFileURI = params.get("CosFileURI")
        self._CosSecretId = params.get("CosSecretId")
        self._CosSecretKey = params.get("CosSecretKey")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceDetail(AbstractModel):
    """价格详情

    """

    def __init__(self):
        r"""
        :param _ResourceId: 节点ID
        :type ResourceId: str
        :param _Formula: 价格计算公式
        :type Formula: str
        :param _OriginalCost: 原价
        :type OriginalCost: float
        :param _DiscountCost: 折扣价
        :type DiscountCost: float
        """
        self._ResourceId = None
        self._Formula = None
        self._OriginalCost = None
        self._DiscountCost = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Formula(self):
        return self._Formula

    @Formula.setter
    def Formula(self, Formula):
        self._Formula = Formula

    @property
    def OriginalCost(self):
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def DiscountCost(self):
        return self._DiscountCost

    @DiscountCost.setter
    def DiscountCost(self, DiscountCost):
        self._DiscountCost = DiscountCost


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Formula = params.get("Formula")
        self._OriginalCost = params.get("OriginalCost")
        self._DiscountCost = params.get("DiscountCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceResource(AbstractModel):
    """询价资源

    """

    def __init__(self):
        r"""
        :param _Spec: 需要的规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param _StorageType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param _DiskType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param _MemSize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _Cpu: 核心数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _MultiDisks: 云盘列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiDisks: list of MultiDisk
        :param _DiskCnt: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskCnt: int
        :param _InstanceType: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _DiskNum: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskNum: int
        :param _LocalDiskNum: 本地盘的数量
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDiskNum: int
        """
        self._Spec = None
        self._StorageType = None
        self._DiskType = None
        self._RootSize = None
        self._MemSize = None
        self._Cpu = None
        self._DiskSize = None
        self._MultiDisks = None
        self._DiskCnt = None
        self._InstanceType = None
        self._Tags = None
        self._DiskNum = None
        self._LocalDiskNum = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def RootSize(self):
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MultiDisks(self):
        return self._MultiDisks

    @MultiDisks.setter
    def MultiDisks(self, MultiDisks):
        self._MultiDisks = MultiDisks

    @property
    def DiskCnt(self):
        return self._DiskCnt

    @DiskCnt.setter
    def DiskCnt(self, DiskCnt):
        self._DiskCnt = DiskCnt

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DiskNum(self):
        return self._DiskNum

    @DiskNum.setter
    def DiskNum(self, DiskNum):
        self._DiskNum = DiskNum

    @property
    def LocalDiskNum(self):
        return self._LocalDiskNum

    @LocalDiskNum.setter
    def LocalDiskNum(self, LocalDiskNum):
        self._LocalDiskNum = LocalDiskNum


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._StorageType = params.get("StorageType")
        self._DiskType = params.get("DiskType")
        self._RootSize = params.get("RootSize")
        self._MemSize = params.get("MemSize")
        self._Cpu = params.get("Cpu")
        self._DiskSize = params.get("DiskSize")
        if params.get("MultiDisks") is not None:
            self._MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self._MultiDisks.append(obj)
        self._DiskCnt = params.get("DiskCnt")
        self._InstanceType = params.get("InstanceType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DiskNum = params.get("DiskNum")
        self._LocalDiskNum = params.get("LocalDiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaEntity(AbstractModel):
    """获取CVM配额

    """

    def __init__(self):
        r"""
        :param _UsedQuota: 已使用配额
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedQuota: int
        :param _RemainingQuota: 剩余配额
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainingQuota: int
        :param _TotalQuota: 总配额
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalQuota: int
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        """
        self._UsedQuota = None
        self._RemainingQuota = None
        self._TotalQuota = None
        self._Zone = None

    @property
    def UsedQuota(self):
        return self._UsedQuota

    @UsedQuota.setter
    def UsedQuota(self, UsedQuota):
        self._UsedQuota = UsedQuota

    @property
    def RemainingQuota(self):
        return self._RemainingQuota

    @RemainingQuota.setter
    def RemainingQuota(self, RemainingQuota):
        self._RemainingQuota = RemainingQuota

    @property
    def TotalQuota(self):
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._UsedQuota = params.get("UsedQuota")
        self._RemainingQuota = params.get("RemainingQuota")
        self._TotalQuota = params.get("TotalQuota")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstancesInfo(AbstractModel):
    """集群续费实例信息

    """

    def __init__(self):
        r"""
        :param _EmrResourceId: 节点资源ID
        :type EmrResourceId: str
        :param _Flag: 节点类型。0:common节点；1:master节点
；2:core节点；3:task节点
        :type Flag: int
        :param _Ip: 内网IP
        :type Ip: str
        :param _MemDesc: 节点内存描述
        :type MemDesc: str
        :param _CpuNum: 节点核数
        :type CpuNum: int
        :param _DiskSize: 硬盘大小
        :type DiskSize: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        :param _Spec: 节点规格
        :type Spec: str
        :param _StorageType: 磁盘类型
        :type StorageType: int
        """
        self._EmrResourceId = None
        self._Flag = None
        self._Ip = None
        self._MemDesc = None
        self._CpuNum = None
        self._DiskSize = None
        self._ExpireTime = None
        self._Spec = None
        self._StorageType = None

    @property
    def EmrResourceId(self):
        return self._EmrResourceId

    @EmrResourceId.setter
    def EmrResourceId(self, EmrResourceId):
        self._EmrResourceId = EmrResourceId

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MemDesc(self):
        return self._MemDesc

    @MemDesc.setter
    def MemDesc(self, MemDesc):
        self._MemDesc = MemDesc

    @property
    def CpuNum(self):
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._EmrResourceId = params.get("EmrResourceId")
        self._Flag = params.get("Flag")
        self._Ip = params.get("Ip")
        self._MemDesc = params.get("MemDesc")
        self._CpuNum = params.get("CpuNum")
        self._DiskSize = params.get("DiskSize")
        self._ExpireTime = params.get("ExpireTime")
        self._Spec = params.get("Spec")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resource(AbstractModel):
    """资源详情

    """

    def __init__(self):
        r"""
        :param _Spec: 节点规格描述，如CVM.SA2。
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param _StorageType: 存储类型
取值范围：
<li>4：表示云SSD。</li>
<li>5：表示高效云盘。</li>
<li>6：表示增强型SSD云硬盘。</li>
<li>11：表示吞吐型云硬盘。</li>
<li>12：表示极速型SSD云硬盘。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param _DiskType: 磁盘类型
取值范围：
<li>CLOUD_SSD：表示云SSD。</li>
<li>CLOUD_PREMIUM：表示高效云盘。</li>
<li>CLOUD_BASIC：表示云硬盘。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _MemSize: 内存容量,单位为M
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _Cpu: CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _DiskSize: 数据盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _RootSize: 系统盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param _MultiDisks: 云盘列表，当数据盘为一块云盘时，直接使用DiskType和DiskSize参数，超出部分使用MultiDisks
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiDisks: list of MultiDisk
        :param _Tags: 需要绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _InstanceType: 规格类型，如S2.MEDIUM8
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _LocalDiskNum: 本地盘数量，该字段已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDiskNum: int
        :param _DiskNum: 本地盘数量，如2
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskNum: int
        """
        self._Spec = None
        self._StorageType = None
        self._DiskType = None
        self._MemSize = None
        self._Cpu = None
        self._DiskSize = None
        self._RootSize = None
        self._MultiDisks = None
        self._Tags = None
        self._InstanceType = None
        self._LocalDiskNum = None
        self._DiskNum = None

    @property
    def Spec(self):
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def RootSize(self):
        return self._RootSize

    @RootSize.setter
    def RootSize(self, RootSize):
        self._RootSize = RootSize

    @property
    def MultiDisks(self):
        return self._MultiDisks

    @MultiDisks.setter
    def MultiDisks(self, MultiDisks):
        self._MultiDisks = MultiDisks

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def LocalDiskNum(self):
        return self._LocalDiskNum

    @LocalDiskNum.setter
    def LocalDiskNum(self, LocalDiskNum):
        self._LocalDiskNum = LocalDiskNum

    @property
    def DiskNum(self):
        return self._DiskNum

    @DiskNum.setter
    def DiskNum(self, DiskNum):
        self._DiskNum = DiskNum


    def _deserialize(self, params):
        self._Spec = params.get("Spec")
        self._StorageType = params.get("StorageType")
        self._DiskType = params.get("DiskType")
        self._MemSize = params.get("MemSize")
        self._Cpu = params.get("Cpu")
        self._DiskSize = params.get("DiskSize")
        self._RootSize = params.get("RootSize")
        if params.get("MultiDisks") is not None:
            self._MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self._MultiDisks.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceType = params.get("InstanceType")
        self._LocalDiskNum = params.get("LocalDiskNum")
        self._DiskNum = params.get("DiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobFlowRequest(AbstractModel):
    """RunJobFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 作业名称。
        :type Name: str
        :param _CreateCluster: 是否新创建集群。
true，新创建集群，则使用Instance中的参数进行集群创建。
false，使用已有集群，则通过InstanceId传入。
        :type CreateCluster: bool
        :param _Steps: 作业流程执行步骤。
        :type Steps: list of Step
        :param _InstancePolicy: 作业流程正常完成时，集群的处理方式，可选择:
Terminate 销毁集群。
Reserve 保留集群。
        :type InstancePolicy: str
        :param _ProductVersion: 只有CreateCluster为true时生效，目前只支持EMR版本，例如EMR-2.2.0，不支持ClickHouse和Druid版本。
        :type ProductVersion: str
        :param _SecurityClusterFlag: 只在CreateCluster为true时生效。
true 表示安装kerberos，false表示不安装kerberos。
        :type SecurityClusterFlag: bool
        :param _Software: 只在CreateCluster为true时生效。
新建集群时，要安装的软件列表。
        :type Software: list of str
        :param _BootstrapActions: 引导脚本。
        :type BootstrapActions: list of BootstrapAction
        :param _Configurations: 指定配置创建集群。
        :type Configurations: list of Configuration
        :param _LogUri: 作业日志保存地址。
        :type LogUri: str
        :param _InstanceId: 只在CreateCluster为false时生效。
        :type InstanceId: str
        :param _ApplicationRole: 自定义应用角色，大数据应用访问外部服务时使用的角色，默认为"EME_QCSRole"。
        :type ApplicationRole: str
        :param _ClientToken: 重入标签，用来可重入检查，防止在一段时间内，创建相同的流程作业。
        :type ClientToken: str
        :param _Instance: 只在CreateCluster为true时生效，使用该配置创建集群。
        :type Instance: :class:`tencentcloud.emr.v20190103.models.ClusterSetting`
        """
        self._Name = None
        self._CreateCluster = None
        self._Steps = None
        self._InstancePolicy = None
        self._ProductVersion = None
        self._SecurityClusterFlag = None
        self._Software = None
        self._BootstrapActions = None
        self._Configurations = None
        self._LogUri = None
        self._InstanceId = None
        self._ApplicationRole = None
        self._ClientToken = None
        self._Instance = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateCluster(self):
        return self._CreateCluster

    @CreateCluster.setter
    def CreateCluster(self, CreateCluster):
        self._CreateCluster = CreateCluster

    @property
    def Steps(self):
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

    @property
    def InstancePolicy(self):
        return self._InstancePolicy

    @InstancePolicy.setter
    def InstancePolicy(self, InstancePolicy):
        self._InstancePolicy = InstancePolicy

    @property
    def ProductVersion(self):
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def SecurityClusterFlag(self):
        return self._SecurityClusterFlag

    @SecurityClusterFlag.setter
    def SecurityClusterFlag(self, SecurityClusterFlag):
        self._SecurityClusterFlag = SecurityClusterFlag

    @property
    def Software(self):
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def BootstrapActions(self):
        return self._BootstrapActions

    @BootstrapActions.setter
    def BootstrapActions(self, BootstrapActions):
        self._BootstrapActions = BootstrapActions

    @property
    def Configurations(self):
        return self._Configurations

    @Configurations.setter
    def Configurations(self, Configurations):
        self._Configurations = Configurations

    @property
    def LogUri(self):
        return self._LogUri

    @LogUri.setter
    def LogUri(self, LogUri):
        self._LogUri = LogUri

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ApplicationRole(self):
        return self._ApplicationRole

    @ApplicationRole.setter
    def ApplicationRole(self, ApplicationRole):
        self._ApplicationRole = ApplicationRole

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Instance(self):
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CreateCluster = params.get("CreateCluster")
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = Step()
                obj._deserialize(item)
                self._Steps.append(obj)
        self._InstancePolicy = params.get("InstancePolicy")
        self._ProductVersion = params.get("ProductVersion")
        self._SecurityClusterFlag = params.get("SecurityClusterFlag")
        self._Software = params.get("Software")
        if params.get("BootstrapActions") is not None:
            self._BootstrapActions = []
            for item in params.get("BootstrapActions"):
                obj = BootstrapAction()
                obj._deserialize(item)
                self._BootstrapActions.append(obj)
        if params.get("Configurations") is not None:
            self._Configurations = []
            for item in params.get("Configurations"):
                obj = Configuration()
                obj._deserialize(item)
                self._Configurations.append(obj)
        self._LogUri = params.get("LogUri")
        self._InstanceId = params.get("InstanceId")
        self._ApplicationRole = params.get("ApplicationRole")
        self._ClientToken = params.get("ClientToken")
        if params.get("Instance") is not None:
            self._Instance = ClusterSetting()
            self._Instance._deserialize(params.get("Instance"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobFlowResponse(AbstractModel):
    """RunJobFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobFlowId: 作业流程ID。
        :type JobFlowId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobFlowId = None
        self._RequestId = None

    @property
    def JobFlowId(self):
        return self._JobFlowId

    @JobFlowId.setter
    def JobFlowId(self, JobFlowId):
        self._JobFlowId = JobFlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobFlowId = params.get("JobFlowId")
        self._RequestId = params.get("RequestId")


class ScaleOutClusterRequest(AbstractModel):
    """ScaleOutCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 节点计费模式。取值范围：
<li>PREPAID：预付费，即包年包月。</li>
<li>POSTPAID_BY_HOUR：按小时后付费。</li>
<li>SPOTPAID：竞价付费（仅支持TASK节点）。</li>
        :type InstanceChargeType: str
        :param _InstanceId: 集群实例ID。
        :type InstanceId: str
        :param _ScaleOutNodeConfig: 扩容节点类型以及数量
        :type ScaleOutNodeConfig: :class:`tencentcloud.emr.v20190103.models.ScaleOutNodeConfig`
        :param _ClientToken: 唯一随机标识，时效5分钟，需要调用者指定 防止客户端重新创建资源，例如 a9a90aa6-751a-41b6-aad6-fae36063280
        :type ClientToken: str
        :param _InstanceChargePrepaid: 即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`
        :param _ScriptBootstrapActionConfig: [引导操作](https://cloud.tencent.com/document/product/589/35656)脚本设置。
        :type ScriptBootstrapActionConfig: list of ScriptBootstrapActionConfig
        :param _SoftDeployInfo: 扩容部署服务，新增节点将默认继承当前节点类型中所部署服务，部署服务含默认可选服务，该参数仅支持可选服务填写，如：存量task节点已部署HDFS、YARN、impala；使用api扩容task节不部署impala时，此参数仅填写HDFS、YARN
        :type SoftDeployInfo: list of int
        :param _ServiceNodeInfo: 部署进程，默认部署扩容服务的全部进程，支持修改部署进程，如：当前task节点部署服务为：HDFS、YARN、impala，默认部署服务为：DataNode,NodeManager,ImpalaServer，若用户需修改部署进程信息，此参数信息可填写：	DataNode,NodeManager,ImpalaServerCoordinator或DataNode,NodeManager,ImpalaServerExecutor
        :type ServiceNodeInfo: list of int
        :param _DisasterRecoverGroupIds: 分散置放群组ID列表，当前只支持指定一个。
该参数可以通过调用 [DescribeDisasterRecoverGroups](https://cloud.tencent.com/document/product/213/17810)的返回值中的DisasterRecoverGroupId字段来获取。
        :type DisasterRecoverGroupIds: list of str
        :param _Tags: 扩容节点绑定标签列表。
        :type Tags: list of Tag
        :param _HardwareSourceType: 扩容所选资源类型，可选范围为"host","pod"，host为普通的CVM资源，Pod为TKE集群或EKS集群提供的资源
        :type HardwareSourceType: str
        :param _PodSpecInfo: Pod相关资源信息
        :type PodSpecInfo: :class:`tencentcloud.emr.v20190103.models.PodSpecInfo`
        :param _ClickHouseClusterName: 使用clickhouse集群扩容时，选择的机器分组名称
        :type ClickHouseClusterName: str
        :param _ClickHouseClusterType: 使用clickhouse集群扩容时，选择的机器分组类型。new为新增，old为选择旧分组
        :type ClickHouseClusterType: str
        :param _YarnNodeLabel: 扩容指定 Yarn Node Label
        :type YarnNodeLabel: str
        :param _EnableStartServiceFlag: 扩容后是否启动服务，默认取值否
<li>true：是</li>
<li>false：否</li>
        :type EnableStartServiceFlag: bool
        :param _ResourceSpec: 规格设置
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeResourceSpec`
        :param _Zone: 实例所属的可用区，例如ap-guangzhou-1。该参数也可以通过调用[DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param _SubnetId: 子网，默认是集群创建时的子网
        :type SubnetId: str
        """
        self._InstanceChargeType = None
        self._InstanceId = None
        self._ScaleOutNodeConfig = None
        self._ClientToken = None
        self._InstanceChargePrepaid = None
        self._ScriptBootstrapActionConfig = None
        self._SoftDeployInfo = None
        self._ServiceNodeInfo = None
        self._DisasterRecoverGroupIds = None
        self._Tags = None
        self._HardwareSourceType = None
        self._PodSpecInfo = None
        self._ClickHouseClusterName = None
        self._ClickHouseClusterType = None
        self._YarnNodeLabel = None
        self._EnableStartServiceFlag = None
        self._ResourceSpec = None
        self._Zone = None
        self._SubnetId = None

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ScaleOutNodeConfig(self):
        return self._ScaleOutNodeConfig

    @ScaleOutNodeConfig.setter
    def ScaleOutNodeConfig(self, ScaleOutNodeConfig):
        self._ScaleOutNodeConfig = ScaleOutNodeConfig

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def ScriptBootstrapActionConfig(self):
        return self._ScriptBootstrapActionConfig

    @ScriptBootstrapActionConfig.setter
    def ScriptBootstrapActionConfig(self, ScriptBootstrapActionConfig):
        self._ScriptBootstrapActionConfig = ScriptBootstrapActionConfig

    @property
    def SoftDeployInfo(self):
        return self._SoftDeployInfo

    @SoftDeployInfo.setter
    def SoftDeployInfo(self, SoftDeployInfo):
        self._SoftDeployInfo = SoftDeployInfo

    @property
    def ServiceNodeInfo(self):
        return self._ServiceNodeInfo

    @ServiceNodeInfo.setter
    def ServiceNodeInfo(self, ServiceNodeInfo):
        self._ServiceNodeInfo = ServiceNodeInfo

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HardwareSourceType(self):
        return self._HardwareSourceType

    @HardwareSourceType.setter
    def HardwareSourceType(self, HardwareSourceType):
        self._HardwareSourceType = HardwareSourceType

    @property
    def PodSpecInfo(self):
        return self._PodSpecInfo

    @PodSpecInfo.setter
    def PodSpecInfo(self, PodSpecInfo):
        self._PodSpecInfo = PodSpecInfo

    @property
    def ClickHouseClusterName(self):
        return self._ClickHouseClusterName

    @ClickHouseClusterName.setter
    def ClickHouseClusterName(self, ClickHouseClusterName):
        self._ClickHouseClusterName = ClickHouseClusterName

    @property
    def ClickHouseClusterType(self):
        return self._ClickHouseClusterType

    @ClickHouseClusterType.setter
    def ClickHouseClusterType(self, ClickHouseClusterType):
        self._ClickHouseClusterType = ClickHouseClusterType

    @property
    def YarnNodeLabel(self):
        return self._YarnNodeLabel

    @YarnNodeLabel.setter
    def YarnNodeLabel(self, YarnNodeLabel):
        self._YarnNodeLabel = YarnNodeLabel

    @property
    def EnableStartServiceFlag(self):
        return self._EnableStartServiceFlag

    @EnableStartServiceFlag.setter
    def EnableStartServiceFlag(self, EnableStartServiceFlag):
        self._EnableStartServiceFlag = EnableStartServiceFlag

    @property
    def ResourceSpec(self):
        return self._ResourceSpec

    @ResourceSpec.setter
    def ResourceSpec(self, ResourceSpec):
        self._ResourceSpec = ResourceSpec

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._InstanceId = params.get("InstanceId")
        if params.get("ScaleOutNodeConfig") is not None:
            self._ScaleOutNodeConfig = ScaleOutNodeConfig()
            self._ScaleOutNodeConfig._deserialize(params.get("ScaleOutNodeConfig"))
        self._ClientToken = params.get("ClientToken")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("ScriptBootstrapActionConfig") is not None:
            self._ScriptBootstrapActionConfig = []
            for item in params.get("ScriptBootstrapActionConfig"):
                obj = ScriptBootstrapActionConfig()
                obj._deserialize(item)
                self._ScriptBootstrapActionConfig.append(obj)
        self._SoftDeployInfo = params.get("SoftDeployInfo")
        self._ServiceNodeInfo = params.get("ServiceNodeInfo")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HardwareSourceType = params.get("HardwareSourceType")
        if params.get("PodSpecInfo") is not None:
            self._PodSpecInfo = PodSpecInfo()
            self._PodSpecInfo._deserialize(params.get("PodSpecInfo"))
        self._ClickHouseClusterName = params.get("ClickHouseClusterName")
        self._ClickHouseClusterType = params.get("ClickHouseClusterType")
        self._YarnNodeLabel = params.get("YarnNodeLabel")
        self._EnableStartServiceFlag = params.get("EnableStartServiceFlag")
        if params.get("ResourceSpec") is not None:
            self._ResourceSpec = NodeResourceSpec()
            self._ResourceSpec._deserialize(params.get("ResourceSpec"))
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutClusterResponse(AbstractModel):
    """ScaleOutCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _ClientToken: 客户端Token。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientToken: str
        :param _FlowId: 扩容流程ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._ClientToken = None
        self._FlowId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClientToken = params.get("ClientToken")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeUnit: 扩容的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param _TimeSpan: 扩容的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param _ClientToken: 客户端Token。
        :type ClientToken: str
        :param _PreExecutedFileSettings: 引导操作脚本设置。
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param _TaskCount: 扩容的Task节点数量。
        :type TaskCount: int
        :param _CoreCount: 扩容的Core节点数量。
        :type CoreCount: int
        :param _UnNecessaryNodeList: 扩容时不需要安装的进程。
        :type UnNecessaryNodeList: list of int non-negative
        :param _RouterCount: 扩容的Router节点数量。
        :type RouterCount: int
        :param _SoftDeployInfo: 部署的服务。
<li>SoftDeployInfo和ServiceNodeInfo是同组参数，和UnNecessaryNodeList参数互斥。</li>
<li>建议使用SoftDeployInfo和ServiceNodeInfo组合。</li>
        :type SoftDeployInfo: list of int non-negative
        :param _ServiceNodeInfo: 启动的进程。
        :type ServiceNodeInfo: list of int non-negative
        :param _DisasterRecoverGroupIds: 分散置放群组ID列表，当前仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param _Tags: 扩容节点绑定标签列表。
        :type Tags: list of Tag
        :param _HardwareResourceType: 扩容所选资源类型，可选范围为"host","pod"，host为普通的CVM资源，Pod为TKE集群或EKS集群提供的资源
        :type HardwareResourceType: str
        :param _PodSpec: 使用Pod资源扩容时，指定的Pod规格以及来源等信息
        :type PodSpec: :class:`tencentcloud.emr.v20190103.models.PodSpec`
        :param _ClickHouseClusterName: 使用clickhouse集群扩容时，选择的机器分组名称
        :type ClickHouseClusterName: str
        :param _ClickHouseClusterType: 使用clickhouse集群扩容时，选择的机器分组类型。new为新增，old为选择旧分组
        :type ClickHouseClusterType: str
        :param _YarnNodeLabel: 规则扩容指定 yarn node label
        :type YarnNodeLabel: str
        :param _PodParameter: POD自定义权限和自定义参数
        :type PodParameter: :class:`tencentcloud.emr.v20190103.models.PodParameter`
        :param _MasterCount: 扩容的Master节点的数量。
使用clickhouse集群扩容时，该参数不生效。
使用kafka集群扩容时，该参数不生效。
当HardwareResourceType=POD时，该参数不生效。
        :type MasterCount: int
        :param _StartServiceAfterScaleOut: 扩容后是否启动服务，true：启动，false：不启动
        :type StartServiceAfterScaleOut: str
        :param _ZoneId: 可用区，默认是集群的主可用区
        :type ZoneId: int
        :param _SubnetId: 子网，默认是集群创建时的子网
        :type SubnetId: str
        :param _ScaleOutServiceConfAssign: 预设配置组
        :type ScaleOutServiceConfAssign: str
        :param _AutoRenew: 0表示关闭自动续费，1表示开启自动续费
        :type AutoRenew: int
        """
        self._TimeUnit = None
        self._TimeSpan = None
        self._InstanceId = None
        self._PayMode = None
        self._ClientToken = None
        self._PreExecutedFileSettings = None
        self._TaskCount = None
        self._CoreCount = None
        self._UnNecessaryNodeList = None
        self._RouterCount = None
        self._SoftDeployInfo = None
        self._ServiceNodeInfo = None
        self._DisasterRecoverGroupIds = None
        self._Tags = None
        self._HardwareResourceType = None
        self._PodSpec = None
        self._ClickHouseClusterName = None
        self._ClickHouseClusterType = None
        self._YarnNodeLabel = None
        self._PodParameter = None
        self._MasterCount = None
        self._StartServiceAfterScaleOut = None
        self._ZoneId = None
        self._SubnetId = None
        self._ScaleOutServiceConfAssign = None
        self._AutoRenew = None

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def PreExecutedFileSettings(self):
        return self._PreExecutedFileSettings

    @PreExecutedFileSettings.setter
    def PreExecutedFileSettings(self, PreExecutedFileSettings):
        self._PreExecutedFileSettings = PreExecutedFileSettings

    @property
    def TaskCount(self):
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def CoreCount(self):
        return self._CoreCount

    @CoreCount.setter
    def CoreCount(self, CoreCount):
        self._CoreCount = CoreCount

    @property
    def UnNecessaryNodeList(self):
        return self._UnNecessaryNodeList

    @UnNecessaryNodeList.setter
    def UnNecessaryNodeList(self, UnNecessaryNodeList):
        self._UnNecessaryNodeList = UnNecessaryNodeList

    @property
    def RouterCount(self):
        return self._RouterCount

    @RouterCount.setter
    def RouterCount(self, RouterCount):
        self._RouterCount = RouterCount

    @property
    def SoftDeployInfo(self):
        return self._SoftDeployInfo

    @SoftDeployInfo.setter
    def SoftDeployInfo(self, SoftDeployInfo):
        self._SoftDeployInfo = SoftDeployInfo

    @property
    def ServiceNodeInfo(self):
        return self._ServiceNodeInfo

    @ServiceNodeInfo.setter
    def ServiceNodeInfo(self, ServiceNodeInfo):
        self._ServiceNodeInfo = ServiceNodeInfo

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HardwareResourceType(self):
        return self._HardwareResourceType

    @HardwareResourceType.setter
    def HardwareResourceType(self, HardwareResourceType):
        self._HardwareResourceType = HardwareResourceType

    @property
    def PodSpec(self):
        return self._PodSpec

    @PodSpec.setter
    def PodSpec(self, PodSpec):
        self._PodSpec = PodSpec

    @property
    def ClickHouseClusterName(self):
        return self._ClickHouseClusterName

    @ClickHouseClusterName.setter
    def ClickHouseClusterName(self, ClickHouseClusterName):
        self._ClickHouseClusterName = ClickHouseClusterName

    @property
    def ClickHouseClusterType(self):
        return self._ClickHouseClusterType

    @ClickHouseClusterType.setter
    def ClickHouseClusterType(self, ClickHouseClusterType):
        self._ClickHouseClusterType = ClickHouseClusterType

    @property
    def YarnNodeLabel(self):
        return self._YarnNodeLabel

    @YarnNodeLabel.setter
    def YarnNodeLabel(self, YarnNodeLabel):
        self._YarnNodeLabel = YarnNodeLabel

    @property
    def PodParameter(self):
        return self._PodParameter

    @PodParameter.setter
    def PodParameter(self, PodParameter):
        self._PodParameter = PodParameter

    @property
    def MasterCount(self):
        return self._MasterCount

    @MasterCount.setter
    def MasterCount(self, MasterCount):
        self._MasterCount = MasterCount

    @property
    def StartServiceAfterScaleOut(self):
        return self._StartServiceAfterScaleOut

    @StartServiceAfterScaleOut.setter
    def StartServiceAfterScaleOut(self, StartServiceAfterScaleOut):
        self._StartServiceAfterScaleOut = StartServiceAfterScaleOut

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ScaleOutServiceConfAssign(self):
        return self._ScaleOutServiceConfAssign

    @ScaleOutServiceConfAssign.setter
    def ScaleOutServiceConfAssign(self, ScaleOutServiceConfAssign):
        self._ScaleOutServiceConfAssign = ScaleOutServiceConfAssign

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew


    def _deserialize(self, params):
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._InstanceId = params.get("InstanceId")
        self._PayMode = params.get("PayMode")
        self._ClientToken = params.get("ClientToken")
        if params.get("PreExecutedFileSettings") is not None:
            self._PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self._PreExecutedFileSettings.append(obj)
        self._TaskCount = params.get("TaskCount")
        self._CoreCount = params.get("CoreCount")
        self._UnNecessaryNodeList = params.get("UnNecessaryNodeList")
        self._RouterCount = params.get("RouterCount")
        self._SoftDeployInfo = params.get("SoftDeployInfo")
        self._ServiceNodeInfo = params.get("ServiceNodeInfo")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HardwareResourceType = params.get("HardwareResourceType")
        if params.get("PodSpec") is not None:
            self._PodSpec = PodSpec()
            self._PodSpec._deserialize(params.get("PodSpec"))
        self._ClickHouseClusterName = params.get("ClickHouseClusterName")
        self._ClickHouseClusterType = params.get("ClickHouseClusterType")
        self._YarnNodeLabel = params.get("YarnNodeLabel")
        if params.get("PodParameter") is not None:
            self._PodParameter = PodParameter()
            self._PodParameter._deserialize(params.get("PodParameter"))
        self._MasterCount = params.get("MasterCount")
        self._StartServiceAfterScaleOut = params.get("StartServiceAfterScaleOut")
        self._ZoneId = params.get("ZoneId")
        self._SubnetId = params.get("SubnetId")
        self._ScaleOutServiceConfAssign = params.get("ScaleOutServiceConfAssign")
        self._AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _DealNames: 订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param _ClientToken: 客户端Token。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientToken: str
        :param _FlowId: 扩容流程ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _BillId: 大订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type BillId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._DealNames = None
        self._ClientToken = None
        self._FlowId = None
        self._BillId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def BillId(self):
        return self._BillId

    @BillId.setter
    def BillId(self, BillId):
        self._BillId = BillId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DealNames = params.get("DealNames")
        self._ClientToken = params.get("ClientToken")
        self._FlowId = params.get("FlowId")
        self._BillId = params.get("BillId")
        self._RequestId = params.get("RequestId")


class ScaleOutNodeConfig(AbstractModel):
    """扩容节点类型以及数量

    """

    def __init__(self):
        r"""
        :param _NodeFlag: 扩容节点类型取值范围：
  <li>MASTER</li>
  <li>TASK</li>
  <li>CORE</li>
  <li>ROUTER</li>
        :type NodeFlag: str
        :param _NodeCount: 扩容节点数量
        :type NodeCount: int
        """
        self._NodeFlag = None
        self._NodeCount = None

    @property
    def NodeFlag(self):
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount


    def _deserialize(self, params):
        self._NodeFlag = params.get("NodeFlag")
        self._NodeCount = params.get("NodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneSoftwareConfig(AbstractModel):
    """集群应用场景以及支持部署组件信息

    """

    def __init__(self):
        r"""
        :param _Software: 部署的组件列表。不同的EMR产品版本ProductVersion 对应不同可选组件列表，不同产品版本可选组件列表查询：[组件版本](https://cloud.tencent.com/document/product/589/20279) ；
填写实例值：hive、flink。
        :type Software: list of str
        :param _SceneName: 默认Hadoop-Default,[场景查询](https://cloud.tencent.com/document/product/589/14624)场景化取值范围：
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
Hadoop-Default
        :type SceneName: str
        """
        self._Software = None
        self._SceneName = None

    @property
    def Software(self):
        return self._Software

    @Software.setter
    def Software(self, Software):
        self._Software = Software

    @property
    def SceneName(self):
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName


    def _deserialize(self, params):
        self._Software = params.get("Software")
        self._SceneName = params.get("SceneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScriptBootstrapActionConfig(AbstractModel):
    """添加引导操作

    """

    def __init__(self):
        r"""
        :param _CosFileURI: 脚本的cos地址，参照格式：https://beijing-111111.cos.ap-beijing.myqcloud.com/data/test.sh查询cos存储桶列表：[存储桶列表](https://console.cloud.tencent.com/cos/bucket)
        :type CosFileURI: str
        :param _ExecutionMoment: 引导脚步执行时机范围
<li>resourceAfter：节点初始化后</li>
<li>clusterAfter：集群启动后</li>
<li>clusterBefore：集群启动前</li>
        :type ExecutionMoment: str
        :param _Args: 执行脚本参数，参数格式请遵循标准Shell规范
        :type Args: list of str
        :param _CosFileName: 脚本文件名
        :type CosFileName: str
        """
        self._CosFileURI = None
        self._ExecutionMoment = None
        self._Args = None
        self._CosFileName = None

    @property
    def CosFileURI(self):
        return self._CosFileURI

    @CosFileURI.setter
    def CosFileURI(self, CosFileURI):
        self._CosFileURI = CosFileURI

    @property
    def ExecutionMoment(self):
        return self._ExecutionMoment

    @ExecutionMoment.setter
    def ExecutionMoment(self, ExecutionMoment):
        self._ExecutionMoment = ExecutionMoment

    @property
    def Args(self):
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def CosFileName(self):
        return self._CosFileName

    @CosFileName.setter
    def CosFileName(self, CosFileName):
        self._CosFileName = CosFileName


    def _deserialize(self, params):
        self._CosFileURI = params.get("CosFileURI")
        self._ExecutionMoment = params.get("ExecutionMoment")
        self._Args = params.get("Args")
        self._CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchItem(AbstractModel):
    """搜索字段

    """

    def __init__(self):
        r"""
        :param _SearchType: 支持搜索的类型
        :type SearchType: str
        :param _SearchValue: 支持搜索的值
        :type SearchValue: str
        """
        self._SearchType = None
        self._SearchValue = None

    @property
    def SearchType(self):
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def SearchValue(self):
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._SearchType = params.get("SearchType")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceBasicRestartInfo(AbstractModel):
    """操作的服务范围

    """

    def __init__(self):
        r"""
        :param _ServiceName: 服务名，必填，如HDFS
        :type ServiceName: str
        :param _ComponentInfoList: 如果没传，则表示所有进程
        :type ComponentInfoList: list of ComponentBasicRestartInfo
        """
        self._ServiceName = None
        self._ComponentInfoList = None

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ComponentInfoList(self):
        return self._ComponentInfoList

    @ComponentInfoList.setter
    def ComponentInfoList(self, ComponentInfoList):
        self._ComponentInfoList = ComponentInfoList


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        if params.get("ComponentInfoList") is not None:
            self._ComponentInfoList = []
            for item in params.get("ComponentInfoList"):
                obj = ComponentBasicRestartInfo()
                obj._deserialize(item)
                self._ComponentInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShortNodeInfo(AbstractModel):
    """节点信息

    """

    def __init__(self):
        r"""
        :param _NodeType: 节点类型，Master/Core/Task/Router/Common
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param _NodeSize: 节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSize: int
        """
        self._NodeType = None
        self._NodeSize = None

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeSize(self):
        return self._NodeSize

    @NodeSize.setter
    def NodeSize(self, NodeSize):
        self._NodeSize = NodeSize


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._NodeSize = params.get("NodeSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SoftDependInfo(AbstractModel):
    """体外客户端组件依赖信息

    """

    def __init__(self):
        r"""
        :param _SoftName: 组件名称
        :type SoftName: str
        :param _Required: 是否必选
        :type Required: bool
        """
        self._SoftName = None
        self._Required = None

    @property
    def SoftName(self):
        return self._SoftName

    @SoftName.setter
    def SoftName(self, SoftName):
        self._SoftName = SoftName

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required


    def _deserialize(self, params):
        self._SoftName = params.get("SoftName")
        self._Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStopServiceOrMonitorRequest(AbstractModel):
    """StartStopServiceOrMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _OpType: 操作类型，当前支持
<li>StartService：启动服务</li>
<li>StopService：停止服务</li>
<li>StartMonitor：退出维护</li>
<li>StopMonitor：进入维护</li>
<li>RestartService：重启服务 如果操作类型选择重启服务 StrategyConfig操作策略则是必填项</li>
        :type OpType: str
        :param _OpScope: 操作范围
        :type OpScope: :class:`tencentcloud.emr.v20190103.models.OpScope`
        :param _StrategyConfig: 操作策略
        :type StrategyConfig: :class:`tencentcloud.emr.v20190103.models.StrategyConfig`
        """
        self._InstanceId = None
        self._OpType = None
        self._OpScope = None
        self._StrategyConfig = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OpType(self):
        return self._OpType

    @OpType.setter
    def OpType(self, OpType):
        self._OpType = OpType

    @property
    def OpScope(self):
        return self._OpScope

    @OpScope.setter
    def OpScope(self, OpScope):
        self._OpScope = OpScope

    @property
    def StrategyConfig(self):
        return self._StrategyConfig

    @StrategyConfig.setter
    def StrategyConfig(self, StrategyConfig):
        self._StrategyConfig = StrategyConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OpType = params.get("OpType")
        if params.get("OpScope") is not None:
            self._OpScope = OpScope()
            self._OpScope._deserialize(params.get("OpScope"))
        if params.get("StrategyConfig") is not None:
            self._StrategyConfig = StrategyConfig()
            self._StrategyConfig._deserialize(params.get("StrategyConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStopServiceOrMonitorResponse(AbstractModel):
    """StartStopServiceOrMonitor返回参数结构体

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


class Step(AbstractModel):
    """执行步骤

    """

    def __init__(self):
        r"""
        :param _Name: 执行步骤名称。
        :type Name: str
        :param _ExecutionStep: 执行动作。
        :type ExecutionStep: :class:`tencentcloud.emr.v20190103.models.Execution`
        :param _ActionOnFailure: 执行失败策略。
1. TERMINATE_CLUSTER 执行失败时退出并销毁集群。
2. CONTINUE 执行失败时跳过并执行后续步骤。
        :type ActionOnFailure: str
        :param _User: 指定执行Step时的用户名，非必须，默认为hadoop。
        :type User: str
        """
        self._Name = None
        self._ExecutionStep = None
        self._ActionOnFailure = None
        self._User = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ExecutionStep(self):
        return self._ExecutionStep

    @ExecutionStep.setter
    def ExecutionStep(self, ExecutionStep):
        self._ExecutionStep = ExecutionStep

    @property
    def ActionOnFailure(self):
        return self._ActionOnFailure

    @ActionOnFailure.setter
    def ActionOnFailure(self, ActionOnFailure):
        self._ActionOnFailure = ActionOnFailure

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("ExecutionStep") is not None:
            self._ExecutionStep = Execution()
            self._ExecutionStep._deserialize(params.get("ExecutionStep"))
        self._ActionOnFailure = params.get("ActionOnFailure")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StrategyConfig(AbstractModel):
    """重启/停止/启动服务/监控的配置

    """

    def __init__(self):
        r"""
        :param _RollingRestartSwitch: 0:关闭滚动重启
1:开启滚动启动
注意：此字段可能返回 null，表示取不到有效值。
        :type RollingRestartSwitch: int
        :param _BatchSize: 滚动重启每批次的重启数量，最大重启台数为 99999 台
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchSize: int
        :param _TimeWait: 滚动重启每批停止等待时间 ,最大间隔为 5 分钟 单位是秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeWait: int
        :param _DealOnFail: 操作失败处理策略，0:失败阻塞, 1:失败自动跳过
注意：此字段可能返回 null，表示取不到有效值。
        :type DealOnFail: int
        """
        self._RollingRestartSwitch = None
        self._BatchSize = None
        self._TimeWait = None
        self._DealOnFail = None

    @property
    def RollingRestartSwitch(self):
        return self._RollingRestartSwitch

    @RollingRestartSwitch.setter
    def RollingRestartSwitch(self, RollingRestartSwitch):
        self._RollingRestartSwitch = RollingRestartSwitch

    @property
    def BatchSize(self):
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def TimeWait(self):
        return self._TimeWait

    @TimeWait.setter
    def TimeWait(self, TimeWait):
        self._TimeWait = TimeWait

    @property
    def DealOnFail(self):
        return self._DealOnFail

    @DealOnFail.setter
    def DealOnFail(self, DealOnFail):
        self._DealOnFail = DealOnFail


    def _deserialize(self, params):
        self._RollingRestartSwitch = params.get("RollingRestartSwitch")
        self._BatchSize = params.get("BatchSize")
        self._TimeWait = params.get("TimeWait")
        self._DealOnFail = params.get("DealOnFail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetInfo(AbstractModel):
    """子网信息

    """

    def __init__(self):
        r"""
        :param _SubnetName: 子网信息（名字）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param _SubnetId: 子网信息（ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self._SubnetName = None
        self._SubnetId = None

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._SubnetName = params.get("SubnetName")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPodStateRequest(AbstractModel):
    """SyncPodState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Message: EmrService中pod状态信息
        :type Message: :class:`tencentcloud.emr.v20190103.models.PodState`
        """
        self._Message = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        if params.get("Message") is not None:
            self._Message = PodState()
            self._Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPodStateResponse(AbstractModel):
    """SyncPodState返回参数结构体

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


class Tag(AbstractModel):
    """标签

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
        


class TerminateClusterNodesRequest(AbstractModel):
    """TerminateClusterNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _CvmInstanceIds: 销毁资源列表
        :type CvmInstanceIds: list of str
        :param _NodeFlag: 销毁节点类型取值范围：
  <li>MASTER</li>
  <li>TASK</li>
  <li>CORE</li>
  <li>ROUTER</li>
        :type NodeFlag: str
        :param _GraceDownFlag: 优雅缩容开关
  <li>true:开启</li>
  <li>false:不开启</li>
        :type GraceDownFlag: bool
        :param _GraceDownTime: 优雅缩容等待时间,时间范围60到1800  单位秒
        :type GraceDownTime: int
        """
        self._InstanceId = None
        self._CvmInstanceIds = None
        self._NodeFlag = None
        self._GraceDownFlag = None
        self._GraceDownTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CvmInstanceIds(self):
        return self._CvmInstanceIds

    @CvmInstanceIds.setter
    def CvmInstanceIds(self, CvmInstanceIds):
        self._CvmInstanceIds = CvmInstanceIds

    @property
    def NodeFlag(self):
        return self._NodeFlag

    @NodeFlag.setter
    def NodeFlag(self, NodeFlag):
        self._NodeFlag = NodeFlag

    @property
    def GraceDownFlag(self):
        return self._GraceDownFlag

    @GraceDownFlag.setter
    def GraceDownFlag(self, GraceDownFlag):
        self._GraceDownFlag = GraceDownFlag

    @property
    def GraceDownTime(self):
        return self._GraceDownTime

    @GraceDownTime.setter
    def GraceDownTime(self, GraceDownTime):
        self._GraceDownTime = GraceDownTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CvmInstanceIds = params.get("CvmInstanceIds")
        self._NodeFlag = params.get("NodeFlag")
        self._GraceDownFlag = params.get("GraceDownFlag")
        self._GraceDownTime = params.get("GraceDownTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateClusterNodesResponse(AbstractModel):
    """TerminateClusterNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 缩容流程ID。
        :type FlowId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class TerminateInstanceRequest(AbstractModel):
    """TerminateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _ResourceIds: 销毁节点ID。该参数为预留参数，用户无需配置。
        :type ResourceIds: list of str
        """
        self._InstanceId = None
        self._ResourceIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstanceResponse(AbstractModel):
    """TerminateInstance返回参数结构体

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


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _ResourceIds: 待销毁节点的资源ID列表。资源ID形如：emr-vm-xxxxxxxx。有效的资源ID可通过登录[控制台](https://console.cloud.tencent.com/emr)查询。
        :type ResourceIds: list of str
        """
        self._InstanceId = None
        self._ResourceIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTasksResponse(AbstractModel):
    """TerminateTasks返回参数结构体

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


class TopologyInfo(AbstractModel):
    """集群节点拓扑信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _Zone: 可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _SubnetInfoList: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetInfoList: list of SubnetInfo
        :param _NodeInfoList: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfoList: list of ShortNodeInfo
        """
        self._ZoneId = None
        self._Zone = None
        self._SubnetInfoList = None
        self._NodeInfoList = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetInfoList(self):
        return self._SubnetInfoList

    @SubnetInfoList.setter
    def SubnetInfoList(self, SubnetInfoList):
        self._SubnetInfoList = SubnetInfoList

    @property
    def NodeInfoList(self):
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        if params.get("SubnetInfoList") is not None:
            self._SubnetInfoList = []
            for item in params.get("SubnetInfoList"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self._SubnetInfoList.append(obj)
        if params.get("NodeInfoList") is not None:
            self._NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = ShortNodeInfo()
                obj._deserialize(item)
                self._NodeInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceSettings(AbstractModel):
    """变配资源规格

    """

    def __init__(self):
        r"""
        :param _Memory: 内存容量，单位为G
        :type Memory: int
        :param _CPUCores: CPU核数
        :type CPUCores: int
        :param _ResourceId: 机器资源ID（EMR测资源标识）
        :type ResourceId: str
        :param _InstanceType: 变配机器规格
        :type InstanceType: str
        """
        self._Memory = None
        self._CPUCores = None
        self._ResourceId = None
        self._InstanceType = None

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def CPUCores(self):
        return self._CPUCores

    @CPUCores.setter
    def CPUCores(self, CPUCores):
        self._CPUCores = CPUCores

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._CPUCores = params.get("CPUCores")
        self._ResourceId = params.get("ResourceId")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserAndGroup(AbstractModel):
    """容器集群用户组信息

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _UserGroup: 用户组
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroup: str
        """
        self._UserName = None
        self._UserGroup = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserGroup = params.get("UserGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfoForUserManager(AbstractModel):
    """添加的用户信息列表

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _UserGroup: 用户所属的组
        :type UserGroup: str
        :param _PassWord: 密码
        :type PassWord: str
        :param _ReMark: 备注
        :type ReMark: str
        """
        self._UserName = None
        self._UserGroup = None
        self._PassWord = None
        self._ReMark = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def PassWord(self):
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def ReMark(self):
        return self._ReMark

    @ReMark.setter
    def ReMark(self, ReMark):
        self._ReMark = ReMark


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserGroup = params.get("UserGroup")
        self._PassWord = params.get("PassWord")
        self._ReMark = params.get("ReMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserManagerFilter(AbstractModel):
    """用户管理列表过滤器

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self._UserName = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserManagerUserBriefInfo(AbstractModel):
    """用户管理中用户的简要信息

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _UserGroup: 用户所属的组
        :type UserGroup: str
        :param _UserType: Manager表示管理员、NormalUser表示普通用户
        :type UserType: str
        :param _CreateTime: 用户创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _SupportDownLoadKeyTab: 是否可以下载用户对应的keytab文件，对开启kerberos的集群才有意义
        :type SupportDownLoadKeyTab: bool
        :param _DownLoadKeyTabUrl: keytab文件的下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownLoadKeyTabUrl: str
        """
        self._UserName = None
        self._UserGroup = None
        self._UserType = None
        self._CreateTime = None
        self._SupportDownLoadKeyTab = None
        self._DownLoadKeyTabUrl = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SupportDownLoadKeyTab(self):
        return self._SupportDownLoadKeyTab

    @SupportDownLoadKeyTab.setter
    def SupportDownLoadKeyTab(self, SupportDownLoadKeyTab):
        self._SupportDownLoadKeyTab = SupportDownLoadKeyTab

    @property
    def DownLoadKeyTabUrl(self):
        return self._DownLoadKeyTabUrl

    @DownLoadKeyTabUrl.setter
    def DownLoadKeyTabUrl(self, DownLoadKeyTabUrl):
        self._DownLoadKeyTabUrl = DownLoadKeyTabUrl


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._UserGroup = params.get("UserGroup")
        self._UserType = params.get("UserType")
        self._CreateTime = params.get("CreateTime")
        self._SupportDownLoadKeyTab = params.get("SupportDownLoadKeyTab")
        self._DownLoadKeyTabUrl = params.get("DownLoadKeyTabUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VPCSettings(AbstractModel):
    """VPC 参数

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

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


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirtualPrivateCloud(AbstractModel):
    """VPC 参数

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

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


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class YarnApplication(AbstractModel):
    """Yarn 运行的Application信息

    """

    def __init__(self):
        r"""
        :param _Id: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _User: 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type User: str
        :param _Name: 应用名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Queue: 队列
注意：此字段可能返回 null，表示取不到有效值。
        :type Queue: str
        :param _ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param _ElapsedTime: 运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ElapsedTime: str
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _FinalStatus: 最终状态
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalStatus: str
        :param _Progress: 进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param _StartedTime: 开始时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type StartedTime: int
        :param _FinishedTime: 结束时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedTime: int
        :param _AllocatedMB: 申请内存MB
注意：此字段可能返回 null，表示取不到有效值。
        :type AllocatedMB: int
        :param _AllocatedVCores: 申请VCores
注意：此字段可能返回 null，表示取不到有效值。
        :type AllocatedVCores: int
        :param _RunningContainers: 运行的Containers数
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningContainers: int
        :param _MemorySeconds: 内存MB*时间秒
注意：此字段可能返回 null，表示取不到有效值。
        :type MemorySeconds: int
        :param _VCoreSeconds: VCores*时间秒
注意：此字段可能返回 null，表示取不到有效值。
        :type VCoreSeconds: int
        :param _QueueUsagePercentage: 队列资源占比
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueUsagePercentage: float
        :param _ClusterUsagePercentage: 集群资源占比
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterUsagePercentage: float
        :param _PreemptedResourceMB: 预占用的内存
注意：此字段可能返回 null，表示取不到有效值。
        :type PreemptedResourceMB: int
        :param _PreemptedResourceVCores: 预占用的VCore
注意：此字段可能返回 null，表示取不到有效值。
        :type PreemptedResourceVCores: int
        :param _NumNonAMContainerPreempted: 预占的非应用程序主节点容器数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NumNonAMContainerPreempted: int
        :param _NumAMContainerPreempted: AM预占用的容器数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NumAMContainerPreempted: int
        :param _MapsTotal: Map总数
注意：此字段可能返回 null，表示取不到有效值。
        :type MapsTotal: int
        :param _MapsCompleted: 完成的Map数
注意：此字段可能返回 null，表示取不到有效值。
        :type MapsCompleted: int
        :param _ReducesTotal: Reduce总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReducesTotal: int
        :param _ReducesCompleted: 完成的Reduce数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReducesCompleted: int
        :param _AvgMapTime: 平均Map时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgMapTime: int
        :param _AvgReduceTime: 平均Reduce时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgReduceTime: int
        :param _AvgShuffleTime: 平均Shuffle时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgShuffleTime: int
        :param _AvgMergeTime: 平均Merge时间毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgMergeTime: int
        :param _FailedReduceAttempts: 失败的Reduce执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReduceAttempts: int
        :param _KilledReduceAttempts: Kill的Reduce执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type KilledReduceAttempts: int
        :param _SuccessfulReduceAttempts: 成功的Reduce执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessfulReduceAttempts: int
        :param _FailedMapAttempts: 失败的Map执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedMapAttempts: int
        :param _KilledMapAttempts: Kill的Map执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type KilledMapAttempts: int
        :param _SuccessfulMapAttempts: 成功的Map执行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessfulMapAttempts: int
        :param _GcTimeMillis: GC毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type GcTimeMillis: int
        :param _VCoreMillisMaps: Map使用的VCore毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type VCoreMillisMaps: int
        :param _MbMillisMaps: Map使用的内存毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type MbMillisMaps: int
        :param _VCoreMillisReduces: Reduce使用的VCore毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type VCoreMillisReduces: int
        :param _MbMillisReduces: Reduce使用的内存毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type MbMillisReduces: int
        :param _TotalLaunchedMaps: 启动Map的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalLaunchedMaps: int
        :param _TotalLaunchedReduces: 启动Reduce的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalLaunchedReduces: int
        :param _MapInputRecords: Map输入记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type MapInputRecords: int
        :param _MapOutputRecords: Map输出记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type MapOutputRecords: int
        :param _ReduceInputRecords: Reduce输入记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReduceInputRecords: int
        :param _ReduceOutputRecords: Reduce输出记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReduceOutputRecords: int
        :param _HDFSBytesWritten: HDFS写入字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type HDFSBytesWritten: int
        :param _HDFSBytesRead: HDFS读取字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type HDFSBytesRead: int
        """
        self._Id = None
        self._User = None
        self._Name = None
        self._Queue = None
        self._ApplicationType = None
        self._ElapsedTime = None
        self._State = None
        self._FinalStatus = None
        self._Progress = None
        self._StartedTime = None
        self._FinishedTime = None
        self._AllocatedMB = None
        self._AllocatedVCores = None
        self._RunningContainers = None
        self._MemorySeconds = None
        self._VCoreSeconds = None
        self._QueueUsagePercentage = None
        self._ClusterUsagePercentage = None
        self._PreemptedResourceMB = None
        self._PreemptedResourceVCores = None
        self._NumNonAMContainerPreempted = None
        self._NumAMContainerPreempted = None
        self._MapsTotal = None
        self._MapsCompleted = None
        self._ReducesTotal = None
        self._ReducesCompleted = None
        self._AvgMapTime = None
        self._AvgReduceTime = None
        self._AvgShuffleTime = None
        self._AvgMergeTime = None
        self._FailedReduceAttempts = None
        self._KilledReduceAttempts = None
        self._SuccessfulReduceAttempts = None
        self._FailedMapAttempts = None
        self._KilledMapAttempts = None
        self._SuccessfulMapAttempts = None
        self._GcTimeMillis = None
        self._VCoreMillisMaps = None
        self._MbMillisMaps = None
        self._VCoreMillisReduces = None
        self._MbMillisReduces = None
        self._TotalLaunchedMaps = None
        self._TotalLaunchedReduces = None
        self._MapInputRecords = None
        self._MapOutputRecords = None
        self._ReduceInputRecords = None
        self._ReduceOutputRecords = None
        self._HDFSBytesWritten = None
        self._HDFSBytesRead = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Queue(self):
        return self._Queue

    @Queue.setter
    def Queue(self, Queue):
        self._Queue = Queue

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ElapsedTime(self):
        return self._ElapsedTime

    @ElapsedTime.setter
    def ElapsedTime(self, ElapsedTime):
        self._ElapsedTime = ElapsedTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def FinalStatus(self):
        return self._FinalStatus

    @FinalStatus.setter
    def FinalStatus(self, FinalStatus):
        self._FinalStatus = FinalStatus

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StartedTime(self):
        return self._StartedTime

    @StartedTime.setter
    def StartedTime(self, StartedTime):
        self._StartedTime = StartedTime

    @property
    def FinishedTime(self):
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime

    @property
    def AllocatedMB(self):
        return self._AllocatedMB

    @AllocatedMB.setter
    def AllocatedMB(self, AllocatedMB):
        self._AllocatedMB = AllocatedMB

    @property
    def AllocatedVCores(self):
        return self._AllocatedVCores

    @AllocatedVCores.setter
    def AllocatedVCores(self, AllocatedVCores):
        self._AllocatedVCores = AllocatedVCores

    @property
    def RunningContainers(self):
        return self._RunningContainers

    @RunningContainers.setter
    def RunningContainers(self, RunningContainers):
        self._RunningContainers = RunningContainers

    @property
    def MemorySeconds(self):
        return self._MemorySeconds

    @MemorySeconds.setter
    def MemorySeconds(self, MemorySeconds):
        self._MemorySeconds = MemorySeconds

    @property
    def VCoreSeconds(self):
        return self._VCoreSeconds

    @VCoreSeconds.setter
    def VCoreSeconds(self, VCoreSeconds):
        self._VCoreSeconds = VCoreSeconds

    @property
    def QueueUsagePercentage(self):
        return self._QueueUsagePercentage

    @QueueUsagePercentage.setter
    def QueueUsagePercentage(self, QueueUsagePercentage):
        self._QueueUsagePercentage = QueueUsagePercentage

    @property
    def ClusterUsagePercentage(self):
        return self._ClusterUsagePercentage

    @ClusterUsagePercentage.setter
    def ClusterUsagePercentage(self, ClusterUsagePercentage):
        self._ClusterUsagePercentage = ClusterUsagePercentage

    @property
    def PreemptedResourceMB(self):
        return self._PreemptedResourceMB

    @PreemptedResourceMB.setter
    def PreemptedResourceMB(self, PreemptedResourceMB):
        self._PreemptedResourceMB = PreemptedResourceMB

    @property
    def PreemptedResourceVCores(self):
        return self._PreemptedResourceVCores

    @PreemptedResourceVCores.setter
    def PreemptedResourceVCores(self, PreemptedResourceVCores):
        self._PreemptedResourceVCores = PreemptedResourceVCores

    @property
    def NumNonAMContainerPreempted(self):
        return self._NumNonAMContainerPreempted

    @NumNonAMContainerPreempted.setter
    def NumNonAMContainerPreempted(self, NumNonAMContainerPreempted):
        self._NumNonAMContainerPreempted = NumNonAMContainerPreempted

    @property
    def NumAMContainerPreempted(self):
        return self._NumAMContainerPreempted

    @NumAMContainerPreempted.setter
    def NumAMContainerPreempted(self, NumAMContainerPreempted):
        self._NumAMContainerPreempted = NumAMContainerPreempted

    @property
    def MapsTotal(self):
        return self._MapsTotal

    @MapsTotal.setter
    def MapsTotal(self, MapsTotal):
        self._MapsTotal = MapsTotal

    @property
    def MapsCompleted(self):
        return self._MapsCompleted

    @MapsCompleted.setter
    def MapsCompleted(self, MapsCompleted):
        self._MapsCompleted = MapsCompleted

    @property
    def ReducesTotal(self):
        return self._ReducesTotal

    @ReducesTotal.setter
    def ReducesTotal(self, ReducesTotal):
        self._ReducesTotal = ReducesTotal

    @property
    def ReducesCompleted(self):
        return self._ReducesCompleted

    @ReducesCompleted.setter
    def ReducesCompleted(self, ReducesCompleted):
        self._ReducesCompleted = ReducesCompleted

    @property
    def AvgMapTime(self):
        return self._AvgMapTime

    @AvgMapTime.setter
    def AvgMapTime(self, AvgMapTime):
        self._AvgMapTime = AvgMapTime

    @property
    def AvgReduceTime(self):
        return self._AvgReduceTime

    @AvgReduceTime.setter
    def AvgReduceTime(self, AvgReduceTime):
        self._AvgReduceTime = AvgReduceTime

    @property
    def AvgShuffleTime(self):
        return self._AvgShuffleTime

    @AvgShuffleTime.setter
    def AvgShuffleTime(self, AvgShuffleTime):
        self._AvgShuffleTime = AvgShuffleTime

    @property
    def AvgMergeTime(self):
        return self._AvgMergeTime

    @AvgMergeTime.setter
    def AvgMergeTime(self, AvgMergeTime):
        self._AvgMergeTime = AvgMergeTime

    @property
    def FailedReduceAttempts(self):
        return self._FailedReduceAttempts

    @FailedReduceAttempts.setter
    def FailedReduceAttempts(self, FailedReduceAttempts):
        self._FailedReduceAttempts = FailedReduceAttempts

    @property
    def KilledReduceAttempts(self):
        return self._KilledReduceAttempts

    @KilledReduceAttempts.setter
    def KilledReduceAttempts(self, KilledReduceAttempts):
        self._KilledReduceAttempts = KilledReduceAttempts

    @property
    def SuccessfulReduceAttempts(self):
        return self._SuccessfulReduceAttempts

    @SuccessfulReduceAttempts.setter
    def SuccessfulReduceAttempts(self, SuccessfulReduceAttempts):
        self._SuccessfulReduceAttempts = SuccessfulReduceAttempts

    @property
    def FailedMapAttempts(self):
        return self._FailedMapAttempts

    @FailedMapAttempts.setter
    def FailedMapAttempts(self, FailedMapAttempts):
        self._FailedMapAttempts = FailedMapAttempts

    @property
    def KilledMapAttempts(self):
        return self._KilledMapAttempts

    @KilledMapAttempts.setter
    def KilledMapAttempts(self, KilledMapAttempts):
        self._KilledMapAttempts = KilledMapAttempts

    @property
    def SuccessfulMapAttempts(self):
        return self._SuccessfulMapAttempts

    @SuccessfulMapAttempts.setter
    def SuccessfulMapAttempts(self, SuccessfulMapAttempts):
        self._SuccessfulMapAttempts = SuccessfulMapAttempts

    @property
    def GcTimeMillis(self):
        return self._GcTimeMillis

    @GcTimeMillis.setter
    def GcTimeMillis(self, GcTimeMillis):
        self._GcTimeMillis = GcTimeMillis

    @property
    def VCoreMillisMaps(self):
        return self._VCoreMillisMaps

    @VCoreMillisMaps.setter
    def VCoreMillisMaps(self, VCoreMillisMaps):
        self._VCoreMillisMaps = VCoreMillisMaps

    @property
    def MbMillisMaps(self):
        return self._MbMillisMaps

    @MbMillisMaps.setter
    def MbMillisMaps(self, MbMillisMaps):
        self._MbMillisMaps = MbMillisMaps

    @property
    def VCoreMillisReduces(self):
        return self._VCoreMillisReduces

    @VCoreMillisReduces.setter
    def VCoreMillisReduces(self, VCoreMillisReduces):
        self._VCoreMillisReduces = VCoreMillisReduces

    @property
    def MbMillisReduces(self):
        return self._MbMillisReduces

    @MbMillisReduces.setter
    def MbMillisReduces(self, MbMillisReduces):
        self._MbMillisReduces = MbMillisReduces

    @property
    def TotalLaunchedMaps(self):
        return self._TotalLaunchedMaps

    @TotalLaunchedMaps.setter
    def TotalLaunchedMaps(self, TotalLaunchedMaps):
        self._TotalLaunchedMaps = TotalLaunchedMaps

    @property
    def TotalLaunchedReduces(self):
        return self._TotalLaunchedReduces

    @TotalLaunchedReduces.setter
    def TotalLaunchedReduces(self, TotalLaunchedReduces):
        self._TotalLaunchedReduces = TotalLaunchedReduces

    @property
    def MapInputRecords(self):
        return self._MapInputRecords

    @MapInputRecords.setter
    def MapInputRecords(self, MapInputRecords):
        self._MapInputRecords = MapInputRecords

    @property
    def MapOutputRecords(self):
        return self._MapOutputRecords

    @MapOutputRecords.setter
    def MapOutputRecords(self, MapOutputRecords):
        self._MapOutputRecords = MapOutputRecords

    @property
    def ReduceInputRecords(self):
        return self._ReduceInputRecords

    @ReduceInputRecords.setter
    def ReduceInputRecords(self, ReduceInputRecords):
        self._ReduceInputRecords = ReduceInputRecords

    @property
    def ReduceOutputRecords(self):
        return self._ReduceOutputRecords

    @ReduceOutputRecords.setter
    def ReduceOutputRecords(self, ReduceOutputRecords):
        self._ReduceOutputRecords = ReduceOutputRecords

    @property
    def HDFSBytesWritten(self):
        return self._HDFSBytesWritten

    @HDFSBytesWritten.setter
    def HDFSBytesWritten(self, HDFSBytesWritten):
        self._HDFSBytesWritten = HDFSBytesWritten

    @property
    def HDFSBytesRead(self):
        return self._HDFSBytesRead

    @HDFSBytesRead.setter
    def HDFSBytesRead(self, HDFSBytesRead):
        self._HDFSBytesRead = HDFSBytesRead


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._User = params.get("User")
        self._Name = params.get("Name")
        self._Queue = params.get("Queue")
        self._ApplicationType = params.get("ApplicationType")
        self._ElapsedTime = params.get("ElapsedTime")
        self._State = params.get("State")
        self._FinalStatus = params.get("FinalStatus")
        self._Progress = params.get("Progress")
        self._StartedTime = params.get("StartedTime")
        self._FinishedTime = params.get("FinishedTime")
        self._AllocatedMB = params.get("AllocatedMB")
        self._AllocatedVCores = params.get("AllocatedVCores")
        self._RunningContainers = params.get("RunningContainers")
        self._MemorySeconds = params.get("MemorySeconds")
        self._VCoreSeconds = params.get("VCoreSeconds")
        self._QueueUsagePercentage = params.get("QueueUsagePercentage")
        self._ClusterUsagePercentage = params.get("ClusterUsagePercentage")
        self._PreemptedResourceMB = params.get("PreemptedResourceMB")
        self._PreemptedResourceVCores = params.get("PreemptedResourceVCores")
        self._NumNonAMContainerPreempted = params.get("NumNonAMContainerPreempted")
        self._NumAMContainerPreempted = params.get("NumAMContainerPreempted")
        self._MapsTotal = params.get("MapsTotal")
        self._MapsCompleted = params.get("MapsCompleted")
        self._ReducesTotal = params.get("ReducesTotal")
        self._ReducesCompleted = params.get("ReducesCompleted")
        self._AvgMapTime = params.get("AvgMapTime")
        self._AvgReduceTime = params.get("AvgReduceTime")
        self._AvgShuffleTime = params.get("AvgShuffleTime")
        self._AvgMergeTime = params.get("AvgMergeTime")
        self._FailedReduceAttempts = params.get("FailedReduceAttempts")
        self._KilledReduceAttempts = params.get("KilledReduceAttempts")
        self._SuccessfulReduceAttempts = params.get("SuccessfulReduceAttempts")
        self._FailedMapAttempts = params.get("FailedMapAttempts")
        self._KilledMapAttempts = params.get("KilledMapAttempts")
        self._SuccessfulMapAttempts = params.get("SuccessfulMapAttempts")
        self._GcTimeMillis = params.get("GcTimeMillis")
        self._VCoreMillisMaps = params.get("VCoreMillisMaps")
        self._MbMillisMaps = params.get("MbMillisMaps")
        self._VCoreMillisReduces = params.get("VCoreMillisReduces")
        self._MbMillisReduces = params.get("MbMillisReduces")
        self._TotalLaunchedMaps = params.get("TotalLaunchedMaps")
        self._TotalLaunchedReduces = params.get("TotalLaunchedReduces")
        self._MapInputRecords = params.get("MapInputRecords")
        self._MapOutputRecords = params.get("MapOutputRecords")
        self._ReduceInputRecords = params.get("ReduceInputRecords")
        self._ReduceOutputRecords = params.get("ReduceOutputRecords")
        self._HDFSBytesWritten = params.get("HDFSBytesWritten")
        self._HDFSBytesRead = params.get("HDFSBytesRead")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDetailPriceResult(AbstractModel):
    """用于创建集群价格清单 不同可用区下价格详情

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _NodeDetailPrice: 不同节点的价格详情
        :type NodeDetailPrice: list of NodeDetailPriceResult
        """
        self._ZoneId = None
        self._NodeDetailPrice = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NodeDetailPrice(self):
        return self._NodeDetailPrice

    @NodeDetailPrice.setter
    def NodeDetailPrice(self, NodeDetailPrice):
        self._NodeDetailPrice = NodeDetailPrice


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("NodeDetailPrice") is not None:
            self._NodeDetailPrice = []
            for item in params.get("NodeDetailPrice"):
                obj = NodeDetailPriceResult()
                obj._deserialize(item)
                self._NodeDetailPrice.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResourceConfiguration(AbstractModel):
    """可用区配置信息

    """

    def __init__(self):
        r"""
        :param _VirtualPrivateCloud: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPrivateCloud: :class:`tencentcloud.emr.v20190103.models.VirtualPrivateCloud`
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param _AllNodeResourceSpec: 所有节点资源的规格
注意：此字段可能返回 null，表示取不到有效值。
        :type AllNodeResourceSpec: :class:`tencentcloud.emr.v20190103.models.AllNodeResourceSpec`
        :param _ZoneTag: 如果是单可用区，ZoneTag可以不用填， 如果是双AZ部署，第一个可用区ZoneTag选择master，第二个可用区ZoneTag选择standby，如果是三AZ部署，第一个可用区ZoneTag选择master，第二个可用区ZoneTag选择standby，第三个可用区ZoneTag选择third-party，取值范围：
  <li>master</li>
  <li>standby</li>
  <li>third-party</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneTag: str
        """
        self._VirtualPrivateCloud = None
        self._Placement = None
        self._AllNodeResourceSpec = None
        self._ZoneTag = None

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def AllNodeResourceSpec(self):
        return self._AllNodeResourceSpec

    @AllNodeResourceSpec.setter
    def AllNodeResourceSpec(self, AllNodeResourceSpec):
        self._AllNodeResourceSpec = AllNodeResourceSpec

    @property
    def ZoneTag(self):
        return self._ZoneTag

    @ZoneTag.setter
    def ZoneTag(self, ZoneTag):
        self._ZoneTag = ZoneTag


    def _deserialize(self, params):
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("AllNodeResourceSpec") is not None:
            self._AllNodeResourceSpec = AllNodeResourceSpec()
            self._AllNodeResourceSpec._deserialize(params.get("AllNodeResourceSpec"))
        self._ZoneTag = params.get("ZoneTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        