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


class CCN(AbstractModel):
    """云联网描述信息

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络 ID
        :type VpcId: str
        :param _SubnetId: 子网 ID
        :type SubnetId: str
        :param _CcnId: 云联网 ID，如 ccn-rahigzjd
        :type CcnId: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._CcnId = None

    @property
    def VpcId(self):
        """私有网络 ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网 ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CcnId(self):
        """云联网 ID，如 ccn-rahigzjd
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckSavepointRequest(AbstractModel):
    """CheckSavepoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业 id
        :type JobId: str
        :param _SerialId: 快照资源 id
        :type SerialId: str
        :param _RecordType: 快照类型 1: savepoint；2: checkpoint；3: cancelWithSavepoint
        :type RecordType: int
        :param _SavepointPath: 快照路径，目前只支持 cos 路径
        :type SavepointPath: str
        :param _WorkSpaceId: 工作空间 id
        :type WorkSpaceId: str
        """
        self._JobId = None
        self._SerialId = None
        self._RecordType = None
        self._SavepointPath = None
        self._WorkSpaceId = None

    @property
    def JobId(self):
        """作业 id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def SerialId(self):
        """快照资源 id
        :rtype: str
        """
        return self._SerialId

    @SerialId.setter
    def SerialId(self, SerialId):
        self._SerialId = SerialId

    @property
    def RecordType(self):
        """快照类型 1: savepoint；2: checkpoint；3: cancelWithSavepoint
        :rtype: int
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def SavepointPath(self):
        """快照路径，目前只支持 cos 路径
        :rtype: str
        """
        return self._SavepointPath

    @SavepointPath.setter
    def SavepointPath(self, SavepointPath):
        self._SavepointPath = SavepointPath

    @property
    def WorkSpaceId(self):
        """工作空间 id
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._SerialId = params.get("SerialId")
        self._RecordType = params.get("RecordType")
        self._SavepointPath = params.get("SavepointPath")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckSavepointResponse(AbstractModel):
    """CheckSavepoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SerialId: 资源 id
        :type SerialId: str
        :param _SavepointStatus: 1=可用，2=不可用
        :type SavepointStatus: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SerialId = None
        self._SavepointStatus = None
        self._RequestId = None

    @property
    def SerialId(self):
        """资源 id
        :rtype: str
        """
        return self._SerialId

    @SerialId.setter
    def SerialId(self, SerialId):
        self._SerialId = SerialId

    @property
    def SavepointStatus(self):
        """1=可用，2=不可用
        :rtype: int
        """
        return self._SavepointStatus

    @SavepointStatus.setter
    def SavepointStatus(self, SavepointStatus):
        self._SavepointStatus = SavepointStatus

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SerialId = params.get("SerialId")
        self._SavepointStatus = params.get("SavepointStatus")
        self._RequestId = params.get("RequestId")


class ClazzLevel(AbstractModel):
    """{
    "Clazz": "c1", // java类全路径
    "Level": "WARN" // 日志级别  TRACE，DEBUG、INFO、WARN、ERROR
    }

    """

    def __init__(self):
        r"""
        :param _Clazz: java类全路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Clazz: str
        :param _Level: 日志级别  TRACE，DEBUG、INFO、WARN、ERROR
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        """
        self._Clazz = None
        self._Level = None

    @property
    def Clazz(self):
        """java类全路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Clazz

    @Clazz.setter
    def Clazz(self, Clazz):
        self._Clazz = Clazz

    @property
    def Level(self):
        """日志级别  TRACE，DEBUG、INFO、WARN、ERROR
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Clazz = params.get("Clazz")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cluster(AbstractModel):
    """描述用户创建的集群信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _Name: 集群名称
        :type Name: str
        :param _Region: 地域
        :type Region: str
        :param _AppId: 用户 AppID
        :type AppId: int
        :param _OwnerUin: 主账号 UIN
        :type OwnerUin: str
        :param _CreatorUin: 创建者 UIN
        :type CreatorUin: str
        :param _Status: 集群状态, 1 未初始化,3 初始化中，2 运行中
        :type Status: int
        :param _Remark: 描述
        :type Remark: str
        :param _CreateTime: 集群创建时间
        :type CreateTime: str
        :param _UpdateTime: 最后一次操作集群的时间
        :type UpdateTime: str
        :param _CuNum: CU 数量
        :type CuNum: int
        :param _CuMem: CU 内存规格
        :type CuMem: int
        :param _Zone: 可用区
        :type Zone: str
        :param _StatusDesc: 状态描述
        :type StatusDesc: str
        :param _CCNs: 网络
        :type CCNs: list of CCN
        :param _NetEnvironmentType: 网络
        :type NetEnvironmentType: int
        :param _FreeCuNum: 空闲 CU
        :type FreeCuNum: int
        :param _Tags: 集群绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _IsolatedTime: 集群隔离时间; 没隔离时间，则为 -
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param _ExpireTime: 集群过期时间; 没过期概念，则为 -
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _SecondsUntilExpiry: 距离过期还有多少秒; 没过期概念，则为 -
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondsUntilExpiry: str
        :param _AutoRenewFlag: 自动续费标记，0 表示默认状态 (用户未设置，即初始状态，用户开通了预付费不停服特权会进行自动续费)， 1 表示自动续费，2表示明确不自动续费(用户设置)
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _DefaultCOSBucket: 集群的默认 COS 存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultCOSBucket: str
        :param _CLSLogSet: 集群的CLS 日志集 LogSet
注意：此字段可能返回 null，表示取不到有效值。
        :type CLSLogSet: str
        :param _CLSTopicId: 集群的CLS 日志主题 TopicId
注意：此字段可能返回 null，表示取不到有效值。
        :type CLSTopicId: str
        :param _CLSLogName: 集群的CLS 日志集  名字
注意：此字段可能返回 null，表示取不到有效值。
        :type CLSLogName: str
        :param _CLSTopicName: 集群的CLS 日志主题  名字
注意：此字段可能返回 null，表示取不到有效值。
        :type CLSTopicName: str
        :param _Version: 集群的版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: :class:`tencentcloud.oceanus.v20190422.models.ClusterVersion`
        :param _FreeCu: 细粒度资源下的空闲CU
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeCu: float
        :param _DefaultLogCollectConf: 集群的默认日志采集配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultLogCollectConf: str
        :param _CustomizedDNSEnabled: 取值：0-没有设置，1-已设置，2-不允许设置
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomizedDNSEnabled: int
        :param _Correlations: 空间信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Correlations: list of WorkSpaceClusterItem
        :param _RunningCu: 运行CU
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningCu: float
        :param _PayMode: 0 后付费,1 预付费
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param _IsNeedManageNode: 前端区分 集群是否需要2CU逻辑 因为历史集群 变配不需要, default 1  新集群都需要
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNeedManageNode: int
        :param _ClusterSessions: session集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterSessions: list of ClusterSession
        :param _ArchGeneration: V3版本 = 2
注意：此字段可能返回 null，表示取不到有效值。
        :type ArchGeneration: int
        :param _ClusterType: 0:TKE, 1:EKS
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: int
        :param _Orders: 订单信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Orders: list of Order
        :param _SqlGateways: Gateway信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlGateways: list of SqlGatewayItem
        :param _WebUIType: 0 公网访问 // 1 内网访问	
注意：此字段可能返回 null，表示取不到有效值。
        :type WebUIType: int
        :param _Type: 2 独享集群
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _SubEks: 子eks集群
注意：此字段可能返回 null，表示取不到有效值。
        :type SubEks: :class:`tencentcloud.oceanus.v20190422.models.SubEks`
        :param _AgentSerialId: 上级集群
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentSerialId: str
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: int
        :param _BillingResourceMode: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingResourceMode: str
        :param _MemRatio: Cu比例
注意：此字段可能返回 null，表示取不到有效值。
        :type MemRatio: int
        :param _CrossTenantEniMode: 是否开启跨租户弹性网卡
        :type CrossTenantEniMode: int
        :param _TotalCpu: 总的CPU
        :type TotalCpu: float
        :param _TotalMem: 总的内存
        :type TotalMem: float
        :param _RunningCpu: 运行的CPU
        :type RunningCpu: float
        :param _RunningMem: 运行的内存
        :type RunningMem: float
        :param _Setats: setats集群
注意：此字段可能返回 null，表示取不到有效值。
        :type Setats: :class:`tencentcloud.oceanus.v20190422.models.Setats`
        """
        self._ClusterId = None
        self._Name = None
        self._Region = None
        self._AppId = None
        self._OwnerUin = None
        self._CreatorUin = None
        self._Status = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CuNum = None
        self._CuMem = None
        self._Zone = None
        self._StatusDesc = None
        self._CCNs = None
        self._NetEnvironmentType = None
        self._FreeCuNum = None
        self._Tags = None
        self._IsolatedTime = None
        self._ExpireTime = None
        self._SecondsUntilExpiry = None
        self._AutoRenewFlag = None
        self._DefaultCOSBucket = None
        self._CLSLogSet = None
        self._CLSTopicId = None
        self._CLSLogName = None
        self._CLSTopicName = None
        self._Version = None
        self._FreeCu = None
        self._DefaultLogCollectConf = None
        self._CustomizedDNSEnabled = None
        self._Correlations = None
        self._RunningCu = None
        self._PayMode = None
        self._IsNeedManageNode = None
        self._ClusterSessions = None
        self._ArchGeneration = None
        self._ClusterType = None
        self._Orders = None
        self._SqlGateways = None
        self._WebUIType = None
        self._Type = None
        self._SubEks = None
        self._AgentSerialId = None
        self._ResourceType = None
        self._BillingResourceMode = None
        self._MemRatio = None
        self._CrossTenantEniMode = None
        self._TotalCpu = None
        self._TotalMem = None
        self._RunningCpu = None
        self._RunningMem = None
        self._Setats = None

    @property
    def ClusterId(self):
        """集群 ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Name(self):
        """集群名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AppId(self):
        """用户 AppID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OwnerUin(self):
        """主账号 UIN
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreatorUin(self):
        """创建者 UIN
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def Status(self):
        """集群状态, 1 未初始化,3 初始化中，2 运行中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        """描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        """集群创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最后一次操作集群的时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CuNum(self):
        """CU 数量
        :rtype: int
        """
        return self._CuNum

    @CuNum.setter
    def CuNum(self, CuNum):
        self._CuNum = CuNum

    @property
    def CuMem(self):
        """CU 内存规格
        :rtype: int
        """
        return self._CuMem

    @CuMem.setter
    def CuMem(self, CuMem):
        self._CuMem = CuMem

    @property
    def Zone(self):
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def StatusDesc(self):
        """状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CCNs(self):
        """网络
        :rtype: list of CCN
        """
        return self._CCNs

    @CCNs.setter
    def CCNs(self, CCNs):
        self._CCNs = CCNs

    @property
    def NetEnvironmentType(self):
        """网络
        :rtype: int
        """
        return self._NetEnvironmentType

    @NetEnvironmentType.setter
    def NetEnvironmentType(self, NetEnvironmentType):
        self._NetEnvironmentType = NetEnvironmentType

    @property
    def FreeCuNum(self):
        """空闲 CU
        :rtype: int
        """
        return self._FreeCuNum

    @FreeCuNum.setter
    def FreeCuNum(self, FreeCuNum):
        self._FreeCuNum = FreeCuNum

    @property
    def Tags(self):
        """集群绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IsolatedTime(self):
        """集群隔离时间; 没隔离时间，则为 -
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def ExpireTime(self):
        """集群过期时间; 没过期概念，则为 -
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def SecondsUntilExpiry(self):
        """距离过期还有多少秒; 没过期概念，则为 -
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecondsUntilExpiry

    @SecondsUntilExpiry.setter
    def SecondsUntilExpiry(self, SecondsUntilExpiry):
        self._SecondsUntilExpiry = SecondsUntilExpiry

    @property
    def AutoRenewFlag(self):
        """自动续费标记，0 表示默认状态 (用户未设置，即初始状态，用户开通了预付费不停服特权会进行自动续费)， 1 表示自动续费，2表示明确不自动续费(用户设置)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def DefaultCOSBucket(self):
        """集群的默认 COS 存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DefaultCOSBucket

    @DefaultCOSBucket.setter
    def DefaultCOSBucket(self, DefaultCOSBucket):
        self._DefaultCOSBucket = DefaultCOSBucket

    @property
    def CLSLogSet(self):
        """集群的CLS 日志集 LogSet
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CLSLogSet

    @CLSLogSet.setter
    def CLSLogSet(self, CLSLogSet):
        self._CLSLogSet = CLSLogSet

    @property
    def CLSTopicId(self):
        """集群的CLS 日志主题 TopicId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CLSTopicId

    @CLSTopicId.setter
    def CLSTopicId(self, CLSTopicId):
        self._CLSTopicId = CLSTopicId

    @property
    def CLSLogName(self):
        """集群的CLS 日志集  名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CLSLogName

    @CLSLogName.setter
    def CLSLogName(self, CLSLogName):
        self._CLSLogName = CLSLogName

    @property
    def CLSTopicName(self):
        """集群的CLS 日志主题  名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CLSTopicName

    @CLSTopicName.setter
    def CLSTopicName(self, CLSTopicName):
        self._CLSTopicName = CLSTopicName

    @property
    def Version(self):
        """集群的版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.ClusterVersion`
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def FreeCu(self):
        """细粒度资源下的空闲CU
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._FreeCu

    @FreeCu.setter
    def FreeCu(self, FreeCu):
        self._FreeCu = FreeCu

    @property
    def DefaultLogCollectConf(self):
        """集群的默认日志采集配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DefaultLogCollectConf

    @DefaultLogCollectConf.setter
    def DefaultLogCollectConf(self, DefaultLogCollectConf):
        self._DefaultLogCollectConf = DefaultLogCollectConf

    @property
    def CustomizedDNSEnabled(self):
        """取值：0-没有设置，1-已设置，2-不允许设置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CustomizedDNSEnabled

    @CustomizedDNSEnabled.setter
    def CustomizedDNSEnabled(self, CustomizedDNSEnabled):
        self._CustomizedDNSEnabled = CustomizedDNSEnabled

    @property
    def Correlations(self):
        """空间信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkSpaceClusterItem
        """
        return self._Correlations

    @Correlations.setter
    def Correlations(self, Correlations):
        self._Correlations = Correlations

    @property
    def RunningCu(self):
        """运行CU
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RunningCu

    @RunningCu.setter
    def RunningCu(self, RunningCu):
        self._RunningCu = RunningCu

    @property
    def PayMode(self):
        """0 后付费,1 预付费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def IsNeedManageNode(self):
        """前端区分 集群是否需要2CU逻辑 因为历史集群 变配不需要, default 1  新集群都需要
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsNeedManageNode

    @IsNeedManageNode.setter
    def IsNeedManageNode(self, IsNeedManageNode):
        self._IsNeedManageNode = IsNeedManageNode

    @property
    def ClusterSessions(self):
        """session集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ClusterSession
        """
        return self._ClusterSessions

    @ClusterSessions.setter
    def ClusterSessions(self, ClusterSessions):
        self._ClusterSessions = ClusterSessions

    @property
    def ArchGeneration(self):
        """V3版本 = 2
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ArchGeneration

    @ArchGeneration.setter
    def ArchGeneration(self, ArchGeneration):
        self._ArchGeneration = ArchGeneration

    @property
    def ClusterType(self):
        """0:TKE, 1:EKS
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Orders(self):
        """订单信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Order
        """
        return self._Orders

    @Orders.setter
    def Orders(self, Orders):
        self._Orders = Orders

    @property
    def SqlGateways(self):
        """Gateway信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SqlGatewayItem
        """
        return self._SqlGateways

    @SqlGateways.setter
    def SqlGateways(self, SqlGateways):
        self._SqlGateways = SqlGateways

    @property
    def WebUIType(self):
        """0 公网访问 // 1 内网访问	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WebUIType

    @WebUIType.setter
    def WebUIType(self, WebUIType):
        self._WebUIType = WebUIType

    @property
    def Type(self):
        """2 独享集群
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubEks(self):
        """子eks集群
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.SubEks`
        """
        return self._SubEks

    @SubEks.setter
    def SubEks(self, SubEks):
        self._SubEks = SubEks

    @property
    def AgentSerialId(self):
        """上级集群
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentSerialId

    @AgentSerialId.setter
    def AgentSerialId(self, AgentSerialId):
        self._AgentSerialId = AgentSerialId

    @property
    def ResourceType(self):
        """资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def BillingResourceMode(self):
        """集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BillingResourceMode

    @BillingResourceMode.setter
    def BillingResourceMode(self, BillingResourceMode):
        self._BillingResourceMode = BillingResourceMode

    @property
    def MemRatio(self):
        """Cu比例
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MemRatio

    @MemRatio.setter
    def MemRatio(self, MemRatio):
        self._MemRatio = MemRatio

    @property
    def CrossTenantEniMode(self):
        """是否开启跨租户弹性网卡
        :rtype: int
        """
        return self._CrossTenantEniMode

    @CrossTenantEniMode.setter
    def CrossTenantEniMode(self, CrossTenantEniMode):
        self._CrossTenantEniMode = CrossTenantEniMode

    @property
    def TotalCpu(self):
        """总的CPU
        :rtype: float
        """
        return self._TotalCpu

    @TotalCpu.setter
    def TotalCpu(self, TotalCpu):
        self._TotalCpu = TotalCpu

    @property
    def TotalMem(self):
        """总的内存
        :rtype: float
        """
        return self._TotalMem

    @TotalMem.setter
    def TotalMem(self, TotalMem):
        self._TotalMem = TotalMem

    @property
    def RunningCpu(self):
        """运行的CPU
        :rtype: float
        """
        return self._RunningCpu

    @RunningCpu.setter
    def RunningCpu(self, RunningCpu):
        self._RunningCpu = RunningCpu

    @property
    def RunningMem(self):
        """运行的内存
        :rtype: float
        """
        return self._RunningMem

    @RunningMem.setter
    def RunningMem(self, RunningMem):
        self._RunningMem = RunningMem

    @property
    def Setats(self):
        """setats集群
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.Setats`
        """
        return self._Setats

    @Setats.setter
    def Setats(self, Setats):
        self._Setats = Setats


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Name = params.get("Name")
        self._Region = params.get("Region")
        self._AppId = params.get("AppId")
        self._OwnerUin = params.get("OwnerUin")
        self._CreatorUin = params.get("CreatorUin")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CuNum = params.get("CuNum")
        self._CuMem = params.get("CuMem")
        self._Zone = params.get("Zone")
        self._StatusDesc = params.get("StatusDesc")
        if params.get("CCNs") is not None:
            self._CCNs = []
            for item in params.get("CCNs"):
                obj = CCN()
                obj._deserialize(item)
                self._CCNs.append(obj)
        self._NetEnvironmentType = params.get("NetEnvironmentType")
        self._FreeCuNum = params.get("FreeCuNum")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IsolatedTime = params.get("IsolatedTime")
        self._ExpireTime = params.get("ExpireTime")
        self._SecondsUntilExpiry = params.get("SecondsUntilExpiry")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._DefaultCOSBucket = params.get("DefaultCOSBucket")
        self._CLSLogSet = params.get("CLSLogSet")
        self._CLSTopicId = params.get("CLSTopicId")
        self._CLSLogName = params.get("CLSLogName")
        self._CLSTopicName = params.get("CLSTopicName")
        if params.get("Version") is not None:
            self._Version = ClusterVersion()
            self._Version._deserialize(params.get("Version"))
        self._FreeCu = params.get("FreeCu")
        self._DefaultLogCollectConf = params.get("DefaultLogCollectConf")
        self._CustomizedDNSEnabled = params.get("CustomizedDNSEnabled")
        if params.get("Correlations") is not None:
            self._Correlations = []
            for item in params.get("Correlations"):
                obj = WorkSpaceClusterItem()
                obj._deserialize(item)
                self._Correlations.append(obj)
        self._RunningCu = params.get("RunningCu")
        self._PayMode = params.get("PayMode")
        self._IsNeedManageNode = params.get("IsNeedManageNode")
        if params.get("ClusterSessions") is not None:
            self._ClusterSessions = []
            for item in params.get("ClusterSessions"):
                obj = ClusterSession()
                obj._deserialize(item)
                self._ClusterSessions.append(obj)
        self._ArchGeneration = params.get("ArchGeneration")
        self._ClusterType = params.get("ClusterType")
        if params.get("Orders") is not None:
            self._Orders = []
            for item in params.get("Orders"):
                obj = Order()
                obj._deserialize(item)
                self._Orders.append(obj)
        if params.get("SqlGateways") is not None:
            self._SqlGateways = []
            for item in params.get("SqlGateways"):
                obj = SqlGatewayItem()
                obj._deserialize(item)
                self._SqlGateways.append(obj)
        self._WebUIType = params.get("WebUIType")
        self._Type = params.get("Type")
        if params.get("SubEks") is not None:
            self._SubEks = SubEks()
            self._SubEks._deserialize(params.get("SubEks"))
        self._AgentSerialId = params.get("AgentSerialId")
        self._ResourceType = params.get("ResourceType")
        self._BillingResourceMode = params.get("BillingResourceMode")
        self._MemRatio = params.get("MemRatio")
        self._CrossTenantEniMode = params.get("CrossTenantEniMode")
        self._TotalCpu = params.get("TotalCpu")
        self._TotalMem = params.get("TotalMem")
        self._RunningCpu = params.get("RunningCpu")
        self._RunningMem = params.get("RunningMem")
        if params.get("Setats") is not None:
            self._Setats = Setats()
            self._Setats._deserialize(params.get("Setats"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterGroupSetItem(AbstractModel):
    """工作空间集群组信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: clusterGroup 的 SerialId
        :type ClusterId: str
        :param _Name: 集群名称
        :type Name: str
        :param _Region: 地域
        :type Region: str
        :param _Zone: 区
        :type Zone: str
        :param _AppId: 账号 APPID
        :type AppId: int
        :param _OwnerUin: 主账号 UIN
        :type OwnerUin: str
        :param _CreatorUin: 创建账号 UIN
        :type CreatorUin: str
        :param _CuNum: CU 数量
        :type CuNum: int
        :param _CuMem: CU 内存规格
        :type CuMem: int
        :param _Status: 集群状态, 1 未初始化,，3 初始化中，2 运行中
        :type Status: int
        :param _StatusDesc: 状态描述
        :type StatusDesc: str
        :param _CreateTime: 集群创建时间
        :type CreateTime: str
        :param _UpdateTime: 最后一次操作集群的时间
        :type UpdateTime: str
        :param _Remark: 描述
        :type Remark: str
        :param _NetEnvironmentType: 网络
        :type NetEnvironmentType: int
        :param _FreeCuNum: 空闲 CU
        :type FreeCuNum: int
        :param _FreeCu: 细粒度资源下的空闲CU
        :type FreeCu: float
        :param _RunningCu: 运行中CU
        :type RunningCu: float
        :param _PayMode: 付费模式
        :type PayMode: int
        :param _SubEks: 弹性
