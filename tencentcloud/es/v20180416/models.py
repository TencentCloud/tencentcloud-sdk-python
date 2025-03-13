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


class BackingIndexMetaField(AbstractModel):
    """后备索引元数据字段

    """

    def __init__(self):
        r"""
        :param _IndexName: 后备索引名
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexName: str
        :param _IndexStatus: 后备索引状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStatus: str
        :param _IndexStorage: 后备索引存储大小
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStorage: int
        :param _IndexPhrase: 后备索引当前生命周期
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexPhrase: str
        :param _IndexCreateTime: 后备索引创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexCreateTime: str
        """
        self._IndexName = None
        self._IndexStatus = None
        self._IndexStorage = None
        self._IndexPhrase = None
        self._IndexCreateTime = None

    @property
    def IndexName(self):
        """后备索引名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IndexStatus(self):
        """后备索引状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus

    @property
    def IndexStorage(self):
        """后备索引存储大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IndexStorage

    @IndexStorage.setter
    def IndexStorage(self, IndexStorage):
        self._IndexStorage = IndexStorage

    @property
    def IndexPhrase(self):
        """后备索引当前生命周期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexPhrase

    @IndexPhrase.setter
    def IndexPhrase(self, IndexPhrase):
        self._IndexPhrase = IndexPhrase

    @property
    def IndexCreateTime(self):
        """后备索引创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexCreateTime

    @IndexCreateTime.setter
    def IndexCreateTime(self, IndexCreateTime):
        self._IndexCreateTime = IndexCreateTime


    def _deserialize(self, params):
        self._IndexName = params.get("IndexName")
        self._IndexStatus = params.get("IndexStatus")
        self._IndexStorage = params.get("IndexStorage")
        self._IndexPhrase = params.get("IndexPhrase")
        self._IndexCreateTime = params.get("IndexCreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckMigrateIndexMetaDataRequest(AbstractModel):
    """CheckMigrateIndexMetaData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerlessId: 索引 id
        :type ServerlessId: str
        :param _Snapshot: 快照名
        :type Snapshot: str
        :param _CosBucket: Cos桶名
        :type CosBucket: str
        :param _BasePath: BasePath路径
        :type BasePath: str
        :param _ClusterInstanceId: 云上集群名
        :type ClusterInstanceId: str
        :param _CommonIndexArr: 普通索引名列表
        :type CommonIndexArr: list of str
        :param _DataStreamArr: 自治索引名列表
        :type DataStreamArr: list of str
        """
        self._ServerlessId = None
        self._Snapshot = None
        self._CosBucket = None
        self._BasePath = None
        self._ClusterInstanceId = None
        self._CommonIndexArr = None
        self._DataStreamArr = None

    @property
    def ServerlessId(self):
        """索引 id
        :rtype: str
        """
        return self._ServerlessId

    @ServerlessId.setter
    def ServerlessId(self, ServerlessId):
        self._ServerlessId = ServerlessId

    @property
    def Snapshot(self):
        """快照名
        :rtype: str
        """
        return self._Snapshot

    @Snapshot.setter
    def Snapshot(self, Snapshot):
        self._Snapshot = Snapshot

    @property
    def CosBucket(self):
        """Cos桶名
        :rtype: str
        """
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def BasePath(self):
        """BasePath路径
        :rtype: str
        """
        return self._BasePath

    @BasePath.setter
    def BasePath(self, BasePath):
        self._BasePath = BasePath

    @property
    def ClusterInstanceId(self):
        """云上集群名
        :rtype: str
        """
        return self._ClusterInstanceId

    @ClusterInstanceId.setter
    def ClusterInstanceId(self, ClusterInstanceId):
        self._ClusterInstanceId = ClusterInstanceId

    @property
    def CommonIndexArr(self):
        """普通索引名列表
        :rtype: list of str
        """
        return self._CommonIndexArr

    @CommonIndexArr.setter
    def CommonIndexArr(self, CommonIndexArr):
        self._CommonIndexArr = CommonIndexArr

    @property
    def DataStreamArr(self):
        """自治索引名列表
        :rtype: list of str
        """
        return self._DataStreamArr

    @DataStreamArr.setter
    def DataStreamArr(self, DataStreamArr):
        self._DataStreamArr = DataStreamArr


    def _deserialize(self, params):
        self._ServerlessId = params.get("ServerlessId")
        self._Snapshot = params.get("Snapshot")
        self._CosBucket = params.get("CosBucket")
        self._BasePath = params.get("BasePath")
        self._ClusterInstanceId = params.get("ClusterInstanceId")
        self._CommonIndexArr = params.get("CommonIndexArr")
        self._DataStreamArr = params.get("DataStreamArr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckMigrateIndexMetaDataResponse(AbstractModel):
    """CheckMigrateIndexMetaData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MappingTimeFieldCheckFailedIndexArr: 不存在于目标索引时间字段相同的字段
        :type MappingTimeFieldCheckFailedIndexArr: list of str
        :param _MappingTimeTypeCheckFailedIndexArr: @timestamp不为date类型，与目标索引时间字段冲突
        :type MappingTimeTypeCheckFailedIndexArr: list of str
        :param _SettingCheckFailedIndexArr: 索引的创建时间不在 serverless的存储周期内
        :type SettingCheckFailedIndexArr: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MappingTimeFieldCheckFailedIndexArr = None
        self._MappingTimeTypeCheckFailedIndexArr = None
        self._SettingCheckFailedIndexArr = None
        self._RequestId = None

    @property
    def MappingTimeFieldCheckFailedIndexArr(self):
        """不存在于目标索引时间字段相同的字段
        :rtype: list of str
        """
        return self._MappingTimeFieldCheckFailedIndexArr

    @MappingTimeFieldCheckFailedIndexArr.setter
    def MappingTimeFieldCheckFailedIndexArr(self, MappingTimeFieldCheckFailedIndexArr):
        self._MappingTimeFieldCheckFailedIndexArr = MappingTimeFieldCheckFailedIndexArr

    @property
    def MappingTimeTypeCheckFailedIndexArr(self):
        """@timestamp不为date类型，与目标索引时间字段冲突
        :rtype: list of str
        """
        return self._MappingTimeTypeCheckFailedIndexArr

    @MappingTimeTypeCheckFailedIndexArr.setter
    def MappingTimeTypeCheckFailedIndexArr(self, MappingTimeTypeCheckFailedIndexArr):
        self._MappingTimeTypeCheckFailedIndexArr = MappingTimeTypeCheckFailedIndexArr

    @property
    def SettingCheckFailedIndexArr(self):
        """索引的创建时间不在 serverless的存储周期内
        :rtype: list of str
        """
        return self._SettingCheckFailedIndexArr

    @SettingCheckFailedIndexArr.setter
    def SettingCheckFailedIndexArr(self, SettingCheckFailedIndexArr):
        self._SettingCheckFailedIndexArr = SettingCheckFailedIndexArr

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
        self._MappingTimeFieldCheckFailedIndexArr = params.get("MappingTimeFieldCheckFailedIndexArr")
        self._MappingTimeTypeCheckFailedIndexArr = params.get("MappingTimeTypeCheckFailedIndexArr")
        self._SettingCheckFailedIndexArr = params.get("SettingCheckFailedIndexArr")
        self._RequestId = params.get("RequestId")


class ClusterView(AbstractModel):
    """集群维度视图数据

    """

    def __init__(self):
        r"""
        :param _Health: 集群健康状态
        :type Health: float
        :param _Visible: 集群是否可见
        :type Visible: float
        :param _Break: 集群是否熔断
        :type Break: float
        :param _AvgDiskUsage: 平均磁盘使用率
        :type AvgDiskUsage: float
        :param _AvgMemUsage: 平均内存使用率
        :type AvgMemUsage: float
        :param _AvgCpuUsage: 平均cpu使用率
        :type AvgCpuUsage: float
        :param _TotalDiskSize: 集群总存储大小
        :type TotalDiskSize: int
        :param _TargetNodeTypes: 客户端请求节点
        :type TargetNodeTypes: list of str
        :param _NodeNum: 在线节点数
        :type NodeNum: int
        :param _TotalNodeNum: 总节点数
        :type TotalNodeNum: int
        :param _DataNodeNum: 数据节点数
        :type DataNodeNum: int
        :param _IndexNum: 索引数
        :type IndexNum: int
        :param _DocNum: 文档数
        :type DocNum: int
        :param _DiskUsedInBytes: 磁盘已使用字节数
        :type DiskUsedInBytes: int
        :param _ShardNum: 分片个数
        :type ShardNum: int
        :param _PrimaryShardNum: 主分片个数
        :type PrimaryShardNum: int
        :param _RelocatingShardNum: 迁移中的分片个数
        :type RelocatingShardNum: int
        :param _InitializingShardNum: 初始化中的分片个数
        :type InitializingShardNum: int
        :param _UnassignedShardNum: 未分配的分片个数
        :type UnassignedShardNum: int
        :param _TotalCosStorage: 企业版COS存储容量大小，单位GB
        :type TotalCosStorage: int
        :param _SearchableSnapshotCosBucket: 企业版集群可搜索快照cos存放的bucket名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchableSnapshotCosBucket: str
        :param _SearchableSnapshotCosAppId: 企业版集群可搜索快照cos所属appid
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchableSnapshotCosAppId: str
        """
        self._Health = None
        self._Visible = None
        self._Break = None
        self._AvgDiskUsage = None
        self._AvgMemUsage = None
        self._AvgCpuUsage = None
        self._TotalDiskSize = None
        self._TargetNodeTypes = None
        self._NodeNum = None
        self._TotalNodeNum = None
        self._DataNodeNum = None
        self._IndexNum = None
        self._DocNum = None
        self._DiskUsedInBytes = None
        self._ShardNum = None
        self._PrimaryShardNum = None
        self._RelocatingShardNum = None
        self._InitializingShardNum = None
        self._UnassignedShardNum = None
        self._TotalCosStorage = None
        self._SearchableSnapshotCosBucket = None
        self._SearchableSnapshotCosAppId = None

    @property
    def Health(self):
        """集群健康状态
        :rtype: float
        """
        return self._Health

    @Health.setter
    def Health(self, Health):
        self._Health = Health

    @property
    def Visible(self):
        """集群是否可见
        :rtype: float
        """
        return self._Visible

    @Visible.setter
    def Visible(self, Visible):
        self._Visible = Visible

    @property
    def Break(self):
        """集群是否熔断
        :rtype: float
        """
        return self._Break

    @Break.setter
    def Break(self, Break):
        self._Break = Break

    @property
    def AvgDiskUsage(self):
        """平均磁盘使用率
        :rtype: float
        """
        return self._AvgDiskUsage

    @AvgDiskUsage.setter
    def AvgDiskUsage(self, AvgDiskUsage):
        self._AvgDiskUsage = AvgDiskUsage

    @property
    def AvgMemUsage(self):
        """平均内存使用率
        :rtype: float
        """
        return self._AvgMemUsage

    @AvgMemUsage.setter
    def AvgMemUsage(self, AvgMemUsage):
        self._AvgMemUsage = AvgMemUsage

    @property
    def AvgCpuUsage(self):
        """平均cpu使用率
        :rtype: float
        """
        return self._AvgCpuUsage

    @AvgCpuUsage.setter
    def AvgCpuUsage(self, AvgCpuUsage):
        self._AvgCpuUsage = AvgCpuUsage

    @property
    def TotalDiskSize(self):
        """集群总存储大小
        :rtype: int
        """
        return self._TotalDiskSize

    @TotalDiskSize.setter
    def TotalDiskSize(self, TotalDiskSize):
        self._TotalDiskSize = TotalDiskSize

    @property
    def TargetNodeTypes(self):
        """客户端请求节点
        :rtype: list of str
        """
        return self._TargetNodeTypes

    @TargetNodeTypes.setter
    def TargetNodeTypes(self, TargetNodeTypes):
        self._TargetNodeTypes = TargetNodeTypes

    @property
    def NodeNum(self):
        """在线节点数
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def TotalNodeNum(self):
        """总节点数
        :rtype: int
        """
        return self._TotalNodeNum

    @TotalNodeNum.setter
    def TotalNodeNum(self, TotalNodeNum):
        self._TotalNodeNum = TotalNodeNum

    @property
    def DataNodeNum(self):
        """数据节点数
        :rtype: int
        """
        return self._DataNodeNum

    @DataNodeNum.setter
    def DataNodeNum(self, DataNodeNum):
        self._DataNodeNum = DataNodeNum

    @property
    def IndexNum(self):
        """索引数
        :rtype: int
        """
        return self._IndexNum

    @IndexNum.setter
    def IndexNum(self, IndexNum):
        self._IndexNum = IndexNum

    @property
    def DocNum(self):
        """文档数
        :rtype: int
        """
        return self._DocNum

    @DocNum.setter
    def DocNum(self, DocNum):
        self._DocNum = DocNum

    @property
    def DiskUsedInBytes(self):
        """磁盘已使用字节数
        :rtype: int
        """
        return self._DiskUsedInBytes

    @DiskUsedInBytes.setter
    def DiskUsedInBytes(self, DiskUsedInBytes):
        self._DiskUsedInBytes = DiskUsedInBytes

    @property
    def ShardNum(self):
        """分片个数
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def PrimaryShardNum(self):
        """主分片个数
        :rtype: int
        """
        return self._PrimaryShardNum

    @PrimaryShardNum.setter
    def PrimaryShardNum(self, PrimaryShardNum):
        self._PrimaryShardNum = PrimaryShardNum

    @property
    def RelocatingShardNum(self):
        """迁移中的分片个数
        :rtype: int
        """
        return self._RelocatingShardNum

    @RelocatingShardNum.setter
    def RelocatingShardNum(self, RelocatingShardNum):
        self._RelocatingShardNum = RelocatingShardNum

    @property
    def InitializingShardNum(self):
        """初始化中的分片个数
        :rtype: int
        """
        return self._InitializingShardNum

    @InitializingShardNum.setter
    def InitializingShardNum(self, InitializingShardNum):
        self._InitializingShardNum = InitializingShardNum

    @property
    def UnassignedShardNum(self):
        """未分配的分片个数
        :rtype: int
        """
        return self._UnassignedShardNum

    @UnassignedShardNum.setter
    def UnassignedShardNum(self, UnassignedShardNum):
        self._UnassignedShardNum = UnassignedShardNum

    @property
    def TotalCosStorage(self):
        """企业版COS存储容量大小，单位GB
        :rtype: int
        """
        return self._TotalCosStorage

    @TotalCosStorage.setter
    def TotalCosStorage(self, TotalCosStorage):
        self._TotalCosStorage = TotalCosStorage

    @property
    def SearchableSnapshotCosBucket(self):
        """企业版集群可搜索快照cos存放的bucket名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SearchableSnapshotCosBucket

    @SearchableSnapshotCosBucket.setter
    def SearchableSnapshotCosBucket(self, SearchableSnapshotCosBucket):
        self._SearchableSnapshotCosBucket = SearchableSnapshotCosBucket

    @property
    def SearchableSnapshotCosAppId(self):
        """企业版集群可搜索快照cos所属appid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SearchableSnapshotCosAppId

    @SearchableSnapshotCosAppId.setter
    def SearchableSnapshotCosAppId(self, SearchableSnapshotCosAppId):
        self._SearchableSnapshotCosAppId = SearchableSnapshotCosAppId


    def _deserialize(self, params):
        self._Health = params.get("Health")
        self._Visible = params.get("Visible")
        self._Break = params.get("Break")
        self._AvgDiskUsage = params.get("AvgDiskUsage")
        self._AvgMemUsage = params.get("AvgMemUsage")
        self._AvgCpuUsage = params.get("AvgCpuUsage")
        self._TotalDiskSize = params.get("TotalDiskSize")
        self._TargetNodeTypes = params.get("TargetNodeTypes")
        self._NodeNum = params.get("NodeNum")
        self._TotalNodeNum = params.get("TotalNodeNum")
        self._DataNodeNum = params.get("DataNodeNum")
        self._IndexNum = params.get("IndexNum")
        self._DocNum = params.get("DocNum")
        self._DiskUsedInBytes = params.get("DiskUsedInBytes")
        self._ShardNum = params.get("ShardNum")
        self._PrimaryShardNum = params.get("PrimaryShardNum")
        self._RelocatingShardNum = params.get("RelocatingShardNum")
        self._InitializingShardNum = params.get("InitializingShardNum")
        self._UnassignedShardNum = params.get("UnassignedShardNum")
        self._TotalCosStorage = params.get("TotalCosStorage")
        self._SearchableSnapshotCosBucket = params.get("SearchableSnapshotCosBucket")
        self._SearchableSnapshotCosAppId = params.get("SearchableSnapshotCosAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonIndexInfo(AbstractModel):
    """普通索引信息列表

    """

    def __init__(self):
        r"""
        :param _IndexName: 普通索引名
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexName: str
        :param _IsShardComplete: 分片状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IsShardComplete: int
        """
        self._IndexName = None
        self._IsShardComplete = None

    @property
    def IndexName(self):
        """普通索引名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IsShardComplete(self):
        """分片状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsShardComplete

    @IsShardComplete.setter
    def IsShardComplete(self, IsShardComplete):
        self._IsShardComplete = IsShardComplete


    def _deserialize(self, params):
        self._IndexName = params.get("IndexName")
        self._IsShardComplete = params.get("IsShardComplete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosBackup(AbstractModel):
    """ES cos自动备份信息

    """

    def __init__(self):
        r"""
        :param _IsAutoBackup: 是否开启cos自动备份
        :type IsAutoBackup: bool
        :param _BackupTime: 自动备份执行时间（精确到小时）, e.g. "22:00"
        :type BackupTime: str
        """
        self._IsAutoBackup = None
        self._BackupTime = None

    @property
    def IsAutoBackup(self):
        """是否开启cos自动备份
        :rtype: bool
        """
        return self._IsAutoBackup

    @IsAutoBackup.setter
    def IsAutoBackup(self, IsAutoBackup):
        self._IsAutoBackup = IsAutoBackup

    @property
    def BackupTime(self):
        """自动备份执行时间（精确到小时）, e.g. "22:00"
        :rtype: str
        """
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime


    def _deserialize(self, params):
        self._IsAutoBackup = params.get("IsAutoBackup")
        self._BackupTime = params.get("BackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosSnapShotInfo(AbstractModel):
    """无

    """

    def __init__(self):
        r"""
        :param _CosBucket: cos 桶名
注意：此字段可能返回 null，表示取不到有效值。
        :type CosBucket: str
        :param _BasePath: base path
注意：此字段可能返回 null，表示取不到有效值。
        :type BasePath: str
        :param _SnapshotName: 快照名
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotName: str
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _Version: 快照版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _CommonIndexArr: 普通索引信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonIndexArr: list of CommonIndexInfo
        :param _DataStreamArr: 自治索引信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DataStreamArr: list of DataStreamInfo
        """
        self._CosBucket = None
        self._BasePath = None
        self._SnapshotName = None
        self._State = None
        self._Version = None
        self._CommonIndexArr = None
        self._DataStreamArr = None

    @property
    def CosBucket(self):
        """cos 桶名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def BasePath(self):
        """base path
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BasePath

    @BasePath.setter
    def BasePath(self, BasePath):
        self._BasePath = BasePath

    @property
    def SnapshotName(self):
        """快照名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def State(self):
        """状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Version(self):
        """快照版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def CommonIndexArr(self):
        """普通索引信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CommonIndexInfo
        """
        return self._CommonIndexArr

    @CommonIndexArr.setter
    def CommonIndexArr(self, CommonIndexArr):
        self._CommonIndexArr = CommonIndexArr

    @property
    def DataStreamArr(self):
        """自治索引信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DataStreamInfo
        """
        return self._DataStreamArr

    @DataStreamArr.setter
    def DataStreamArr(self, DataStreamArr):
        self._DataStreamArr = DataStreamArr


    def _deserialize(self, params):
        self._CosBucket = params.get("CosBucket")
        self._BasePath = params.get("BasePath")
        self._SnapshotName = params.get("SnapshotName")
        self._State = params.get("State")
        self._Version = params.get("Version")
        if params.get("CommonIndexArr") is not None:
            self._CommonIndexArr = []
            for item in params.get("CommonIndexArr"):
                obj = CommonIndexInfo()
                obj._deserialize(item)
                self._CommonIndexArr.append(obj)
        if params.get("DataStreamArr") is not None:
            self._DataStreamArr = []
            for item in params.get("DataStreamArr"):
                obj = DataStreamInfo()
                obj._deserialize(item)
                self._DataStreamArr.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterSnapshotRequest(AbstractModel):
    """CreateClusterSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名称
        :type InstanceId: str
        :param _SnapshotName: 快照名称
        :type SnapshotName: str
        :param _Indices: 索引名称
        :type Indices: str
        """
        self._InstanceId = None
        self._SnapshotName = None
        self._Indices = None

    @property
    def InstanceId(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SnapshotName(self):
        """快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Indices(self):
        """索引名称
        :rtype: str
        """
        return self._Indices

    @Indices.setter
    def Indices(self, Indices):
        self._Indices = Indices


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SnapshotName = params.get("SnapshotName")
        self._Indices = params.get("Indices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterSnapshotResponse(AbstractModel):
    """CreateClusterSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateCosMigrateToServerlessInstanceRequest(AbstractModel):
    """CreateCosMigrateToServerlessInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Snapshot: 快照名
        :type Snapshot: str
        :param _ServerlessId: 索引 id
        :type ServerlessId: str
        :param _CosBucket: cos 桶名
        :type CosBucket: str
        :param _BasePath: BasePath 路径
        :type BasePath: str
        :param _ClusterInstanceId: 云上集群 id
        :type ClusterInstanceId: str
        :param _CommonIndexArr: 待迁移普通索引名列表
        :type CommonIndexArr: list of str
        :param _DataStreamArr: 待迁移自治索引名列表
        :type DataStreamArr: list of str
        """
        self._Snapshot = None
        self._ServerlessId = None
        self._CosBucket = None
        self._BasePath = None
        self._ClusterInstanceId = None
        self._CommonIndexArr = None
        self._DataStreamArr = None

    @property
    def Snapshot(self):
        """快照名
        :rtype: str
        """
        return self._Snapshot

    @Snapshot.setter
    def Snapshot(self, Snapshot):
        self._Snapshot = Snapshot

    @property
    def ServerlessId(self):
        """索引 id
        :rtype: str
        """
        return self._ServerlessId

    @ServerlessId.setter
    def ServerlessId(self, ServerlessId):
        self._ServerlessId = ServerlessId

    @property
    def CosBucket(self):
        """cos 桶名
        :rtype: str
        """
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def BasePath(self):
        """BasePath 路径
        :rtype: str
        """
        return self._BasePath

    @BasePath.setter
    def BasePath(self, BasePath):
        self._BasePath = BasePath

    @property
    def ClusterInstanceId(self):
        """云上集群 id
        :rtype: str
        """
        return self._ClusterInstanceId

    @ClusterInstanceId.setter
    def ClusterInstanceId(self, ClusterInstanceId):
        self._ClusterInstanceId = ClusterInstanceId

    @property
    def CommonIndexArr(self):
        """待迁移普通索引名列表
        :rtype: list of str
        """
        return self._CommonIndexArr

    @CommonIndexArr.setter
    def CommonIndexArr(self, CommonIndexArr):
        self._CommonIndexArr = CommonIndexArr

    @property
    def DataStreamArr(self):
        """待迁移自治索引名列表
        :rtype: list of str
        """
        return self._DataStreamArr

    @DataStreamArr.setter
    def DataStreamArr(self, DataStreamArr):
        self._DataStreamArr = DataStreamArr


    def _deserialize(self, params):
        self._Snapshot = params.get("Snapshot")
        self._ServerlessId = params.get("ServerlessId")
        self._CosBucket = params.get("CosBucket")
        self._BasePath = params.get("BasePath")
        self._ClusterInstanceId = params.get("ClusterInstanceId")
        self._CommonIndexArr = params.get("CommonIndexArr")
        self._DataStreamArr = params.get("DataStreamArr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosMigrateToServerlessInstanceResponse(AbstractModel):
    """CreateCosMigrateToServerlessInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 迁移 taskid
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """迁移 taskid
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateIndexRequest(AbstractModel):
    """CreateIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES集群ID
        :type InstanceId: str
        :param _IndexType: 创建的索引类型。auto：自治索引；normal：普通索引
        :type IndexType: str
        :param _IndexName: 创建的索引名
        :type IndexName: str
        :param _IndexMetaJson: 【必填】创建的索引元数据JSON，如mappings、settings
        :type IndexMetaJson: str
        :param _Username: 集群访问用户名
        :type Username: str
        :param _Password: 集群访问密码
        :type Password: str
        """
        self._InstanceId = None
        self._IndexType = None
        self._IndexName = None
        self._IndexMetaJson = None
        self._Username = None
        self._Password = None

    @property
    def InstanceId(self):
        """ES集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexType(self):
        """创建的索引类型。auto：自治索引；normal：普通索引
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        """创建的索引名
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IndexMetaJson(self):
        """【必填】创建的索引元数据JSON，如mappings、settings
        :rtype: str
        """
        return self._IndexMetaJson

    @IndexMetaJson.setter
    def IndexMetaJson(self, IndexMetaJson):
        self._IndexMetaJson = IndexMetaJson

    @property
    def Username(self):
        """集群访问用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """集群访问密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._IndexMetaJson = params.get("IndexMetaJson")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexResponse(AbstractModel):
    """CreateIndex返回参数结构体

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


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _EsVersion: 实例版本（支持"5.6.4"、"6.4.3"、"6.8.2"、"7.5.1"、"7.10.1"）
        :type EsVersion: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _Password: 访问密码（密码需8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）
        :type Password: str
        :param _InstanceName: 实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）
        :type InstanceName: str
        :param _NodeNum: 已废弃请使用NodeInfoList
节点数量（2-50个）
        :type NodeNum: int
        :param _ChargeType: 计费类型<li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li>默认值POSTPAID_BY_HOUR
        :type ChargeType: str
        :param _ChargePeriod: 包年包月购买时长（单位由参数TimeUnit决定）
        :type ChargePeriod: int
        :param _RenewFlag: 自动续费标识<li>RENEW_FLAG_AUTO：自动续费</li><li>RENEW_FLAG_MANUAL：不自动续费，用户手动续费</li>ChargeType为PREPAID时需要设置，如不传递该参数，普通用户默认不自动续费，SVIP用户自动续费
        :type RenewFlag: str
        :param _NodeType: 已废弃请使用NodeInfoList
节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param _DiskType: 已废弃请使用NodeInfoList
节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高性能云硬盘</li><li> CLOUD_HSSD：增强型SSD云硬盘</li><li> CLOUD_BSSD：通用型SSD云硬盘</li>默认值CLOUD_SSD
        :type DiskType: str
        :param _DiskSize: 已废弃请使用NodeInfoList
节点磁盘容量（单位GB）
        :type DiskSize: int
        :param _TimeUnit: 计费时长单位（ChargeType为PREPAID时需要设置，默认值为“m”，表示月，当前只支持“m”）
        :type TimeUnit: str
        :param _AutoVoucher: 是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID列表（目前仅支持指定一张代金券）
        :type VoucherIds: list of str
        :param _EnableDedicatedMaster: 已废弃请使用NodeInfoList
是否创建专用主节点<li>true：开启专用主节点</li><li>false：不开启专用主节点</li>默认值false
        :type EnableDedicatedMaster: bool
        :param _MasterNodeNum: 已废弃请使用NodeInfoList
专用主节点个数（只支持3个和5个，EnableDedicatedMaster为true时该值必传）
        :type MasterNodeNum: int
        :param _MasterNodeType: 已废弃请使用NodeInfoList
专用主节点类型（EnableDedicatedMaster为true时必传）<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type MasterNodeType: str
        :param _MasterNodeDiskSize: 已废弃请使用NodeInfoList
专用主节点磁盘大小（单位GB，非必传，若传递则必须为50，暂不支持自定义）
        :type MasterNodeDiskSize: int
        :param _ClusterNameInConf: 集群配置文件中的ClusterName（系统默认配置为实例ID，暂不支持自定义）
        :type ClusterNameInConf: str
        :param _DeployMode: 集群部署方式<li>0：单可用区部署</li><li>1：多可用区部署，北京、上海、上海金融、广州、南京、香港、新加坡、法兰克福（白名单控制）</li>默认为0
        :type DeployMode: int
        :param _MultiZoneInfo: 多可用区部署时可用区的详细信息(DeployMode为1时必传)
        :type MultiZoneInfo: list of ZoneDetail
        :param _LicenseType: License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum
        :type LicenseType: str
        :param _NodeInfoList: 节点信息列表， 用于描述集群各类节点的规格信息如节点类型，节点个数，节点规格，磁盘类型，磁盘大小等
        :type NodeInfoList: list of NodeInfo
        :param _TagList: 节点标签信息列表
        :type TagList: list of TagInfo
        :param _BasicSecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
        :type BasicSecurityType: int
        :param _SceneType: 场景化模板类型 0：不启用 1：通用 2：日志 3：搜索
        :type SceneType: int
        :param _WebNodeTypeInfo: 可视化节点配置
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param _Protocol: 创建https集群，默认是http
        :type Protocol: str
        :param _OperationDuration: 可维护时间段
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        :param _EnableHybridStorage: 是否开启存算分离
        :type EnableHybridStorage: bool
        :param _DiskEnhance: 是否开启essd 增强型云盘
        :type DiskEnhance: int
        :param _EnableDiagnose: 是否开启智能巡检
        :type EnableDiagnose: bool
        :param _CdcId: cdcId，使用cdc子网时传递
        :type CdcId: str
        :param _DisasterRecoverGroupAffinity: 置放群组亲和度，范围[0,10]，0表示不开启
        :type DisasterRecoverGroupAffinity: int
        :param _SubProductCode: 子产品ID枚举值： 开源版："sp_es_io2"， 基础版："sp_es_basic"，白金版："sp_es_platinum"，企业版："sp_es_enterprise"，CDC白金版："sp_es_cdc_platinum"，日志增强版："sp_es_enlogging"，tsearch："sp_tsearch_io2"，logstash："sp_es_logstash" ，可以为空，为空的时候后台取LicenseType映射该字段
        :type SubProductCode: str
        :param _ReadWriteMode: 读写分离模式：0-不开启，1-本地读写分离，2-远端读写分离
        :type ReadWriteMode: int
        :param _EnableScheduleRecoverGroup: 置放群组是否开启异步任务
        :type EnableScheduleRecoverGroup: bool
        :param _EnableScheduleOperationDuration: 置放群组开启异步任务的可维护时间段
        :type EnableScheduleOperationDuration: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        self._Zone = None
        self._EsVersion = None
        self._VpcId = None
        self._SubnetId = None
        self._Password = None
        self._InstanceName = None
        self._NodeNum = None
        self._ChargeType = None
        self._ChargePeriod = None
        self._RenewFlag = None
        self._NodeType = None
        self._DiskType = None
        self._DiskSize = None
        self._TimeUnit = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._EnableDedicatedMaster = None
        self._MasterNodeNum = None
        self._MasterNodeType = None
        self._MasterNodeDiskSize = None
        self._ClusterNameInConf = None
        self._DeployMode = None
        self._MultiZoneInfo = None
        self._LicenseType = None
        self._NodeInfoList = None
        self._TagList = None
        self._BasicSecurityType = None
        self._SceneType = None
        self._WebNodeTypeInfo = None
        self._Protocol = None
        self._OperationDuration = None
        self._EnableHybridStorage = None
        self._DiskEnhance = None
        self._EnableDiagnose = None
        self._CdcId = None
        self._DisasterRecoverGroupAffinity = None
        self._SubProductCode = None
        self._ReadWriteMode = None
        self._EnableScheduleRecoverGroup = None
        self._EnableScheduleOperationDuration = None

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
    def EsVersion(self):
        """实例版本（支持"5.6.4"、"6.4.3"、"6.8.2"、"7.5.1"、"7.10.1"）
        :rtype: str
        """
        return self._EsVersion

    @EsVersion.setter
    def EsVersion(self, EsVersion):
        self._EsVersion = EsVersion

    @property
    def VpcId(self):
        """私有网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Password(self):
        """访问密码（密码需8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def InstanceName(self):
        """实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NodeNum(self):
        """已废弃请使用NodeInfoList
节点数量（2-50个）
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def ChargeType(self):
        """计费类型<li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li>默认值POSTPAID_BY_HOUR
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargePeriod(self):
        """包年包月购买时长（单位由参数TimeUnit决定）
        :rtype: int
        """
        return self._ChargePeriod

    @ChargePeriod.setter
    def ChargePeriod(self, ChargePeriod):
        self._ChargePeriod = ChargePeriod

    @property
    def RenewFlag(self):
        """自动续费标识<li>RENEW_FLAG_AUTO：自动续费</li><li>RENEW_FLAG_MANUAL：不自动续费，用户手动续费</li>ChargeType为PREPAID时需要设置，如不传递该参数，普通用户默认不自动续费，SVIP用户自动续费
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def NodeType(self):
        """已废弃请使用NodeInfoList
节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def DiskType(self):
        """已废弃请使用NodeInfoList
节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高性能云硬盘</li><li> CLOUD_HSSD：增强型SSD云硬盘</li><li> CLOUD_BSSD：通用型SSD云硬盘</li>默认值CLOUD_SSD
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """已废弃请使用NodeInfoList
节点磁盘容量（单位GB）
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def TimeUnit(self):
        """计费时长单位（ChargeType为PREPAID时需要设置，默认值为“m”，表示月，当前只支持“m”）
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def AutoVoucher(self):
        """是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """代金券ID列表（目前仅支持指定一张代金券）
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def EnableDedicatedMaster(self):
        """已废弃请使用NodeInfoList
是否创建专用主节点<li>true：开启专用主节点</li><li>false：不开启专用主节点</li>默认值false
        :rtype: bool
        """
        return self._EnableDedicatedMaster

    @EnableDedicatedMaster.setter
    def EnableDedicatedMaster(self, EnableDedicatedMaster):
        self._EnableDedicatedMaster = EnableDedicatedMaster

    @property
    def MasterNodeNum(self):
        """已废弃请使用NodeInfoList
专用主节点个数（只支持3个和5个，EnableDedicatedMaster为true时该值必传）
        :rtype: int
        """
        return self._MasterNodeNum

    @MasterNodeNum.setter
    def MasterNodeNum(self, MasterNodeNum):
        self._MasterNodeNum = MasterNodeNum

    @property
    def MasterNodeType(self):
        """已废弃请使用NodeInfoList
专用主节点类型（EnableDedicatedMaster为true时必传）<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :rtype: str
        """
        return self._MasterNodeType

    @MasterNodeType.setter
    def MasterNodeType(self, MasterNodeType):
        self._MasterNodeType = MasterNodeType

    @property
    def MasterNodeDiskSize(self):
        """已废弃请使用NodeInfoList
专用主节点磁盘大小（单位GB，非必传，若传递则必须为50，暂不支持自定义）
        :rtype: int
        """
        return self._MasterNodeDiskSize

    @MasterNodeDiskSize.setter
    def MasterNodeDiskSize(self, MasterNodeDiskSize):
        self._MasterNodeDiskSize = MasterNodeDiskSize

    @property
    def ClusterNameInConf(self):
        """集群配置文件中的ClusterName（系统默认配置为实例ID，暂不支持自定义）
        :rtype: str
        """
        return self._ClusterNameInConf

    @ClusterNameInConf.setter
    def ClusterNameInConf(self, ClusterNameInConf):
        self._ClusterNameInConf = ClusterNameInConf

    @property
    def DeployMode(self):
        """集群部署方式<li>0：单可用区部署</li><li>1：多可用区部署，北京、上海、上海金融、广州、南京、香港、新加坡、法兰克福（白名单控制）</li>默认为0
        :rtype: int
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def MultiZoneInfo(self):
        """多可用区部署时可用区的详细信息(DeployMode为1时必传)
        :rtype: list of ZoneDetail
        """
        return self._MultiZoneInfo

    @MultiZoneInfo.setter
    def MultiZoneInfo(self, MultiZoneInfo):
        self._MultiZoneInfo = MultiZoneInfo

    @property
    def LicenseType(self):
        """License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def NodeInfoList(self):
        """节点信息列表， 用于描述集群各类节点的规格信息如节点类型，节点个数，节点规格，磁盘类型，磁盘大小等
        :rtype: list of NodeInfo
        """
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList

    @property
    def TagList(self):
        """节点标签信息列表
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def BasicSecurityType(self):
        """6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def SceneType(self):
        """场景化模板类型 0：不启用 1：通用 2：日志 3：搜索
        :rtype: int
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def WebNodeTypeInfo(self):
        """可视化节点配置
        :rtype: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        """
        return self._WebNodeTypeInfo

    @WebNodeTypeInfo.setter
    def WebNodeTypeInfo(self, WebNodeTypeInfo):
        self._WebNodeTypeInfo = WebNodeTypeInfo

    @property
    def Protocol(self):
        """创建https集群，默认是http
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OperationDuration(self):
        """可维护时间段
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration

    @property
    def EnableHybridStorage(self):
        """是否开启存算分离
        :rtype: bool
        """
        return self._EnableHybridStorage

    @EnableHybridStorage.setter
    def EnableHybridStorage(self, EnableHybridStorage):
        self._EnableHybridStorage = EnableHybridStorage

    @property
    def DiskEnhance(self):
        """是否开启essd 增强型云盘
        :rtype: int
        """
        return self._DiskEnhance

    @DiskEnhance.setter
    def DiskEnhance(self, DiskEnhance):
        self._DiskEnhance = DiskEnhance

    @property
    def EnableDiagnose(self):
        """是否开启智能巡检
        :rtype: bool
        """
        return self._EnableDiagnose

    @EnableDiagnose.setter
    def EnableDiagnose(self, EnableDiagnose):
        self._EnableDiagnose = EnableDiagnose

    @property
    def CdcId(self):
        """cdcId，使用cdc子网时传递
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def DisasterRecoverGroupAffinity(self):
        """置放群组亲和度，范围[0,10]，0表示不开启
        :rtype: int
        """
        return self._DisasterRecoverGroupAffinity

    @DisasterRecoverGroupAffinity.setter
    def DisasterRecoverGroupAffinity(self, DisasterRecoverGroupAffinity):
        self._DisasterRecoverGroupAffinity = DisasterRecoverGroupAffinity

    @property
    def SubProductCode(self):
        """子产品ID枚举值： 开源版："sp_es_io2"， 基础版："sp_es_basic"，白金版："sp_es_platinum"，企业版："sp_es_enterprise"，CDC白金版："sp_es_cdc_platinum"，日志增强版："sp_es_enlogging"，tsearch："sp_tsearch_io2"，logstash："sp_es_logstash" ，可以为空，为空的时候后台取LicenseType映射该字段
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def ReadWriteMode(self):
        """读写分离模式：0-不开启，1-本地读写分离，2-远端读写分离
        :rtype: int
        """
        return self._ReadWriteMode

    @ReadWriteMode.setter
    def ReadWriteMode(self, ReadWriteMode):
        self._ReadWriteMode = ReadWriteMode

    @property
    def EnableScheduleRecoverGroup(self):
        """置放群组是否开启异步任务
        :rtype: bool
        """
        return self._EnableScheduleRecoverGroup

    @EnableScheduleRecoverGroup.setter
    def EnableScheduleRecoverGroup(self, EnableScheduleRecoverGroup):
        self._EnableScheduleRecoverGroup = EnableScheduleRecoverGroup

    @property
    def EnableScheduleOperationDuration(self):
        """置放群组开启异步任务的可维护时间段
        :rtype: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        return self._EnableScheduleOperationDuration

    @EnableScheduleOperationDuration.setter
    def EnableScheduleOperationDuration(self, EnableScheduleOperationDuration):
        self._EnableScheduleOperationDuration = EnableScheduleOperationDuration


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._EsVersion = params.get("EsVersion")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Password = params.get("Password")
        self._InstanceName = params.get("InstanceName")
        self._NodeNum = params.get("NodeNum")
        self._ChargeType = params.get("ChargeType")
        self._ChargePeriod = params.get("ChargePeriod")
        self._RenewFlag = params.get("RenewFlag")
        self._NodeType = params.get("NodeType")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._TimeUnit = params.get("TimeUnit")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self._MasterNodeNum = params.get("MasterNodeNum")
        self._MasterNodeType = params.get("MasterNodeType")
        self._MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self._ClusterNameInConf = params.get("ClusterNameInConf")
        self._DeployMode = params.get("DeployMode")
        if params.get("MultiZoneInfo") is not None:
            self._MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self._MultiZoneInfo.append(obj)
        self._LicenseType = params.get("LicenseType")
        if params.get("NodeInfoList") is not None:
            self._NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeInfoList.append(obj)
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._BasicSecurityType = params.get("BasicSecurityType")
        self._SceneType = params.get("SceneType")
        if params.get("WebNodeTypeInfo") is not None:
            self._WebNodeTypeInfo = WebNodeTypeInfo()
            self._WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self._Protocol = params.get("Protocol")
        if params.get("OperationDuration") is not None:
            self._OperationDuration = OperationDuration()
            self._OperationDuration._deserialize(params.get("OperationDuration"))
        self._EnableHybridStorage = params.get("EnableHybridStorage")
        self._DiskEnhance = params.get("DiskEnhance")
        self._EnableDiagnose = params.get("EnableDiagnose")
        self._CdcId = params.get("CdcId")
        self._DisasterRecoverGroupAffinity = params.get("DisasterRecoverGroupAffinity")
        self._SubProductCode = params.get("SubProductCode")
        self._ReadWriteMode = params.get("ReadWriteMode")
        self._EnableScheduleRecoverGroup = params.get("EnableScheduleRecoverGroup")
        if params.get("EnableScheduleOperationDuration") is not None:
            self._EnableScheduleOperationDuration = EnableScheduleOperationDuration()
            self._EnableScheduleOperationDuration._deserialize(params.get("EnableScheduleOperationDuration"))
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
        :type InstanceId: str
        :param _DealName: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._DealName = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealName(self):
        """订单号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._InstanceId = params.get("InstanceId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateLogstashInstanceRequest(AbstractModel):
    """CreateLogstashInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）
        :type InstanceName: str
        :param _Zone: 可用区
        :type Zone: str
        :param _LogstashVersion: 实例版本（支持"6.8.13"、"7.10.1"）
        :type LogstashVersion: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _NodeNum: 节点数量（2-50个）
        :type NodeNum: int
        :param _ChargeType: 计费类型<li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li>默认值POSTPAID_BY_HOUR
        :type ChargeType: str
        :param _ChargePeriod: 包年包月购买时长（单位由参数TimeUnit决定）
        :type ChargePeriod: int
        :param _TimeUnit: 计费时长单位（ChargeType为PREPAID时需要设置，默认值为“m”，表示月，当前只支持“m”）
        :type TimeUnit: str
        :param _AutoVoucher: 是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID列表（目前仅支持指定一张代金券）
        :type VoucherIds: list of str
        :param _RenewFlag: 自动续费标识<li>RENEW_FLAG_AUTO：自动续费</li><li>RENEW_FLAG_MANUAL：不自动续费，用户手动续费</li>ChargeType为PREPAID时需要设置，如不传递该参数，普通用户默认不自动续费，SVIP用户自动续费
        :type RenewFlag: str
        :param _NodeType: 节点规格<li>LOGSTASH.S1.SMALL2：1核2G</li><li>LOGSTASH.S1.MEDIUM4：2核4G</li><li>LOGSTASH.S1.MEDIUM8：2核8G</li><li>LOGSTASH.S1.LARGE16：4核16G</li><li>LOGSTASH.S1.2XLARGE32：8核32G</li><li>LOGSTASH.S1.4XLARGE32：16核32G</li><li>LOGSTASH.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param _DiskType: 节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高硬能云硬盘</li>默认值CLOUD_SSD
        :type DiskType: str
        :param _DiskSize: 节点磁盘容量（单位GB）
        :type DiskSize: int
        :param _LicenseType: License类型<li>oss：开源版</li><li>xpack：xpack版</li>默认值xpack
        :type LicenseType: str
        :param _TagList: 标签信息列表
        :type TagList: list of TagInfo
        :param _OperationDuration: 可维护时间段
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        """
        self._InstanceName = None
        self._Zone = None
        self._LogstashVersion = None
        self._VpcId = None
        self._SubnetId = None
        self._NodeNum = None
        self._ChargeType = None
        self._ChargePeriod = None
        self._TimeUnit = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._RenewFlag = None
        self._NodeType = None
        self._DiskType = None
        self._DiskSize = None
        self._LicenseType = None
        self._TagList = None
        self._OperationDuration = None

    @property
    def InstanceName(self):
        """实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

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
    def LogstashVersion(self):
        """实例版本（支持"6.8.13"、"7.10.1"）
        :rtype: str
        """
        return self._LogstashVersion

    @LogstashVersion.setter
    def LogstashVersion(self, LogstashVersion):
        self._LogstashVersion = LogstashVersion

    @property
    def VpcId(self):
        """私有网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def NodeNum(self):
        """节点数量（2-50个）
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def ChargeType(self):
        """计费类型<li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li>默认值POSTPAID_BY_HOUR
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargePeriod(self):
        """包年包月购买时长（单位由参数TimeUnit决定）
        :rtype: int
        """
        return self._ChargePeriod

    @ChargePeriod.setter
    def ChargePeriod(self, ChargePeriod):
        self._ChargePeriod = ChargePeriod

    @property
    def TimeUnit(self):
        """计费时长单位（ChargeType为PREPAID时需要设置，默认值为“m”，表示月，当前只支持“m”）
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def AutoVoucher(self):
        """是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """代金券ID列表（目前仅支持指定一张代金券）
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def RenewFlag(self):
        """自动续费标识<li>RENEW_FLAG_AUTO：自动续费</li><li>RENEW_FLAG_MANUAL：不自动续费，用户手动续费</li>ChargeType为PREPAID时需要设置，如不传递该参数，普通用户默认不自动续费，SVIP用户自动续费
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def NodeType(self):
        """节点规格<li>LOGSTASH.S1.SMALL2：1核2G</li><li>LOGSTASH.S1.MEDIUM4：2核4G</li><li>LOGSTASH.S1.MEDIUM8：2核8G</li><li>LOGSTASH.S1.LARGE16：4核16G</li><li>LOGSTASH.S1.2XLARGE32：8核32G</li><li>LOGSTASH.S1.4XLARGE32：16核32G</li><li>LOGSTASH.S1.4XLARGE64：16核64G</li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def DiskType(self):
        """节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高硬能云硬盘</li>默认值CLOUD_SSD
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """节点磁盘容量（单位GB）
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def LicenseType(self):
        """License类型<li>oss：开源版</li><li>xpack：xpack版</li>默认值xpack
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def TagList(self):
        """标签信息列表
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def OperationDuration(self):
        """可维护时间段
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._Zone = params.get("Zone")
        self._LogstashVersion = params.get("LogstashVersion")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._NodeNum = params.get("NodeNum")
        self._ChargeType = params.get("ChargeType")
        self._ChargePeriod = params.get("ChargePeriod")
        self._TimeUnit = params.get("TimeUnit")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._RenewFlag = params.get("RenewFlag")
        self._NodeType = params.get("NodeType")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._LicenseType = params.get("LicenseType")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        if params.get("OperationDuration") is not None:
            self._OperationDuration = OperationDuration()
            self._OperationDuration._deserialize(params.get("OperationDuration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogstashInstanceResponse(AbstractModel):
    """CreateLogstashInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateServerlessInstanceRequest(AbstractModel):
    """CreateServerlessInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IndexName: 索引名，需以-AppId结尾
        :type IndexName: str
        :param _Zone: 可用区
        :type Zone: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _IndexMetaJson: 创建的索引元数据JSON，如mappings、settings
        :type IndexMetaJson: str
        :param _SpaceId: 创建索引的空间ID
        :type SpaceId: str
        :param _Username: 创建索引的用户名
        :type Username: str
        :param _Password: 创建索引的密码
        :type Password: str
        :param _ServerlessDi: 创建数据接入
        :type ServerlessDi: :class:`tencentcloud.es.v20180416.models.ServerlessDi`
        :param _AutoGetIp: 是否自行添加白名单ip
        :type AutoGetIp: int
        :param _TagList: 标签信息
        :type TagList: list of TagInfo
        :param _KibanaWhiteIpList: kibana公网白名单
        :type KibanaWhiteIpList: list of str
        """
        self._IndexName = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._IndexMetaJson = None
        self._SpaceId = None
        self._Username = None
        self._Password = None
        self._ServerlessDi = None
        self._AutoGetIp = None
        self._TagList = None
        self._KibanaWhiteIpList = None

    @property
    def IndexName(self):
        """索引名，需以-AppId结尾
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

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
    def VpcId(self):
        """私有网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def IndexMetaJson(self):
        """创建的索引元数据JSON，如mappings、settings
        :rtype: str
        """
        return self._IndexMetaJson

    @IndexMetaJson.setter
    def IndexMetaJson(self, IndexMetaJson):
        self._IndexMetaJson = IndexMetaJson

    @property
    def SpaceId(self):
        """创建索引的空间ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Username(self):
        """创建索引的用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """创建索引的密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ServerlessDi(self):
        """创建数据接入
        :rtype: :class:`tencentcloud.es.v20180416.models.ServerlessDi`
        """
        return self._ServerlessDi

    @ServerlessDi.setter
    def ServerlessDi(self, ServerlessDi):
        self._ServerlessDi = ServerlessDi

    @property
    def AutoGetIp(self):
        """是否自行添加白名单ip
        :rtype: int
        """
        return self._AutoGetIp

    @AutoGetIp.setter
    def AutoGetIp(self, AutoGetIp):
        self._AutoGetIp = AutoGetIp

    @property
    def TagList(self):
        """标签信息
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def KibanaWhiteIpList(self):
        """kibana公网白名单
        :rtype: list of str
        """
        return self._KibanaWhiteIpList

    @KibanaWhiteIpList.setter
    def KibanaWhiteIpList(self, KibanaWhiteIpList):
        self._KibanaWhiteIpList = KibanaWhiteIpList


    def _deserialize(self, params):
        self._IndexName = params.get("IndexName")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._IndexMetaJson = params.get("IndexMetaJson")
        self._SpaceId = params.get("SpaceId")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        if params.get("ServerlessDi") is not None:
            self._ServerlessDi = ServerlessDi()
            self._ServerlessDi._deserialize(params.get("ServerlessDi"))
        self._AutoGetIp = params.get("AutoGetIp")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._KibanaWhiteIpList = params.get("KibanaWhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerlessInstanceResponse(AbstractModel):
    """CreateServerlessInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _DealName: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._DealName = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealName(self):
        """订单号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._InstanceId = params.get("InstanceId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateServerlessSpaceV2Request(AbstractModel):
    """CreateServerlessSpaceV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcInfo: vpc信息
        :type VpcInfo: list of VpcInfo
        :param _SpaceName: 索引空间名
        :type SpaceName: str
        :param _Zone: 空间名称
        :type Zone: str
        :param _KibanaWhiteIpList: 白名单列表
        :type KibanaWhiteIpList: list of str
        :param _ZoneId: 空间id
        :type ZoneId: int
        :param _TagList: 标签信息
        :type TagList: list of TagInfo
        """
        self._VpcInfo = None
        self._SpaceName = None
        self._Zone = None
        self._KibanaWhiteIpList = None
        self._ZoneId = None
        self._TagList = None

    @property
    def VpcInfo(self):
        """vpc信息
        :rtype: list of VpcInfo
        """
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo

    @property
    def SpaceName(self):
        """索引空间名
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def Zone(self):
        """空间名称
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def KibanaWhiteIpList(self):
        """白名单列表
        :rtype: list of str
        """
        return self._KibanaWhiteIpList

    @KibanaWhiteIpList.setter
    def KibanaWhiteIpList(self, KibanaWhiteIpList):
        self._KibanaWhiteIpList = KibanaWhiteIpList

    @property
    def ZoneId(self):
        """空间id
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TagList(self):
        """标签信息
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        if params.get("VpcInfo") is not None:
            self._VpcInfo = []
            for item in params.get("VpcInfo"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfo.append(obj)
        self._SpaceName = params.get("SpaceName")
        self._Zone = params.get("Zone")
        self._KibanaWhiteIpList = params.get("KibanaWhiteIpList")
        self._ZoneId = params.get("ZoneId")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerlessSpaceV2Response(AbstractModel):
    """CreateServerlessSpaceV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间ID
        :type SpaceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpaceId = None
        self._RequestId = None

    @property
    def SpaceId(self):
        """空间ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

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
        self._SpaceId = params.get("SpaceId")
        self._RequestId = params.get("RequestId")


class DataStreamInfo(AbstractModel):
    """自治索引信息

    """

    def __init__(self):
        r"""
        :param _DataStreamName: 自治索引名
注意：此字段可能返回 null，表示取不到有效值。
        :type DataStreamName: str
        :param _IsShardComplete: 分片状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IsShardComplete: int
        """
        self._DataStreamName = None
        self._IsShardComplete = None

    @property
    def DataStreamName(self):
        """自治索引名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DataStreamName

    @DataStreamName.setter
    def DataStreamName(self, DataStreamName):
        self._DataStreamName = DataStreamName

    @property
    def IsShardComplete(self):
        """分片状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsShardComplete

    @IsShardComplete.setter
    def IsShardComplete(self, IsShardComplete):
        self._IsShardComplete = IsShardComplete


    def _deserialize(self, params):
        self._DataStreamName = params.get("DataStreamName")
        self._IsShardComplete = params.get("IsShardComplete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterSnapshotRequest(AbstractModel):
    """DeleteClusterSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id，格式：es-xxxx
        :type InstanceId: str
        :param _RepositoryName: 快照仓库名称
        :type RepositoryName: str
        :param _SnapshotName: 集群快照名称
        :type SnapshotName: str
        """
        self._InstanceId = None
        self._RepositoryName = None
        self._SnapshotName = None

    @property
    def InstanceId(self):
        """集群实例Id，格式：es-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RepositoryName(self):
        """快照仓库名称
        :rtype: str
        """
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def SnapshotName(self):
        """集群快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RepositoryName = params.get("RepositoryName")
        self._SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterSnapshotResponse(AbstractModel):
    """DeleteClusterSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DeleteIndexRequest(AbstractModel):
    """DeleteIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES集群ID
        :type InstanceId: str
        :param _IndexType: 删除的索引类型。auto：自治索引；normal：普通索引
        :type IndexType: str
        :param _IndexName: 删除的索引名
        :type IndexName: str
        :param _Username: 集群访问用户名
        :type Username: str
        :param _Password: 集群访问密码
        :type Password: str
        :param _BackingIndexName: 后备索引名
        :type BackingIndexName: str
        """
        self._InstanceId = None
        self._IndexType = None
        self._IndexName = None
        self._Username = None
        self._Password = None
        self._BackingIndexName = None

    @property
    def InstanceId(self):
        """ES集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexType(self):
        """删除的索引类型。auto：自治索引；normal：普通索引
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        """删除的索引名
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def Username(self):
        """集群访问用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """集群访问密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def BackingIndexName(self):
        """后备索引名
        :rtype: str
        """
        return self._BackingIndexName

    @BackingIndexName.setter
    def BackingIndexName(self, BackingIndexName):
        self._BackingIndexName = BackingIndexName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._BackingIndexName = params.get("BackingIndexName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIndexResponse(AbstractModel):
    """DeleteIndex返回参数结构体

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


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
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
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

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


class DeleteLogstashInstanceRequest(AbstractModel):
    """DeleteLogstashInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
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
        


class DeleteLogstashInstanceResponse(AbstractModel):
    """DeleteLogstashInstance返回参数结构体

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


class DeleteLogstashPipelinesRequest(AbstractModel):
    """DeleteLogstashPipelines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _PipelineIds: 管道ID列表
        :type PipelineIds: list of str
        """
        self._InstanceId = None
        self._PipelineIds = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PipelineIds(self):
        """管道ID列表
        :rtype: list of str
        """
        return self._PipelineIds

    @PipelineIds.setter
    def PipelineIds(self, PipelineIds):
        self._PipelineIds = PipelineIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PipelineIds = params.get("PipelineIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogstashPipelinesResponse(AbstractModel):
    """DeleteLogstashPipelines返回参数结构体

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


class DeleteServerlessInstanceRequest(AbstractModel):
    """DeleteServerlessInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: serverless实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """serverless实例ID
        :rtype: str
        """
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
        


class DeleteServerlessInstanceResponse(AbstractModel):
    """DeleteServerlessInstance返回参数结构体

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


class DeleteServerlessSpaceUserRequest(AbstractModel):
    """DeleteServerlessSpaceUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间的ID
        :type SpaceId: str
        :param _Username: 创建索引的用户名
        :type Username: str
        """
        self._SpaceId = None
        self._Username = None

    @property
    def SpaceId(self):
        """空间的ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Username(self):
        """创建索引的用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._Username = params.get("Username")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServerlessSpaceUserResponse(AbstractModel):
    """DeleteServerlessSpaceUser返回参数结构体

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


class DescribeClusterSnapshotRequest(AbstractModel):
    """DescribeClusterSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id，格式：es-xxxx
        :type InstanceId: str
        :param _RepositoryName: 快照仓库名称
        :type RepositoryName: str
        :param _SnapshotName: 集群快照名称
        :type SnapshotName: str
        """
        self._InstanceId = None
        self._RepositoryName = None
        self._SnapshotName = None

    @property
    def InstanceId(self):
        """集群实例Id，格式：es-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RepositoryName(self):
        """快照仓库名称
        :rtype: str
        """
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def SnapshotName(self):
        """集群快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RepositoryName = params.get("RepositoryName")
        self._SnapshotName = params.get("SnapshotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterSnapshotResponse(AbstractModel):
    """DescribeClusterSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id，格式：es-xxxx
        :type InstanceId: str
        :param _Snapshots: 快照备份详情列表
        :type Snapshots: list of Snapshots
        :param _RepositoryName: 快照仓库名称
        :type RepositoryName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Snapshots = None
        self._RepositoryName = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """集群实例Id，格式：es-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Snapshots(self):
        """快照备份详情列表
        :rtype: list of Snapshots
        """
        return self._Snapshots

    @Snapshots.setter
    def Snapshots(self, Snapshots):
        self._Snapshots = Snapshots

    @property
    def RepositoryName(self):
        """快照仓库名称
        :rtype: str
        """
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

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
        self._InstanceId = params.get("InstanceId")
        if params.get("Snapshots") is not None:
            self._Snapshots = []
            for item in params.get("Snapshots"):
                obj = Snapshots()
                obj._deserialize(item)
                self._Snapshots.append(obj)
        self._RepositoryName = params.get("RepositoryName")
        self._RequestId = params.get("RequestId")


class DescribeDiagnoseRequest(AbstractModel):
    """DescribeDiagnose请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES实例ID
        :type InstanceId: str
        :param _Date: 报告日期，格式20210301
        :type Date: str
        :param _Limit: 报告返回份数
        :type Limit: int
        """
        self._InstanceId = None
        self._Date = None
        self._Limit = None

    @property
    def InstanceId(self):
        """ES实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        """报告日期，格式20210301
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Limit(self):
        """报告返回份数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiagnoseResponse(AbstractModel):
    """DescribeDiagnose返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 诊断报告个数
        :type Total: int
        :param _DiagnoseResults: 诊断报告列表
        :type DiagnoseResults: list of DiagnoseResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DiagnoseResults = None
        self._RequestId = None

    @property
    def Total(self):
        """诊断报告个数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DiagnoseResults(self):
        """诊断报告列表
        :rtype: list of DiagnoseResult
        """
        return self._DiagnoseResults

    @DiagnoseResults.setter
    def DiagnoseResults(self, DiagnoseResults):
        self._DiagnoseResults = DiagnoseResults

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
        self._Total = params.get("Total")
        if params.get("DiagnoseResults") is not None:
            self._DiagnoseResults = []
            for item in params.get("DiagnoseResults"):
                obj = DiagnoseResult()
                obj._deserialize(item)
                self._DiagnoseResults.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIndexListRequest(AbstractModel):
    """DescribeIndexList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IndexType: 索引类型。auto：自治索引；normal：普通索引
        :type IndexType: str
        :param _InstanceId: ES集群ID
        :type InstanceId: str
        :param _IndexName: 索引名，若填空则获取所有索引
        :type IndexName: str
        :param _Username: 集群访问用户名
        :type Username: str
        :param _Password: 集群访问密码
        :type Password: str
        :param _Offset: 分页起始位置
        :type Offset: int
        :param _Limit: 一页展示数量
        :type Limit: int
        :param _OrderBy: 排序字段，支持索引名：IndexName、索引存储量：IndexStorage、索引创建时间：IndexCreateTime
        :type OrderBy: str
        :param _IndexStatusList: 过滤索引状态
        :type IndexStatusList: list of str
        :param _Order: 排序顺序，支持asc、desc，默认为desc 数据格式"asc","desc"
        :type Order: str
        """
        self._IndexType = None
        self._InstanceId = None
        self._IndexName = None
        self._Username = None
        self._Password = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._IndexStatusList = None
        self._Order = None

    @property
    def IndexType(self):
        """索引类型。auto：自治索引；normal：普通索引
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def InstanceId(self):
        """ES集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexName(self):
        """索引名，若填空则获取所有索引
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def Username(self):
        """集群访问用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """集群访问密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Offset(self):
        """分页起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页展示数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        """排序字段，支持索引名：IndexName、索引存储量：IndexStorage、索引创建时间：IndexCreateTime
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def IndexStatusList(self):
        """过滤索引状态
        :rtype: list of str
        """
        return self._IndexStatusList

    @IndexStatusList.setter
    def IndexStatusList(self, IndexStatusList):
        self._IndexStatusList = IndexStatusList

    @property
    def Order(self):
        """排序顺序，支持asc、desc，默认为desc 数据格式"asc","desc"
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._IndexType = params.get("IndexType")
        self._InstanceId = params.get("InstanceId")
        self._IndexName = params.get("IndexName")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._IndexStatusList = params.get("IndexStatusList")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexListResponse(AbstractModel):
    """DescribeIndexList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IndexMetaFields: 索引元数据字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexMetaFields: list of IndexMetaField
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IndexMetaFields = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def IndexMetaFields(self):
        """索引元数据字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IndexMetaField
        """
        return self._IndexMetaFields

    @IndexMetaFields.setter
    def IndexMetaFields(self, IndexMetaFields):
        self._IndexMetaFields = IndexMetaFields

    @property
    def TotalCount(self):
        """查询总数
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
        if params.get("IndexMetaFields") is not None:
            self._IndexMetaFields = []
            for item in params.get("IndexMetaFields"):
                obj = IndexMetaField()
                obj._deserialize(item)
                self._IndexMetaFields.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIndexMetaRequest(AbstractModel):
    """DescribeIndexMeta请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES集群ID
        :type InstanceId: str
        :param _IndexType: 索引类型。auto：自治索引；normal：普通索引
        :type IndexType: str
        :param _IndexName: 索引名，若填空则获取所有索引
        :type IndexName: str
        :param _Username: 集群访问用户名
        :type Username: str
        :param _Password: 集群访问密码
        :type Password: str
        """
        self._InstanceId = None
        self._IndexType = None
        self._IndexName = None
        self._Username = None
        self._Password = None

    @property
    def InstanceId(self):
        """ES集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexType(self):
        """索引类型。auto：自治索引；normal：普通索引
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        """索引名，若填空则获取所有索引
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def Username(self):
        """集群访问用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """集群访问密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexMetaResponse(AbstractModel):
    """DescribeIndexMeta返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IndexMetaField: 索引元数据字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexMetaField: :class:`tencentcloud.es.v20180416.models.IndexMetaField`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IndexMetaField = None
        self._RequestId = None

    @property
    def IndexMetaField(self):
        """索引元数据字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexMetaField`
        """
        return self._IndexMetaField

    @IndexMetaField.setter
    def IndexMetaField(self, IndexMetaField):
        self._IndexMetaField = IndexMetaField

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
        if params.get("IndexMetaField") is not None:
            self._IndexMetaField = IndexMetaField()
            self._IndexMetaField._deserialize(params.get("IndexMetaField"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    """DescribeInstanceLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _LogType: 日志类型，默认值为1
<li>1, 主日志</li>
<li>2, 搜索慢日志</li>
<li>3, 索引慢日志</li>
<li>4, GC日志</li>
        :type LogType: int
        :param _SearchKey: 搜索词，支持LUCENE语法，如 level:WARN、ip:1.1.1.1、message:test-index等
        :type SearchKey: str
        :param _StartTime: 日志开始时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :type StartTime: str
        :param _EndTime: 日志结束时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :type EndTime: str
        :param _Offset: 分页起始值, 默认值为0
        :type Offset: int
        :param _Limit: 分页大小，默认值为100，最大值100
        :type Limit: int
        :param _OrderByType: 时间排序方式，默认值为0
<li>0, 降序</li>
<li>1, 升序</li>
        :type OrderByType: int
        """
        self._InstanceId = None
        self._LogType = None
        self._SearchKey = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        """集群实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogType(self):
        """日志类型，默认值为1
<li>1, 主日志</li>
<li>2, 搜索慢日志</li>
<li>3, 索引慢日志</li>
<li>4, GC日志</li>
        :rtype: int
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def SearchKey(self):
        """搜索词，支持LUCENE语法，如 level:WARN、ip:1.1.1.1、message:test-index等
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def StartTime(self):
        """日志开始时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """日志结束时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """分页起始值, 默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小，默认值为100，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByType(self):
        """时间排序方式，默认值为0
<li>0, 降序</li>
<li>1, 升序</li>
        :rtype: int
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogType = params.get("LogType")
        self._SearchKey = params.get("SearchKey")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLogsResponse(AbstractModel):
    """DescribeInstanceLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的日志条数
        :type TotalCount: int
        :param _InstanceLogList: 日志详细信息列表
        :type InstanceLogList: list of InstanceLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceLogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的日志条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceLogList(self):
        """日志详细信息列表
        :rtype: list of InstanceLog
        """
        return self._InstanceLogList

    @InstanceLogList.setter
    def InstanceLogList(self, InstanceLogList):
        self._InstanceLogList = InstanceLogList

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
        if params.get("InstanceLogList") is not None:
            self._InstanceLogList = []
            for item in params.get("InstanceLogList"):
                obj = InstanceLog()
                obj._deserialize(item)
                self._InstanceLogList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    """DescribeInstanceOperations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _StartTime: 起始时间, e.g. "2019-03-07 16:30:39"
        :type StartTime: str
        :param _EndTime: 结束时间, e.g. "2019-03-30 20:18:03"
        :type EndTime: str
        :param _Offset: 分页起始值
        :type Offset: int
        :param _Limit: 分页大小
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """集群实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """起始时间, e.g. "2019-03-07 16:30:39"
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间, e.g. "2019-03-30 20:18:03"
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """分页起始值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
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
        


class DescribeInstanceOperationsResponse(AbstractModel):
    """DescribeInstanceOperations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 操作记录总数
        :type TotalCount: int
        :param _Operations: 操作记录
        :type Operations: list of Operation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Operations = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """操作记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Operations(self):
        """操作记录
        :rtype: list of Operation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

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
        if params.get("Operations") is not None:
            self._Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self._Operations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancePluginInfo(AbstractModel):
    """插件信息

    """

    def __init__(self):
        r"""
        :param _PluginName: 插件名
        :type PluginName: str
        :param _PluginVersion: 插件版本
        :type PluginVersion: str
        :param _PluginDesc: 插件描述
        :type PluginDesc: str
        :param _Status: 插件状态：-2 已卸载 -1 卸载中 0 安装中 1 已安装
        :type Status: int
        :param _Removable: 插件是否可卸载
        :type Removable: bool
        :param _PluginType: 0：系统插件
        :type PluginType: int
        :param _PluginUpdateTime: 插件变更时间
        :type PluginUpdateTime: str
        """
        self._PluginName = None
        self._PluginVersion = None
        self._PluginDesc = None
        self._Status = None
        self._Removable = None
        self._PluginType = None
        self._PluginUpdateTime = None

    @property
    def PluginName(self):
        """插件名
        :rtype: str
        """
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginVersion(self):
        """插件版本
        :rtype: str
        """
        return self._PluginVersion

    @PluginVersion.setter
    def PluginVersion(self, PluginVersion):
        self._PluginVersion = PluginVersion

    @property
    def PluginDesc(self):
        """插件描述
        :rtype: str
        """
        return self._PluginDesc

    @PluginDesc.setter
    def PluginDesc(self, PluginDesc):
        self._PluginDesc = PluginDesc

    @property
    def Status(self):
        """插件状态：-2 已卸载 -1 卸载中 0 安装中 1 已安装
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Removable(self):
        """插件是否可卸载
        :rtype: bool
        """
        return self._Removable

    @Removable.setter
    def Removable(self, Removable):
        self._Removable = Removable

    @property
    def PluginType(self):
        """0：系统插件
        :rtype: int
        """
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def PluginUpdateTime(self):
        """插件变更时间
        :rtype: str
        """
        return self._PluginUpdateTime

    @PluginUpdateTime.setter
    def PluginUpdateTime(self, PluginUpdateTime):
        self._PluginUpdateTime = PluginUpdateTime


    def _deserialize(self, params):
        self._PluginName = params.get("PluginName")
        self._PluginVersion = params.get("PluginVersion")
        self._PluginDesc = params.get("PluginDesc")
        self._Status = params.get("Status")
        self._Removable = params.get("Removable")
        self._PluginType = params.get("PluginType")
        self._PluginUpdateTime = params.get("PluginUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancePluginListRequest(AbstractModel):
    """DescribeInstancePluginList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Offset: 分页起始值, 默认值0
        :type Offset: int
        :param _Limit: 分页大小，默认值10
        :type Limit: int
        :param _OrderBy: 排序字段<li>1：插件名 pluginName</li>
        :type OrderBy: str
        :param _OrderByType: 排序方式<li>0：升序 asc</li><li>1：降序 desc</li>
        :type OrderByType: str
        :param _PluginType: 0：系统插件
        :type PluginType: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderByType = None
        self._PluginType = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """分页起始值, 默认值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小，默认值10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        """排序字段<li>1：插件名 pluginName</li>
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        """排序方式<li>0：升序 asc</li><li>1：降序 desc</li>
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def PluginType(self):
        """0：系统插件
        :rtype: int
        """
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._PluginType = params.get("PluginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancePluginListResponse(AbstractModel):
    """DescribeInstancePluginList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的插件个数
        :type TotalCount: int
        :param _PluginList: 插件信息列表
        :type PluginList: list of DescribeInstancePluginInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PluginList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的插件个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PluginList(self):
        """插件信息列表
        :rtype: list of DescribeInstancePluginInfo
        """
        return self._PluginList

    @PluginList.setter
    def PluginList(self, PluginList):
        self._PluginList = PluginList

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
        if params.get("PluginList") is not None:
            self._PluginList = []
            for item in params.get("PluginList"):
                obj = DescribeInstancePluginInfo()
                obj._deserialize(item)
                self._PluginList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 集群实例所属可用区，不传则默认所有可用区
        :type Zone: str
        :param _InstanceIds: 集群实例ID列表
        :type InstanceIds: list of str
        :param _InstanceNames: 集群实例名称列表
        :type InstanceNames: list of str
        :param _Offset: 分页起始值, 默认值0
        :type Offset: int
        :param _Limit: 分页大小，默认值20
        :type Limit: int
        :param _OrderByKey: 排序字段<li>1：实例ID</li><li>2：实例名称</li><li>3：可用区</li><li>4：创建时间</li>若orderByKey未传递则按创建时间降序排序
        :type OrderByKey: int
        :param _OrderByType: 排序方式<li>0：升序</li><li>1：降序</li>若传递了orderByKey未传递orderByType, 则默认升序
        :type OrderByType: int
        :param _TagList: 节点标签信息列表
        :type TagList: list of TagInfo
        :param _IpList: 私有网络vip列表
        :type IpList: list of str
        :param _ZoneList: 可用区列表
        :type ZoneList: list of str
        :param _HealthStatus: 健康状态筛列表:0表示绿色，1表示黄色，2表示红色,-1表示未知
        :type HealthStatus: list of int
        :param _VpcIds: Vpc列表 筛选项
        :type VpcIds: list of str
        :param _CdcId: cdc集群id
        :type CdcId: str
        """
        self._Zone = None
        self._InstanceIds = None
        self._InstanceNames = None
        self._Offset = None
        self._Limit = None
        self._OrderByKey = None
        self._OrderByType = None
        self._TagList = None
        self._IpList = None
        self._ZoneList = None
        self._HealthStatus = None
        self._VpcIds = None
        self._CdcId = None

    @property
    def Zone(self):
        """集群实例所属可用区，不传则默认所有可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceIds(self):
        """集群实例ID列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        """集群实例名称列表
        :rtype: list of str
        """
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def Offset(self):
        """分页起始值, 默认值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小，默认值20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByKey(self):
        """排序字段<li>1：实例ID</li><li>2：实例名称</li><li>3：可用区</li><li>4：创建时间</li>若orderByKey未传递则按创建时间降序排序
        :rtype: int
        """
        return self._OrderByKey

    @OrderByKey.setter
    def OrderByKey(self, OrderByKey):
        self._OrderByKey = OrderByKey

    @property
    def OrderByType(self):
        """排序方式<li>0：升序</li><li>1：降序</li>若传递了orderByKey未传递orderByType, 则默认升序
        :rtype: int
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def TagList(self):
        """节点标签信息列表
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def IpList(self):
        """私有网络vip列表
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def ZoneList(self):
        """可用区列表
        :rtype: list of str
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def HealthStatus(self):
        """健康状态筛列表:0表示绿色，1表示黄色，2表示红色,-1表示未知
        :rtype: list of int
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def VpcIds(self):
        """Vpc列表 筛选项
        :rtype: list of str
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def CdcId(self):
        """cdc集群id
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByKey = params.get("OrderByKey")
        self._OrderByType = params.get("OrderByType")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._IpList = params.get("IpList")
        self._ZoneList = params.get("ZoneList")
        self._HealthStatus = params.get("HealthStatus")
        self._VpcIds = params.get("VpcIds")
        self._CdcId = params.get("CdcId")
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
        :param _TotalCount: 返回的实例个数
        :type TotalCount: int
        :param _InstanceList: 实例详细信息列表
        :type InstanceList: list of InstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的实例个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """实例详细信息列表
        :rtype: list of InstanceInfo
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

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
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogstashInstanceLogsRequest(AbstractModel):
    """DescribeLogstashInstanceLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _LogType: 日志类型，默认值为1
<li>1, 主日志</li>
<li>2, 慢日志</li>
<li>3, GC日志</li>
        :type LogType: int
        :param _SearchKey: 搜索词，支持LUCENE语法，如 level:WARN、ip:1.1.1.1、message:test-index等
        :type SearchKey: str
        :param _StartTime: 日志开始时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :type StartTime: str
        :param _EndTime: 日志结束时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :type EndTime: str
        :param _Offset: 分页起始值, 默认值为0
        :type Offset: int
        :param _Limit: 分页大小，默认值为100，最大值100
        :type Limit: int
        :param _OrderByType: 时间排序方式，默认值为0
<li>0, 降序</li>
<li>1, 升序</li>
        :type OrderByType: int
        """
        self._InstanceId = None
        self._LogType = None
        self._SearchKey = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LogType(self):
        """日志类型，默认值为1
<li>1, 主日志</li>
<li>2, 慢日志</li>
<li>3, GC日志</li>
        :rtype: int
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def SearchKey(self):
        """搜索词，支持LUCENE语法，如 level:WARN、ip:1.1.1.1、message:test-index等
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def StartTime(self):
        """日志开始时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """日志结束时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """分页起始值, 默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小，默认值为100，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByType(self):
        """时间排序方式，默认值为0
<li>0, 降序</li>
<li>1, 升序</li>
        :rtype: int
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LogType = params.get("LogType")
        self._SearchKey = params.get("SearchKey")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogstashInstanceLogsResponse(AbstractModel):
    """DescribeLogstashInstanceLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的日志条数
        :type TotalCount: int
        :param _InstanceLogList: 日志详细信息列表
        :type InstanceLogList: list of InstanceLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceLogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的日志条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceLogList(self):
        """日志详细信息列表
        :rtype: list of InstanceLog
        """
        return self._InstanceLogList

    @InstanceLogList.setter
    def InstanceLogList(self, InstanceLogList):
        self._InstanceLogList = InstanceLogList

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
        if params.get("InstanceLogList") is not None:
            self._InstanceLogList = []
            for item in params.get("InstanceLogList"):
                obj = InstanceLog()
                obj._deserialize(item)
                self._InstanceLogList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogstashInstanceOperationsRequest(AbstractModel):
    """DescribeLogstashInstanceOperations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StartTime: 起始时间, e.g. "2019-03-07 16:30:39"
        :type StartTime: str
        :param _EndTime: 结束时间, e.g. "2019-03-30 20:18:03"
        :type EndTime: str
        :param _Offset: 分页起始值
        :type Offset: int
        :param _Limit: 分页大小
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        """起始时间, e.g. "2019-03-07 16:30:39"
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间, e.g. "2019-03-30 20:18:03"
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """分页起始值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
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
        


class DescribeLogstashInstanceOperationsResponse(AbstractModel):
    """DescribeLogstashInstanceOperations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 操作记录总数
        :type TotalCount: int
        :param _Operations: 操作记录
        :type Operations: list of Operation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Operations = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """操作记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Operations(self):
        """操作记录
        :rtype: list of Operation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

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
        if params.get("Operations") is not None:
            self._Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self._Operations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogstashInstancesRequest(AbstractModel):
    """DescribeLogstashInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 实例所属可用区，不传则默认所有可用区
        :type Zone: str
        :param _InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param _InstanceNames: 实例名称列表
        :type InstanceNames: list of str
        :param _Offset: 分页起始值, 默认值0
        :type Offset: int
        :param _Limit: 分页大小，默认值20
        :type Limit: int
        :param _OrderByKey: 排序字段<li>1：实例ID</li><li>2：实例名称</li><li>3：可用区</li><li>4：创建时间</li>若orderKey未传递则按创建时间降序排序
        :type OrderByKey: int
        :param _OrderByType: 排序方式<li>0：升序</li><li>1：降序</li>若传递了orderByKey未传递orderByType, 则默认升序
        :type OrderByType: int
        :param _VpcIds: VpcId 筛选项
        :type VpcIds: list of str
        :param _TagList: 标签信息列表
        :type TagList: list of TagInfo
        """
        self._Zone = None
        self._InstanceIds = None
        self._InstanceNames = None
        self._Offset = None
        self._Limit = None
        self._OrderByKey = None
        self._OrderByType = None
        self._VpcIds = None
        self._TagList = None

    @property
    def Zone(self):
        """实例所属可用区，不传则默认所有可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceIds(self):
        """实例ID列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        """实例名称列表
        :rtype: list of str
        """
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def Offset(self):
        """分页起始值, 默认值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小，默认值20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByKey(self):
        """排序字段<li>1：实例ID</li><li>2：实例名称</li><li>3：可用区</li><li>4：创建时间</li>若orderKey未传递则按创建时间降序排序
        :rtype: int
        """
        return self._OrderByKey

    @OrderByKey.setter
    def OrderByKey(self, OrderByKey):
        self._OrderByKey = OrderByKey

    @property
    def OrderByType(self):
        """排序方式<li>0：升序</li><li>1：降序</li>若传递了orderByKey未传递orderByType, 则默认升序
        :rtype: int
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def VpcIds(self):
        """VpcId 筛选项
        :rtype: list of str
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def TagList(self):
        """标签信息列表
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByKey = params.get("OrderByKey")
        self._OrderByType = params.get("OrderByType")
        self._VpcIds = params.get("VpcIds")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogstashInstancesResponse(AbstractModel):
    """DescribeLogstashInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的实例个数
        :type TotalCount: int
        :param _InstanceList: 实例详细信息列表
        :type InstanceList: list of LogstashInstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的实例个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """实例详细信息列表
        :rtype: list of LogstashInstanceInfo
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

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
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = LogstashInstanceInfo()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogstashPipelinesRequest(AbstractModel):
    """DescribeLogstashPipelines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
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
        


class DescribeLogstashPipelinesResponse(AbstractModel):
    """DescribeLogstashPipelines返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 管道总数
        :type TotalCount: int
        :param _LogstashPipelineList: 管道列表
        :type LogstashPipelineList: list of LogstashPipelineInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LogstashPipelineList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """管道总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LogstashPipelineList(self):
        """管道列表
        :rtype: list of LogstashPipelineInfo
        """
        return self._LogstashPipelineList

    @LogstashPipelineList.setter
    def LogstashPipelineList(self, LogstashPipelineList):
        self._LogstashPipelineList = LogstashPipelineList

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
        if params.get("LogstashPipelineList") is not None:
            self._LogstashPipelineList = []
            for item in params.get("LogstashPipelineList"):
                obj = LogstashPipelineInfo()
                obj._deserialize(item)
                self._LogstashPipelineList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServerlessInstancesRequest(AbstractModel):
    """DescribeServerlessInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 索引集群ID
        :type InstanceIds: list of str
        :param _IndexNames: 索引名
        :type IndexNames: list of str
        :param _Offset: 分页起始位置
        :type Offset: int
        :param _Limit: 一页展示数量
        :type Limit: int
        :param _OrderBy: 排序字段，支持索引名：IndexName、索引存储量：IndexStorage、索引创建时间：IndexCreateTime
        :type OrderBy: str
        :param _IndexStatusList: 过滤索引状态
        :type IndexStatusList: list of str
        :param _Order: 排序顺序，支持asc、desc，默认为desc
        :type Order: str
        :param _SpaceIds: 索引空间ID列表
        :type SpaceIds: list of str
        :param _DiSourceTypes: 数据链路数据源类型
        :type DiSourceTypes: list of str
        :param _TagList: 标签信息
        :type TagList: list of TagInfo
        """
        self._InstanceIds = None
        self._IndexNames = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._IndexStatusList = None
        self._Order = None
        self._SpaceIds = None
        self._DiSourceTypes = None
        self._TagList = None

    @property
    def InstanceIds(self):
        """索引集群ID
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def IndexNames(self):
        """索引名
        :rtype: list of str
        """
        return self._IndexNames

    @IndexNames.setter
    def IndexNames(self, IndexNames):
        self._IndexNames = IndexNames

    @property
    def Offset(self):
        """分页起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页展示数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        """排序字段，支持索引名：IndexName、索引存储量：IndexStorage、索引创建时间：IndexCreateTime
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def IndexStatusList(self):
        """过滤索引状态
        :rtype: list of str
        """
        return self._IndexStatusList

    @IndexStatusList.setter
    def IndexStatusList(self, IndexStatusList):
        self._IndexStatusList = IndexStatusList

    @property
    def Order(self):
        """排序顺序，支持asc、desc，默认为desc
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def SpaceIds(self):
        """索引空间ID列表
        :rtype: list of str
        """
        return self._SpaceIds

    @SpaceIds.setter
    def SpaceIds(self, SpaceIds):
        self._SpaceIds = SpaceIds

    @property
    def DiSourceTypes(self):
        """数据链路数据源类型
        :rtype: list of str
        """
        return self._DiSourceTypes

    @DiSourceTypes.setter
    def DiSourceTypes(self, DiSourceTypes):
        self._DiSourceTypes = DiSourceTypes

    @property
    def TagList(self):
        """标签信息
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._IndexNames = params.get("IndexNames")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._IndexStatusList = params.get("IndexStatusList")
        self._Order = params.get("Order")
        self._SpaceIds = params.get("SpaceIds")
        self._DiSourceTypes = params.get("DiSourceTypes")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerlessInstancesResponse(AbstractModel):
    """DescribeServerlessInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IndexMetaFields: 索引元数据字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexMetaFields: list of ServerlessIndexMetaField
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IndexMetaFields = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def IndexMetaFields(self):
        """索引元数据字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ServerlessIndexMetaField
        """
        return self._IndexMetaFields

    @IndexMetaFields.setter
    def IndexMetaFields(self, IndexMetaFields):
        self._IndexMetaFields = IndexMetaFields

    @property
    def TotalCount(self):
        """查询总数
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
        if params.get("IndexMetaFields") is not None:
            self._IndexMetaFields = []
            for item in params.get("IndexMetaFields"):
                obj = ServerlessIndexMetaField()
                obj._deserialize(item)
                self._IndexMetaFields.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeServerlessMetricsRequest(AbstractModel):
    """DescribeServerlessMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: space空间id
        :type SpaceId: str
        :param _IndexId: index索引id
        :type IndexId: str
        :param _MetricType: 指标类型，暂时只支持Storage(存储大小),AllMetric(所有存储指标：索引流量、存储大小、文档数量、读请求和写请求)
        :type MetricType: list of str
        :param _DurationType: 时间长度类型DurationType(1: 3小时, 2: 昨天1天,3: 今日0点到现在)
        :type DurationType: int
        :param _BatchIndexList: 索引数据
        :type BatchIndexList: list of str
        """
        self._SpaceId = None
        self._IndexId = None
        self._MetricType = None
        self._DurationType = None
        self._BatchIndexList = None

    @property
    def SpaceId(self):
        """space空间id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def IndexId(self):
        """index索引id
        :rtype: str
        """
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId

    @property
    def MetricType(self):
        """指标类型，暂时只支持Storage(存储大小),AllMetric(所有存储指标：索引流量、存储大小、文档数量、读请求和写请求)
        :rtype: list of str
        """
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def DurationType(self):
        """时间长度类型DurationType(1: 3小时, 2: 昨天1天,3: 今日0点到现在)
        :rtype: int
        """
        return self._DurationType

    @DurationType.setter
    def DurationType(self, DurationType):
        self._DurationType = DurationType

    @property
    def BatchIndexList(self):
        """索引数据
        :rtype: list of str
        """
        return self._BatchIndexList

    @BatchIndexList.setter
    def BatchIndexList(self, BatchIndexList):
        self._BatchIndexList = BatchIndexList


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._IndexId = params.get("IndexId")
        self._MetricType = params.get("MetricType")
        self._DurationType = params.get("DurationType")
        self._BatchIndexList = params.get("BatchIndexList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerlessMetricsResponse(AbstractModel):
    """DescribeServerlessMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Storage: storage指标值，单位byte
        :type Storage: float
        :param _IndexTraffic: IndexTraffic指标值，单位byte
        :type IndexTraffic: float
        :param _ReadReqTimes: 读请求数，单位次数
        :type ReadReqTimes: int
        :param _WriteReqTimes: 写请求数，单位次数
        :type WriteReqTimes: int
        :param _DocCount: 文档数量，单位个数
        :type DocCount: int
        :param _MetricMapList: 指标数据数据
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricMapList: list of MetricMapByIndexId
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Storage = None
        self._IndexTraffic = None
        self._ReadReqTimes = None
        self._WriteReqTimes = None
        self._DocCount = None
        self._MetricMapList = None
        self._RequestId = None

    @property
    def Storage(self):
        """storage指标值，单位byte
        :rtype: float
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def IndexTraffic(self):
        """IndexTraffic指标值，单位byte
        :rtype: float
        """
        return self._IndexTraffic

    @IndexTraffic.setter
    def IndexTraffic(self, IndexTraffic):
        self._IndexTraffic = IndexTraffic

    @property
    def ReadReqTimes(self):
        """读请求数，单位次数
        :rtype: int
        """
        return self._ReadReqTimes

    @ReadReqTimes.setter
    def ReadReqTimes(self, ReadReqTimes):
        self._ReadReqTimes = ReadReqTimes

    @property
    def WriteReqTimes(self):
        """写请求数，单位次数
        :rtype: int
        """
        return self._WriteReqTimes

    @WriteReqTimes.setter
    def WriteReqTimes(self, WriteReqTimes):
        self._WriteReqTimes = WriteReqTimes

    @property
    def DocCount(self):
        """文档数量，单位个数
        :rtype: int
        """
        return self._DocCount

    @DocCount.setter
    def DocCount(self, DocCount):
        self._DocCount = DocCount

    @property
    def MetricMapList(self):
        """指标数据数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MetricMapByIndexId
        """
        return self._MetricMapList

    @MetricMapList.setter
    def MetricMapList(self, MetricMapList):
        self._MetricMapList = MetricMapList

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
        self._Storage = params.get("Storage")
        self._IndexTraffic = params.get("IndexTraffic")
        self._ReadReqTimes = params.get("ReadReqTimes")
        self._WriteReqTimes = params.get("WriteReqTimes")
        self._DocCount = params.get("DocCount")
        if params.get("MetricMapList") is not None:
            self._MetricMapList = []
            for item in params.get("MetricMapList"):
                obj = MetricMapByIndexId()
                obj._deserialize(item)
                self._MetricMapList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServerlessSpaceUserRequest(AbstractModel):
    """DescribeServerlessSpaceUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间的ID
        :type SpaceId: str
        :param _Offset: 游标
        :type Offset: int
        :param _Limit: 页条数
        :type Limit: int
        :param _UserNames: 用户名列表过滤
        :type UserNames: list of str
        :param _UserTypes: 用户类型
        :type UserTypes: list of int
        :param _PrivilegeTypes: 权限类型
        :type PrivilegeTypes: list of int
        """
        self._SpaceId = None
        self._Offset = None
        self._Limit = None
        self._UserNames = None
        self._UserTypes = None
        self._PrivilegeTypes = None

    @property
    def SpaceId(self):
        """空间的ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Offset(self):
        """游标
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def UserNames(self):
        """用户名列表过滤
        :rtype: list of str
        """
        return self._UserNames

    @UserNames.setter
    def UserNames(self, UserNames):
        self._UserNames = UserNames

    @property
    def UserTypes(self):
        """用户类型
        :rtype: list of int
        """
        return self._UserTypes

    @UserTypes.setter
    def UserTypes(self, UserTypes):
        self._UserTypes = UserTypes

    @property
    def PrivilegeTypes(self):
        """权限类型
        :rtype: list of int
        """
        return self._PrivilegeTypes

    @PrivilegeTypes.setter
    def PrivilegeTypes(self, PrivilegeTypes):
        self._PrivilegeTypes = PrivilegeTypes


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._UserNames = params.get("UserNames")
        self._UserTypes = params.get("UserTypes")
        self._PrivilegeTypes = params.get("PrivilegeTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerlessSpaceUserResponse(AbstractModel):
    """DescribeServerlessSpaceUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerlessSpaceUsers: 用户数组
        :type ServerlessSpaceUsers: list of ServerlessSpaceUser
        :param _TotalCount: 用户总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServerlessSpaceUsers = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ServerlessSpaceUsers(self):
        """用户数组
        :rtype: list of ServerlessSpaceUser
        """
        return self._ServerlessSpaceUsers

    @ServerlessSpaceUsers.setter
    def ServerlessSpaceUsers(self, ServerlessSpaceUsers):
        self._ServerlessSpaceUsers = ServerlessSpaceUsers

    @property
    def TotalCount(self):
        """用户总数
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
        if params.get("ServerlessSpaceUsers") is not None:
            self._ServerlessSpaceUsers = []
            for item in params.get("ServerlessSpaceUsers"):
                obj = ServerlessSpaceUser()
                obj._deserialize(item)
                self._ServerlessSpaceUsers.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeServerlessSpacesRequest(AbstractModel):
    """DescribeServerlessSpaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceIds: 过滤的空间ID
        :type SpaceIds: list of str
        :param _SpaceNames: 过滤的空间名
        :type SpaceNames: list of str
        :param _Order: 排序顺序，支持升序asc、降序desc
        :type Order: str
        :param _OrderBy: 排序字段，支持空间创建时间SpaceCreateTime
        :type OrderBy: str
        :param _VpcIds: vpcId信息数组
        :type VpcIds: list of str
        :param _Offset: 分页起始
        :type Offset: int
        :param _Limit: 分页条数
        :type Limit: int
        :param _TagList: 标签信息
        :type TagList: list of TagInfo
        """
        self._SpaceIds = None
        self._SpaceNames = None
        self._Order = None
        self._OrderBy = None
        self._VpcIds = None
        self._Offset = None
        self._Limit = None
        self._TagList = None

    @property
    def SpaceIds(self):
        """过滤的空间ID
        :rtype: list of str
        """
        return self._SpaceIds

    @SpaceIds.setter
    def SpaceIds(self, SpaceIds):
        self._SpaceIds = SpaceIds

    @property
    def SpaceNames(self):
        """过滤的空间名
        :rtype: list of str
        """
        return self._SpaceNames

    @SpaceNames.setter
    def SpaceNames(self, SpaceNames):
        self._SpaceNames = SpaceNames

    @property
    def Order(self):
        """排序顺序，支持升序asc、降序desc
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderBy(self):
        """排序字段，支持空间创建时间SpaceCreateTime
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def VpcIds(self):
        """vpcId信息数组
        :rtype: list of str
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def Offset(self):
        """分页起始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagList(self):
        """标签信息
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._SpaceIds = params.get("SpaceIds")
        self._SpaceNames = params.get("SpaceNames")
        self._Order = params.get("Order")
        self._OrderBy = params.get("OrderBy")
        self._VpcIds = params.get("VpcIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerlessSpacesResponse(AbstractModel):
    """DescribeServerlessSpaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ServerlessSpaces: Serverless空间信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerlessSpaces: list of ServerlessSpace
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ServerlessSpaces = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ServerlessSpaces(self):
        """Serverless空间信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ServerlessSpace
        """
        return self._ServerlessSpaces

    @ServerlessSpaces.setter
    def ServerlessSpaces(self, ServerlessSpaces):
        self._ServerlessSpaces = ServerlessSpaces

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
        if params.get("ServerlessSpaces") is not None:
            self._ServerlessSpaces = []
            for item in params.get("ServerlessSpaces"):
                obj = ServerlessSpace()
                obj._deserialize(item)
                self._ServerlessSpaces.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSpaceKibanaToolsRequest(AbstractModel):
    """DescribeSpaceKibanaTools请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: space的ID
        :type SpaceId: str
        """
        self._SpaceId = None

    @property
    def SpaceId(self):
        """space的ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpaceKibanaToolsResponse(AbstractModel):
    """DescribeSpaceKibanaTools返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KibanaToken: 该token用于登录内嵌kibana
        :type KibanaToken: str
        :param _ExpireTime: token的过期时间
        :type ExpireTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KibanaToken = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def KibanaToken(self):
        """该token用于登录内嵌kibana
        :rtype: str
        """
        return self._KibanaToken

    @KibanaToken.setter
    def KibanaToken(self, KibanaToken):
        self._KibanaToken = KibanaToken

    @property
    def ExpireTime(self):
        """token的过期时间
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

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
        self._KibanaToken = params.get("KibanaToken")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class DescribeUserCosSnapshotListRequest(AbstractModel):
    """DescribeUserCosSnapshotList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CosBucket: cos桶名
        :type CosBucket: str
        :param _BasePath: bucket 桶下的备份路径
        :type BasePath: str
        :param _ClusterInstanceId: 云上集群迁移集群名
        :type ClusterInstanceId: str
        """
        self._CosBucket = None
        self._BasePath = None
        self._ClusterInstanceId = None

    @property
    def CosBucket(self):
        """cos桶名
        :rtype: str
        """
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def BasePath(self):
        """bucket 桶下的备份路径
        :rtype: str
        """
        return self._BasePath

    @BasePath.setter
    def BasePath(self, BasePath):
        self._BasePath = BasePath

    @property
    def ClusterInstanceId(self):
        """云上集群迁移集群名
        :rtype: str
        """
        return self._ClusterInstanceId

    @ClusterInstanceId.setter
    def ClusterInstanceId(self, ClusterInstanceId):
        self._ClusterInstanceId = ClusterInstanceId


    def _deserialize(self, params):
        self._CosBucket = params.get("CosBucket")
        self._BasePath = params.get("BasePath")
        self._ClusterInstanceId = params.get("ClusterInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserCosSnapshotListResponse(AbstractModel):
    """DescribeUserCosSnapshotList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosSnapshotInfoList: cos 快照信息列表
        :type CosSnapshotInfoList: list of CosSnapShotInfo
        :param _TotalCount: cos 快照数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosSnapshotInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CosSnapshotInfoList(self):
        """cos 快照信息列表
        :rtype: list of CosSnapShotInfo
        """
        return self._CosSnapshotInfoList

    @CosSnapshotInfoList.setter
    def CosSnapshotInfoList(self, CosSnapshotInfoList):
        self._CosSnapshotInfoList = CosSnapshotInfoList

    @property
    def TotalCount(self):
        """cos 快照数量
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
        if params.get("CosSnapshotInfoList") is not None:
            self._CosSnapshotInfoList = []
            for item in params.get("CosSnapshotInfoList"):
                obj = CosSnapShotInfo()
                obj._deserialize(item)
                self._CosSnapshotInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeViewsRequest(AbstractModel):
    """DescribeViews请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群实例ID
        :rtype: str
        """
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
        


class DescribeViewsResponse(AbstractModel):
    """DescribeViews返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterView: 集群维度视图
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterView: :class:`tencentcloud.es.v20180416.models.ClusterView`
        :param _NodesView: 节点维度视图
注意：此字段可能返回 null，表示取不到有效值。
        :type NodesView: list of NodeView
        :param _KibanasView: Kibana维度视图
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanasView: list of KibanaView
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterView = None
        self._NodesView = None
        self._KibanasView = None
        self._RequestId = None

    @property
    def ClusterView(self):
        """集群维度视图
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.ClusterView`
        """
        return self._ClusterView

    @ClusterView.setter
    def ClusterView(self, ClusterView):
        self._ClusterView = ClusterView

    @property
    def NodesView(self):
        """节点维度视图
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of NodeView
        """
        return self._NodesView

    @NodesView.setter
    def NodesView(self, NodesView):
        self._NodesView = NodesView

    @property
    def KibanasView(self):
        """Kibana维度视图
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of KibanaView
        """
        return self._KibanasView

    @KibanasView.setter
    def KibanasView(self, KibanasView):
        self._KibanasView = KibanasView

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
        if params.get("ClusterView") is not None:
            self._ClusterView = ClusterView()
            self._ClusterView._deserialize(params.get("ClusterView"))
        if params.get("NodesView") is not None:
            self._NodesView = []
            for item in params.get("NodesView"):
                obj = NodeView()
                obj._deserialize(item)
                self._NodesView.append(obj)
        if params.get("KibanasView") is not None:
            self._KibanasView = []
            for item in params.get("KibanasView"):
                obj = KibanaView()
                obj._deserialize(item)
                self._KibanasView.append(obj)
        self._RequestId = params.get("RequestId")


class DiData(AbstractModel):
    """数据接入信息

    """

    def __init__(self):
        r"""
        :param _DiId: 数据接入id
注意：此字段可能返回 null，表示取不到有效值。
        :type DiId: str
        :param _CreateTime: 数据接入创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Status: 数据接入状态，0处理中，1正常，-2删除中，-3已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _DiDataSourceCvm: cvm数据源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DiDataSourceCvm: :class:`tencentcloud.es.v20180416.models.DiDataSourceCvm`
        :param _DiDataSourceTke: tke数据源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DiDataSourceTke: :class:`tencentcloud.es.v20180416.models.DiDataSourceTke`
        :param _DiDataSinkServerless: serverless目的端信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DiDataSinkServerless: :class:`tencentcloud.es.v20180416.models.DiDataSinkServerless`
        :param _DiDataSourceType: 数据接入类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiDataSourceType: str
        """
        self._DiId = None
        self._CreateTime = None
        self._Status = None
        self._DiDataSourceCvm = None
        self._DiDataSourceTke = None
        self._DiDataSinkServerless = None
        self._DiDataSourceType = None

    @property
    def DiId(self):
        """数据接入id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiId

    @DiId.setter
    def DiId(self, DiId):
        self._DiId = DiId

    @property
    def CreateTime(self):
        """数据接入创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        """数据接入状态，0处理中，1正常，-2删除中，-3已删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DiDataSourceCvm(self):
        """cvm数据源信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.DiDataSourceCvm`
        """
        return self._DiDataSourceCvm

    @DiDataSourceCvm.setter
    def DiDataSourceCvm(self, DiDataSourceCvm):
        self._DiDataSourceCvm = DiDataSourceCvm

    @property
    def DiDataSourceTke(self):
        """tke数据源信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.DiDataSourceTke`
        """
        return self._DiDataSourceTke

    @DiDataSourceTke.setter
    def DiDataSourceTke(self, DiDataSourceTke):
        self._DiDataSourceTke = DiDataSourceTke

    @property
    def DiDataSinkServerless(self):
        """serverless目的端信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.DiDataSinkServerless`
        """
        return self._DiDataSinkServerless

    @DiDataSinkServerless.setter
    def DiDataSinkServerless(self, DiDataSinkServerless):
        self._DiDataSinkServerless = DiDataSinkServerless

    @property
    def DiDataSourceType(self):
        """数据接入类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiDataSourceType

    @DiDataSourceType.setter
    def DiDataSourceType(self, DiDataSourceType):
        self._DiDataSourceType = DiDataSourceType


    def _deserialize(self, params):
        self._DiId = params.get("DiId")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        if params.get("DiDataSourceCvm") is not None:
            self._DiDataSourceCvm = DiDataSourceCvm()
            self._DiDataSourceCvm._deserialize(params.get("DiDataSourceCvm"))
        if params.get("DiDataSourceTke") is not None:
            self._DiDataSourceTke = DiDataSourceTke()
            self._DiDataSourceTke._deserialize(params.get("DiDataSourceTke"))
        if params.get("DiDataSinkServerless") is not None:
            self._DiDataSinkServerless = DiDataSinkServerless()
            self._DiDataSinkServerless._deserialize(params.get("DiDataSinkServerless"))
        self._DiDataSourceType = params.get("DiDataSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiDataSinkServerless(AbstractModel):
    """数据接入serverless目的端信息

    """

    def __init__(self):
        r"""
        :param _ServerlessId: serverless实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerlessId: str
        """
        self._ServerlessId = None

    @property
    def ServerlessId(self):
        """serverless实例id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServerlessId

    @ServerlessId.setter
    def ServerlessId(self, ServerlessId):
        self._ServerlessId = ServerlessId


    def _deserialize(self, params):
        self._ServerlessId = params.get("ServerlessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiDataSourceCvm(AbstractModel):
    """数据接入cvm数据源信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _LogPaths: 采集路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogPaths: list of str
        :param _CvmInstances: cvm实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmInstances: list of DiDataSourceCvmInstance
        :param _CollectorId: 采集器id
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectorId: str
        """
        self._VpcId = None
        self._LogPaths = None
        self._CvmInstances = None
        self._CollectorId = None

    @property
    def VpcId(self):
        """vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def LogPaths(self):
        """采集路径列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LogPaths

    @LogPaths.setter
    def LogPaths(self, LogPaths):
        self._LogPaths = LogPaths

    @property
    def CvmInstances(self):
        """cvm实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DiDataSourceCvmInstance
        """
        return self._CvmInstances

    @CvmInstances.setter
    def CvmInstances(self, CvmInstances):
        self._CvmInstances = CvmInstances

    @property
    def CollectorId(self):
        """采集器id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CollectorId

    @CollectorId.setter
    def CollectorId(self, CollectorId):
        self._CollectorId = CollectorId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._LogPaths = params.get("LogPaths")
        if params.get("CvmInstances") is not None:
            self._CvmInstances = []
            for item in params.get("CvmInstances"):
                obj = DiDataSourceCvmInstance()
                obj._deserialize(item)
                self._CvmInstances.append(obj)
        self._CollectorId = params.get("CollectorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiDataSourceCvmInstance(AbstractModel):
    """数据接入cvm实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: cvm实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._ErrMsg = None

    @property
    def InstanceId(self):
        """cvm实例id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VpcId(self):
        """vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ErrMsg(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiDataSourceTke(AbstractModel):
    """数据接入tke数据源信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _TkeId: tke实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type TkeId: str
        :param _CollectorId: 采集器id
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectorId: str
        :param _CollectorName: 采集源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectorName: str
        :param _CollectorType: 采集器类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectorType: str
        :param _CollectorVersion: 采集器版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectorVersion: str
        :param _IncludeNamespaces: tke包含的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeNamespaces: list of str
        :param _ExcludeNamespaces: tke不包含的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeNamespaces: list of str
        :param _PodLabelKeys: tke pod标签名
注意：此字段可能返回 null，表示取不到有效值。
        :type PodLabelKeys: list of str
        :param _PodLabelValues: tke pod标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type PodLabelValues: list of str
        :param _ContainerName: tke容器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerName: str
        :param _ConfigContent: tke采集器beat配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigContent: str
        :param _InputType: /
注意：此字段可能返回 null，表示取不到有效值。
        :type InputType: str
        :param _InputPath: TKE 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :type InputPath: str
        """
        self._VpcId = None
        self._TkeId = None
        self._CollectorId = None
        self._CollectorName = None
        self._CollectorType = None
        self._CollectorVersion = None
        self._IncludeNamespaces = None
        self._ExcludeNamespaces = None
        self._PodLabelKeys = None
        self._PodLabelValues = None
        self._ContainerName = None
        self._ConfigContent = None
        self._InputType = None
        self._InputPath = None

    @property
    def VpcId(self):
        """vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def TkeId(self):
        """tke实例id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TkeId

    @TkeId.setter
    def TkeId(self, TkeId):
        self._TkeId = TkeId

    @property
    def CollectorId(self):
        """采集器id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CollectorId

    @CollectorId.setter
    def CollectorId(self, CollectorId):
        self._CollectorId = CollectorId

    @property
    def CollectorName(self):
        """采集源名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CollectorName

    @CollectorName.setter
    def CollectorName(self, CollectorName):
        self._CollectorName = CollectorName

    @property
    def CollectorType(self):
        """采集器类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CollectorType

    @CollectorType.setter
    def CollectorType(self, CollectorType):
        self._CollectorType = CollectorType

    @property
    def CollectorVersion(self):
        """采集器版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CollectorVersion

    @CollectorVersion.setter
    def CollectorVersion(self, CollectorVersion):
        self._CollectorVersion = CollectorVersion

    @property
    def IncludeNamespaces(self):
        """tke包含的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._IncludeNamespaces

    @IncludeNamespaces.setter
    def IncludeNamespaces(self, IncludeNamespaces):
        self._IncludeNamespaces = IncludeNamespaces

    @property
    def ExcludeNamespaces(self):
        """tke不包含的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ExcludeNamespaces

    @ExcludeNamespaces.setter
    def ExcludeNamespaces(self, ExcludeNamespaces):
        self._ExcludeNamespaces = ExcludeNamespaces

    @property
    def PodLabelKeys(self):
        """tke pod标签名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._PodLabelKeys

    @PodLabelKeys.setter
    def PodLabelKeys(self, PodLabelKeys):
        self._PodLabelKeys = PodLabelKeys

    @property
    def PodLabelValues(self):
        """tke pod标签值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._PodLabelValues

    @PodLabelValues.setter
    def PodLabelValues(self, PodLabelValues):
        self._PodLabelValues = PodLabelValues

    @property
    def ContainerName(self):
        """tke容器名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def ConfigContent(self):
        """tke采集器beat配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigContent

    @ConfigContent.setter
    def ConfigContent(self, ConfigContent):
        self._ConfigContent = ConfigContent

    @property
    def InputType(self):
        """/
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def InputPath(self):
        """TKE 日志采集路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InputPath

    @InputPath.setter
    def InputPath(self, InputPath):
        self._InputPath = InputPath


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._TkeId = params.get("TkeId")
        self._CollectorId = params.get("CollectorId")
        self._CollectorName = params.get("CollectorName")
        self._CollectorType = params.get("CollectorType")
        self._CollectorVersion = params.get("CollectorVersion")
        self._IncludeNamespaces = params.get("IncludeNamespaces")
        self._ExcludeNamespaces = params.get("ExcludeNamespaces")
        self._PodLabelKeys = params.get("PodLabelKeys")
        self._PodLabelValues = params.get("PodLabelValues")
        self._ContainerName = params.get("ContainerName")
        self._ConfigContent = params.get("ConfigContent")
        self._InputType = params.get("InputType")
        self._InputPath = params.get("InputPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiSourceCvm(AbstractModel):
    """数据接入cvm数据源

    """

    def __init__(self):
        r"""
        :param _VpcId: 数据源所属vpc id，创建后不允许修改
        :type VpcId: str
        :param _CvmIds: cvm列表
        :type CvmIds: list of str
        :param _LogPaths: 采集路径列表，支持通配符
        :type LogPaths: list of str
        """
        self._VpcId = None
        self._CvmIds = None
        self._LogPaths = None

    @property
    def VpcId(self):
        """数据源所属vpc id，创建后不允许修改
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def CvmIds(self):
        """cvm列表
        :rtype: list of str
        """
        return self._CvmIds

    @CvmIds.setter
    def CvmIds(self, CvmIds):
        self._CvmIds = CvmIds

    @property
    def LogPaths(self):
        """采集路径列表，支持通配符
        :rtype: list of str
        """
        return self._LogPaths

    @LogPaths.setter
    def LogPaths(self, LogPaths):
        self._LogPaths = LogPaths


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._CvmIds = params.get("CvmIds")
        self._LogPaths = params.get("LogPaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiSourceTke(AbstractModel):
    """数据接入tke数据源

    """

    def __init__(self):
        r"""
        :param _VpcId: 数据源所属vpc id，创建后不允许修改
        :type VpcId: str
        :param _TkeId: tke实例id，创建后不允许修改
        :type TkeId: str
        :param _IncludeNamespaces: tke包含的命名空间
        :type IncludeNamespaces: list of str
        :param _ExcludeNamespaces: tke不包含的命名空间
        :type ExcludeNamespaces: list of str
        :param _ContainerName: tke容器名称
        :type ContainerName: str
        :param _LogFilters: tke日志内容过滤
        :type LogFilters: str
        :param _ConfigContent: tke beats配置项
        :type ConfigContent: str
        :param _PodLabel: tke pod标签
        :type PodLabel: list of DiSourceTkePodLabel
        :param _InputType: /
        :type InputType: str
        :param _InputPath: tke 日志采集路径
        :type InputPath: str
        """
        self._VpcId = None
        self._TkeId = None
        self._IncludeNamespaces = None
        self._ExcludeNamespaces = None
        self._ContainerName = None
        self._LogFilters = None
        self._ConfigContent = None
        self._PodLabel = None
        self._InputType = None
        self._InputPath = None

    @property
    def VpcId(self):
        """数据源所属vpc id，创建后不允许修改
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def TkeId(self):
        """tke实例id，创建后不允许修改
        :rtype: str
        """
        return self._TkeId

    @TkeId.setter
    def TkeId(self, TkeId):
        self._TkeId = TkeId

    @property
    def IncludeNamespaces(self):
        """tke包含的命名空间
        :rtype: list of str
        """
        return self._IncludeNamespaces

    @IncludeNamespaces.setter
    def IncludeNamespaces(self, IncludeNamespaces):
        self._IncludeNamespaces = IncludeNamespaces

    @property
    def ExcludeNamespaces(self):
        """tke不包含的命名空间
        :rtype: list of str
        """
        return self._ExcludeNamespaces

    @ExcludeNamespaces.setter
    def ExcludeNamespaces(self, ExcludeNamespaces):
        self._ExcludeNamespaces = ExcludeNamespaces

    @property
    def ContainerName(self):
        """tke容器名称
        :rtype: str
        """
        return self._ContainerName

    @ContainerName.setter
    def ContainerName(self, ContainerName):
        self._ContainerName = ContainerName

    @property
    def LogFilters(self):
        """tke日志内容过滤
        :rtype: str
        """
        return self._LogFilters

    @LogFilters.setter
    def LogFilters(self, LogFilters):
        self._LogFilters = LogFilters

    @property
    def ConfigContent(self):
        """tke beats配置项
        :rtype: str
        """
        return self._ConfigContent

    @ConfigContent.setter
    def ConfigContent(self, ConfigContent):
        self._ConfigContent = ConfigContent

    @property
    def PodLabel(self):
        """tke pod标签
        :rtype: list of DiSourceTkePodLabel
        """
        return self._PodLabel

    @PodLabel.setter
    def PodLabel(self, PodLabel):
        self._PodLabel = PodLabel

    @property
    def InputType(self):
        """/
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def InputPath(self):
        """tke 日志采集路径
        :rtype: str
        """
        return self._InputPath

    @InputPath.setter
    def InputPath(self, InputPath):
        self._InputPath = InputPath


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._TkeId = params.get("TkeId")
        self._IncludeNamespaces = params.get("IncludeNamespaces")
        self._ExcludeNamespaces = params.get("ExcludeNamespaces")
        self._ContainerName = params.get("ContainerName")
        self._LogFilters = params.get("LogFilters")
        self._ConfigContent = params.get("ConfigContent")
        if params.get("PodLabel") is not None:
            self._PodLabel = []
            for item in params.get("PodLabel"):
                obj = DiSourceTkePodLabel()
                obj._deserialize(item)
                self._PodLabel.append(obj)
        self._InputType = params.get("InputType")
        self._InputPath = params.get("InputPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiSourceTkePodLabel(AbstractModel):
    """tke pod标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 标签value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """标签key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签value
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
        


class DiagnoseInstanceRequest(AbstractModel):
    """DiagnoseInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES实例ID
        :type InstanceId: str
        :param _DiagnoseJobs: 需要触发的诊断项
        :type DiagnoseJobs: list of str
        :param _DiagnoseIndices: 需要诊断的索引，支持通配符
        :type DiagnoseIndices: str
        """
        self._InstanceId = None
        self._DiagnoseJobs = None
        self._DiagnoseIndices = None

    @property
    def InstanceId(self):
        """ES实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiagnoseJobs(self):
        """需要触发的诊断项
        :rtype: list of str
        """
        return self._DiagnoseJobs

    @DiagnoseJobs.setter
    def DiagnoseJobs(self, DiagnoseJobs):
        self._DiagnoseJobs = DiagnoseJobs

    @property
    def DiagnoseIndices(self):
        """需要诊断的索引，支持通配符
        :rtype: str
        """
        return self._DiagnoseIndices

    @DiagnoseIndices.setter
    def DiagnoseIndices(self, DiagnoseIndices):
        self._DiagnoseIndices = DiagnoseIndices


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DiagnoseJobs = params.get("DiagnoseJobs")
        self._DiagnoseIndices = params.get("DiagnoseIndices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseInstanceResponse(AbstractModel):
    """DiagnoseInstance返回参数结构体

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


class DiagnoseJobMeta(AbstractModel):
    """智能运维支持的诊断项和元信息

    """

    def __init__(self):
        r"""
        :param _JobName: 智能运维诊断项英文名
        :type JobName: str
        :param _JobZhName: 智能运维诊断项中文名
        :type JobZhName: str
        :param _JobDescription: 智能运维诊断项描述
        :type JobDescription: str
        """
        self._JobName = None
        self._JobZhName = None
        self._JobDescription = None

    @property
    def JobName(self):
        """智能运维诊断项英文名
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobZhName(self):
        """智能运维诊断项中文名
        :rtype: str
        """
        return self._JobZhName

    @JobZhName.setter
    def JobZhName(self, JobZhName):
        self._JobZhName = JobZhName

    @property
    def JobDescription(self):
        """智能运维诊断项描述
        :rtype: str
        """
        return self._JobDescription

    @JobDescription.setter
    def JobDescription(self, JobDescription):
        self._JobDescription = JobDescription


    def _deserialize(self, params):
        self._JobName = params.get("JobName")
        self._JobZhName = params.get("JobZhName")
        self._JobDescription = params.get("JobDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseJobResult(AbstractModel):
    """智能运维诊断项结果

    """

    def __init__(self):
        r"""
        :param _JobName: 诊断项名
        :type JobName: str
        :param _Status: 诊断项状态：-2失败，-1待重试，0运行中，1成功
        :type Status: int
        :param _Score: 诊断项得分
        :type Score: int
        :param _Summary: 诊断摘要
        :type Summary: str
        :param _Advise: 诊断建议
        :type Advise: str
        :param _Detail: 诊断详情
        :type Detail: str
        :param _MetricDetails: 诊断指标详情
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricDetails: list of MetricDetail
        :param _LogDetails: 诊断日志详情
注意：此字段可能返回 null，表示取不到有效值。
        :type LogDetails: list of LogDetail
        :param _SettingDetails: 诊断配置详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SettingDetails: list of SettingDetail
        """
        self._JobName = None
        self._Status = None
        self._Score = None
        self._Summary = None
        self._Advise = None
        self._Detail = None
        self._MetricDetails = None
        self._LogDetails = None
        self._SettingDetails = None

    @property
    def JobName(self):
        """诊断项名
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Status(self):
        """诊断项状态：-2失败，-1待重试，0运行中，1成功
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Score(self):
        """诊断项得分
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Summary(self):
        """诊断摘要
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def Advise(self):
        """诊断建议
        :rtype: str
        """
        return self._Advise

    @Advise.setter
    def Advise(self, Advise):
        self._Advise = Advise

    @property
    def Detail(self):
        """诊断详情
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def MetricDetails(self):
        """诊断指标详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MetricDetail
        """
        return self._MetricDetails

    @MetricDetails.setter
    def MetricDetails(self, MetricDetails):
        self._MetricDetails = MetricDetails

    @property
    def LogDetails(self):
        """诊断日志详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogDetail
        """
        return self._LogDetails

    @LogDetails.setter
    def LogDetails(self, LogDetails):
        self._LogDetails = LogDetails

    @property
    def SettingDetails(self):
        """诊断配置详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SettingDetail
        """
        return self._SettingDetails

    @SettingDetails.setter
    def SettingDetails(self, SettingDetails):
        self._SettingDetails = SettingDetails


    def _deserialize(self, params):
        self._JobName = params.get("JobName")
        self._Status = params.get("Status")
        self._Score = params.get("Score")
        self._Summary = params.get("Summary")
        self._Advise = params.get("Advise")
        self._Detail = params.get("Detail")
        if params.get("MetricDetails") is not None:
            self._MetricDetails = []
            for item in params.get("MetricDetails"):
                obj = MetricDetail()
                obj._deserialize(item)
                self._MetricDetails.append(obj)
        if params.get("LogDetails") is not None:
            self._LogDetails = []
            for item in params.get("LogDetails"):
                obj = LogDetail()
                obj._deserialize(item)
                self._LogDetails.append(obj)
        if params.get("SettingDetails") is not None:
            self._SettingDetails = []
            for item in params.get("SettingDetails"):
                obj = SettingDetail()
                obj._deserialize(item)
                self._SettingDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseResult(AbstractModel):
    """智能运维诊断结果

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES实例ID
        :type InstanceId: str
        :param _RequestId: 诊断报告ID
        :type RequestId: str
        :param _CreateTime: 诊断触发时间
        :type CreateTime: str
        :param _Completed: 诊断是否完成
        :type Completed: bool
        :param _Score: 诊断总得分
        :type Score: int
        :param _JobType: 诊断类型，2 定时诊断，3 客户手动触发诊断
        :type JobType: int
        :param _JobParam: 诊断参数，如诊断时间，诊断索引等
        :type JobParam: :class:`tencentcloud.es.v20180416.models.JobParam`
        :param _JobResults: 诊断项结果列表
        :type JobResults: list of DiagnoseJobResult
        """
        self._InstanceId = None
        self._RequestId = None
        self._CreateTime = None
        self._Completed = None
        self._Score = None
        self._JobType = None
        self._JobParam = None
        self._JobResults = None

    @property
    def InstanceId(self):
        """ES实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        """诊断报告ID
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def CreateTime(self):
        """诊断触发时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Completed(self):
        """诊断是否完成
        :rtype: bool
        """
        return self._Completed

    @Completed.setter
    def Completed(self, Completed):
        self._Completed = Completed

    @property
    def Score(self):
        """诊断总得分
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def JobType(self):
        """诊断类型，2 定时诊断，3 客户手动触发诊断
        :rtype: int
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def JobParam(self):
        """诊断参数，如诊断时间，诊断索引等
        :rtype: :class:`tencentcloud.es.v20180416.models.JobParam`
        """
        return self._JobParam

    @JobParam.setter
    def JobParam(self, JobParam):
        self._JobParam = JobParam

    @property
    def JobResults(self):
        """诊断项结果列表
        :rtype: list of DiagnoseJobResult
        """
        return self._JobResults

    @JobResults.setter
    def JobResults(self, JobResults):
        self._JobResults = JobResults


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")
        self._CreateTime = params.get("CreateTime")
        self._Completed = params.get("Completed")
        self._Score = params.get("Score")
        self._JobType = params.get("JobType")
        if params.get("JobParam") is not None:
            self._JobParam = JobParam()
            self._JobParam._deserialize(params.get("JobParam"))
        if params.get("JobResults") is not None:
            self._JobResults = []
            for item in params.get("JobResults"):
                obj = DiagnoseJobResult()
                obj._deserialize(item)
                self._JobResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DictInfo(AbstractModel):
    """ik插件词典信息

    """

    def __init__(self):
        r"""
        :param _Key: 词典键值
        :type Key: str
        :param _Name: 词典名称
        :type Name: str
        :param _Size: 词典大小，单位B
        :type Size: int
        """
        self._Key = None
        self._Name = None
        self._Size = None

    @property
    def Key(self):
        """词典键值
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Name(self):
        """词典名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        """词典大小，单位B
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Dimension(AbstractModel):
    """智能运维指标维度

    """

    def __init__(self):
        r"""
        :param _Key: 智能运维指标维度Key
        :type Key: str
        :param _Value: 智能运维指标维度值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """智能运维指标维度Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """智能运维指标维度值
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
        


class EnableScheduleOperationDuration(AbstractModel):
    """置放群组异步任务维护的时间段

    """

    def __init__(self):
        r"""
        :param _Periods: 支持开启异步任务的日期
注意：此字段可能返回 null，表示取不到有效值。
        :type Periods: list of str
        :param _TimeStart: 支持开启异步的开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeStart: str
        :param _TimeEnd: 支持开启异步的结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeEnd: str
        :param _TimeZone: 支持开启异步的时区
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeZone: str
        """
        self._Periods = None
        self._TimeStart = None
        self._TimeEnd = None
        self._TimeZone = None

    @property
    def Periods(self):
        """支持开启异步任务的日期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def TimeStart(self):
        """支持开启异步的开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeStart

    @TimeStart.setter
    def TimeStart(self, TimeStart):
        self._TimeStart = TimeStart

    @property
    def TimeEnd(self):
        """支持开启异步的结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def TimeZone(self):
        """支持开启异步的时区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Periods = params.get("Periods")
        self._TimeStart = params.get("TimeStart")
        self._TimeEnd = params.get("TimeEnd")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsAcl(AbstractModel):
    """ES集群配置项

    """

    def __init__(self):
        r"""
        :param _BlackIpList: kibana访问黑名单
        :type BlackIpList: list of str
        :param _WhiteIpList: kibana访问白名单
        :type WhiteIpList: list of str
        """
        self._BlackIpList = None
        self._WhiteIpList = None

    @property
    def BlackIpList(self):
        """kibana访问黑名单
        :rtype: list of str
        """
        return self._BlackIpList

    @BlackIpList.setter
    def BlackIpList(self, BlackIpList):
        self._BlackIpList = BlackIpList

    @property
    def WhiteIpList(self):
        """kibana访问白名单
        :rtype: list of str
        """
        return self._WhiteIpList

    @WhiteIpList.setter
    def WhiteIpList(self, WhiteIpList):
        self._WhiteIpList = WhiteIpList


    def _deserialize(self, params):
        self._BlackIpList = params.get("BlackIpList")
        self._WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsConfigSetInfo(AbstractModel):
    """配置组信息

    """

    def __init__(self):
        r"""
        :param _Type: 配置组类型，如ldap,ad等
        :type Type: str
        :param _EsConfig: "{\"order\":0,\"url\":\"ldap://10.0.1.72:389\",\"bind_dn\":\"cn=admin,dc=tencent,dc=com\",\"user_search.base_dn\":\"dc=tencent,dc=com\",\"user_search.filter\":\"(cn={0})\",\"group_search.base_dn\":\"dc=tencent,dc=com\"}"
        :type EsConfig: str
        """
        self._Type = None
        self._EsConfig = None

    @property
    def Type(self):
        """配置组类型，如ldap,ad等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EsConfig(self):
        """"{\"order\":0,\"url\":\"ldap://10.0.1.72:389\",\"bind_dn\":\"cn=admin,dc=tencent,dc=com\",\"user_search.base_dn\":\"dc=tencent,dc=com\",\"user_search.filter\":\"(cn={0})\",\"group_search.base_dn\":\"dc=tencent,dc=com\"}"
        :rtype: str
        """
        return self._EsConfig

    @EsConfig.setter
    def EsConfig(self, EsConfig):
        self._EsConfig = EsConfig


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._EsConfig = params.get("EsConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsDictionaryInfo(AbstractModel):
    """ES 词库信息

    """

    def __init__(self):
        r"""
        :param _MainDict: 启用词词典列表
        :type MainDict: list of DictInfo
        :param _Stopwords: 停用词词典列表
        :type Stopwords: list of DictInfo
        :param _QQDict: QQ分词词典列表
        :type QQDict: list of DictInfo
        :param _Synonym: 同义词词典列表
        :type Synonym: list of DictInfo
        :param _UpdateType: 更新词典类型
        :type UpdateType: str
        :param _AnsjMain: ansj启用词词典列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AnsjMain: list of DictInfo
        :param _AnsjStop: ansj停用词词典列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AnsjStop: list of DictInfo
        :param _AnsjAmbiguity: ansj歧义词库列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AnsjAmbiguity: list of DictInfo
        :param _AnsjSynonyms: ansj同义词词典列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AnsjSynonyms: list of DictInfo
        """
        self._MainDict = None
        self._Stopwords = None
        self._QQDict = None
        self._Synonym = None
        self._UpdateType = None
        self._AnsjMain = None
        self._AnsjStop = None
        self._AnsjAmbiguity = None
        self._AnsjSynonyms = None

    @property
    def MainDict(self):
        """启用词词典列表
        :rtype: list of DictInfo
        """
        return self._MainDict

    @MainDict.setter
    def MainDict(self, MainDict):
        self._MainDict = MainDict

    @property
    def Stopwords(self):
        """停用词词典列表
        :rtype: list of DictInfo
        """
        return self._Stopwords

    @Stopwords.setter
    def Stopwords(self, Stopwords):
        self._Stopwords = Stopwords

    @property
    def QQDict(self):
        """QQ分词词典列表
        :rtype: list of DictInfo
        """
        return self._QQDict

    @QQDict.setter
    def QQDict(self, QQDict):
        self._QQDict = QQDict

    @property
    def Synonym(self):
        """同义词词典列表
        :rtype: list of DictInfo
        """
        return self._Synonym

    @Synonym.setter
    def Synonym(self, Synonym):
        self._Synonym = Synonym

    @property
    def UpdateType(self):
        """更新词典类型
        :rtype: str
        """
        return self._UpdateType

    @UpdateType.setter
    def UpdateType(self, UpdateType):
        self._UpdateType = UpdateType

    @property
    def AnsjMain(self):
        """ansj启用词词典列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DictInfo
        """
        return self._AnsjMain

    @AnsjMain.setter
    def AnsjMain(self, AnsjMain):
        self._AnsjMain = AnsjMain

    @property
    def AnsjStop(self):
        """ansj停用词词典列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DictInfo
        """
        return self._AnsjStop

    @AnsjStop.setter
    def AnsjStop(self, AnsjStop):
        self._AnsjStop = AnsjStop

    @property
    def AnsjAmbiguity(self):
        """ansj歧义词库列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DictInfo
        """
        return self._AnsjAmbiguity

    @AnsjAmbiguity.setter
    def AnsjAmbiguity(self, AnsjAmbiguity):
        self._AnsjAmbiguity = AnsjAmbiguity

    @property
    def AnsjSynonyms(self):
        """ansj同义词词典列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DictInfo
        """
        return self._AnsjSynonyms

    @AnsjSynonyms.setter
    def AnsjSynonyms(self, AnsjSynonyms):
        self._AnsjSynonyms = AnsjSynonyms


    def _deserialize(self, params):
        if params.get("MainDict") is not None:
            self._MainDict = []
            for item in params.get("MainDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self._MainDict.append(obj)
        if params.get("Stopwords") is not None:
            self._Stopwords = []
            for item in params.get("Stopwords"):
                obj = DictInfo()
                obj._deserialize(item)
                self._Stopwords.append(obj)
        if params.get("QQDict") is not None:
            self._QQDict = []
            for item in params.get("QQDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self._QQDict.append(obj)
        if params.get("Synonym") is not None:
            self._Synonym = []
            for item in params.get("Synonym"):
                obj = DictInfo()
                obj._deserialize(item)
                self._Synonym.append(obj)
        self._UpdateType = params.get("UpdateType")
        if params.get("AnsjMain") is not None:
            self._AnsjMain = []
            for item in params.get("AnsjMain"):
                obj = DictInfo()
                obj._deserialize(item)
                self._AnsjMain.append(obj)
        if params.get("AnsjStop") is not None:
            self._AnsjStop = []
            for item in params.get("AnsjStop"):
                obj = DictInfo()
                obj._deserialize(item)
                self._AnsjStop.append(obj)
        if params.get("AnsjAmbiguity") is not None:
            self._AnsjAmbiguity = []
            for item in params.get("AnsjAmbiguity"):
                obj = DictInfo()
                obj._deserialize(item)
                self._AnsjAmbiguity.append(obj)
        if params.get("AnsjSynonyms") is not None:
            self._AnsjSynonyms = []
            for item in params.get("AnsjSynonyms"):
                obj = DictInfo()
                obj._deserialize(item)
                self._AnsjSynonyms.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsPublicAcl(AbstractModel):
    """ES公网访问控制信息

    """

    def __init__(self):
        r"""
        :param _BlackIpList: 访问黑名单
        :type BlackIpList: list of str
        :param _WhiteIpList: 访问白名单
        :type WhiteIpList: list of str
        """
        self._BlackIpList = None
        self._WhiteIpList = None

    @property
    def BlackIpList(self):
        """访问黑名单
        :rtype: list of str
        """
        return self._BlackIpList

    @BlackIpList.setter
    def BlackIpList(self, BlackIpList):
        self._BlackIpList = BlackIpList

    @property
    def WhiteIpList(self):
        """访问白名单
        :rtype: list of str
        """
        return self._WhiteIpList

    @WhiteIpList.setter
    def WhiteIpList(self, WhiteIpList):
        self._WhiteIpList = WhiteIpList


    def _deserialize(self, params):
        self._BlackIpList = params.get("BlackIpList")
        self._WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Failures(AbstractModel):
    """索引备份失败的数据结构

    """

    def __init__(self):
        r"""
        :param _Index: 备份失败的索引名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: str
        :param _ShardId: 快照失败的分片号
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardId: int
        :param _Reason: 快照失败的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param _Status: 快照失败的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._Index = None
        self._ShardId = None
        self._Reason = None
        self._Status = None

    @property
    def Index(self):
        """备份失败的索引名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def ShardId(self):
        """快照失败的分片号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def Reason(self):
        """快照失败的原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Status(self):
        """快照失败的状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._ShardId = params.get("ShardId")
        self._Reason = params.get("Reason")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDiagnoseSettingsRequest(AbstractModel):
    """GetDiagnoseSettings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """ES实例ID
        :rtype: str
        """
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
        


class GetDiagnoseSettingsResponse(AbstractModel):
    """GetDiagnoseSettings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiagnoseJobMetas: 智能运维诊断项和元信息
        :type DiagnoseJobMetas: list of DiagnoseJobMeta
        :param _Status: 0：开启智能运维；-1：关闭智能运维
        :type Status: int
        :param _CronTime: 智能运维每天定时巡检时间
        :type CronTime: str
        :param _Count: 智能运维当天已手动触发诊断次数
        :type Count: int
        :param _MaxCount: 智能运维每天最大可手动触发次数
        :type MaxCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiagnoseJobMetas = None
        self._Status = None
        self._CronTime = None
        self._Count = None
        self._MaxCount = None
        self._RequestId = None

    @property
    def DiagnoseJobMetas(self):
        """智能运维诊断项和元信息
        :rtype: list of DiagnoseJobMeta
        """
        return self._DiagnoseJobMetas

    @DiagnoseJobMetas.setter
    def DiagnoseJobMetas(self, DiagnoseJobMetas):
        self._DiagnoseJobMetas = DiagnoseJobMetas

    @property
    def Status(self):
        """0：开启智能运维；-1：关闭智能运维
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CronTime(self):
        """智能运维每天定时巡检时间
        :rtype: str
        """
        return self._CronTime

    @CronTime.setter
    def CronTime(self, CronTime):
        self._CronTime = CronTime

    @property
    def Count(self):
        """智能运维当天已手动触发诊断次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def MaxCount(self):
        """智能运维每天最大可手动触发次数
        :rtype: int
        """
        return self._MaxCount

    @MaxCount.setter
    def MaxCount(self, MaxCount):
        self._MaxCount = MaxCount

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
        if params.get("DiagnoseJobMetas") is not None:
            self._DiagnoseJobMetas = []
            for item in params.get("DiagnoseJobMetas"):
                obj = DiagnoseJobMeta()
                obj._deserialize(item)
                self._DiagnoseJobMetas.append(obj)
        self._Status = params.get("Status")
        self._CronTime = params.get("CronTime")
        self._Count = params.get("Count")
        self._MaxCount = params.get("MaxCount")
        self._RequestId = params.get("RequestId")


class GetRequestTargetNodeTypesRequest(AbstractModel):
    """GetRequestTargetNodeTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
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
        


class GetRequestTargetNodeTypesResponse(AbstractModel):
    """GetRequestTargetNodeTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetNodeTypes: 接收请求的目标节点类型列表
        :type TargetNodeTypes: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TargetNodeTypes = None
        self._RequestId = None

    @property
    def TargetNodeTypes(self):
        """接收请求的目标节点类型列表
        :rtype: list of str
        """
        return self._TargetNodeTypes

    @TargetNodeTypes.setter
    def TargetNodeTypes(self, TargetNodeTypes):
        self._TargetNodeTypes = TargetNodeTypes

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
        self._TargetNodeTypes = params.get("TargetNodeTypes")
        self._RequestId = params.get("RequestId")


class IndexMetaField(AbstractModel):
    """索引元数据字段

    """

    def __init__(self):
        r"""
        :param _IndexType: 索引类型
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexType: str
        :param _IndexName: 索引名
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexName: str
        :param _IndexMetaJson: 索引元数据JSON
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexMetaJson: str
        :param _IndexStatus: 索引状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStatus: str
        :param _IndexStorage: 索引存储大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStorage: int
        :param _IndexCreateTime: 索引创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexCreateTime: str
        :param _BackingIndices: 后备索引
注意：此字段可能返回 null，表示取不到有效值。
        :type BackingIndices: list of BackingIndexMetaField
        :param _ClusterId: 索引所属集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 索引所属集群名
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _ClusterVersion: 索引所属集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterVersion: str
        :param _IndexPolicyField: 索引生命周期字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexPolicyField: :class:`tencentcloud.es.v20180416.models.IndexPolicyField`
        :param _IndexOptionsField: 索引自治字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexOptionsField: :class:`tencentcloud.es.v20180416.models.IndexOptionsField`
        :param _IndexSettingsField: 索引配置字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexSettingsField: :class:`tencentcloud.es.v20180416.models.IndexSettingsField`
        :param _IndexAliasesField: 索引别名字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexAliasesField: list of str
        :param _AppId: 索引所属集群APP ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _IndexDocs: 索引文档数
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexDocs: int
        """
        self._IndexType = None
        self._IndexName = None
        self._IndexMetaJson = None
        self._IndexStatus = None
        self._IndexStorage = None
        self._IndexCreateTime = None
        self._BackingIndices = None
        self._ClusterId = None
        self._ClusterName = None
        self._ClusterVersion = None
        self._IndexPolicyField = None
        self._IndexOptionsField = None
        self._IndexSettingsField = None
        self._IndexAliasesField = None
        self._AppId = None
        self._IndexDocs = None

    @property
    def IndexType(self):
        """索引类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        """索引名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IndexMetaJson(self):
        """索引元数据JSON
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexMetaJson

    @IndexMetaJson.setter
    def IndexMetaJson(self, IndexMetaJson):
        self._IndexMetaJson = IndexMetaJson

    @property
    def IndexStatus(self):
        """索引状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus

    @property
    def IndexStorage(self):
        """索引存储大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IndexStorage

    @IndexStorage.setter
    def IndexStorage(self, IndexStorage):
        self._IndexStorage = IndexStorage

    @property
    def IndexCreateTime(self):
        """索引创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexCreateTime

    @IndexCreateTime.setter
    def IndexCreateTime(self, IndexCreateTime):
        self._IndexCreateTime = IndexCreateTime

    @property
    def BackingIndices(self):
        """后备索引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BackingIndexMetaField
        """
        return self._BackingIndices

    @BackingIndices.setter
    def BackingIndices(self, BackingIndices):
        self._BackingIndices = BackingIndices

    @property
    def ClusterId(self):
        """索引所属集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """索引所属集群名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterVersion(self):
        """索引所属集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def IndexPolicyField(self):
        """索引生命周期字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexPolicyField`
        """
        return self._IndexPolicyField

    @IndexPolicyField.setter
    def IndexPolicyField(self, IndexPolicyField):
        self._IndexPolicyField = IndexPolicyField

    @property
    def IndexOptionsField(self):
        """索引自治字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexOptionsField`
        """
        return self._IndexOptionsField

    @IndexOptionsField.setter
    def IndexOptionsField(self, IndexOptionsField):
        self._IndexOptionsField = IndexOptionsField

    @property
    def IndexSettingsField(self):
        """索引配置字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.IndexSettingsField`
        """
        return self._IndexSettingsField

    @IndexSettingsField.setter
    def IndexSettingsField(self, IndexSettingsField):
        self._IndexSettingsField = IndexSettingsField

    @property
    def IndexAliasesField(self):
        """索引别名字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._IndexAliasesField

    @IndexAliasesField.setter
    def IndexAliasesField(self, IndexAliasesField):
        self._IndexAliasesField = IndexAliasesField

    @property
    def AppId(self):
        """索引所属集群APP ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def IndexDocs(self):
        """索引文档数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IndexDocs

    @IndexDocs.setter
    def IndexDocs(self, IndexDocs):
        self._IndexDocs = IndexDocs


    def _deserialize(self, params):
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._IndexMetaJson = params.get("IndexMetaJson")
        self._IndexStatus = params.get("IndexStatus")
        self._IndexStorage = params.get("IndexStorage")
        self._IndexCreateTime = params.get("IndexCreateTime")
        if params.get("BackingIndices") is not None:
            self._BackingIndices = []
            for item in params.get("BackingIndices"):
                obj = BackingIndexMetaField()
                obj._deserialize(item)
                self._BackingIndices.append(obj)
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._ClusterVersion = params.get("ClusterVersion")
        if params.get("IndexPolicyField") is not None:
            self._IndexPolicyField = IndexPolicyField()
            self._IndexPolicyField._deserialize(params.get("IndexPolicyField"))
        if params.get("IndexOptionsField") is not None:
            self._IndexOptionsField = IndexOptionsField()
            self._IndexOptionsField._deserialize(params.get("IndexOptionsField"))
        if params.get("IndexSettingsField") is not None:
            self._IndexSettingsField = IndexSettingsField()
            self._IndexSettingsField._deserialize(params.get("IndexSettingsField"))
        self._IndexAliasesField = params.get("IndexAliasesField")
        self._AppId = params.get("AppId")
        self._IndexDocs = params.get("IndexDocs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexOptionsField(AbstractModel):
    """索引自治字段

    """

    def __init__(self):
        r"""
        :param _ExpireMaxAge: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireMaxAge: str
        :param _ExpireMaxSize: 过期大小
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireMaxSize: str
        :param _RolloverMaxAge: 滚动周期
注意：此字段可能返回 null，表示取不到有效值。
        :type RolloverMaxAge: str
        :param _RolloverDynamic: 是否开启动态滚动
注意：此字段可能返回 null，表示取不到有效值。
        :type RolloverDynamic: str
        :param _ShardNumDynamic: 是否开启动态分片
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardNumDynamic: str
        :param _TimestampField: 时间分区字段
注意：此字段可能返回 null，表示取不到有效值。
        :type TimestampField: str
        :param _WriteMode: 写入模式
注意：此字段可能返回 null，表示取不到有效值。
        :type WriteMode: str
        """
        self._ExpireMaxAge = None
        self._ExpireMaxSize = None
        self._RolloverMaxAge = None
        self._RolloverDynamic = None
        self._ShardNumDynamic = None
        self._TimestampField = None
        self._WriteMode = None

    @property
    def ExpireMaxAge(self):
        """过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireMaxAge

    @ExpireMaxAge.setter
    def ExpireMaxAge(self, ExpireMaxAge):
        self._ExpireMaxAge = ExpireMaxAge

    @property
    def ExpireMaxSize(self):
        """过期大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireMaxSize

    @ExpireMaxSize.setter
    def ExpireMaxSize(self, ExpireMaxSize):
        self._ExpireMaxSize = ExpireMaxSize

    @property
    def RolloverMaxAge(self):
        """滚动周期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RolloverMaxAge

    @RolloverMaxAge.setter
    def RolloverMaxAge(self, RolloverMaxAge):
        self._RolloverMaxAge = RolloverMaxAge

    @property
    def RolloverDynamic(self):
        """是否开启动态滚动
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RolloverDynamic

    @RolloverDynamic.setter
    def RolloverDynamic(self, RolloverDynamic):
        self._RolloverDynamic = RolloverDynamic

    @property
    def ShardNumDynamic(self):
        """是否开启动态分片
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ShardNumDynamic

    @ShardNumDynamic.setter
    def ShardNumDynamic(self, ShardNumDynamic):
        self._ShardNumDynamic = ShardNumDynamic

    @property
    def TimestampField(self):
        """时间分区字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimestampField

    @TimestampField.setter
    def TimestampField(self, TimestampField):
        self._TimestampField = TimestampField

    @property
    def WriteMode(self):
        """写入模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WriteMode

    @WriteMode.setter
    def WriteMode(self, WriteMode):
        self._WriteMode = WriteMode


    def _deserialize(self, params):
        self._ExpireMaxAge = params.get("ExpireMaxAge")
        self._ExpireMaxSize = params.get("ExpireMaxSize")
        self._RolloverMaxAge = params.get("RolloverMaxAge")
        self._RolloverDynamic = params.get("RolloverDynamic")
        self._ShardNumDynamic = params.get("ShardNumDynamic")
        self._TimestampField = params.get("TimestampField")
        self._WriteMode = params.get("WriteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexPolicyField(AbstractModel):
    """索引生命周期字段

    """

    def __init__(self):
        r"""
        :param _WarmEnable: 是否开启warm阶段
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmEnable: str
        :param _WarmMinAge: warm阶段转入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmMinAge: str
        :param _ColdEnable: 是否开启cold阶段
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdEnable: str
        :param _ColdMinAge: cold阶段转入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdMinAge: str
        :param _FrozenEnable: 是否开启frozen阶段
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenEnable: str
        :param _FrozenMinAge: frozen阶段转入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenMinAge: str
        :param _ColdAction: /
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdAction: str
        """
        self._WarmEnable = None
        self._WarmMinAge = None
        self._ColdEnable = None
        self._ColdMinAge = None
        self._FrozenEnable = None
        self._FrozenMinAge = None
        self._ColdAction = None

    @property
    def WarmEnable(self):
        """是否开启warm阶段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WarmEnable

    @WarmEnable.setter
    def WarmEnable(self, WarmEnable):
        self._WarmEnable = WarmEnable

    @property
    def WarmMinAge(self):
        """warm阶段转入时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WarmMinAge

    @WarmMinAge.setter
    def WarmMinAge(self, WarmMinAge):
        self._WarmMinAge = WarmMinAge

    @property
    def ColdEnable(self):
        """是否开启cold阶段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ColdEnable

    @ColdEnable.setter
    def ColdEnable(self, ColdEnable):
        self._ColdEnable = ColdEnable

    @property
    def ColdMinAge(self):
        """cold阶段转入时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ColdMinAge

    @ColdMinAge.setter
    def ColdMinAge(self, ColdMinAge):
        self._ColdMinAge = ColdMinAge

    @property
    def FrozenEnable(self):
        """是否开启frozen阶段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FrozenEnable

    @FrozenEnable.setter
    def FrozenEnable(self, FrozenEnable):
        self._FrozenEnable = FrozenEnable

    @property
    def FrozenMinAge(self):
        """frozen阶段转入时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FrozenMinAge

    @FrozenMinAge.setter
    def FrozenMinAge(self, FrozenMinAge):
        self._FrozenMinAge = FrozenMinAge

    @property
    def ColdAction(self):
        """/
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ColdAction

    @ColdAction.setter
    def ColdAction(self, ColdAction):
        self._ColdAction = ColdAction


    def _deserialize(self, params):
        self._WarmEnable = params.get("WarmEnable")
        self._WarmMinAge = params.get("WarmMinAge")
        self._ColdEnable = params.get("ColdEnable")
        self._ColdMinAge = params.get("ColdMinAge")
        self._FrozenEnable = params.get("FrozenEnable")
        self._FrozenMinAge = params.get("FrozenMinAge")
        self._ColdAction = params.get("ColdAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexSettingsField(AbstractModel):
    """索引配置字段

    """

    def __init__(self):
        r"""
        :param _NumberOfShards: 索引主分片数
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfShards: str
        :param _NumberOfReplicas: 索引副本分片数
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfReplicas: str
        :param _RefreshInterval: 索引刷新频率
注意：此字段可能返回 null，表示取不到有效值。
        :type RefreshInterval: str
        """
        self._NumberOfShards = None
        self._NumberOfReplicas = None
        self._RefreshInterval = None

    @property
    def NumberOfShards(self):
        """索引主分片数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NumberOfShards

    @NumberOfShards.setter
    def NumberOfShards(self, NumberOfShards):
        self._NumberOfShards = NumberOfShards

    @property
    def NumberOfReplicas(self):
        """索引副本分片数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NumberOfReplicas

    @NumberOfReplicas.setter
    def NumberOfReplicas(self, NumberOfReplicas):
        self._NumberOfReplicas = NumberOfReplicas

    @property
    def RefreshInterval(self):
        """索引刷新频率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RefreshInterval

    @RefreshInterval.setter
    def RefreshInterval(self, RefreshInterval):
        self._RefreshInterval = RefreshInterval


    def _deserialize(self, params):
        self._NumberOfShards = params.get("NumberOfShards")
        self._NumberOfReplicas = params.get("NumberOfReplicas")
        self._RefreshInterval = params.get("RefreshInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewInstanceRequest(AbstractModel):
    """InquirePriceRenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
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
        


class InquirePriceRenewInstanceResponse(AbstractModel):
    """InquirePriceRenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginalPrice: 刊例价，即集群原始价格
        :type OriginalPrice: float
        :param _DiscountPrice: 折后价
        :type DiscountPrice: float
        :param _Discount: 折扣，如65折
        :type Discount: float
        :param _Currency: 货币，如CNY代表人民币
        :type Currency: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._Discount = None
        self._Currency = None
        self._RequestId = None

    @property
    def OriginalPrice(self):
        """刊例价，即集群原始价格
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        """折后价
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        """折扣，如65折
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def Currency(self):
        """货币，如CNY代表人民币
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

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
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Discount = params.get("Discount")
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class InstallInstanceModelRequest(AbstractModel):
    """InstallInstanceModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _UsrCosModelUrlList: 客户上传到cos的模型地址，单次请求限制一个。cos文件为压缩文件，格式包括：zip、tgz和tar.gz
        :type UsrCosModelUrlList: list of str
        :param _ModelNames: 客户指定安装的模型名称，可为空，默认为模型文件名
        :type ModelNames: list of str
        :param _TaskTypes: 模型使用的任务类型，包括：fill_mask, ner, question_answering, text_classification, text_embedding, text_expansion, text_similarity和zero_shot_classification，默认为text_embedding
        :type TaskTypes: list of str
        """
        self._InstanceId = None
        self._UsrCosModelUrlList = None
        self._ModelNames = None
        self._TaskTypes = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UsrCosModelUrlList(self):
        """客户上传到cos的模型地址，单次请求限制一个。cos文件为压缩文件，格式包括：zip、tgz和tar.gz
        :rtype: list of str
        """
        return self._UsrCosModelUrlList

    @UsrCosModelUrlList.setter
    def UsrCosModelUrlList(self, UsrCosModelUrlList):
        self._UsrCosModelUrlList = UsrCosModelUrlList

    @property
    def ModelNames(self):
        """客户指定安装的模型名称，可为空，默认为模型文件名
        :rtype: list of str
        """
        return self._ModelNames

    @ModelNames.setter
    def ModelNames(self, ModelNames):
        self._ModelNames = ModelNames

    @property
    def TaskTypes(self):
        """模型使用的任务类型，包括：fill_mask, ner, question_answering, text_classification, text_embedding, text_expansion, text_similarity和zero_shot_classification，默认为text_embedding
        :rtype: list of str
        """
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UsrCosModelUrlList = params.get("UsrCosModelUrlList")
        self._ModelNames = params.get("ModelNames")
        self._TaskTypes = params.get("TaskTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallInstanceModelResponse(AbstractModel):
    """InstallInstanceModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 发起异步流程的flowId
        :type FlowId: str
        :param _ErrMsg: 调用接口的错误信息
        :type ErrMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        """发起异步流程的flowId
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrMsg(self):
        """调用接口的错误信息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrMsg = params.get("ErrMsg")
        self._RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _AppId: 用户ID
        :type AppId: int
        :param _Uin: 用户UIN
        :type Uin: str
        :param _VpcUid: 实例所属VPC的UID
        :type VpcUid: str
        :param _SubnetUid: 实例所属子网的UID
        :type SubnetUid: str
        :param _Status: 实例状态，0:处理中,1:正常,-1:停止,-2:销毁中,-3:已销毁, -4:隔离中,2:创建集群时初始化中
        :type Status: int
        :param _RenewFlag: 自动续费标识。取值范围：
RENEW_FLAG_AUTO：自动续费  
RENEW_FLAG_MANUAL：不自动续费
默认取值：
RENEW_FLAG_DEFAULT：不自动续费
若该参数指定为 RENEW_FLAG_AUTO，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        :param _ChargeType: 实例计费模式。取值范围：  PREPAID：表示预付费，即包年包月  POSTPAID_BY_HOUR：表示后付费，即按量计费  CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
        :type ChargeType: str
        :param _ChargePeriod: 包年包月购买时长,单位:月
        :type ChargePeriod: int
        :param _NodeType: 节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param _NodeNum: 节点个数
        :type NodeNum: int
        :param _CpuNum: 节点CPU核数
        :type CpuNum: int
        :param _MemSize: 节点内存大小，单位GB
        :type MemSize: int
        :param _DiskType: 节点磁盘类型
        :type DiskType: str
        :param _DiskSize: 节点磁盘大小，单位GB
        :type DiskSize: int
        :param _EsDomain: ES域名
        :type EsDomain: str
        :param _EsVip: ES VIP
        :type EsVip: str
        :param _EsPort: ES端口
        :type EsPort: int
        :param _KibanaUrl: Kibana访问url
        :type KibanaUrl: str
        :param _EsVersion: ES版本号
        :type EsVersion: str
        :param _EsConfig: ES配置项
        :type EsConfig: str
        :param _EsAcl: Kibana访问控制配置
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param _CreateTime: 实例创建时间
        :type CreateTime: str
        :param _UpdateTime: 实例最后修改操作时间
        :type UpdateTime: str
        :param _Deadline: 实例到期时间
        :type Deadline: str
        :param _InstanceType: 实例类型（实例类型标识，当前只有1,2两种）
        :type InstanceType: int
        :param _IkConfig: Ik分词器配置
        :type IkConfig: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`
        :param _MasterNodeInfo: 专用主节点配置
        :type MasterNodeInfo: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`
        :param _CosBackup: cos自动备份配置
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param _AllowCosBackup: 是否允许cos自动备份
        :type AllowCosBackup: bool
        :param _TagList: 实例拥有的标签列表
        :type TagList: list of TagInfo
        :param _LicenseType: License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum
        :type LicenseType: str
        :param _EnableHotWarmMode: 是否为冷热集群<li>true: 冷热集群</li><li>false: 非冷热集群</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableHotWarmMode: bool
        :param _WarmNodeType: 温节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmNodeType: str
        :param _WarmNodeNum: 温节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmNodeNum: int
        :param _WarmCpuNum: 温节点CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmCpuNum: int
        :param _WarmMemSize: 温节点内存内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmMemSize: int
        :param _WarmDiskType: 温节点磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmDiskType: str
        :param _WarmDiskSize: 温节点磁盘大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmDiskSize: int
        :param _NodeInfoList: 集群节点信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfoList: list of NodeInfo
        :param _EsPublicUrl: Es公网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EsPublicUrl: str
        :param _MultiZoneInfo: 多可用区网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiZoneInfo: list of ZoneDetail
        :param _DeployMode: 部署模式<li>0：单可用区</li><li>1：多可用区，北京、上海、上海金融、广州、南京、香港、新加坡、法兰克福（白名单控制）</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMode: int
        :param _PublicAccess: ES公网访问状态<li>OPEN：开启</li><li>CLOSE：关闭</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicAccess: str
        :param _EsPublicAcl: ES公网访问控制配置
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param _KibanaPrivateUrl: Kibana内网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaPrivateUrl: str
        :param _KibanaPublicAccess: Kibana公网访问状态<li>OPEN：开启</li><li>CLOSE：关闭</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaPublicAccess: str
        :param _KibanaPrivateAccess: Kibana内网访问状态<li>OPEN：开启</li><li>CLOSE：关闭</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaPrivateAccess: str
        :param _SecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityType: int
        :param _SceneType: 场景化模板类型：0、不开启；1、通用场景；2、日志场景；3、搜索场景
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneType: int
        :param _KibanaConfig: Kibana配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaConfig: str
        :param _KibanaNodeInfo: Kibana节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaNodeInfo: :class:`tencentcloud.es.v20180416.models.KibanaNodeInfo`
        :param _WebNodeTypeInfo: 可视化节点配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param _Jdk: JDK类型，oracle或kona
注意：此字段可能返回 null，表示取不到有效值。
        :type Jdk: str
        :param _Protocol: 集群网络通讯协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _SecurityGroups: 安全组id
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroups: list of str
        :param _ColdNodeType: 冷节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdNodeType: str
        :param _ColdNodeNum: 冷节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdNodeNum: int
        :param _ColdCpuNum: 冷节点CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdCpuNum: int
        :param _ColdMemSize: 冷节点内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdMemSize: int
        :param _ColdDiskType: 冷节点磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdDiskType: str
        :param _ColdDiskSize: 冷节点磁盘大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdDiskSize: int
        :param _FrozenNodeType: 冻节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenNodeType: str
        :param _FrozenNodeNum: 冻节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenNodeNum: int
        :param _FrozenCpuNum: 冻节点CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenCpuNum: int
        :param _FrozenMemSize: 冻节点内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenMemSize: int
        :param _FrozenDiskType: 冻节点磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenDiskType: str
        :param _FrozenDiskSize: 冻节点磁盘大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenDiskSize: int
        :param _HealthStatus: 集群健康状态 -1 未知；0 Green; 1 Yellow; 2 Red
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthStatus: int
        :param _EsPrivateUrl: https集群内网url
注意：此字段可能返回 null，表示取不到有效值。
        :type EsPrivateUrl: str
        :param _EsPrivateDomain: https集群内网域名
注意：此字段可能返回 null，表示取不到有效值。
        :type EsPrivateDomain: str
        :param _EsConfigSets: 集群的配置组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EsConfigSets: list of EsConfigSetInfo
        :param _OperationDuration: 集群可维护时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        :param _OptionalWebServiceInfos: web节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OptionalWebServiceInfos: list of OptionalWebServiceInfo
        :param _AutoIndexEnabled: 自治索引开关
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoIndexEnabled: bool
        :param _EnableHybridStorage: 是否支持存储计算分离
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableHybridStorage: bool
        :param _ProcessPercent: 流程进度
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessPercent: float
        :param _KibanaAlteringPublicAccess: Kibana的alerting外网告警策略<li>OPEN：开启</li><li>CLOSE：关闭</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaAlteringPublicAccess: str
        :param _HasKernelUpgrade: 本月是否有内核可以更新：false-无，true-有
注意：此字段可能返回 null，表示取不到有效值。
        :type HasKernelUpgrade: bool
        :param _CdcId: cdcId，使用cdc子网时传递
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcId: str
        :param _KibanaPrivateVip: kibana内网vip
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaPrivateVip: str
        :param _CustomKibanaPrivateUrl: 自定义kibana内网url
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomKibanaPrivateUrl: str
        :param _OutboundPublicAcls: 节点出站访问详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OutboundPublicAcls: list of OutboundPublicAcl
        :param _NetConnectScheme: 网络连接方案
注意：此字段可能返回 null，表示取不到有效值。
        :type NetConnectScheme: str
        :param _DisasterRecoverGroupAffinity: 置放群组相关参数
注意：此字段可能返回 null，表示取不到有效值。
        :type DisasterRecoverGroupAffinity: int
        :param _SubProductCode: 子产品ID枚举值： 开源版："sp_es_io2"， 基础版："sp_es_basic"，白金版："sp_es_platinum"，企业版："sp_es_enterprise"，CDC白金版："sp_es_cdc_platinum"，日志增强版："sp_es_enlogging"，tsearch："sp_tsearch_io2"，logstash："sp_es_logstash" ，可以为空，为空的时候后台取LicenseType映射该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductCode: str
        :param _CosBucketStorageSize: 存算分离cos用量，单位M
注意：此字段可能返回 null，表示取不到有效值。
        :type CosBucketStorageSize: int
        :param _ReadWriteMode: 读写分离模式：0-不开启，1-本地读写分离，2-远端读写分离
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadWriteMode: int
        :param _EnableScheduleRecoverGroup: 是否有置放群组异步调度任务
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableScheduleRecoverGroup: bool
        :param _EnableScheduleOperationDuration: 异步调度任务的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableScheduleOperationDuration: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        :param _EnableDestroyProtection: 开启集群保护：OPEN-开启，CLOSE-关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableDestroyProtection: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._Zone = None
        self._AppId = None
        self._Uin = None
        self._VpcUid = None
        self._SubnetUid = None
        self._Status = None
        self._RenewFlag = None
        self._ChargeType = None
        self._ChargePeriod = None
        self._NodeType = None
        self._NodeNum = None
        self._CpuNum = None
        self._MemSize = None
        self._DiskType = None
        self._DiskSize = None
        self._EsDomain = None
        self._EsVip = None
        self._EsPort = None
        self._KibanaUrl = None
        self._EsVersion = None
        self._EsConfig = None
        self._EsAcl = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Deadline = None
        self._InstanceType = None
        self._IkConfig = None
        self._MasterNodeInfo = None
        self._CosBackup = None
        self._AllowCosBackup = None
        self._TagList = None
        self._LicenseType = None
        self._EnableHotWarmMode = None
        self._WarmNodeType = None
        self._WarmNodeNum = None
        self._WarmCpuNum = None
        self._WarmMemSize = None
        self._WarmDiskType = None
        self._WarmDiskSize = None
        self._NodeInfoList = None
        self._EsPublicUrl = None
        self._MultiZoneInfo = None
        self._DeployMode = None
        self._PublicAccess = None
        self._EsPublicAcl = None
        self._KibanaPrivateUrl = None
        self._KibanaPublicAccess = None
        self._KibanaPrivateAccess = None
        self._SecurityType = None
        self._SceneType = None
        self._KibanaConfig = None
        self._KibanaNodeInfo = None
        self._WebNodeTypeInfo = None
        self._Jdk = None
        self._Protocol = None
        self._SecurityGroups = None
        self._ColdNodeType = None
        self._ColdNodeNum = None
        self._ColdCpuNum = None
        self._ColdMemSize = None
        self._ColdDiskType = None
        self._ColdDiskSize = None
        self._FrozenNodeType = None
        self._FrozenNodeNum = None
        self._FrozenCpuNum = None
        self._FrozenMemSize = None
        self._FrozenDiskType = None
        self._FrozenDiskSize = None
        self._HealthStatus = None
        self._EsPrivateUrl = None
        self._EsPrivateDomain = None
        self._EsConfigSets = None
        self._OperationDuration = None
        self._OptionalWebServiceInfos = None
        self._AutoIndexEnabled = None
        self._EnableHybridStorage = None
        self._ProcessPercent = None
        self._KibanaAlteringPublicAccess = None
        self._HasKernelUpgrade = None
        self._CdcId = None
        self._KibanaPrivateVip = None
        self._CustomKibanaPrivateUrl = None
        self._OutboundPublicAcls = None
        self._NetConnectScheme = None
        self._DisasterRecoverGroupAffinity = None
        self._SubProductCode = None
        self._CosBucketStorageSize = None
        self._ReadWriteMode = None
        self._EnableScheduleRecoverGroup = None
        self._EnableScheduleOperationDuration = None
        self._EnableDestroyProtection = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

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
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AppId(self):
        """用户ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        """用户UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcUid(self):
        """实例所属VPC的UID
        :rtype: str
        """
        return self._VpcUid

    @VpcUid.setter
    def VpcUid(self, VpcUid):
        self._VpcUid = VpcUid

    @property
    def SubnetUid(self):
        """实例所属子网的UID
        :rtype: str
        """
        return self._SubnetUid

    @SubnetUid.setter
    def SubnetUid(self, SubnetUid):
        self._SubnetUid = SubnetUid

    @property
    def Status(self):
        """实例状态，0:处理中,1:正常,-1:停止,-2:销毁中,-3:已销毁, -4:隔离中,2:创建集群时初始化中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RenewFlag(self):
        """自动续费标识。取值范围：
RENEW_FLAG_AUTO：自动续费  
RENEW_FLAG_MANUAL：不自动续费
默认取值：
RENEW_FLAG_DEFAULT：不自动续费
若该参数指定为 RENEW_FLAG_AUTO，在账户余额充足的情况下，实例到期后将按月自动续费。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ChargeType(self):
        """实例计费模式。取值范围：  PREPAID：表示预付费，即包年包月  POSTPAID_BY_HOUR：表示后付费，即按量计费  CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargePeriod(self):
        """包年包月购买时长,单位:月
        :rtype: int
        """
        return self._ChargePeriod

    @ChargePeriod.setter
    def ChargePeriod(self, ChargePeriod):
        self._ChargePeriod = ChargePeriod

    @property
    def NodeType(self):
        """节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeNum(self):
        """节点个数
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def CpuNum(self):
        """节点CPU核数
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MemSize(self):
        """节点内存大小，单位GB
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def DiskType(self):
        """节点磁盘类型
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """节点磁盘大小，单位GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def EsDomain(self):
        """ES域名
        :rtype: str
        """
        return self._EsDomain

    @EsDomain.setter
    def EsDomain(self, EsDomain):
        self._EsDomain = EsDomain

    @property
    def EsVip(self):
        """ES VIP
        :rtype: str
        """
        return self._EsVip

    @EsVip.setter
    def EsVip(self, EsVip):
        self._EsVip = EsVip

    @property
    def EsPort(self):
        """ES端口
        :rtype: int
        """
        return self._EsPort

    @EsPort.setter
    def EsPort(self, EsPort):
        self._EsPort = EsPort

    @property
    def KibanaUrl(self):
        """Kibana访问url
        :rtype: str
        """
        return self._KibanaUrl

    @KibanaUrl.setter
    def KibanaUrl(self, KibanaUrl):
        self._KibanaUrl = KibanaUrl

    @property
    def EsVersion(self):
        """ES版本号
        :rtype: str
        """
        return self._EsVersion

    @EsVersion.setter
    def EsVersion(self, EsVersion):
        self._EsVersion = EsVersion

    @property
    def EsConfig(self):
        """ES配置项
        :rtype: str
        """
        return self._EsConfig

    @EsConfig.setter
    def EsConfig(self, EsConfig):
        self._EsConfig = EsConfig

    @property
    def EsAcl(self):
        """Kibana访问控制配置
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._EsAcl

    @EsAcl.setter
    def EsAcl(self, EsAcl):
        self._EsAcl = EsAcl

    @property
    def CreateTime(self):
        """实例创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """实例最后修改操作时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Deadline(self):
        """实例到期时间
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def InstanceType(self):
        """实例类型（实例类型标识，当前只有1,2两种）
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def IkConfig(self):
        """Ik分词器配置
        :rtype: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`
        """
        return self._IkConfig

    @IkConfig.setter
    def IkConfig(self, IkConfig):
        self._IkConfig = IkConfig

    @property
    def MasterNodeInfo(self):
        """专用主节点配置
        :rtype: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`
        """
        return self._MasterNodeInfo

    @MasterNodeInfo.setter
    def MasterNodeInfo(self, MasterNodeInfo):
        self._MasterNodeInfo = MasterNodeInfo

    @property
    def CosBackup(self):
        """cos自动备份配置
        :rtype: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup

    @property
    def AllowCosBackup(self):
        """是否允许cos自动备份
        :rtype: bool
        """
        return self._AllowCosBackup

    @AllowCosBackup.setter
    def AllowCosBackup(self, AllowCosBackup):
        self._AllowCosBackup = AllowCosBackup

    @property
    def TagList(self):
        """实例拥有的标签列表
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def LicenseType(self):
        """License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def EnableHotWarmMode(self):
        """是否为冷热集群<li>true: 冷热集群</li><li>false: 非冷热集群</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableHotWarmMode

    @EnableHotWarmMode.setter
    def EnableHotWarmMode(self, EnableHotWarmMode):
        self._EnableHotWarmMode = EnableHotWarmMode

    @property
    def WarmNodeType(self):
        """温节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WarmNodeType

    @WarmNodeType.setter
    def WarmNodeType(self, WarmNodeType):
        self._WarmNodeType = WarmNodeType

    @property
    def WarmNodeNum(self):
        """温节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WarmNodeNum

    @WarmNodeNum.setter
    def WarmNodeNum(self, WarmNodeNum):
        self._WarmNodeNum = WarmNodeNum

    @property
    def WarmCpuNum(self):
        """温节点CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WarmCpuNum

    @WarmCpuNum.setter
    def WarmCpuNum(self, WarmCpuNum):
        self._WarmCpuNum = WarmCpuNum

    @property
    def WarmMemSize(self):
        """温节点内存内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WarmMemSize

    @WarmMemSize.setter
    def WarmMemSize(self, WarmMemSize):
        self._WarmMemSize = WarmMemSize

    @property
    def WarmDiskType(self):
        """温节点磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WarmDiskType

    @WarmDiskType.setter
    def WarmDiskType(self, WarmDiskType):
        self._WarmDiskType = WarmDiskType

    @property
    def WarmDiskSize(self):
        """温节点磁盘大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WarmDiskSize

    @WarmDiskSize.setter
    def WarmDiskSize(self, WarmDiskSize):
        self._WarmDiskSize = WarmDiskSize

    @property
    def NodeInfoList(self):
        """集群节点信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of NodeInfo
        """
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList

    @property
    def EsPublicUrl(self):
        """Es公网地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EsPublicUrl

    @EsPublicUrl.setter
    def EsPublicUrl(self, EsPublicUrl):
        self._EsPublicUrl = EsPublicUrl

    @property
    def MultiZoneInfo(self):
        """多可用区网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ZoneDetail
        """
        return self._MultiZoneInfo

    @MultiZoneInfo.setter
    def MultiZoneInfo(self, MultiZoneInfo):
        self._MultiZoneInfo = MultiZoneInfo

    @property
    def DeployMode(self):
        """部署模式<li>0：单可用区</li><li>1：多可用区，北京、上海、上海金融、广州、南京、香港、新加坡、法兰克福（白名单控制）</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def PublicAccess(self):
        """ES公网访问状态<li>OPEN：开启</li><li>CLOSE：关闭</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicAccess

    @PublicAccess.setter
    def PublicAccess(self, PublicAccess):
        self._PublicAccess = PublicAccess

    @property
    def EsPublicAcl(self):
        """ES公网访问控制配置
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._EsPublicAcl

    @EsPublicAcl.setter
    def EsPublicAcl(self, EsPublicAcl):
        self._EsPublicAcl = EsPublicAcl

    @property
    def KibanaPrivateUrl(self):
        """Kibana内网地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaPrivateUrl

    @KibanaPrivateUrl.setter
    def KibanaPrivateUrl(self, KibanaPrivateUrl):
        self._KibanaPrivateUrl = KibanaPrivateUrl

    @property
    def KibanaPublicAccess(self):
        """Kibana公网访问状态<li>OPEN：开启</li><li>CLOSE：关闭</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaPublicAccess

    @KibanaPublicAccess.setter
    def KibanaPublicAccess(self, KibanaPublicAccess):
        self._KibanaPublicAccess = KibanaPublicAccess

    @property
    def KibanaPrivateAccess(self):
        """Kibana内网访问状态<li>OPEN：开启</li><li>CLOSE：关闭</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaPrivateAccess

    @KibanaPrivateAccess.setter
    def KibanaPrivateAccess(self, KibanaPrivateAccess):
        self._KibanaPrivateAccess = KibanaPrivateAccess

    @property
    def SecurityType(self):
        """6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def SceneType(self):
        """场景化模板类型：0、不开启；1、通用场景；2、日志场景；3、搜索场景
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def KibanaConfig(self):
        """Kibana配置项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaConfig

    @KibanaConfig.setter
    def KibanaConfig(self, KibanaConfig):
        self._KibanaConfig = KibanaConfig

    @property
    def KibanaNodeInfo(self):
        """Kibana节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.KibanaNodeInfo`
        """
        return self._KibanaNodeInfo

    @KibanaNodeInfo.setter
    def KibanaNodeInfo(self, KibanaNodeInfo):
        self._KibanaNodeInfo = KibanaNodeInfo

    @property
    def WebNodeTypeInfo(self):
        """可视化节点配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        """
        return self._WebNodeTypeInfo

    @WebNodeTypeInfo.setter
    def WebNodeTypeInfo(self, WebNodeTypeInfo):
        self._WebNodeTypeInfo = WebNodeTypeInfo

    @property
    def Jdk(self):
        """JDK类型，oracle或kona
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Jdk

    @Jdk.setter
    def Jdk(self, Jdk):
        self._Jdk = Jdk

    @property
    def Protocol(self):
        """集群网络通讯协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SecurityGroups(self):
        """安全组id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def ColdNodeType(self):
        """冷节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ColdNodeType

    @ColdNodeType.setter
    def ColdNodeType(self, ColdNodeType):
        self._ColdNodeType = ColdNodeType

    @property
    def ColdNodeNum(self):
        """冷节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ColdNodeNum

    @ColdNodeNum.setter
    def ColdNodeNum(self, ColdNodeNum):
        self._ColdNodeNum = ColdNodeNum

    @property
    def ColdCpuNum(self):
        """冷节点CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ColdCpuNum

    @ColdCpuNum.setter
    def ColdCpuNum(self, ColdCpuNum):
        self._ColdCpuNum = ColdCpuNum

    @property
    def ColdMemSize(self):
        """冷节点内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ColdMemSize

    @ColdMemSize.setter
    def ColdMemSize(self, ColdMemSize):
        self._ColdMemSize = ColdMemSize

    @property
    def ColdDiskType(self):
        """冷节点磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ColdDiskType

    @ColdDiskType.setter
    def ColdDiskType(self, ColdDiskType):
        self._ColdDiskType = ColdDiskType

    @property
    def ColdDiskSize(self):
        """冷节点磁盘大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ColdDiskSize

    @ColdDiskSize.setter
    def ColdDiskSize(self, ColdDiskSize):
        self._ColdDiskSize = ColdDiskSize

    @property
    def FrozenNodeType(self):
        """冻节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FrozenNodeType

    @FrozenNodeType.setter
    def FrozenNodeType(self, FrozenNodeType):
        self._FrozenNodeType = FrozenNodeType

    @property
    def FrozenNodeNum(self):
        """冻节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FrozenNodeNum

    @FrozenNodeNum.setter
    def FrozenNodeNum(self, FrozenNodeNum):
        self._FrozenNodeNum = FrozenNodeNum

    @property
    def FrozenCpuNum(self):
        """冻节点CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FrozenCpuNum

    @FrozenCpuNum.setter
    def FrozenCpuNum(self, FrozenCpuNum):
        self._FrozenCpuNum = FrozenCpuNum

    @property
    def FrozenMemSize(self):
        """冻节点内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FrozenMemSize

    @FrozenMemSize.setter
    def FrozenMemSize(self, FrozenMemSize):
        self._FrozenMemSize = FrozenMemSize

    @property
    def FrozenDiskType(self):
        """冻节点磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FrozenDiskType

    @FrozenDiskType.setter
    def FrozenDiskType(self, FrozenDiskType):
        self._FrozenDiskType = FrozenDiskType

    @property
    def FrozenDiskSize(self):
        """冻节点磁盘大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FrozenDiskSize

    @FrozenDiskSize.setter
    def FrozenDiskSize(self, FrozenDiskSize):
        self._FrozenDiskSize = FrozenDiskSize

    @property
    def HealthStatus(self):
        """集群健康状态 -1 未知；0 Green; 1 Yellow; 2 Red
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def EsPrivateUrl(self):
        """https集群内网url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EsPrivateUrl

    @EsPrivateUrl.setter
    def EsPrivateUrl(self, EsPrivateUrl):
        self._EsPrivateUrl = EsPrivateUrl

    @property
    def EsPrivateDomain(self):
        """https集群内网域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EsPrivateDomain

    @EsPrivateDomain.setter
    def EsPrivateDomain(self, EsPrivateDomain):
        self._EsPrivateDomain = EsPrivateDomain

    @property
    def EsConfigSets(self):
        """集群的配置组信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EsConfigSetInfo
        """
        return self._EsConfigSets

    @EsConfigSets.setter
    def EsConfigSets(self, EsConfigSets):
        self._EsConfigSets = EsConfigSets

    @property
    def OperationDuration(self):
        """集群可维护时间段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration

    @property
    def OptionalWebServiceInfos(self):
        """web节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OptionalWebServiceInfo
        """
        return self._OptionalWebServiceInfos

    @OptionalWebServiceInfos.setter
    def OptionalWebServiceInfos(self, OptionalWebServiceInfos):
        self._OptionalWebServiceInfos = OptionalWebServiceInfos

    @property
    def AutoIndexEnabled(self):
        """自治索引开关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AutoIndexEnabled

    @AutoIndexEnabled.setter
    def AutoIndexEnabled(self, AutoIndexEnabled):
        self._AutoIndexEnabled = AutoIndexEnabled

    @property
    def EnableHybridStorage(self):
        """是否支持存储计算分离
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableHybridStorage

    @EnableHybridStorage.setter
    def EnableHybridStorage(self, EnableHybridStorage):
        self._EnableHybridStorage = EnableHybridStorage

    @property
    def ProcessPercent(self):
        """流程进度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._ProcessPercent

    @ProcessPercent.setter
    def ProcessPercent(self, ProcessPercent):
        self._ProcessPercent = ProcessPercent

    @property
    def KibanaAlteringPublicAccess(self):
        """Kibana的alerting外网告警策略<li>OPEN：开启</li><li>CLOSE：关闭</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaAlteringPublicAccess

    @KibanaAlteringPublicAccess.setter
    def KibanaAlteringPublicAccess(self, KibanaAlteringPublicAccess):
        self._KibanaAlteringPublicAccess = KibanaAlteringPublicAccess

    @property
    def HasKernelUpgrade(self):
        """本月是否有内核可以更新：false-无，true-有
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._HasKernelUpgrade

    @HasKernelUpgrade.setter
    def HasKernelUpgrade(self, HasKernelUpgrade):
        self._HasKernelUpgrade = HasKernelUpgrade

    @property
    def CdcId(self):
        """cdcId，使用cdc子网时传递
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def KibanaPrivateVip(self):
        """kibana内网vip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaPrivateVip

    @KibanaPrivateVip.setter
    def KibanaPrivateVip(self, KibanaPrivateVip):
        self._KibanaPrivateVip = KibanaPrivateVip

    @property
    def CustomKibanaPrivateUrl(self):
        """自定义kibana内网url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CustomKibanaPrivateUrl

    @CustomKibanaPrivateUrl.setter
    def CustomKibanaPrivateUrl(self, CustomKibanaPrivateUrl):
        self._CustomKibanaPrivateUrl = CustomKibanaPrivateUrl

    @property
    def OutboundPublicAcls(self):
        """节点出站访问详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OutboundPublicAcl
        """
        return self._OutboundPublicAcls

    @OutboundPublicAcls.setter
    def OutboundPublicAcls(self, OutboundPublicAcls):
        self._OutboundPublicAcls = OutboundPublicAcls

    @property
    def NetConnectScheme(self):
        """网络连接方案
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NetConnectScheme

    @NetConnectScheme.setter
    def NetConnectScheme(self, NetConnectScheme):
        self._NetConnectScheme = NetConnectScheme

    @property
    def DisasterRecoverGroupAffinity(self):
        """置放群组相关参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DisasterRecoverGroupAffinity

    @DisasterRecoverGroupAffinity.setter
    def DisasterRecoverGroupAffinity(self, DisasterRecoverGroupAffinity):
        self._DisasterRecoverGroupAffinity = DisasterRecoverGroupAffinity

    @property
    def SubProductCode(self):
        """子产品ID枚举值： 开源版："sp_es_io2"， 基础版："sp_es_basic"，白金版："sp_es_platinum"，企业版："sp_es_enterprise"，CDC白金版："sp_es_cdc_platinum"，日志增强版："sp_es_enlogging"，tsearch："sp_tsearch_io2"，logstash："sp_es_logstash" ，可以为空，为空的时候后台取LicenseType映射该字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def CosBucketStorageSize(self):
        """存算分离cos用量，单位M
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CosBucketStorageSize

    @CosBucketStorageSize.setter
    def CosBucketStorageSize(self, CosBucketStorageSize):
        self._CosBucketStorageSize = CosBucketStorageSize

    @property
    def ReadWriteMode(self):
        """读写分离模式：0-不开启，1-本地读写分离，2-远端读写分离
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReadWriteMode

    @ReadWriteMode.setter
    def ReadWriteMode(self, ReadWriteMode):
        self._ReadWriteMode = ReadWriteMode

    @property
    def EnableScheduleRecoverGroup(self):
        """是否有置放群组异步调度任务
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableScheduleRecoverGroup

    @EnableScheduleRecoverGroup.setter
    def EnableScheduleRecoverGroup(self, EnableScheduleRecoverGroup):
        self._EnableScheduleRecoverGroup = EnableScheduleRecoverGroup

    @property
    def EnableScheduleOperationDuration(self):
        """异步调度任务的时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        return self._EnableScheduleOperationDuration

    @EnableScheduleOperationDuration.setter
    def EnableScheduleOperationDuration(self, EnableScheduleOperationDuration):
        self._EnableScheduleOperationDuration = EnableScheduleOperationDuration

    @property
    def EnableDestroyProtection(self):
        """开启集群保护：OPEN-开启，CLOSE-关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EnableDestroyProtection

    @EnableDestroyProtection.setter
    def EnableDestroyProtection(self, EnableDestroyProtection):
        self._EnableDestroyProtection = EnableDestroyProtection


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._VpcUid = params.get("VpcUid")
        self._SubnetUid = params.get("SubnetUid")
        self._Status = params.get("Status")
        self._RenewFlag = params.get("RenewFlag")
        self._ChargeType = params.get("ChargeType")
        self._ChargePeriod = params.get("ChargePeriod")
        self._NodeType = params.get("NodeType")
        self._NodeNum = params.get("NodeNum")
        self._CpuNum = params.get("CpuNum")
        self._MemSize = params.get("MemSize")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._EsDomain = params.get("EsDomain")
        self._EsVip = params.get("EsVip")
        self._EsPort = params.get("EsPort")
        self._KibanaUrl = params.get("KibanaUrl")
        self._EsVersion = params.get("EsVersion")
        self._EsConfig = params.get("EsConfig")
        if params.get("EsAcl") is not None:
            self._EsAcl = EsAcl()
            self._EsAcl._deserialize(params.get("EsAcl"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Deadline = params.get("Deadline")
        self._InstanceType = params.get("InstanceType")
        if params.get("IkConfig") is not None:
            self._IkConfig = EsDictionaryInfo()
            self._IkConfig._deserialize(params.get("IkConfig"))
        if params.get("MasterNodeInfo") is not None:
            self._MasterNodeInfo = MasterNodeInfo()
            self._MasterNodeInfo._deserialize(params.get("MasterNodeInfo"))
        if params.get("CosBackup") is not None:
            self._CosBackup = CosBackup()
            self._CosBackup._deserialize(params.get("CosBackup"))
        self._AllowCosBackup = params.get("AllowCosBackup")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._LicenseType = params.get("LicenseType")
        self._EnableHotWarmMode = params.get("EnableHotWarmMode")
        self._WarmNodeType = params.get("WarmNodeType")
        self._WarmNodeNum = params.get("WarmNodeNum")
        self._WarmCpuNum = params.get("WarmCpuNum")
        self._WarmMemSize = params.get("WarmMemSize")
        self._WarmDiskType = params.get("WarmDiskType")
        self._WarmDiskSize = params.get("WarmDiskSize")
        if params.get("NodeInfoList") is not None:
            self._NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeInfoList.append(obj)
        self._EsPublicUrl = params.get("EsPublicUrl")
        if params.get("MultiZoneInfo") is not None:
            self._MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self._MultiZoneInfo.append(obj)
        self._DeployMode = params.get("DeployMode")
        self._PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self._EsPublicAcl = EsAcl()
            self._EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self._KibanaPrivateUrl = params.get("KibanaPrivateUrl")
        self._KibanaPublicAccess = params.get("KibanaPublicAccess")
        self._KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self._SecurityType = params.get("SecurityType")
        self._SceneType = params.get("SceneType")
        self._KibanaConfig = params.get("KibanaConfig")
        if params.get("KibanaNodeInfo") is not None:
            self._KibanaNodeInfo = KibanaNodeInfo()
            self._KibanaNodeInfo._deserialize(params.get("KibanaNodeInfo"))
        if params.get("WebNodeTypeInfo") is not None:
            self._WebNodeTypeInfo = WebNodeTypeInfo()
            self._WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self._Jdk = params.get("Jdk")
        self._Protocol = params.get("Protocol")
        self._SecurityGroups = params.get("SecurityGroups")
        self._ColdNodeType = params.get("ColdNodeType")
        self._ColdNodeNum = params.get("ColdNodeNum")
        self._ColdCpuNum = params.get("ColdCpuNum")
        self._ColdMemSize = params.get("ColdMemSize")
        self._ColdDiskType = params.get("ColdDiskType")
        self._ColdDiskSize = params.get("ColdDiskSize")
        self._FrozenNodeType = params.get("FrozenNodeType")
        self._FrozenNodeNum = params.get("FrozenNodeNum")
        self._FrozenCpuNum = params.get("FrozenCpuNum")
        self._FrozenMemSize = params.get("FrozenMemSize")
        self._FrozenDiskType = params.get("FrozenDiskType")
        self._FrozenDiskSize = params.get("FrozenDiskSize")
        self._HealthStatus = params.get("HealthStatus")
        self._EsPrivateUrl = params.get("EsPrivateUrl")
        self._EsPrivateDomain = params.get("EsPrivateDomain")
        if params.get("EsConfigSets") is not None:
            self._EsConfigSets = []
            for item in params.get("EsConfigSets"):
                obj = EsConfigSetInfo()
                obj._deserialize(item)
                self._EsConfigSets.append(obj)
        if params.get("OperationDuration") is not None:
            self._OperationDuration = OperationDuration()
            self._OperationDuration._deserialize(params.get("OperationDuration"))
        if params.get("OptionalWebServiceInfos") is not None:
            self._OptionalWebServiceInfos = []
            for item in params.get("OptionalWebServiceInfos"):
                obj = OptionalWebServiceInfo()
                obj._deserialize(item)
                self._OptionalWebServiceInfos.append(obj)
        self._AutoIndexEnabled = params.get("AutoIndexEnabled")
        self._EnableHybridStorage = params.get("EnableHybridStorage")
        self._ProcessPercent = params.get("ProcessPercent")
        self._KibanaAlteringPublicAccess = params.get("KibanaAlteringPublicAccess")
        self._HasKernelUpgrade = params.get("HasKernelUpgrade")
        self._CdcId = params.get("CdcId")
        self._KibanaPrivateVip = params.get("KibanaPrivateVip")
        self._CustomKibanaPrivateUrl = params.get("CustomKibanaPrivateUrl")
        if params.get("OutboundPublicAcls") is not None:
            self._OutboundPublicAcls = []
            for item in params.get("OutboundPublicAcls"):
                obj = OutboundPublicAcl()
                obj._deserialize(item)
                self._OutboundPublicAcls.append(obj)
        self._NetConnectScheme = params.get("NetConnectScheme")
        self._DisasterRecoverGroupAffinity = params.get("DisasterRecoverGroupAffinity")
        self._SubProductCode = params.get("SubProductCode")
        self._CosBucketStorageSize = params.get("CosBucketStorageSize")
        self._ReadWriteMode = params.get("ReadWriteMode")
        self._EnableScheduleRecoverGroup = params.get("EnableScheduleRecoverGroup")
        if params.get("EnableScheduleOperationDuration") is not None:
            self._EnableScheduleOperationDuration = EnableScheduleOperationDuration()
            self._EnableScheduleOperationDuration._deserialize(params.get("EnableScheduleOperationDuration"))
        self._EnableDestroyProtection = params.get("EnableDestroyProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceLog(AbstractModel):
    """ES集群日志详细信息

    """

    def __init__(self):
        r"""
        :param _Time: 日志时间
        :type Time: str
        :param _Level: 日志级别
        :type Level: str
        :param _Ip: 集群节点ip
        :type Ip: str
        :param _Message: 日志内容
        :type Message: str
        :param _NodeID: 集群节点ID
        :type NodeID: str
        """
        self._Time = None
        self._Level = None
        self._Ip = None
        self._Message = None
        self._NodeID = None

    @property
    def Time(self):
        """日志时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Level(self):
        """日志级别
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Ip(self):
        """集群节点ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Message(self):
        """日志内容
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def NodeID(self):
        """集群节点ID
        :rtype: str
        """
        return self._NodeID

    @NodeID.setter
    def NodeID(self, NodeID):
        self._NodeID = NodeID


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Level = params.get("Level")
        self._Ip = params.get("Ip")
        self._Message = params.get("Message")
        self._NodeID = params.get("NodeID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobParam(AbstractModel):
    """智能运维诊断参数

    """

    def __init__(self):
        r"""
        :param _Jobs: 诊断项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Jobs: list of str
        :param _Indices: 诊断索引
        :type Indices: str
        :param _Interval: 历史诊断时间
        :type Interval: int
        """
        self._Jobs = None
        self._Indices = None
        self._Interval = None

    @property
    def Jobs(self):
        """诊断项列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Jobs

    @Jobs.setter
    def Jobs(self, Jobs):
        self._Jobs = Jobs

    @property
    def Indices(self):
        """诊断索引
        :rtype: str
        """
        return self._Indices

    @Indices.setter
    def Indices(self, Indices):
        self._Indices = Indices

    @property
    def Interval(self):
        """历史诊断时间
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._Jobs = params.get("Jobs")
        self._Indices = params.get("Indices")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """OperationDetail使用此结构的数组描述新旧配置

    """

    def __init__(self):
        r"""
        :param _Key: 键
        :type Key: str
        :param _Value: 值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """值
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
        


class KibanaNodeInfo(AbstractModel):
    """实例Kibana节点相关信息

    """

    def __init__(self):
        r"""
        :param _KibanaNodeType: Kibana节点规格
        :type KibanaNodeType: str
        :param _KibanaNodeNum: Kibana节点个数
        :type KibanaNodeNum: int
        :param _KibanaNodeCpuNum: Kibana节点CPU数
        :type KibanaNodeCpuNum: int
        :param _KibanaNodeMemSize: Kibana节点内存GB
        :type KibanaNodeMemSize: int
        :param _KibanaNodeDiskType: Kibana节点磁盘类型
        :type KibanaNodeDiskType: str
        :param _KibanaNodeDiskSize: Kibana节点磁盘大小
        :type KibanaNodeDiskSize: int
        """
        self._KibanaNodeType = None
        self._KibanaNodeNum = None
        self._KibanaNodeCpuNum = None
        self._KibanaNodeMemSize = None
        self._KibanaNodeDiskType = None
        self._KibanaNodeDiskSize = None

    @property
    def KibanaNodeType(self):
        """Kibana节点规格
        :rtype: str
        """
        return self._KibanaNodeType

    @KibanaNodeType.setter
    def KibanaNodeType(self, KibanaNodeType):
        self._KibanaNodeType = KibanaNodeType

    @property
    def KibanaNodeNum(self):
        """Kibana节点个数
        :rtype: int
        """
        return self._KibanaNodeNum

    @KibanaNodeNum.setter
    def KibanaNodeNum(self, KibanaNodeNum):
        self._KibanaNodeNum = KibanaNodeNum

    @property
    def KibanaNodeCpuNum(self):
        """Kibana节点CPU数
        :rtype: int
        """
        return self._KibanaNodeCpuNum

    @KibanaNodeCpuNum.setter
    def KibanaNodeCpuNum(self, KibanaNodeCpuNum):
        self._KibanaNodeCpuNum = KibanaNodeCpuNum

    @property
    def KibanaNodeMemSize(self):
        """Kibana节点内存GB
        :rtype: int
        """
        return self._KibanaNodeMemSize

    @KibanaNodeMemSize.setter
    def KibanaNodeMemSize(self, KibanaNodeMemSize):
        self._KibanaNodeMemSize = KibanaNodeMemSize

    @property
    def KibanaNodeDiskType(self):
        """Kibana节点磁盘类型
        :rtype: str
        """
        return self._KibanaNodeDiskType

    @KibanaNodeDiskType.setter
    def KibanaNodeDiskType(self, KibanaNodeDiskType):
        self._KibanaNodeDiskType = KibanaNodeDiskType

    @property
    def KibanaNodeDiskSize(self):
        """Kibana节点磁盘大小
        :rtype: int
        """
        return self._KibanaNodeDiskSize

    @KibanaNodeDiskSize.setter
    def KibanaNodeDiskSize(self, KibanaNodeDiskSize):
        self._KibanaNodeDiskSize = KibanaNodeDiskSize


    def _deserialize(self, params):
        self._KibanaNodeType = params.get("KibanaNodeType")
        self._KibanaNodeNum = params.get("KibanaNodeNum")
        self._KibanaNodeCpuNum = params.get("KibanaNodeCpuNum")
        self._KibanaNodeMemSize = params.get("KibanaNodeMemSize")
        self._KibanaNodeDiskType = params.get("KibanaNodeDiskType")
        self._KibanaNodeDiskSize = params.get("KibanaNodeDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KibanaPublicAcl(AbstractModel):
    """kibana公网域名白名单参数

    """

    def __init__(self):
        r"""
        :param _WhiteIpList: kibana访问白名单
        :type WhiteIpList: list of str
        """
        self._WhiteIpList = None

    @property
    def WhiteIpList(self):
        """kibana访问白名单
        :rtype: list of str
        """
        return self._WhiteIpList

    @WhiteIpList.setter
    def WhiteIpList(self, WhiteIpList):
        self._WhiteIpList = WhiteIpList


    def _deserialize(self, params):
        self._WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KibanaView(AbstractModel):
    """Kibana视图数据

    """

    def __init__(self):
        r"""
        :param _Ip: Kibana节点IP
        :type Ip: str
        :param _DiskSize: 节点总磁盘大小
        :type DiskSize: int
        :param _DiskUsage: 磁盘使用率
        :type DiskUsage: float
        :param _MemSize: 节点内存大小
        :type MemSize: int
        :param _MemUsage: 内存使用率
        :type MemUsage: float
        :param _CpuNum: 节点cpu个数
        :type CpuNum: int
        :param _CpuUsage: cpu使用率
        :type CpuUsage: float
        :param _Zone: 可用区
        :type Zone: str
        :param _NodeId: ts-0noqayxu-az6-hot-03222010-0
        :type NodeId: str
        """
        self._Ip = None
        self._DiskSize = None
        self._DiskUsage = None
        self._MemSize = None
        self._MemUsage = None
        self._CpuNum = None
        self._CpuUsage = None
        self._Zone = None
        self._NodeId = None

    @property
    def Ip(self):
        """Kibana节点IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def DiskSize(self):
        """节点总磁盘大小
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskUsage(self):
        """磁盘使用率
        :rtype: float
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def MemSize(self):
        """节点内存大小
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def MemUsage(self):
        """内存使用率
        :rtype: float
        """
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def CpuNum(self):
        """节点cpu个数
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def CpuUsage(self):
        """cpu使用率
        :rtype: float
        """
        return self._CpuUsage

    @CpuUsage.setter
    def CpuUsage(self, CpuUsage):
        self._CpuUsage = CpuUsage

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
    def NodeId(self):
        """ts-0noqayxu-az6-hot-03222010-0
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._DiskSize = params.get("DiskSize")
        self._DiskUsage = params.get("DiskUsage")
        self._MemSize = params.get("MemSize")
        self._MemUsage = params.get("MemUsage")
        self._CpuNum = params.get("CpuNum")
        self._CpuUsage = params.get("CpuUsage")
        self._Zone = params.get("Zone")
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskInfo(AbstractModel):
    """节点本地盘信息

    """

    def __init__(self):
        r"""
        :param _LocalDiskType: 本地盘类型<li>LOCAL_SATA：大数据型</li><li>NVME_SSD：高IO型</li>
        :type LocalDiskType: str
        :param _LocalDiskSize: 本地盘单盘大小
        :type LocalDiskSize: int
        :param _LocalDiskCount: 本地盘块数
        :type LocalDiskCount: int
        """
        self._LocalDiskType = None
        self._LocalDiskSize = None
        self._LocalDiskCount = None

    @property
    def LocalDiskType(self):
        """本地盘类型<li>LOCAL_SATA：大数据型</li><li>NVME_SSD：高IO型</li>
        :rtype: str
        """
        return self._LocalDiskType

    @LocalDiskType.setter
    def LocalDiskType(self, LocalDiskType):
        self._LocalDiskType = LocalDiskType

    @property
    def LocalDiskSize(self):
        """本地盘单盘大小
        :rtype: int
        """
        return self._LocalDiskSize

    @LocalDiskSize.setter
    def LocalDiskSize(self, LocalDiskSize):
        self._LocalDiskSize = LocalDiskSize

    @property
    def LocalDiskCount(self):
        """本地盘块数
        :rtype: int
        """
        return self._LocalDiskCount

    @LocalDiskCount.setter
    def LocalDiskCount(self, LocalDiskCount):
        self._LocalDiskCount = LocalDiskCount


    def _deserialize(self, params):
        self._LocalDiskType = params.get("LocalDiskType")
        self._LocalDiskSize = params.get("LocalDiskSize")
        self._LocalDiskCount = params.get("LocalDiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogDetail(AbstractModel):
    """智能运维日志详情

    """

    def __init__(self):
        r"""
        :param _Key: 日志异常名
        :type Key: str
        :param _Advise: 日志异常处理建议
        :type Advise: str
        :param _Count: 日志异常名出现次数
        :type Count: int
        """
        self._Key = None
        self._Advise = None
        self._Count = None

    @property
    def Key(self):
        """日志异常名
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Advise(self):
        """日志异常处理建议
        :rtype: str
        """
        return self._Advise

    @Advise.setter
    def Advise(self, Advise):
        self._Advise = Advise

    @property
    def Count(self):
        """日志异常名出现次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Advise = params.get("Advise")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashBindedES(AbstractModel):
    """Logstash绑定的ES集群信息

    """

    def __init__(self):
        r"""
        :param _ESInstanceId: ES集群ID
        :type ESInstanceId: str
        :param _ESUserName: ES集群用户名
        :type ESUserName: str
        :param _ESPassword: ES集群密码
        :type ESPassword: str
        """
        self._ESInstanceId = None
        self._ESUserName = None
        self._ESPassword = None

    @property
    def ESInstanceId(self):
        """ES集群ID
        :rtype: str
        """
        return self._ESInstanceId

    @ESInstanceId.setter
    def ESInstanceId(self, ESInstanceId):
        self._ESInstanceId = ESInstanceId

    @property
    def ESUserName(self):
        """ES集群用户名
        :rtype: str
        """
        return self._ESUserName

    @ESUserName.setter
    def ESUserName(self, ESUserName):
        self._ESUserName = ESUserName

    @property
    def ESPassword(self):
        """ES集群密码
        :rtype: str
        """
        return self._ESPassword

    @ESPassword.setter
    def ESPassword(self, ESPassword):
        self._ESPassword = ESPassword


    def _deserialize(self, params):
        self._ESInstanceId = params.get("ESInstanceId")
        self._ESUserName = params.get("ESUserName")
        self._ESPassword = params.get("ESPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashExtendedFile(AbstractModel):
    """Logstash扩展文件信息

    """

    def __init__(self):
        r"""
        :param _Name: 扩展文件名称
        :type Name: str
        :param _Size: 扩展文件大小，单位B
        :type Size: int
        """
        self._Name = None
        self._Size = None

    @property
    def Name(self):
        """扩展文件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        """扩展文件大小，单位B
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashInstanceInfo(AbstractModel):
    """Logstash实例详细信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _AppId: 用户ID
        :type AppId: int
        :param _Uin: 用户UIN
        :type Uin: str
        :param _VpcId: 实例所属VPC的ID
        :type VpcId: str
        :param _SubnetId: 实例所属子网的ID
        :type SubnetId: str
        :param _Status: 实例状态，0:处理中,1:正常,-1停止,-2:销毁中,-3:已销毁
        :type Status: int
        :param _ChargeType: 实例计费模式。取值范围：  PREPAID：表示预付费，即包年包月  POSTPAID_BY_HOUR：表示后付费，即按量计费  CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
        :type ChargeType: str
        :param _ChargePeriod: 包年包月购买时长,单位:月
        :type ChargePeriod: int
        :param _RenewFlag: 自动续费标识。取值范围：  NOTIFY_AND_AUTO_RENEW：通知过期且自动续费  NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费  DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费  默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        :param _NodeType: 节点规格<li>LOGSTASH.S1.SMALL2：1核2G</li><li>LOGSTASH.S1.MEDIUM4：2核4G</li><li>LOGSTASH.S1.MEDIUM8：2核8G</li><li>LOGSTASH.S1.LARGE16：4核16G</li><li>LOGSTASH.S1.2XLARGE32：8核32G</li><li>LOGSTASH.S1.4XLARGE32：16核32G</li><li>LOGSTASH.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param _NodeNum: 节点个数
        :type NodeNum: int
        :param _DiskType: 节点磁盘类型
        :type DiskType: str
        :param _DiskSize: 节点磁盘大小，单位GB
        :type DiskSize: int
        :param _LogstashVersion: Logstash版本号
        :type LogstashVersion: str
        :param _LicenseType: License类型<li>oss：开源版</li><li>xpack：基础版</li>默认值xpack
        :type LicenseType: str
        :param _CreateTime: 实例创建时间
        :type CreateTime: str
        :param _UpdateTime: 实例最后修改操作时间
        :type UpdateTime: str
        :param _Deadline: 实例到期时间
        :type Deadline: str
        :param _Nodes: 实例节点类型
        :type Nodes: list of LogstashNodeInfo
        :param _BindedESInstanceId: 实例绑定的ES集群ID
        :type BindedESInstanceId: str
        :param _YMLConfig: 实例的YML配置
注意：此字段可能返回 null，表示取不到有效值。
        :type YMLConfig: str
        :param _ExtendedFiles: 扩展文件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtendedFiles: list of LogstashExtendedFile
        :param _OperationDuration: 可维护时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        :param _CpuNum: CPU数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuNum: int
        :param _TagList: 实例标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of TagInfo
        :param _MemSize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._Zone = None
        self._AppId = None
        self._Uin = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._ChargeType = None
        self._ChargePeriod = None
        self._RenewFlag = None
        self._NodeType = None
        self._NodeNum = None
        self._DiskType = None
        self._DiskSize = None
        self._LogstashVersion = None
        self._LicenseType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Deadline = None
        self._Nodes = None
        self._BindedESInstanceId = None
        self._YMLConfig = None
        self._ExtendedFiles = None
        self._OperationDuration = None
        self._CpuNum = None
        self._TagList = None
        self._MemSize = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

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
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def AppId(self):
        """用户ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        """用户UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcId(self):
        """实例所属VPC的ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """实例所属子网的ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        """实例状态，0:处理中,1:正常,-1停止,-2:销毁中,-3:已销毁
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChargeType(self):
        """实例计费模式。取值范围：  PREPAID：表示预付费，即包年包月  POSTPAID_BY_HOUR：表示后付费，即按量计费  CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargePeriod(self):
        """包年包月购买时长,单位:月
        :rtype: int
        """
        return self._ChargePeriod

    @ChargePeriod.setter
    def ChargePeriod(self, ChargePeriod):
        self._ChargePeriod = ChargePeriod

    @property
    def RenewFlag(self):
        """自动续费标识。取值范围：  NOTIFY_AND_AUTO_RENEW：通知过期且自动续费  NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费  DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费  默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def NodeType(self):
        """节点规格<li>LOGSTASH.S1.SMALL2：1核2G</li><li>LOGSTASH.S1.MEDIUM4：2核4G</li><li>LOGSTASH.S1.MEDIUM8：2核8G</li><li>LOGSTASH.S1.LARGE16：4核16G</li><li>LOGSTASH.S1.2XLARGE32：8核32G</li><li>LOGSTASH.S1.4XLARGE32：16核32G</li><li>LOGSTASH.S1.4XLARGE64：16核64G</li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeNum(self):
        """节点个数
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def DiskType(self):
        """节点磁盘类型
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """节点磁盘大小，单位GB
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def LogstashVersion(self):
        """Logstash版本号
        :rtype: str
        """
        return self._LogstashVersion

    @LogstashVersion.setter
    def LogstashVersion(self, LogstashVersion):
        self._LogstashVersion = LogstashVersion

    @property
    def LicenseType(self):
        """License类型<li>oss：开源版</li><li>xpack：基础版</li>默认值xpack
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def CreateTime(self):
        """实例创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """实例最后修改操作时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Deadline(self):
        """实例到期时间
        :rtype: str
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def Nodes(self):
        """实例节点类型
        :rtype: list of LogstashNodeInfo
        """
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def BindedESInstanceId(self):
        """实例绑定的ES集群ID
        :rtype: str
        """
        return self._BindedESInstanceId

    @BindedESInstanceId.setter
    def BindedESInstanceId(self, BindedESInstanceId):
        self._BindedESInstanceId = BindedESInstanceId

    @property
    def YMLConfig(self):
        """实例的YML配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._YMLConfig

    @YMLConfig.setter
    def YMLConfig(self, YMLConfig):
        self._YMLConfig = YMLConfig

    @property
    def ExtendedFiles(self):
        """扩展文件列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogstashExtendedFile
        """
        return self._ExtendedFiles

    @ExtendedFiles.setter
    def ExtendedFiles(self, ExtendedFiles):
        self._ExtendedFiles = ExtendedFiles

    @property
    def OperationDuration(self):
        """可维护时间段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration

    @property
    def CpuNum(self):
        """CPU数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def TagList(self):
        """实例标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def MemSize(self):
        """内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._ChargeType = params.get("ChargeType")
        self._ChargePeriod = params.get("ChargePeriod")
        self._RenewFlag = params.get("RenewFlag")
        self._NodeType = params.get("NodeType")
        self._NodeNum = params.get("NodeNum")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._LogstashVersion = params.get("LogstashVersion")
        self._LicenseType = params.get("LicenseType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Deadline = params.get("Deadline")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = LogstashNodeInfo()
                obj._deserialize(item)
                self._Nodes.append(obj)
        self._BindedESInstanceId = params.get("BindedESInstanceId")
        self._YMLConfig = params.get("YMLConfig")
        if params.get("ExtendedFiles") is not None:
            self._ExtendedFiles = []
            for item in params.get("ExtendedFiles"):
                obj = LogstashExtendedFile()
                obj._deserialize(item)
                self._ExtendedFiles.append(obj)
        if params.get("OperationDuration") is not None:
            self._OperationDuration = OperationDuration()
            self._OperationDuration._deserialize(params.get("OperationDuration"))
        self._CpuNum = params.get("CpuNum")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._MemSize = params.get("MemSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashNodeInfo(AbstractModel):
    """Logstash节点信息

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID
        :type NodeId: str
        :param _Ip: 节点IP
        :type Ip: str
        :param _Port: 节点端口
        :type Port: int
        """
        self._NodeId = None
        self._Ip = None
        self._Port = None

    @property
    def NodeId(self):
        """节点ID
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Ip(self):
        """节点IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """节点端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashPipeline(AbstractModel):
    """Logstash管道信息

    """

    def __init__(self):
        r"""
        :param _PipelineId: 管道ID
        :type PipelineId: str
        :param _PipelineDesc: 管道描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PipelineDesc: str
        :param _Config: 管道配置内容
        :type Config: str
        :param _Workers: 管道的Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Workers: int
        :param _BatchSize: 管道批处理大小
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchSize: int
        :param _BatchDelay: 管道批处理延迟
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchDelay: int
        :param _QueueType: 管道缓冲队列类型
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueType: str
        :param _QueueMaxBytes: 管道缓冲队列大小
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueMaxBytes: str
        :param _QueueCheckPointWrites: 管道缓冲队列检查点写入数
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueCheckPointWrites: int
        """
        self._PipelineId = None
        self._PipelineDesc = None
        self._Config = None
        self._Workers = None
        self._BatchSize = None
        self._BatchDelay = None
        self._QueueType = None
        self._QueueMaxBytes = None
        self._QueueCheckPointWrites = None

    @property
    def PipelineId(self):
        """管道ID
        :rtype: str
        """
        return self._PipelineId

    @PipelineId.setter
    def PipelineId(self, PipelineId):
        self._PipelineId = PipelineId

    @property
    def PipelineDesc(self):
        """管道描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PipelineDesc

    @PipelineDesc.setter
    def PipelineDesc(self, PipelineDesc):
        self._PipelineDesc = PipelineDesc

    @property
    def Config(self):
        """管道配置内容
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Workers(self):
        """管道的Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Workers

    @Workers.setter
    def Workers(self, Workers):
        self._Workers = Workers

    @property
    def BatchSize(self):
        """管道批处理大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def BatchDelay(self):
        """管道批处理延迟
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BatchDelay

    @BatchDelay.setter
    def BatchDelay(self, BatchDelay):
        self._BatchDelay = BatchDelay

    @property
    def QueueType(self):
        """管道缓冲队列类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def QueueMaxBytes(self):
        """管道缓冲队列大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueueMaxBytes

    @QueueMaxBytes.setter
    def QueueMaxBytes(self, QueueMaxBytes):
        self._QueueMaxBytes = QueueMaxBytes

    @property
    def QueueCheckPointWrites(self):
        """管道缓冲队列检查点写入数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._QueueCheckPointWrites

    @QueueCheckPointWrites.setter
    def QueueCheckPointWrites(self, QueueCheckPointWrites):
        self._QueueCheckPointWrites = QueueCheckPointWrites


    def _deserialize(self, params):
        self._PipelineId = params.get("PipelineId")
        self._PipelineDesc = params.get("PipelineDesc")
        self._Config = params.get("Config")
        self._Workers = params.get("Workers")
        self._BatchSize = params.get("BatchSize")
        self._BatchDelay = params.get("BatchDelay")
        self._QueueType = params.get("QueueType")
        self._QueueMaxBytes = params.get("QueueMaxBytes")
        self._QueueCheckPointWrites = params.get("QueueCheckPointWrites")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashPipelineInfo(AbstractModel):
    """Logstash管道信息

    """

    def __init__(self):
        r"""
        :param _PipelineId: 管道ID
        :type PipelineId: str
        :param _PipelineDesc: 管道描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PipelineDesc: str
        :param _Config: 管道配置内容
        :type Config: str
        :param _Status: 管道状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Workers: 管道的Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Workers: int
        :param _BatchSize: 管道批处理大小
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchSize: int
        :param _BatchDelay: 管道批处理延迟
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchDelay: int
        :param _QueueType: 管道缓冲队列类型
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueType: str
        :param _QueueMaxBytes: 管道缓冲队列大小
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueMaxBytes: str
        :param _QueueCheckPointWrites: 管道缓冲队列检查点写入数
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueCheckPointWrites: int
        """
        self._PipelineId = None
        self._PipelineDesc = None
        self._Config = None
        self._Status = None
        self._Workers = None
        self._BatchSize = None
        self._BatchDelay = None
        self._QueueType = None
        self._QueueMaxBytes = None
        self._QueueCheckPointWrites = None

    @property
    def PipelineId(self):
        """管道ID
        :rtype: str
        """
        return self._PipelineId

    @PipelineId.setter
    def PipelineId(self, PipelineId):
        self._PipelineId = PipelineId

    @property
    def PipelineDesc(self):
        """管道描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PipelineDesc

    @PipelineDesc.setter
    def PipelineDesc(self, PipelineDesc):
        self._PipelineDesc = PipelineDesc

    @property
    def Config(self):
        """管道配置内容
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Status(self):
        """管道状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Workers(self):
        """管道的Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Workers

    @Workers.setter
    def Workers(self, Workers):
        self._Workers = Workers

    @property
    def BatchSize(self):
        """管道批处理大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def BatchDelay(self):
        """管道批处理延迟
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BatchDelay

    @BatchDelay.setter
    def BatchDelay(self, BatchDelay):
        self._BatchDelay = BatchDelay

    @property
    def QueueType(self):
        """管道缓冲队列类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def QueueMaxBytes(self):
        """管道缓冲队列大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueueMaxBytes

    @QueueMaxBytes.setter
    def QueueMaxBytes(self, QueueMaxBytes):
        self._QueueMaxBytes = QueueMaxBytes

    @property
    def QueueCheckPointWrites(self):
        """管道缓冲队列检查点写入数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._QueueCheckPointWrites

    @QueueCheckPointWrites.setter
    def QueueCheckPointWrites(self, QueueCheckPointWrites):
        self._QueueCheckPointWrites = QueueCheckPointWrites


    def _deserialize(self, params):
        self._PipelineId = params.get("PipelineId")
        self._PipelineDesc = params.get("PipelineDesc")
        self._Config = params.get("Config")
        self._Status = params.get("Status")
        self._Workers = params.get("Workers")
        self._BatchSize = params.get("BatchSize")
        self._BatchDelay = params.get("BatchDelay")
        self._QueueType = params.get("QueueType")
        self._QueueMaxBytes = params.get("QueueMaxBytes")
        self._QueueCheckPointWrites = params.get("QueueCheckPointWrites")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MasterNodeInfo(AbstractModel):
    """实例专用主节点相关信息

    """

    def __init__(self):
        r"""
        :param _EnableDedicatedMaster: 是否启用了专用主节点
        :type EnableDedicatedMaster: bool
        :param _MasterNodeType: 专用主节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type MasterNodeType: str
        :param _MasterNodeNum: 专用主节点个数
        :type MasterNodeNum: int
        :param _MasterNodeCpuNum: 专用主节点CPU核数
        :type MasterNodeCpuNum: int
        :param _MasterNodeMemSize: 专用主节点内存大小，单位GB
        :type MasterNodeMemSize: int
        :param _MasterNodeDiskSize: 专用主节点磁盘大小，单位GB
        :type MasterNodeDiskSize: int
        :param _MasterNodeDiskType: 专用主节点磁盘类型
        :type MasterNodeDiskType: str
        """
        self._EnableDedicatedMaster = None
        self._MasterNodeType = None
        self._MasterNodeNum = None
        self._MasterNodeCpuNum = None
        self._MasterNodeMemSize = None
        self._MasterNodeDiskSize = None
        self._MasterNodeDiskType = None

    @property
    def EnableDedicatedMaster(self):
        """是否启用了专用主节点
        :rtype: bool
        """
        return self._EnableDedicatedMaster

    @EnableDedicatedMaster.setter
    def EnableDedicatedMaster(self, EnableDedicatedMaster):
        self._EnableDedicatedMaster = EnableDedicatedMaster

    @property
    def MasterNodeType(self):
        """专用主节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :rtype: str
        """
        return self._MasterNodeType

    @MasterNodeType.setter
    def MasterNodeType(self, MasterNodeType):
        self._MasterNodeType = MasterNodeType

    @property
    def MasterNodeNum(self):
        """专用主节点个数
        :rtype: int
        """
        return self._MasterNodeNum

    @MasterNodeNum.setter
    def MasterNodeNum(self, MasterNodeNum):
        self._MasterNodeNum = MasterNodeNum

    @property
    def MasterNodeCpuNum(self):
        """专用主节点CPU核数
        :rtype: int
        """
        return self._MasterNodeCpuNum

    @MasterNodeCpuNum.setter
    def MasterNodeCpuNum(self, MasterNodeCpuNum):
        self._MasterNodeCpuNum = MasterNodeCpuNum

    @property
    def MasterNodeMemSize(self):
        """专用主节点内存大小，单位GB
        :rtype: int
        """
        return self._MasterNodeMemSize

    @MasterNodeMemSize.setter
    def MasterNodeMemSize(self, MasterNodeMemSize):
        self._MasterNodeMemSize = MasterNodeMemSize

    @property
    def MasterNodeDiskSize(self):
        """专用主节点磁盘大小，单位GB
        :rtype: int
        """
        return self._MasterNodeDiskSize

    @MasterNodeDiskSize.setter
    def MasterNodeDiskSize(self, MasterNodeDiskSize):
        self._MasterNodeDiskSize = MasterNodeDiskSize

    @property
    def MasterNodeDiskType(self):
        """专用主节点磁盘类型
        :rtype: str
        """
        return self._MasterNodeDiskType

    @MasterNodeDiskType.setter
    def MasterNodeDiskType(self, MasterNodeDiskType):
        self._MasterNodeDiskType = MasterNodeDiskType


    def _deserialize(self, params):
        self._EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self._MasterNodeType = params.get("MasterNodeType")
        self._MasterNodeNum = params.get("MasterNodeNum")
        self._MasterNodeCpuNum = params.get("MasterNodeCpuNum")
        self._MasterNodeMemSize = params.get("MasterNodeMemSize")
        self._MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self._MasterNodeDiskType = params.get("MasterNodeDiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Metric(AbstractModel):
    """智能运维指标

    """

    def __init__(self):
        r"""
        :param _Dimensions: 指标维度族
        :type Dimensions: list of Dimension
        :param _Value: 指标值
        :type Value: float
        """
        self._Dimensions = None
        self._Value = None

    @property
    def Dimensions(self):
        """指标维度族
        :rtype: list of Dimension
        """
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def Value(self):
        """指标值
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricAllData(AbstractModel):
    """全部指标数据

    """

    def __init__(self):
        r"""
        :param _IndexTraffic: 索引流量
        :type IndexTraffic: float
        :param _Storage: 存储大小
        :type Storage: float
        :param _ReadReqTimes: 读请求次数
        :type ReadReqTimes: int
        :param _WriteReqTimes: 写请求次数
        :type WriteReqTimes: int
        :param _DocCount: 文档数量
        :type DocCount: int
        """
        self._IndexTraffic = None
        self._Storage = None
        self._ReadReqTimes = None
        self._WriteReqTimes = None
        self._DocCount = None

    @property
    def IndexTraffic(self):
        """索引流量
        :rtype: float
        """
        return self._IndexTraffic

    @IndexTraffic.setter
    def IndexTraffic(self, IndexTraffic):
        self._IndexTraffic = IndexTraffic

    @property
    def Storage(self):
        """存储大小
        :rtype: float
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def ReadReqTimes(self):
        """读请求次数
        :rtype: int
        """
        return self._ReadReqTimes

    @ReadReqTimes.setter
    def ReadReqTimes(self, ReadReqTimes):
        self._ReadReqTimes = ReadReqTimes

    @property
    def WriteReqTimes(self):
        """写请求次数
        :rtype: int
        """
        return self._WriteReqTimes

    @WriteReqTimes.setter
    def WriteReqTimes(self, WriteReqTimes):
        self._WriteReqTimes = WriteReqTimes

    @property
    def DocCount(self):
        """文档数量
        :rtype: int
        """
        return self._DocCount

    @DocCount.setter
    def DocCount(self, DocCount):
        self._DocCount = DocCount


    def _deserialize(self, params):
        self._IndexTraffic = params.get("IndexTraffic")
        self._Storage = params.get("Storage")
        self._ReadReqTimes = params.get("ReadReqTimes")
        self._WriteReqTimes = params.get("WriteReqTimes")
        self._DocCount = params.get("DocCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDetail(AbstractModel):
    """智能运维指标详情

    """

    def __init__(self):
        r"""
        :param _Key: 指标详情名
        :type Key: str
        :param _Metrics: 指标详情值
        :type Metrics: list of Metric
        """
        self._Key = None
        self._Metrics = None

    @property
    def Key(self):
        """指标详情名
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Metrics(self):
        """指标详情值
        :rtype: list of Metric
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = Metric()
                obj._deserialize(item)
                self._Metrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricMapByIndexId(AbstractModel):
    """指标数据map

    """

    def __init__(self):
        r"""
        :param _IndexId: 实例id
        :type IndexId: str
        :param _MetricAllData: 指标数据
        :type MetricAllData: :class:`tencentcloud.es.v20180416.models.MetricAllData`
        """
        self._IndexId = None
        self._MetricAllData = None

    @property
    def IndexId(self):
        """实例id
        :rtype: str
        """
        return self._IndexId

    @IndexId.setter
    def IndexId(self, IndexId):
        self._IndexId = IndexId

    @property
    def MetricAllData(self):
        """指标数据
        :rtype: :class:`tencentcloud.es.v20180416.models.MetricAllData`
        """
        return self._MetricAllData

    @MetricAllData.setter
    def MetricAllData(self, MetricAllData):
        self._MetricAllData = MetricAllData


    def _deserialize(self, params):
        self._IndexId = params.get("IndexId")
        if params.get("MetricAllData") is not None:
            self._MetricAllData = MetricAllData()
            self._MetricAllData._deserialize(params.get("MetricAllData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEsVipSecurityGroupRequest(AbstractModel):
    """ModifyEsVipSecurityGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: es集群的实例id
        :type InstanceId: str
        :param _SecurityGroupIds: 安全组id列表
        :type SecurityGroupIds: list of str
        """
        self._InstanceId = None
        self._SecurityGroupIds = None

    @property
    def InstanceId(self):
        """es集群的实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        """安全组id列表
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEsVipSecurityGroupResponse(AbstractModel):
    """ModifyEsVipSecurityGroup返回参数结构体

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


class NodeInfo(AbstractModel):
    """集群中一种节点类型（如热数据节点，冷数据节点，专用主节点等）的规格描述信息，包括节点类型，节点个数，节点规格，磁盘类型，磁盘大小等, Type不指定时默认为热数据节点；如果节点为master节点，则DiskType和DiskSize参数会被忽略（主节点无数据盘）

    """

    def __init__(self):
        r"""
        :param _NodeNum: 节点数量
        :type NodeNum: int
        :param _NodeType: 节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param _Type: 节点类型<li>hotData: 热数据节点</li>
<li>warmData: 冷数据节点</li>
<li>dedicatedMaster: 专用主节点</li>
默认值为hotData
        :type Type: str
        :param _DiskType: 节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高硬能云硬盘</li>默认值CLOUD_SSD
        :type DiskType: str
        :param _DiskSize: 节点磁盘容量（单位GB）
        :type DiskSize: int
        :param _LocalDiskInfo: 节点本地盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDiskInfo: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`
        :param _DiskCount: 节点磁盘块数
        :type DiskCount: int
        :param _DiskEncrypt: 节点磁盘是否加密 0: 不加密，1: 加密；默认不加密
        :type DiskEncrypt: int
        :param _CpuNum: cpu数目
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuNum: int
        :param _MemSize: 内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param _DiskEnhance: /
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskEnhance: int
        """
        self._NodeNum = None
        self._NodeType = None
        self._Type = None
        self._DiskType = None
        self._DiskSize = None
        self._LocalDiskInfo = None
        self._DiskCount = None
        self._DiskEncrypt = None
        self._CpuNum = None
        self._MemSize = None
        self._DiskEnhance = None

    @property
    def NodeNum(self):
        """节点数量
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def NodeType(self):
        """节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def Type(self):
        """节点类型<li>hotData: 热数据节点</li>
<li>warmData: 冷数据节点</li>
<li>dedicatedMaster: 专用主节点</li>
默认值为hotData
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DiskType(self):
        """节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高硬能云硬盘</li>默认值CLOUD_SSD
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """节点磁盘容量（单位GB）
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def LocalDiskInfo(self):
        """节点本地盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`
        """
        return self._LocalDiskInfo

    @LocalDiskInfo.setter
    def LocalDiskInfo(self, LocalDiskInfo):
        self._LocalDiskInfo = LocalDiskInfo

    @property
    def DiskCount(self):
        """节点磁盘块数
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def DiskEncrypt(self):
        """节点磁盘是否加密 0: 不加密，1: 加密；默认不加密
        :rtype: int
        """
        return self._DiskEncrypt

    @DiskEncrypt.setter
    def DiskEncrypt(self, DiskEncrypt):
        self._DiskEncrypt = DiskEncrypt

    @property
    def CpuNum(self):
        """cpu数目
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MemSize(self):
        """内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def DiskEnhance(self):
        """/
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskEnhance

    @DiskEnhance.setter
    def DiskEnhance(self, DiskEnhance):
        self._DiskEnhance = DiskEnhance


    def _deserialize(self, params):
        self._NodeNum = params.get("NodeNum")
        self._NodeType = params.get("NodeType")
        self._Type = params.get("Type")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        if params.get("LocalDiskInfo") is not None:
            self._LocalDiskInfo = LocalDiskInfo()
            self._LocalDiskInfo._deserialize(params.get("LocalDiskInfo"))
        self._DiskCount = params.get("DiskCount")
        self._DiskEncrypt = params.get("DiskEncrypt")
        self._CpuNum = params.get("CpuNum")
        self._MemSize = params.get("MemSize")
        self._DiskEnhance = params.get("DiskEnhance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeView(AbstractModel):
    """节点维度视图数据

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID
        :type NodeId: str
        :param _NodeIp: 节点IP
        :type NodeIp: str
        :param _Visible: 节点是否可见
        :type Visible: float
        :param _Break: 是否熔断
        :type Break: float
        :param _DiskSize: 节点总磁盘大小
        :type DiskSize: int
        :param _DiskUsage: 磁盘使用率
        :type DiskUsage: float
        :param _MemSize: 节点内存大小，单位GB
        :type MemSize: int
        :param _MemUsage: 内存使用率
        :type MemUsage: float
        :param _CpuNum: 节点cpu个数
        :type CpuNum: int
        :param _CpuUsage: cpu使用率
        :type CpuUsage: float
        :param _Zone: 可用区
        :type Zone: str
        :param _NodeRole: 节点角色
        :type NodeRole: str
        :param _NodeHttpIp: 节点HTTP IP
        :type NodeHttpIp: str
        :param _JvmMemUsage: JVM内存使用率
        :type JvmMemUsage: float
        :param _ShardNum: 节点分片数
        :type ShardNum: int
        :param _DiskIds: 节点上磁盘ID列表
        :type DiskIds: list of str
        :param _Hidden: 是否为隐藏可用区
        :type Hidden: bool
        :param _IsCoordinationNode: 是否充当协调节点的角色
        :type IsCoordinationNode: bool
        :param _CVMStatus: CVM运行状态
        :type CVMStatus: str
        :param _CVMDisasterRecoverGroupId: cvm绑定的置放群组的id
注意：此字段可能返回 null，表示取不到有效值。
        :type CVMDisasterRecoverGroupId: str
        :param _CVMDisasterRecoverGroupStatus: cvm绑定置放群组的状态。2: 已绑定；1: 绑定中；0: 未开启
注意：此字段可能返回 null，表示取不到有效值。
        :type CVMDisasterRecoverGroupStatus: int
        """
        self._NodeId = None
        self._NodeIp = None
        self._Visible = None
        self._Break = None
        self._DiskSize = None
        self._DiskUsage = None
        self._MemSize = None
        self._MemUsage = None
        self._CpuNum = None
        self._CpuUsage = None
        self._Zone = None
        self._NodeRole = None
        self._NodeHttpIp = None
        self._JvmMemUsage = None
        self._ShardNum = None
        self._DiskIds = None
        self._Hidden = None
        self._IsCoordinationNode = None
        self._CVMStatus = None
        self._CVMDisasterRecoverGroupId = None
        self._CVMDisasterRecoverGroupStatus = None

    @property
    def NodeId(self):
        """节点ID
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeIp(self):
        """节点IP
        :rtype: str
        """
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp

    @property
    def Visible(self):
        """节点是否可见
        :rtype: float
        """
        return self._Visible

    @Visible.setter
    def Visible(self, Visible):
        self._Visible = Visible

    @property
    def Break(self):
        """是否熔断
        :rtype: float
        """
        return self._Break

    @Break.setter
    def Break(self, Break):
        self._Break = Break

    @property
    def DiskSize(self):
        """节点总磁盘大小
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskUsage(self):
        """磁盘使用率
        :rtype: float
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def MemSize(self):
        """节点内存大小，单位GB
        :rtype: int
        """
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def MemUsage(self):
        """内存使用率
        :rtype: float
        """
        return self._MemUsage

    @MemUsage.setter
    def MemUsage(self, MemUsage):
        self._MemUsage = MemUsage

    @property
    def CpuNum(self):
        """节点cpu个数
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def CpuUsage(self):
        """cpu使用率
        :rtype: float
        """
        return self._CpuUsage

    @CpuUsage.setter
    def CpuUsage(self, CpuUsage):
        self._CpuUsage = CpuUsage

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
    def NodeRole(self):
        """节点角色
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def NodeHttpIp(self):
        """节点HTTP IP
        :rtype: str
        """
        return self._NodeHttpIp

    @NodeHttpIp.setter
    def NodeHttpIp(self, NodeHttpIp):
        self._NodeHttpIp = NodeHttpIp

    @property
    def JvmMemUsage(self):
        """JVM内存使用率
        :rtype: float
        """
        return self._JvmMemUsage

    @JvmMemUsage.setter
    def JvmMemUsage(self, JvmMemUsage):
        self._JvmMemUsage = JvmMemUsage

    @property
    def ShardNum(self):
        """节点分片数
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def DiskIds(self):
        """节点上磁盘ID列表
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Hidden(self):
        """是否为隐藏可用区
        :rtype: bool
        """
        return self._Hidden

    @Hidden.setter
    def Hidden(self, Hidden):
        self._Hidden = Hidden

    @property
    def IsCoordinationNode(self):
        """是否充当协调节点的角色
        :rtype: bool
        """
        return self._IsCoordinationNode

    @IsCoordinationNode.setter
    def IsCoordinationNode(self, IsCoordinationNode):
        self._IsCoordinationNode = IsCoordinationNode

    @property
    def CVMStatus(self):
        """CVM运行状态
        :rtype: str
        """
        return self._CVMStatus

    @CVMStatus.setter
    def CVMStatus(self, CVMStatus):
        self._CVMStatus = CVMStatus

    @property
    def CVMDisasterRecoverGroupId(self):
        """cvm绑定的置放群组的id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CVMDisasterRecoverGroupId

    @CVMDisasterRecoverGroupId.setter
    def CVMDisasterRecoverGroupId(self, CVMDisasterRecoverGroupId):
        self._CVMDisasterRecoverGroupId = CVMDisasterRecoverGroupId

    @property
    def CVMDisasterRecoverGroupStatus(self):
        """cvm绑定置放群组的状态。2: 已绑定；1: 绑定中；0: 未开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CVMDisasterRecoverGroupStatus

    @CVMDisasterRecoverGroupStatus.setter
    def CVMDisasterRecoverGroupStatus(self, CVMDisasterRecoverGroupStatus):
        self._CVMDisasterRecoverGroupStatus = CVMDisasterRecoverGroupStatus


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeIp = params.get("NodeIp")
        self._Visible = params.get("Visible")
        self._Break = params.get("Break")
        self._DiskSize = params.get("DiskSize")
        self._DiskUsage = params.get("DiskUsage")
        self._MemSize = params.get("MemSize")
        self._MemUsage = params.get("MemUsage")
        self._CpuNum = params.get("CpuNum")
        self._CpuUsage = params.get("CpuUsage")
        self._Zone = params.get("Zone")
        self._NodeRole = params.get("NodeRole")
        self._NodeHttpIp = params.get("NodeHttpIp")
        self._JvmMemUsage = params.get("JvmMemUsage")
        self._ShardNum = params.get("ShardNum")
        self._DiskIds = params.get("DiskIds")
        self._Hidden = params.get("Hidden")
        self._IsCoordinationNode = params.get("IsCoordinationNode")
        self._CVMStatus = params.get("CVMStatus")
        self._CVMDisasterRecoverGroupId = params.get("CVMDisasterRecoverGroupId")
        self._CVMDisasterRecoverGroupStatus = params.get("CVMDisasterRecoverGroupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Operation(AbstractModel):
    """ES集群操作详细信息

    """

    def __init__(self):
        r"""
        :param _Id: 操作唯一id
        :type Id: int
        :param _StartTime: 操作开始时间
        :type StartTime: str
        :param _Type: 操作类型
        :type Type: str
        :param _Detail: 操作详情
        :type Detail: :class:`tencentcloud.es.v20180416.models.OperationDetail`
        :param _Result: 操作结果
        :type Result: str
        :param _Tasks: 流程任务信息
        :type Tasks: list of TaskDetail
        :param _Progress: 操作进度
        :type Progress: float
        :param _RollbackTag: 回滚标记， 0未回滚 ，1回滚中，2已回滚
        :type RollbackTag: int
        :param _SubAccountUin: 操作者Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        """
        self._Id = None
        self._StartTime = None
        self._Type = None
        self._Detail = None
        self._Result = None
        self._Tasks = None
        self._Progress = None
        self._RollbackTag = None
        self._SubAccountUin = None

    @property
    def Id(self):
        """操作唯一id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        """操作开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """操作类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Detail(self):
        """操作详情
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDetail`
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Result(self):
        """操作结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Tasks(self):
        """流程任务信息
        :rtype: list of TaskDetail
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Progress(self):
        """操作进度
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RollbackTag(self):
        """回滚标记， 0未回滚 ，1回滚中，2已回滚
        :rtype: int
        """
        return self._RollbackTag

    @RollbackTag.setter
    def RollbackTag(self, RollbackTag):
        self._RollbackTag = RollbackTag

    @property
    def SubAccountUin(self):
        """操作者Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        if params.get("Detail") is not None:
            self._Detail = OperationDetail()
            self._Detail._deserialize(params.get("Detail"))
        self._Result = params.get("Result")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskDetail()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Progress = params.get("Progress")
        self._RollbackTag = params.get("RollbackTag")
        self._SubAccountUin = params.get("SubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDetail(AbstractModel):
    """操作详情

    """

    def __init__(self):
        r"""
        :param _OldInfo: 实例原始配置信息
        :type OldInfo: list of KeyValue
        :param _NewInfo: 实例更新后配置信息
        :type NewInfo: list of KeyValue
        """
        self._OldInfo = None
        self._NewInfo = None

    @property
    def OldInfo(self):
        """实例原始配置信息
        :rtype: list of KeyValue
        """
        return self._OldInfo

    @OldInfo.setter
    def OldInfo(self, OldInfo):
        self._OldInfo = OldInfo

    @property
    def NewInfo(self):
        """实例更新后配置信息
        :rtype: list of KeyValue
        """
        return self._NewInfo

    @NewInfo.setter
    def NewInfo(self, NewInfo):
        self._NewInfo = NewInfo


    def _deserialize(self, params):
        if params.get("OldInfo") is not None:
            self._OldInfo = []
            for item in params.get("OldInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self._OldInfo.append(obj)
        if params.get("NewInfo") is not None:
            self._NewInfo = []
            for item in params.get("NewInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self._NewInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDuration(AbstractModel):
    """集群可运维时间

    """

    def __init__(self):
        r"""
        :param _Periods: 维护周期，表示周一到周日，可取值[0, 6]
注意：此字段可能返回 null，表示取不到有效值。
        :type Periods: list of int non-negative
        :param _TimeStart: 维护开始时间
        :type TimeStart: str
        :param _TimeEnd: 维护结束时间
        :type TimeEnd: str
        :param _TimeZone: 时区，以UTC形式表示
        :type TimeZone: str
        """
        self._Periods = None
        self._TimeStart = None
        self._TimeEnd = None
        self._TimeZone = None

    @property
    def Periods(self):
        """维护周期，表示周一到周日，可取值[0, 6]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int non-negative
        """
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def TimeStart(self):
        """维护开始时间
        :rtype: str
        """
        return self._TimeStart

    @TimeStart.setter
    def TimeStart(self, TimeStart):
        self._TimeStart = TimeStart

    @property
    def TimeEnd(self):
        """维护结束时间
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def TimeZone(self):
        """时区，以UTC形式表示
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Periods = params.get("Periods")
        self._TimeStart = params.get("TimeStart")
        self._TimeEnd = params.get("TimeEnd")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDurationUpdated(AbstractModel):
    """集群可运维时间

    """

    def __init__(self):
        r"""
        :param _Periods: 维护周期，表示周一到周日，可取值[0, 6]
        :type Periods: list of int non-negative
        :param _TimeStart: 维护开始时间
        :type TimeStart: str
        :param _TimeEnd: 维护结束时间
        :type TimeEnd: str
        :param _TimeZone: 时区，以UTC形式表示
        :type TimeZone: str
        :param _MoreInstances: ES集群ID数组
        :type MoreInstances: list of str
        """
        self._Periods = None
        self._TimeStart = None
        self._TimeEnd = None
        self._TimeZone = None
        self._MoreInstances = None

    @property
    def Periods(self):
        """维护周期，表示周一到周日，可取值[0, 6]
        :rtype: list of int non-negative
        """
        return self._Periods

    @Periods.setter
    def Periods(self, Periods):
        self._Periods = Periods

    @property
    def TimeStart(self):
        """维护开始时间
        :rtype: str
        """
        return self._TimeStart

    @TimeStart.setter
    def TimeStart(self, TimeStart):
        self._TimeStart = TimeStart

    @property
    def TimeEnd(self):
        """维护结束时间
        :rtype: str
        """
        return self._TimeEnd

    @TimeEnd.setter
    def TimeEnd(self, TimeEnd):
        self._TimeEnd = TimeEnd

    @property
    def TimeZone(self):
        """时区，以UTC形式表示
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def MoreInstances(self):
        """ES集群ID数组
        :rtype: list of str
        """
        return self._MoreInstances

    @MoreInstances.setter
    def MoreInstances(self, MoreInstances):
        self._MoreInstances = MoreInstances


    def _deserialize(self, params):
        self._Periods = params.get("Periods")
        self._TimeStart = params.get("TimeStart")
        self._TimeEnd = params.get("TimeEnd")
        self._TimeZone = params.get("TimeZone")
        self._MoreInstances = params.get("MoreInstances")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OptionalWebServiceInfo(AbstractModel):
    """可选web组件信息

    """

    def __init__(self):
        r"""
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _PublicUrl: 公网url
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicUrl: str
        :param _PrivateUrl: 内网url
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateUrl: str
        :param _PublicAccess: 公网访问权限
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicAccess: str
        :param _PrivateAccess: 内网访问权限
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateAccess: str
        :param _Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _PrivateVip: web服务内网vip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateVip: str
        :param _CustomPrivateUrl: 自定义cerebro内网url
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomPrivateUrl: str
        """
        self._Type = None
        self._Status = None
        self._PublicUrl = None
        self._PrivateUrl = None
        self._PublicAccess = None
        self._PrivateAccess = None
        self._Version = None
        self._PrivateVip = None
        self._CustomPrivateUrl = None

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
    def PublicUrl(self):
        """公网url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicUrl

    @PublicUrl.setter
    def PublicUrl(self, PublicUrl):
        self._PublicUrl = PublicUrl

    @property
    def PrivateUrl(self):
        """内网url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateUrl

    @PrivateUrl.setter
    def PrivateUrl(self, PrivateUrl):
        self._PrivateUrl = PrivateUrl

    @property
    def PublicAccess(self):
        """公网访问权限
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicAccess

    @PublicAccess.setter
    def PublicAccess(self, PublicAccess):
        self._PublicAccess = PublicAccess

    @property
    def PrivateAccess(self):
        """内网访问权限
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateAccess

    @PrivateAccess.setter
    def PrivateAccess(self, PrivateAccess):
        self._PrivateAccess = PrivateAccess

    @property
    def Version(self):
        """版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def PrivateVip(self):
        """web服务内网vip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateVip

    @PrivateVip.setter
    def PrivateVip(self, PrivateVip):
        self._PrivateVip = PrivateVip

    @property
    def CustomPrivateUrl(self):
        """自定义cerebro内网url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CustomPrivateUrl

    @CustomPrivateUrl.setter
    def CustomPrivateUrl(self, CustomPrivateUrl):
        self._CustomPrivateUrl = CustomPrivateUrl


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._PublicUrl = params.get("PublicUrl")
        self._PrivateUrl = params.get("PrivateUrl")
        self._PublicAccess = params.get("PublicAccess")
        self._PrivateAccess = params.get("PrivateAccess")
        self._Version = params.get("Version")
        self._PrivateVip = params.get("PrivateVip")
        self._CustomPrivateUrl = params.get("CustomPrivateUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutboundPublicAcl(AbstractModel):
    """节点出站访问信息

    """

    def __init__(self):
        r"""
        :param _NodeType: 允许节点出站访问的节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param _WhiteHostList: 允许节点出站访问的白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type WhiteHostList: list of str
        """
        self._NodeType = None
        self._WhiteHostList = None

    @property
    def NodeType(self):
        """允许节点出站访问的节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def WhiteHostList(self):
        """允许节点出站访问的白名单
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._WhiteHostList

    @WhiteHostList.setter
    def WhiteHostList(self, WhiteHostList):
        self._WhiteHostList = WhiteHostList


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._WhiteHostList = params.get("WhiteHostList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessDetail(AbstractModel):
    """任务进度详情

    """

    def __init__(self):
        r"""
        :param _Completed: 已完成数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Completed: int
        :param _Remain: 剩余数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Remain: int
        :param _Total: 总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _TaskType: 任务类型：
60：重启型任务
70：分片迁移型任务
80：节点变配任务
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: int
        """
        self._Completed = None
        self._Remain = None
        self._Total = None
        self._TaskType = None

    @property
    def Completed(self):
        """已完成数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Completed

    @Completed.setter
    def Completed(self, Completed):
        self._Completed = Completed

    @property
    def Remain(self):
        """剩余数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Remain

    @Remain.setter
    def Remain(self, Remain):
        self._Remain = Remain

    @property
    def Total(self):
        """总数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TaskType(self):
        """任务类型：
60：重启型任务
70：分片迁移型任务
80：节点变配任务
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._Completed = params.get("Completed")
        self._Remain = params.get("Remain")
        self._Total = params.get("Total")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceRequest(AbstractModel):
    """RestartInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ForceRestart: 是否强制重启<li>true：强制重启</li><li>false：不强制重启</li>默认false
        :type ForceRestart: bool
        :param _RestartMode: 重启模式：0 滚动重启； 1 全量重启
        :type RestartMode: int
        :param _UpgradeKernel: 重启时选择是否升级内核patch版本
        :type UpgradeKernel: bool
        """
        self._InstanceId = None
        self._ForceRestart = None
        self._RestartMode = None
        self._UpgradeKernel = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ForceRestart(self):
        """是否强制重启<li>true：强制重启</li><li>false：不强制重启</li>默认false
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def RestartMode(self):
        """重启模式：0 滚动重启； 1 全量重启
        :rtype: int
        """
        return self._RestartMode

    @RestartMode.setter
    def RestartMode(self, RestartMode):
        self._RestartMode = RestartMode

    @property
    def UpgradeKernel(self):
        """重启时选择是否升级内核patch版本
        :rtype: bool
        """
        return self._UpgradeKernel

    @UpgradeKernel.setter
    def UpgradeKernel(self, UpgradeKernel):
        self._UpgradeKernel = UpgradeKernel


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ForceRestart = params.get("ForceRestart")
        self._RestartMode = params.get("RestartMode")
        self._UpgradeKernel = params.get("UpgradeKernel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceResponse(AbstractModel):
    """RestartInstance返回参数结构体

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


class RestartKibanaRequest(AbstractModel):
    """RestartKibana请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """ES实例ID
        :rtype: str
        """
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
        


class RestartKibanaResponse(AbstractModel):
    """RestartKibana返回参数结构体

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


class RestartLogstashInstanceRequest(AbstractModel):
    """RestartLogstashInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Type: 重启类型，0全量重启，1滚动重启
        :type Type: int
        """
        self._InstanceId = None
        self._Type = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """重启类型，0全量重启，1滚动重启
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartLogstashInstanceResponse(AbstractModel):
    """RestartLogstashInstance返回参数结构体

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


class RestartNodesRequest(AbstractModel):
    """RestartNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        :param _NodeNames: 节点名称列表
        :type NodeNames: list of str
        :param _ForceRestart: 是否强制重启
        :type ForceRestart: bool
        :param _RestartMode: 可选重启模式"in-place","blue-green"，分别表示重启，蓝绿重启；默认值为"in-place"
        :type RestartMode: str
        :param _IsOffline: 节点状态，在蓝绿模式中使用；离线节点蓝绿有风险
        :type IsOffline: bool
        :param _CvmDelayOnlineTime: cvm延迟上架时间
        :type CvmDelayOnlineTime: int
        :param _ShardAllocationConcurrents: 分片迁移并发数
        :type ShardAllocationConcurrents: int
        :param _ShardAllocationBytes: 分片迁移并发速度
        :type ShardAllocationBytes: int
        :param _EnableScheduleRecoverGroup: 是否开启置放群组异步任务
        :type EnableScheduleRecoverGroup: bool
        :param _EnableScheduleOperationDuration: 置放群组异步任务时间段
        :type EnableScheduleOperationDuration: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        self._InstanceId = None
        self._NodeNames = None
        self._ForceRestart = None
        self._RestartMode = None
        self._IsOffline = None
        self._CvmDelayOnlineTime = None
        self._ShardAllocationConcurrents = None
        self._ShardAllocationBytes = None
        self._EnableScheduleRecoverGroup = None
        self._EnableScheduleOperationDuration = None

    @property
    def InstanceId(self):
        """集群实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeNames(self):
        """节点名称列表
        :rtype: list of str
        """
        return self._NodeNames

    @NodeNames.setter
    def NodeNames(self, NodeNames):
        self._NodeNames = NodeNames

    @property
    def ForceRestart(self):
        """是否强制重启
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def RestartMode(self):
        """可选重启模式"in-place","blue-green"，分别表示重启，蓝绿重启；默认值为"in-place"
        :rtype: str
        """
        return self._RestartMode

    @RestartMode.setter
    def RestartMode(self, RestartMode):
        self._RestartMode = RestartMode

    @property
    def IsOffline(self):
        """节点状态，在蓝绿模式中使用；离线节点蓝绿有风险
        :rtype: bool
        """
        return self._IsOffline

    @IsOffline.setter
    def IsOffline(self, IsOffline):
        self._IsOffline = IsOffline

    @property
    def CvmDelayOnlineTime(self):
        """cvm延迟上架时间
        :rtype: int
        """
        return self._CvmDelayOnlineTime

    @CvmDelayOnlineTime.setter
    def CvmDelayOnlineTime(self, CvmDelayOnlineTime):
        self._CvmDelayOnlineTime = CvmDelayOnlineTime

    @property
    def ShardAllocationConcurrents(self):
        """分片迁移并发数
        :rtype: int
        """
        return self._ShardAllocationConcurrents

    @ShardAllocationConcurrents.setter
    def ShardAllocationConcurrents(self, ShardAllocationConcurrents):
        self._ShardAllocationConcurrents = ShardAllocationConcurrents

    @property
    def ShardAllocationBytes(self):
        """分片迁移并发速度
        :rtype: int
        """
        return self._ShardAllocationBytes

    @ShardAllocationBytes.setter
    def ShardAllocationBytes(self, ShardAllocationBytes):
        self._ShardAllocationBytes = ShardAllocationBytes

    @property
    def EnableScheduleRecoverGroup(self):
        """是否开启置放群组异步任务
        :rtype: bool
        """
        return self._EnableScheduleRecoverGroup

    @EnableScheduleRecoverGroup.setter
    def EnableScheduleRecoverGroup(self, EnableScheduleRecoverGroup):
        self._EnableScheduleRecoverGroup = EnableScheduleRecoverGroup

    @property
    def EnableScheduleOperationDuration(self):
        """置放群组异步任务时间段
        :rtype: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        return self._EnableScheduleOperationDuration

    @EnableScheduleOperationDuration.setter
    def EnableScheduleOperationDuration(self, EnableScheduleOperationDuration):
        self._EnableScheduleOperationDuration = EnableScheduleOperationDuration


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeNames = params.get("NodeNames")
        self._ForceRestart = params.get("ForceRestart")
        self._RestartMode = params.get("RestartMode")
        self._IsOffline = params.get("IsOffline")
        self._CvmDelayOnlineTime = params.get("CvmDelayOnlineTime")
        self._ShardAllocationConcurrents = params.get("ShardAllocationConcurrents")
        self._ShardAllocationBytes = params.get("ShardAllocationBytes")
        self._EnableScheduleRecoverGroup = params.get("EnableScheduleRecoverGroup")
        if params.get("EnableScheduleOperationDuration") is not None:
            self._EnableScheduleOperationDuration = EnableScheduleOperationDuration()
            self._EnableScheduleOperationDuration._deserialize(params.get("EnableScheduleOperationDuration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartNodesResponse(AbstractModel):
    """RestartNodes返回参数结构体

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


class RestoreClusterSnapshotRequest(AbstractModel):
    """RestoreClusterSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id，格式：es-xxxx
        :type InstanceId: str
        :param _RepositoryName: 仓库名称
        :type RepositoryName: str
        :param _SnapshotName: 集群快照名称
        :type SnapshotName: str
        :param _TargetInstanceId: 目标集群实例Id，格式：es-xxxx，如果是恢复到本地，则和InstanceId一致
        :type TargetInstanceId: str
        :param _Password: elastic用户名对应的密码信息
        :type Password: str
        :param _IndexSettings: 要在所有恢复的索引中添加或更改的设置的逗号分隔列表。使用此参数可以在恢复快照时覆盖索引设置。
        :type IndexSettings: str
        :param _IncludeGlobalState: 不应从快照还原的以逗号分隔的索引设置列表。
        :type IncludeGlobalState: list of str
        :param _Indices: 需要恢复的索引名称，非必填，为空则表示恢复所有

支持传多个索引名称
        :type Indices: str
        :param _Partial: 如果为 false，则如果快照中包含的一个或多个索引没有所有主分片可用，则整个恢复操作将失败。默认为 false,

如果为 true，则允许恢复具有不可用分片的索引的部分快照。只有成功包含在快照中的分片才会被恢复。所有丢失的碎片将被重新创建为空
        :type Partial: str
        """
        self._InstanceId = None
        self._RepositoryName = None
        self._SnapshotName = None
        self._TargetInstanceId = None
        self._Password = None
        self._IndexSettings = None
        self._IncludeGlobalState = None
        self._Indices = None
        self._Partial = None

    @property
    def InstanceId(self):
        """集群实例Id，格式：es-xxxx
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RepositoryName(self):
        """仓库名称
        :rtype: str
        """
        return self._RepositoryName

    @RepositoryName.setter
    def RepositoryName(self, RepositoryName):
        self._RepositoryName = RepositoryName

    @property
    def SnapshotName(self):
        """集群快照名称
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def TargetInstanceId(self):
        """目标集群实例Id，格式：es-xxxx，如果是恢复到本地，则和InstanceId一致
        :rtype: str
        """
        return self._TargetInstanceId

    @TargetInstanceId.setter
    def TargetInstanceId(self, TargetInstanceId):
        self._TargetInstanceId = TargetInstanceId

    @property
    def Password(self):
        """elastic用户名对应的密码信息
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def IndexSettings(self):
        """要在所有恢复的索引中添加或更改的设置的逗号分隔列表。使用此参数可以在恢复快照时覆盖索引设置。
        :rtype: str
        """
        return self._IndexSettings

    @IndexSettings.setter
    def IndexSettings(self, IndexSettings):
        self._IndexSettings = IndexSettings

    @property
    def IncludeGlobalState(self):
        """不应从快照还原的以逗号分隔的索引设置列表。
        :rtype: list of str
        """
        return self._IncludeGlobalState

    @IncludeGlobalState.setter
    def IncludeGlobalState(self, IncludeGlobalState):
        self._IncludeGlobalState = IncludeGlobalState

    @property
    def Indices(self):
        """需要恢复的索引名称，非必填，为空则表示恢复所有

支持传多个索引名称
        :rtype: str
        """
        return self._Indices

    @Indices.setter
    def Indices(self, Indices):
        self._Indices = Indices

    @property
    def Partial(self):
        """如果为 false，则如果快照中包含的一个或多个索引没有所有主分片可用，则整个恢复操作将失败。默认为 false,

如果为 true，则允许恢复具有不可用分片的索引的部分快照。只有成功包含在快照中的分片才会被恢复。所有丢失的碎片将被重新创建为空
        :rtype: str
        """
        return self._Partial

    @Partial.setter
    def Partial(self, Partial):
        self._Partial = Partial


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RepositoryName = params.get("RepositoryName")
        self._SnapshotName = params.get("SnapshotName")
        self._TargetInstanceId = params.get("TargetInstanceId")
        self._Password = params.get("Password")
        self._IndexSettings = params.get("IndexSettings")
        self._IncludeGlobalState = params.get("IncludeGlobalState")
        self._Indices = params.get("Indices")
        self._Partial = params.get("Partial")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreClusterSnapshotResponse(AbstractModel):
    """RestoreClusterSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例id
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """集群实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class SaveAndDeployLogstashPipelineRequest(AbstractModel):
    """SaveAndDeployLogstashPipeline请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Pipeline: 实例管道信息
        :type Pipeline: :class:`tencentcloud.es.v20180416.models.LogstashPipeline`
        :param _OpType: 操作类型<li>1：只保存</li><li>2：保存并部署</li>
        :type OpType: int
        """
        self._InstanceId = None
        self._Pipeline = None
        self._OpType = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Pipeline(self):
        """实例管道信息
        :rtype: :class:`tencentcloud.es.v20180416.models.LogstashPipeline`
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def OpType(self):
        """操作类型<li>1：只保存</li><li>2：保存并部署</li>
        :rtype: int
        """
        return self._OpType

    @OpType.setter
    def OpType(self, OpType):
        self._OpType = OpType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Pipeline") is not None:
            self._Pipeline = LogstashPipeline()
            self._Pipeline._deserialize(params.get("Pipeline"))
        self._OpType = params.get("OpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveAndDeployLogstashPipelineResponse(AbstractModel):
    """SaveAndDeployLogstashPipeline返回参数结构体

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


class ServerlessDi(AbstractModel):
    """创建serverless索引时创建数据接入

    """

    def __init__(self):
        r"""
        :param _DiSourceType: 数据链路采集源类型，如cvm_collector、tke_collector
        :type DiSourceType: str
        :param _DiSourceCvm: cvm数据源
        :type DiSourceCvm: :class:`tencentcloud.es.v20180416.models.DiSourceCvm`
        :param _DiSourceTke: tke数据源
        :type DiSourceTke: :class:`tencentcloud.es.v20180416.models.DiSourceTke`
        """
        self._DiSourceType = None
        self._DiSourceCvm = None
        self._DiSourceTke = None

    @property
    def DiSourceType(self):
        """数据链路采集源类型，如cvm_collector、tke_collector
        :rtype: str
        """
        return self._DiSourceType

    @DiSourceType.setter
    def DiSourceType(self, DiSourceType):
        self._DiSourceType = DiSourceType

    @property
    def DiSourceCvm(self):
        """cvm数据源
        :rtype: :class:`tencentcloud.es.v20180416.models.DiSourceCvm`
        """
        return self._DiSourceCvm

    @DiSourceCvm.setter
    def DiSourceCvm(self, DiSourceCvm):
        self._DiSourceCvm = DiSourceCvm

    @property
    def DiSourceTke(self):
        """tke数据源
        :rtype: :class:`tencentcloud.es.v20180416.models.DiSourceTke`
        """
        return self._DiSourceTke

    @DiSourceTke.setter
    def DiSourceTke(self, DiSourceTke):
        self._DiSourceTke = DiSourceTke


    def _deserialize(self, params):
        self._DiSourceType = params.get("DiSourceType")
        if params.get("DiSourceCvm") is not None:
            self._DiSourceCvm = DiSourceCvm()
            self._DiSourceCvm._deserialize(params.get("DiSourceCvm"))
        if params.get("DiSourceTke") is not None:
            self._DiSourceTke = DiSourceTke()
            self._DiSourceTke._deserialize(params.get("DiSourceTke"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessIndexMetaField(AbstractModel):
    """索引元数据字段

    """

    def __init__(self):
        r"""
        :param _AppId: 索引所属集群APP ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _IndexName: 索引名
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexName: str
        :param _IndexMetaJson: 索引元数据JSON
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexMetaJson: str
        :param _IndexDocs: 索引文档数
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexDocs: int
        :param _IndexStorage: 索引存储大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStorage: int
        :param _IndexCreateTime: 索引创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexCreateTime: str
        :param _InstanceId: 索引实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _IndexOptionsField: 索引自治字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexOptionsField: :class:`tencentcloud.es.v20180416.models.ServerlessIndexOptionsField`
        :param _IndexSettingsField: 索引配置字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexSettingsField: :class:`tencentcloud.es.v20180416.models.ServerlessIndexSettingsField`
        :param _IndexNetworkField: 索引所属连接相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexNetworkField: :class:`tencentcloud.es.v20180416.models.ServerlessIndexNetworkField`
        :param _KibanaUrl: Kibana公网域名
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaUrl: str
        :param _KibanaPrivateUrl: Kibana内网域名
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaPrivateUrl: str
        :param _IndexAccessUrl: 索引内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexAccessUrl: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _SpaceId: 索引空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SpaceId: str
        :param _SpaceName: 索引空间名
注意：此字段可能返回 null，表示取不到有效值。
        :type SpaceName: str
        :param _StorageType: 存储类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param _TagList: 标签信息
        :type TagList: list of TagInfo
        :param _IndexTraffic: 3782478.47
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexTraffic: float
        """
        self._AppId = None
        self._IndexName = None
        self._IndexMetaJson = None
        self._IndexDocs = None
        self._IndexStorage = None
        self._IndexCreateTime = None
        self._InstanceId = None
        self._IndexOptionsField = None
        self._IndexSettingsField = None
        self._IndexNetworkField = None
        self._KibanaUrl = None
        self._KibanaPrivateUrl = None
        self._IndexAccessUrl = None
        self._Status = None
        self._SpaceId = None
        self._SpaceName = None
        self._StorageType = None
        self._TagList = None
        self._IndexTraffic = None

    @property
    def AppId(self):
        """索引所属集群APP ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def IndexName(self):
        """索引名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def IndexMetaJson(self):
        """索引元数据JSON
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexMetaJson

    @IndexMetaJson.setter
    def IndexMetaJson(self, IndexMetaJson):
        self._IndexMetaJson = IndexMetaJson

    @property
    def IndexDocs(self):
        """索引文档数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IndexDocs

    @IndexDocs.setter
    def IndexDocs(self, IndexDocs):
        self._IndexDocs = IndexDocs

    @property
    def IndexStorage(self):
        """索引存储大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IndexStorage

    @IndexStorage.setter
    def IndexStorage(self, IndexStorage):
        self._IndexStorage = IndexStorage

    @property
    def IndexCreateTime(self):
        """索引创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexCreateTime

    @IndexCreateTime.setter
    def IndexCreateTime(self, IndexCreateTime):
        self._IndexCreateTime = IndexCreateTime

    @property
    def InstanceId(self):
        """索引实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexOptionsField(self):
        """索引自治字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.ServerlessIndexOptionsField`
        """
        return self._IndexOptionsField

    @IndexOptionsField.setter
    def IndexOptionsField(self, IndexOptionsField):
        self._IndexOptionsField = IndexOptionsField

    @property
    def IndexSettingsField(self):
        """索引配置字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.ServerlessIndexSettingsField`
        """
        return self._IndexSettingsField

    @IndexSettingsField.setter
    def IndexSettingsField(self, IndexSettingsField):
        self._IndexSettingsField = IndexSettingsField

    @property
    def IndexNetworkField(self):
        """索引所属连接相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.ServerlessIndexNetworkField`
        """
        return self._IndexNetworkField

    @IndexNetworkField.setter
    def IndexNetworkField(self, IndexNetworkField):
        self._IndexNetworkField = IndexNetworkField

    @property
    def KibanaUrl(self):
        """Kibana公网域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaUrl

    @KibanaUrl.setter
    def KibanaUrl(self, KibanaUrl):
        self._KibanaUrl = KibanaUrl

    @property
    def KibanaPrivateUrl(self):
        """Kibana内网域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaPrivateUrl

    @KibanaPrivateUrl.setter
    def KibanaPrivateUrl(self, KibanaPrivateUrl):
        self._KibanaPrivateUrl = KibanaPrivateUrl

    @property
    def IndexAccessUrl(self):
        """索引内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexAccessUrl

    @IndexAccessUrl.setter
    def IndexAccessUrl(self, IndexAccessUrl):
        self._IndexAccessUrl = IndexAccessUrl

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
    def SpaceId(self):
        """索引空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def SpaceName(self):
        """索引空间名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def StorageType(self):
        """存储类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def TagList(self):
        """标签信息
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def IndexTraffic(self):
        """3782478.47
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._IndexTraffic

    @IndexTraffic.setter
    def IndexTraffic(self, IndexTraffic):
        self._IndexTraffic = IndexTraffic


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._IndexName = params.get("IndexName")
        self._IndexMetaJson = params.get("IndexMetaJson")
        self._IndexDocs = params.get("IndexDocs")
        self._IndexStorage = params.get("IndexStorage")
        self._IndexCreateTime = params.get("IndexCreateTime")
        self._InstanceId = params.get("InstanceId")
        if params.get("IndexOptionsField") is not None:
            self._IndexOptionsField = ServerlessIndexOptionsField()
            self._IndexOptionsField._deserialize(params.get("IndexOptionsField"))
        if params.get("IndexSettingsField") is not None:
            self._IndexSettingsField = ServerlessIndexSettingsField()
            self._IndexSettingsField._deserialize(params.get("IndexSettingsField"))
        if params.get("IndexNetworkField") is not None:
            self._IndexNetworkField = ServerlessIndexNetworkField()
            self._IndexNetworkField._deserialize(params.get("IndexNetworkField"))
        self._KibanaUrl = params.get("KibanaUrl")
        self._KibanaPrivateUrl = params.get("KibanaPrivateUrl")
        self._IndexAccessUrl = params.get("IndexAccessUrl")
        self._Status = params.get("Status")
        self._SpaceId = params.get("SpaceId")
        self._SpaceName = params.get("SpaceName")
        self._StorageType = params.get("StorageType")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._IndexTraffic = params.get("IndexTraffic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessIndexNetworkField(AbstractModel):
    """Serverless实例，网络、索引、kibana等连接信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Zone: 区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _VpcUid: vpc唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcUid: str
        :param _SubnetUid: 子网唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetUid: str
        :param _Username: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Username: str
        :param _Password: 密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        """
        self._Region = None
        self._Zone = None
        self._VpcUid = None
        self._SubnetUid = None
        self._Username = None
        self._Password = None

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
        """区域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcUid(self):
        """vpc唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcUid

    @VpcUid.setter
    def VpcUid(self, VpcUid):
        self._VpcUid = VpcUid

    @property
    def SubnetUid(self):
        """子网唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetUid

    @SubnetUid.setter
    def SubnetUid(self, SubnetUid):
        self._SubnetUid = SubnetUid

    @property
    def Username(self):
        """用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """密码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcUid = params.get("VpcUid")
        self._SubnetUid = params.get("SubnetUid")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessIndexOptionsField(AbstractModel):
    """索引自治字段

    """

    def __init__(self):
        r"""
        :param _ExpireMaxAge: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireMaxAge: str
        :param _TimestampField: 时间分区字段
注意：此字段可能返回 null，表示取不到有效值。
        :type TimestampField: str
        :param _SinkCycleAge: 标准存储时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SinkCycleAge: str
        :param _StandardStorageAge: 标准存储时长
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardStorageAge: str
        """
        self._ExpireMaxAge = None
        self._TimestampField = None
        self._SinkCycleAge = None
        self._StandardStorageAge = None

    @property
    def ExpireMaxAge(self):
        """过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireMaxAge

    @ExpireMaxAge.setter
    def ExpireMaxAge(self, ExpireMaxAge):
        self._ExpireMaxAge = ExpireMaxAge

    @property
    def TimestampField(self):
        """时间分区字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimestampField

    @TimestampField.setter
    def TimestampField(self, TimestampField):
        self._TimestampField = TimestampField

    @property
    def SinkCycleAge(self):
        """标准存储时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SinkCycleAge

    @SinkCycleAge.setter
    def SinkCycleAge(self, SinkCycleAge):
        self._SinkCycleAge = SinkCycleAge

    @property
    def StandardStorageAge(self):
        """标准存储时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StandardStorageAge

    @StandardStorageAge.setter
    def StandardStorageAge(self, StandardStorageAge):
        self._StandardStorageAge = StandardStorageAge


    def _deserialize(self, params):
        self._ExpireMaxAge = params.get("ExpireMaxAge")
        self._TimestampField = params.get("TimestampField")
        self._SinkCycleAge = params.get("SinkCycleAge")
        self._StandardStorageAge = params.get("StandardStorageAge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessIndexSettingsField(AbstractModel):
    """索引配置字段

    """

    def __init__(self):
        r"""
        :param _NumberOfShards: 索引主分片数
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfShards: str
        :param _RefreshInterval: 索引刷新频率
注意：此字段可能返回 null，表示取不到有效值。
        :type RefreshInterval: str
        :param _CustomSetting: 自定义参数
        :type CustomSetting: str
        """
        self._NumberOfShards = None
        self._RefreshInterval = None
        self._CustomSetting = None

    @property
    def NumberOfShards(self):
        """索引主分片数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NumberOfShards

    @NumberOfShards.setter
    def NumberOfShards(self, NumberOfShards):
        self._NumberOfShards = NumberOfShards

    @property
    def RefreshInterval(self):
        """索引刷新频率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RefreshInterval

    @RefreshInterval.setter
    def RefreshInterval(self, RefreshInterval):
        self._RefreshInterval = RefreshInterval

    @property
    def CustomSetting(self):
        """自定义参数
        :rtype: str
        """
        return self._CustomSetting

    @CustomSetting.setter
    def CustomSetting(self, CustomSetting):
        self._CustomSetting = CustomSetting


    def _deserialize(self, params):
        self._NumberOfShards = params.get("NumberOfShards")
        self._RefreshInterval = params.get("RefreshInterval")
        self._CustomSetting = params.get("CustomSetting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessSpace(AbstractModel):
    """Serverless索引空间信息

    """

    def __init__(self):
        r"""
        :param _SpaceId: Serverless索引空间ID
        :type SpaceId: str
        :param _SpaceName: Serverless索引空间名
        :type SpaceName: str
        :param _Status: Serverless索引空间状态，0正常，-1已删除
        :type Status: int
        :param _CreateTime: 创建日期
        :type CreateTime: str
        :param _IndexCount: 空间内索引数量
        :type IndexCount: int
        :param _KibanaUrl: kibana公网uri
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaUrl: str
        :param _KibanaPrivateUrl: kibana内网url
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaPrivateUrl: str
        :param _IndexAccessUrl: 空间内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexAccessUrl: str
        :param _KibanaPublicAcl: 空间白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaPublicAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param _KibanaEmbedUrl: 空间检索分析域名
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaEmbedUrl: str
        :param _DiDataList: 数据联路
注意：此字段可能返回 null，表示取不到有效值。
        :type DiDataList: :class:`tencentcloud.es.v20180416.models.DiData`
        :param _VpcInfo: 空间vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcInfo: list of VpcInfo
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _EnableKibanaPublicAccess: kibana公网开关，0关闭，1开启
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableKibanaPublicAccess: int
        :param _EnableKibanaPrivateAccess: kibana内网开关，0关闭，1开启
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableKibanaPrivateAccess: int
        :param _AppId: 空间所属appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _KibanaLanguage: //默认en， 可选zh-CN
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaLanguage: str
        :param _ClusterType: 0
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: int
        :param _TagList: key:value
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of TagInfo
        """
        self._SpaceId = None
        self._SpaceName = None
        self._Status = None
        self._CreateTime = None
        self._IndexCount = None
        self._KibanaUrl = None
        self._KibanaPrivateUrl = None
        self._IndexAccessUrl = None
        self._KibanaPublicAcl = None
        self._KibanaEmbedUrl = None
        self._DiDataList = None
        self._VpcInfo = None
        self._Region = None
        self._Zone = None
        self._EnableKibanaPublicAccess = None
        self._EnableKibanaPrivateAccess = None
        self._AppId = None
        self._KibanaLanguage = None
        self._ClusterType = None
        self._TagList = None

    @property
    def SpaceId(self):
        """Serverless索引空间ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def SpaceName(self):
        """Serverless索引空间名
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def Status(self):
        """Serverless索引空间状态，0正常，-1已删除
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建日期
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IndexCount(self):
        """空间内索引数量
        :rtype: int
        """
        return self._IndexCount

    @IndexCount.setter
    def IndexCount(self, IndexCount):
        self._IndexCount = IndexCount

    @property
    def KibanaUrl(self):
        """kibana公网uri
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaUrl

    @KibanaUrl.setter
    def KibanaUrl(self, KibanaUrl):
        self._KibanaUrl = KibanaUrl

    @property
    def KibanaPrivateUrl(self):
        """kibana内网url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaPrivateUrl

    @KibanaPrivateUrl.setter
    def KibanaPrivateUrl(self, KibanaPrivateUrl):
        self._KibanaPrivateUrl = KibanaPrivateUrl

    @property
    def IndexAccessUrl(self):
        """空间内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexAccessUrl

    @IndexAccessUrl.setter
    def IndexAccessUrl(self, IndexAccessUrl):
        self._IndexAccessUrl = IndexAccessUrl

    @property
    def KibanaPublicAcl(self):
        """空间白名单
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._KibanaPublicAcl

    @KibanaPublicAcl.setter
    def KibanaPublicAcl(self, KibanaPublicAcl):
        self._KibanaPublicAcl = KibanaPublicAcl

    @property
    def KibanaEmbedUrl(self):
        """空间检索分析域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaEmbedUrl

    @KibanaEmbedUrl.setter
    def KibanaEmbedUrl(self, KibanaEmbedUrl):
        self._KibanaEmbedUrl = KibanaEmbedUrl

    @property
    def DiDataList(self):
        """数据联路
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.DiData`
        """
        return self._DiDataList

    @DiDataList.setter
    def DiDataList(self, DiDataList):
        self._DiDataList = DiDataList

    @property
    def VpcInfo(self):
        """空间vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VpcInfo
        """
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo

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
    def EnableKibanaPublicAccess(self):
        """kibana公网开关，0关闭，1开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EnableKibanaPublicAccess

    @EnableKibanaPublicAccess.setter
    def EnableKibanaPublicAccess(self, EnableKibanaPublicAccess):
        self._EnableKibanaPublicAccess = EnableKibanaPublicAccess

    @property
    def EnableKibanaPrivateAccess(self):
        """kibana内网开关，0关闭，1开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EnableKibanaPrivateAccess

    @EnableKibanaPrivateAccess.setter
    def EnableKibanaPrivateAccess(self, EnableKibanaPrivateAccess):
        self._EnableKibanaPrivateAccess = EnableKibanaPrivateAccess

    @property
    def AppId(self):
        """空间所属appid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def KibanaLanguage(self):
        """//默认en， 可选zh-CN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KibanaLanguage

    @KibanaLanguage.setter
    def KibanaLanguage(self, KibanaLanguage):
        self._KibanaLanguage = KibanaLanguage

    @property
    def ClusterType(self):
        """0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def TagList(self):
        """key:value
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TagInfo
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._SpaceName = params.get("SpaceName")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._IndexCount = params.get("IndexCount")
        self._KibanaUrl = params.get("KibanaUrl")
        self._KibanaPrivateUrl = params.get("KibanaPrivateUrl")
        self._IndexAccessUrl = params.get("IndexAccessUrl")
        if params.get("KibanaPublicAcl") is not None:
            self._KibanaPublicAcl = EsAcl()
            self._KibanaPublicAcl._deserialize(params.get("KibanaPublicAcl"))
        self._KibanaEmbedUrl = params.get("KibanaEmbedUrl")
        if params.get("DiDataList") is not None:
            self._DiDataList = DiData()
            self._DiDataList._deserialize(params.get("DiDataList"))
        if params.get("VpcInfo") is not None:
            self._VpcInfo = []
            for item in params.get("VpcInfo"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfo.append(obj)
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._EnableKibanaPublicAccess = params.get("EnableKibanaPublicAccess")
        self._EnableKibanaPrivateAccess = params.get("EnableKibanaPrivateAccess")
        self._AppId = params.get("AppId")
        self._KibanaLanguage = params.get("KibanaLanguage")
        self._ClusterType = params.get("ClusterType")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessSpaceUser(AbstractModel):
    """ServerlessSpaceUser

    """

    def __init__(self):
        r"""
        :param _Username: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Username: str
        :param _Password: 用户密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Status: 用户状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _IndicesScope: 有权限的索引数组
注意：此字段可能返回 null，表示取不到有效值。
        :type IndicesScope: list of str
        :param _PrivilegeType: 权限类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivilegeType: int
        """
        self._Username = None
        self._Password = None
        self._CreateTime = None
        self._Status = None
        self._IndicesScope = None
        self._PrivilegeType = None

    @property
    def Username(self):
        """用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """用户密码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

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
    def Status(self):
        """用户状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IndicesScope(self):
        """有权限的索引数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._IndicesScope

    @IndicesScope.setter
    def IndicesScope(self, IndicesScope):
        self._IndicesScope = IndicesScope

    @property
    def PrivilegeType(self):
        """权限类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PrivilegeType

    @PrivilegeType.setter
    def PrivilegeType(self, PrivilegeType):
        self._PrivilegeType = PrivilegeType


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._IndicesScope = params.get("IndicesScope")
        self._PrivilegeType = params.get("PrivilegeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SettingDetail(AbstractModel):
    """智能运维集群配置详情

    """

    def __init__(self):
        r"""
        :param _Key: 配置key
        :type Key: str
        :param _Value: 配置当前值
        :type Value: str
        :param _Advise: 配置处理建议
        :type Advise: str
        """
        self._Key = None
        self._Value = None
        self._Advise = None

    @property
    def Key(self):
        """配置key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """配置当前值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Advise(self):
        """配置处理建议
        :rtype: str
        """
        return self._Advise

    @Advise.setter
    def Advise(self, Advise):
        self._Advise = Advise


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Advise = params.get("Advise")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshots(AbstractModel):
    """集群快照数据结构

    """

    def __init__(self):
        r"""
        :param _SnapshotName: 快照名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotName: str
        :param _Uuid: 快照Uuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuid: str
        :param _Version: 该快照所属集群的版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Indices: 备份的索引列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Indices: list of str
        :param _DataStreams: 备份的datastream列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DataStreams: list of str
        :param _State: 备份的状态

FAILED            备份失败

IN_PROGRESS 备份执行中

PARTIAL          备份部分成功，部分失败，备份失败的索引和原因会在Failures字段中展示

SUCCESS     备份成功
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _StartTime: 快照备份的开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 快照备份的结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _DurationInMillis: 快照备份的耗时时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationInMillis: int
        :param _TotalShards: 备份的总分片数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalShards: int
        :param _FailedShards: 备份失败的分片数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedShards: int
        :param _SuccessfulShards: 备份成功的分片数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessfulShards: int
        :param _Failures: 备份失败的索引分片和失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Failures: list of Failures
        """
        self._SnapshotName = None
        self._Uuid = None
        self._Version = None
        self._Indices = None
        self._DataStreams = None
        self._State = None
        self._StartTime = None
        self._EndTime = None
        self._DurationInMillis = None
        self._TotalShards = None
        self._FailedShards = None
        self._SuccessfulShards = None
        self._Failures = None

    @property
    def SnapshotName(self):
        """快照名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Uuid(self):
        """快照Uuid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Version(self):
        """该快照所属集群的版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Indices(self):
        """备份的索引列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Indices

    @Indices.setter
    def Indices(self, Indices):
        self._Indices = Indices

    @property
    def DataStreams(self):
        """备份的datastream列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DataStreams

    @DataStreams.setter
    def DataStreams(self, DataStreams):
        self._DataStreams = DataStreams

    @property
    def State(self):
        """备份的状态

FAILED            备份失败

IN_PROGRESS 备份执行中

PARTIAL          备份部分成功，部分失败，备份失败的索引和原因会在Failures字段中展示

SUCCESS     备份成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def StartTime(self):
        """快照备份的开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """快照备份的结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DurationInMillis(self):
        """快照备份的耗时时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DurationInMillis

    @DurationInMillis.setter
    def DurationInMillis(self, DurationInMillis):
        self._DurationInMillis = DurationInMillis

    @property
    def TotalShards(self):
        """备份的总分片数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalShards

    @TotalShards.setter
    def TotalShards(self, TotalShards):
        self._TotalShards = TotalShards

    @property
    def FailedShards(self):
        """备份失败的分片数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FailedShards

    @FailedShards.setter
    def FailedShards(self, FailedShards):
        self._FailedShards = FailedShards

    @property
    def SuccessfulShards(self):
        """备份成功的分片数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SuccessfulShards

    @SuccessfulShards.setter
    def SuccessfulShards(self, SuccessfulShards):
        self._SuccessfulShards = SuccessfulShards

    @property
    def Failures(self):
        """备份失败的索引分片和失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Failures
        """
        return self._Failures

    @Failures.setter
    def Failures(self, Failures):
        self._Failures = Failures


    def _deserialize(self, params):
        self._SnapshotName = params.get("SnapshotName")
        self._Uuid = params.get("Uuid")
        self._Version = params.get("Version")
        self._Indices = params.get("Indices")
        self._DataStreams = params.get("DataStreams")
        self._State = params.get("State")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DurationInMillis = params.get("DurationInMillis")
        self._TotalShards = params.get("TotalShards")
        self._FailedShards = params.get("FailedShards")
        self._SuccessfulShards = params.get("SuccessfulShards")
        if params.get("Failures") is not None:
            self._Failures = []
            for item in params.get("Failures"):
                obj = Failures()
                obj._deserialize(item)
                self._Failures.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLogstashPipelinesRequest(AbstractModel):
    """StartLogstashPipelines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _PipelineIds: 管道ID列表
        :type PipelineIds: list of str
        """
        self._InstanceId = None
        self._PipelineIds = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PipelineIds(self):
        """管道ID列表
        :rtype: list of str
        """
        return self._PipelineIds

    @PipelineIds.setter
    def PipelineIds(self, PipelineIds):
        self._PipelineIds = PipelineIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PipelineIds = params.get("PipelineIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLogstashPipelinesResponse(AbstractModel):
    """StartLogstashPipelines返回参数结构体

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


class StopLogstashPipelinesRequest(AbstractModel):
    """StopLogstashPipelines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _PipelineIds: 管道ID列表
        :type PipelineIds: list of str
        """
        self._InstanceId = None
        self._PipelineIds = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PipelineIds(self):
        """管道ID列表
        :rtype: list of str
        """
        return self._PipelineIds

    @PipelineIds.setter
    def PipelineIds(self, PipelineIds):
        self._PipelineIds = PipelineIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PipelineIds = params.get("PipelineIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopLogstashPipelinesResponse(AbstractModel):
    """StopLogstashPipelines返回参数结构体

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


class SubTaskDetail(AbstractModel):
    """实例操作记录流程任务中的子任务信息（如升级检查任务中的各个检查项）

    """

    def __init__(self):
        r"""
        :param _Name: 子任务名
        :type Name: str
        :param _Result: 子任务结果
        :type Result: bool
        :param _ErrMsg: 子任务错误信息
        :type ErrMsg: str
        :param _Type: 子任务类型
        :type Type: str
        :param _Status: 子任务状态，0处理中 1成功 -1失败
        :type Status: int
        :param _FailedIndices: 升级检查失败的索引名
        :type FailedIndices: list of str
        :param _FinishTime: 子任务结束时间
        :type FinishTime: str
        :param _Level: 子任务等级，1警告 2失败
        :type Level: int
        """
        self._Name = None
        self._Result = None
        self._ErrMsg = None
        self._Type = None
        self._Status = None
        self._FailedIndices = None
        self._FinishTime = None
        self._Level = None

    @property
    def Name(self):
        """子任务名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Result(self):
        """子任务结果
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ErrMsg(self):
        """子任务错误信息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Type(self):
        """子任务类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """子任务状态，0处理中 1成功 -1失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailedIndices(self):
        """升级检查失败的索引名
        :rtype: list of str
        """
        return self._FailedIndices

    @FailedIndices.setter
    def FailedIndices(self, FailedIndices):
        self._FailedIndices = FailedIndices

    @property
    def FinishTime(self):
        """子任务结束时间
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def Level(self):
        """子任务等级，1警告 2失败
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Result = params.get("Result")
        self._ErrMsg = params.get("ErrMsg")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._FailedIndices = params.get("FailedIndices")
        self._FinishTime = params.get("FinishTime")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
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
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
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
        


class TaskDetail(AbstractModel):
    """实例操作记录中的流程任务信息

    """

    def __init__(self):
        r"""
        :param _Name: 任务名
        :type Name: str
        :param _Progress: 任务进度
        :type Progress: float
        :param _FinishTime: 任务完成时间
        :type FinishTime: str
        :param _SubTasks: 子任务
        :type SubTasks: list of SubTaskDetail
        :param _ElapsedTime: 任务花费时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ElapsedTime: int
        :param _ProcessInfo: 任务进度详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessInfo: :class:`tencentcloud.es.v20180416.models.ProcessDetail`
        """
        self._Name = None
        self._Progress = None
        self._FinishTime = None
        self._SubTasks = None
        self._ElapsedTime = None
        self._ProcessInfo = None

    @property
    def Name(self):
        """任务名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Progress(self):
        """任务进度
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def FinishTime(self):
        """任务完成时间
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def SubTasks(self):
        """子任务
        :rtype: list of SubTaskDetail
        """
        return self._SubTasks

    @SubTasks.setter
    def SubTasks(self, SubTasks):
        self._SubTasks = SubTasks

    @property
    def ElapsedTime(self):
        """任务花费时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ElapsedTime

    @ElapsedTime.setter
    def ElapsedTime(self, ElapsedTime):
        self._ElapsedTime = ElapsedTime

    @property
    def ProcessInfo(self):
        """任务进度详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.es.v20180416.models.ProcessDetail`
        """
        return self._ProcessInfo

    @ProcessInfo.setter
    def ProcessInfo(self, ProcessInfo):
        self._ProcessInfo = ProcessInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Progress = params.get("Progress")
        self._FinishTime = params.get("FinishTime")
        if params.get("SubTasks") is not None:
            self._SubTasks = []
            for item in params.get("SubTasks"):
                obj = SubTaskDetail()
                obj._deserialize(item)
                self._SubTasks.append(obj)
        self._ElapsedTime = params.get("ElapsedTime")
        if params.get("ProcessInfo") is not None:
            self._ProcessInfo = ProcessDetail()
            self._ProcessInfo._deserialize(params.get("ProcessInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDiagnoseSettingsRequest(AbstractModel):
    """UpdateDiagnoseSettings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES实例ID
        :type InstanceId: str
        :param _Status: 0：开启智能运维；-1：关闭智能运维
        :type Status: int
        :param _CronTime: 智能运维每天定时巡检时间，时间格式为HH:00:00，例如15:00:00
        :type CronTime: str
        """
        self._InstanceId = None
        self._Status = None
        self._CronTime = None

    @property
    def InstanceId(self):
        """ES实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        """0：开启智能运维；-1：关闭智能运维
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CronTime(self):
        """智能运维每天定时巡检时间，时间格式为HH:00:00，例如15:00:00
        :rtype: str
        """
        return self._CronTime

    @CronTime.setter
    def CronTime(self, CronTime):
        self._CronTime = CronTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        self._CronTime = params.get("CronTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDiagnoseSettingsResponse(AbstractModel):
    """UpdateDiagnoseSettings返回参数结构体

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


class UpdateDictionariesRequest(AbstractModel):
    """UpdateDictionaries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES实例ID
        :type InstanceId: str
        :param _IkMainDicts: 安装时填IK分词主词典COS地址，删除时填词典名如test.dic
        :type IkMainDicts: list of str
        :param _IkStopwords: 安装时填IK分词停用词词典COS地址，删除时填词典名如test.dic
        :type IkStopwords: list of str
        :param _Synonym: 安装时填同义词词典COS地址，删除时填词典名如test.dic
        :type Synonym: list of str
        :param _QQDict: 安装时填QQ分词词典COS地址，删除时填词典名如test.dic
        :type QQDict: list of str
        :param _UpdateType: 0：安装；1：删除。默认值0
        :type UpdateType: int
        :param _ForceRestart: 是否强制重启集群。默认值false
        :type ForceRestart: bool
        """
        self._InstanceId = None
        self._IkMainDicts = None
        self._IkStopwords = None
        self._Synonym = None
        self._QQDict = None
        self._UpdateType = None
        self._ForceRestart = None

    @property
    def InstanceId(self):
        """ES实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IkMainDicts(self):
        """安装时填IK分词主词典COS地址，删除时填词典名如test.dic
        :rtype: list of str
        """
        return self._IkMainDicts

    @IkMainDicts.setter
    def IkMainDicts(self, IkMainDicts):
        self._IkMainDicts = IkMainDicts

    @property
    def IkStopwords(self):
        """安装时填IK分词停用词词典COS地址，删除时填词典名如test.dic
        :rtype: list of str
        """
        return self._IkStopwords

    @IkStopwords.setter
    def IkStopwords(self, IkStopwords):
        self._IkStopwords = IkStopwords

    @property
    def Synonym(self):
        """安装时填同义词词典COS地址，删除时填词典名如test.dic
        :rtype: list of str
        """
        return self._Synonym

    @Synonym.setter
    def Synonym(self, Synonym):
        self._Synonym = Synonym

    @property
    def QQDict(self):
        """安装时填QQ分词词典COS地址，删除时填词典名如test.dic
        :rtype: list of str
        """
        return self._QQDict

    @QQDict.setter
    def QQDict(self, QQDict):
        self._QQDict = QQDict

    @property
    def UpdateType(self):
        """0：安装；1：删除。默认值0
        :rtype: int
        """
        return self._UpdateType

    @UpdateType.setter
    def UpdateType(self, UpdateType):
        self._UpdateType = UpdateType

    @property
    def ForceRestart(self):
        """是否强制重启集群。默认值false
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IkMainDicts = params.get("IkMainDicts")
        self._IkStopwords = params.get("IkStopwords")
        self._Synonym = params.get("Synonym")
        self._QQDict = params.get("QQDict")
        self._UpdateType = params.get("UpdateType")
        self._ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDictionariesResponse(AbstractModel):
    """UpdateDictionaries返回参数结构体

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


class UpdateIndexRequest(AbstractModel):
    """UpdateIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES集群ID
        :type InstanceId: str
        :param _IndexType: 更新的索引类型。auto：自治索引；normal：普通索引
        :type IndexType: str
        :param _IndexName: 更新的索引名
        :type IndexName: str
        :param _UpdateMetaJson: 更新的索引元数据JSON，如mappings、settings
        :type UpdateMetaJson: str
        :param _Username: 集群访问用户名
        :type Username: str
        :param _Password: 集群访问密码
        :type Password: str
        :param _RolloverBackingIndex: 是否滚动后备索引
        :type RolloverBackingIndex: bool
        """
        self._InstanceId = None
        self._IndexType = None
        self._IndexName = None
        self._UpdateMetaJson = None
        self._Username = None
        self._Password = None
        self._RolloverBackingIndex = None

    @property
    def InstanceId(self):
        """ES集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IndexType(self):
        """更新的索引类型。auto：自治索引；normal：普通索引
        :rtype: str
        """
        return self._IndexType

    @IndexType.setter
    def IndexType(self, IndexType):
        self._IndexType = IndexType

    @property
    def IndexName(self):
        """更新的索引名
        :rtype: str
        """
        return self._IndexName

    @IndexName.setter
    def IndexName(self, IndexName):
        self._IndexName = IndexName

    @property
    def UpdateMetaJson(self):
        """更新的索引元数据JSON，如mappings、settings
        :rtype: str
        """
        return self._UpdateMetaJson

    @UpdateMetaJson.setter
    def UpdateMetaJson(self, UpdateMetaJson):
        self._UpdateMetaJson = UpdateMetaJson

    @property
    def Username(self):
        """集群访问用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """集群访问密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def RolloverBackingIndex(self):
        """是否滚动后备索引
        :rtype: bool
        """
        return self._RolloverBackingIndex

    @RolloverBackingIndex.setter
    def RolloverBackingIndex(self, RolloverBackingIndex):
        self._RolloverBackingIndex = RolloverBackingIndex


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IndexType = params.get("IndexType")
        self._IndexName = params.get("IndexName")
        self._UpdateMetaJson = params.get("UpdateMetaJson")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._RolloverBackingIndex = params.get("RolloverBackingIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateIndexResponse(AbstractModel):
    """UpdateIndex返回参数结构体

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


class UpdateInstanceRequest(AbstractModel):
    """UpdateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）
        :type InstanceName: str
        :param _NodeNum: 已废弃请使用NodeInfoList
节点个数（2-50个）
        :type NodeNum: int
        :param _EsConfig: ES配置项（JSON格式字符串）
        :type EsConfig: str
        :param _Password: 默认用户elastic的密码（8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）
        :type Password: str
        :param _EsAcl: 可视化组件（Kibana、Cerebro）的公网访问策略
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param _DiskSize: 已废弃请使用NodeInfoList
磁盘大小（单位GB）
        :type DiskSize: int
        :param _NodeType: 已废弃请使用NodeInfoList
节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param _MasterNodeNum: 已废弃请使用NodeInfoList
专用主节点个数（只支持3个或5个）
        :type MasterNodeNum: int
        :param _MasterNodeType: 已废弃请使用NodeInfoList
专用主节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type MasterNodeType: str
        :param _MasterNodeDiskSize: 已废弃请使用NodeInfoList
专用主节点磁盘大小（单位GB系统默认配置为50GB,暂不支持自定义）
        :type MasterNodeDiskSize: int
        :param _ForceRestart: 更新配置时是否强制重启<li>true强制重启</li><li>false不强制重启</li>当前仅更新EsConfig时需要设置，默认值为false
        :type ForceRestart: bool
        :param _CosBackup: COS自动备份信息
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param _NodeInfoList: 节点信息列表，可以只传递要更新的节点及其对应的规格信息。支持的操作包括<li>修改一种节点的个数</li><li>修改一种节点的节点规格及磁盘大小</li><li>增加一种节点类型（需要同时指定该节点的类型，个数，规格，磁盘等信息）</li>上述操作一次只能进行一种，且磁盘类型不支持修改
        :type NodeInfoList: list of NodeInfo
        :param _PublicAccess: ES集群公网访问状态
OPEN 开启
CLOSE 关闭
        :type PublicAccess: str
        :param _EsPublicAcl: 公网访问控制列表
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`
        :param _KibanaPublicAccess: Kibana公网访问状态
OPEN 开启
CLOSE 关闭
        :type KibanaPublicAccess: str
        :param _KibanaPrivateAccess: Kibana内网访问状态
OPEN 开启
CLOSE 关闭
        :type KibanaPrivateAccess: str
        :param _BasicSecurityType: ES 6.8及以上版本基础版开启或关闭用户认证
        :type BasicSecurityType: int
        :param _KibanaPrivatePort: Kibana内网端口
        :type KibanaPrivatePort: int
        :param _ScaleType: 0: 蓝绿变更方式扩容，集群不重启 （默认） 1: 磁盘解挂载扩容，集群滚动重启
        :type ScaleType: int
        :param _MultiZoneInfo: 多可用区部署
        :type MultiZoneInfo: list of ZoneDetail
        :param _SceneType: 场景化模板类型 -1：不启用 1：通用 2：日志 3：搜索
        :type SceneType: int
        :param _KibanaConfig: Kibana配置项（JSON格式字符串）
        :type KibanaConfig: str
        :param _WebNodeTypeInfo: 可视化节点配置
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param _SwitchPrivateLink: 切换到新网络架构
        :type SwitchPrivateLink: str
        :param _EnableCerebro: 启用Cerebro
        :type EnableCerebro: bool
        :param _CerebroPublicAccess: Cerebro公网访问状态
OPEN 开启
CLOSE 关闭
        :type CerebroPublicAccess: str
        :param _CerebroPrivateAccess: Cerebro内网访问状态
OPEN 开启
CLOSE 关闭
        :type CerebroPrivateAccess: str
        :param _EsConfigSet: 新增或修改的配置组信息
        :type EsConfigSet: :class:`tencentcloud.es.v20180416.models.EsConfigSetInfo`
        :param _OperationDuration: 可维护时间段
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDurationUpdated`
        :param _KibanaAlteringPublicAccess: 是否开启Alerting 外网告警输出：
OPEN 开启
CLOSE 关闭
        :type KibanaAlteringPublicAccess: str
        :param _KibanaPrivateDomain: kibana内网自定义域名
        :type KibanaPrivateDomain: str
        :param _CerebroPrivateDomain: cerebro内网自定义域名
        :type CerebroPrivateDomain: str
        :param _Protocol: 变更为https集群，默认是http
        :type Protocol: str
        :param _OutboundPublicAcls: 节点出站访问详细信息

        :type OutboundPublicAcls: list of OutboundPublicAcl
        :param _OutboundPublicAccess: 节点出站访问操作
OPEN 开启
CLOSE 关闭
        :type OutboundPublicAccess: str
        :param _CvmDelayOnlineTime: cvm延迟上架参数
        :type CvmDelayOnlineTime: int
        :param _ShardAllocationConcurrents: 分片迁移并发数
        :type ShardAllocationConcurrents: int
        :param _ShardAllocationBytes: 分片迁移并发速度
        :type ShardAllocationBytes: int
        :param _ReadWriteMode: 读写分离模式：-1-不开启，1-本地读写分离，2-远端读写分离
        :type ReadWriteMode: int
        :param _EnableScheduleRecoverGroup: 是否开启置放群组异步任务
        :type EnableScheduleRecoverGroup: bool
        :param _EnableScheduleOperationDuration: 置放群组异步任务可维护时间段
        :type EnableScheduleOperationDuration: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        :param _EnableDestroyProtection: 开启集群保护：OPEN-开启，CLOSE-关闭
        :type EnableDestroyProtection: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._NodeNum = None
        self._EsConfig = None
        self._Password = None
        self._EsAcl = None
        self._DiskSize = None
        self._NodeType = None
        self._MasterNodeNum = None
        self._MasterNodeType = None
        self._MasterNodeDiskSize = None
        self._ForceRestart = None
        self._CosBackup = None
        self._NodeInfoList = None
        self._PublicAccess = None
        self._EsPublicAcl = None
        self._KibanaPublicAccess = None
        self._KibanaPrivateAccess = None
        self._BasicSecurityType = None
        self._KibanaPrivatePort = None
        self._ScaleType = None
        self._MultiZoneInfo = None
        self._SceneType = None
        self._KibanaConfig = None
        self._WebNodeTypeInfo = None
        self._SwitchPrivateLink = None
        self._EnableCerebro = None
        self._CerebroPublicAccess = None
        self._CerebroPrivateAccess = None
        self._EsConfigSet = None
        self._OperationDuration = None
        self._KibanaAlteringPublicAccess = None
        self._KibanaPrivateDomain = None
        self._CerebroPrivateDomain = None
        self._Protocol = None
        self._OutboundPublicAcls = None
        self._OutboundPublicAccess = None
        self._CvmDelayOnlineTime = None
        self._ShardAllocationConcurrents = None
        self._ShardAllocationBytes = None
        self._ReadWriteMode = None
        self._EnableScheduleRecoverGroup = None
        self._EnableScheduleOperationDuration = None
        self._EnableDestroyProtection = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NodeNum(self):
        """已废弃请使用NodeInfoList
节点个数（2-50个）
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def EsConfig(self):
        """ES配置项（JSON格式字符串）
        :rtype: str
        """
        return self._EsConfig

    @EsConfig.setter
    def EsConfig(self, EsConfig):
        self._EsConfig = EsConfig

    @property
    def Password(self):
        """默认用户elastic的密码（8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EsAcl(self):
        """可视化组件（Kibana、Cerebro）的公网访问策略
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._EsAcl

    @EsAcl.setter
    def EsAcl(self, EsAcl):
        self._EsAcl = EsAcl

    @property
    def DiskSize(self):
        """已废弃请使用NodeInfoList
磁盘大小（单位GB）
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def NodeType(self):
        """已废弃请使用NodeInfoList
节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def MasterNodeNum(self):
        """已废弃请使用NodeInfoList
专用主节点个数（只支持3个或5个）
        :rtype: int
        """
        return self._MasterNodeNum

    @MasterNodeNum.setter
    def MasterNodeNum(self, MasterNodeNum):
        self._MasterNodeNum = MasterNodeNum

    @property
    def MasterNodeType(self):
        """已废弃请使用NodeInfoList
专用主节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :rtype: str
        """
        return self._MasterNodeType

    @MasterNodeType.setter
    def MasterNodeType(self, MasterNodeType):
        self._MasterNodeType = MasterNodeType

    @property
    def MasterNodeDiskSize(self):
        """已废弃请使用NodeInfoList
专用主节点磁盘大小（单位GB系统默认配置为50GB,暂不支持自定义）
        :rtype: int
        """
        return self._MasterNodeDiskSize

    @MasterNodeDiskSize.setter
    def MasterNodeDiskSize(self, MasterNodeDiskSize):
        self._MasterNodeDiskSize = MasterNodeDiskSize

    @property
    def ForceRestart(self):
        """更新配置时是否强制重启<li>true强制重启</li><li>false不强制重启</li>当前仅更新EsConfig时需要设置，默认值为false
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def CosBackup(self):
        """COS自动备份信息
        :rtype: :class:`tencentcloud.es.v20180416.models.CosBackup`
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup

    @property
    def NodeInfoList(self):
        """节点信息列表，可以只传递要更新的节点及其对应的规格信息。支持的操作包括<li>修改一种节点的个数</li><li>修改一种节点的节点规格及磁盘大小</li><li>增加一种节点类型（需要同时指定该节点的类型，个数，规格，磁盘等信息）</li>上述操作一次只能进行一种，且磁盘类型不支持修改
        :rtype: list of NodeInfo
        """
        return self._NodeInfoList

    @NodeInfoList.setter
    def NodeInfoList(self, NodeInfoList):
        self._NodeInfoList = NodeInfoList

    @property
    def PublicAccess(self):
        """ES集群公网访问状态
OPEN 开启
CLOSE 关闭
        :rtype: str
        """
        return self._PublicAccess

    @PublicAccess.setter
    def PublicAccess(self, PublicAccess):
        self._PublicAccess = PublicAccess

    @property
    def EsPublicAcl(self):
        """公网访问控制列表
        :rtype: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`
        """
        return self._EsPublicAcl

    @EsPublicAcl.setter
    def EsPublicAcl(self, EsPublicAcl):
        self._EsPublicAcl = EsPublicAcl

    @property
    def KibanaPublicAccess(self):
        """Kibana公网访问状态
OPEN 开启
CLOSE 关闭
        :rtype: str
        """
        return self._KibanaPublicAccess

    @KibanaPublicAccess.setter
    def KibanaPublicAccess(self, KibanaPublicAccess):
        self._KibanaPublicAccess = KibanaPublicAccess

    @property
    def KibanaPrivateAccess(self):
        """Kibana内网访问状态
OPEN 开启
CLOSE 关闭
        :rtype: str
        """
        return self._KibanaPrivateAccess

    @KibanaPrivateAccess.setter
    def KibanaPrivateAccess(self, KibanaPrivateAccess):
        self._KibanaPrivateAccess = KibanaPrivateAccess

    @property
    def BasicSecurityType(self):
        """ES 6.8及以上版本基础版开启或关闭用户认证
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def KibanaPrivatePort(self):
        """Kibana内网端口
        :rtype: int
        """
        return self._KibanaPrivatePort

    @KibanaPrivatePort.setter
    def KibanaPrivatePort(self, KibanaPrivatePort):
        self._KibanaPrivatePort = KibanaPrivatePort

    @property
    def ScaleType(self):
        """0: 蓝绿变更方式扩容，集群不重启 （默认） 1: 磁盘解挂载扩容，集群滚动重启
        :rtype: int
        """
        return self._ScaleType

    @ScaleType.setter
    def ScaleType(self, ScaleType):
        self._ScaleType = ScaleType

    @property
    def MultiZoneInfo(self):
        """多可用区部署
        :rtype: list of ZoneDetail
        """
        return self._MultiZoneInfo

    @MultiZoneInfo.setter
    def MultiZoneInfo(self, MultiZoneInfo):
        self._MultiZoneInfo = MultiZoneInfo

    @property
    def SceneType(self):
        """场景化模板类型 -1：不启用 1：通用 2：日志 3：搜索
        :rtype: int
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def KibanaConfig(self):
        """Kibana配置项（JSON格式字符串）
        :rtype: str
        """
        return self._KibanaConfig

    @KibanaConfig.setter
    def KibanaConfig(self, KibanaConfig):
        self._KibanaConfig = KibanaConfig

    @property
    def WebNodeTypeInfo(self):
        """可视化节点配置
        :rtype: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        """
        return self._WebNodeTypeInfo

    @WebNodeTypeInfo.setter
    def WebNodeTypeInfo(self, WebNodeTypeInfo):
        self._WebNodeTypeInfo = WebNodeTypeInfo

    @property
    def SwitchPrivateLink(self):
        """切换到新网络架构
        :rtype: str
        """
        return self._SwitchPrivateLink

    @SwitchPrivateLink.setter
    def SwitchPrivateLink(self, SwitchPrivateLink):
        self._SwitchPrivateLink = SwitchPrivateLink

    @property
    def EnableCerebro(self):
        """启用Cerebro
        :rtype: bool
        """
        return self._EnableCerebro

    @EnableCerebro.setter
    def EnableCerebro(self, EnableCerebro):
        self._EnableCerebro = EnableCerebro

    @property
    def CerebroPublicAccess(self):
        """Cerebro公网访问状态
OPEN 开启
CLOSE 关闭
        :rtype: str
        """
        return self._CerebroPublicAccess

    @CerebroPublicAccess.setter
    def CerebroPublicAccess(self, CerebroPublicAccess):
        self._CerebroPublicAccess = CerebroPublicAccess

    @property
    def CerebroPrivateAccess(self):
        """Cerebro内网访问状态
OPEN 开启
CLOSE 关闭
        :rtype: str
        """
        return self._CerebroPrivateAccess

    @CerebroPrivateAccess.setter
    def CerebroPrivateAccess(self, CerebroPrivateAccess):
        self._CerebroPrivateAccess = CerebroPrivateAccess

    @property
    def EsConfigSet(self):
        """新增或修改的配置组信息
        :rtype: :class:`tencentcloud.es.v20180416.models.EsConfigSetInfo`
        """
        return self._EsConfigSet

    @EsConfigSet.setter
    def EsConfigSet(self, EsConfigSet):
        self._EsConfigSet = EsConfigSet

    @property
    def OperationDuration(self):
        """可维护时间段
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDurationUpdated`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration

    @property
    def KibanaAlteringPublicAccess(self):
        """是否开启Alerting 外网告警输出：
OPEN 开启
CLOSE 关闭
        :rtype: str
        """
        return self._KibanaAlteringPublicAccess

    @KibanaAlteringPublicAccess.setter
    def KibanaAlteringPublicAccess(self, KibanaAlteringPublicAccess):
        self._KibanaAlteringPublicAccess = KibanaAlteringPublicAccess

    @property
    def KibanaPrivateDomain(self):
        """kibana内网自定义域名
        :rtype: str
        """
        return self._KibanaPrivateDomain

    @KibanaPrivateDomain.setter
    def KibanaPrivateDomain(self, KibanaPrivateDomain):
        self._KibanaPrivateDomain = KibanaPrivateDomain

    @property
    def CerebroPrivateDomain(self):
        """cerebro内网自定义域名
        :rtype: str
        """
        return self._CerebroPrivateDomain

    @CerebroPrivateDomain.setter
    def CerebroPrivateDomain(self, CerebroPrivateDomain):
        self._CerebroPrivateDomain = CerebroPrivateDomain

    @property
    def Protocol(self):
        """变更为https集群，默认是http
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OutboundPublicAcls(self):
        """节点出站访问详细信息

        :rtype: list of OutboundPublicAcl
        """
        return self._OutboundPublicAcls

    @OutboundPublicAcls.setter
    def OutboundPublicAcls(self, OutboundPublicAcls):
        self._OutboundPublicAcls = OutboundPublicAcls

    @property
    def OutboundPublicAccess(self):
        """节点出站访问操作
OPEN 开启
CLOSE 关闭
        :rtype: str
        """
        return self._OutboundPublicAccess

    @OutboundPublicAccess.setter
    def OutboundPublicAccess(self, OutboundPublicAccess):
        self._OutboundPublicAccess = OutboundPublicAccess

    @property
    def CvmDelayOnlineTime(self):
        """cvm延迟上架参数
        :rtype: int
        """
        return self._CvmDelayOnlineTime

    @CvmDelayOnlineTime.setter
    def CvmDelayOnlineTime(self, CvmDelayOnlineTime):
        self._CvmDelayOnlineTime = CvmDelayOnlineTime

    @property
    def ShardAllocationConcurrents(self):
        """分片迁移并发数
        :rtype: int
        """
        return self._ShardAllocationConcurrents

    @ShardAllocationConcurrents.setter
    def ShardAllocationConcurrents(self, ShardAllocationConcurrents):
        self._ShardAllocationConcurrents = ShardAllocationConcurrents

    @property
    def ShardAllocationBytes(self):
        """分片迁移并发速度
        :rtype: int
        """
        return self._ShardAllocationBytes

    @ShardAllocationBytes.setter
    def ShardAllocationBytes(self, ShardAllocationBytes):
        self._ShardAllocationBytes = ShardAllocationBytes

    @property
    def ReadWriteMode(self):
        """读写分离模式：-1-不开启，1-本地读写分离，2-远端读写分离
        :rtype: int
        """
        return self._ReadWriteMode

    @ReadWriteMode.setter
    def ReadWriteMode(self, ReadWriteMode):
        self._ReadWriteMode = ReadWriteMode

    @property
    def EnableScheduleRecoverGroup(self):
        """是否开启置放群组异步任务
        :rtype: bool
        """
        return self._EnableScheduleRecoverGroup

    @EnableScheduleRecoverGroup.setter
    def EnableScheduleRecoverGroup(self, EnableScheduleRecoverGroup):
        self._EnableScheduleRecoverGroup = EnableScheduleRecoverGroup

    @property
    def EnableScheduleOperationDuration(self):
        """置放群组异步任务可维护时间段
        :rtype: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        return self._EnableScheduleOperationDuration

    @EnableScheduleOperationDuration.setter
    def EnableScheduleOperationDuration(self, EnableScheduleOperationDuration):
        self._EnableScheduleOperationDuration = EnableScheduleOperationDuration

    @property
    def EnableDestroyProtection(self):
        """开启集群保护：OPEN-开启，CLOSE-关闭
        :rtype: str
        """
        return self._EnableDestroyProtection

    @EnableDestroyProtection.setter
    def EnableDestroyProtection(self, EnableDestroyProtection):
        self._EnableDestroyProtection = EnableDestroyProtection


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._NodeNum = params.get("NodeNum")
        self._EsConfig = params.get("EsConfig")
        self._Password = params.get("Password")
        if params.get("EsAcl") is not None:
            self._EsAcl = EsAcl()
            self._EsAcl._deserialize(params.get("EsAcl"))
        self._DiskSize = params.get("DiskSize")
        self._NodeType = params.get("NodeType")
        self._MasterNodeNum = params.get("MasterNodeNum")
        self._MasterNodeType = params.get("MasterNodeType")
        self._MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self._ForceRestart = params.get("ForceRestart")
        if params.get("CosBackup") is not None:
            self._CosBackup = CosBackup()
            self._CosBackup._deserialize(params.get("CosBackup"))
        if params.get("NodeInfoList") is not None:
            self._NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeInfoList.append(obj)
        self._PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self._EsPublicAcl = EsPublicAcl()
            self._EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self._KibanaPublicAccess = params.get("KibanaPublicAccess")
        self._KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self._BasicSecurityType = params.get("BasicSecurityType")
        self._KibanaPrivatePort = params.get("KibanaPrivatePort")
        self._ScaleType = params.get("ScaleType")
        if params.get("MultiZoneInfo") is not None:
            self._MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self._MultiZoneInfo.append(obj)
        self._SceneType = params.get("SceneType")
        self._KibanaConfig = params.get("KibanaConfig")
        if params.get("WebNodeTypeInfo") is not None:
            self._WebNodeTypeInfo = WebNodeTypeInfo()
            self._WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self._SwitchPrivateLink = params.get("SwitchPrivateLink")
        self._EnableCerebro = params.get("EnableCerebro")
        self._CerebroPublicAccess = params.get("CerebroPublicAccess")
        self._CerebroPrivateAccess = params.get("CerebroPrivateAccess")
        if params.get("EsConfigSet") is not None:
            self._EsConfigSet = EsConfigSetInfo()
            self._EsConfigSet._deserialize(params.get("EsConfigSet"))
        if params.get("OperationDuration") is not None:
            self._OperationDuration = OperationDurationUpdated()
            self._OperationDuration._deserialize(params.get("OperationDuration"))
        self._KibanaAlteringPublicAccess = params.get("KibanaAlteringPublicAccess")
        self._KibanaPrivateDomain = params.get("KibanaPrivateDomain")
        self._CerebroPrivateDomain = params.get("CerebroPrivateDomain")
        self._Protocol = params.get("Protocol")
        if params.get("OutboundPublicAcls") is not None:
            self._OutboundPublicAcls = []
            for item in params.get("OutboundPublicAcls"):
                obj = OutboundPublicAcl()
                obj._deserialize(item)
                self._OutboundPublicAcls.append(obj)
        self._OutboundPublicAccess = params.get("OutboundPublicAccess")
        self._CvmDelayOnlineTime = params.get("CvmDelayOnlineTime")
        self._ShardAllocationConcurrents = params.get("ShardAllocationConcurrents")
        self._ShardAllocationBytes = params.get("ShardAllocationBytes")
        self._ReadWriteMode = params.get("ReadWriteMode")
        self._EnableScheduleRecoverGroup = params.get("EnableScheduleRecoverGroup")
        if params.get("EnableScheduleOperationDuration") is not None:
            self._EnableScheduleOperationDuration = EnableScheduleOperationDuration()
            self._EnableScheduleOperationDuration._deserialize(params.get("EnableScheduleOperationDuration"))
        self._EnableDestroyProtection = params.get("EnableDestroyProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceResponse(AbstractModel):
    """UpdateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        """订单号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class UpdateJdkRequest(AbstractModel):
    """UpdateJdk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ES实例ID
        :type InstanceId: str
        :param _Jdk: Jdk类型，支持kona和oracle
        :type Jdk: str
        :param _Gc: Gc类型，支持g1和cms
        :type Gc: str
        :param _ForceRestart: 是否强制重启
        :type ForceRestart: bool
        """
        self._InstanceId = None
        self._Jdk = None
        self._Gc = None
        self._ForceRestart = None

    @property
    def InstanceId(self):
        """ES实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Jdk(self):
        """Jdk类型，支持kona和oracle
        :rtype: str
        """
        return self._Jdk

    @Jdk.setter
    def Jdk(self, Jdk):
        self._Jdk = Jdk

    @property
    def Gc(self):
        """Gc类型，支持g1和cms
        :rtype: str
        """
        return self._Gc

    @Gc.setter
    def Gc(self, Gc):
        self._Gc = Gc

    @property
    def ForceRestart(self):
        """是否强制重启
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Jdk = params.get("Jdk")
        self._Gc = params.get("Gc")
        self._ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateJdkResponse(AbstractModel):
    """UpdateJdk返回参数结构体

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


class UpdateLogstashInstanceRequest(AbstractModel):
    """UpdateLogstashInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _NodeNum: 实例节点数量
        :type NodeNum: int
        :param _YMLConfig: 实例YML配置
        :type YMLConfig: str
        :param _BindedES: 实例绑定的ES集群信息
        :type BindedES: :class:`tencentcloud.es.v20180416.models.LogstashBindedES`
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _ExtendedFiles: 扩展文件列表
        :type ExtendedFiles: list of LogstashExtendedFile
        :param _NodeType: 实例规格
        :type NodeType: str
        :param _DiskSize: 节点磁盘容量
        :type DiskSize: int
        :param _OperationDuration: 可维护时间段
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDurationUpdated`
        """
        self._InstanceId = None
        self._NodeNum = None
        self._YMLConfig = None
        self._BindedES = None
        self._InstanceName = None
        self._ExtendedFiles = None
        self._NodeType = None
        self._DiskSize = None
        self._OperationDuration = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeNum(self):
        """实例节点数量
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def YMLConfig(self):
        """实例YML配置
        :rtype: str
        """
        return self._YMLConfig

    @YMLConfig.setter
    def YMLConfig(self, YMLConfig):
        self._YMLConfig = YMLConfig

    @property
    def BindedES(self):
        """实例绑定的ES集群信息
        :rtype: :class:`tencentcloud.es.v20180416.models.LogstashBindedES`
        """
        return self._BindedES

    @BindedES.setter
    def BindedES(self, BindedES):
        self._BindedES = BindedES

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ExtendedFiles(self):
        """扩展文件列表
        :rtype: list of LogstashExtendedFile
        """
        return self._ExtendedFiles

    @ExtendedFiles.setter
    def ExtendedFiles(self, ExtendedFiles):
        self._ExtendedFiles = ExtendedFiles

    @property
    def NodeType(self):
        """实例规格
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def DiskSize(self):
        """节点磁盘容量
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def OperationDuration(self):
        """可维护时间段
        :rtype: :class:`tencentcloud.es.v20180416.models.OperationDurationUpdated`
        """
        return self._OperationDuration

    @OperationDuration.setter
    def OperationDuration(self, OperationDuration):
        self._OperationDuration = OperationDuration


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeNum = params.get("NodeNum")
        self._YMLConfig = params.get("YMLConfig")
        if params.get("BindedES") is not None:
            self._BindedES = LogstashBindedES()
            self._BindedES._deserialize(params.get("BindedES"))
        self._InstanceName = params.get("InstanceName")
        if params.get("ExtendedFiles") is not None:
            self._ExtendedFiles = []
            for item in params.get("ExtendedFiles"):
                obj = LogstashExtendedFile()
                obj._deserialize(item)
                self._ExtendedFiles.append(obj)
        self._NodeType = params.get("NodeType")
        self._DiskSize = params.get("DiskSize")
        if params.get("OperationDuration") is not None:
            self._OperationDuration = OperationDurationUpdated()
            self._OperationDuration._deserialize(params.get("OperationDuration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateLogstashInstanceResponse(AbstractModel):
    """UpdateLogstashInstance返回参数结构体

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


class UpdateLogstashPipelineDescRequest(AbstractModel):
    """UpdateLogstashPipelineDesc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _PipelineId: 实例管道ID
        :type PipelineId: str
        :param _PipelineDesc: 管道描述信息
        :type PipelineDesc: str
        """
        self._InstanceId = None
        self._PipelineId = None
        self._PipelineDesc = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PipelineId(self):
        """实例管道ID
        :rtype: str
        """
        return self._PipelineId

    @PipelineId.setter
    def PipelineId(self, PipelineId):
        self._PipelineId = PipelineId

    @property
    def PipelineDesc(self):
        """管道描述信息
        :rtype: str
        """
        return self._PipelineDesc

    @PipelineDesc.setter
    def PipelineDesc(self, PipelineDesc):
        self._PipelineDesc = PipelineDesc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PipelineId = params.get("PipelineId")
        self._PipelineDesc = params.get("PipelineDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateLogstashPipelineDescResponse(AbstractModel):
    """UpdateLogstashPipelineDesc返回参数结构体

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


class UpdatePluginsRequest(AbstractModel):
    """UpdatePlugins请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstallPluginList: 需要安装的插件名列表
        :type InstallPluginList: list of str
        :param _RemovePluginList: 需要卸载的插件名列表
        :type RemovePluginList: list of str
        :param _ForceRestart: 是否强制重启，默认值false
        :type ForceRestart: bool
        :param _ForceUpdate: 是否重新安装，默认值false
        :type ForceUpdate: bool
        :param _PluginType: 0：系统插件
        :type PluginType: int
        """
        self._InstanceId = None
        self._InstallPluginList = None
        self._RemovePluginList = None
        self._ForceRestart = None
        self._ForceUpdate = None
        self._PluginType = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstallPluginList(self):
        """需要安装的插件名列表
        :rtype: list of str
        """
        return self._InstallPluginList

    @InstallPluginList.setter
    def InstallPluginList(self, InstallPluginList):
        self._InstallPluginList = InstallPluginList

    @property
    def RemovePluginList(self):
        """需要卸载的插件名列表
        :rtype: list of str
        """
        return self._RemovePluginList

    @RemovePluginList.setter
    def RemovePluginList(self, RemovePluginList):
        self._RemovePluginList = RemovePluginList

    @property
    def ForceRestart(self):
        """是否强制重启，默认值false
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart

    @property
    def ForceUpdate(self):
        """是否重新安装，默认值false
        :rtype: bool
        """
        return self._ForceUpdate

    @ForceUpdate.setter
    def ForceUpdate(self, ForceUpdate):
        self._ForceUpdate = ForceUpdate

    @property
    def PluginType(self):
        """0：系统插件
        :rtype: int
        """
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstallPluginList = params.get("InstallPluginList")
        self._RemovePluginList = params.get("RemovePluginList")
        self._ForceRestart = params.get("ForceRestart")
        self._ForceUpdate = params.get("ForceUpdate")
        self._PluginType = params.get("PluginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePluginsResponse(AbstractModel):
    """UpdatePlugins返回参数结构体

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


class UpdateRequestTargetNodeTypesRequest(AbstractModel):
    """UpdateRequestTargetNodeTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _TargetNodeTypes: 接收请求的目标节点类型列表
        :type TargetNodeTypes: list of str
        """
        self._InstanceId = None
        self._TargetNodeTypes = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TargetNodeTypes(self):
        """接收请求的目标节点类型列表
        :rtype: list of str
        """
        return self._TargetNodeTypes

    @TargetNodeTypes.setter
    def TargetNodeTypes(self, TargetNodeTypes):
        self._TargetNodeTypes = TargetNodeTypes


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TargetNodeTypes = params.get("TargetNodeTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRequestTargetNodeTypesResponse(AbstractModel):
    """UpdateRequestTargetNodeTypes返回参数结构体

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


class UpdateServerlessInstanceRequest(AbstractModel):
    """UpdateServerlessInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: Serveless实例ID
        :type InstanceId: str
        :param _UpdateMetaJson: 更新的索引元数据JSON，如mappings、settings
        :type UpdateMetaJson: str
        :param _Password: 实例访问密码
        :type Password: str
        :param _KibanaPrivateAccess: 开启kibana内网访问，如OPEN、CLOSE
        :type KibanaPrivateAccess: str
        :param _KibanaPublicAccess: 开启kibana外网访问，如OPEN、CLOSE
        :type KibanaPublicAccess: str
        :param _KibanaPublicAcl: 访问控制列表
        :type KibanaPublicAcl: :class:`tencentcloud.es.v20180416.models.KibanaPublicAcl`
        """
        self._InstanceId = None
        self._UpdateMetaJson = None
        self._Password = None
        self._KibanaPrivateAccess = None
        self._KibanaPublicAccess = None
        self._KibanaPublicAcl = None

    @property
    def InstanceId(self):
        """Serveless实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpdateMetaJson(self):
        """更新的索引元数据JSON，如mappings、settings
        :rtype: str
        """
        return self._UpdateMetaJson

    @UpdateMetaJson.setter
    def UpdateMetaJson(self, UpdateMetaJson):
        self._UpdateMetaJson = UpdateMetaJson

    @property
    def Password(self):
        """实例访问密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KibanaPrivateAccess(self):
        """开启kibana内网访问，如OPEN、CLOSE
        :rtype: str
        """
        return self._KibanaPrivateAccess

    @KibanaPrivateAccess.setter
    def KibanaPrivateAccess(self, KibanaPrivateAccess):
        self._KibanaPrivateAccess = KibanaPrivateAccess

    @property
    def KibanaPublicAccess(self):
        """开启kibana外网访问，如OPEN、CLOSE
        :rtype: str
        """
        return self._KibanaPublicAccess

    @KibanaPublicAccess.setter
    def KibanaPublicAccess(self, KibanaPublicAccess):
        self._KibanaPublicAccess = KibanaPublicAccess

    @property
    def KibanaPublicAcl(self):
        """访问控制列表
        :rtype: :class:`tencentcloud.es.v20180416.models.KibanaPublicAcl`
        """
        return self._KibanaPublicAcl

    @KibanaPublicAcl.setter
    def KibanaPublicAcl(self, KibanaPublicAcl):
        self._KibanaPublicAcl = KibanaPublicAcl


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UpdateMetaJson = params.get("UpdateMetaJson")
        self._Password = params.get("Password")
        self._KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self._KibanaPublicAccess = params.get("KibanaPublicAccess")
        if params.get("KibanaPublicAcl") is not None:
            self._KibanaPublicAcl = KibanaPublicAcl()
            self._KibanaPublicAcl._deserialize(params.get("KibanaPublicAcl"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateServerlessInstanceResponse(AbstractModel):
    """UpdateServerlessInstance返回参数结构体

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


class UpdateServerlessSpaceRequest(AbstractModel):
    """UpdateServerlessSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: Serveless索引空间ID
        :type SpaceId: str
        :param _SpaceName: Serveless索引空间名
        :type SpaceName: str
        :param _KibanaPrivateAccess: kibana内网开关
        :type KibanaPrivateAccess: str
        :param _KibanaPublicAccess: kibana公网开关
        :type KibanaPublicAccess: str
        :param _KibanaPublicAcl: kibana公网白名单
        :type KibanaPublicAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        self._SpaceId = None
        self._SpaceName = None
        self._KibanaPrivateAccess = None
        self._KibanaPublicAccess = None
        self._KibanaPublicAcl = None

    @property
    def SpaceId(self):
        """Serveless索引空间ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def SpaceName(self):
        """Serveless索引空间名
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def KibanaPrivateAccess(self):
        """kibana内网开关
        :rtype: str
        """
        return self._KibanaPrivateAccess

    @KibanaPrivateAccess.setter
    def KibanaPrivateAccess(self, KibanaPrivateAccess):
        self._KibanaPrivateAccess = KibanaPrivateAccess

    @property
    def KibanaPublicAccess(self):
        """kibana公网开关
        :rtype: str
        """
        return self._KibanaPublicAccess

    @KibanaPublicAccess.setter
    def KibanaPublicAccess(self, KibanaPublicAccess):
        self._KibanaPublicAccess = KibanaPublicAccess

    @property
    def KibanaPublicAcl(self):
        """kibana公网白名单
        :rtype: :class:`tencentcloud.es.v20180416.models.EsAcl`
        """
        return self._KibanaPublicAcl

    @KibanaPublicAcl.setter
    def KibanaPublicAcl(self, KibanaPublicAcl):
        self._KibanaPublicAcl = KibanaPublicAcl


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._SpaceName = params.get("SpaceName")
        self._KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self._KibanaPublicAccess = params.get("KibanaPublicAccess")
        if params.get("KibanaPublicAcl") is not None:
            self._KibanaPublicAcl = EsAcl()
            self._KibanaPublicAcl._deserialize(params.get("KibanaPublicAcl"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateServerlessSpaceResponse(AbstractModel):
    """UpdateServerlessSpace返回参数结构体

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


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _EsVersion: 目标ES版本，支持：”6.4.3“, "6.8.2"，"7.5.1", "7.10.1", "7.14.2"
        :type EsVersion: str
        :param _CheckOnly: 是否只做升级检查，默认值为false
        :type CheckOnly: bool
        :param _LicenseType: 目标商业特性版本：<li>oss 开源版</li><li>basic 基础版</li>当前仅在5.6.4升级6.x版本时使用，默认值为basic
        :type LicenseType: str
        :param _BasicSecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
        :type BasicSecurityType: int
        :param _UpgradeMode: 升级方式：<li>scale 蓝绿变更</li><li>restart 滚动重启</li>默认值为scale
        :type UpgradeMode: str
        :param _CosBackup: 升级版本前是否对集群进行备份，默认不备份
        :type CosBackup: bool
        :param _SkipCheckForceRestart: 滚动模式时，是否跳过检查，进行强制重启。默认值为false
        :type SkipCheckForceRestart: bool
        :param _CvmDelayOnlineTime: cvm延迟上架参数
        :type CvmDelayOnlineTime: int
        :param _ShardAllocationConcurrents: 分片迁移并发数
        :type ShardAllocationConcurrents: int
        :param _ShardAllocationBytes: 分片迁移并发速度
        :type ShardAllocationBytes: int
        :param _EnableScheduleRecoverGroup: 是否开启置放群组异步任务
        :type EnableScheduleRecoverGroup: bool
        :param _EnableScheduleOperationDuration: 置放群组异步任务时间段
        :type EnableScheduleOperationDuration: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        self._InstanceId = None
        self._EsVersion = None
        self._CheckOnly = None
        self._LicenseType = None
        self._BasicSecurityType = None
        self._UpgradeMode = None
        self._CosBackup = None
        self._SkipCheckForceRestart = None
        self._CvmDelayOnlineTime = None
        self._ShardAllocationConcurrents = None
        self._ShardAllocationBytes = None
        self._EnableScheduleRecoverGroup = None
        self._EnableScheduleOperationDuration = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EsVersion(self):
        """目标ES版本，支持：”6.4.3“, "6.8.2"，"7.5.1", "7.10.1", "7.14.2"
        :rtype: str
        """
        return self._EsVersion

    @EsVersion.setter
    def EsVersion(self, EsVersion):
        self._EsVersion = EsVersion

    @property
    def CheckOnly(self):
        """是否只做升级检查，默认值为false
        :rtype: bool
        """
        return self._CheckOnly

    @CheckOnly.setter
    def CheckOnly(self, CheckOnly):
        self._CheckOnly = CheckOnly

    @property
    def LicenseType(self):
        """目标商业特性版本：<li>oss 开源版</li><li>basic 基础版</li>当前仅在5.6.4升级6.x版本时使用，默认值为basic
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def BasicSecurityType(self):
        """6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def UpgradeMode(self):
        """升级方式：<li>scale 蓝绿变更</li><li>restart 滚动重启</li>默认值为scale
        :rtype: str
        """
        return self._UpgradeMode

    @UpgradeMode.setter
    def UpgradeMode(self, UpgradeMode):
        self._UpgradeMode = UpgradeMode

    @property
    def CosBackup(self):
        """升级版本前是否对集群进行备份，默认不备份
        :rtype: bool
        """
        return self._CosBackup

    @CosBackup.setter
    def CosBackup(self, CosBackup):
        self._CosBackup = CosBackup

    @property
    def SkipCheckForceRestart(self):
        """滚动模式时，是否跳过检查，进行强制重启。默认值为false
        :rtype: bool
        """
        return self._SkipCheckForceRestart

    @SkipCheckForceRestart.setter
    def SkipCheckForceRestart(self, SkipCheckForceRestart):
        self._SkipCheckForceRestart = SkipCheckForceRestart

    @property
    def CvmDelayOnlineTime(self):
        """cvm延迟上架参数
        :rtype: int
        """
        return self._CvmDelayOnlineTime

    @CvmDelayOnlineTime.setter
    def CvmDelayOnlineTime(self, CvmDelayOnlineTime):
        self._CvmDelayOnlineTime = CvmDelayOnlineTime

    @property
    def ShardAllocationConcurrents(self):
        """分片迁移并发数
        :rtype: int
        """
        return self._ShardAllocationConcurrents

    @ShardAllocationConcurrents.setter
    def ShardAllocationConcurrents(self, ShardAllocationConcurrents):
        self._ShardAllocationConcurrents = ShardAllocationConcurrents

    @property
    def ShardAllocationBytes(self):
        """分片迁移并发速度
        :rtype: int
        """
        return self._ShardAllocationBytes

    @ShardAllocationBytes.setter
    def ShardAllocationBytes(self, ShardAllocationBytes):
        self._ShardAllocationBytes = ShardAllocationBytes

    @property
    def EnableScheduleRecoverGroup(self):
        """是否开启置放群组异步任务
        :rtype: bool
        """
        return self._EnableScheduleRecoverGroup

    @EnableScheduleRecoverGroup.setter
    def EnableScheduleRecoverGroup(self, EnableScheduleRecoverGroup):
        self._EnableScheduleRecoverGroup = EnableScheduleRecoverGroup

    @property
    def EnableScheduleOperationDuration(self):
        """置放群组异步任务时间段
        :rtype: :class:`tencentcloud.es.v20180416.models.EnableScheduleOperationDuration`
        """
        return self._EnableScheduleOperationDuration

    @EnableScheduleOperationDuration.setter
    def EnableScheduleOperationDuration(self, EnableScheduleOperationDuration):
        self._EnableScheduleOperationDuration = EnableScheduleOperationDuration


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EsVersion = params.get("EsVersion")
        self._CheckOnly = params.get("CheckOnly")
        self._LicenseType = params.get("LicenseType")
        self._BasicSecurityType = params.get("BasicSecurityType")
        self._UpgradeMode = params.get("UpgradeMode")
        self._CosBackup = params.get("CosBackup")
        self._SkipCheckForceRestart = params.get("SkipCheckForceRestart")
        self._CvmDelayOnlineTime = params.get("CvmDelayOnlineTime")
        self._ShardAllocationConcurrents = params.get("ShardAllocationConcurrents")
        self._ShardAllocationBytes = params.get("ShardAllocationBytes")
        self._EnableScheduleRecoverGroup = params.get("EnableScheduleRecoverGroup")
        if params.get("EnableScheduleOperationDuration") is not None:
            self._EnableScheduleOperationDuration = EnableScheduleOperationDuration()
            self._EnableScheduleOperationDuration._deserialize(params.get("EnableScheduleOperationDuration"))
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


class UpgradeLicenseRequest(AbstractModel):
    """UpgradeLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _LicenseType: License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum
        :type LicenseType: str
        :param _AutoVoucher: 是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0
        :type AutoVoucher: int
        :param _VoucherIds: 代金券ID列表（目前仅支持指定一张代金券）
        :type VoucherIds: list of str
        :param _BasicSecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li><li>不传参时会默认维持原状，传参时需注意只能由不开启变为开启，无法由开启变为不开启</li>
        :type BasicSecurityType: int
        :param _ForceRestart: 是否强制重启<li>true强制重启</li><li>false不强制重启</li> 默认值false
        :type ForceRestart: bool
        """
        self._InstanceId = None
        self._LicenseType = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._BasicSecurityType = None
        self._ForceRestart = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LicenseType(self):
        """License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def AutoVoucher(self):
        """是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        """代金券ID列表（目前仅支持指定一张代金券）
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def BasicSecurityType(self):
        """6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li><li>不传参时会默认维持原状，传参时需注意只能由不开启变为开启，无法由开启变为不开启</li>
        :rtype: int
        """
        return self._BasicSecurityType

    @BasicSecurityType.setter
    def BasicSecurityType(self, BasicSecurityType):
        self._BasicSecurityType = BasicSecurityType

    @property
    def ForceRestart(self):
        """是否强制重启<li>true强制重启</li><li>false不强制重启</li> 默认值false
        :rtype: bool
        """
        return self._ForceRestart

    @ForceRestart.setter
    def ForceRestart(self, ForceRestart):
        self._ForceRestart = ForceRestart


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LicenseType = params.get("LicenseType")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        self._BasicSecurityType = params.get("BasicSecurityType")
        self._ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLicenseResponse(AbstractModel):
    """UpgradeLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        """订单号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class VpcInfo(AbstractModel):
    """vpc信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpcId信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: SubnetId信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _VpcUid: VpcUid信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcUid: int
        :param _SubnetUid: SubnetUid 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetUid: int
        :param _AvailableIpAddressCount: 可用ip数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableIpAddressCount: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._VpcUid = None
        self._SubnetUid = None
        self._AvailableIpAddressCount = None

    @property
    def VpcId(self):
        """vpcId信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """SubnetId信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcUid(self):
        """VpcUid信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VpcUid

    @VpcUid.setter
    def VpcUid(self, VpcUid):
        self._VpcUid = VpcUid

    @property
    def SubnetUid(self):
        """SubnetUid 信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SubnetUid

    @SubnetUid.setter
    def SubnetUid(self, SubnetUid):
        self._SubnetUid = SubnetUid

    @property
    def AvailableIpAddressCount(self):
        """可用ip数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AvailableIpAddressCount

    @AvailableIpAddressCount.setter
    def AvailableIpAddressCount(self, AvailableIpAddressCount):
        self._AvailableIpAddressCount = AvailableIpAddressCount


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VpcUid = params.get("VpcUid")
        self._SubnetUid = params.get("SubnetUid")
        self._AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebNodeTypeInfo(AbstractModel):
    """可视化节点配置

    """

    def __init__(self):
        r"""
        :param _NodeNum: 可视化节点个数，固定为1
        :type NodeNum: int
        :param _NodeType: 可视化节点规格
        :type NodeType: str
        """
        self._NodeNum = None
        self._NodeType = None

    @property
    def NodeNum(self):
        """可视化节点个数，固定为1
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def NodeType(self):
        """可视化节点规格
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType


    def _deserialize(self, params):
        self._NodeNum = params.get("NodeNum")
        self._NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDetail(AbstractModel):
    """多可用区部署时可用区的详细信息

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        """
        self._Zone = None
        self._SubnetId = None

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
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        