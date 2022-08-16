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
        :param IndexName: 后备索引名
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexName: str
        :param IndexStatus: 后备索引状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStatus: str
        :param IndexStorage: 后备索引存储大小
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStorage: int
        :param IndexPhrase: 后备索引当前生命周期
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexPhrase: str
        :param IndexCreateTime: 后备索引创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexCreateTime: str
        """
        self.IndexName = None
        self.IndexStatus = None
        self.IndexStorage = None
        self.IndexPhrase = None
        self.IndexCreateTime = None


    def _deserialize(self, params):
        self.IndexName = params.get("IndexName")
        self.IndexStatus = params.get("IndexStatus")
        self.IndexStorage = params.get("IndexStorage")
        self.IndexPhrase = params.get("IndexPhrase")
        self.IndexCreateTime = params.get("IndexCreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterView(AbstractModel):
    """集群维度视图数据

    """

    def __init__(self):
        r"""
        :param Health: 集群健康状态
        :type Health: float
        :param Visible: 集群是否可见
        :type Visible: float
        :param Break: 集群是否熔断
        :type Break: float
        :param AvgDiskUsage: 平均磁盘使用率
        :type AvgDiskUsage: float
        :param AvgMemUsage: 平均内存使用率
        :type AvgMemUsage: float
        :param AvgCpuUsage: 平均cpu使用率
        :type AvgCpuUsage: float
        :param TotalDiskSize: 集群总存储大小
        :type TotalDiskSize: int
        :param TargetNodeTypes: 客户端请求节点
        :type TargetNodeTypes: list of str
        :param NodeNum: 在线节点数
        :type NodeNum: int
        :param TotalNodeNum: 总节点数
        :type TotalNodeNum: int
        :param DataNodeNum: 数据节点数
        :type DataNodeNum: int
        :param IndexNum: 索引数
        :type IndexNum: int
        :param DocNum: 文档数
        :type DocNum: int
        :param DiskUsedInBytes: 磁盘已使用字节数
        :type DiskUsedInBytes: int
        :param ShardNum: 分片个数
        :type ShardNum: int
        :param PrimaryShardNum: 主分片个数
        :type PrimaryShardNum: int
        :param RelocatingShardNum: 迁移中的分片个数
        :type RelocatingShardNum: int
        :param InitializingShardNum: 初始化中的分片个数
        :type InitializingShardNum: int
        :param UnassignedShardNum: 未分配的分片个数
        :type UnassignedShardNum: int
        :param TotalCosStorage: 企业版COS存储容量大小，单位GB
        :type TotalCosStorage: int
        :param SearchableSnapshotCosBucket: 企业版集群可搜索快照cos存放的bucket名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchableSnapshotCosBucket: str
        :param SearchableSnapshotCosAppId: 企业版集群可搜索快照cos所属appid
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchableSnapshotCosAppId: str
        """
        self.Health = None
        self.Visible = None
        self.Break = None
        self.AvgDiskUsage = None
        self.AvgMemUsage = None
        self.AvgCpuUsage = None
        self.TotalDiskSize = None
        self.TargetNodeTypes = None
        self.NodeNum = None
        self.TotalNodeNum = None
        self.DataNodeNum = None
        self.IndexNum = None
        self.DocNum = None
        self.DiskUsedInBytes = None
        self.ShardNum = None
        self.PrimaryShardNum = None
        self.RelocatingShardNum = None
        self.InitializingShardNum = None
        self.UnassignedShardNum = None
        self.TotalCosStorage = None
        self.SearchableSnapshotCosBucket = None
        self.SearchableSnapshotCosAppId = None


    def _deserialize(self, params):
        self.Health = params.get("Health")
        self.Visible = params.get("Visible")
        self.Break = params.get("Break")
        self.AvgDiskUsage = params.get("AvgDiskUsage")
        self.AvgMemUsage = params.get("AvgMemUsage")
        self.AvgCpuUsage = params.get("AvgCpuUsage")
        self.TotalDiskSize = params.get("TotalDiskSize")
        self.TargetNodeTypes = params.get("TargetNodeTypes")
        self.NodeNum = params.get("NodeNum")
        self.TotalNodeNum = params.get("TotalNodeNum")
        self.DataNodeNum = params.get("DataNodeNum")
        self.IndexNum = params.get("IndexNum")
        self.DocNum = params.get("DocNum")
        self.DiskUsedInBytes = params.get("DiskUsedInBytes")
        self.ShardNum = params.get("ShardNum")
        self.PrimaryShardNum = params.get("PrimaryShardNum")
        self.RelocatingShardNum = params.get("RelocatingShardNum")
        self.InitializingShardNum = params.get("InitializingShardNum")
        self.UnassignedShardNum = params.get("UnassignedShardNum")
        self.TotalCosStorage = params.get("TotalCosStorage")
        self.SearchableSnapshotCosBucket = params.get("SearchableSnapshotCosBucket")
        self.SearchableSnapshotCosAppId = params.get("SearchableSnapshotCosAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosBackup(AbstractModel):
    """ES cos自动备份信息

    """

    def __init__(self):
        r"""
        :param IsAutoBackup: 是否开启cos自动备份
        :type IsAutoBackup: bool
        :param BackupTime: 自动备份执行时间（精确到小时）, e.g. "22:00"
        :type BackupTime: str
        """
        self.IsAutoBackup = None
        self.BackupTime = None


    def _deserialize(self, params):
        self.IsAutoBackup = params.get("IsAutoBackup")
        self.BackupTime = params.get("BackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexRequest(AbstractModel):
    """CreateIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ES集群ID
        :type InstanceId: str
        :param IndexType: 创建的索引类型。auto：自治索引；normal：普通索引
        :type IndexType: str
        :param IndexName: 创建的索引名
        :type IndexName: str
        :param IndexMetaJson: 创建的索引元数据JSON，如mappings、settings
        :type IndexMetaJson: str
        :param Username: 集群访问用户名
        :type Username: str
        :param Password: 集群访问密码
        :type Password: str
        """
        self.InstanceId = None
        self.IndexType = None
        self.IndexName = None
        self.IndexMetaJson = None
        self.Username = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IndexType = params.get("IndexType")
        self.IndexName = params.get("IndexName")
        self.IndexMetaJson = params.get("IndexMetaJson")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIndexResponse(AbstractModel):
    """CreateIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区
        :type Zone: str
        :param EsVersion: 实例版本（支持"5.6.4"、"6.4.3"、"6.8.2"、"7.5.1"、"7.10.1"）
        :type EsVersion: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Password: 访问密码（密码需8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）
        :type Password: str
        :param InstanceName: 实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）
        :type InstanceName: str
        :param NodeNum: 已废弃请使用NodeInfoList
节点数量（2-50个）
        :type NodeNum: int
        :param ChargeType: 计费类型<li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li>默认值POSTPAID_BY_HOUR
        :type ChargeType: str
        :param ChargePeriod: 包年包月购买时长（单位由参数TimeUnit决定）
        :type ChargePeriod: int
        :param RenewFlag: 自动续费标识<li>RENEW_FLAG_AUTO：自动续费</li><li>RENEW_FLAG_MANUAL：不自动续费，用户手动续费</li>ChargeType为PREPAID时需要设置，如不传递该参数，普通用户默认不自动续费，SVIP用户自动续费
        :type RenewFlag: str
        :param NodeType: 已废弃请使用NodeInfoList
节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param DiskType: 已废弃请使用NodeInfoList
节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高硬能云硬盘</li>默认值CLOUD_SSD
        :type DiskType: str
        :param DiskSize: 已废弃请使用NodeInfoList
节点磁盘容量（单位GB）
        :type DiskSize: int
        :param TimeUnit: 计费时长单位（ChargeType为PREPAID时需要设置，默认值为“m”，表示月，当前只支持“m”）
        :type TimeUnit: str
        :param AutoVoucher: 是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表（目前仅支持指定一张代金券）
        :type VoucherIds: list of str
        :param EnableDedicatedMaster: 已废弃请使用NodeInfoList
是否创建专用主节点<li>true：开启专用主节点</li><li>false：不开启专用主节点</li>默认值false
        :type EnableDedicatedMaster: bool
        :param MasterNodeNum: 已废弃请使用NodeInfoList
专用主节点个数（只支持3个和5个，EnableDedicatedMaster为true时该值必传）
        :type MasterNodeNum: int
        :param MasterNodeType: 已废弃请使用NodeInfoList
专用主节点类型（EnableDedicatedMaster为true时必传）<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type MasterNodeType: str
        :param MasterNodeDiskSize: 已废弃请使用NodeInfoList