注意：此字段可能返回 null，表示取不到有效值。
        :type SubEks: :class:`tencentcloud.oceanus.v20190422.models.SubEks`
        :param _BillingResourceMode: 默认 "" 包销模式 "exclusiveSale"
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingResourceMode: str
        :param _TotalCpu: TotalCpu
        :type TotalCpu: float
        :param _TotalMem: TotalMem
        :type TotalMem: float
        :param _RunningCpu: RunningCpu
        :type RunningCpu: float
        :param _RunningMem: RunningMem
        :type RunningMem: float
        """
        self._ClusterId = None
        self._Name = None
        self._Region = None
        self._Zone = None
        self._AppId = None
        self._OwnerUin = None
        self._CreatorUin = None
        self._CuNum = None
        self._CuMem = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Remark = None
        self._NetEnvironmentType = None
        self._FreeCuNum = None
        self._FreeCu = None
        self._RunningCu = None
        self._PayMode = None
        self._SubEks = None
        self._BillingResourceMode = None
        self._TotalCpu = None
        self._TotalMem = None
        self._RunningCpu = None
        self._RunningMem = None

    @property
    def ClusterId(self):
        """clusterGroup 的 SerialId
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Name(self):
        """集群名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AppId(self):
        """账号 APPID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OwnerUin(self):
        """主账号 UIN
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreatorUin(self):
        """创建账号 UIN
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def CuNum(self):
        """CU 数量
        :rtype: int
        """
        return self._CuNum

    @CuNum.setter
    def CuNum(self, CuNum):
        self._CuNum = CuNum

    @property
    def CuMem(self):
        """CU 内存规格
        :rtype: int
        """
        return self._CuMem

    @CuMem.setter
    def CuMem(self, CuMem):
        self._CuMem = CuMem

    @property
    def Status(self):
        """集群状态, 1 未初始化,，3 初始化中，2 运行中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        """集群创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最后一次操作集群的时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Remark(self):
        """描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def NetEnvironmentType(self):
        """网络
        :rtype: int
        """
        return self._NetEnvironmentType

    @NetEnvironmentType.setter
    def NetEnvironmentType(self, NetEnvironmentType):
        self._NetEnvironmentType = NetEnvironmentType

    @property
    def FreeCuNum(self):
        """空闲 CU
        :rtype: int
        """
        return self._FreeCuNum

    @FreeCuNum.setter
    def FreeCuNum(self, FreeCuNum):
        self._FreeCuNum = FreeCuNum

    @property
    def FreeCu(self):
        """细粒度资源下的空闲CU
        :rtype: float
        """
        return self._FreeCu

    @FreeCu.setter
    def FreeCu(self, FreeCu):
        self._FreeCu = FreeCu

    @property
    def RunningCu(self):
        """运行中CU
        :rtype: float
        """
        return self._RunningCu

    @RunningCu.setter
    def RunningCu(self, RunningCu):
        self._RunningCu = RunningCu

    @property
    def PayMode(self):
        """付费模式
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SubEks(self):
        """弹性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.SubEks`
        """
        return self._SubEks

    @SubEks.setter
    def SubEks(self, SubEks):
        self._SubEks = SubEks

    @property
    def BillingResourceMode(self):
        """默认 "" 包销模式 "exclusiveSale"
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BillingResourceMode

    @BillingResourceMode.setter
    def BillingResourceMode(self, BillingResourceMode):
        self._BillingResourceMode = BillingResourceMode

    @property
    def TotalCpu(self):
        """TotalCpu
        :rtype: float
        """
        return self._TotalCpu

    @TotalCpu.setter
    def TotalCpu(self, TotalCpu):
        self._TotalCpu = TotalCpu

    @property
    def TotalMem(self):
        """TotalMem
        :rtype: float
        """
        return self._TotalMem

    @TotalMem.setter
    def TotalMem(self, TotalMem):
        self._TotalMem = TotalMem

    @property
    def RunningCpu(self):
        """RunningCpu
        :rtype: float
        """
        return self._RunningCpu

    @RunningCpu.setter
    def RunningCpu(self, RunningCpu):
        self._RunningCpu = RunningCpu

    @property
    def RunningMem(self):
        """RunningMem
        :rtype: float
        """
        return self._RunningMem

    @RunningMem.setter
    def RunningMem(self, RunningMem):
        self._RunningMem = RunningMem


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Name = params.get("Name")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._AppId = params.get("AppId")
        self._OwnerUin = params.get("OwnerUin")
        self._CreatorUin = params.get("CreatorUin")
        self._CuNum = params.get("CuNum")
        self._CuMem = params.get("CuMem")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Remark = params.get("Remark")
        self._NetEnvironmentType = params.get("NetEnvironmentType")
        self._FreeCuNum = params.get("FreeCuNum")
        self._FreeCu = params.get("FreeCu")
        self._RunningCu = params.get("RunningCu")
        self._PayMode = params.get("PayMode")
        if params.get("SubEks") is not None:
            self._SubEks = SubEks()
            self._SubEks._deserialize(params.get("SubEks"))
        self._BillingResourceMode = params.get("BillingResourceMode")
        self._TotalCpu = params.get("TotalCpu")
        self._TotalMem = params.get("TotalMem")
        self._RunningCpu = params.get("RunningCpu")
        self._RunningMem = params.get("RunningMem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterSession(AbstractModel):
    """session集群信息

    """

    def __init__(self):
        r"""
        :param _ClusterGroupSerialId: 集群SerialId
        :type ClusterGroupSerialId: str
        :param _AppId: 创建者appId
        :type AppId: int
        :param _OwnerUin: 创建者主账号
        :type OwnerUin: str
        :param _CreatorUin: 创建者账号
        :type CreatorUin: str
        :param _Region: 区域
        :type Region: str
        :param _Zone: zone
        :type Zone: str
        :param _Status: Session集群状态
        :type Status: int
        :param _CuNum: Session集群消耗的cu数量
        :type CuNum: float
        :param _FlinkVersion: Session集群的Flink版本
        :type FlinkVersion: str
        :param _WebUIUrl: session集群FlinkUi地址
        :type WebUIUrl: str
        :param _Properties: session集群高级参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param _ResourceRefs: 引用资源
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRefs: list of SessionClusterRefItem
        :param _JobManagerCuSpec: JobManager的规格
        :type JobManagerCuSpec: float
        :param _TaskManagerCuSpec: TaskManager的规格
        :type TaskManagerCuSpec: float
        :param _TaskManagerNum: TaskManager启动的数量
        :type TaskManagerNum: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _JobManagerCpu: JobManagerCpu
        :type JobManagerCpu: float
        :param _JobManagerMem: JobManagerMem
        :type JobManagerMem: float
        :param _TaskManagerCpu: TaskManagerCpu
        :type TaskManagerCpu: float
        :param _TaskManagerMem: TaskManagerMem
        :type TaskManagerMem: float
        """
        self._ClusterGroupSerialId = None
        self._AppId = None
        self._OwnerUin = None
        self._CreatorUin = None
        self._Region = None
        self._Zone = None
        self._Status = None
        self._CuNum = None
        self._FlinkVersion = None
        self._WebUIUrl = None
        self._Properties = None
        self._ResourceRefs = None
        self._JobManagerCuSpec = None
        self._TaskManagerCuSpec = None
        self._TaskManagerNum = None
        self._CreateTime = None
        self._UpdateTime = None
        self._JobManagerCpu = None
        self._JobManagerMem = None
        self._TaskManagerCpu = None
        self._TaskManagerMem = None

    @property
    def ClusterGroupSerialId(self):
        """集群SerialId
        :rtype: str
        """
        return self._ClusterGroupSerialId

    @ClusterGroupSerialId.setter
    def ClusterGroupSerialId(self, ClusterGroupSerialId):
        self._ClusterGroupSerialId = ClusterGroupSerialId

    @property
    def AppId(self):
        """创建者appId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OwnerUin(self):
        """创建者主账号
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreatorUin(self):
        """创建者账号
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def Region(self):
        """区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        """Session集群状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CuNum(self):
        """Session集群消耗的cu数量
        :rtype: float
        """
        return self._CuNum

    @CuNum.setter
    def CuNum(self, CuNum):
        self._CuNum = CuNum

    @property
    def FlinkVersion(self):
        """Session集群的Flink版本
        :rtype: str
        """
        return self._FlinkVersion

    @FlinkVersion.setter
    def FlinkVersion(self, FlinkVersion):
        self._FlinkVersion = FlinkVersion

    @property
    def WebUIUrl(self):
        """session集群FlinkUi地址
        :rtype: str
        """
        return self._WebUIUrl

    @WebUIUrl.setter
    def WebUIUrl(self, WebUIUrl):
        self._WebUIUrl = WebUIUrl

    @property
    def Properties(self):
        """session集群高级参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Property
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def ResourceRefs(self):
        """引用资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SessionClusterRefItem
        """
        return self._ResourceRefs

    @ResourceRefs.setter
    def ResourceRefs(self, ResourceRefs):
        self._ResourceRefs = ResourceRefs

    @property
    def JobManagerCuSpec(self):
        """JobManager的规格
        :rtype: float
        """
        return self._JobManagerCuSpec

    @JobManagerCuSpec.setter
    def JobManagerCuSpec(self, JobManagerCuSpec):
        self._JobManagerCuSpec = JobManagerCuSpec

    @property
    def TaskManagerCuSpec(self):
        """TaskManager的规格
        :rtype: float
        """
        return self._TaskManagerCuSpec

    @TaskManagerCuSpec.setter
    def TaskManagerCuSpec(self, TaskManagerCuSpec):
        self._TaskManagerCuSpec = TaskManagerCuSpec

    @property
    def TaskManagerNum(self):
        """TaskManager启动的数量
        :rtype: int
        """
        return self._TaskManagerNum

    @TaskManagerNum.setter
    def TaskManagerNum(self, TaskManagerNum):
        self._TaskManagerNum = TaskManagerNum

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def JobManagerCpu(self):
        """JobManagerCpu
        :rtype: float
        """
        return self._JobManagerCpu

    @JobManagerCpu.setter
    def JobManagerCpu(self, JobManagerCpu):
        self._JobManagerCpu = JobManagerCpu

    @property
    def JobManagerMem(self):
        """JobManagerMem
        :rtype: float
        """
        return self._JobManagerMem

    @JobManagerMem.setter
    def JobManagerMem(self, JobManagerMem):
        self._JobManagerMem = JobManagerMem

    @property
    def TaskManagerCpu(self):
        """TaskManagerCpu
        :rtype: float
        """
        return self._TaskManagerCpu

    @TaskManagerCpu.setter
    def TaskManagerCpu(self, TaskManagerCpu):
        self._TaskManagerCpu = TaskManagerCpu

    @property
    def TaskManagerMem(self):
        """TaskManagerMem
        :rtype: float
        """
        return self._TaskManagerMem

    @TaskManagerMem.setter
    def TaskManagerMem(self, TaskManagerMem):
        self._TaskManagerMem = TaskManagerMem


    def _deserialize(self, params):
        self._ClusterGroupSerialId = params.get("ClusterGroupSerialId")
        self._AppId = params.get("AppId")
        self._OwnerUin = params.get("OwnerUin")
        self._CreatorUin = params.get("CreatorUin")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        self._CuNum = params.get("CuNum")
        self._FlinkVersion = params.get("FlinkVersion")
        self._WebUIUrl = params.get("WebUIUrl")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        if params.get("ResourceRefs") is not None:
            self._ResourceRefs = []
            for item in params.get("ResourceRefs"):
                obj = SessionClusterRefItem()
                obj._deserialize(item)
                self._ResourceRefs.append(obj)
        self._JobManagerCuSpec = params.get("JobManagerCuSpec")
        self._TaskManagerCuSpec = params.get("TaskManagerCuSpec")
        self._TaskManagerNum = params.get("TaskManagerNum")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._JobManagerCpu = params.get("JobManagerCpu")
        self._JobManagerMem = params.get("JobManagerMem")
        self._TaskManagerCpu = params.get("TaskManagerCpu")
        self._TaskManagerMem = params.get("TaskManagerMem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterVersion(AbstractModel):
    """集群的版本相关信息

    """

    def __init__(self):
        r"""
        :param _Flink: 集群的Flink版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Flink: str
        :param _SupportedFlink: 集群支持的Flink版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportedFlink: list of str
        """
        self._Flink = None
        self._SupportedFlink = None

    @property
    def Flink(self):
        """集群的Flink版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Flink

    @Flink.setter
    def Flink(self, Flink):
        self._Flink = Flink

    @property
    def SupportedFlink(self):
        """集群支持的Flink版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SupportedFlink

    @SupportedFlink.setter
    def SupportedFlink(self, SupportedFlink):
        self._SupportedFlink = SupportedFlink


    def _deserialize(self, params):
        self._Flink = params.get("Flink")
        self._SupportedFlink = params.get("SupportedFlink")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyJobItem(AbstractModel):
    """复制作业单条明细

    """

    def __init__(self):
        r"""
        :param _SourceId: 需要复制的作业serial id
        :type SourceId: str
        :param _TargetClusterId: 目标集群的cluster serial id
        :type TargetClusterId: str
        :param _SourceName: 需要复制的作业名称
        :type SourceName: str
        :param _TargetName: 新作业的名称
        :type TargetName: str
        :param _TargetFolderId: 新作业的目录id
        :type TargetFolderId: str
        :param _JobType: 源作业类型
        :type JobType: int
        """
        self._SourceId = None
        self._TargetClusterId = None
        self._SourceName = None
        self._TargetName = None
        self._TargetFolderId = None
        self._JobType = None

    @property
    def SourceId(self):
        """需要复制的作业serial id
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def TargetClusterId(self):
        """目标集群的cluster serial id
        :rtype: str
        """
        return self._TargetClusterId

    @TargetClusterId.setter
    def TargetClusterId(self, TargetClusterId):
        self._TargetClusterId = TargetClusterId

    @property
    def SourceName(self):
        """需要复制的作业名称
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def TargetName(self):
        """新作业的名称
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def TargetFolderId(self):
        """新作业的目录id
        :rtype: str
        """
        return self._TargetFolderId

    @TargetFolderId.setter
    def TargetFolderId(self, TargetFolderId):
        self._TargetFolderId = TargetFolderId

    @property
    def JobType(self):
        """源作业类型
        :rtype: int
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType


    def _deserialize(self, params):
        self._SourceId = params.get("SourceId")
        self._TargetClusterId = params.get("TargetClusterId")
        self._SourceName = params.get("SourceName")
        self._TargetName = params.get("TargetName")
        self._TargetFolderId = params.get("TargetFolderId")
        self._JobType = params.get("JobType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyJobResult(AbstractModel):
    """复制作业单条明细结果

    """

    def __init__(self):
        r"""
        :param _JobId: 原作业id
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _JobName: 原作业名称
注意：此字段可能返回 null，表示取不到有效值。
        :type JobName: str
        :param _TargetJobName: 新作业名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetJobName: str
        :param _TargetJobId: 新作业id
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetJobId: str
        :param _Message: 失败时候的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Result: 0 成功  -1 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: int
        :param _ClusterName: 目标集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _ClusterId: 目标集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _JobType: 作业类型
注意：此字段可能返回 null，表示取不到有效值。
        :type JobType: int
        """
        self._JobId = None
        self._JobName = None
        self._TargetJobName = None
        self._TargetJobId = None
        self._Message = None
        self._Result = None
        self._ClusterName = None
        self._ClusterId = None
        self._JobType = None

    @property
    def JobId(self):
        """原作业id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """原作业名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def TargetJobName(self):
        """新作业名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetJobName

    @TargetJobName.setter
    def TargetJobName(self, TargetJobName):
        self._TargetJobName = TargetJobName

    @property
    def TargetJobId(self):
        """新作业id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetJobId

    @TargetJobId.setter
    def TargetJobId(self, TargetJobId):
        self._TargetJobId = TargetJobId

    @property
    def Message(self):
        """失败时候的信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Result(self):
        """0 成功  -1 失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ClusterName(self):
        """目标集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterId(self):
        """目标集群id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def JobType(self):
        """作业类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._TargetJobName = params.get("TargetJobName")
        self._TargetJobId = params.get("TargetJobId")
        self._Message = params.get("Message")
        self._Result = params.get("Result")
        self._ClusterName = params.get("ClusterName")
        self._ClusterId = params.get("ClusterId")
        self._JobType = params.get("JobType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyJobsRequest(AbstractModel):
    """CopyJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobItems: 复制明细列表
        :type JobItems: list of CopyJobItem
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _TargetWorkspaceId: 目标工作空间 SerialId
        :type TargetWorkspaceId: str
        """
        self._JobItems = None
        self._WorkSpaceId = None
        self._TargetWorkspaceId = None

    @property
    def JobItems(self):
        """复制明细列表
        :rtype: list of CopyJobItem
        """
        return self._JobItems

    @JobItems.setter
    def JobItems(self, JobItems):
        self._JobItems = JobItems

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def TargetWorkspaceId(self):
        """目标工作空间 SerialId
        :rtype: str
        """
        return self._TargetWorkspaceId

    @TargetWorkspaceId.setter
    def TargetWorkspaceId(self, TargetWorkspaceId):
        self._TargetWorkspaceId = TargetWorkspaceId


    def _deserialize(self, params):
        if params.get("JobItems") is not None:
            self._JobItems = []
            for item in params.get("JobItems"):
                obj = CopyJobItem()
                obj._deserialize(item)
                self._JobItems.append(obj)
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._TargetWorkspaceId = params.get("TargetWorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyJobsResponse(AbstractModel):
    """CopyJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessCount: 成功条数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param _FailCount: 失败条数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailCount: int
        :param _CopyJobsResults: 结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CopyJobsResults: list of CopyJobResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessCount = None
        self._FailCount = None
        self._CopyJobsResults = None
        self._RequestId = None

    @property
    def SuccessCount(self):
        """成功条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailCount(self):
        """失败条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FailCount

    @FailCount.setter
    def FailCount(self, FailCount):
        self._FailCount = FailCount

    @property
    def CopyJobsResults(self):
        """结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CopyJobResult
        """
        return self._CopyJobsResults

    @CopyJobsResults.setter
    def CopyJobsResults(self, CopyJobsResults):
        self._CopyJobsResults = CopyJobsResults

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessCount = params.get("SuccessCount")
        self._FailCount = params.get("FailCount")
        if params.get("CopyJobsResults") is not None:
            self._CopyJobsResults = []
            for item in params.get("CopyJobsResults"):
                obj = CopyJobResult()
                obj._deserialize(item)
                self._CopyJobsResults.append(obj)
        self._RequestId = params.get("RequestId")


class CreateFolderRequest(AbstractModel):
    """CreateFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FolderName: 新建文件夹名
        :type FolderName: str
        :param _ParentId: 新建文件夹的父目录ID（根目录为"root"）
        :type ParentId: str
        :param _FolderType: 文件夹类型，0是任务文件夹，1是依赖文件夹
        :type FolderType: int
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._FolderName = None
        self._ParentId = None
        self._FolderType = None
        self._WorkSpaceId = None

    @property
    def FolderName(self):
        """新建文件夹名
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def ParentId(self):
        """新建文件夹的父目录ID（根目录为"root"）
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def FolderType(self):
        """文件夹类型，0是任务文件夹，1是依赖文件夹
        :rtype: int
        """
        return self._FolderType

    @FolderType.setter
    def FolderType(self, FolderType):
        self._FolderType = FolderType

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._FolderName = params.get("FolderName")
        self._ParentId = params.get("ParentId")
        self._FolderType = params.get("FolderType")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFolderResponse(AbstractModel):
    """CreateFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FolderId: 新建文件夹的唯一ID
        :type FolderId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FolderId = None
        self._RequestId = None

    @property
    def FolderId(self):
        """新建文件夹的唯一ID
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._RequestId = params.get("RequestId")


class CreateJobConfigRequest(AbstractModel):
    """CreateJobConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业Id
        :type JobId: str
        :param _EntrypointClass: 主类
        :type EntrypointClass: str
        :param _ProgramArgs: 主类入参，需要区分下Sql作业配置，Jar作业配置，Python作业配置，具体参考下面的示例值
        :type ProgramArgs: str
        :param _Remark: 备注
        :type Remark: str
        :param _ResourceRefs: 资源引用数组
        :type ResourceRefs: list of ResourceRef
        :param _DefaultParallelism: 作业默认并行度
        :type DefaultParallelism: int
        :param _Properties: 系统参数
        :type Properties: list of Property
        :param _AutoDelete: 1: 作业配置达到上限之后，自动删除可删除的最早版本
        :type AutoDelete: int
        :param _COSBucket: 作业使用的 COS 存储桶名
        :type COSBucket: str
        :param _LogCollect: 是否采集作业日志
        :type LogCollect: bool
        :param _JobManagerSpec: JobManager规格
        :type JobManagerSpec: float
        :param _TaskManagerSpec: TaskManager规格
        :type TaskManagerSpec: float
        :param _ClsLogsetId: CLS日志集ID
        :type ClsLogsetId: str
        :param _ClsTopicId: CLS日志主题ID
        :type ClsTopicId: str
        :param _LogCollectType: 日志采集类型 2：CLS；3：COS
        :type LogCollectType: int
        :param _PythonVersion: pyflink作业运行时使用的python版本
        :type PythonVersion: str
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _LogLevel: 日志级别
        :type LogLevel: str
        :param _AutoRecover: Oceanus 平台恢复作业开关 1:开启 -1: 关闭
        :type AutoRecover: int
        :param _ClazzLevels: 类日志级别
        :type ClazzLevels: list of ClazzLevel
        :param _ExpertModeOn: 是否打开专家模式
        :type ExpertModeOn: bool
        :param _ExpertModeConfiguration: 专家模式的配置
        :type ExpertModeConfiguration: :class:`tencentcloud.oceanus.v20190422.models.ExpertModeConfiguration`
        :param _TraceModeOn: trace链路
        :type TraceModeOn: bool
        :param _TraceModeConfiguration: trace链路配置
        :type TraceModeConfiguration: :class:`tencentcloud.oceanus.v20190422.models.TraceModeConfiguration`
        :param _CheckpointRetainedNum: checkpoint保留个数
        :type CheckpointRetainedNum: int
        :param _JobGraph: 算子拓扑图
        :type JobGraph: :class:`tencentcloud.oceanus.v20190422.models.JobGraph`
        :param _EsServerlessIndex: es索引名称
        :type EsServerlessIndex: str
        :param _EsServerlessSpace: es索引空间
        :type EsServerlessSpace: str
        :param _FlinkVersion: flink版本
        :type FlinkVersion: str
        :param _JobManagerCpu: JobManager cpu
        :type JobManagerCpu: float
        :param _JobManagerMem: JobManager 内存
        :type JobManagerMem: float
        :param _TaskManagerCpu: TaskManager cpu
        :type TaskManagerCpu: float
        :param _TaskManagerMem: TaskManager 内存
        :type TaskManagerMem: float
        """
        self._JobId = None
        self._EntrypointClass = None
        self._ProgramArgs = None
        self._Remark = None
        self._ResourceRefs = None
        self._DefaultParallelism = None
        self._Properties = None
        self._AutoDelete = None
        self._COSBucket = None
        self._LogCollect = None
        self._JobManagerSpec = None
        self._TaskManagerSpec = None
        self._ClsLogsetId = None
        self._ClsTopicId = None
        self._LogCollectType = None
        self._PythonVersion = None
        self._WorkSpaceId = None
        self._LogLevel = None
        self._AutoRecover = None
        self._ClazzLevels = None
        self._ExpertModeOn = None
        self._ExpertModeConfiguration = None
        self._TraceModeOn = None
        self._TraceModeConfiguration = None
        self._CheckpointRetainedNum = None
        self._JobGraph = None
        self._EsServerlessIndex = None
        self._EsServerlessSpace = None
        self._FlinkVersion = None
        self._JobManagerCpu = None
        self._JobManagerMem = None
        self._TaskManagerCpu = None
        self._TaskManagerMem = None

    @property
    def JobId(self):
        """作业Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def EntrypointClass(self):
        """主类
        :rtype: str
        """
        return self._EntrypointClass

    @EntrypointClass.setter
    def EntrypointClass(self, EntrypointClass):
        self._EntrypointClass = EntrypointClass

    @property
    def ProgramArgs(self):
        """主类入参，需要区分下Sql作业配置，Jar作业配置，Python作业配置，具体参考下面的示例值
        :rtype: str
        """
        return self._ProgramArgs

    @ProgramArgs.setter
    def ProgramArgs(self, ProgramArgs):
        self._ProgramArgs = ProgramArgs

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ResourceRefs(self):
        """资源引用数组
        :rtype: list of ResourceRef
        """
        return self._ResourceRefs

    @ResourceRefs.setter
    def ResourceRefs(self, ResourceRefs):
        self._ResourceRefs = ResourceRefs

    @property
    def DefaultParallelism(self):
        """作业默认并行度
        :rtype: int
        """
        return self._DefaultParallelism

    @DefaultParallelism.setter
    def DefaultParallelism(self, DefaultParallelism):
        self._DefaultParallelism = DefaultParallelism

    @property
    def Properties(self):
        """系统参数
        :rtype: list of Property
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def AutoDelete(self):
        """1: 作业配置达到上限之后，自动删除可删除的最早版本
        :rtype: int
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def COSBucket(self):
        """作业使用的 COS 存储桶名
        :rtype: str
        """
        return self._COSBucket

    @COSBucket.setter
    def COSBucket(self, COSBucket):
        self._COSBucket = COSBucket

    @property
    def LogCollect(self):
        """是否采集作业日志
        :rtype: bool
        """
        return self._LogCollect

    @LogCollect.setter
    def LogCollect(self, LogCollect):
        self._LogCollect = LogCollect

    @property
    def JobManagerSpec(self):
        """JobManager规格
        :rtype: float
        """
        return self._JobManagerSpec

    @JobManagerSpec.setter
    def JobManagerSpec(self, JobManagerSpec):
        self._JobManagerSpec = JobManagerSpec

    @property
    def TaskManagerSpec(self):
        """TaskManager规格
        :rtype: float
        """
        return self._TaskManagerSpec

    @TaskManagerSpec.setter
    def TaskManagerSpec(self, TaskManagerSpec):
        self._TaskManagerSpec = TaskManagerSpec

    @property
    def ClsLogsetId(self):
        """CLS日志集ID
        :rtype: str
        """
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsTopicId(self):
        """CLS日志主题ID
        :rtype: str
        """
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def LogCollectType(self):
        """日志采集类型 2：CLS；3：COS
        :rtype: int
        """
        return self._LogCollectType

    @LogCollectType.setter
    def LogCollectType(self, LogCollectType):
        self._LogCollectType = LogCollectType

    @property
    def PythonVersion(self):
        """pyflink作业运行时使用的python版本
        :rtype: str
        """
        return self._PythonVersion

    @PythonVersion.setter
    def PythonVersion(self, PythonVersion):
        self._PythonVersion = PythonVersion

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def LogLevel(self):
        """日志级别
        :rtype: str
        """
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def AutoRecover(self):
        """Oceanus 平台恢复作业开关 1:开启 -1: 关闭
        :rtype: int
        """
        return self._AutoRecover

    @AutoRecover.setter
    def AutoRecover(self, AutoRecover):
        self._AutoRecover = AutoRecover

    @property
    def ClazzLevels(self):
        """类日志级别
        :rtype: list of ClazzLevel
        """
        return self._ClazzLevels

    @ClazzLevels.setter
    def ClazzLevels(self, ClazzLevels):
        self._ClazzLevels = ClazzLevels

    @property
    def ExpertModeOn(self):
        """是否打开专家模式
        :rtype: bool
        """
        return self._ExpertModeOn

    @ExpertModeOn.setter
    def ExpertModeOn(self, ExpertModeOn):
        self._ExpertModeOn = ExpertModeOn

    @property
    def ExpertModeConfiguration(self):
        """专家模式的配置
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.ExpertModeConfiguration`
        """
        return self._ExpertModeConfiguration

    @ExpertModeConfiguration.setter
    def ExpertModeConfiguration(self, ExpertModeConfiguration):
        self._ExpertModeConfiguration = ExpertModeConfiguration

    @property
    def TraceModeOn(self):
        """trace链路
        :rtype: bool
        """
        return self._TraceModeOn

    @TraceModeOn.setter
    def TraceModeOn(self, TraceModeOn):
        self._TraceModeOn = TraceModeOn

    @property
    def TraceModeConfiguration(self):
        """trace链路配置
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.TraceModeConfiguration`
        """
        return self._TraceModeConfiguration

    @TraceModeConfiguration.setter
    def TraceModeConfiguration(self, TraceModeConfiguration):
        self._TraceModeConfiguration = TraceModeConfiguration

    @property
    def CheckpointRetainedNum(self):
        """checkpoint保留个数
        :rtype: int
        """
        return self._CheckpointRetainedNum

    @CheckpointRetainedNum.setter
    def CheckpointRetainedNum(self, CheckpointRetainedNum):
        self._CheckpointRetainedNum = CheckpointRetainedNum

    @property
    def JobGraph(self):
        """算子拓扑图
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.JobGraph`
        """
        return self._JobGraph

    @JobGraph.setter
    def JobGraph(self, JobGraph):
        self._JobGraph = JobGraph

    @property
    def EsServerlessIndex(self):
        """es索引名称
        :rtype: str
        """
        return self._EsServerlessIndex

    @EsServerlessIndex.setter
    def EsServerlessIndex(self, EsServerlessIndex):
        self._EsServerlessIndex = EsServerlessIndex

    @property
    def EsServerlessSpace(self):
        """es索引空间
        :rtype: str
        """
        return self._EsServerlessSpace

    @EsServerlessSpace.setter
    def EsServerlessSpace(self, EsServerlessSpace):
        self._EsServerlessSpace = EsServerlessSpace

    @property
    def FlinkVersion(self):
        """flink版本
        :rtype: str
        """
        return self._FlinkVersion

    @FlinkVersion.setter
    def FlinkVersion(self, FlinkVersion):
        self._FlinkVersion = FlinkVersion

    @property
    def JobManagerCpu(self):
        """JobManager cpu
        :rtype: float
        """
        return self._JobManagerCpu

    @JobManagerCpu.setter
    def JobManagerCpu(self, JobManagerCpu):
        self._JobManagerCpu = JobManagerCpu

    @property
    def JobManagerMem(self):
        """JobManager 内存
        :rtype: float
        """
        return self._JobManagerMem

    @JobManagerMem.setter
    def JobManagerMem(self, JobManagerMem):
        self._JobManagerMem = JobManagerMem

    @property
    def TaskManagerCpu(self):
        """TaskManager cpu
        :rtype: float
        """
        return self._TaskManagerCpu

    @TaskManagerCpu.setter
    def TaskManagerCpu(self, TaskManagerCpu):
        self._TaskManagerCpu = TaskManagerCpu

    @property
    def TaskManagerMem(self):
        """TaskManager 内存
        :rtype: float
        """
        return self._TaskManagerMem

    @TaskManagerMem.setter
    def TaskManagerMem(self, TaskManagerMem):
        self._TaskManagerMem = TaskManagerMem


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._EntrypointClass = params.get("EntrypointClass")
        self._ProgramArgs = params.get("ProgramArgs")
        self._Remark = params.get("Remark")
        if params.get("ResourceRefs") is not None:
            self._ResourceRefs = []
            for item in params.get("ResourceRefs"):
                obj = ResourceRef()
                obj._deserialize(item)
                self._ResourceRefs.append(obj)
        self._DefaultParallelism = params.get("DefaultParallelism")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._AutoDelete = params.get("AutoDelete")
        self._COSBucket = params.get("COSBucket")
        self._LogCollect = params.get("LogCollect")
        self._JobManagerSpec = params.get("JobManagerSpec")
        self._TaskManagerSpec = params.get("TaskManagerSpec")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._ClsTopicId = params.get("ClsTopicId")
        self._LogCollectType = params.get("LogCollectType")
        self._PythonVersion = params.get("PythonVersion")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._LogLevel = params.get("LogLevel")
        self._AutoRecover = params.get("AutoRecover")
        if params.get("ClazzLevels") is not None:
            self._ClazzLevels = []
            for item in params.get("ClazzLevels"):
                obj = ClazzLevel()
                obj._deserialize(item)
                self._ClazzLevels.append(obj)
        self._ExpertModeOn = params.get("ExpertModeOn")
        if params.get("ExpertModeConfiguration") is not None:
            self._ExpertModeConfiguration = ExpertModeConfiguration()
            self._ExpertModeConfiguration._deserialize(params.get("ExpertModeConfiguration"))
        self._TraceModeOn = params.get("TraceModeOn")
        if params.get("TraceModeConfiguration") is not None:
            self._TraceModeConfiguration = TraceModeConfiguration()
            self._TraceModeConfiguration._deserialize(params.get("TraceModeConfiguration"))
        self._CheckpointRetainedNum = params.get("CheckpointRetainedNum")
        if params.get("JobGraph") is not None:
            self._JobGraph = JobGraph()
            self._JobGraph._deserialize(params.get("JobGraph"))
        self._EsServerlessIndex = params.get("EsServerlessIndex")
        self._EsServerlessSpace = params.get("EsServerlessSpace")
        self._FlinkVersion = params.get("FlinkVersion")
        self._JobManagerCpu = params.get("JobManagerCpu")
        self._JobManagerMem = params.get("JobManagerMem")
        self._TaskManagerCpu = params.get("TaskManagerCpu")
        self._TaskManagerMem = params.get("TaskManagerMem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateJobConfigResponse(AbstractModel):
    """CreateJobConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: 作业配置版本号
        :type Version: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Version = None
        self._RequestId = None

    @property
    def Version(self):
        """作业配置版本号
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._RequestId = params.get("RequestId")


class CreateJobRequest(AbstractModel):
    """CreateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 作业名称，允许输入长度小于50个字符的中文、英文、数字、-（横线）、_（下划线）、.（点），且符号必须半角字符。注意作业名不能和现有作业同名
        :type Name: str
        :param _JobType: 作业的类型，1 表示 SQL 作业，2 表示 JAR 作业
        :type JobType: int
        :param _ClusterType: 集群的类型，1 表示共享集群，2 表示独享集群
        :type ClusterType: int
        :param _ClusterId: 当 ClusterType=2 时，必选，用来指定该作业提交的独享集群 ID
        :type ClusterId: str
        :param _CuMem: 设置每 CU 的内存规格，单位为 GB，支持 2、4、8、16（需申请开通白名单后使用）。默认为 4，即 1 CU 对应 4 GB 的运行内存
        :type CuMem: int
        :param _Remark: 作业的备注信息，可以随意设置
        :type Remark: str
        :param _FolderId: 作业名所属文件夹ID，根目录为"root"
        :type FolderId: str
        :param _FlinkVersion: 作业运行的Flink版本
        :type FlinkVersion: str
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _Tags: 作业标签
        :type Tags: list of Tag
        :param _Description: 作业描述
        :type Description: str
        :param _OpenJobDefaultAlarm: 开启默认告警
        :type OpenJobDefaultAlarm: int
        """
        self._Name = None
        self._JobType = None
        self._ClusterType = None
        self._ClusterId = None
        self._CuMem = None
        self._Remark = None
        self._FolderId = None
        self._FlinkVersion = None
        self._WorkSpaceId = None
        self._Tags = None
        self._Description = None
        self._OpenJobDefaultAlarm = None

    @property
    def Name(self):
        """作业名称，允许输入长度小于50个字符的中文、英文、数字、-（横线）、_（下划线）、.（点），且符号必须半角字符。注意作业名不能和现有作业同名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def JobType(self):
        """作业的类型，1 表示 SQL 作业，2 表示 JAR 作业
        :rtype: int
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def ClusterType(self):
        """集群的类型，1 表示共享集群，2 表示独享集群
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterId(self):
        """当 ClusterType=2 时，必选，用来指定该作业提交的独享集群 ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CuMem(self):
        """设置每 CU 的内存规格，单位为 GB，支持 2、4、8、16（需申请开通白名单后使用）。默认为 4，即 1 CU 对应 4 GB 的运行内存
        :rtype: int
        """
        return self._CuMem

    @CuMem.setter
    def CuMem(self, CuMem):
        self._CuMem = CuMem

    @property
    def Remark(self):
        """作业的备注信息，可以随意设置
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def FolderId(self):
        """作业名所属文件夹ID，根目录为"root"
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FlinkVersion(self):
        """作业运行的Flink版本
        :rtype: str
        """
        return self._FlinkVersion

    @FlinkVersion.setter
    def FlinkVersion(self, FlinkVersion):
        self._FlinkVersion = FlinkVersion

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def Tags(self):
        """作业标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Description(self):
        """作业描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OpenJobDefaultAlarm(self):
        """开启默认告警
        :rtype: int
        """
        return self._OpenJobDefaultAlarm

    @OpenJobDefaultAlarm.setter
    def OpenJobDefaultAlarm(self, OpenJobDefaultAlarm):
        self._OpenJobDefaultAlarm = OpenJobDefaultAlarm


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._JobType = params.get("JobType")
        self._ClusterType = params.get("ClusterType")
        self._ClusterId = params.get("ClusterId")
        self._CuMem = params.get("CuMem")
        self._Remark = params.get("Remark")
        self._FolderId = params.get("FolderId")
        self._FlinkVersion = params.get("FlinkVersion")
        self._WorkSpaceId = params.get("WorkSpaceId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Description = params.get("Description")
        self._OpenJobDefaultAlarm = params.get("OpenJobDefaultAlarm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateJobResponse(AbstractModel):
    """CreateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业Id
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        """作业Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class CreateResourceConfigRequest(AbstractModel):
    """CreateResourceConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _ResourceLoc: 位置信息
        :type ResourceLoc: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        :param _Remark: 资源描述信息
        :type Remark: str
        :param _AutoDelete: 1： 资源版本达到上限，自动删除最早可删除的版本
        :type AutoDelete: int
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._ResourceId = None
        self._ResourceLoc = None
        self._Remark = None
        self._AutoDelete = None
        self._WorkSpaceId = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceLoc(self):
        """位置信息
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        """
        return self._ResourceLoc

    @ResourceLoc.setter
    def ResourceLoc(self, ResourceLoc):
        self._ResourceLoc = ResourceLoc

    @property
    def Remark(self):
        """资源描述信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AutoDelete(self):
        """1： 资源版本达到上限，自动删除最早可删除的版本
        :rtype: int
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        if params.get("ResourceLoc") is not None:
            self._ResourceLoc = ResourceLoc()
            self._ResourceLoc._deserialize(params.get("ResourceLoc"))
        self._Remark = params.get("Remark")
        self._AutoDelete = params.get("AutoDelete")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceConfigResponse(AbstractModel):
    """CreateResourceConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: 资源版本ID
        :type Version: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Version = None
        self._RequestId = None

    @property
    def Version(self):
        """资源版本ID
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._RequestId = params.get("RequestId")


class CreateResourceRequest(AbstractModel):
    """CreateResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceLoc: 资源位置
        :type ResourceLoc: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        :param _ResourceType: 资源类型。目前只支持 JAR，取值为 1
        :type ResourceType: int
        :param _Remark: 资源描述
        :type Remark: str
        :param _Name: 资源名称
        :type Name: str
        :param _ResourceConfigRemark: 资源版本描述
        :type ResourceConfigRemark: str
        :param _FolderId: 目录ID
        :type FolderId: str
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._ResourceLoc = None
        self._ResourceType = None
        self._Remark = None
        self._Name = None
        self._ResourceConfigRemark = None
        self._FolderId = None
        self._WorkSpaceId = None

    @property
    def ResourceLoc(self):
        """资源位置
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        """
        return self._ResourceLoc

    @ResourceLoc.setter
    def ResourceLoc(self, ResourceLoc):
        self._ResourceLoc = ResourceLoc

    @property
    def ResourceType(self):
        """资源类型。目前只支持 JAR，取值为 1
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Remark(self):
        """资源描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Name(self):
        """资源名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ResourceConfigRemark(self):
        """资源版本描述
        :rtype: str
        """
        return self._ResourceConfigRemark

    @ResourceConfigRemark.setter
    def ResourceConfigRemark(self, ResourceConfigRemark):
        self._ResourceConfigRemark = ResourceConfigRemark

    @property
    def FolderId(self):
        """目录ID
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        if params.get("ResourceLoc") is not None:
            self._ResourceLoc = ResourceLoc()
            self._ResourceLoc._deserialize(params.get("ResourceLoc"))
        self._ResourceType = params.get("ResourceType")
        self._Remark = params.get("Remark")
        self._Name = params.get("Name")
        self._ResourceConfigRemark = params.get("ResourceConfigRemark")
        self._FolderId = params.get("FolderId")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceResponse(AbstractModel):
    """CreateResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _Version: 资源版本
        :type Version: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceId = None
        self._Version = None
        self._RequestId = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Version(self):
        """资源版本
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Version = params.get("Version")
        self._RequestId = params.get("RequestId")


class CreateWorkSpaceRequest(AbstractModel):
    """CreateWorkSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkSpaceName: 工作空间名称
        :type WorkSpaceName: str
        :param _Description: 项目空间备注
        :type Description: str
        """
        self._WorkSpaceName = None
        self._Description = None

    @property
    def WorkSpaceName(self):
        """工作空间名称
        :rtype: str
        """
        return self._WorkSpaceName

    @WorkSpaceName.setter
    def WorkSpaceName(self, WorkSpaceName):
        self._WorkSpaceName = WorkSpaceName

    @property
    def Description(self):
        """项目空间备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._WorkSpaceName = params.get("WorkSpaceName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkSpaceResponse(AbstractModel):
    """CreateWorkSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkSpaceId = None
        self._RequestId = None

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._RequestId = params.get("RequestId")


class DeleteFoldersRequest(AbstractModel):
    """DeleteFolders请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FolderIds: 需删除的文件夹唯一ID
        :type FolderIds: list of str
        :param _FolderType: 文件夹类型，0是任务文件夹，1是依赖文件夹
        :type FolderType: int
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._FolderIds = None
        self._FolderType = None
        self._WorkSpaceId = None

    @property
    def FolderIds(self):
        """需删除的文件夹唯一ID
        :rtype: list of str
        """
        return self._FolderIds

    @FolderIds.setter
    def FolderIds(self, FolderIds):
        self._FolderIds = FolderIds

    @property
    def FolderType(self):
        """文件夹类型，0是任务文件夹，1是依赖文件夹
        :rtype: int
        """
        return self._FolderType

    @FolderType.setter
    def FolderType(self, FolderType):
        self._FolderType = FolderType

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._FolderIds = params.get("FolderIds")
        self._FolderType = params.get("FolderType")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFoldersResponse(AbstractModel):
    """DeleteFolders返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteJobConfigsRequest(AbstractModel):
    """DeleteJobConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        :param _JobConfigVersions: 作业配置版本数组
        :type JobConfigVersions: list of int
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._JobId = None
        self._JobConfigVersions = None
        self._WorkSpaceId = None

    @property
    def JobId(self):
        """作业ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobConfigVersions(self):
        """作业配置版本数组
        :rtype: list of int
        """
        return self._JobConfigVersions

    @JobConfigVersions.setter
    def JobConfigVersions(self, JobConfigVersions):
        self._JobConfigVersions = JobConfigVersions

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobConfigVersions = params.get("JobConfigVersions")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteJobConfigsResponse(AbstractModel):
    """DeleteJobConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteJobsRequest(AbstractModel):
    """DeleteJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobIds: 作业Id列表
        :type JobIds: list of str
        :param _WorkSpaceId: 工作空间Id
        :type WorkSpaceId: str
        :param _JobNames: 作业名称列表
        :type JobNames: list of str
        """
        self._JobIds = None
        self._WorkSpaceId = None
        self._JobNames = None

    @property
    def JobIds(self):
        """作业Id列表
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def WorkSpaceId(self):
        """工作空间Id
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def JobNames(self):
        """作业名称列表
        :rtype: list of str
        """
        return self._JobNames

    @JobNames.setter
    def JobNames(self, JobNames):
        self._JobNames = JobNames


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._JobNames = params.get("JobNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteJobsResponse(AbstractModel):
    """DeleteJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteResourceConfigsRequest(AbstractModel):
    """DeleteResourceConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _ResourceConfigVersions: 资源版本数组
        :type ResourceConfigVersions: list of int
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._ResourceId = None
        self._ResourceConfigVersions = None
        self._WorkSpaceId = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceConfigVersions(self):
        """资源版本数组
        :rtype: list of int
        """
        return self._ResourceConfigVersions

    @ResourceConfigVersions.setter
    def ResourceConfigVersions(self, ResourceConfigVersions):
        self._ResourceConfigVersions = ResourceConfigVersions

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceConfigVersions = params.get("ResourceConfigVersions")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceConfigsResponse(AbstractModel):
    """DeleteResourceConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteResourcesRequest(AbstractModel):
    """DeleteResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 待删除资源ID列表
        :type ResourceIds: list of str
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._ResourceIds = None
        self._WorkSpaceId = None

    @property
    def ResourceIds(self):
        """待删除资源ID列表
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourcesResponse(AbstractModel):
    """DeleteResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTableConfigRequest(AbstractModel):
    """DeleteTableConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        :param _DebugId: 调试作业ID
        :type DebugId: int
        :param _TableName: 表名
        :type TableName: str
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._JobId = None
        self._DebugId = None
        self._TableName = None
        self._WorkSpaceId = None

    @property
    def JobId(self):
        """作业ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DebugId(self):
        """调试作业ID
        :rtype: int
        """
        return self._DebugId

    @DebugId.setter
    def DebugId(self, DebugId):
        self._DebugId = DebugId

    @property
    def TableName(self):
        """表名
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._DebugId = params.get("DebugId")
        self._TableName = params.get("TableName")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTableConfigResponse(AbstractModel):
    """DeleteTableConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteWorkSpaceRequest(AbstractModel):
    """DeleteWorkSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._WorkSpaceId = None

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkSpaceResponse(AbstractModel):
    """DeleteWorkSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Delete: 是否删除
        :type Delete: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Delete = None
        self._RequestId = None

    @property
    def Delete(self):
        """是否删除
        :rtype: bool
        """
        return self._Delete

    @Delete.setter
    def Delete(self, Delete):
        self._Delete = Delete

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Delete = params.get("Delete")
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterIds: 按照一个或者多个集群 ID 查询，每次请求的集群上限为 100
        :type ClusterIds: list of str
        :param _Offset: 偏移量，默认 0
        :type Offset: int
        :param _Limit: 请求的集群数量，默认 20，最大值 100
        :type Limit: int
        :param _OrderType: 集群信息结果排序规则，1 按时间降序，2 按照时间升序，3  按照状态排序
        :type OrderType: int
        :param _Filters: 过滤规则
    
- Name
    按照集群的名字进行模糊查询。例如：测试
    类型： String
    必选： 否
    
        :type Filters: list of Filter
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._ClusterIds = None
        self._Offset = None
        self._Limit = None
        self._OrderType = None
        self._Filters = None
        self._WorkSpaceId = None

    @property
    def ClusterIds(self):
        """按照一个或者多个集群 ID 查询，每次请求的集群上限为 100
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def Offset(self):
        """偏移量，默认 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """请求的集群数量，默认 20，最大值 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderType(self):
        """集群信息结果排序规则，1 按时间降序，2 按照时间升序，3  按照状态排序
        :rtype: int
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def Filters(self):
        """过滤规则
    
- Name
    按照集群的名字进行模糊查询。例如：测试
    类型： String
    必选： 否
    
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderType = params.get("OrderType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._WorkSpaceId = params.get("WorkSpaceId")
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
        :param _TotalCount: 集群总数
        :type TotalCount: int
        :param _ClusterSet: 集群列表
        :type ClusterSet: list of Cluster
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """集群总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterSet(self):
        """集群列表
        :rtype: list of Cluster
        """
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeFolderRequest(AbstractModel):
    """DescribeFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FolderId: folder id
        :type FolderId: str
        :param _WorkSpaceId: workspace id
        :type WorkSpaceId: str
        :param _FolderType: 1:资源文件夹
其他:作业文件夹
        :type FolderType: int
        """
        self._FolderId = None
        self._WorkSpaceId = None
        self._FolderType = None

    @property
    def FolderId(self):
        """folder id
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def WorkSpaceId(self):
        """workspace id
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def FolderType(self):
        """1:资源文件夹
其他:作业文件夹
        :rtype: int
        """
        return self._FolderType

    @FolderType.setter
    def FolderType(self, FolderType):
        self._FolderType = FolderType


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._FolderType = params.get("FolderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFolderResponse(AbstractModel):
    """DescribeFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FolderId: folder id
        :type FolderId: str
        :param _FolderName: folder name
        :type FolderName: str
        :param _ParentId: 父文件夹id
        :type ParentId: str
        :param _FolderType: 文件夹类型
        :type FolderType: int
        :param _WorkSpaceId: workspace id
        :type WorkSpaceId: str
        :param _SubFolderInfo: 子文件夹信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubFolderInfo: list of SubFolderInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FolderId = None
        self._FolderName = None
        self._ParentId = None
        self._FolderType = None
        self._WorkSpaceId = None
        self._SubFolderInfo = None
        self._RequestId = None

    @property
    def FolderId(self):
        """folder id
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        """folder name
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def ParentId(self):
        """父文件夹id
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def FolderType(self):
        """文件夹类型
        :rtype: int
        """
        return self._FolderType

    @FolderType.setter
    def FolderType(self, FolderType):
        self._FolderType = FolderType

    @property
    def WorkSpaceId(self):
        """workspace id
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def SubFolderInfo(self):
        """子文件夹信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SubFolderInfo
        """
        return self._SubFolderInfo

    @SubFolderInfo.setter
    def SubFolderInfo(self, SubFolderInfo):
        self._SubFolderInfo = SubFolderInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        self._ParentId = params.get("ParentId")
        self._FolderType = params.get("FolderType")
        self._WorkSpaceId = params.get("WorkSpaceId")
        if params.get("SubFolderInfo") is not None:
            self._SubFolderInfo = []
            for item in params.get("SubFolderInfo"):
                obj = SubFolderInfo()
                obj._deserialize(item)
                self._SubFolderInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobConfigsRequest(AbstractModel):
    """DescribeJobConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业Id
        :type JobId: str
        :param _JobConfigVersions: 作业配置版本
        :type JobConfigVersions: list of int non-negative
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 分页大小，默认20，最大100
        :type Limit: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _OnlyDraft: true 表示只展示草稿
        :type OnlyDraft: bool
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._JobId = None
        self._JobConfigVersions = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._OnlyDraft = None
        self._WorkSpaceId = None

    @property
    def JobId(self):
        """作业Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobConfigVersions(self):
        """作业配置版本
        :rtype: list of int non-negative
        """
        return self._JobConfigVersions

    @JobConfigVersions.setter
    def JobConfigVersions(self, JobConfigVersions):
        self._JobConfigVersions = JobConfigVersions

    @property
    def Offset(self):
        """偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小，默认20，最大100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OnlyDraft(self):
        """true 表示只展示草稿
        :rtype: bool
        """
        return self._OnlyDraft

    @OnlyDraft.setter
    def OnlyDraft(self, OnlyDraft):
        self._OnlyDraft = OnlyDraft

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobConfigVersions = params.get("JobConfigVersions")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OnlyDraft = params.get("OnlyDraft")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobConfigsResponse(AbstractModel):
    """DescribeJobConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总的配置版本数量
        :type TotalCount: int
        :param _JobConfigSet: 作业配置列表
        :type JobConfigSet: list of JobConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._JobConfigSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总的配置版本数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def JobConfigSet(self):
        """作业配置列表
        :rtype: list of JobConfig
        """
        return self._JobConfigSet

    @JobConfigSet.setter
    def JobConfigSet(self, JobConfigSet):
        self._JobConfigSet = JobConfigSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("JobConfigSet") is not None:
            self._JobConfigSet = []
            for item in params.get("JobConfigSet"):
                obj = JobConfig()
                obj._deserialize(item)
                self._JobConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobEventsRequest(AbstractModel):
    """DescribeJobEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业的 ID
        :type JobId: str
        :param _StartTimestamp: 筛选条件：起始 Unix 时间戳（秒）
        :type StartTimestamp: int
        :param _EndTimestamp: 筛选条件：结束 Unix 时间戳（秒）
        :type EndTimestamp: int
        :param _Types: 事件类型。如果不传则返回所有类型的数据
        :type Types: list of str
        :param _RunningOrderIds: 运行实例 ID 数组
        :type RunningOrderIds: list of int non-negative
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._JobId = None
        self._StartTimestamp = None
        self._EndTimestamp = None
        self._Types = None
        self._RunningOrderIds = None
        self._WorkSpaceId = None

    @property
    def JobId(self):
        """作业的 ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StartTimestamp(self):
        """筛选条件：起始 Unix 时间戳（秒）
        :rtype: int
        """
        return self._StartTimestamp

    @StartTimestamp.setter
    def StartTimestamp(self, StartTimestamp):
        self._StartTimestamp = StartTimestamp

    @property
    def EndTimestamp(self):
        """筛选条件：结束 Unix 时间戳（秒）
        :rtype: int
        """
        return self._EndTimestamp

    @EndTimestamp.setter
    def EndTimestamp(self, EndTimestamp):
        self._EndTimestamp = EndTimestamp

    @property
    def Types(self):
        """事件类型。如果不传则返回所有类型的数据
        :rtype: list of str
        """
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def RunningOrderIds(self):
        """运行实例 ID 数组
        :rtype: list of int non-negative
        """
        return self._RunningOrderIds

    @RunningOrderIds.setter
    def RunningOrderIds(self, RunningOrderIds):
        self._RunningOrderIds = RunningOrderIds

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StartTimestamp = params.get("StartTimestamp")
        self._EndTimestamp = params.get("EndTimestamp")
        self._Types = params.get("Types")
        self._RunningOrderIds = params.get("RunningOrderIds")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobEventsResponse(AbstractModel):
    """DescribeJobEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 该作业指定范围内的事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of JobEvent
        :param _RunningOrderIds: 该作业指定范围内运行实例 ID 数组，仅当入参没有传入 RunningOrderIds 参数时才会返回。倒序输出
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningOrderIds: list of int non-negative
        :param _TotalCount: 事件的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Versions: 实例对应的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Versions: list of int non-negative
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._RunningOrderIds = None
        self._TotalCount = None
        self._Versions = None
        self._RequestId = None

    @property
    def Events(self):
        """该作业指定范围内的事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of JobEvent
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def RunningOrderIds(self):
        """该作业指定范围内运行实例 ID 数组，仅当入参没有传入 RunningOrderIds 参数时才会返回。倒序输出
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int non-negative
        """
        return self._RunningOrderIds

    @RunningOrderIds.setter
    def RunningOrderIds(self, RunningOrderIds):
        self._RunningOrderIds = RunningOrderIds

    @property
    def TotalCount(self):
        """事件的总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Versions(self):
        """实例对应的版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int non-negative
        """
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = JobEvent()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RunningOrderIds = params.get("RunningOrderIds")
        self._TotalCount = params.get("TotalCount")
        self._Versions = params.get("Versions")
        self._RequestId = params.get("RequestId")


class DescribeJobRuntimeInfoRequest(AbstractModel):
    """DescribeJobRuntimeInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
        :type JobId: str
        :param _WorkSpaceId: 工作空间ID
        :type WorkSpaceId: str
        :param _IncludeInfo: 作业运行信息 key
        :type IncludeInfo: list of str
        """
        self._JobId = None
        self._WorkSpaceId = None
        self._IncludeInfo = None

    @property
    def JobId(self):
        """作业ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def WorkSpaceId(self):
        """工作空间ID
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def IncludeInfo(self):
        """作业运行信息 key
        :rtype: list of str
        """
        return self._IncludeInfo

    @IncludeInfo.setter
    def IncludeInfo(self, IncludeInfo):
        self._IncludeInfo = IncludeInfo


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._IncludeInfo = params.get("IncludeInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobRuntimeInfoResponse(AbstractModel):
    """DescribeJobRuntimeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobRuntimeInfo: 作业运行时信息
        :type JobRuntimeInfo: list of JobRuntimeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobRuntimeInfo = None
        self._RequestId = None

    @property
    def JobRuntimeInfo(self):
        """作业运行时信息
        :rtype: list of JobRuntimeInfo
        """
        return self._JobRuntimeInfo

    @JobRuntimeInfo.setter
    def JobRuntimeInfo(self, JobRuntimeInfo):
        self._JobRuntimeInfo = JobRuntimeInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("JobRuntimeInfo") is not None:
            self._JobRuntimeInfo = []
            for item in params.get("JobRuntimeInfo"):
                obj = JobRuntimeInfo()
                obj._deserialize(item)
                self._JobRuntimeInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobSavepointRequest(AbstractModel):
    """DescribeJobSavepoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业 SerialId
        :type JobId: str
        :param _Limit: 分页参数，单页总数
        :type Limit: int
        :param _Offset: 分页参数，偏移量
        :type Offset: int
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _RecordTypes: 2 是checkpoint
1 是触发savepoint
3 停止触发的savepoint
        :type RecordTypes: list of int
        """
        self._JobId = None
        self._Limit = None
        self._Offset = None
        self._WorkSpaceId = None
        self._RecordTypes = None

    @property
    def JobId(self):
        """作业 SerialId
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Limit(self):
        """分页参数，单页总数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页参数，偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def RecordTypes(self):
        """2 是checkpoint
1 是触发savepoint
3 停止触发的savepoint
        :rtype: list of int
        """
        return self._RecordTypes

    @RecordTypes.setter
    def RecordTypes(self, RecordTypes):
        self._RecordTypes = RecordTypes


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._RecordTypes = params.get("RecordTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobSavepointResponse(AbstractModel):
    """DescribeJobSavepoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNumber: 快照列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNumber: int
        :param _Savepoint: 快照列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Savepoint: list of Savepoint
        :param _RunningSavepoint: 进行中的快照列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningSavepoint: list of Savepoint
        :param _RunningTotalNumber: 进行中的快照列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningTotalNumber: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNumber = None
        self._Savepoint = None
        self._RunningSavepoint = None
        self._RunningTotalNumber = None
        self._RequestId = None

    @property
    def TotalNumber(self):
        """快照列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalNumber

    @TotalNumber.setter
    def TotalNumber(self, TotalNumber):
        self._TotalNumber = TotalNumber

    @property
    def Savepoint(self):
        """快照列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Savepoint
        """
        return self._Savepoint

    @Savepoint.setter
    def Savepoint(self, Savepoint):
        self._Savepoint = Savepoint

    @property
    def RunningSavepoint(self):
        """进行中的快照列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Savepoint
        """
        return self._RunningSavepoint

    @RunningSavepoint.setter
    def RunningSavepoint(self, RunningSavepoint):
        self._RunningSavepoint = RunningSavepoint

    @property
    def RunningTotalNumber(self):
        """进行中的快照列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RunningTotalNumber

    @RunningTotalNumber.setter
    def RunningTotalNumber(self, RunningTotalNumber):
        self._RunningTotalNumber = RunningTotalNumber

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNumber = params.get("TotalNumber")
        if params.get("Savepoint") is not None:
            self._Savepoint = []
            for item in params.get("Savepoint"):
                obj = Savepoint()
                obj._deserialize(item)
                self._Savepoint.append(obj)
        if params.get("RunningSavepoint") is not None:
            self._RunningSavepoint = []
            for item in params.get("RunningSavepoint"):
                obj = Savepoint()
                obj._deserialize(item)
                self._RunningSavepoint.append(obj)
        self._RunningTotalNumber = params.get("RunningTotalNumber")
        self._RequestId = params.get("RequestId")


class DescribeJobSubmissionLogRequest(AbstractModel):
    """DescribeJobSubmissionLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID，例如：cql-6v1jkxrn
        :type JobId: str
        :param _StartTime: 起始时间，unix时间戳，毫秒级，例如：1611754219108
        :type StartTime: int
        :param _EndTime: 结束时间，unix时间戳，毫秒级，例如：1611754219108
        :type EndTime: int
        :param _RunningOrderId: 作业运行的实例ID, 例如：1,2,3。默认为0，表示未选中任何实例，搜索该时间段内最近的一个实例的日志
        :type RunningOrderId: int
        :param _Keyword: 日志搜索的关键词，默认为空
        :type Keyword: str
        :param _Cursor: 日志搜索的游标，可透传上次返回的值，默认为空
        :type Cursor: str
        :param _OrderType: 时间戳排序规则，asc - 升序，desc - 降序。默认为升序
        :type OrderType: str
        :param _Limit: 搜索的日志条数上限值，最大为100
        :type Limit: int
        """
        self._JobId = None
        self._StartTime = None
        self._EndTime = None
        self._RunningOrderId = None
        self._Keyword = None
        self._Cursor = None
        self._OrderType = None
        self._Limit = None

    @property
    def JobId(self):
        """作业ID，例如：cql-6v1jkxrn
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StartTime(self):
        """起始时间，unix时间戳，毫秒级，例如：1611754219108
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，unix时间戳，毫秒级，例如：1611754219108
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RunningOrderId(self):
        """作业运行的实例ID, 例如：1,2,3。默认为0，表示未选中任何实例，搜索该时间段内最近的一个实例的日志
        :rtype: int
        """
        return self._RunningOrderId

    @RunningOrderId.setter
    def RunningOrderId(self, RunningOrderId):
        self._RunningOrderId = RunningOrderId

    @property
    def Keyword(self):
        """日志搜索的关键词，默认为空
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Cursor(self):
        """日志搜索的游标，可透传上次返回的值，默认为空
        :rtype: str
        """
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def OrderType(self):
        """时间戳排序规则，asc - 升序，desc - 降序。默认为升序
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def Limit(self):
        """搜索的日志条数上限值，最大为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RunningOrderId = params.get("RunningOrderId")
        self._Keyword = params.get("Keyword")
        self._Cursor = params.get("Cursor")
        self._OrderType = params.get("OrderType")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobSubmissionLogResponse(AbstractModel):
    """DescribeJobSubmissionLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 日志搜索的游标，需要搜索更多时透传这个值
        :type Cursor: str
        :param _ListOver: 是否返回了所有的日志记录
        :type ListOver: bool
        :param _JobRequestId: 作业启动的requestId
注意：此字段可能返回 null，表示取不到有效值。
        :type JobRequestId: str
        :param _JobInstanceList: 该时间段内符合关键字的所有的作业实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type JobInstanceList: list of JobInstanceForSubmissionLog
        :param _LogList: 废弃，请使用LogContentList
注意：此字段可能返回 null，表示取不到有效值。
        :type LogList: list of str
        :param _LogContentList: 日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogContentList: list of LogContent
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Cursor = None
        self._ListOver = None
        self._JobRequestId = None
        self._JobInstanceList = None
        self._LogList = None
        self._LogContentList = None
        self._RequestId = None

    @property
    def Cursor(self):
        """日志搜索的游标，需要搜索更多时透传这个值
        :rtype: str
        """
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def ListOver(self):
        """是否返回了所有的日志记录
        :rtype: bool
        """
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def JobRequestId(self):
        """作业启动的requestId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobRequestId

    @JobRequestId.setter
    def JobRequestId(self, JobRequestId):
        self._JobRequestId = JobRequestId

    @property
    def JobInstanceList(self):
        """该时间段内符合关键字的所有的作业实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of JobInstanceForSubmissionLog
        """
        return self._JobInstanceList

    @JobInstanceList.setter
    def JobInstanceList(self, JobInstanceList):
        self._JobInstanceList = JobInstanceList

    @property
    def LogList(self):
        """废弃，请使用LogContentList
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LogList

    @LogList.setter
    def LogList(self, LogList):
        self._LogList = LogList

    @property
    def LogContentList(self):
        """日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogContent
        """
        return self._LogContentList

    @LogContentList.setter
    def LogContentList(self, LogContentList):
        self._LogContentList = LogContentList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Cursor = params.get("Cursor")
        self._ListOver = params.get("ListOver")
        self._JobRequestId = params.get("JobRequestId")
        if params.get("JobInstanceList") is not None:
            self._JobInstanceList = []
            for item in params.get("JobInstanceList"):
                obj = JobInstanceForSubmissionLog()
                obj._deserialize(item)
                self._JobInstanceList.append(obj)
        self._LogList = params.get("LogList")
        if params.get("LogContentList") is not None:
            self._LogContentList = []
            for item in params.get("LogContentList"):
                obj = LogContent()
                obj._deserialize(item)
                self._LogContentList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobsRequest(AbstractModel):
    """DescribeJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobIds: 按照一个或者多个作业ID查询。作业ID形如：cql-11112222，每次请求的作业上限为100。参数不支持同时指定JobIds和Filters。
        :type JobIds: list of str
        :param _Filters: 过滤条件，支持的 Filter.Name 为：作业名 Name、作业状态 Status、所属集群 ClusterId、作业id JobId、集群名称 ClusterName。 每次请求的 Filters 个数的上限为 5，Filter.Values 的个数上限为 5。参数不支持同时指定 JobIds 和 Filters。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 分页大小，默认为20，最大值为100
        :type Limit: int
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _ExtraResult: 查询额外的作业信息,例如 JobEventInfo	
        :type ExtraResult: list of str
        :param _ConnectorOptions: 查询引用connector
        :type ConnectorOptions: str
        """
        self._JobIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._WorkSpaceId = None
        self._ExtraResult = None
        self._ConnectorOptions = None

    @property
    def JobIds(self):
        """按照一个或者多个作业ID查询。作业ID形如：cql-11112222，每次请求的作业上限为100。参数不支持同时指定JobIds和Filters。
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def Filters(self):
        """过滤条件，支持的 Filter.Name 为：作业名 Name、作业状态 Status、所属集群 ClusterId、作业id JobId、集群名称 ClusterName。 每次请求的 Filters 个数的上限为 5，Filter.Values 的个数上限为 5。参数不支持同时指定 JobIds 和 Filters。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def ExtraResult(self):
        """查询额外的作业信息,例如 JobEventInfo	
        :rtype: list of str
        """
        return self._ExtraResult

    @ExtraResult.setter
    def ExtraResult(self, ExtraResult):
        self._ExtraResult = ExtraResult

    @property
    def ConnectorOptions(self):
        """查询引用connector
        :rtype: str
        """
        return self._ConnectorOptions

    @ConnectorOptions.setter
    def ConnectorOptions(self, ConnectorOptions):
        self._ConnectorOptions = ConnectorOptions


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._ExtraResult = params.get("ExtraResult")
        self._ConnectorOptions = params.get("ConnectorOptions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobsResponse(AbstractModel):
    """DescribeJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 作业总数
        :type TotalCount: int
        :param _JobSet: 作业列表
        :type JobSet: list of JobV1
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._JobSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """作业总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def JobSet(self):
        """作业列表
        :rtype: list of JobV1
        """
        return self._JobSet

    @JobSet.setter
    def JobSet(self, JobSet):
        self._JobSet = JobSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("JobSet") is not None:
            self._JobSet = []
            for item in params.get("JobSet"):
                obj = JobV1()
                obj._deserialize(item)
                self._JobSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceConfigsRequest(AbstractModel):
    """DescribeResourceConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _Offset: 偏移量，仅当设置 Limit 时该参数有效
        :type Offset: int
        :param _Limit: 返回值大小，不填则返回全量数据
        :type Limit: int
        :param _ResourceConfigVersions: 资源配置Versions集合
        :type ResourceConfigVersions: list of int
        :param _JobConfigVersion: 作业配置版本
        :type JobConfigVersion: int
        :param _JobId: 作业ID
        :type JobId: str
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._ResourceId = None
        self._Offset = None
        self._Limit = None
        self._ResourceConfigVersions = None
        self._JobConfigVersion = None
        self._JobId = None
        self._WorkSpaceId = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Offset(self):
        """偏移量，仅当设置 Limit 时该参数有效
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回值大小，不填则返回全量数据
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourceConfigVersions(self):
        """资源配置Versions集合
        :rtype: list of int
        """
        return self._ResourceConfigVersions

    @ResourceConfigVersions.setter
    def ResourceConfigVersions(self, ResourceConfigVersions):
        self._ResourceConfigVersions = ResourceConfigVersions

    @property
    def JobConfigVersion(self):
        """作业配置版本
        :rtype: int
        """
        return self._JobConfigVersion

    @JobConfigVersion.setter
    def JobConfigVersion(self, JobConfigVersion):
        self._JobConfigVersion = JobConfigVersion

    @property
    def JobId(self):
        """作业ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ResourceConfigVersions = params.get("ResourceConfigVersions")
        self._JobConfigVersion = params.get("JobConfigVersion")
        self._JobId = params.get("JobId")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceConfigsResponse(AbstractModel):
    """DescribeResourceConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceConfigSet: 资源配置描述数组
        :type ResourceConfigSet: list of ResourceConfigItem
        :param _TotalCount: 资源配置数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceConfigSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ResourceConfigSet(self):
        """资源配置描述数组
        :rtype: list of ResourceConfigItem
        """
        return self._ResourceConfigSet

    @ResourceConfigSet.setter
    def ResourceConfigSet(self, ResourceConfigSet):
        self._ResourceConfigSet = ResourceConfigSet

    @property
    def TotalCount(self):
        """资源配置数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResourceConfigSet") is not None:
            self._ResourceConfigSet = []
            for item in params.get("ResourceConfigSet"):
                obj = ResourceConfigItem()
                obj._deserialize(item)
                self._ResourceConfigSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeResourceRelatedJobsRequest(AbstractModel):
    """DescribeResourceRelatedJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _DESCByJobConfigCreateTime: 默认0;   1： 按照作业版本创建时间降序
        :type DESCByJobConfigCreateTime: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 分页大小，默认为20，最大值为100
        :type Limit: int
        :param _ResourceConfigVersion: 资源版本号
        :type ResourceConfigVersion: int
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._ResourceId = None
        self._DESCByJobConfigCreateTime = None
        self._Offset = None
        self._Limit = None
        self._ResourceConfigVersion = None
        self._WorkSpaceId = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def DESCByJobConfigCreateTime(self):
        """默认0;   1： 按照作业版本创建时间降序
        :rtype: int
        """
        return self._DESCByJobConfigCreateTime

    @DESCByJobConfigCreateTime.setter
    def DESCByJobConfigCreateTime(self, DESCByJobConfigCreateTime):
        self._DESCByJobConfigCreateTime = DESCByJobConfigCreateTime

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourceConfigVersion(self):
        """资源版本号
        :rtype: int
        """
        return self._ResourceConfigVersion

    @ResourceConfigVersion.setter
    def ResourceConfigVersion(self, ResourceConfigVersion):
        self._ResourceConfigVersion = ResourceConfigVersion

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._DESCByJobConfigCreateTime = params.get("DESCByJobConfigCreateTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ResourceConfigVersion = params.get("ResourceConfigVersion")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceRelatedJobsResponse(AbstractModel):
    """DescribeResourceRelatedJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RefJobInfos: 关联作业信息
        :type RefJobInfos: list of ResourceRefJobInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RefJobInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RefJobInfos(self):
        """关联作业信息
        :rtype: list of ResourceRefJobInfo
        """
        return self._RefJobInfos

    @RefJobInfos.setter
    def RefJobInfos(self, RefJobInfos):
        self._RefJobInfos = RefJobInfos

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RefJobInfos") is not None:
            self._RefJobInfos = []
            for item in params.get("RefJobInfos"):
                obj = ResourceRefJobInfo()
                obj._deserialize(item)
                self._RefJobInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcesRequest(AbstractModel):
    """DescribeResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 需要查询的资源ID数组，数量不超过100个。如果填写了该参数则忽略Filters参数。
        :type ResourceIds: list of str
        :param _Offset: 偏移量，仅当设置 Limit 参数时有效
        :type Offset: int
        :param _Limit: 条数限制。如果不填，默认返回 20 条
        :type Limit: int
        :param _Filters: <li><strong>ResourceName</strong></li>
<p style="padding-left: 30px;">按照资源名字过滤，支持模糊过滤。传入的过滤名字不超过5个</p><p style="padding-left: 30px;">类型: String</p><p style="padding-left: 30px;">必选: 否</p>
        :type Filters: list of Filter
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _SystemResource: 资源类型，0=用户，1系统connector，2=用户自定义connector
        :type SystemResource: int
        """
        self._ResourceIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._WorkSpaceId = None
        self._SystemResource = None

    @property
    def ResourceIds(self):
        """需要查询的资源ID数组，数量不超过100个。如果填写了该参数则忽略Filters参数。
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Offset(self):
        """偏移量，仅当设置 Limit 参数时有效
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """条数限制。如果不填，默认返回 20 条
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """<li><strong>ResourceName</strong></li>
<p style="padding-left: 30px;">按照资源名字过滤，支持模糊过滤。传入的过滤名字不超过5个</p><p style="padding-left: 30px;">类型: String</p><p style="padding-left: 30px;">必选: 否</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def SystemResource(self):
        """资源类型，0=用户，1系统connector，2=用户自定义connector
        :rtype: int
        """
        return self._SystemResource

    @SystemResource.setter
    def SystemResource(self, SystemResource):
        self._SystemResource = SystemResource


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._SystemResource = params.get("SystemResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesResponse(AbstractModel):
    """DescribeResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceSet: 资源详细信息集合
        :type ResourceSet: list of ResourceItem
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ResourceSet(self):
        """资源详细信息集合
        :rtype: list of ResourceItem
        """
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

    @property
    def TotalCount(self):
        """总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResourceSet") is not None:
            self._ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = ResourceItem()
                obj._deserialize(item)
                self._ResourceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSystemResourcesRequest(AbstractModel):
    """DescribeSystemResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 需要查询的资源ID数组
        :type ResourceIds: list of str
        :param _Offset: 偏移量，仅当设置 Limit 参数时有效
        :type Offset: int
        :param _Limit: 条数限制，默认返回 20 条
        :type Limit: int
        :param _Filters: 查询资源配置列表， 如果不填写，返回该 ResourceIds.N 下所有作业配置列表
        :type Filters: list of Filter
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _FlinkVersion: 查询对应Flink版本的内置connector
        :type FlinkVersion: str
        :param _WorkSpaceId: 空间
        :type WorkSpaceId: str
        """
        self._ResourceIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._ClusterId = None
        self._FlinkVersion = None
        self._WorkSpaceId = None

    @property
    def ResourceIds(self):
        """需要查询的资源ID数组
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Offset(self):
        """偏移量，仅当设置 Limit 参数时有效
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """条数限制，默认返回 20 条
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """查询资源配置列表， 如果不填写，返回该 ResourceIds.N 下所有作业配置列表
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ClusterId(self):
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def FlinkVersion(self):
        """查询对应Flink版本的内置connector
        :rtype: str
        """
        return self._FlinkVersion

    @FlinkVersion.setter
    def FlinkVersion(self, FlinkVersion):
        self._FlinkVersion = FlinkVersion

    @property
    def WorkSpaceId(self):
        """空间
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ClusterId = params.get("ClusterId")
        self._FlinkVersion = params.get("FlinkVersion")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSystemResourcesResponse(AbstractModel):
    """DescribeSystemResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceSet: 资源详细信息集合
        :type ResourceSet: list of SystemResourceItem
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ResourceSet(self):
        """资源详细信息集合
        :rtype: list of SystemResourceItem
        """
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

    @property
    def TotalCount(self):
        """总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResourceSet") is not None:
            self._ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = SystemResourceItem()
                obj._deserialize(item)
                self._ResourceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTreeJobsRequest(AbstractModel):
    """DescribeTreeJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 筛选条件字段
        :type Filters: list of Filter
        :param _WorkSpaceId: 工作空间 Serialid
        :type WorkSpaceId: str
        """
        self._Filters = None
        self._WorkSpaceId = None

    @property
    def Filters(self):
        """筛选条件字段
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def WorkSpaceId(self):
        """工作空间 Serialid
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTreeJobsResponse(AbstractModel):
    """DescribeTreeJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ParentId: 父节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: str
        :param _Id: 当前文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Name: 当前文件夹名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _JobSet: 当前文件夹下的作业列表
注意：此字段可能返回 null，表示取不到有效值。
        :type JobSet: list of TreeJobSets
        :param _Children: 迭代子目录
注意：此字段可能返回 null，表示取不到有效值。
        :type Children: list of DescribeTreeJobsRsp
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ParentId = None
        self._Id = None
        self._Name = None
        self._JobSet = None
        self._Children = None
        self._RequestId = None

    @property
    def ParentId(self):
        """父节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Id(self):
        """当前文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """当前文件夹名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def JobSet(self):
        """当前文件夹下的作业列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TreeJobSets
        """
        return self._JobSet

    @JobSet.setter
    def JobSet(self, JobSet):
        self._JobSet = JobSet

    @property
    def Children(self):
        """迭代子目录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DescribeTreeJobsRsp
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ParentId = params.get("ParentId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("JobSet") is not None:
            self._JobSet = []
            for item in params.get("JobSet"):
                obj = TreeJobSets()
                obj._deserialize(item)
                self._JobSet.append(obj)
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = DescribeTreeJobsRsp()
                obj._deserialize(item)
                self._Children.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTreeJobsRsp(AbstractModel):
    """自定义树结构遍历子节点

    """

    def __init__(self):
        r"""
        :param _ParentId: 父节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: str
        :param _Id: 当前文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Name: 当前文件夹名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _JobSet: 当前文件夹下的作业集合
注意：此字段可能返回 null，表示取不到有效值。
        :type JobSet: list of TreeJobSets
        :param _Children: 迭代子目录
注意：此字段可能返回 null，表示取不到有效值。
        :type Children: list of DescribeTreeJobsRsp
        :param _RequestId: 请求ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestId: str
        """
        self._ParentId = None
        self._Id = None
        self._Name = None
        self._JobSet = None
        self._Children = None
        self._RequestId = None

    @property
    def ParentId(self):
        """父节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Id(self):
        """当前文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """当前文件夹名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def JobSet(self):
        """当前文件夹下的作业集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TreeJobSets
        """
        return self._JobSet

    @JobSet.setter
    def JobSet(self, JobSet):
        self._JobSet = JobSet

    @property
    def Children(self):
        """迭代子目录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DescribeTreeJobsRsp
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def RequestId(self):
        """请求ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ParentId = params.get("ParentId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("JobSet") is not None:
            self._JobSet = []
            for item in params.get("JobSet"):
                obj = TreeJobSets()
                obj._deserialize(item)
                self._JobSet.append(obj)
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = DescribeTreeJobsRsp()
                obj._deserialize(item)
                self._Children.append(obj)
        self._RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTreeResourcesRequest(AbstractModel):
    """DescribeTreeResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 筛选条件字段
        :type Filters: list of Filter
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _Offset: 分页游标
        :type Offset: int
        :param _Limit: 单页显示数
        :type Limit: int
        """
        self._Filters = None
        self._WorkSpaceId = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """筛选条件字段
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def Offset(self):
        """分页游标
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """单页显示数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTreeResourcesResponse(AbstractModel):
    """DescribeTreeResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ParentId: 父节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: str
        :param _Id: 文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Name: 文件夹名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Items: 文件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of TreeResourceItem
        :param _Children: 子目录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Children: list of DescribeTreeResourcesRsp
        :param _TotalCount: 资源总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ParentId = None
        self._Id = None
        self._Name = None
        self._Items = None
        self._Children = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ParentId(self):
        """父节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Id(self):
        """文件夹ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """文件夹名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Items(self):
        """文件列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TreeResourceItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Children(self):
        """子目录列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DescribeTreeResourcesRsp
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def TotalCount(self):
        """资源总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ParentId = params.get("ParentId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TreeResourceItem()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = DescribeTreeResourcesRsp()
                obj._deserialize(item)
                self._Children.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTreeResourcesRsp(AbstractModel):
    """树状结构资源列表对象

    """

    def __init__(self):
        r"""
        :param _ParentId: 父节点ID
        :type ParentId: str
        :param _Id: 文件夹ID
        :type Id: str
        :param _Name: 文件夹名称
        :type Name: str
        :param _Items: 文件夹下资源数字
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of TreeResourceItem
        :param _Children: 子节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Children: list of DescribeTreeResourcesRsp
        :param _TotalCount: 资源总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._ParentId = None
        self._Id = None
        self._Name = None
        self._Items = None
        self._Children = None
        self._TotalCount = None

    @property
    def ParentId(self):
        """父节点ID
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Id(self):
        """文件夹ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """文件夹名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Items(self):
        """文件夹下资源数字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TreeResourceItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Children(self):
        """子节点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DescribeTreeResourcesRsp
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def TotalCount(self):
        """资源总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._ParentId = params.get("ParentId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = TreeResourceItem()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = DescribeTreeResourcesRsp()
                obj._deserialize(item)
                self._Children.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkSpacesRequest(AbstractModel):
    """DescribeWorkSpaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认 0
        :type Offset: int
        :param _OrderType: 1 按照创建时间降序排序(默认) 2.按照创建时间升序排序，3. 按照状态降序排序 4. 按照状态升序排序 默认为0
        :type OrderType: int
        :param _Limit: 请求的集群数量，默认 20
        :type Limit: int
        :param _Filters: 过滤规则
        :type Filters: list of Filter
        """
        self._Offset = None
        self._OrderType = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        """偏移量，默认 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderType(self):
        """1 按照创建时间降序排序(默认) 2.按照创建时间升序排序，3. 按照状态降序排序 4. 按照状态升序排序 默认为0
        :rtype: int
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def Limit(self):
        """请求的集群数量，默认 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤规则
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._OrderType = params.get("OrderType")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkSpacesResponse(AbstractModel):
    """DescribeWorkSpaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkSpaceSetItem: 空间详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkSpaceSetItem: list of WorkSpaceSetItem
        :param _TotalCount: 空间总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkSpaceSetItem = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WorkSpaceSetItem(self):
        """空间详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WorkSpaceSetItem
        """
        return self._WorkSpaceSetItem

    @WorkSpaceSetItem.setter
    def WorkSpaceSetItem(self, WorkSpaceSetItem):
        self._WorkSpaceSetItem = WorkSpaceSetItem

    @property
    def TotalCount(self):
        """空间总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WorkSpaceSetItem") is not None:
            self._WorkSpaceSetItem = []
            for item in params.get("WorkSpaceSetItem"):
                obj = WorkSpaceSetItem()
                obj._deserialize(item)
                self._WorkSpaceSetItem.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ExpertModeConfiguration(AbstractModel):
    """作业配置 -- 专家模式的详细配置

    """

    def __init__(self):
        r"""
        :param _JobGraph: Job graph
注意：此字段可能返回 null，表示取不到有效值。
        :type JobGraph: :class:`tencentcloud.oceanus.v20190422.models.JobGraph`
        :param _NodeConfig: Node configuration
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeConfig: list of NodeConfig
        :param _SlotSharingGroups: Slot sharing groups
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotSharingGroups: list of SlotSharingGroup
        """
        self._JobGraph = None
        self._NodeConfig = None
        self._SlotSharingGroups = None

    @property
    def JobGraph(self):
        """Job graph
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.JobGraph`
        """
        return self._JobGraph

    @JobGraph.setter
    def JobGraph(self, JobGraph):
        self._JobGraph = JobGraph

    @property
    def NodeConfig(self):
        """Node configuration
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of NodeConfig
        """
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def SlotSharingGroups(self):
        """Slot sharing groups
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SlotSharingGroup
        """
        return self._SlotSharingGroups

    @SlotSharingGroups.setter
    def SlotSharingGroups(self, SlotSharingGroups):
        self._SlotSharingGroups = SlotSharingGroups


    def _deserialize(self, params):
        if params.get("JobGraph") is not None:
            self._JobGraph = JobGraph()
            self._JobGraph._deserialize(params.get("JobGraph"))
        if params.get("NodeConfig") is not None:
            self._NodeConfig = []
            for item in params.get("NodeConfig"):
                obj = NodeConfig()
                obj._deserialize(item)
                self._NodeConfig.append(obj)
        if params.get("SlotSharingGroups") is not None:
            self._SlotSharingGroups = []
            for item in params.get("SlotSharingGroups"):
                obj = SlotSharingGroup()
                obj._deserialize(item)
                self._SlotSharingGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchSqlGatewayStatementResultRequest(AbstractModel):
    """FetchSqlGatewayStatementResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _SessionId: Sql Gateway会话ID
        :type SessionId: str
        :param _OperationHandleId: sql的查询id
        :type OperationHandleId: str
        :param _ResultUri: 下一条结果的获取url，首次获取执行结果时可以为空，当获取下一批查询结果时需要传递
        :type ResultUri: str
        """
        self._ClusterId = None
        self._SessionId = None
        self._OperationHandleId = None
        self._ResultUri = None

    @property
    def ClusterId(self):
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SessionId(self):
        """Sql Gateway会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def OperationHandleId(self):
        """sql的查询id
        :rtype: str
        """
        return self._OperationHandleId

    @OperationHandleId.setter
    def OperationHandleId(self, OperationHandleId):
        self._OperationHandleId = OperationHandleId

    @property
    def ResultUri(self):
        """下一条结果的获取url，首次获取执行结果时可以为空，当获取下一批查询结果时需要传递
        :rtype: str
        """
        return self._ResultUri

    @ResultUri.setter
    def ResultUri(self, ResultUri):
        self._ResultUri = ResultUri


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SessionId = params.get("SessionId")
        self._OperationHandleId = params.get("OperationHandleId")
        self._ResultUri = params.get("ResultUri")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchSqlGatewayStatementResultResponse(AbstractModel):
    """FetchSqlGatewayStatementResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMessage: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: list of str
        :param _ResultType: 返回类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultType: str
        :param _IsQueryResult: 是否DQL结果
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQueryResult: bool
        :param _ResultKind: 结果类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultKind: str
        :param _Results: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: :class:`tencentcloud.oceanus.v20190422.models.StatementResult`
        :param _NextResultUri: 下一次请求的uri
注意：此字段可能返回 null，表示取不到有效值。
        :type NextResultUri: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMessage = None
        self._ResultType = None
        self._IsQueryResult = None
        self._ResultKind = None
        self._Results = None
        self._NextResultUri = None
        self._RequestId = None

    @property
    def ErrorMessage(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultType(self):
        """返回类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def IsQueryResult(self):
        """是否DQL结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsQueryResult

    @IsQueryResult.setter
    def IsQueryResult(self, IsQueryResult):
        self._IsQueryResult = IsQueryResult

    @property
    def ResultKind(self):
        """结果类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultKind

    @ResultKind.setter
    def ResultKind(self, ResultKind):
        self._ResultKind = ResultKind

    @property
    def Results(self):
        """结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.StatementResult`
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def NextResultUri(self):
        """下一次请求的uri
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextResultUri

    @NextResultUri.setter
    def NextResultUri(self, NextResultUri):
        self._NextResultUri = NextResultUri

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultType = params.get("ResultType")
        self._IsQueryResult = params.get("IsQueryResult")
        self._ResultKind = params.get("ResultKind")
        if params.get("Results") is not None:
            self._Results = StatementResult()
            self._Results._deserialize(params.get("Results"))
        self._NextResultUri = params.get("NextResultUri")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查询作业列表时的过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 要过滤的字段
        :type Name: str
        :param _Values: 字段的过滤值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """要过滤的字段
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """字段的过滤值
        :rtype: list of str
        """
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
        


class GatewayRefItem(AbstractModel):
    """Gateway引用资源信息

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 空间唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: str
        :param _ResourceId: 资源唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: int
        :param _Type: 引用类型，0:用户资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        """
        self._WorkspaceId = None
        self._ResourceId = None
        self._Version = None
        self._Type = None

    @property
    def WorkspaceId(self):
        """空间唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ResourceId(self):
        """资源唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Version(self):
        """版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Type(self):
        """引用类型，0:用户资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ResourceId = params.get("ResourceId")
        self._Version = params.get("Version")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMetaTableRequest(AbstractModel):
    """GetMetaTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Catalog: 目录名
        :type Catalog: str
        :param _Database: 库名
        :type Database: str
        :param _Table: 表名
        :type Table: str
        :param _WorkSpaceId: 空间唯一标识
        :type WorkSpaceId: str
        """
        self._Catalog = None
        self._Database = None
        self._Table = None
        self._WorkSpaceId = None

    @property
    def Catalog(self):
        """目录名
        :rtype: str
        """
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Database(self):
        """库名
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """表名
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def WorkSpaceId(self):
        """空间唯一标识
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._Catalog = params.get("Catalog")
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMetaTableResponse(AbstractModel):
    """GetMetaTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SerialId: 元数据表唯一标识
        :type SerialId: str
        :param _Catalog: 目录名
        :type Catalog: str
        :param _Database: 库名
        :type Database: str
        :param _Table: 表名
        :type Table: str
        :param _DDL: 建表语句,使用 Base64 编码。
例如
Q1JFQVRFIFRBQkxFIGRhdGFnZW5fc291cmNlX3RhYmxlICggCiAgICBpZCBJTlQsIAogICAgbmFtZSBTVFJJTkcgCikgV0lUSCAoCidjb25uZWN0b3InPSdkYXRhZ2VuJywKJ3Jvd3MtcGVyLXNlY29uZCcgPSAnMScKKTs=
        :type DDL: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SerialId = None
        self._Catalog = None
        self._Database = None
        self._Table = None
        self._DDL = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def SerialId(self):
        """元数据表唯一标识
        :rtype: str
        """
        return self._SerialId

    @SerialId.setter
    def SerialId(self, SerialId):
        self._SerialId = SerialId

    @property
    def Catalog(self):
        """目录名
        :rtype: str
        """
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def Database(self):
        """库名
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def Table(self):
        """表名
        :rtype: str
        """
        return self._Table

    @Table.setter
    def Table(self, Table):
        self._Table = Table

    @property
    def DDL(self):
        """建表语句,使用 Base64 编码。
例如
Q1JFQVRFIFRBQkxFIGRhdGFnZW5fc291cmNlX3RhYmxlICggCiAgICBpZCBJTlQsIAogICAgbmFtZSBTVFJJTkcgCikgV0lUSCAoCidjb25uZWN0b3InPSdkYXRhZ2VuJywKJ3Jvd3MtcGVyLXNlY29uZCcgPSAnMScKKTs=
        :rtype: str
        """
        return self._DDL

    @DDL.setter
    def DDL(self, DDL):
        self._DDL = DDL

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SerialId = params.get("SerialId")
        self._Catalog = params.get("Catalog")
        self._Database = params.get("Database")
        self._Table = params.get("Table")
        self._DDL = params.get("DDL")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class JobConfig(AbstractModel):
    """作业配置详情

    """

    def __init__(self):
        r"""
        :param _JobId: 作业Id
        :type JobId: str
        :param _EntrypointClass: 主类
注意：此字段可能返回 null，表示取不到有效值。
        :type EntrypointClass: str
        :param _ProgramArgs: 主类入参
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgramArgs: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _CreateTime: 作业配置创建时间
        :type CreateTime: str
        :param _Version: 作业配置的版本号
        :type Version: int
        :param _DefaultParallelism: 作业默认并行度
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultParallelism: int
        :param _Properties: 系统参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param _ResourceRefDetails: 引用资源
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRefDetails: list of ResourceRefDetail
        :param _CreatorUin: 创建者uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param _UpdateTime: 作业配置上次启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _COSBucket: 作业绑定的存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :type COSBucket: str
        :param _LogCollect: 是否启用日志收集，0-未启用，1-已启用，2-历史集群未设置日志集，3-历史集群已开启
注意：此字段可能返回 null，表示取不到有效值。
        :type LogCollect: int
        :param _MaxParallelism: 作业的最大并行度
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxParallelism: int
        :param _JobManagerSpec: JobManager规格
注意：此字段可能返回 null，表示取不到有效值。
        :type JobManagerSpec: float
        :param _TaskManagerSpec: TaskManager规格
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskManagerSpec: float
        :param _ClsLogsetId: CLS日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsLogsetId: str
        :param _ClsTopicId: CLS日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsTopicId: str
        :param _PythonVersion: pyflink作业运行的python版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PythonVersion: str
        :param _AutoRecover: Oceanus 平台恢复作业开关 1:开启 -1: 关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRecover: int
        :param _LogLevel: 日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: str
        :param _ClazzLevels: 类日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :type ClazzLevels: list of ClazzLevel
        :param _ExpertModeOn: 是否开启专家模式
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpertModeOn: bool
        :param _ExpertModeConfiguration: 专家模式的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpertModeConfiguration: :class:`tencentcloud.oceanus.v20190422.models.ExpertModeConfiguration`
        :param _TraceModeOn: trace链路
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceModeOn: bool
        :param _TraceModeConfiguration: trace链路配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceModeConfiguration: :class:`tencentcloud.oceanus.v20190422.models.TraceModeConfiguration`
        :param _CheckpointRetainedNum: checkpoint保留个数
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckpointRetainedNum: int
        :param _JobGraph: 算子拓扑图
注意：此字段可能返回 null，表示取不到有效值。
        :type JobGraph: :class:`tencentcloud.oceanus.v20190422.models.JobGraph`
        :param _EsServerlessIndex: es索引
注意：此字段可能返回 null，表示取不到有效值。
        :type EsServerlessIndex: str
        :param _EsServerlessSpace: es空间
注意：此字段可能返回 null，表示取不到有效值。
        :type EsServerlessSpace: str
        :param _IndexName: es索引中文
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexName: str
        :param _WorkspaceName: es空间中文
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceName: str
        :param _FlinkVersion: flink 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FlinkVersion: str
        :param _JobManagerCpu: jm使用cpu数目
注意：此字段可能返回 null，表示取不到有效值。
        :type JobManagerCpu: float
        :param _JobManagerMem: jm使用内存数目
注意：此字段可能返回 null，表示取不到有效值。
        :type JobManagerMem: float
        :param _TaskManagerCpu: tm使用cpu数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskManagerCpu: float
        :param _TaskManagerMem: tm使用mem数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskManagerMem: float
        :param _JobConfigItem: 运行中配置
注意：此字段可能返回 null，表示取不到有效值。
        :type JobConfigItem: :class:`tencentcloud.oceanus.v20190422.models.JobConfig`
        """
        self._JobId = None
        self._EntrypointClass = None
        self._ProgramArgs = None
        self._Remark = None
        self._CreateTime = None
        self._Version = None
        self._DefaultParallelism = None
        self._Properties = None
        self._ResourceRefDetails = None
        self._CreatorUin = None
        self._UpdateTime = None
        self._COSBucket = None
        self._LogCollect = None
        self._MaxParallelism = None
        self._JobManagerSpec = None
        self._TaskManagerSpec = None
        self._ClsLogsetId = None
        self._ClsTopicId = None
        self._PythonVersion = None
        self._AutoRecover = None
        self._LogLevel = None
        self._ClazzLevels = None
        self._ExpertModeOn = None
        self._ExpertModeConfiguration = None
        self._TraceModeOn = None
        self._TraceModeConfiguration = None
        self._CheckpointRetainedNum = None
        self._JobGraph = None
        self._EsServerlessIndex = None
        self._EsServerlessSpace = None
        self._IndexName = None
        self._WorkspaceName = None
        self._FlinkVersion = None
        self._JobManagerCpu = None
        self._JobManagerMem = None
        self._TaskManagerCpu = None
        self._TaskManagerMem = None
        self._JobConfigItem = None

    @property
    def JobId(self):
        """作业Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def EntrypointClass(self):
        """主类
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EntrypointClass

    @EntrypointClass.setter
    def EntrypointClass(self, EntrypointClass):
        self._EntrypointClass = EntrypointClass

    @property
    def ProgramArgs(self):
        """主类入参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProgramArgs

    @ProgramArgs.setter
    def ProgramArgs(self, ProgramArgs):
        self._ProgramArgs = ProgramArgs

    @property
    def Remark(self):
        """备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        """作业配置创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Version(self):
        """作业配置的版本号
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def DefaultParallelism(self):
        """作业默认并行度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DefaultParallelism

    @DefaultParallelism.setter
    def DefaultParallelism(self, DefaultParallelism):
        self._DefaultParallelism = DefaultParallelism

    @property
    def Properties(self):
        """系统参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Property
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def ResourceRefDetails(self):
        """引用资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceRefDetail
        """
        return self._ResourceRefDetails

    @ResourceRefDetails.setter
    def ResourceRefDetails(self, ResourceRefDetails):
        self._ResourceRefDetails = ResourceRefDetails

    @property
    def CreatorUin(self):
        """创建者uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def UpdateTime(self):
        """作业配置上次启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def COSBucket(self):
        """作业绑定的存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._COSBucket

    @COSBucket.setter
    def COSBucket(self, COSBucket):
        self._COSBucket = COSBucket

    @property
    def LogCollect(self):
        """是否启用日志收集，0-未启用，1-已启用，2-历史集群未设置日志集，3-历史集群已开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LogCollect

    @LogCollect.setter
    def LogCollect(self, LogCollect):
        self._LogCollect = LogCollect

    @property
    def MaxParallelism(self):
        """作业的最大并行度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxParallelism

    @MaxParallelism.setter
    def MaxParallelism(self, MaxParallelism):
        self._MaxParallelism = MaxParallelism

    @property
    def JobManagerSpec(self):
        """JobManager规格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._JobManagerSpec

    @JobManagerSpec.setter
    def JobManagerSpec(self, JobManagerSpec):
        self._JobManagerSpec = JobManagerSpec

    @property
    def TaskManagerSpec(self):
        """TaskManager规格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TaskManagerSpec

    @TaskManagerSpec.setter
    def TaskManagerSpec(self, TaskManagerSpec):
        self._TaskManagerSpec = TaskManagerSpec

    @property
    def ClsLogsetId(self):
        """CLS日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsTopicId(self):
        """CLS日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def PythonVersion(self):
        """pyflink作业运行的python版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PythonVersion

    @PythonVersion.setter
    def PythonVersion(self, PythonVersion):
        self._PythonVersion = PythonVersion

    @property
    def AutoRecover(self):
        """Oceanus 平台恢复作业开关 1:开启 -1: 关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AutoRecover

    @AutoRecover.setter
    def AutoRecover(self, AutoRecover):
        self._AutoRecover = AutoRecover

    @property
    def LogLevel(self):
        """日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def ClazzLevels(self):
        """类日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ClazzLevel
        """
        return self._ClazzLevels

    @ClazzLevels.setter
    def ClazzLevels(self, ClazzLevels):
        self._ClazzLevels = ClazzLevels

    @property
    def ExpertModeOn(self):
        """是否开启专家模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ExpertModeOn

    @ExpertModeOn.setter
    def ExpertModeOn(self, ExpertModeOn):
        self._ExpertModeOn = ExpertModeOn

    @property
    def ExpertModeConfiguration(self):
        """专家模式的配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.ExpertModeConfiguration`
        """
        return self._ExpertModeConfiguration

    @ExpertModeConfiguration.setter
    def ExpertModeConfiguration(self, ExpertModeConfiguration):
        self._ExpertModeConfiguration = ExpertModeConfiguration

    @property
    def TraceModeOn(self):
        """trace链路
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._TraceModeOn

    @TraceModeOn.setter
    def TraceModeOn(self, TraceModeOn):
        self._TraceModeOn = TraceModeOn

    @property
    def TraceModeConfiguration(self):
        """trace链路配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.TraceModeConfiguration`
        """
        return self._TraceModeConfiguration

    @TraceModeConfiguration.setter
    def TraceModeConfiguration(self, TraceModeConfiguration):
        self._TraceModeConfiguration = TraceModeConfiguration

    @property
    def CheckpointRetainedNum(self):
        """checkpoint保留个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CheckpointRetainedNum

    @CheckpointRetainedNum.setter
    def CheckpointRetainedNum(self, CheckpointRetainedNum):
        self._CheckpointRetainedNum = CheckpointRetainedNum

    @property
    def JobGraph(self):
        """算子拓扑图
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.JobGraph`
        """
        return self._JobGraph

    @JobGraph.setter
    def JobGraph(self, JobGraph):
        self._JobGraph = JobGraph

    @property
    def EsServerlessIndex(self):
        """es索引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EsServerlessIndex

    @EsServerlessIndex.setter
    def EsServerlessIndex(self, EsServerlessIndex):
        self._EsServerlessIndex = EsServerlessIndex

    @property
    def EsServerlessSpace(self):
        """es空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EsServerlessSpace

    @EsServerlessSpace.setter
    def EsServerlessSpace(self, EsServerlessSpace):
        self._EsServerlessSpace = EsServerlessSpace

    @property
    def IndexName(self):
        """es索引中文
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def WorkspaceName(self):
        """es空间中文
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkspaceName

    @WorkspaceName.setter
    def WorkspaceName(self, WorkspaceName):
        self._WorkspaceName = WorkspaceName

    @property
    def FlinkVersion(self):
        """flink 版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FlinkVersion

    @FlinkVersion.setter
    def FlinkVersion(self, FlinkVersion):
        self._FlinkVersion = FlinkVersion

    @property
    def JobManagerCpu(self):
        """jm使用cpu数目
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._JobManagerCpu

    @JobManagerCpu.setter
    def JobManagerCpu(self, JobManagerCpu):
        self._JobManagerCpu = JobManagerCpu

    @property
    def JobManagerMem(self):
        """jm使用内存数目
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._JobManagerMem

    @JobManagerMem.setter
    def JobManagerMem(self, JobManagerMem):
        self._JobManagerMem = JobManagerMem

    @property
    def TaskManagerCpu(self):
        """tm使用cpu数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TaskManagerCpu

    @TaskManagerCpu.setter
    def TaskManagerCpu(self, TaskManagerCpu):
        self._TaskManagerCpu = TaskManagerCpu

    @property
    def TaskManagerMem(self):
        """tm使用mem数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TaskManagerMem

    @TaskManagerMem.setter
    def TaskManagerMem(self, TaskManagerMem):
        self._TaskManagerMem = TaskManagerMem

    @property
    def JobConfigItem(self):
        """运行中配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.JobConfig`
        """
        return self._JobConfigItem

    @JobConfigItem.setter
    def JobConfigItem(self, JobConfigItem):
        self._JobConfigItem = JobConfigItem


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._EntrypointClass = params.get("EntrypointClass")
        self._ProgramArgs = params.get("ProgramArgs")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._Version = params.get("Version")
        self._DefaultParallelism = params.get("DefaultParallelism")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        if params.get("ResourceRefDetails") is not None:
            self._ResourceRefDetails = []
            for item in params.get("ResourceRefDetails"):
                obj = ResourceRefDetail()
                obj._deserialize(item)
                self._ResourceRefDetails.append(obj)
        self._CreatorUin = params.get("CreatorUin")
        self._UpdateTime = params.get("UpdateTime")
        self._COSBucket = params.get("COSBucket")
        self._LogCollect = params.get("LogCollect")
        self._MaxParallelism = params.get("MaxParallelism")
        self._JobManagerSpec = params.get("JobManagerSpec")
        self._TaskManagerSpec = params.get("TaskManagerSpec")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._ClsTopicId = params.get("ClsTopicId")
        self._PythonVersion = params.get("PythonVersion")
        self._AutoRecover = params.get("AutoRecover")
        self._LogLevel = params.get("LogLevel")
        if params.get("ClazzLevels") is not None:
            self._ClazzLevels = []
            for item in params.get("ClazzLevels"):
                obj = ClazzLevel()
                obj._deserialize(item)
                self._ClazzLevels.append(obj)
        self._ExpertModeOn = params.get("ExpertModeOn")
        if params.get("ExpertModeConfiguration") is not None:
            self._ExpertModeConfiguration = ExpertModeConfiguration()
            self._ExpertModeConfiguration._deserialize(params.get("ExpertModeConfiguration"))
        self._TraceModeOn = params.get("TraceModeOn")
        if params.get("TraceModeConfiguration") is not None:
            self._TraceModeConfiguration = TraceModeConfiguration()
            self._TraceModeConfiguration._deserialize(params.get("TraceModeConfiguration"))
        self._CheckpointRetainedNum = params.get("CheckpointRetainedNum")
        if params.get("JobGraph") is not None:
            self._JobGraph = JobGraph()
            self._JobGraph._deserialize(params.get("JobGraph"))
        self._EsServerlessIndex = params.get("EsServerlessIndex")
        self._EsServerlessSpace = params.get("EsServerlessSpace")
        self._IndexName = params.get("IndexName")
        self._WorkspaceName = params.get("WorkspaceName")
        self._FlinkVersion = params.get("FlinkVersion")
        self._JobManagerCpu = params.get("JobManagerCpu")
        self._JobManagerMem = params.get("JobManagerMem")
        self._TaskManagerCpu = params.get("TaskManagerCpu")
        self._TaskManagerMem = params.get("TaskManagerMem")
        if params.get("JobConfigItem") is not None:
            self._JobConfigItem = JobConfig()
            self._JobConfigItem._deserialize(params.get("JobConfigItem"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobEvent(AbstractModel):
    """描述作业发生的一个事件

    """

    def __init__(self):
        r"""
        :param _Type: 内部定义的事件类型
        :type Type: str
        :param _Description: 事件类型的说明文字
        :type Description: str
        :param _Timestamp: 事件发生的 Unix 时间戳（秒）
        :type Timestamp: int
        :param _RunningOrderId: 事件发生时的运行 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningOrderId: int
        :param _Message: 事件的一些可选说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _SolutionLink: 异常事件的排查手册链接
注意：此字段可能返回 null，表示取不到有效值。
        :type SolutionLink: str
        """
        self._Type = None
        self._Description = None
        self._Timestamp = None
        self._RunningOrderId = None
        self._Message = None
        self._SolutionLink = None

    @property
    def Type(self):
        """内部定义的事件类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        """事件类型的说明文字
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Timestamp(self):
        """事件发生的 Unix 时间戳（秒）
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def RunningOrderId(self):
        """事件发生时的运行 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RunningOrderId

    @RunningOrderId.setter
    def RunningOrderId(self, RunningOrderId):
        self._RunningOrderId = RunningOrderId

    @property
    def Message(self):
        """事件的一些可选说明
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def SolutionLink(self):
        """异常事件的排查手册链接
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SolutionLink

    @SolutionLink.setter
    def SolutionLink(self, SolutionLink):
        self._SolutionLink = SolutionLink


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Description = params.get("Description")
        self._Timestamp = params.get("Timestamp")
        self._RunningOrderId = params.get("RunningOrderId")
        self._Message = params.get("Message")
        self._SolutionLink = params.get("SolutionLink")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobEventInfo(AbstractModel):
    """事件信息

    """

    def __init__(self):
        r"""
        :param _ErrorEventTotal: 异常事件总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorEventTotal: int
        """
        self._ErrorEventTotal = None

    @property
    def ErrorEventTotal(self):
        """异常事件总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ErrorEventTotal

    @ErrorEventTotal.setter
    def ErrorEventTotal(self, ErrorEventTotal):
        self._ErrorEventTotal = ErrorEventTotal


    def _deserialize(self, params):
        self._ErrorEventTotal = params.get("ErrorEventTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobGraph(AbstractModel):
    """作业运行图

    """

    def __init__(self):
        r"""
        :param _Nodes: 运行图的点集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Nodes: list of JobGraphNode
        :param _Edges: 运行图的边集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Edges: list of JobGraphEdge
        """
        self._Nodes = None
        self._Edges = None

    @property
    def Nodes(self):
        """运行图的点集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of JobGraphNode
        """
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def Edges(self):
        """运行图的边集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of JobGraphEdge
        """
        return self._Edges

    @Edges.setter
    def Edges(self, Edges):
        self._Edges = Edges


    def _deserialize(self, params):
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = JobGraphNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        if params.get("Edges") is not None:
            self._Edges = []
            for item in params.get("Edges"):
                obj = JobGraphEdge()
                obj._deserialize(item)
                self._Edges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobGraphEdge(AbstractModel):
    """Flink Job 运行图的边信息

    """

    def __init__(self):
        r"""
        :param _Source: 边的起始节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        :param _Target: 边的目标节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Target: int
        """
        self._Source = None
        self._Target = None

    @property
    def Source(self):
        """边的起始节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        """边的目标节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobGraphNode(AbstractModel):
    """Flink Job 运行图的点信息

    """

    def __init__(self):
        r"""
        :param _Id: 节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Description: 节点描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Name: 节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Parallelism: 节点并行度
注意：此字段可能返回 null，表示取不到有效值。
        :type Parallelism: int
        """
        self._Id = None
        self._Description = None
        self._Name = None
        self._Parallelism = None

    @property
    def Id(self):
        """节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Description(self):
        """节点描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        """节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Parallelism(self):
        """节点并行度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Parallelism

    @Parallelism.setter
    def Parallelism(self, Parallelism):
        self._Parallelism = Parallelism


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._Parallelism = params.get("Parallelism")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobInstanceForSubmissionLog(AbstractModel):
    """搜索启动日志时返回的作业实例

    """

    def __init__(self):
        r"""
        :param _RunningOrderId: 实例的Id, 按照启动的时间顺序，从1开始
        :type RunningOrderId: int
        :param _JobInstanceStartTime: 作业实例的启动时间
        :type JobInstanceStartTime: str
        :param _StartingMillis: 作业实例启动的时间（毫秒）
        :type StartingMillis: int
        """
        self._RunningOrderId = None
        self._JobInstanceStartTime = None
        self._StartingMillis = None

    @property
    def RunningOrderId(self):
        """实例的Id, 按照启动的时间顺序，从1开始
        :rtype: int
        """
        return self._RunningOrderId

    @RunningOrderId.setter
    def RunningOrderId(self, RunningOrderId):
        self._RunningOrderId = RunningOrderId

    @property
    def JobInstanceStartTime(self):
        """作业实例的启动时间
        :rtype: str
        """
        return self._JobInstanceStartTime

    @JobInstanceStartTime.setter
    def JobInstanceStartTime(self, JobInstanceStartTime):
        self._JobInstanceStartTime = JobInstanceStartTime

    @property
    def StartingMillis(self):
        """作业实例启动的时间（毫秒）
        :rtype: int
        """
        return self._StartingMillis

    @StartingMillis.setter
    def StartingMillis(self, StartingMillis):
        self._StartingMillis = StartingMillis


    def _deserialize(self, params):
        self._RunningOrderId = params.get("RunningOrderId")
        self._JobInstanceStartTime = params.get("JobInstanceStartTime")
        self._StartingMillis = params.get("StartingMillis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobRuntimeInfo(AbstractModel):
    """作业运行时信息

    """

    def __init__(self):
        r"""
        :param _Key: 运行信息的key，目前支持：TaskManagers：taskmanager pod 列表； StreamGraph：作业对应的 StreamGraph；SubTasks：作业的 subtask 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 运行信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """运行信息的key，目前支持：TaskManagers：taskmanager pod 列表； StreamGraph：作业对应的 StreamGraph；SubTasks：作业的 subtask 列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """运行信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class JobV1(AbstractModel):
    """Job详细信息

    """

    def __init__(self):
        r"""
        :param _JobId: 作业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _OwnerUin: 用户UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _CreatorUin: 创建者UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param _Name: 作业名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _JobType: 作业类型，1：sql作业，2：Jar作业
注意：此字段可能返回 null，表示取不到有效值。
        :type JobType: int
        :param _Status: 作业状态，1：未初始化，2：未发布，3：操作中，4：运行中，5：停止，6：暂停，-1：故障
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateTime: 作业创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _StartTime: 作业启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _StopTime: 作业停止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StopTime: str
        :param _UpdateTime: 作业更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _TotalRunMillis: 作业累计运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalRunMillis: int
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _LastOpResult: 操作错误提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOpResult: str
        :param _ClusterName: 集群名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _LatestJobConfigVersion: 最新配置版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestJobConfigVersion: int
        :param _PublishedJobConfigVersion: 已发布的配置版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishedJobConfigVersion: int
        :param _RunningCuNum: 运行的CU数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningCuNum: int
        :param _CuMem: 作业内存规格
注意：此字段可能返回 null，表示取不到有效值。
        :type CuMem: int
        :param _StatusDesc: 作业状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _CurrentRunMillis: 运行状态时表示单次运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentRunMillis: int
        :param _ClusterId: 作业所在的集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _WebUIUrl: 作业管理WEB UI 入口
注意：此字段可能返回 null，表示取不到有效值。
        :type WebUIUrl: str
        :param _SchedulerType: 作业所在集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SchedulerType: int
        :param _ClusterStatus: 作业所在集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStatus: int
        :param _RunningCu: 细粒度下的运行的CU数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningCu: float
        :param _FlinkVersion: 作业运行的 Flink 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FlinkVersion: str
        :param _WorkSpaceId: 工作空间 SerialId
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkSpaceId: str
        :param _WorkSpaceName: 工作空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkSpaceName: str
        :param _Tags: 作业标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _EventInfo: 作业异常事件信息	
注意：此字段可能返回 null，表示取不到有效值。
        :type EventInfo: :class:`tencentcloud.oceanus.v20190422.models.JobEventInfo`
        :param _Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ScalingType: 0:代表没开启调优任务，1:开启智能调优，2:代表定时调优

注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingType: int
        :param _RunningCpu: 使用CPU数目
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningCpu: float
        :param _RunningMem: 使用内存数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningMem: float
        :param _OpenJobDefaultAlarm: 是否开了默认告警
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenJobDefaultAlarm: int
        :param _ProgressDesc: 操作中描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgressDesc: str
        """
        self._JobId = None
        self._Region = None
        self._Zone = None
        self._AppId = None
        self._OwnerUin = None
        self._CreatorUin = None
        self._Name = None
        self._JobType = None
        self._Status = None
        self._CreateTime = None
        self._StartTime = None
        self._StopTime = None
        self._UpdateTime = None
        self._TotalRunMillis = None
        self._Remark = None
        self._LastOpResult = None
        self._ClusterName = None
        self._LatestJobConfigVersion = None
        self._PublishedJobConfigVersion = None
        self._RunningCuNum = None
        self._CuMem = None
        self._StatusDesc = None
        self._CurrentRunMillis = None
        self._ClusterId = None
        self._WebUIUrl = None
        self._SchedulerType = None
        self._ClusterStatus = None
        self._RunningCu = None
        self._FlinkVersion = None
        self._WorkSpaceId = None
        self._WorkSpaceName = None
        self._Tags = None
        self._EventInfo = None
        self._Description = None
        self._ScalingType = None
        self._RunningCpu = None
        self._RunningMem = None
        self._OpenJobDefaultAlarm = None
        self._ProgressDesc = None

    @property
    def JobId(self):
        """作业ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Region(self):
        """地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AppId(self):
        """用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OwnerUin(self):
        """用户UIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreatorUin(self):
        """创建者UIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def Name(self):
        """作业名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def JobType(self):
        """作业类型，1：sql作业，2：Jar作业
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def Status(self):
        """作业状态，1：未初始化，2：未发布，3：操作中，4：运行中，5：停止，6：暂停，-1：故障
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """作业创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """作业启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StopTime(self):
        """作业停止时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StopTime

    @StopTime.setter
    def StopTime(self, StopTime):
        self._StopTime = StopTime

    @property
    def UpdateTime(self):
        """作业更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TotalRunMillis(self):
        """作业累计运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalRunMillis

    @TotalRunMillis.setter
    def TotalRunMillis(self, TotalRunMillis):
        self._TotalRunMillis = TotalRunMillis

    @property
    def Remark(self):
        """备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def LastOpResult(self):
        """操作错误提示信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastOpResult

    @LastOpResult.setter
    def LastOpResult(self, LastOpResult):
        self._LastOpResult = LastOpResult

    @property
    def ClusterName(self):
        """集群名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def LatestJobConfigVersion(self):
        """最新配置版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LatestJobConfigVersion

    @LatestJobConfigVersion.setter
    def LatestJobConfigVersion(self, LatestJobConfigVersion):
        self._LatestJobConfigVersion = LatestJobConfigVersion

    @property
    def PublishedJobConfigVersion(self):
        """已发布的配置版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PublishedJobConfigVersion

    @PublishedJobConfigVersion.setter
    def PublishedJobConfigVersion(self, PublishedJobConfigVersion):
        self._PublishedJobConfigVersion = PublishedJobConfigVersion

    @property
    def RunningCuNum(self):
        """运行的CU数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RunningCuNum

    @RunningCuNum.setter
    def RunningCuNum(self, RunningCuNum):
        self._RunningCuNum = RunningCuNum

    @property
    def CuMem(self):
        """作业内存规格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CuMem

    @CuMem.setter
    def CuMem(self, CuMem):
        self._CuMem = CuMem

    @property
    def StatusDesc(self):
        """作业状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CurrentRunMillis(self):
        """运行状态时表示单次运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CurrentRunMillis

    @CurrentRunMillis.setter
    def CurrentRunMillis(self, CurrentRunMillis):
        self._CurrentRunMillis = CurrentRunMillis

    @property
    def ClusterId(self):
        """作业所在的集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def WebUIUrl(self):
        """作业管理WEB UI 入口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WebUIUrl

    @WebUIUrl.setter
    def WebUIUrl(self, WebUIUrl):
        self._WebUIUrl = WebUIUrl

    @property
    def SchedulerType(self):
        """作业所在集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SchedulerType

    @SchedulerType.setter
    def SchedulerType(self, SchedulerType):
        self._SchedulerType = SchedulerType

    @property
    def ClusterStatus(self):
        """作业所在集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def RunningCu(self):
        """细粒度下的运行的CU数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RunningCu

    @RunningCu.setter
    def RunningCu(self, RunningCu):
        self._RunningCu = RunningCu

    @property
    def FlinkVersion(self):
        """作业运行的 Flink 版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FlinkVersion

    @FlinkVersion.setter
    def FlinkVersion(self, FlinkVersion):
        self._FlinkVersion = FlinkVersion

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def WorkSpaceName(self):
        """工作空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkSpaceName

    @WorkSpaceName.setter
    def WorkSpaceName(self, WorkSpaceName):
        self._WorkSpaceName = WorkSpaceName

    @property
    def Tags(self):
        """作业标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EventInfo(self):
        """作业异常事件信息	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.JobEventInfo`
        """
        return self._EventInfo

    @EventInfo.setter
    def EventInfo(self, EventInfo):
        self._EventInfo = EventInfo

    @property
    def Description(self):
        """描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ScalingType(self):
        """0:代表没开启调优任务，1:开启智能调优，2:代表定时调优

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ScalingType

    @ScalingType.setter
    def ScalingType(self, ScalingType):
        self._ScalingType = ScalingType

    @property
    def RunningCpu(self):
        """使用CPU数目
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RunningCpu

    @RunningCpu.setter
    def RunningCpu(self, RunningCpu):
        self._RunningCpu = RunningCpu

    @property
    def RunningMem(self):
        """使用内存数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RunningMem

    @RunningMem.setter
    def RunningMem(self, RunningMem):
        self._RunningMem = RunningMem

    @property
    def OpenJobDefaultAlarm(self):
        """是否开了默认告警
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OpenJobDefaultAlarm

    @OpenJobDefaultAlarm.setter
    def OpenJobDefaultAlarm(self, OpenJobDefaultAlarm):
        self._OpenJobDefaultAlarm = OpenJobDefaultAlarm

    @property
    def ProgressDesc(self):
        """操作中描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProgressDesc

    @ProgressDesc.setter
    def ProgressDesc(self, ProgressDesc):
        self._ProgressDesc = ProgressDesc


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._AppId = params.get("AppId")
        self._OwnerUin = params.get("OwnerUin")
        self._CreatorUin = params.get("CreatorUin")
        self._Name = params.get("Name")
        self._JobType = params.get("JobType")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._StopTime = params.get("StopTime")
        self._UpdateTime = params.get("UpdateTime")
        self._TotalRunMillis = params.get("TotalRunMillis")
        self._Remark = params.get("Remark")
        self._LastOpResult = params.get("LastOpResult")
        self._ClusterName = params.get("ClusterName")
        self._LatestJobConfigVersion = params.get("LatestJobConfigVersion")
        self._PublishedJobConfigVersion = params.get("PublishedJobConfigVersion")
        self._RunningCuNum = params.get("RunningCuNum")
        self._CuMem = params.get("CuMem")
        self._StatusDesc = params.get("StatusDesc")
        self._CurrentRunMillis = params.get("CurrentRunMillis")
        self._ClusterId = params.get("ClusterId")
        self._WebUIUrl = params.get("WebUIUrl")
        self._SchedulerType = params.get("SchedulerType")
        self._ClusterStatus = params.get("ClusterStatus")
        self._RunningCu = params.get("RunningCu")
        self._FlinkVersion = params.get("FlinkVersion")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._WorkSpaceName = params.get("WorkSpaceName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("EventInfo") is not None:
            self._EventInfo = JobEventInfo()
            self._EventInfo._deserialize(params.get("EventInfo"))
        self._Description = params.get("Description")
        self._ScalingType = params.get("ScalingType")
        self._RunningCpu = params.get("RunningCpu")
        self._RunningMem = params.get("RunningMem")
        self._OpenJobDefaultAlarm = params.get("OpenJobDefaultAlarm")
        self._ProgressDesc = params.get("ProgressDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogContent(AbstractModel):
    """日志查询的每行日志信息

    """

    def __init__(self):
        r"""
        :param _Log: 日志内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Log: str
        :param _Time: 毫秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param _PkgId: 日志组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param _PkgLogId: 日志Id，在日志组范围里唯一
        :type PkgLogId: int
        :param _ContainerName: 日志所属的容器名
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerName: str
        """
        self._Log = None
        self._Time = None
        self._PkgId = None
        self._PkgLogId = None
        self._ContainerName = None

    @property
    def Log(self):
        """日志内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def Time(self):
        """毫秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def PkgId(self):
        """日志组Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        """日志Id，在日志组范围里唯一
        :rtype: int
        """
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def ContainerName(self):
        """日志所属的容器名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName


    def _deserialize(self, params):
        self._Log = params.get("Log")
        self._Time = params.get("Time")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._ContainerName = params.get("ContainerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogicalType(AbstractModel):
    """SqlGateway返回LogicalType类型

    """

    def __init__(self):
        r"""
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _NullAble: 是否允许为空
注意：此字段可能返回 null，表示取不到有效值。
        :type NullAble: bool
        :param _Length: 长度
注意：此字段可能返回 null，表示取不到有效值。
        :type Length: int
        """
        self._Type = None
        self._NullAble = None
        self._Length = None

    @property
    def Type(self):
        """类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NullAble(self):
        """是否允许为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._NullAble

    @NullAble.setter
    def NullAble(self, NullAble):
        self._NullAble = NullAble

    @property
    def Length(self):
        """长度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._NullAble = params.get("NullAble")
        self._Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFolderRequest(AbstractModel):
    """ModifyFolder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceFolderId: 文件夹ID（必填）
        :type SourceFolderId: str
        :param _TargetFolderId: 如需拖拽文件夹，需传入目标文件夹ID
        :type TargetFolderId: str
        :param _FolderName: 如需修改文件夹名，需传入FolderName字段
        :type FolderName: str
        :param _FolderType: 文件夹类型，0是任务文件夹，1是依赖文件夹
        :type FolderType: int
        :param _SourceJobIds: 批量移动的作业serial id 列表
        :type SourceJobIds: list of str
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._SourceFolderId = None
        self._TargetFolderId = None
        self._FolderName = None
        self._FolderType = None
        self._SourceJobIds = None
        self._WorkSpaceId = None

    @property
    def SourceFolderId(self):
        """文件夹ID（必填）
        :rtype: str
        """
        return self._SourceFolderId

    @SourceFolderId.setter
    def SourceFolderId(self, SourceFolderId):
        self._SourceFolderId = SourceFolderId

    @property
    def TargetFolderId(self):
        """如需拖拽文件夹，需传入目标文件夹ID
        :rtype: str
        """
        return self._TargetFolderId

    @TargetFolderId.setter
    def TargetFolderId(self, TargetFolderId):
        self._TargetFolderId = TargetFolderId

    @property
    def FolderName(self):
        """如需修改文件夹名，需传入FolderName字段
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName

    @property
    def FolderType(self):
        """文件夹类型，0是任务文件夹，1是依赖文件夹
        :rtype: int
        """
        return self._FolderType

    @FolderType.setter
    def FolderType(self, FolderType):
        self._FolderType = FolderType

    @property
    def SourceJobIds(self):
        """批量移动的作业serial id 列表
        :rtype: list of str
        """
        return self._SourceJobIds

    @SourceJobIds.setter
    def SourceJobIds(self, SourceJobIds):
        self._SourceJobIds = SourceJobIds

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._SourceFolderId = params.get("SourceFolderId")
        self._TargetFolderId = params.get("TargetFolderId")
        self._FolderName = params.get("FolderName")
        self._FolderType = params.get("FolderType")
        self._SourceJobIds = params.get("SourceJobIds")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFolderResponse(AbstractModel):
    """ModifyFolder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyJobRequest(AbstractModel):
    """ModifyJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业Id
        :type JobId: str
        :param _Name: 作业名称，支持长度小于50的中文/英文/数字/”-”/”_”/”.”，不能重名
        :type Name: str
        :param _Remark: 描述
        :type Remark: str
        :param _TargetFolderId: 拖拽文件需传入此参数
        :type TargetFolderId: str
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _Description: 作业描述
        :type Description: str
        """
        self._JobId = None
        self._Name = None
        self._Remark = None
        self._TargetFolderId = None
        self._WorkSpaceId = None
        self._Description = None

    @property
    def JobId(self):
        """作业Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Name(self):
        """作业名称，支持长度小于50的中文/英文/数字/”-”/”_”/”.”，不能重名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TargetFolderId(self):
        """拖拽文件需传入此参数
        :rtype: str
        """
        return self._TargetFolderId

    @TargetFolderId.setter
    def TargetFolderId(self, TargetFolderId):
        self._TargetFolderId = TargetFolderId

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def Description(self):
        """作业描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._TargetFolderId = params.get("TargetFolderId")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyJobResponse(AbstractModel):
    """ModifyJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyWorkSpaceRequest(AbstractModel):
    """ModifyWorkSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _WorkSpaceName: 待修改的工作空间名称
        :type WorkSpaceName: str
        :param _Description: 待修改的工作空间备注
        :type Description: str
        """
        self._WorkSpaceId = None
        self._WorkSpaceName = None
        self._Description = None

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def WorkSpaceName(self):
        """待修改的工作空间名称
        :rtype: str
        """
        return self._WorkSpaceName

    @WorkSpaceName.setter
    def WorkSpaceName(self, WorkSpaceName):
        self._WorkSpaceName = WorkSpaceName

    @property
    def Description(self):
        """待修改的工作空间备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._WorkSpaceName = params.get("WorkSpaceName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkSpaceResponse(AbstractModel):
    """ModifyWorkSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NodeConfig(AbstractModel):
    """专家模式  计算节点的配置信息

    """

    def __init__(self):
        r"""
        :param _Id: Node ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Parallelism: Node parallelism
注意：此字段可能返回 null，表示取不到有效值。
        :type Parallelism: int
        :param _SlotSharingGroup: Slot sharing group
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotSharingGroup: str
        :param _Configuration: Configuration properties
注意：此字段可能返回 null，表示取不到有效值。
        :type Configuration: list of Property
        :param _StateTTL: 节点的状态ttl配置, 多个用 ; 分割
注意：此字段可能返回 null，表示取不到有效值。
        :type StateTTL: str
        """
        self._Id = None
        self._Parallelism = None
        self._SlotSharingGroup = None
        self._Configuration = None
        self._StateTTL = None

    @property
    def Id(self):
        """Node ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Parallelism(self):
        """Node parallelism
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Parallelism

    @Parallelism.setter
    def Parallelism(self, Parallelism):
        self._Parallelism = Parallelism

    @property
    def SlotSharingGroup(self):
        """Slot sharing group
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SlotSharingGroup

    @SlotSharingGroup.setter
    def SlotSharingGroup(self, SlotSharingGroup):
        self._SlotSharingGroup = SlotSharingGroup

    @property
    def Configuration(self):
        """Configuration properties
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Property
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def StateTTL(self):
        """节点的状态ttl配置, 多个用 ; 分割
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StateTTL

    @StateTTL.setter
    def StateTTL(self, StateTTL):
        self._StateTTL = StateTTL


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Parallelism = params.get("Parallelism")
        self._SlotSharingGroup = params.get("SlotSharingGroup")
        if params.get("Configuration") is not None:
            self._Configuration = []
            for item in params.get("Configuration"):
                obj = Property()
                obj._deserialize(item)
                self._Configuration.append(obj)
        self._StateTTL = params.get("StateTTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Order(AbstractModel):
    """集群购买、扩缩容、续费订单信息

    """

    def __init__(self):
        r"""
        :param _Type: 创建、续费、扩缩容 1 2 3
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _AutoRenewFlag: 自动续费 1
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _OperateUin: 操作人的UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateUin: str
        :param _ComputeCu: 最终集群的CU数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ComputeCu: int
        :param _OrderTime: 订单的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderTime: str
        """
        self._Type = None
        self._AutoRenewFlag = None
        self._OperateUin = None
        self._ComputeCu = None
        self._OrderTime = None

    @property
    def Type(self):
        """创建、续费、扩缩容 1 2 3
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AutoRenewFlag(self):
        """自动续费 1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def OperateUin(self):
        """操作人的UIN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def ComputeCu(self):
        """最终集群的CU数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ComputeCu

    @ComputeCu.setter
    def ComputeCu(self, ComputeCu):
        self._ComputeCu = ComputeCu

    @property
    def OrderTime(self):
        """订单的时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrderTime

    @OrderTime.setter
    def OrderTime(self, OrderTime):
        self._OrderTime = OrderTime


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._OperateUin = params.get("OperateUin")
        self._ComputeCu = params.get("ComputeCu")
        self._OrderTime = params.get("OrderTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Property(AbstractModel):
    """系统配置属性

    """

    def __init__(self):
        r"""
        :param _Key: 系统配置的Key
        :type Key: str
        :param _Value: 系统配置的Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """系统配置的Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """系统配置的Value
        :rtype: str
        """
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
        


class RefJobStatusCountItem(AbstractModel):
    """依赖作业分状态计数信息

    """

    def __init__(self):
        r"""
        :param _JobStatus: 作业状态
注意：此字段可能返回 null，表示取不到有效值。
        :type JobStatus: int
        :param _Count: 作业数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._JobStatus = None
        self._Count = None

    @property
    def JobStatus(self):
        """作业状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def Count(self):
        """作业数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._JobStatus = params.get("JobStatus")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceConfigItem(AbstractModel):
    """描述资源配置的返回参数

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _ResourceType: 资源类型
        :type ResourceType: int
        :param _Region: 资源所属地域
        :type Region: str
        :param _AppId: 资源所属AppId
        :type AppId: int
        :param _OwnerUin: 主账号Uin
        :type OwnerUin: str
        :param _CreatorUin: 子账号Uin
        :type CreatorUin: str
        :param _ResourceLoc: 资源位置描述
        :type ResourceLoc: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        :param _CreateTime: 资源创建时间
        :type CreateTime: str
        :param _Version: 资源版本
        :type Version: int
        :param _Remark: 资源描述
        :type Remark: str
        :param _Status: 资源状态：0: 资源同步中，1:资源已就绪
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _RefJobCount: 关联作业个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RefJobCount: int
        :param _RefJobStatusCountSet: 分状态统计关联作业数
注意：此字段可能返回 null，表示取不到有效值。
        :type RefJobStatusCountSet: list of RefJobStatusCountItem
        """
        self._ResourceId = None
        self._ResourceType = None
        self._Region = None
        self._AppId = None
        self._OwnerUin = None
        self._CreatorUin = None
        self._ResourceLoc = None
        self._CreateTime = None
        self._Version = None
        self._Remark = None
        self._Status = None
        self._RefJobCount = None
        self._RefJobStatusCountSet = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        """资源类型
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Region(self):
        """资源所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AppId(self):
        """资源所属AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OwnerUin(self):
        """主账号Uin
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreatorUin(self):
        """子账号Uin
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def ResourceLoc(self):
        """资源位置描述
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        """
        return self._ResourceLoc

    @ResourceLoc.setter
    def ResourceLoc(self, ResourceLoc):
        self._ResourceLoc = ResourceLoc

    @property
    def CreateTime(self):
        """资源创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Version(self):
        """资源版本
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Remark(self):
        """资源描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Status(self):
        """资源状态：0: 资源同步中，1:资源已就绪
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RefJobCount(self):
        """关联作业个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RefJobCount

    @RefJobCount.setter
    def RefJobCount(self, RefJobCount):
        self._RefJobCount = RefJobCount

    @property
    def RefJobStatusCountSet(self):
        """分状态统计关联作业数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RefJobStatusCountItem
        """
        return self._RefJobStatusCountSet

    @RefJobStatusCountSet.setter
    def RefJobStatusCountSet(self, RefJobStatusCountSet):
        self._RefJobStatusCountSet = RefJobStatusCountSet


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._Region = params.get("Region")
        self._AppId = params.get("AppId")
        self._OwnerUin = params.get("OwnerUin")
        self._CreatorUin = params.get("CreatorUin")
        if params.get("ResourceLoc") is not None:
            self._ResourceLoc = ResourceLoc()
            self._ResourceLoc._deserialize(params.get("ResourceLoc"))
        self._CreateTime = params.get("CreateTime")
        self._Version = params.get("Version")
        self._Remark = params.get("Remark")
        self._Status = params.get("Status")
        self._RefJobCount = params.get("RefJobCount")
        if params.get("RefJobStatusCountSet") is not None:
            self._RefJobStatusCountSet = []
            for item in params.get("RefJobStatusCountSet"):
                obj = RefJobStatusCountItem()
                obj._deserialize(item)
                self._RefJobStatusCountSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceItem(AbstractModel):
    """资源详细描述

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _Name: 资源名称
        :type Name: str
        :param _ResourceType: 资源类型
        :type ResourceType: int
        :param _ResourceLoc: 资源位置
        :type ResourceLoc: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        :param _Region: 资源地域
        :type Region: str
        :param _AppId: 应用ID
        :type AppId: int
        :param _OwnerUin: 主账号Uin
        :type OwnerUin: str
        :param _CreatorUin: 子账号Uin
        :type CreatorUin: str
        :param _CreateTime: 资源创建时间
        :type CreateTime: str
        :param _UpdateTime: 资源最后更新时间
        :type UpdateTime: str
        :param _LatestResourceConfigVersion: 资源的资源版本ID
        :type LatestResourceConfigVersion: int
        :param _Remark: 资源备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _VersionCount: 版本个数
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionCount: int
        :param _RefJobCount: 关联作业数
注意：此字段可能返回 null，表示取不到有效值。
        :type RefJobCount: int
        :param _IsJobRun: 作业运行状态
        :type IsJobRun: int
        :param _FileName: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _WorkSpaceId: 工作空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkSpaceId: int
        :param _RefJobStatusCountSet: 分状态统计关联作业数
注意：此字段可能返回 null，表示取不到有效值。
        :type RefJobStatusCountSet: list of RefJobStatusCountItem
        :param _Connector: 连接器名称
        :type Connector: str
        :param _ConnectorVersion: 连接器版本
        :type ConnectorVersion: str
        :param _ConnectionMethod: 连接方式
        :type ConnectionMethod: str
        :param _RelatedResourceId: connector关联的资源id
        :type RelatedResourceId: str
        :param _Icon: 图标
        :type Icon: str
        :param _ConnectorName: 连接器中文名
        :type ConnectorName: str
        :param _ConnectorUrl: 连接器官网链接
        :type ConnectorUrl: str
        """
        self._ResourceId = None
        self._Name = None
        self._ResourceType = None
        self._ResourceLoc = None
        self._Region = None
        self._AppId = None
        self._OwnerUin = None
        self._CreatorUin = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LatestResourceConfigVersion = None
        self._Remark = None
        self._VersionCount = None
        self._RefJobCount = None
        self._IsJobRun = None
        self._FileName = None
        self._WorkSpaceId = None
        self._RefJobStatusCountSet = None
        self._Connector = None
        self._ConnectorVersion = None
        self._ConnectionMethod = None
        self._RelatedResourceId = None
        self._Icon = None
        self._ConnectorName = None
        self._ConnectorUrl = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Name(self):
        """资源名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ResourceType(self):
        """资源类型
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceLoc(self):
        """资源位置
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.ResourceLoc`
        """
        return self._ResourceLoc

    @ResourceLoc.setter
    def ResourceLoc(self, ResourceLoc):
        self._ResourceLoc = ResourceLoc

    @property
    def Region(self):
        """资源地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AppId(self):
        """应用ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OwnerUin(self):
        """主账号Uin
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreatorUin(self):
        """子账号Uin
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def CreateTime(self):
        """资源创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """资源最后更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LatestResourceConfigVersion(self):
        """资源的资源版本ID
        :rtype: int
        """
        return self._LatestResourceConfigVersion

    @LatestResourceConfigVersion.setter
    def LatestResourceConfigVersion(self, LatestResourceConfigVersion):
        self._LatestResourceConfigVersion = LatestResourceConfigVersion

    @property
    def Remark(self):
        """资源备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def VersionCount(self):
        """版本个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VersionCount

    @VersionCount.setter
    def VersionCount(self, VersionCount):
        self._VersionCount = VersionCount

    @property
    def RefJobCount(self):
        """关联作业数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RefJobCount

    @RefJobCount.setter
    def RefJobCount(self, RefJobCount):
        self._RefJobCount = RefJobCount

    @property
    def IsJobRun(self):
        """作业运行状态
        :rtype: int
        """
        return self._IsJobRun

    @IsJobRun.setter
    def IsJobRun(self, IsJobRun):
        self._IsJobRun = IsJobRun

    @property
    def FileName(self):
        """文件名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def WorkSpaceId(self):
        """工作空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def RefJobStatusCountSet(self):
        """分状态统计关联作业数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RefJobStatusCountItem
        """
        return self._RefJobStatusCountSet

    @RefJobStatusCountSet.setter
    def RefJobStatusCountSet(self, RefJobStatusCountSet):
        self._RefJobStatusCountSet = RefJobStatusCountSet

    @property
    def Connector(self):
        """连接器名称
        :rtype: str
        """
        return self._Connector

    @Connector.setter
    def Connector(self, Connector):
        self._Connector = Connector

    @property
    def ConnectorVersion(self):
        """连接器版本
        :rtype: str
        """
        return self._ConnectorVersion

    @ConnectorVersion.setter
    def ConnectorVersion(self, ConnectorVersion):
        self._ConnectorVersion = ConnectorVersion

    @property
    def ConnectionMethod(self):
        """连接方式
        :rtype: str
        """
        return self._ConnectionMethod

    @ConnectionMethod.setter
    def ConnectionMethod(self, ConnectionMethod):
        self._ConnectionMethod = ConnectionMethod

    @property
    def RelatedResourceId(self):
        """connector关联的资源id
        :rtype: str
        """
        return self._RelatedResourceId

    @RelatedResourceId.setter
    def RelatedResourceId(self, RelatedResourceId):
        self._RelatedResourceId = RelatedResourceId

    @property
    def Icon(self):
        """图标
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def ConnectorName(self):
        """连接器中文名
        :rtype: str
        """
        return self._ConnectorName

    @ConnectorName.setter
    def ConnectorName(self, ConnectorName):
        self._ConnectorName = ConnectorName

    @property
    def ConnectorUrl(self):
        """连接器官网链接
        :rtype: str
        """
        return self._ConnectorUrl

    @ConnectorUrl.setter
    def ConnectorUrl(self, ConnectorUrl):
        self._ConnectorUrl = ConnectorUrl


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Name = params.get("Name")
        self._ResourceType = params.get("ResourceType")
        if params.get("ResourceLoc") is not None:
            self._ResourceLoc = ResourceLoc()
            self._ResourceLoc._deserialize(params.get("ResourceLoc"))
        self._Region = params.get("Region")
        self._AppId = params.get("AppId")
        self._OwnerUin = params.get("OwnerUin")
        self._CreatorUin = params.get("CreatorUin")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._LatestResourceConfigVersion = params.get("LatestResourceConfigVersion")
        self._Remark = params.get("Remark")
        self._VersionCount = params.get("VersionCount")
        self._RefJobCount = params.get("RefJobCount")
        self._IsJobRun = params.get("IsJobRun")
        self._FileName = params.get("FileName")
        self._WorkSpaceId = params.get("WorkSpaceId")
        if params.get("RefJobStatusCountSet") is not None:
            self._RefJobStatusCountSet = []
            for item in params.get("RefJobStatusCountSet"):
                obj = RefJobStatusCountItem()
                obj._deserialize(item)
                self._RefJobStatusCountSet.append(obj)
        self._Connector = params.get("Connector")
        self._ConnectorVersion = params.get("ConnectorVersion")
        self._ConnectionMethod = params.get("ConnectionMethod")
        self._RelatedResourceId = params.get("RelatedResourceId")
        self._Icon = params.get("Icon")
        self._ConnectorName = params.get("ConnectorName")
        self._ConnectorUrl = params.get("ConnectorUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceLoc(AbstractModel):
    """资源位置描述

    """

    def __init__(self):
        r"""
        :param _StorageType: 资源位置的存储类型，目前只支持1:COS
        :type StorageType: int
        :param _Param: 描述资源位置的json
        :type Param: :class:`tencentcloud.oceanus.v20190422.models.ResourceLocParam`
        """
        self._StorageType = None
        self._Param = None

    @property
    def StorageType(self):
        """资源位置的存储类型，目前只支持1:COS
        :rtype: int
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Param(self):
        """描述资源位置的json
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.ResourceLocParam`
        """
        return self._Param

    @Param.setter
    def Param(self, Param):
        self._Param = Param


    def _deserialize(self, params):
        self._StorageType = params.get("StorageType")
        if params.get("Param") is not None:
            self._Param = ResourceLocParam()
            self._Param._deserialize(params.get("Param"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceLocParam(AbstractModel):
    """资源参数描述

    """

    def __init__(self):
        r"""
        :param _Bucket: 资源bucket
        :type Bucket: str
        :param _Path: 资源路径
        :type Path: str
        :param _Region: 资源所在地域，如果不填，则使用Resource的Region
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._Bucket = None
        self._Path = None
        self._Region = None

    @property
    def Bucket(self):
        """资源bucket
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Path(self):
        """资源路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Region(self):
        """资源所在地域，如果不填，则使用Resource的Region
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Path = params.get("Path")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceRef(AbstractModel):
    """资源引用参数

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _Version: 资源版本ID，-1表示使用最新版本
        :type Version: int
        :param _Type: 引用资源类型，例如主资源设置为1，代表main class所在的jar包
        :type Type: int
        """
        self._ResourceId = None
        self._Version = None
        self._Type = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Version(self):
        """资源版本ID，-1表示使用最新版本
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Type(self):
        """引用资源类型，例如主资源设置为1，代表main class所在的jar包
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Version = params.get("Version")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceRefDetail(AbstractModel):
    """JobConfig引用资源信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _Version: 资源版本，-1表示使用最新版本
        :type Version: int
        :param _Name: 资源名称
        :type Name: str
        :param _Type: 1: 主资源
        :type Type: int
        :param _SystemProvide: 1: 系统内置资源
        :type SystemProvide: int
        :param _Connector: Connector
        :type Connector: str
        """
        self._ResourceId = None
        self._Version = None
        self._Name = None
        self._Type = None
        self._SystemProvide = None
        self._Connector = None

    @property
    def ResourceId(self):
        """资源id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Version(self):
        """资源版本，-1表示使用最新版本
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Name(self):
        """资源名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """1: 主资源
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SystemProvide(self):
        """1: 系统内置资源
        :rtype: int
        """
        return self._SystemProvide

    @SystemProvide.setter
    def SystemProvide(self, SystemProvide):
        self._SystemProvide = SystemProvide

    @property
    def Connector(self):
        """Connector
        :rtype: str
        """
        return self._Connector

    @Connector.setter
    def Connector(self, Connector):
        self._Connector = Connector


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Version = params.get("Version")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._SystemProvide = params.get("SystemProvide")
        self._Connector = params.get("Connector")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceRefJobInfo(AbstractModel):
    """资源被Job 引用信息

    """

    def __init__(self):
        r"""
        :param _JobId: Job id
        :type JobId: str
        :param _JobConfigVersion: Job配置版本
        :type JobConfigVersion: int
        :param _ResourceVersion: 资源版本
        :type ResourceVersion: int
        """
        self._JobId = None
        self._JobConfigVersion = None
        self._ResourceVersion = None

    @property
    def JobId(self):
        """Job id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobConfigVersion(self):
        """Job配置版本
        :rtype: int
        """
        return self._JobConfigVersion

    @JobConfigVersion.setter
    def JobConfigVersion(self, JobConfigVersion):
        self._JobConfigVersion = JobConfigVersion

    @property
    def ResourceVersion(self):
        """资源版本
        :rtype: int
        """
        return self._ResourceVersion

    @ResourceVersion.setter
    def ResourceVersion(self, ResourceVersion):
        self._ResourceVersion = ResourceVersion


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobConfigVersion = params.get("JobConfigVersion")
        self._ResourceVersion = params.get("ResourceVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceRefLatest(AbstractModel):
    """资源引用

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: int
        :param _Type: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _WorkspaceId: 空间id
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: str
        :param _Name: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._ResourceId = None
        self._Version = None
        self._Type = None
        self._Status = None
        self._WorkspaceId = None
        self._Name = None

    @property
    def ResourceId(self):
        """资源id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Version(self):
        """版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Type(self):
        """资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WorkspaceId(self):
        """空间id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Name(self):
        """资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Version = params.get("Version")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._WorkspaceId = params.get("WorkspaceId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultColumn(AbstractModel):
    """Sql Gateway返回Column类型

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _LogicalType: 本地类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type LogicalType: :class:`tencentcloud.oceanus.v20190422.models.LogicalType`
        :param _Comment: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        """
        self._Name = None
        self._LogicalType = None
        self._Comment = None

    @property
    def Name(self):
        """名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LogicalType(self):
        """本地类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.LogicalType`
        """
        return self._LogicalType

    @LogicalType.setter
    def LogicalType(self, LogicalType):
        self._LogicalType = LogicalType

    @property
    def Comment(self):
        """备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("LogicalType") is not None:
            self._LogicalType = LogicalType()
            self._LogicalType._deserialize(params.get("LogicalType"))
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultData(AbstractModel):
    """Sql Gateway返回数据

    """

    def __init__(self):
        r"""
        :param _Kind: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Kind: str
        :param _Fields: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Fields: list of str
        """
        self._Kind = None
        self._Fields = None

    @property
    def Kind(self):
        """操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Fields(self):
        """结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._Kind = params.get("Kind")
        self._Fields = params.get("Fields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleAuth(AbstractModel):
    """角色授权信息

    """

    def __init__(self):
        r"""
        :param _AppId: 用户 AppID
        :type AppId: int
        :param _WorkSpaceSerialId: 工作空间 SerialId
        :type WorkSpaceSerialId: str
        :param _OwnerUin: 主账号 UIN
        :type OwnerUin: str
        :param _CreatorUin: 创建者 UIN
        :type CreatorUin: str
        :param _AuthSubAccountUin: 绑定授权的 UIN
        :type AuthSubAccountUin: str
        :param _Permission: 对应 role表的id
        :type Permission: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 最后一次操作时间
        :type UpdateTime: str
        :param _Status: 2 启用 1 停用
        :type Status: int
        :param _Id: id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _WorkSpaceId: 工作空间id
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkSpaceId: int
        :param _RoleName: 权限名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        """
        self._AppId = None
        self._WorkSpaceSerialId = None
        self._OwnerUin = None
        self._CreatorUin = None
        self._AuthSubAccountUin = None
        self._Permission = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Status = None
        self._Id = None
        self._WorkSpaceId = None
        self._RoleName = None

    @property
    def AppId(self):
        """用户 AppID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def WorkSpaceSerialId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceSerialId

    @WorkSpaceSerialId.setter
    def WorkSpaceSerialId(self, WorkSpaceSerialId):
        self._WorkSpaceSerialId = WorkSpaceSerialId

    @property
    def OwnerUin(self):
        """主账号 UIN
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreatorUin(self):
        """创建者 UIN
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def AuthSubAccountUin(self):
        """绑定授权的 UIN
        :rtype: str
        """
        return self._AuthSubAccountUin

    @AuthSubAccountUin.setter
    def AuthSubAccountUin(self, AuthSubAccountUin):
        self._AuthSubAccountUin = AuthSubAccountUin

    @property
    def Permission(self):
        """对应 role表的id
        :rtype: int
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最后一次操作时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """2 启用 1 停用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        """id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def WorkSpaceId(self):
        """工作空间id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def RoleName(self):
        """权限名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._WorkSpaceSerialId = params.get("WorkSpaceSerialId")
        self._OwnerUin = params.get("OwnerUin")
        self._CreatorUin = params.get("CreatorUin")
        self._AuthSubAccountUin = params.get("AuthSubAccountUin")
        self._Permission = params.get("Permission")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobDescription(AbstractModel):
    """作业启动详情

    """

    def __init__(self):
        r"""
        :param _JobId: 作业Id
        :type JobId: str
        :param _RunType: 运行类型，1：启动，2：恢复
        :type RunType: int
        :param _StartMode: 兼容旧版 SQL 类型作业启动参数：指定数据源消费起始时间点（建议传值）
保证参数为 LATEST、EARLIEST、T+Timestamp （例:T1557394288000）
        :type StartMode: str
        :param _JobConfigVersion: 当前作业的某个版本
（不传默认为非草稿的作业版本）
        :type JobConfigVersion: int
        :param _SavepointPath: Savepoint路径
        :type SavepointPath: str
        :param _SavepointId: Savepoint的Id
        :type SavepointId: str
        :param _UseOldSystemConnector: 使用历史版本系统依赖
        :type UseOldSystemConnector: bool
        :param _CustomTimestamp: 自定义时间戳
        :type CustomTimestamp: int
        :param _KafkaScanMode: timestamp; latest-offset;  earliest-offset; 任选一种
        :type KafkaScanMode: str
        """
        self._JobId = None
        self._RunType = None
        self._StartMode = None
        self._JobConfigVersion = None
        self._SavepointPath = None
        self._SavepointId = None
        self._UseOldSystemConnector = None
        self._CustomTimestamp = None
        self._KafkaScanMode = None

    @property
    def JobId(self):
        """作业Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RunType(self):
        """运行类型，1：启动，2：恢复
        :rtype: int
        """
        return self._RunType

    @RunType.setter
    def RunType(self, RunType):
        self._RunType = RunType

    @property
    def StartMode(self):
        """兼容旧版 SQL 类型作业启动参数：指定数据源消费起始时间点（建议传值）
保证参数为 LATEST、EARLIEST、T+Timestamp （例:T1557394288000）
        :rtype: str
        """
        return self._StartMode

    @StartMode.setter
    def StartMode(self, StartMode):
        self._StartMode = StartMode

    @property
    def JobConfigVersion(self):
        """当前作业的某个版本
（不传默认为非草稿的作业版本）
        :rtype: int
        """
        return self._JobConfigVersion

    @JobConfigVersion.setter
    def JobConfigVersion(self, JobConfigVersion):
        self._JobConfigVersion = JobConfigVersion

    @property
    def SavepointPath(self):
        """Savepoint路径
        :rtype: str
        """
        return self._SavepointPath

    @SavepointPath.setter
    def SavepointPath(self, SavepointPath):
        self._SavepointPath = SavepointPath

    @property
    def SavepointId(self):
        """Savepoint的Id
        :rtype: str
        """
        return self._SavepointId

    @SavepointId.setter
    def SavepointId(self, SavepointId):
        self._SavepointId = SavepointId

    @property
    def UseOldSystemConnector(self):
        """使用历史版本系统依赖
        :rtype: bool
        """
        return self._UseOldSystemConnector

    @UseOldSystemConnector.setter
    def UseOldSystemConnector(self, UseOldSystemConnector):
        self._UseOldSystemConnector = UseOldSystemConnector

    @property
    def CustomTimestamp(self):
        """自定义时间戳
        :rtype: int
        """
        return self._CustomTimestamp

    @CustomTimestamp.setter
    def CustomTimestamp(self, CustomTimestamp):
        self._CustomTimestamp = CustomTimestamp

    @property
    def KafkaScanMode(self):
        """timestamp; latest-offset;  earliest-offset; 任选一种
        :rtype: str
        """
        return self._KafkaScanMode

    @KafkaScanMode.setter
    def KafkaScanMode(self, KafkaScanMode):
        self._KafkaScanMode = KafkaScanMode


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RunType = params.get("RunType")
        self._StartMode = params.get("StartMode")
        self._JobConfigVersion = params.get("JobConfigVersion")
        self._SavepointPath = params.get("SavepointPath")
        self._SavepointId = params.get("SavepointId")
        self._UseOldSystemConnector = params.get("UseOldSystemConnector")
        self._CustomTimestamp = params.get("CustomTimestamp")
        self._KafkaScanMode = params.get("KafkaScanMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobsRequest(AbstractModel):
    """RunJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RunJobDescriptions: 批量启动作业的描述信息
        :type RunJobDescriptions: list of RunJobDescription
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._RunJobDescriptions = None
        self._WorkSpaceId = None

    @property
    def RunJobDescriptions(self):
        """批量启动作业的描述信息
        :rtype: list of RunJobDescription
        """
        return self._RunJobDescriptions

    @RunJobDescriptions.setter
    def RunJobDescriptions(self, RunJobDescriptions):
        self._RunJobDescriptions = RunJobDescriptions

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        if params.get("RunJobDescriptions") is not None:
            self._RunJobDescriptions = []
            for item in params.get("RunJobDescriptions"):
                obj = RunJobDescription()
                obj._deserialize(item)
                self._RunJobDescriptions.append(obj)
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobsResponse(AbstractModel):
    """RunJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RunSqlGatewayStatementRequest(AbstractModel):
    """RunSqlGatewayStatement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Sql: 需要执行的sql，该sql会被Sql Gateway执行，当前支持的是paimon修改需求，因此主要是DDL语句
        :type Sql: str
        :param _SessionId: Sql Gateway会话ID，可不填，如果不填则会自动创建一个会话ID，每个会话ID都有一个存活时间，测试环境为10分钟，线上默认是30分钟
        :type SessionId: str
        """
        self._ClusterId = None
        self._Sql = None
        self._SessionId = None

    @property
    def ClusterId(self):
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Sql(self):
        """需要执行的sql，该sql会被Sql Gateway执行，当前支持的是paimon修改需求，因此主要是DDL语句
        :rtype: str
        """
        return self._Sql

    @Sql.setter
    def Sql(self, Sql):
        self._Sql = Sql

    @property
    def SessionId(self):
        """Sql Gateway会话ID，可不填，如果不填则会自动创建一个会话ID，每个会话ID都有一个存活时间，测试环境为10分钟，线上默认是30分钟
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Sql = params.get("Sql")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSqlGatewayStatementResponse(AbstractModel):
    """RunSqlGatewayStatement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMessage: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: list of str
        :param _SessionId: 会话id，若入参未传，则返回自动创建的会话id，若入参已经传递，则返回值与原传入值一致
        :type SessionId: str
        :param _OperationHandleId: 返回执行id，可以根据该执行id和会话id获取执行结果
        :type OperationHandleId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMessage = None
        self._SessionId = None
        self._OperationHandleId = None
        self._RequestId = None

    @property
    def ErrorMessage(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def SessionId(self):
        """会话id，若入参未传，则返回自动创建的会话id，若入参已经传递，则返回值与原传入值一致
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def OperationHandleId(self):
        """返回执行id，可以根据该执行id和会话id获取执行结果
        :rtype: str
        """
        return self._OperationHandleId

    @OperationHandleId.setter
    def OperationHandleId(self, OperationHandleId):
        self._OperationHandleId = OperationHandleId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorMessage = params.get("ErrorMessage")
        self._SessionId = params.get("SessionId")
        self._OperationHandleId = params.get("OperationHandleId")
        self._RequestId = params.get("RequestId")


class Savepoint(AbstractModel):
    """描述Savepoint信息

    """

    def __init__(self):
        r"""
        :param _Id: 主键
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _VersionId: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param _Status: 状态 1: Active; 2: Expired; 3: InProgress; 4: Failed; 5: Timeout
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _Path: 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Size: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param _RecordType: 快照类型 1: savepoint；2: checkpoint；3: cancelWithSavepoint
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordType: int
        :param _JobRuntimeId: 运行作业实例的顺序 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobRuntimeId: int
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Timeout: 固定超时时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param _SerialId: 快照 serialId
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialId: str
        :param _TimeConsuming: 耗时
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeConsuming: int
        :param _PathStatus: 快照路径状态 1：可用；2：不可用；
注意：此字段可能返回 null，表示取不到有效值。
        :type PathStatus: int
        """
        self._Id = None
        self._VersionId = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Path = None
        self._Size = None
        self._RecordType = None
        self._JobRuntimeId = None
        self._Description = None
        self._Timeout = None
        self._SerialId = None
        self._TimeConsuming = None
        self._PathStatus = None

    @property
    def Id(self):
        """主键
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def VersionId(self):
        """版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Status(self):
        """状态 1: Active; 2: Expired; 3: InProgress; 4: Failed; 5: Timeout
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Path(self):
        """路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Size(self):
        """大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def RecordType(self):
        """快照类型 1: savepoint；2: checkpoint；3: cancelWithSavepoint
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def JobRuntimeId(self):
        """运行作业实例的顺序 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._JobRuntimeId

    @JobRuntimeId.setter
    def JobRuntimeId(self, JobRuntimeId):
        self._JobRuntimeId = JobRuntimeId

    @property
    def Description(self):
        """描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Timeout(self):
        """固定超时时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def SerialId(self):
        """快照 serialId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SerialId

    @SerialId.setter
    def SerialId(self, SerialId):
        self._SerialId = SerialId

    @property
    def TimeConsuming(self):
        """耗时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimeConsuming

    @TimeConsuming.setter
    def TimeConsuming(self, TimeConsuming):
        self._TimeConsuming = TimeConsuming

    @property
    def PathStatus(self):
        """快照路径状态 1：可用；2：不可用；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PathStatus

    @PathStatus.setter
    def PathStatus(self, PathStatus):
        self._PathStatus = PathStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._VersionId = params.get("VersionId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Path = params.get("Path")
        self._Size = params.get("Size")
        self._RecordType = params.get("RecordType")
        self._JobRuntimeId = params.get("JobRuntimeId")
        self._Description = params.get("Description")
        self._Timeout = params.get("Timeout")
        self._SerialId = params.get("SerialId")
        self._TimeConsuming = params.get("TimeConsuming")
        self._PathStatus = params.get("PathStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionClusterRefItem(AbstractModel):
    """session集群引用资源信息

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 空间唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: str
        :param _ResourceId: 资源唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: int
        :param _Type: 引用类型，0:用户资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        """
        self._WorkspaceId = None
        self._ResourceId = None
        self._Version = None
        self._Type = None

    @property
    def WorkspaceId(self):
        """空间唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ResourceId(self):
        """资源唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Version(self):
        """版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Type(self):
        """引用类型，0:用户资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ResourceId = params.get("ResourceId")
        self._Version = params.get("Version")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Setats(AbstractModel):
    """setats类型

    """

    def __init__(self):
        r"""
        :param _SetatsSerialId: setats serialId
注意：此字段可能返回 null，表示取不到有效值。
        :type SetatsSerialId: str
        :param _Status: 1  // 停止
2  // 运行中
3  // 初始化中
4  // 扩容中
5  // Warehoouse未配置
6  // Warehoouse配置中
7  // 重启中
-2 // 已删除(集群被销毁时更新为此状态)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Warehouse: setats warehouse
注意：此字段可能返回 null，表示取不到有效值。
        :type Warehouse: :class:`tencentcloud.oceanus.v20190422.models.Warehouse`
        :param _MasterInfo: setats master 机器规格
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterInfo: :class:`tencentcloud.oceanus.v20190422.models.SetatsCvmInfo`
        :param _WorkerInfo: setats worker规格
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkerInfo: :class:`tencentcloud.oceanus.v20190422.models.SetatsCvmInfo`
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _AutoRenewFlag: 自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _SecondsUntilExpiry: 过期时间 秒
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondsUntilExpiry: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ManagerUrl: manager url
注意：此字段可能返回 null，表示取不到有效值。
        :type ManagerUrl: str
        :param _IsolatedTime: 隔离时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        """
        self._SetatsSerialId = None
        self._Status = None
        self._Warehouse = None
        self._MasterInfo = None
        self._WorkerInfo = None
        self._Tags = None
        self._AutoRenewFlag = None
        self._ExpireTime = None
        self._SecondsUntilExpiry = None
        self._CreateTime = None
        self._ManagerUrl = None
        self._IsolatedTime = None

    @property
    def SetatsSerialId(self):
        """setats serialId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SetatsSerialId

    @SetatsSerialId.setter
    def SetatsSerialId(self, SetatsSerialId):
        self._SetatsSerialId = SetatsSerialId

    @property
    def Status(self):
        """1  // 停止
2  // 运行中
3  // 初始化中
4  // 扩容中
5  // Warehoouse未配置
6  // Warehoouse配置中
7  // 重启中
-2 // 已删除(集群被销毁时更新为此状态)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Warehouse(self):
        """setats warehouse
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.Warehouse`
        """
        return self._Warehouse

    @Warehouse.setter
    def Warehouse(self, Warehouse):
        self._Warehouse = Warehouse

    @property
    def MasterInfo(self):
        """setats master 机器规格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.SetatsCvmInfo`
        """
        return self._MasterInfo

    @MasterInfo.setter
    def MasterInfo(self, MasterInfo):
        self._MasterInfo = MasterInfo

    @property
    def WorkerInfo(self):
        """setats worker规格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.SetatsCvmInfo`
        """
        return self._WorkerInfo

    @WorkerInfo.setter
    def WorkerInfo(self, WorkerInfo):
        self._WorkerInfo = WorkerInfo

    @property
    def Tags(self):
        """标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRenewFlag(self):
        """自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ExpireTime(self):
        """过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def SecondsUntilExpiry(self):
        """过期时间 秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecondsUntilExpiry

    @SecondsUntilExpiry.setter
    def SecondsUntilExpiry(self, SecondsUntilExpiry):
        self._SecondsUntilExpiry = SecondsUntilExpiry

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ManagerUrl(self):
        """manager url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ManagerUrl

    @ManagerUrl.setter
    def ManagerUrl(self, ManagerUrl):
        self._ManagerUrl = ManagerUrl

    @property
    def IsolatedTime(self):
        """隔离时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime


    def _deserialize(self, params):
        self._SetatsSerialId = params.get("SetatsSerialId")
        self._Status = params.get("Status")
        if params.get("Warehouse") is not None:
            self._Warehouse = Warehouse()
            self._Warehouse._deserialize(params.get("Warehouse"))
        if params.get("MasterInfo") is not None:
            self._MasterInfo = SetatsCvmInfo()
            self._MasterInfo._deserialize(params.get("MasterInfo"))
        if params.get("WorkerInfo") is not None:
            self._WorkerInfo = SetatsCvmInfo()
            self._WorkerInfo._deserialize(params.get("WorkerInfo"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ExpireTime = params.get("ExpireTime")
        self._SecondsUntilExpiry = params.get("SecondsUntilExpiry")
        self._CreateTime = params.get("CreateTime")
        self._ManagerUrl = params.get("ManagerUrl")
        self._IsolatedTime = params.get("IsolatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetatsCvmInfo(AbstractModel):
    """setats 机器规格

    """

    def __init__(self):
        r"""
        :param _Cpu: setats机器cpu
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: float
        :param _Mem: setats机器内存
注意：此字段可能返回 null，表示取不到有效值。
        :type Mem: float
        :param _DefaultParallelism: setats worker 并行度
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultParallelism: int
        :param _Disk: setats 机器磁盘
注意：此字段可能返回 null，表示取不到有效值。
        :type Disk: :class:`tencentcloud.oceanus.v20190422.models.SetatsDisk`
        """
        self._Cpu = None
        self._Mem = None
        self._DefaultParallelism = None
        self._Disk = None

    @property
    def Cpu(self):
        """setats机器cpu
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        """setats机器内存
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def DefaultParallelism(self):
        """setats worker 并行度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DefaultParallelism

    @DefaultParallelism.setter
    def DefaultParallelism(self, DefaultParallelism):
        self._DefaultParallelism = DefaultParallelism

    @property
    def Disk(self):
        """setats 机器磁盘
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.SetatsDisk`
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._DefaultParallelism = params.get("DefaultParallelism")
        if params.get("Disk") is not None:
            self._Disk = SetatsDisk()
            self._Disk._deserialize(params.get("Disk"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetatsDisk(AbstractModel):
    """setats disk

    """

    def __init__(self):
        r"""
        :param _DiskType: 磁盘类型
CLOUD_BSSD
CLOUD_SSD
CLOUD_HSSD
CLOUD_PREMIUM
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskSize: 磁盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        """磁盘类型
CLOUD_BSSD
CLOUD_SSD
CLOUD_HSSD
CLOUD_PREMIUM
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """磁盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
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
        


class SlotSharingGroup(AbstractModel):
    """SlotSharingGroup 描述

    """

    def __init__(self):
        r"""
        :param _Name: SlotSharingGroup的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Spec: SlotSharingGroup的规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: :class:`tencentcloud.oceanus.v20190422.models.SlotSharingGroupSpec`
        :param _Description: SlotSharingGroup的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Configuration: SlotSharingGroup的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Configuration: list of Property
        """
        self._Name = None
        self._Spec = None
        self._Description = None
        self._Configuration = None

    @property
    def Name(self):
        """SlotSharingGroup的名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Spec(self):
        """SlotSharingGroup的规格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.SlotSharingGroupSpec`
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Description(self):
        """SlotSharingGroup的描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Configuration(self):
        """SlotSharingGroup的配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Property
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Spec") is not None:
            self._Spec = SlotSharingGroupSpec()
            self._Spec._deserialize(params.get("Spec"))
        self._Description = params.get("Description")
        if params.get("Configuration") is not None:
            self._Configuration = []
            for item in params.get("Configuration"):
                obj = Property()
                obj._deserialize(item)
                self._Configuration.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlotSharingGroupSpec(AbstractModel):
    """SlotSharingGroup的规格描述

    """

    def __init__(self):
        r"""
        :param _CPU: 适用的cpu
注意：此字段可能返回 null，表示取不到有效值。
        :type CPU: float
        :param _HeapMemory: 默认为b, 支持单位有 b, kb, mb, gb
注意：此字段可能返回 null，表示取不到有效值。
        :type HeapMemory: str
        :param _OffHeapMemory: 默认为b, 支持单位有 b, kb, mb, gb
注意：此字段可能返回 null，表示取不到有效值。
        :type OffHeapMemory: str
        :param _ManagedMemory: 默认为b, 支持单位有 b, kb, mb, gb
注意：此字段可能返回 null，表示取不到有效值。
        :type ManagedMemory: str
        """
        self._CPU = None
        self._HeapMemory = None
        self._OffHeapMemory = None
        self._ManagedMemory = None

    @property
    def CPU(self):
        """适用的cpu
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def HeapMemory(self):
        """默认为b, 支持单位有 b, kb, mb, gb
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HeapMemory

    @HeapMemory.setter
    def HeapMemory(self, HeapMemory):
        self._HeapMemory = HeapMemory

    @property
    def OffHeapMemory(self):
        """默认为b, 支持单位有 b, kb, mb, gb
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OffHeapMemory

    @OffHeapMemory.setter
    def OffHeapMemory(self, OffHeapMemory):
        self._OffHeapMemory = OffHeapMemory

    @property
    def ManagedMemory(self):
        """默认为b, 支持单位有 b, kb, mb, gb
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ManagedMemory

    @ManagedMemory.setter
    def ManagedMemory(self, ManagedMemory):
        self._ManagedMemory = ManagedMemory


    def _deserialize(self, params):
        self._CPU = params.get("CPU")
        self._HeapMemory = params.get("HeapMemory")
        self._OffHeapMemory = params.get("OffHeapMemory")
        self._ManagedMemory = params.get("ManagedMemory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SqlGatewayItem(AbstractModel):
    """SqlGateway配置信息

    """

    def __init__(self):
        r"""
        :param _SerialId: 唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialId: str
        :param _FlinkVersion: Flink内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FlinkVersion: str
        :param _Status: 状态，1.停止 2. 开启中 3. 开启 4. 开启失败 5. 停止中
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreatorUin: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param _ResourceRefs: 引用资源
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRefs: list of GatewayRefItem
        :param _CuSpec: Cu规格
注意：此字段可能返回 null，表示取不到有效值。
        :type CuSpec: float
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Properties: 配置参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        :param _Cpu: Cpu
        :type Cpu: float
        :param _Mem: Mem
        :type Mem: float
        """
        self._SerialId = None
        self._FlinkVersion = None
        self._Status = None
        self._CreatorUin = None
        self._ResourceRefs = None
        self._CuSpec = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Properties = None
        self._Cpu = None
        self._Mem = None

    @property
    def SerialId(self):
        """唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SerialId

    @SerialId.setter
    def SerialId(self, SerialId):
        self._SerialId = SerialId

    @property
    def FlinkVersion(self):
        """Flink内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FlinkVersion

    @FlinkVersion.setter
    def FlinkVersion(self, FlinkVersion):
        self._FlinkVersion = FlinkVersion

    @property
    def Status(self):
        """状态，1.停止 2. 开启中 3. 开启 4. 开启失败 5. 停止中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatorUin(self):
        """创建人
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def ResourceRefs(self):
        """引用资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of GatewayRefItem
        """
        return self._ResourceRefs

    @ResourceRefs.setter
    def ResourceRefs(self, ResourceRefs):
        self._ResourceRefs = ResourceRefs

    @property
    def CuSpec(self):
        """Cu规格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._CuSpec

    @CuSpec.setter
    def CuSpec(self, CuSpec):
        self._CuSpec = CuSpec

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Properties(self):
        """配置参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Property
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def Cpu(self):
        """Cpu
        :rtype: float
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Mem(self):
        """Mem
        :rtype: float
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem


    def _deserialize(self, params):
        self._SerialId = params.get("SerialId")
        self._FlinkVersion = params.get("FlinkVersion")
        self._Status = params.get("Status")
        self._CreatorUin = params.get("CreatorUin")
        if params.get("ResourceRefs") is not None:
            self._ResourceRefs = []
            for item in params.get("ResourceRefs"):
                obj = GatewayRefItem()
                obj._deserialize(item)
                self._ResourceRefs.append(obj)
        self._CuSpec = params.get("CuSpec")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatementResult(AbstractModel):
    """Sql Gateway 返回Result结构类型

    """

    def __init__(self):
        r"""
        :param _Columns: 返回结果列
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of ResultColumn
        :param _RowFormat: 格式
注意：此字段可能返回 null，表示取不到有效值。
        :type RowFormat: str
        :param _Data: 结果值
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ResultData
        """
        self._Columns = None
        self._RowFormat = None
        self._Data = None

    @property
    def Columns(self):
        """返回结果列
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResultColumn
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def RowFormat(self):
        """格式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RowFormat

    @RowFormat.setter
    def RowFormat(self, RowFormat):
        self._RowFormat = RowFormat

    @property
    def Data(self):
        """结果值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResultData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = ResultColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._RowFormat = params.get("RowFormat")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResultData()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopJobDescription(AbstractModel):
    """停止作业的描述信息

    """

    def __init__(self):
        r"""
        :param _JobId: 作业Id
        :type JobId: str
        :param _StopType: 停止类型，1 停止 2 暂停
        :type StopType: int
        """
        self._JobId = None
        self._StopType = None

    @property
    def JobId(self):
        """作业Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StopType(self):
        """停止类型，1 停止 2 暂停
        :rtype: int
        """
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopJobsRequest(AbstractModel):
    """StopJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StopJobDescriptions: 批量停止作业的描述信息
        :type StopJobDescriptions: list of StopJobDescription
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._StopJobDescriptions = None
        self._WorkSpaceId = None

    @property
    def StopJobDescriptions(self):
        """批量停止作业的描述信息
        :rtype: list of StopJobDescription
        """
        return self._StopJobDescriptions

    @StopJobDescriptions.setter
    def StopJobDescriptions(self, StopJobDescriptions):
        self._StopJobDescriptions = StopJobDescriptions

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        if params.get("StopJobDescriptions") is not None:
            self._StopJobDescriptions = []
            for item in params.get("StopJobDescriptions"):
                obj = StopJobDescription()
                obj._deserialize(item)
                self._StopJobDescriptions.append(obj)
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopJobsResponse(AbstractModel):
    """StopJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SubEks(AbstractModel):
    """混合计费

    """

    def __init__(self):
        r"""
        :param _SerialId: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialId: str
        :param _CuNum: cu数
注意：此字段可能返回 null，表示取不到有效值。
        :type CuNum: int
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _RunningCu: 运行cu
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningCu: float
        :param _TotalCpu: 总的CPU
        :type TotalCpu: float
        :param _TotalMem: 总的内存
        :type TotalMem: float
        :param _RunningCpu: 运行的CPU
        :type RunningCpu: float
        :param _RunningMem: 运行的内存
        :type RunningMem: float
        """
        self._SerialId = None
        self._CuNum = None
        self._Status = None
        self._StatusDesc = None
        self._RunningCu = None
        self._TotalCpu = None
        self._TotalMem = None
        self._RunningCpu = None
        self._RunningMem = None

    @property
    def SerialId(self):
        """集群id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SerialId

    @SerialId.setter
    def SerialId(self, SerialId):
        self._SerialId = SerialId

    @property
    def CuNum(self):
        """cu数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CuNum

    @CuNum.setter
    def CuNum(self, CuNum):
        self._CuNum = CuNum

    @property
    def Status(self):
        """状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def RunningCu(self):
        """运行cu
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RunningCu

    @RunningCu.setter
    def RunningCu(self, RunningCu):
        self._RunningCu = RunningCu

    @property
    def TotalCpu(self):
        """总的CPU
        :rtype: float
        """
        return self._TotalCpu

    @TotalCpu.setter
    def TotalCpu(self, TotalCpu):
        self._TotalCpu = TotalCpu

    @property
    def TotalMem(self):
        """总的内存
        :rtype: float
        """
        return self._TotalMem

    @TotalMem.setter
    def TotalMem(self, TotalMem):
        self._TotalMem = TotalMem

    @property
    def RunningCpu(self):
        """运行的CPU
        :rtype: float
        """
        return self._RunningCpu

    @RunningCpu.setter
    def RunningCpu(self, RunningCpu):
        self._RunningCpu = RunningCpu

    @property
    def RunningMem(self):
        """运行的内存
        :rtype: float
        """
        return self._RunningMem

    @RunningMem.setter
    def RunningMem(self, RunningMem):
        self._RunningMem = RunningMem


    def _deserialize(self, params):
        self._SerialId = params.get("SerialId")
        self._CuNum = params.get("CuNum")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._RunningCu = params.get("RunningCu")
        self._TotalCpu = params.get("TotalCpu")
        self._TotalMem = params.get("TotalMem")
        self._RunningCpu = params.get("RunningCpu")
        self._RunningMem = params.get("RunningMem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubFolderInfo(AbstractModel):
    """子目录信息

    """

    def __init__(self):
        r"""
        :param _FolderId: folder id
        :type FolderId: str
        :param _FolderName: folder name
        :type FolderName: str
        """
        self._FolderId = None
        self._FolderName = None

    @property
    def FolderId(self):
        """folder id
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def FolderName(self):
        """folder name
        :rtype: str
        """
        return self._FolderName

    @FolderName.setter
    def FolderName(self, FolderName):
        self._FolderName = FolderName


    def _deserialize(self, params):
        self._FolderId = params.get("FolderId")
        self._FolderName = params.get("FolderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemResourceItem(AbstractModel):
    """系统资源返回值

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _Name: 资源名称
        :type Name: str
        :param _ResourceType: 资源类型。1 表示 JAR 包，目前只支持该值。
        :type ResourceType: int
        :param _Remark: 资源备注
        :type Remark: str
        :param _Region: 资源所属地域
        :type Region: str
        :param _LatestResourceConfigVersion: 资源的最新版本
        :type LatestResourceConfigVersion: int
        :param _SystemProvide: 1 是系统提供资源 2 用户提供CONNECTOR
        :type SystemProvide: int
        """
        self._ResourceId = None
        self._Name = None
        self._ResourceType = None
        self._Remark = None
        self._Region = None
        self._LatestResourceConfigVersion = None
        self._SystemProvide = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Name(self):
        """资源名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ResourceType(self):
        """资源类型。1 表示 JAR 包，目前只支持该值。
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Remark(self):
        """资源备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Region(self):
        """资源所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def LatestResourceConfigVersion(self):
        """资源的最新版本
        :rtype: int
        """
        return self._LatestResourceConfigVersion

    @LatestResourceConfigVersion.setter
    def LatestResourceConfigVersion(self, LatestResourceConfigVersion):
        self._LatestResourceConfigVersion = LatestResourceConfigVersion

    @property
    def SystemProvide(self):
        """1 是系统提供资源 2 用户提供CONNECTOR
        :rtype: int
        """
        return self._SystemProvide

    @SystemProvide.setter
    def SystemProvide(self, SystemProvide):
        self._SystemProvide = SystemProvide


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Name = params.get("Name")
        self._ResourceType = params.get("ResourceType")
        self._Remark = params.get("Remark")
        self._Region = params.get("Region")
        self._LatestResourceConfigVersion = params.get("LatestResourceConfigVersion")
        self._SystemProvide = params.get("SystemProvide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

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
        """标签键
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class TraceModeConfiguration(AbstractModel):
    """{
      "Rate": "0.01",  ///如1%转换为0.01
      "Operator":  "1:OUT,2:IN_AND_OUT,3:IN"  ///如1%转换为0.01
    }
    Operator
    算子ID顺序配置，可以对每个算子配置IN、OUT、IN_AND_OUT三个值，分别表示采集输入数据、采集输出数据、同时采集输入和输出数据，配置示例:

    """

    def __init__(self):
        r"""
        :param _Rate: 如1%转换为0.01
注意：此字段可能返回 null，表示取不到有效值。
        :type Rate: str
        :param _Operator: 按照算子ID顺序配置，可以对每个算子配置IN、OUT、IN_AND_OUT三个值，分别表示采集输入数据、采集输出数据、同时采集输入和输出数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        """
        self._Rate = None
        self._Operator = None

    @property
    def Rate(self):
        """如1%转换为0.01
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Operator(self):
        """按照算子ID顺序配置，可以对每个算子配置IN、OUT、IN_AND_OUT三个值，分别表示采集输入数据、采集输出数据、同时采集输入和输出数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._Rate = params.get("Rate")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TreeJobSets(AbstractModel):
    """自定义树结构出参作业列表

    """

    def __init__(self):
        r"""
        :param _JobId: 作业Id
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _Name: 作业名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _JobType: 作业类型
注意：此字段可能返回 null，表示取不到有效值。
        :type JobType: int
        :param _RunningCu: 作业占用资源
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningCu: float
        :param _Status: 作业状态 启动或者停止或者暂停
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ScalingType: 0:代表没开启调优任务，1:开启智能调优，2:代表定时调优

注意：此字段可能返回 null，表示取不到有效值。
        :type ScalingType: int
        :param _RunningCpu: RunningCpu
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningCpu: float
        :param _RunningMem: RunningMem
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningMem: float
        :param _DecodeSqlCode: sql
注意：此字段可能返回 null，表示取不到有效值。
        :type DecodeSqlCode: str
        """
        self._JobId = None
        self._Name = None
        self._JobType = None
        self._RunningCu = None
        self._Status = None
        self._ScalingType = None
        self._RunningCpu = None
        self._RunningMem = None
        self._DecodeSqlCode = None

    @property
    def JobId(self):
        """作业Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Name(self):
        """作业名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def JobType(self):
        """作业类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def RunningCu(self):
        """作业占用资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RunningCu

    @RunningCu.setter
    def RunningCu(self, RunningCu):
        self._RunningCu = RunningCu

    @property
    def Status(self):
        """作业状态 启动或者停止或者暂停
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ScalingType(self):
        """0:代表没开启调优任务，1:开启智能调优，2:代表定时调优

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ScalingType

    @ScalingType.setter
    def ScalingType(self, ScalingType):
        self._ScalingType = ScalingType

    @property
    def RunningCpu(self):
        """RunningCpu
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RunningCpu

    @RunningCpu.setter
    def RunningCpu(self, RunningCpu):
        self._RunningCpu = RunningCpu

    @property
    def RunningMem(self):
        """RunningMem
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RunningMem

    @RunningMem.setter
    def RunningMem(self, RunningMem):
        self._RunningMem = RunningMem

    @property
    def DecodeSqlCode(self):
        """sql
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DecodeSqlCode

    @DecodeSqlCode.setter
    def DecodeSqlCode(self, DecodeSqlCode):
        self._DecodeSqlCode = DecodeSqlCode


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Name = params.get("Name")
        self._JobType = params.get("JobType")
        self._RunningCu = params.get("RunningCu")
        self._Status = params.get("Status")
        self._ScalingType = params.get("ScalingType")
        self._RunningCpu = params.get("RunningCpu")
        self._RunningMem = params.get("RunningMem")
        self._DecodeSqlCode = params.get("DecodeSqlCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TreeResourceItem(AbstractModel):
    """树状结构资源对象

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _Name: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ResourceType: 资源类型
        :type ResourceType: int
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _FileName: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FolderId: 目录ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FolderId: str
        :param _RefJobStatusCountSet: 分状态统计关联作业数
注意：此字段可能返回 null，表示取不到有效值。
        :type RefJobStatusCountSet: list of RefJobStatusCountItem
        """
        self._ResourceId = None
        self._Name = None
        self._ResourceType = None
        self._Remark = None
        self._FileName = None
        self._FolderId = None
        self._RefJobStatusCountSet = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Name(self):
        """资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ResourceType(self):
        """资源类型
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Remark(self):
        """备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def FileName(self):
        """文件名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FolderId(self):
        """目录ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FolderId

    @FolderId.setter
    def FolderId(self, FolderId):
        self._FolderId = FolderId

    @property
    def RefJobStatusCountSet(self):
        """分状态统计关联作业数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RefJobStatusCountItem
        """
        return self._RefJobStatusCountSet

    @RefJobStatusCountSet.setter
    def RefJobStatusCountSet(self, RefJobStatusCountSet):
        self._RefJobStatusCountSet = RefJobStatusCountSet


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Name = params.get("Name")
        self._ResourceType = params.get("ResourceType")
        self._Remark = params.get("Remark")
        self._FileName = params.get("FileName")
        self._FolderId = params.get("FolderId")
        if params.get("RefJobStatusCountSet") is not None:
            self._RefJobStatusCountSet = []
            for item in params.get("RefJobStatusCountSet"):
                obj = RefJobStatusCountItem()
                obj._deserialize(item)
                self._RefJobStatusCountSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerJobSavepointRequest(AbstractModel):
    """TriggerJobSavepoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 作业 SerialId
        :type JobId: str
        :param _Description: 描述
        :type Description: str
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        """
        self._JobId = None
        self._Description = None
        self._WorkSpaceId = None

    @property
    def JobId(self):
        """作业 SerialId
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Description = params.get("Description")
        self._WorkSpaceId = params.get("WorkSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerJobSavepointResponse(AbstractModel):
    """TriggerJobSavepoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SavepointTrigger: 是否成功
        :type SavepointTrigger: bool
        :param _ErrorMsg: 错误消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _FinalSavepointPath: 快照路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalSavepointPath: str
        :param _SavepointId: 快照 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SavepointId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SavepointTrigger = None
        self._ErrorMsg = None
        self._FinalSavepointPath = None
        self._SavepointId = None
        self._RequestId = None

    @property
    def SavepointTrigger(self):
        """是否成功
        :rtype: bool
        """
        return self._SavepointTrigger

    @SavepointTrigger.setter
    def SavepointTrigger(self, SavepointTrigger):
        self._SavepointTrigger = SavepointTrigger

    @property
    def ErrorMsg(self):
        """错误消息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def FinalSavepointPath(self):
        """快照路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FinalSavepointPath

    @FinalSavepointPath.setter
    def FinalSavepointPath(self, FinalSavepointPath):
        self._FinalSavepointPath = FinalSavepointPath

    @property
    def SavepointId(self):
        """快照 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SavepointId

    @SavepointId.setter
    def SavepointId(self, SavepointId):
        self._SavepointId = SavepointId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SavepointTrigger = params.get("SavepointTrigger")
        self._ErrorMsg = params.get("ErrorMsg")
        self._FinalSavepointPath = params.get("FinalSavepointPath")
        self._SavepointId = params.get("SavepointId")
        self._RequestId = params.get("RequestId")


class Warehouse(AbstractModel):
    """Setats Warehouse结构

    """

    def __init__(self):
        r"""
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Location: location
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param _CatalogType: catalogtype
注意：此字段可能返回 null，表示取不到有效值。
        :type CatalogType: str
        :param _Uri: uri
注意：此字段可能返回 null，表示取不到有效值。
        :type Uri: str
        :param _WarehouseUrl: warehouse url
注意：此字段可能返回 null，表示取不到有效值。
        :type WarehouseUrl: str
        :param _Authentication: 认证方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Authentication: str
        :param _ResourceRefs: 资源
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRefs: list of ResourceRefLatest
        :param _HiveUri: hive warehouse uri
注意：此字段可能返回 null，表示取不到有效值。
        :type HiveUri: str
        :param _Properties: 高级参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: list of Property
        """
        self._Status = None
        self._Location = None
        self._CatalogType = None
        self._Uri = None
        self._WarehouseUrl = None
        self._Authentication = None
        self._ResourceRefs = None
        self._HiveUri = None
        self._Properties = None

    @property
    def Status(self):
        """状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Location(self):
        """location
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def CatalogType(self):
        """catalogtype
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CatalogType

    @CatalogType.setter
    def CatalogType(self, CatalogType):
        self._CatalogType = CatalogType

    @property
    def Uri(self):
        """uri
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def WarehouseUrl(self):
        """warehouse url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WarehouseUrl

    @WarehouseUrl.setter
    def WarehouseUrl(self, WarehouseUrl):
        self._WarehouseUrl = WarehouseUrl

    @property
    def Authentication(self):
        """认证方式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def ResourceRefs(self):
        """资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceRefLatest
        """
        return self._ResourceRefs

    @ResourceRefs.setter
    def ResourceRefs(self, ResourceRefs):
        self._ResourceRefs = ResourceRefs

    @property
    def HiveUri(self):
        """hive warehouse uri
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HiveUri

    @HiveUri.setter
    def HiveUri(self, HiveUri):
        self._HiveUri = HiveUri

    @property
    def Properties(self):
        """高级参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Property
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Location = params.get("Location")
        self._CatalogType = params.get("CatalogType")
        self._Uri = params.get("Uri")
        self._WarehouseUrl = params.get("WarehouseUrl")
        self._Authentication = params.get("Authentication")
        if params.get("ResourceRefs") is not None:
            self._ResourceRefs = []
            for item in params.get("ResourceRefs"):
                obj = ResourceRefLatest()
                obj._deserialize(item)
                self._ResourceRefs.append(obj)
        self._HiveUri = params.get("HiveUri")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = Property()
                obj._deserialize(item)
                self._Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkSpaceClusterItem(AbstractModel):
    """空间和集群绑定关系

    """

    def __init__(self):
        r"""
        :param _ClusterGroupId: 集群 ID
        :type ClusterGroupId: int
        :param _ClusterGroupSerialId: 集群 SerialId
        :type ClusterGroupSerialId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _WorkSpaceName: 工作空间名称
        :type WorkSpaceName: str
        :param _Status: 绑定状态  2 绑定 1  解除绑定
        :type Status: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ProjectIdStr: 项目ID string类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectIdStr: str
        """
        self._ClusterGroupId = None
        self._ClusterGroupSerialId = None
        self._ClusterName = None
        self._WorkSpaceId = None
        self._WorkSpaceName = None
        self._Status = None
        self._ProjectId = None
        self._ProjectIdStr = None

    @property
    def ClusterGroupId(self):
        """集群 ID
        :rtype: int
        """
        return self._ClusterGroupId

    @ClusterGroupId.setter
    def ClusterGroupId(self, ClusterGroupId):
        self._ClusterGroupId = ClusterGroupId

    @property
    def ClusterGroupSerialId(self):
        """集群 SerialId
        :rtype: str
        """
        return self._ClusterGroupSerialId

    @ClusterGroupSerialId.setter
    def ClusterGroupSerialId(self, ClusterGroupSerialId):
        self._ClusterGroupSerialId = ClusterGroupSerialId

    @property
    def ClusterName(self):
        """集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def WorkSpaceName(self):
        """工作空间名称
        :rtype: str
        """
        return self._WorkSpaceName

    @WorkSpaceName.setter
    def WorkSpaceName(self, WorkSpaceName):
        self._WorkSpaceName = WorkSpaceName

    @property
    def Status(self):
        """绑定状态  2 绑定 1  解除绑定
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectIdStr(self):
        """项目ID string类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectIdStr

    @ProjectIdStr.setter
    def ProjectIdStr(self, ProjectIdStr):
        self._ProjectIdStr = ProjectIdStr


    def _deserialize(self, params):
        self._ClusterGroupId = params.get("ClusterGroupId")
        self._ClusterGroupSerialId = params.get("ClusterGroupSerialId")
        self._ClusterName = params.get("ClusterName")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._WorkSpaceName = params.get("WorkSpaceName")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        self._ProjectIdStr = params.get("ProjectIdStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkSpaceSetItem(AbstractModel):
    """工作空间详情

    """

    def __init__(self):
        r"""
        :param _SerialId: 工作空间 SerialId
        :type SerialId: str
        :param _AppId: 用户 APPID
        :type AppId: int
        :param _OwnerUin: 主账号 UIN
        :type OwnerUin: str
        :param _CreatorUin: 创建者 UIN
        :type CreatorUin: str
        :param _WorkSpaceName: 工作空间名称
        :type WorkSpaceName: str
        :param _Region: 区域
        :type Region: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Status: 1 未初始化 2 可用  -1 已删除
        :type Status: int
        :param _Description: 工作空间描述
        :type Description: str
        :param _ClusterGroupSetItem: 工作空间包含集群信息
        :type ClusterGroupSetItem: list of ClusterGroupSetItem
        :param _RoleAuth: 工作空间角色的信息
        :type RoleAuth: list of RoleAuth
        :param _RoleAuthCount: 工作空间成员数量
        :type RoleAuthCount: int
        :param _WorkSpaceId: 工作空间 SerialId
        :type WorkSpaceId: str
        :param _JobsCount: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type JobsCount: int
        """
        self._SerialId = None
        self._AppId = None
        self._OwnerUin = None
        self._CreatorUin = None
        self._WorkSpaceName = None
        self._Region = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Status = None
        self._Description = None
        self._ClusterGroupSetItem = None
        self._RoleAuth = None
        self._RoleAuthCount = None
        self._WorkSpaceId = None
        self._JobsCount = None

    @property
    def SerialId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._SerialId

    @SerialId.setter
    def SerialId(self, SerialId):
        self._SerialId = SerialId

    @property
    def AppId(self):
        """用户 APPID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def OwnerUin(self):
        """主账号 UIN
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreatorUin(self):
        """创建者 UIN
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def WorkSpaceName(self):
        """工作空间名称
        :rtype: str
        """
        return self._WorkSpaceName

    @WorkSpaceName.setter
    def WorkSpaceName(self, WorkSpaceName):
        self._WorkSpaceName = WorkSpaceName

    @property
    def Region(self):
        """区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """1 未初始化 2 可用  -1 已删除
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        """工作空间描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClusterGroupSetItem(self):
        """工作空间包含集群信息
        :rtype: list of ClusterGroupSetItem
        """
        return self._ClusterGroupSetItem

    @ClusterGroupSetItem.setter
    def ClusterGroupSetItem(self, ClusterGroupSetItem):
        self._ClusterGroupSetItem = ClusterGroupSetItem

    @property
    def RoleAuth(self):
        """工作空间角色的信息
        :rtype: list of RoleAuth
        """
        return self._RoleAuth

    @RoleAuth.setter
    def RoleAuth(self, RoleAuth):
        self._RoleAuth = RoleAuth

    @property
    def RoleAuthCount(self):
        """工作空间成员数量
        :rtype: int
        """
        return self._RoleAuthCount

    @RoleAuthCount.setter
    def RoleAuthCount(self, RoleAuthCount):
        self._RoleAuthCount = RoleAuthCount

    @property
    def WorkSpaceId(self):
        """工作空间 SerialId
        :rtype: str
        """
        return self._WorkSpaceId

    @WorkSpaceId.setter
    def WorkSpaceId(self, WorkSpaceId):
        self._WorkSpaceId = WorkSpaceId

    @property
    def JobsCount(self):
        """1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._JobsCount

    @JobsCount.setter
    def JobsCount(self, JobsCount):
        self._JobsCount = JobsCount


    def _deserialize(self, params):
        self._SerialId = params.get("SerialId")
        self._AppId = params.get("AppId")
        self._OwnerUin = params.get("OwnerUin")
        self._CreatorUin = params.get("CreatorUin")
        self._WorkSpaceName = params.get("WorkSpaceName")
        self._Region = params.get("Region")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        if params.get("ClusterGroupSetItem") is not None:
            self._ClusterGroupSetItem = []
            for item in params.get("ClusterGroupSetItem"):
                obj = ClusterGroupSetItem()
                obj._deserialize(item)
                self._ClusterGroupSetItem.append(obj)
        if params.get("RoleAuth") is not None:
            self._RoleAuth = []
            for item in params.get("RoleAuth"):
                obj = RoleAuth()
                obj._deserialize(item)
                self._RoleAuth.append(obj)
        self._RoleAuthCount = params.get("RoleAuthCount")
        self._WorkSpaceId = params.get("WorkSpaceId")
        self._JobsCount = params.get("JobsCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        