专用主节点磁盘大小（单位GB，非必传，若传递则必须为50，暂不支持自定义）
        :type MasterNodeDiskSize: int
        :param ClusterNameInConf: 集群配置文件中的ClusterName（系统默认配置为实例ID，暂不支持自定义）
        :type ClusterNameInConf: str
        :param DeployMode: 集群部署方式<li>0：单可用区部署</li><li>1：多可用区部署</li>默认为0
        :type DeployMode: int
        :param MultiZoneInfo: 多可用区部署时可用区的详细信息(DeployMode为1时必传)
        :type MultiZoneInfo: list of ZoneDetail
        :param LicenseType: License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum
        :type LicenseType: str
        :param NodeInfoList: 节点信息列表， 用于描述集群各类节点的规格信息如节点类型，节点个数，节点规格，磁盘类型，磁盘大小等
        :type NodeInfoList: list of NodeInfo
        :param TagList: 节点标签信息列表
        :type TagList: list of TagInfo
        :param BasicSecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
        :type BasicSecurityType: int
        :param SceneType: 场景化模板类型 0：不启用 1：通用 2：日志 3：搜索
        :type SceneType: int
        :param WebNodeTypeInfo: 可视化节点配置
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param Protocol: 创建https集群，默认是http
        :type Protocol: str
        :param OperationDuration: 可维护时间段
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        """
        self.Zone = None
        self.EsVersion = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.InstanceName = None
        self.NodeNum = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.NodeType = None
        self.DiskType = None
        self.DiskSize = None
        self.TimeUnit = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.EnableDedicatedMaster = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ClusterNameInConf = None
        self.DeployMode = None
        self.MultiZoneInfo = None
        self.LicenseType = None
        self.NodeInfoList = None
        self.TagList = None
        self.BasicSecurityType = None
        self.SceneType = None
        self.WebNodeTypeInfo = None
        self.Protocol = None
        self.OperationDuration = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.EsVersion = params.get("EsVersion")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        self.InstanceName = params.get("InstanceName")
        self.NodeNum = params.get("NodeNum")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ClusterNameInConf = params.get("ClusterNameInConf")
        self.DeployMode = params.get("DeployMode")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.LicenseType = params.get("LicenseType")
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.SceneType = params.get("SceneType")
        if params.get("WebNodeTypeInfo") is not None:
            self.WebNodeTypeInfo = WebNodeTypeInfo()
            self.WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self.Protocol = params.get("Protocol")
        if params.get("OperationDuration") is not None:
            self.OperationDuration = OperationDuration()
            self.OperationDuration._deserialize(params.get("OperationDuration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param DealName: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class CreateLogstashInstanceRequest(AbstractModel):
    """CreateLogstashInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceName: 实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）
        :type InstanceName: str
        :param Zone: 可用区
        :type Zone: str
        :param LogstashVersion: 实例版本（支持"6.8.13"、"7.10.1"）
        :type LogstashVersion: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param NodeNum: 节点数量（2-50个）
        :type NodeNum: int
        :param ChargeType: 计费类型<li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li>默认值POSTPAID_BY_HOUR
        :type ChargeType: str
        :param ChargePeriod: 包年包月购买时长（单位由参数TimeUnit决定）
        :type ChargePeriod: int
        :param TimeUnit: 计费时长单位（ChargeType为PREPAID时需要设置，默认值为“m”，表示月，当前只支持“m”）
        :type TimeUnit: str
        :param AutoVoucher: 是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表（目前仅支持指定一张代金券）
        :type VoucherIds: list of str
        :param RenewFlag: 自动续费标识<li>RENEW_FLAG_AUTO：自动续费</li><li>RENEW_FLAG_MANUAL：不自动续费，用户手动续费</li>ChargeType为PREPAID时需要设置，如不传递该参数，普通用户默认不自动续费，SVIP用户自动续费
        :type RenewFlag: str
        :param NodeType: 节点规格<li>LOGSTASH.S1.SMALL2：1核2G</li><li>LOGSTASH.S1.MEDIUM4：2核4G</li><li>LOGSTASH.S1.MEDIUM8：2核8G</li><li>LOGSTASH.S1.LARGE16：4核16G</li><li>LOGSTASH.S1.2XLARGE32：8核32G</li><li>LOGSTASH.S1.4XLARGE32：16核32G</li><li>LOGSTASH.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param DiskType: 节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高硬能云硬盘</li>默认值CLOUD_SSD
        :type DiskType: str
        :param DiskSize: 节点磁盘容量（单位GB）
        :type DiskSize: int
        :param LicenseType: License类型<li>oss：开源版</li><li>xpack：xpack版</li>默认值xpack
        :type LicenseType: str
        :param TagList: 标签信息列表
        :type TagList: list of TagInfo
        """
        self.InstanceName = None
        self.Zone = None
        self.LogstashVersion = None
        self.VpcId = None
        self.SubnetId = None
        self.NodeNum = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.TimeUnit = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.RenewFlag = None
        self.NodeType = None
        self.DiskType = None
        self.DiskSize = None
        self.LicenseType = None
        self.TagList = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.Zone = params.get("Zone")
        self.LogstashVersion = params.get("LogstashVersion")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.NodeNum = params.get("NodeNum")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.LicenseType = params.get("LicenseType")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogstashInstanceResponse(AbstractModel):
    """CreateLogstashInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DeleteIndexRequest(AbstractModel):
    """DeleteIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ES集群ID
        :type InstanceId: str
        :param IndexType: 删除的索引类型。auto：自治索引；normal：普通索引
        :type IndexType: str
        :param IndexName: 删除的索引名
        :type IndexName: str
        :param Username: 集群访问用户名
        :type Username: str
        :param Password: 集群访问密码
        :type Password: str
        :param BackingIndexName: 后备索引名
        :type BackingIndexName: str
        """
        self.InstanceId = None
        self.IndexType = None
        self.IndexName = None
        self.Username = None
        self.Password = None
        self.BackingIndexName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IndexType = params.get("IndexType")
        self.IndexName = params.get("IndexName")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.BackingIndexName = params.get("BackingIndexName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIndexResponse(AbstractModel):
    """DeleteIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLogstashInstanceRequest(AbstractModel):
    """DeleteLogstashInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogstashInstanceResponse(AbstractModel):
    """DeleteLogstashInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLogstashPipelinesRequest(AbstractModel):
    """DeleteLogstashPipelines请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param PipelineIds: 管道ID列表
        :type PipelineIds: list of str
        """
        self.InstanceId = None
        self.PipelineIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PipelineIds = params.get("PipelineIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogstashPipelinesResponse(AbstractModel):
    """DeleteLogstashPipelines返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeIndexListRequest(AbstractModel):
    """DescribeIndexList请求参数结构体

    """

    def __init__(self):
        r"""
        :param IndexType: 索引类型。auto：自治索引；normal：普通索引
        :type IndexType: str
        :param InstanceId: ES集群ID
        :type InstanceId: str
        :param IndexName: 索引名，若填空则获取所有索引
        :type IndexName: str
        :param Username: 集群访问用户名
        :type Username: str
        :param Password: 集群访问密码
        :type Password: str
        :param Offset: 分页起始位置
        :type Offset: int
        :param Limit: 一页展示数量
        :type Limit: int
        :param OrderBy: 排序字段，支持索引名：IndexName、索引存储量：IndexStorage、索引创建时间：IndexCreateTime
        :type OrderBy: str
        :param IndexStatusList: 过滤索引状态
        :type IndexStatusList: list of str
        :param Order: 排序顺序，支持asc、desc
        :type Order: str
        """
        self.IndexType = None
        self.InstanceId = None
        self.IndexName = None
        self.Username = None
        self.Password = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.IndexStatusList = None
        self.Order = None


    def _deserialize(self, params):
        self.IndexType = params.get("IndexType")
        self.InstanceId = params.get("InstanceId")
        self.IndexName = params.get("IndexName")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.IndexStatusList = params.get("IndexStatusList")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexListResponse(AbstractModel):
    """DescribeIndexList返回参数结构体

    """

    def __init__(self):
        r"""
        :param IndexMetaFields: 索引元数据字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexMetaFields: list of IndexMetaField
        :param TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IndexMetaFields = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IndexMetaFields") is not None:
            self.IndexMetaFields = []
            for item in params.get("IndexMetaFields"):
                obj = IndexMetaField()
                obj._deserialize(item)
                self.IndexMetaFields.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIndexMetaRequest(AbstractModel):
    """DescribeIndexMeta请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ES集群ID
        :type InstanceId: str
        :param IndexType: 索引类型。auto：自治索引；normal：普通索引
        :type IndexType: str
        :param IndexName: 索引名，若填空则获取所有索引
        :type IndexName: str
        :param Username: 集群访问用户名
        :type Username: str
        :param Password: 集群访问密码
        :type Password: str
        """
        self.InstanceId = None
        self.IndexType = None
        self.IndexName = None
        self.Username = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IndexType = params.get("IndexType")
        self.IndexName = params.get("IndexName")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndexMetaResponse(AbstractModel):
    """DescribeIndexMeta返回参数结构体

    """

    def __init__(self):
        r"""
        :param IndexMetaField: 索引元数据字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexMetaField: :class:`tencentcloud.es.v20180416.models.IndexMetaField`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IndexMetaField = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IndexMetaField") is not None:
            self.IndexMetaField = IndexMetaField()
            self.IndexMetaField._deserialize(params.get("IndexMetaField"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    """DescribeInstanceLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例ID
        :type InstanceId: str
        :param LogType: 日志类型，默认值为1
<li>1, 主日志</li>
<li>2, 搜索慢日志</li>
<li>3, 索引慢日志</li>
<li>4, GC日志</li>
        :type LogType: int
        :param SearchKey: 搜索词，支持LUCENE语法，如 level:WARN、ip:1.1.1.1、message:test-index等
        :type SearchKey: str
        :param StartTime: 日志开始时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :type StartTime: str
        :param EndTime: 日志结束时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :type EndTime: str
        :param Offset: 分页起始值, 默认值为0
        :type Offset: int
        :param Limit: 分页大小，默认值为100，最大值100
        :type Limit: int
        :param OrderByType: 时间排序方式，默认值为0
<li>0, 降序</li>
<li>1, 升序</li>
        :type OrderByType: int
        """
        self.InstanceId = None
        self.LogType = None
        self.SearchKey = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LogType = params.get("LogType")
        self.SearchKey = params.get("SearchKey")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceLogsResponse(AbstractModel):
    """DescribeInstanceLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的日志条数
        :type TotalCount: int
        :param InstanceLogList: 日志详细信息列表
        :type InstanceLogList: list of InstanceLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceLogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceLogList") is not None:
            self.InstanceLogList = []
            for item in params.get("InstanceLogList"):
                obj = InstanceLog()
                obj._deserialize(item)
                self.InstanceLogList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    """DescribeInstanceOperations请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例ID
        :type InstanceId: str
        :param StartTime: 起始时间, e.g. "2019-03-07 16:30:39"
        :type StartTime: str
        :param EndTime: 结束时间, e.g. "2019-03-30 20:18:03"
        :type EndTime: str
        :param Offset: 分页起始值
        :type Offset: int
        :param Limit: 分页大小
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceOperationsResponse(AbstractModel):
    """DescribeInstanceOperations返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 操作记录总数
        :type TotalCount: int
        :param Operations: 操作记录
        :type Operations: list of Operation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Operations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Operations") is not None:
            self.Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self.Operations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 集群实例所属可用区，不传则默认所有可用区
        :type Zone: str
        :param InstanceIds: 集群实例ID列表
        :type InstanceIds: list of str
        :param InstanceNames: 集群实例名称列表
        :type InstanceNames: list of str
        :param Offset: 分页起始值, 默认值0
        :type Offset: int
        :param Limit: 分页大小，默认值20
        :type Limit: int
        :param OrderByKey: 排序字段<li>1：实例ID</li><li>2：实例名称</li><li>3：可用区</li><li>4：创建时间</li>若orderKey未传递则按创建时间降序排序
        :type OrderByKey: int
        :param OrderByType: 排序方式<li>0：升序</li><li>1：降序</li>若传递了orderByKey未传递orderByType, 则默认升序
        :type OrderByType: int
        :param TagList: 节点标签信息列表
        :type TagList: list of TagInfo
        :param IpList: 私有网络vip列表
        :type IpList: list of str
        :param ZoneList: 可用区列表
        :type ZoneList: list of str
        :param HealthStatus: 健康状态筛列表
        :type HealthStatus: list of int
        :param VpcIds: Vpc列表 筛选项
        :type VpcIds: list of str
        """
        self.Zone = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.Offset = None
        self.Limit = None
        self.OrderByKey = None
        self.OrderByType = None
        self.TagList = None
        self.IpList = None
        self.ZoneList = None
        self.HealthStatus = None
        self.VpcIds = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByKey = params.get("OrderByKey")
        self.OrderByType = params.get("OrderByType")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.IpList = params.get("IpList")
        self.ZoneList = params.get("ZoneList")
        self.HealthStatus = params.get("HealthStatus")
        self.VpcIds = params.get("VpcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的实例个数
        :type TotalCount: int
        :param InstanceList: 实例详细信息列表
        :type InstanceList: list of InstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogstashInstanceLogsRequest(AbstractModel):
    """DescribeLogstashInstanceLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param LogType: 日志类型，默认值为1
<li>1, 主日志</li>
<li>2, 慢日志</li>
<li>3, GC日志</li>
        :type LogType: int
        :param SearchKey: 搜索词，支持LUCENE语法，如 level:WARN、ip:1.1.1.1、message:test-index等
        :type SearchKey: str
        :param StartTime: 日志开始时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :type StartTime: str
        :param EndTime: 日志结束时间，格式为YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :type EndTime: str
        :param Offset: 分页起始值, 默认值为0
        :type Offset: int
        :param Limit: 分页大小，默认值为100，最大值100
        :type Limit: int
        :param OrderByType: 时间排序方式，默认值为0
<li>0, 降序</li>
<li>1, 升序</li>
        :type OrderByType: int
        """
        self.InstanceId = None
        self.LogType = None
        self.SearchKey = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LogType = params.get("LogType")
        self.SearchKey = params.get("SearchKey")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogstashInstanceLogsResponse(AbstractModel):
    """DescribeLogstashInstanceLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的日志条数
        :type TotalCount: int
        :param InstanceLogList: 日志详细信息列表
        :type InstanceLogList: list of InstanceLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceLogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceLogList") is not None:
            self.InstanceLogList = []
            for item in params.get("InstanceLogList"):
                obj = InstanceLog()
                obj._deserialize(item)
                self.InstanceLogList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogstashInstanceOperationsRequest(AbstractModel):
    """DescribeLogstashInstanceOperations请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param StartTime: 起始时间, e.g. "2019-03-07 16:30:39"
        :type StartTime: str
        :param EndTime: 结束时间, e.g. "2019-03-30 20:18:03"
        :type EndTime: str
        :param Offset: 分页起始值
        :type Offset: int
        :param Limit: 分页大小
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogstashInstanceOperationsResponse(AbstractModel):
    """DescribeLogstashInstanceOperations返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 操作记录总数
        :type TotalCount: int
        :param Operations: 操作记录
        :type Operations: list of Operation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Operations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Operations") is not None:
            self.Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self.Operations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogstashInstancesRequest(AbstractModel):
    """DescribeLogstashInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 实例所属可用区，不传则默认所有可用区
        :type Zone: str
        :param InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param InstanceNames: 实例名称列表
        :type InstanceNames: list of str
        :param Offset: 分页起始值, 默认值0
        :type Offset: int
        :param Limit: 分页大小，默认值20
        :type Limit: int
        :param OrderByKey: 排序字段<li>1：实例ID</li><li>2：实例名称</li><li>3：可用区</li><li>4：创建时间</li>若orderKey未传递则按创建时间降序排序
        :type OrderByKey: int
        :param OrderByType: 排序方式<li>0：升序</li><li>1：降序</li>若传递了orderByKey未传递orderByType, 则默认升序
        :type OrderByType: int
        :param VpcIds: VpcId 筛选项
        :type VpcIds: list of str
        """
        self.Zone = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.Offset = None
        self.Limit = None
        self.OrderByKey = None
        self.OrderByType = None
        self.VpcIds = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByKey = params.get("OrderByKey")
        self.OrderByType = params.get("OrderByType")
        self.VpcIds = params.get("VpcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogstashInstancesResponse(AbstractModel):
    """DescribeLogstashInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的实例个数
        :type TotalCount: int
        :param InstanceList: 实例详细信息列表
        :type InstanceList: list of LogstashInstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = LogstashInstanceInfo()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogstashPipelinesRequest(AbstractModel):
    """DescribeLogstashPipelines请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogstashPipelinesResponse(AbstractModel):
    """DescribeLogstashPipelines返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 管道总数
        :type TotalCount: int
        :param LogstashPipelineList: 管道列表
        :type LogstashPipelineList: list of LogstashPipelineInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LogstashPipelineList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LogstashPipelineList") is not None:
            self.LogstashPipelineList = []
            for item in params.get("LogstashPipelineList"):
                obj = LogstashPipelineInfo()
                obj._deserialize(item)
                self.LogstashPipelineList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeViewsRequest(AbstractModel):
    """DescribeViews请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeViewsResponse(AbstractModel):
    """DescribeViews返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterView: 集群维度视图
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterView: :class:`tencentcloud.es.v20180416.models.ClusterView`
        :param NodesView: 节点维度视图
注意：此字段可能返回 null，表示取不到有效值。
        :type NodesView: list of NodeView
        :param KibanasView: Kibana维度视图
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanasView: list of KibanaView
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterView = None
        self.NodesView = None
        self.KibanasView = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterView") is not None:
            self.ClusterView = ClusterView()
            self.ClusterView._deserialize(params.get("ClusterView"))
        if params.get("NodesView") is not None:
            self.NodesView = []
            for item in params.get("NodesView"):
                obj = NodeView()
                obj._deserialize(item)
                self.NodesView.append(obj)
        if params.get("KibanasView") is not None:
            self.KibanasView = []
            for item in params.get("KibanasView"):
                obj = KibanaView()
                obj._deserialize(item)
                self.KibanasView.append(obj)
        self.RequestId = params.get("RequestId")


class DiagnoseInstanceRequest(AbstractModel):
    """DiagnoseInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ES实例ID
        :type InstanceId: str
        :param DiagnoseJobs: 需要触发的诊断项
        :type DiagnoseJobs: list of str
        :param DiagnoseIndices: 需要诊断的索引，支持通配符
        :type DiagnoseIndices: str
        """
        self.InstanceId = None
        self.DiagnoseJobs = None
        self.DiagnoseIndices = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DiagnoseJobs = params.get("DiagnoseJobs")
        self.DiagnoseIndices = params.get("DiagnoseIndices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseInstanceResponse(AbstractModel):
    """DiagnoseInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DictInfo(AbstractModel):
    """ik插件词典信息

    """

    def __init__(self):
        r"""
        :param Key: 词典键值
        :type Key: str
        :param Name: 词典名称
        :type Name: str
        :param Size: 词典大小，单位B
        :type Size: int
        """
        self.Key = None
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsAcl(AbstractModel):
    """ES集群配置项

    """

    def __init__(self):
        r"""
        :param BlackIpList: kibana访问黑名单
        :type BlackIpList: list of str
        :param WhiteIpList: kibana访问白名单
        :type WhiteIpList: list of str
        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsConfigSetInfo(AbstractModel):
    """配置组信息

    """

    def __init__(self):
        r"""
        :param Type: 配置组类型，如ldap,ad等
        :type Type: str
        :param EsConfig: "{\"order\":0,\"url\":\"ldap://10.0.1.72:389\",\"bind_dn\":\"cn=admin,dc=tencent,dc=com\",\"user_search.base_dn\":\"dc=tencent,dc=com\",\"user_search.filter\":\"(cn={0})\",\"group_search.base_dn\":\"dc=tencent,dc=com\"}"
        :type EsConfig: str
        """
        self.Type = None
        self.EsConfig = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.EsConfig = params.get("EsConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsDictionaryInfo(AbstractModel):
    """ES 词库信息

    """

    def __init__(self):
        r"""
        :param MainDict: 启用词词典列表
        :type MainDict: list of DictInfo
        :param Stopwords: 停用词词典列表
        :type Stopwords: list of DictInfo
        :param QQDict: QQ分词词典列表
        :type QQDict: list of DictInfo
        :param Synonym: 同义词词典列表
        :type Synonym: list of DictInfo
        :param UpdateType: 更新词典类型
        :type UpdateType: str
        """
        self.MainDict = None
        self.Stopwords = None
        self.QQDict = None
        self.Synonym = None
        self.UpdateType = None


    def _deserialize(self, params):
        if params.get("MainDict") is not None:
            self.MainDict = []
            for item in params.get("MainDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self.MainDict.append(obj)
        if params.get("Stopwords") is not None:
            self.Stopwords = []
            for item in params.get("Stopwords"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Stopwords.append(obj)
        if params.get("QQDict") is not None:
            self.QQDict = []
            for item in params.get("QQDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self.QQDict.append(obj)
        if params.get("Synonym") is not None:
            self.Synonym = []
            for item in params.get("Synonym"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Synonym.append(obj)
        self.UpdateType = params.get("UpdateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsPublicAcl(AbstractModel):
    """ES公网访问访问控制信息

    """

    def __init__(self):
        r"""
        :param BlackIpList: 访问黑名单
        :type BlackIpList: list of str
        :param WhiteIpList: 访问白名单
        :type WhiteIpList: list of str
        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestTargetNodeTypesRequest(AbstractModel):
    """GetRequestTargetNodeTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRequestTargetNodeTypesResponse(AbstractModel):
    """GetRequestTargetNodeTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param TargetNodeTypes: 接收请求的目标节点类型列表
        :type TargetNodeTypes: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TargetNodeTypes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetNodeTypes = params.get("TargetNodeTypes")
        self.RequestId = params.get("RequestId")


class IndexMetaField(AbstractModel):
    """索引元数据字段

    """

    def __init__(self):
        r"""
        :param IndexType: 索引类型
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexType: str
        :param IndexName: 索引名
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexName: str
        :param IndexStatus: 索引状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStatus: str
        :param IndexStorage: 索引存储大小，单位Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStorage: int
        :param IndexCreateTime: 索引创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexCreateTime: str
        :param BackingIndices: 后备索引
注意：此字段可能返回 null，表示取不到有效值。
        :type BackingIndices: list of BackingIndexMetaField
        :param ClusterId: 索引所属集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 索引所属集群名
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ClusterVersion: 索引所属集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterVersion: str
        :param IndexPolicyField: 索引生命周期字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexPolicyField: :class:`tencentcloud.es.v20180416.models.IndexPolicyField`
        :param IndexOptionsField: 索引自治字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexOptionsField: :class:`tencentcloud.es.v20180416.models.IndexOptionsField`
        :param IndexSettingsField: 索引配置字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexSettingsField: :class:`tencentcloud.es.v20180416.models.IndexSettingsField`
        :param AppId: 索引所属集群APP ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        """
        self.IndexType = None
        self.IndexName = None
        self.IndexStatus = None
        self.IndexStorage = None
        self.IndexCreateTime = None
        self.BackingIndices = None
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterVersion = None
        self.IndexPolicyField = None
        self.IndexOptionsField = None
        self.IndexSettingsField = None
        self.AppId = None


    def _deserialize(self, params):
        self.IndexType = params.get("IndexType")
        self.IndexName = params.get("IndexName")
        self.IndexStatus = params.get("IndexStatus")
        self.IndexStorage = params.get("IndexStorage")
        self.IndexCreateTime = params.get("IndexCreateTime")
        if params.get("BackingIndices") is not None:
            self.BackingIndices = []
            for item in params.get("BackingIndices"):
                obj = BackingIndexMetaField()
                obj._deserialize(item)
                self.BackingIndices.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterVersion = params.get("ClusterVersion")
        if params.get("IndexPolicyField") is not None:
            self.IndexPolicyField = IndexPolicyField()
            self.IndexPolicyField._deserialize(params.get("IndexPolicyField"))
        if params.get("IndexOptionsField") is not None:
            self.IndexOptionsField = IndexOptionsField()
            self.IndexOptionsField._deserialize(params.get("IndexOptionsField"))
        if params.get("IndexSettingsField") is not None:
            self.IndexSettingsField = IndexSettingsField()
            self.IndexSettingsField._deserialize(params.get("IndexSettingsField"))
        self.AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexOptionsField(AbstractModel):
    """索引自治字段

    """

    def __init__(self):
        r"""
        :param ExpireMaxAge: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireMaxAge: str
        :param ExpireMaxSize: 过期大小
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireMaxSize: str
        :param RolloverMaxAge: 滚动周期
注意：此字段可能返回 null，表示取不到有效值。
        :type RolloverMaxAge: str
        :param RolloverDynamic: 是否开启动态滚动
注意：此字段可能返回 null，表示取不到有效值。
        :type RolloverDynamic: str
        :param ShardNumDynamic: 是否开启动态分片
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardNumDynamic: str
        :param TimestampField: 时间分区字段
注意：此字段可能返回 null，表示取不到有效值。
        :type TimestampField: str
        :param WriteMode: 写入模式
注意：此字段可能返回 null，表示取不到有效值。
        :type WriteMode: str
        """
        self.ExpireMaxAge = None
        self.ExpireMaxSize = None
        self.RolloverMaxAge = None
        self.RolloverDynamic = None
        self.ShardNumDynamic = None
        self.TimestampField = None
        self.WriteMode = None


    def _deserialize(self, params):
        self.ExpireMaxAge = params.get("ExpireMaxAge")
        self.ExpireMaxSize = params.get("ExpireMaxSize")
        self.RolloverMaxAge = params.get("RolloverMaxAge")
        self.RolloverDynamic = params.get("RolloverDynamic")
        self.ShardNumDynamic = params.get("ShardNumDynamic")
        self.TimestampField = params.get("TimestampField")
        self.WriteMode = params.get("WriteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexPolicyField(AbstractModel):
    """索引生命周期字段

    """

    def __init__(self):
        r"""
        :param WarmEnable: 是否开启warm阶段
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmEnable: str
        :param WarmMinAge: warm阶段转入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmMinAge: str
        :param ColdEnable: 是否开启cold阶段
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdEnable: str
        :param ColdMinAge: cold阶段转入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdMinAge: str
        :param FrozenEnable: 是否开启frozen阶段
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenEnable: str
        :param FrozenMinAge: frozen阶段转入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenMinAge: str
        """
        self.WarmEnable = None
        self.WarmMinAge = None
        self.ColdEnable = None
        self.ColdMinAge = None
        self.FrozenEnable = None
        self.FrozenMinAge = None


    def _deserialize(self, params):
        self.WarmEnable = params.get("WarmEnable")
        self.WarmMinAge = params.get("WarmMinAge")
        self.ColdEnable = params.get("ColdEnable")
        self.ColdMinAge = params.get("ColdMinAge")
        self.FrozenEnable = params.get("FrozenEnable")
        self.FrozenMinAge = params.get("FrozenMinAge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndexSettingsField(AbstractModel):
    """索引配置字段

    """

    def __init__(self):
        r"""
        :param NumberOfShards: 索引主分片数
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfShards: str
        :param NumberOfReplicas: 索引副本分片数
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfReplicas: str
        :param RefreshInterval: 索引刷新频率
注意：此字段可能返回 null，表示取不到有效值。
        :type RefreshInterval: str
        """
        self.NumberOfShards = None
        self.NumberOfReplicas = None
        self.RefreshInterval = None


    def _deserialize(self, params):
        self.NumberOfShards = params.get("NumberOfShards")
        self.NumberOfReplicas = params.get("NumberOfReplicas")
        self.RefreshInterval = params.get("RefreshInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param AppId: 用户ID
        :type AppId: int
        :param Uin: 用户UIN
        :type Uin: str
        :param VpcUid: 实例所属VPC的UID
        :type VpcUid: str
        :param SubnetUid: 实例所属子网的UID
        :type SubnetUid: str
        :param Status: 实例状态，0:处理中,1:正常,-1停止,-2:销毁中,-3:已销毁
        :type Status: int
        :param RenewFlag: 自动续费标识。取值范围：
RENEW_FLAG_AUTO：自动续费  
RENEW_FLAG_MANUAL：不自动续费
默认取值：
RENEW_FLAG_DEFAULT：不自动续费
若该参数指定为 RENEW_FLAG_AUTO，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        :param ChargeType: 实例计费模式。取值范围：  PREPAID：表示预付费，即包年包月  POSTPAID_BY_HOUR：表示后付费，即按量计费  CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
        :type ChargeType: str
        :param ChargePeriod: 包年包月购买时长,单位:月
        :type ChargePeriod: int
        :param NodeType: 节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param NodeNum: 节点个数
        :type NodeNum: int
        :param CpuNum: 节点CPU核数
        :type CpuNum: int
        :param MemSize: 节点内存大小，单位GB
        :type MemSize: int
        :param DiskType: 节点磁盘类型
        :type DiskType: str
        :param DiskSize: 节点磁盘大小，单位GB
        :type DiskSize: int
        :param EsDomain: ES域名
        :type EsDomain: str
        :param EsVip: ES VIP
        :type EsVip: str
        :param EsPort: ES端口
        :type EsPort: int
        :param KibanaUrl: Kibana访问url
        :type KibanaUrl: str
        :param EsVersion: ES版本号
        :type EsVersion: str
        :param EsConfig: ES配置项
        :type EsConfig: str
        :param EsAcl: Kibana访问控制配置
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param CreateTime: 实例创建时间
        :type CreateTime: str
        :param UpdateTime: 实例最后修改操作时间
        :type UpdateTime: str
        :param Deadline: 实例到期时间
        :type Deadline: str
        :param InstanceType: 实例类型（实例类型标识，当前只有1,2两种）
        :type InstanceType: int
        :param IkConfig: Ik分词器配置
        :type IkConfig: :class:`tencentcloud.es.v20180416.models.EsDictionaryInfo`
        :param MasterNodeInfo: 专用主节点配置
        :type MasterNodeInfo: :class:`tencentcloud.es.v20180416.models.MasterNodeInfo`
        :param CosBackup: cos自动备份配置
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param AllowCosBackup: 是否允许cos自动备份
        :type AllowCosBackup: bool
        :param TagList: 实例拥有的标签列表
        :type TagList: list of TagInfo
        :param LicenseType: License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum
        :type LicenseType: str
        :param EnableHotWarmMode: 是否为冷热集群<li>true: 冷热集群</li><li>false: 非冷热集群</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableHotWarmMode: bool
        :param WarmNodeType: 温节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmNodeType: str
        :param WarmNodeNum: 温节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmNodeNum: int
        :param WarmCpuNum: 温节点CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmCpuNum: int
        :param WarmMemSize: 温节点内存内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmMemSize: int
        :param WarmDiskType: 温节点磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmDiskType: str
        :param WarmDiskSize: 温节点磁盘大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type WarmDiskSize: int
        :param NodeInfoList: 集群节点信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInfoList: list of NodeInfo
        :param EsPublicUrl: Es公网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EsPublicUrl: str
        :param MultiZoneInfo: 多可用区网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiZoneInfo: list of ZoneDetail
        :param DeployMode: 部署模式<li>0：单可用区</li><li>1：多可用区</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMode: int
        :param PublicAccess: ES公网访问状态<li>OPEN：开启</li><li>CLOSE：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicAccess: str
        :param EsPublicAcl: ES公网访问控制配置
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param KibanaPrivateUrl: Kibana内网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaPrivateUrl: str
        :param KibanaPublicAccess: Kibana公网访问状态<li>OPEN：开启</li><li>CLOSE：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaPublicAccess: str
        :param KibanaPrivateAccess: Kibana内网访问状态<li>OPEN：开启</li><li>CLOSE：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaPrivateAccess: str
        :param SecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityType: int
        :param SceneType: 场景化模板类型：0、不开启；1、通用场景；2、日志场景；3、搜索场景
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneType: int
        :param KibanaConfig: Kibana配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaConfig: str
        :param KibanaNodeInfo: Kibana节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KibanaNodeInfo: :class:`tencentcloud.es.v20180416.models.KibanaNodeInfo`
        :param WebNodeTypeInfo: 可视化节点配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param Jdk: JDK类型，oracle或kona
注意：此字段可能返回 null，表示取不到有效值。
        :type Jdk: str
        :param Protocol: 集群网络通讯协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param SecurityGroups: 安全组id
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroups: list of str
        :param ColdNodeType: 冷节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdNodeType: str
        :param ColdNodeNum: 冷节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdNodeNum: int
        :param ColdCpuNum: 冷节点CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdCpuNum: int
        :param ColdMemSize: 冷节点内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdMemSize: int
        :param ColdDiskType: 冷节点磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdDiskType: str
        :param ColdDiskSize: 冷节点磁盘大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type ColdDiskSize: int
        :param FrozenNodeType: 冻节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenNodeType: str
        :param FrozenNodeNum: 冻节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenNodeNum: int
        :param FrozenCpuNum: 冻节点CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenCpuNum: int
        :param FrozenMemSize: 冻节点内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenMemSize: int
        :param FrozenDiskType: 冻节点磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenDiskType: str
        :param FrozenDiskSize: 冻节点磁盘大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type FrozenDiskSize: int
        :param HealthStatus: 集群健康状态 -1 未知；0 Green; 1 Yellow; 2 Red
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthStatus: int
        :param EsPrivateUrl: https集群内网url
注意：此字段可能返回 null，表示取不到有效值。
        :type EsPrivateUrl: str
        :param EsPrivateDomain: https集群内网域名
注意：此字段可能返回 null，表示取不到有效值。
        :type EsPrivateDomain: str
        :param EsConfigSets: 集群的配置组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EsConfigSets: list of EsConfigSetInfo
        :param OperationDuration: 集群可维护时间段
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDuration`
        :param OptionalWebServiceInfos: web节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OptionalWebServiceInfos: list of OptionalWebServiceInfo
        :param AutoIndexEnabled: 自治索引开关
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoIndexEnabled: bool
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.Zone = None
        self.AppId = None
        self.Uin = None
        self.VpcUid = None
        self.SubnetUid = None
        self.Status = None
        self.RenewFlag = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.NodeType = None
        self.NodeNum = None
        self.CpuNum = None
        self.MemSize = None
        self.DiskType = None
        self.DiskSize = None
        self.EsDomain = None
        self.EsVip = None
        self.EsPort = None
        self.KibanaUrl = None
        self.EsVersion = None
        self.EsConfig = None
        self.EsAcl = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Deadline = None
        self.InstanceType = None
        self.IkConfig = None
        self.MasterNodeInfo = None
        self.CosBackup = None
        self.AllowCosBackup = None
        self.TagList = None
        self.LicenseType = None
        self.EnableHotWarmMode = None
        self.WarmNodeType = None
        self.WarmNodeNum = None
        self.WarmCpuNum = None
        self.WarmMemSize = None
        self.WarmDiskType = None
        self.WarmDiskSize = None
        self.NodeInfoList = None
        self.EsPublicUrl = None
        self.MultiZoneInfo = None
        self.DeployMode = None
        self.PublicAccess = None
        self.EsPublicAcl = None
        self.KibanaPrivateUrl = None
        self.KibanaPublicAccess = None
        self.KibanaPrivateAccess = None
        self.SecurityType = None
        self.SceneType = None
        self.KibanaConfig = None
        self.KibanaNodeInfo = None
        self.WebNodeTypeInfo = None
        self.Jdk = None
        self.Protocol = None
        self.SecurityGroups = None
        self.ColdNodeType = None
        self.ColdNodeNum = None
        self.ColdCpuNum = None
        self.ColdMemSize = None
        self.ColdDiskType = None
        self.ColdDiskSize = None
        self.FrozenNodeType = None
        self.FrozenNodeNum = None
        self.FrozenCpuNum = None
        self.FrozenMemSize = None
        self.FrozenDiskType = None
        self.FrozenDiskSize = None
        self.HealthStatus = None
        self.EsPrivateUrl = None
        self.EsPrivateDomain = None
        self.EsConfigSets = None
        self.OperationDuration = None
        self.OptionalWebServiceInfos = None
        self.AutoIndexEnabled = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.VpcUid = params.get("VpcUid")
        self.SubnetUid = params.get("SubnetUid")
        self.Status = params.get("Status")
        self.RenewFlag = params.get("RenewFlag")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.NodeType = params.get("NodeType")
        self.NodeNum = params.get("NodeNum")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.EsDomain = params.get("EsDomain")
        self.EsVip = params.get("EsVip")
        self.EsPort = params.get("EsPort")
        self.KibanaUrl = params.get("KibanaUrl")
        self.EsVersion = params.get("EsVersion")
        self.EsConfig = params.get("EsConfig")
        if params.get("EsAcl") is not None:
            self.EsAcl = EsAcl()
            self.EsAcl._deserialize(params.get("EsAcl"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Deadline = params.get("Deadline")
        self.InstanceType = params.get("InstanceType")
        if params.get("IkConfig") is not None:
            self.IkConfig = EsDictionaryInfo()
            self.IkConfig._deserialize(params.get("IkConfig"))
        if params.get("MasterNodeInfo") is not None:
            self.MasterNodeInfo = MasterNodeInfo()
            self.MasterNodeInfo._deserialize(params.get("MasterNodeInfo"))
        if params.get("CosBackup") is not None:
            self.CosBackup = CosBackup()
            self.CosBackup._deserialize(params.get("CosBackup"))
        self.AllowCosBackup = params.get("AllowCosBackup")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.LicenseType = params.get("LicenseType")
        self.EnableHotWarmMode = params.get("EnableHotWarmMode")
        self.WarmNodeType = params.get("WarmNodeType")
        self.WarmNodeNum = params.get("WarmNodeNum")
        self.WarmCpuNum = params.get("WarmCpuNum")
        self.WarmMemSize = params.get("WarmMemSize")
        self.WarmDiskType = params.get("WarmDiskType")
        self.WarmDiskSize = params.get("WarmDiskSize")
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        self.EsPublicUrl = params.get("EsPublicUrl")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.DeployMode = params.get("DeployMode")
        self.PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self.EsPublicAcl = EsAcl()
            self.EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self.KibanaPrivateUrl = params.get("KibanaPrivateUrl")
        self.KibanaPublicAccess = params.get("KibanaPublicAccess")
        self.KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self.SecurityType = params.get("SecurityType")
        self.SceneType = params.get("SceneType")
        self.KibanaConfig = params.get("KibanaConfig")
        if params.get("KibanaNodeInfo") is not None:
            self.KibanaNodeInfo = KibanaNodeInfo()
            self.KibanaNodeInfo._deserialize(params.get("KibanaNodeInfo"))
        if params.get("WebNodeTypeInfo") is not None:
            self.WebNodeTypeInfo = WebNodeTypeInfo()
            self.WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self.Jdk = params.get("Jdk")
        self.Protocol = params.get("Protocol")
        self.SecurityGroups = params.get("SecurityGroups")
        self.ColdNodeType = params.get("ColdNodeType")
        self.ColdNodeNum = params.get("ColdNodeNum")
        self.ColdCpuNum = params.get("ColdCpuNum")
        self.ColdMemSize = params.get("ColdMemSize")
        self.ColdDiskType = params.get("ColdDiskType")
        self.ColdDiskSize = params.get("ColdDiskSize")
        self.FrozenNodeType = params.get("FrozenNodeType")
        self.FrozenNodeNum = params.get("FrozenNodeNum")
        self.FrozenCpuNum = params.get("FrozenCpuNum")
        self.FrozenMemSize = params.get("FrozenMemSize")
        self.FrozenDiskType = params.get("FrozenDiskType")
        self.FrozenDiskSize = params.get("FrozenDiskSize")
        self.HealthStatus = params.get("HealthStatus")
        self.EsPrivateUrl = params.get("EsPrivateUrl")
        self.EsPrivateDomain = params.get("EsPrivateDomain")
        if params.get("EsConfigSets") is not None:
            self.EsConfigSets = []
            for item in params.get("EsConfigSets"):
                obj = EsConfigSetInfo()
                obj._deserialize(item)
                self.EsConfigSets.append(obj)
        if params.get("OperationDuration") is not None:
            self.OperationDuration = OperationDuration()
            self.OperationDuration._deserialize(params.get("OperationDuration"))
        if params.get("OptionalWebServiceInfos") is not None:
            self.OptionalWebServiceInfos = []
            for item in params.get("OptionalWebServiceInfos"):
                obj = OptionalWebServiceInfo()
                obj._deserialize(item)
                self.OptionalWebServiceInfos.append(obj)
        self.AutoIndexEnabled = params.get("AutoIndexEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceLog(AbstractModel):
    """ES集群日志详细信息

    """

    def __init__(self):
        r"""
        :param Time: 日志时间
        :type Time: str
        :param Level: 日志级别
        :type Level: str
        :param Ip: 集群节点ip
        :type Ip: str
        :param Message: 日志内容
        :type Message: str
        """
        self.Time = None
        self.Level = None
        self.Ip = None
        self.Message = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Level = params.get("Level")
        self.Ip = params.get("Ip")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """OperationDetail使用此结构的数组描述新旧配置

    """

    def __init__(self):
        r"""
        :param Key: 键
        :type Key: str
        :param Value: 值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KibanaNodeInfo(AbstractModel):
    """实例Kibana节点相关信息

    """

    def __init__(self):
        r"""
        :param KibanaNodeType: Kibana节点规格
        :type KibanaNodeType: str
        :param KibanaNodeNum: Kibana节点个数
        :type KibanaNodeNum: int
        :param KibanaNodeCpuNum: Kibana节点CPU数
        :type KibanaNodeCpuNum: int
        :param KibanaNodeMemSize: Kibana节点内存GB
        :type KibanaNodeMemSize: int
        :param KibanaNodeDiskType: Kibana节点磁盘类型
        :type KibanaNodeDiskType: str
        :param KibanaNodeDiskSize: Kibana节点磁盘大小
        :type KibanaNodeDiskSize: int
        """
        self.KibanaNodeType = None
        self.KibanaNodeNum = None
        self.KibanaNodeCpuNum = None
        self.KibanaNodeMemSize = None
        self.KibanaNodeDiskType = None
        self.KibanaNodeDiskSize = None


    def _deserialize(self, params):
        self.KibanaNodeType = params.get("KibanaNodeType")
        self.KibanaNodeNum = params.get("KibanaNodeNum")
        self.KibanaNodeCpuNum = params.get("KibanaNodeCpuNum")
        self.KibanaNodeMemSize = params.get("KibanaNodeMemSize")
        self.KibanaNodeDiskType = params.get("KibanaNodeDiskType")
        self.KibanaNodeDiskSize = params.get("KibanaNodeDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KibanaView(AbstractModel):
    """Kibana视图数据

    """

    def __init__(self):
        r"""
        :param Ip: Kibana节点IP
        :type Ip: str
        :param DiskSize: 节点总磁盘大小
        :type DiskSize: int
        :param DiskUsage: 磁盘使用率
        :type DiskUsage: float
        :param MemSize: 节点内存大小
        :type MemSize: int
        :param MemUsage: 内存使用率
        :type MemUsage: float
        :param CpuNum: 节点cpu个数
        :type CpuNum: int
        :param CpuUsage: cpu使用率
        :type CpuUsage: float
        :param Zone: 可用区
        :type Zone: str
        """
        self.Ip = None
        self.DiskSize = None
        self.DiskUsage = None
        self.MemSize = None
        self.MemUsage = None
        self.CpuNum = None
        self.CpuUsage = None
        self.Zone = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.DiskSize = params.get("DiskSize")
        self.DiskUsage = params.get("DiskUsage")
        self.MemSize = params.get("MemSize")
        self.MemUsage = params.get("MemUsage")
        self.CpuNum = params.get("CpuNum")
        self.CpuUsage = params.get("CpuUsage")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskInfo(AbstractModel):
    """节点本地盘信息

    """

    def __init__(self):
        r"""
        :param LocalDiskType: 本地盘类型<li>LOCAL_SATA：大数据型</li><li>NVME_SSD：高IO型</li>
        :type LocalDiskType: str
        :param LocalDiskSize: 本地盘单盘大小
        :type LocalDiskSize: int
        :param LocalDiskCount: 本地盘块数
        :type LocalDiskCount: int
        """
        self.LocalDiskType = None
        self.LocalDiskSize = None
        self.LocalDiskCount = None


    def _deserialize(self, params):
        self.LocalDiskType = params.get("LocalDiskType")
        self.LocalDiskSize = params.get("LocalDiskSize")
        self.LocalDiskCount = params.get("LocalDiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashBindedES(AbstractModel):
    """Logstash绑定的ES集群信息

    """

    def __init__(self):
        r"""
        :param ESInstanceId: ES集群ID
        :type ESInstanceId: str
        :param ESUserName: ES集群用户名
        :type ESUserName: str
        :param ESPassword: ES集群密码
        :type ESPassword: str
        """
        self.ESInstanceId = None
        self.ESUserName = None
        self.ESPassword = None


    def _deserialize(self, params):
        self.ESInstanceId = params.get("ESInstanceId")
        self.ESUserName = params.get("ESUserName")
        self.ESPassword = params.get("ESPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashExtendedFile(AbstractModel):
    """Logstash扩展文件信息

    """

    def __init__(self):
        r"""
        :param Name: 扩展文件名称
        :type Name: str
        :param Size: 扩展文件大小，单位B
        :type Size: int
        """
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashInstanceInfo(AbstractModel):
    """Logstash实例详细信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param AppId: 用户ID
        :type AppId: int
        :param Uin: 用户UIN
        :type Uin: str
        :param VpcId: 实例所属VPC的ID
        :type VpcId: str
        :param SubnetId: 实例所属子网的ID
        :type SubnetId: str
        :param Status: 实例状态，0:处理中,1:正常,-1停止,-2:销毁中,-3:已销毁
        :type Status: int
        :param ChargeType: 实例计费模式。取值范围：  PREPAID：表示预付费，即包年包月  POSTPAID_BY_HOUR：表示后付费，即按量计费  CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
        :type ChargeType: str
        :param ChargePeriod: 包年包月购买时长,单位:月
        :type ChargePeriod: int
        :param RenewFlag: 自动续费标识。取值范围：  NOTIFY_AND_AUTO_RENEW：通知过期且自动续费  NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费  DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费  默认取值：NOTIFY_AND_AUTO_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        :param NodeType: 节点规格<li>LOGSTASH.S1.SMALL2：1核2G</li><li>LOGSTASH.S1.MEDIUM4：2核4G</li><li>LOGSTASH.S1.MEDIUM8：2核8G</li><li>LOGSTASH.S1.LARGE16：4核16G</li><li>LOGSTASH.S1.2XLARGE32：8核32G</li><li>LOGSTASH.S1.4XLARGE32：16核32G</li><li>LOGSTASH.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param NodeNum: 节点个数
        :type NodeNum: int
        :param DiskType: 节点磁盘类型
        :type DiskType: str
        :param DiskSize: 节点磁盘大小，单位GB
        :type DiskSize: int
        :param LogstashVersion: Logstash版本号
        :type LogstashVersion: str
        :param LicenseType: License类型<li>oss：开源版</li><li>xpack：基础版</li>默认值xpack
        :type LicenseType: str
        :param CreateTime: 实例创建时间
        :type CreateTime: str
        :param UpdateTime: 实例最后修改操作时间
        :type UpdateTime: str
        :param Deadline: 实例到期时间
        :type Deadline: str
        :param Nodes: 实例节点类型
        :type Nodes: list of LogstashNodeInfo
        :param BindedESInstanceId: 实例绑定的ES集群ID
        :type BindedESInstanceId: str
        :param YMLConfig: 实例的YML配置
注意：此字段可能返回 null，表示取不到有效值。
        :type YMLConfig: str
        :param ExtendedFiles: 扩展文件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtendedFiles: list of LogstashExtendedFile
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.Zone = None
        self.AppId = None
        self.Uin = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.NodeType = None
        self.NodeNum = None
        self.DiskType = None
        self.DiskSize = None
        self.LogstashVersion = None
        self.LicenseType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Deadline = None
        self.Nodes = None
        self.BindedESInstanceId = None
        self.YMLConfig = None
        self.ExtendedFiles = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.NodeNum = params.get("NodeNum")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.LogstashVersion = params.get("LogstashVersion")
        self.LicenseType = params.get("LicenseType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Deadline = params.get("Deadline")
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = LogstashNodeInfo()
                obj._deserialize(item)
                self.Nodes.append(obj)
        self.BindedESInstanceId = params.get("BindedESInstanceId")
        self.YMLConfig = params.get("YMLConfig")
        if params.get("ExtendedFiles") is not None:
            self.ExtendedFiles = []
            for item in params.get("ExtendedFiles"):
                obj = LogstashExtendedFile()
                obj._deserialize(item)
                self.ExtendedFiles.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashNodeInfo(AbstractModel):
    """Logstash节点信息

    """

    def __init__(self):
        r"""
        :param NodeId: 节点ID
        :type NodeId: str
        :param Ip: 节点IP
        :type Ip: str
        :param Port: 节点端口
        :type Port: int
        """
        self.NodeId = None
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashPipeline(AbstractModel):
    """Logstash管道信息

    """

    def __init__(self):
        r"""
        :param PipelineId: 管道ID
        :type PipelineId: str
        :param PipelineDesc: 管道描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PipelineDesc: str
        :param Config: 管道配置内容
        :type Config: str
        :param Workers: 管道的Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Workers: int
        :param BatchSize: 管道批处理大小
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchSize: int
        :param BatchDelay: 管道批处理延迟
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchDelay: int
        :param QueueType: 管道缓冲队列类型
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueType: str
        :param QueueMaxBytes: 管道缓冲队列大小
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueMaxBytes: str
        :param QueueCheckPointWrites: 管道缓冲队列检查点写入数
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueCheckPointWrites: int
        """
        self.PipelineId = None
        self.PipelineDesc = None
        self.Config = None
        self.Workers = None
        self.BatchSize = None
        self.BatchDelay = None
        self.QueueType = None
        self.QueueMaxBytes = None
        self.QueueCheckPointWrites = None


    def _deserialize(self, params):
        self.PipelineId = params.get("PipelineId")
        self.PipelineDesc = params.get("PipelineDesc")
        self.Config = params.get("Config")
        self.Workers = params.get("Workers")
        self.BatchSize = params.get("BatchSize")
        self.BatchDelay = params.get("BatchDelay")
        self.QueueType = params.get("QueueType")
        self.QueueMaxBytes = params.get("QueueMaxBytes")
        self.QueueCheckPointWrites = params.get("QueueCheckPointWrites")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogstashPipelineInfo(AbstractModel):
    """Logstash管道信息

    """

    def __init__(self):
        r"""
        :param PipelineId: 管道ID
        :type PipelineId: str
        :param PipelineDesc: 管道描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PipelineDesc: str
        :param Config: 管道配置内容
        :type Config: str
        :param Status: 管道状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Workers: 管道的Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Workers: int
        :param BatchSize: 管道批处理大小
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchSize: int
        :param BatchDelay: 管道批处理延迟
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchDelay: int
        :param QueueType: 管道缓冲队列类型
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueType: str
        :param QueueMaxBytes: 管道缓冲队列大小
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueMaxBytes: str
        :param QueueCheckPointWrites: 管道缓冲队列检查点写入数
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueCheckPointWrites: int
        """
        self.PipelineId = None
        self.PipelineDesc = None
        self.Config = None
        self.Status = None
        self.Workers = None
        self.BatchSize = None
        self.BatchDelay = None
        self.QueueType = None
        self.QueueMaxBytes = None
        self.QueueCheckPointWrites = None


    def _deserialize(self, params):
        self.PipelineId = params.get("PipelineId")
        self.PipelineDesc = params.get("PipelineDesc")
        self.Config = params.get("Config")
        self.Status = params.get("Status")
        self.Workers = params.get("Workers")
        self.BatchSize = params.get("BatchSize")
        self.BatchDelay = params.get("BatchDelay")
        self.QueueType = params.get("QueueType")
        self.QueueMaxBytes = params.get("QueueMaxBytes")
        self.QueueCheckPointWrites = params.get("QueueCheckPointWrites")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MasterNodeInfo(AbstractModel):
    """实例专用主节点相关信息

    """

    def __init__(self):
        r"""
        :param EnableDedicatedMaster: 是否启用了专用主节点
        :type EnableDedicatedMaster: bool
        :param MasterNodeType: 专用主节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type MasterNodeType: str
        :param MasterNodeNum: 专用主节点个数
        :type MasterNodeNum: int
        :param MasterNodeCpuNum: 专用主节点CPU核数
        :type MasterNodeCpuNum: int
        :param MasterNodeMemSize: 专用主节点内存大小，单位GB
        :type MasterNodeMemSize: int
        :param MasterNodeDiskSize: 专用主节点磁盘大小，单位GB
        :type MasterNodeDiskSize: int
        :param MasterNodeDiskType: 专用主节点磁盘类型
        :type MasterNodeDiskType: str
        """
        self.EnableDedicatedMaster = None
        self.MasterNodeType = None
        self.MasterNodeNum = None
        self.MasterNodeCpuNum = None
        self.MasterNodeMemSize = None
        self.MasterNodeDiskSize = None
        self.MasterNodeDiskType = None


    def _deserialize(self, params):
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeCpuNum = params.get("MasterNodeCpuNum")
        self.MasterNodeMemSize = params.get("MasterNodeMemSize")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.MasterNodeDiskType = params.get("MasterNodeDiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """集群中一种节点类型（如热数据节点，冷数据节点，专用主节点等）的规格描述信息，包括节点类型，节点个数，节点规格，磁盘类型，磁盘大小等, Type不指定时默认为热数据节点；如果节点为master节点，则DiskType和DiskSize参数会被忽略（主节点无数据盘）

    """

    def __init__(self):
        r"""
        :param NodeNum: 节点数量
        :type NodeNum: int
        :param NodeType: 节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param Type: 节点类型<li>hotData: 热数据节点</li>
<li>warmData: 冷数据节点</li>
<li>dedicatedMaster: 专用主节点</li>
默认值为hotData
        :type Type: str
        :param DiskType: 节点磁盘类型<li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高硬能云硬盘</li>默认值CLOUD_SSD
        :type DiskType: str
        :param DiskSize: 节点磁盘容量（单位GB）
        :type DiskSize: int
        :param LocalDiskInfo: 节点本地盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDiskInfo: :class:`tencentcloud.es.v20180416.models.LocalDiskInfo`
        :param DiskCount: 节点磁盘块数
        :type DiskCount: int
        :param DiskEncrypt: 节点磁盘是否加密 0: 不加密，1: 加密；默认不加密
        :type DiskEncrypt: int
        :param CpuNum: cpu数目
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuNum: int
        :param MemSize: 内存大小，单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        """
        self.NodeNum = None
        self.NodeType = None
        self.Type = None
        self.DiskType = None
        self.DiskSize = None
        self.LocalDiskInfo = None
        self.DiskCount = None
        self.DiskEncrypt = None
        self.CpuNum = None
        self.MemSize = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.NodeType = params.get("NodeType")
        self.Type = params.get("Type")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        if params.get("LocalDiskInfo") is not None:
            self.LocalDiskInfo = LocalDiskInfo()
            self.LocalDiskInfo._deserialize(params.get("LocalDiskInfo"))
        self.DiskCount = params.get("DiskCount")
        self.DiskEncrypt = params.get("DiskEncrypt")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeView(AbstractModel):
    """节点维度视图数据

    """

    def __init__(self):
        r"""
        :param NodeId: 节点ID
        :type NodeId: str
        :param NodeIp: 节点IP
        :type NodeIp: str
        :param Visible: 节点是否可见
        :type Visible: float
        :param Break: 是否熔断
        :type Break: float
        :param DiskSize: 节点总磁盘大小
        :type DiskSize: int
        :param DiskUsage: 磁盘使用率
        :type DiskUsage: float
        :param MemSize: 节点内存大小，单位GB
        :type MemSize: int
        :param MemUsage: 内存使用率
        :type MemUsage: float
        :param CpuNum: 节点cpu个数
        :type CpuNum: int
        :param CpuUsage: cpu使用率
        :type CpuUsage: float
        :param Zone: 可用区
        :type Zone: str
        :param NodeRole: 节点角色
        :type NodeRole: str
        :param NodeHttpIp: 节点HTTP IP
        :type NodeHttpIp: str
        :param JvmMemUsage: JVM内存使用率
        :type JvmMemUsage: float
        :param ShardNum: 节点分片数
        :type ShardNum: int
        :param DiskIds: 节点上磁盘ID列表
        :type DiskIds: list of str
        :param Hidden: 是否为隐藏可用区
        :type Hidden: bool
        """
        self.NodeId = None
        self.NodeIp = None
        self.Visible = None
        self.Break = None
        self.DiskSize = None
        self.DiskUsage = None
        self.MemSize = None
        self.MemUsage = None
        self.CpuNum = None
        self.CpuUsage = None
        self.Zone = None
        self.NodeRole = None
        self.NodeHttpIp = None
        self.JvmMemUsage = None
        self.ShardNum = None
        self.DiskIds = None
        self.Hidden = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.NodeIp = params.get("NodeIp")
        self.Visible = params.get("Visible")
        self.Break = params.get("Break")
        self.DiskSize = params.get("DiskSize")
        self.DiskUsage = params.get("DiskUsage")
        self.MemSize = params.get("MemSize")
        self.MemUsage = params.get("MemUsage")
        self.CpuNum = params.get("CpuNum")
        self.CpuUsage = params.get("CpuUsage")
        self.Zone = params.get("Zone")
        self.NodeRole = params.get("NodeRole")
        self.NodeHttpIp = params.get("NodeHttpIp")
        self.JvmMemUsage = params.get("JvmMemUsage")
        self.ShardNum = params.get("ShardNum")
        self.DiskIds = params.get("DiskIds")
        self.Hidden = params.get("Hidden")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Operation(AbstractModel):
    """ES集群操作详细信息

    """

    def __init__(self):
        r"""
        :param Id: 操作唯一id
        :type Id: int
        :param StartTime: 操作开始时间
        :type StartTime: str
        :param Type: 操作类型
        :type Type: str
        :param Detail: 操作详情
        :type Detail: :class:`tencentcloud.es.v20180416.models.OperationDetail`
        :param Result: 操作结果
        :type Result: str
        :param Tasks: 流程任务信息
        :type Tasks: list of TaskDetail
        :param Progress: 操作进度
        :type Progress: float
        """
        self.Id = None
        self.StartTime = None
        self.Type = None
        self.Detail = None
        self.Result = None
        self.Tasks = None
        self.Progress = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        if params.get("Detail") is not None:
            self.Detail = OperationDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.Result = params.get("Result")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskDetail()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Progress = params.get("Progress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDetail(AbstractModel):
    """操作详情

    """

    def __init__(self):
        r"""
        :param OldInfo: 实例原始配置信息
        :type OldInfo: list of KeyValue
        :param NewInfo: 实例更新后配置信息
        :type NewInfo: list of KeyValue
        """
        self.OldInfo = None
        self.NewInfo = None


    def _deserialize(self, params):
        if params.get("OldInfo") is not None:
            self.OldInfo = []
            for item in params.get("OldInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self.OldInfo.append(obj)
        if params.get("NewInfo") is not None:
            self.NewInfo = []
            for item in params.get("NewInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self.NewInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDuration(AbstractModel):
    """集群可运维时间

    """

    def __init__(self):
        r"""
        :param Periods: 维护周期，表示周一到周日，可取值[0, 6]
注意：此字段可能返回 null，表示取不到有效值。
        :type Periods: list of int non-negative
        :param TimeStart: 维护开始时间
        :type TimeStart: str
        :param TimeEnd: 维护结束时间
        :type TimeEnd: str
        :param TimeZone: 时区，以UTC形式表示
        :type TimeZone: str
        """
        self.Periods = None
        self.TimeStart = None
        self.TimeEnd = None
        self.TimeZone = None


    def _deserialize(self, params):
        self.Periods = params.get("Periods")
        self.TimeStart = params.get("TimeStart")
        self.TimeEnd = params.get("TimeEnd")
        self.TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationDurationUpdated(AbstractModel):
    """集群可运维时间

    """

    def __init__(self):
        r"""
        :param Periods: 维护周期，表示周一到周日，可取值[0, 6]
        :type Periods: list of int non-negative
        :param TimeStart: 维护开始时间
        :type TimeStart: str
        :param TimeEnd: 维护结束时间
        :type TimeEnd: str
        :param TimeZone: 时区，以UTC形式表示
        :type TimeZone: str
        :param MoreInstances: ES集群ID数组
        :type MoreInstances: list of str
        """
        self.Periods = None
        self.TimeStart = None
        self.TimeEnd = None
        self.TimeZone = None
        self.MoreInstances = None


    def _deserialize(self, params):
        self.Periods = params.get("Periods")
        self.TimeStart = params.get("TimeStart")
        self.TimeEnd = params.get("TimeEnd")
        self.TimeZone = params.get("TimeZone")
        self.MoreInstances = params.get("MoreInstances")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OptionalWebServiceInfo(AbstractModel):
    """可选web组件信息

    """

    def __init__(self):
        r"""
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param PublicUrl: 公网url
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicUrl: str
        :param PrivateUrl: 内网url
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateUrl: str
        :param PublicAccess: 公网访问权限
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicAccess: str
        :param PrivateAccess: 内网访问权限
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateAccess: str
        :param Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self.Type = None
        self.Status = None
        self.PublicUrl = None
        self.PrivateUrl = None
        self.PublicAccess = None
        self.PrivateAccess = None
        self.Version = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.PublicUrl = params.get("PublicUrl")
        self.PrivateUrl = params.get("PrivateUrl")
        self.PublicAccess = params.get("PublicAccess")
        self.PrivateAccess = params.get("PrivateAccess")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceRequest(AbstractModel):
    """RestartInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ForceRestart: 是否强制重启<li>true：强制重启</li><li>false：不强制重启</li>默认false
        :type ForceRestart: bool
        :param RestartMode: 重启模式：0 滚动重启； 1 全量重启
        :type RestartMode: int
        """
        self.InstanceId = None
        self.ForceRestart = None
        self.RestartMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ForceRestart = params.get("ForceRestart")
        self.RestartMode = params.get("RestartMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceResponse(AbstractModel):
    """RestartInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartKibanaRequest(AbstractModel):
    """RestartKibana请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ES实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartKibanaResponse(AbstractModel):
    """RestartKibana返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartLogstashInstanceRequest(AbstractModel):
    """RestartLogstashInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Type: 重启类型，0全量重启，1滚动重启
        :type Type: int
        """
        self.InstanceId = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartLogstashInstanceResponse(AbstractModel):
    """RestartLogstashInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartNodesRequest(AbstractModel):
    """RestartNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例ID
        :type InstanceId: str
        :param NodeNames: 节点名称列表
        :type NodeNames: list of str
        :param ForceRestart: 是否强制重启
        :type ForceRestart: bool
        """
        self.InstanceId = None
        self.NodeNames = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeNames = params.get("NodeNames")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartNodesResponse(AbstractModel):
    """RestartNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SaveAndDeployLogstashPipelineRequest(AbstractModel):
    """SaveAndDeployLogstashPipeline请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Pipeline: 实例管道信息
        :type Pipeline: :class:`tencentcloud.es.v20180416.models.LogstashPipeline`
        :param OpType: 操作类型<li>1：只保存</li><li>2：保存并部署</li>
        :type OpType: int
        """
        self.InstanceId = None
        self.Pipeline = None
        self.OpType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Pipeline") is not None:
            self.Pipeline = LogstashPipeline()
            self.Pipeline._deserialize(params.get("Pipeline"))
        self.OpType = params.get("OpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveAndDeployLogstashPipelineResponse(AbstractModel):
    """SaveAndDeployLogstashPipeline返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartLogstashPipelinesRequest(AbstractModel):
    """StartLogstashPipelines请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param PipelineIds: 管道ID列表
        :type PipelineIds: list of str
        """
        self.InstanceId = None
        self.PipelineIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PipelineIds = params.get("PipelineIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartLogstashPipelinesResponse(AbstractModel):
    """StartLogstashPipelines返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopLogstashPipelinesRequest(AbstractModel):
    """StopLogstashPipelines请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param PipelineIds: 管道ID列表
        :type PipelineIds: list of str
        """
        self.InstanceId = None
        self.PipelineIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PipelineIds = params.get("PipelineIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopLogstashPipelinesResponse(AbstractModel):
    """StopLogstashPipelines返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubTaskDetail(AbstractModel):
    """实例操作记录流程任务中的子任务信息（如升级检查任务中的各个检查项）

    """

    def __init__(self):
        r"""
        :param Name: 子任务名
        :type Name: str
        :param Result: 子任务结果
        :type Result: bool
        :param ErrMsg: 子任务错误信息
        :type ErrMsg: str
        :param Type: 子任务类型
        :type Type: str
        :param Status: 子任务状态，0处理中 1成功 -1失败
        :type Status: int
        :param FailedIndices: 升级检查失败的索引名
        :type FailedIndices: list of str
        :param FinishTime: 子任务结束时间
        :type FinishTime: str
        :param Level: 子任务等级，1警告 2失败
        :type Level: int
        """
        self.Name = None
        self.Result = None
        self.ErrMsg = None
        self.Type = None
        self.Status = None
        self.FailedIndices = None
        self.FinishTime = None
        self.Level = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.FailedIndices = params.get("FailedIndices")
        self.FinishTime = params.get("FinishTime")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """实例标签信息

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
        


class TaskDetail(AbstractModel):
    """实例操作记录中的流程任务信息

    """

    def __init__(self):
        r"""
        :param Name: 任务名
        :type Name: str
        :param Progress: 任务进度
        :type Progress: float
        :param FinishTime: 任务完成时间
        :type FinishTime: str
        :param SubTasks: 子任务
        :type SubTasks: list of SubTaskDetail
        """
        self.Name = None
        self.Progress = None
        self.FinishTime = None
        self.SubTasks = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Progress = params.get("Progress")
        self.FinishTime = params.get("FinishTime")
        if params.get("SubTasks") is not None:
            self.SubTasks = []
            for item in params.get("SubTasks"):
                obj = SubTaskDetail()
                obj._deserialize(item)
                self.SubTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDiagnoseSettingsRequest(AbstractModel):
    """UpdateDiagnoseSettings请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ES实例ID
        :type InstanceId: str
        :param Status: 0：开启智能运维；-1：关闭智能运维
        :type Status: int
        :param CronTime: 智能运维每天定时巡检时间
        :type CronTime: str
        """
        self.InstanceId = None
        self.Status = None
        self.CronTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        self.CronTime = params.get("CronTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDiagnoseSettingsResponse(AbstractModel):
    """UpdateDiagnoseSettings返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDictionariesRequest(AbstractModel):
    """UpdateDictionaries请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ES实例ID
        :type InstanceId: str
        :param IkMainDicts: IK分词主词典COS地址
        :type IkMainDicts: list of str
        :param IkStopwords: IK分词停用词词典COS地址
        :type IkStopwords: list of str
        :param Synonym: 同义词词典COS地址
        :type Synonym: list of str
        :param QQDict: QQ分词词典COS地址
        :type QQDict: list of str
        :param UpdateType: 0：安装；1：删除。默认值0
        :type UpdateType: int
        :param ForceRestart: 是否强制重启集群。默认值false
        :type ForceRestart: bool
        """
        self.InstanceId = None
        self.IkMainDicts = None
        self.IkStopwords = None
        self.Synonym = None
        self.QQDict = None
        self.UpdateType = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IkMainDicts = params.get("IkMainDicts")
        self.IkStopwords = params.get("IkStopwords")
        self.Synonym = params.get("Synonym")
        self.QQDict = params.get("QQDict")
        self.UpdateType = params.get("UpdateType")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDictionariesResponse(AbstractModel):
    """UpdateDictionaries返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateIndexRequest(AbstractModel):
    """UpdateIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ES集群ID
        :type InstanceId: str
        :param IndexType: 更新的索引类型。auto：自治索引；normal：普通索引
        :type IndexType: str
        :param IndexName: 更新的索引名
        :type IndexName: str
        :param UpdateMetaJson: 更新的索引元数据JSON，如mappings、settings
        :type UpdateMetaJson: str
        :param Username: 集群访问用户名
        :type Username: str
        :param Password: 集群访问密码
        :type Password: str
        :param RolloverBackingIndex: 是否滚动后备索引
        :type RolloverBackingIndex: bool
        """
        self.InstanceId = None
        self.IndexType = None
        self.IndexName = None
        self.UpdateMetaJson = None
        self.Username = None
        self.Password = None
        self.RolloverBackingIndex = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IndexType = params.get("IndexType")
        self.IndexName = params.get("IndexName")
        self.UpdateMetaJson = params.get("UpdateMetaJson")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.RolloverBackingIndex = params.get("RolloverBackingIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateIndexResponse(AbstractModel):
    """UpdateIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateInstanceRequest(AbstractModel):
    """UpdateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称（1-50 个英文、汉字、数字、连接线-或下划线_）
        :type InstanceName: str
        :param NodeNum: 已废弃请使用NodeInfoList
节点个数（2-50个）
        :type NodeNum: int
        :param EsConfig: ES配置项（JSON格式字符串）
        :type EsConfig: str
        :param Password: 默认用户elastic的密码（8到16位，至少包括两项（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）
        :type Password: str
        :param EsAcl: 访问控制列表
        :type EsAcl: :class:`tencentcloud.es.v20180416.models.EsAcl`
        :param DiskSize: 已废弃请使用NodeInfoList
磁盘大小（单位GB）
        :type DiskSize: int
        :param NodeType: 已废弃请使用NodeInfoList
节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param MasterNodeNum: 已废弃请使用NodeInfoList
专用主节点个数（只支持3个或5个）
        :type MasterNodeNum: int
        :param MasterNodeType: 已废弃请使用NodeInfoList
专用主节点规格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type MasterNodeType: str
        :param MasterNodeDiskSize: 已废弃请使用NodeInfoList
专用主节点磁盘大小（单位GB系统默认配置为50GB,暂不支持自定义）
        :type MasterNodeDiskSize: int
        :param ForceRestart: 更新配置时是否强制重启<li>true强制重启</li><li>false不强制重启</li>当前仅更新EsConfig时需要设置，默认值为false
        :type ForceRestart: bool
        :param CosBackup: COS自动备份信息
        :type CosBackup: :class:`tencentcloud.es.v20180416.models.CosBackup`
        :param NodeInfoList: 节点信息列表，可以只传递要更新的节点及其对应的规格信息。支持的操作包括<li>修改一种节点的个数</li><li>修改一种节点的节点规格及磁盘大小</li><li>增加一种节点类型（需要同时指定该节点的类型，个数，规格，磁盘等信息）</li>上述操作一次只能进行一种，且磁盘类型不支持修改
        :type NodeInfoList: list of NodeInfo
        :param PublicAccess: 公网访问状态
        :type PublicAccess: str
        :param EsPublicAcl: 公网访问控制列表
        :type EsPublicAcl: :class:`tencentcloud.es.v20180416.models.EsPublicAcl`
        :param KibanaPublicAccess: Kibana公网访问状态
        :type KibanaPublicAccess: str
        :param KibanaPrivateAccess: Kibana内网访问状态
        :type KibanaPrivateAccess: str
        :param BasicSecurityType: ES 6.8及以上版本基础版开启或关闭用户认证
        :type BasicSecurityType: int
        :param KibanaPrivatePort: Kibana内网端口
        :type KibanaPrivatePort: int
        :param ScaleType: 0: 蓝绿变更方式扩容，集群不重启 （默认） 1: 磁盘解挂载扩容，集群滚动重启
        :type ScaleType: int
        :param MultiZoneInfo: 多可用区部署
        :type MultiZoneInfo: list of ZoneDetail
        :param SceneType: 场景化模板类型 -1：不启用 1：通用 2：日志 3：搜索
        :type SceneType: int
        :param KibanaConfig: Kibana配置项（JSON格式字符串）
        :type KibanaConfig: str
        :param WebNodeTypeInfo: 可视化节点配置
        :type WebNodeTypeInfo: :class:`tencentcloud.es.v20180416.models.WebNodeTypeInfo`
        :param SwitchPrivateLink: 切换到新网络架构
        :type SwitchPrivateLink: str
        :param EnableCerebro: 启用Cerebro
        :type EnableCerebro: bool
        :param CerebroPublicAccess: Cerebro公网访问状态
        :type CerebroPublicAccess: str
        :param CerebroPrivateAccess: Cerebro内网访问状态
        :type CerebroPrivateAccess: str
        :param EsConfigSet: 新增或修改的配置组信息
        :type EsConfigSet: :class:`tencentcloud.es.v20180416.models.EsConfigSetInfo`
        :param OperationDuration: 可维护时间段
        :type OperationDuration: :class:`tencentcloud.es.v20180416.models.OperationDurationUpdated`
        """
        self.InstanceId = None
        self.InstanceName = None
        self.NodeNum = None
        self.EsConfig = None
        self.Password = None
        self.EsAcl = None
        self.DiskSize = None
        self.NodeType = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ForceRestart = None
        self.CosBackup = None
        self.NodeInfoList = None
        self.PublicAccess = None
        self.EsPublicAcl = None
        self.KibanaPublicAccess = None
        self.KibanaPrivateAccess = None
        self.BasicSecurityType = None
        self.KibanaPrivatePort = None
        self.ScaleType = None
        self.MultiZoneInfo = None
        self.SceneType = None
        self.KibanaConfig = None
        self.WebNodeTypeInfo = None
        self.SwitchPrivateLink = None
        self.EnableCerebro = None
        self.CerebroPublicAccess = None
        self.CerebroPrivateAccess = None
        self.EsConfigSet = None
        self.OperationDuration = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.NodeNum = params.get("NodeNum")
        self.EsConfig = params.get("EsConfig")
        self.Password = params.get("Password")
        if params.get("EsAcl") is not None:
            self.EsAcl = EsAcl()
            self.EsAcl._deserialize(params.get("EsAcl"))
        self.DiskSize = params.get("DiskSize")
        self.NodeType = params.get("NodeType")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ForceRestart = params.get("ForceRestart")
        if params.get("CosBackup") is not None:
            self.CosBackup = CosBackup()
            self.CosBackup._deserialize(params.get("CosBackup"))
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        self.PublicAccess = params.get("PublicAccess")
        if params.get("EsPublicAcl") is not None:
            self.EsPublicAcl = EsPublicAcl()
            self.EsPublicAcl._deserialize(params.get("EsPublicAcl"))
        self.KibanaPublicAccess = params.get("KibanaPublicAccess")
        self.KibanaPrivateAccess = params.get("KibanaPrivateAccess")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.KibanaPrivatePort = params.get("KibanaPrivatePort")
        self.ScaleType = params.get("ScaleType")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = ZoneDetail()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.SceneType = params.get("SceneType")
        self.KibanaConfig = params.get("KibanaConfig")
        if params.get("WebNodeTypeInfo") is not None:
            self.WebNodeTypeInfo = WebNodeTypeInfo()
            self.WebNodeTypeInfo._deserialize(params.get("WebNodeTypeInfo"))
        self.SwitchPrivateLink = params.get("SwitchPrivateLink")
        self.EnableCerebro = params.get("EnableCerebro")
        self.CerebroPublicAccess = params.get("CerebroPublicAccess")
        self.CerebroPrivateAccess = params.get("CerebroPrivateAccess")
        if params.get("EsConfigSet") is not None:
            self.EsConfigSet = EsConfigSetInfo()
            self.EsConfigSet._deserialize(params.get("EsConfigSet"))
        if params.get("OperationDuration") is not None:
            self.OperationDuration = OperationDurationUpdated()
            self.OperationDuration._deserialize(params.get("OperationDuration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceResponse(AbstractModel):
    """UpdateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class UpdateJdkRequest(AbstractModel):
    """UpdateJdk请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: ES实例ID
        :type InstanceId: str
        :param Jdk: Jdk类型，支持kona和oracle
        :type Jdk: str
        :param Gc: Gc类型，支持g1和cms
        :type Gc: str
        :param ForceRestart: 是否强制重启
        :type ForceRestart: bool
        """
        self.InstanceId = None
        self.Jdk = None
        self.Gc = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Jdk = params.get("Jdk")
        self.Gc = params.get("Gc")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateJdkResponse(AbstractModel):
    """UpdateJdk返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateLogstashInstanceRequest(AbstractModel):
    """UpdateLogstashInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param NodeNum: 实例节点数量
        :type NodeNum: int
        :param YMLConfig: 实例YML配置
        :type YMLConfig: str
        :param BindedES: 实例绑定的ES集群信息
        :type BindedES: :class:`tencentcloud.es.v20180416.models.LogstashBindedES`
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param ExtendedFiles: 扩展文件列表
        :type ExtendedFiles: list of LogstashExtendedFile
        :param NodeType: 实例规格
        :type NodeType: str
        :param DiskSize: 节点磁盘容量
        :type DiskSize: int
        """
        self.InstanceId = None
        self.NodeNum = None
        self.YMLConfig = None
        self.BindedES = None
        self.InstanceName = None
        self.ExtendedFiles = None
        self.NodeType = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeNum = params.get("NodeNum")
        self.YMLConfig = params.get("YMLConfig")
        if params.get("BindedES") is not None:
            self.BindedES = LogstashBindedES()
            self.BindedES._deserialize(params.get("BindedES"))
        self.InstanceName = params.get("InstanceName")
        if params.get("ExtendedFiles") is not None:
            self.ExtendedFiles = []
            for item in params.get("ExtendedFiles"):
                obj = LogstashExtendedFile()
                obj._deserialize(item)
                self.ExtendedFiles.append(obj)
        self.NodeType = params.get("NodeType")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateLogstashInstanceResponse(AbstractModel):
    """UpdateLogstashInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateLogstashPipelineDescRequest(AbstractModel):
    """UpdateLogstashPipelineDesc请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param PipelineId: 实例管道ID
        :type PipelineId: str
        :param PipelineDesc: 管道描述信息
        :type PipelineDesc: str
        """
        self.InstanceId = None
        self.PipelineId = None
        self.PipelineDesc = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PipelineId = params.get("PipelineId")
        self.PipelineDesc = params.get("PipelineDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateLogstashPipelineDescResponse(AbstractModel):
    """UpdateLogstashPipelineDesc返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePluginsRequest(AbstractModel):
    """UpdatePlugins请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstallPluginList: 需要安装的插件名列表
        :type InstallPluginList: list of str
        :param RemovePluginList: 需要卸载的插件名列表
        :type RemovePluginList: list of str
        :param ForceRestart: 是否强制重启，默认值false
        :type ForceRestart: bool
        :param ForceUpdate: 是否重新安装，默认值false
        :type ForceUpdate: bool
        :param PluginType: 0：系统插件
        :type PluginType: int
        """
        self.InstanceId = None
        self.InstallPluginList = None
        self.RemovePluginList = None
        self.ForceRestart = None
        self.ForceUpdate = None
        self.PluginType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstallPluginList = params.get("InstallPluginList")
        self.RemovePluginList = params.get("RemovePluginList")
        self.ForceRestart = params.get("ForceRestart")
        self.ForceUpdate = params.get("ForceUpdate")
        self.PluginType = params.get("PluginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePluginsResponse(AbstractModel):
    """UpdatePlugins返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRequestTargetNodeTypesRequest(AbstractModel):
    """UpdateRequestTargetNodeTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param TargetNodeTypes: 接收请求的目标节点类型列表
        :type TargetNodeTypes: list of str
        """
        self.InstanceId = None
        self.TargetNodeTypes = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TargetNodeTypes = params.get("TargetNodeTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRequestTargetNodeTypesResponse(AbstractModel):
    """UpdateRequestTargetNodeTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param EsVersion: 目标ES版本，支持：”6.4.3“, "6.8.2"，"7.5.1"
        :type EsVersion: str
        :param CheckOnly: 是否只做升级检查，默认值为false
        :type CheckOnly: bool
        :param LicenseType: 目标商业特性版本：<li>oss 开源版</li><li>basic 基础版</li>当前仅在5.6.4升级6.x版本时使用，默认值为basic
        :type LicenseType: str
        :param BasicSecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
        :type BasicSecurityType: int
        :param UpgradeMode: 升级方式：<li>scale 蓝绿变更</li><li>restart 滚动重启</li>默认值为scale
        :type UpgradeMode: str
        :param CosBackup: 升级版本前是否对集群进行备份，默认不备份
        :type CosBackup: bool
        """
        self.InstanceId = None
        self.EsVersion = None
        self.CheckOnly = None
        self.LicenseType = None
        self.BasicSecurityType = None
        self.UpgradeMode = None
        self.CosBackup = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EsVersion = params.get("EsVersion")
        self.CheckOnly = params.get("CheckOnly")
        self.LicenseType = params.get("LicenseType")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.UpgradeMode = params.get("UpgradeMode")
        self.CosBackup = params.get("CosBackup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeLicenseRequest(AbstractModel):
    """UpgradeLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param LicenseType: License类型<li>oss：开源版</li><li>basic：基础版</li><li>platinum：白金版</li>默认值platinum
        :type LicenseType: str
        :param AutoVoucher: 是否自动使用代金券<li>0：不自动使用</li><li>1：自动使用</li>默认值0
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表（目前仅支持指定一张代金券）
        :type VoucherIds: list of str
        :param BasicSecurityType: 6.8（及以上版本）基础版是否开启xpack security认证<li>1：不开启</li><li>2：开启</li>
        :type BasicSecurityType: int
        :param ForceRestart: 是否强制重启<li>true强制重启</li><li>false不强制重启</li> 默认值false
        :type ForceRestart: bool
        """
        self.InstanceId = None
        self.LicenseType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.BasicSecurityType = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LicenseType = params.get("LicenseType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.BasicSecurityType = params.get("BasicSecurityType")
        self.ForceRestart = params.get("ForceRestart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLicenseResponse(AbstractModel):
    """UpgradeLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class WebNodeTypeInfo(AbstractModel):
    """可视化节点配置

    """

    def __init__(self):
        r"""
        :param NodeNum: 可视化节点个数，固定为1
        :type NodeNum: int
        :param NodeType: 可视化节点规格
        :type NodeType: str
        """
        self.NodeNum = None
        self.NodeType = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDetail(AbstractModel):
    """多可用区部署时可用区的详细信息

    """

    def __init__(self):
        r"""
        :param Zone: 可用区
        :type Zone: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        """
        self.Zone = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        