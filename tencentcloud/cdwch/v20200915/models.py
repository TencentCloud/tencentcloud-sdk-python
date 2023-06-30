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


class ActionAlterCkUserRequest(AbstractModel):
    """ActionAlterCkUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserInfo: 用户信息
        :type UserInfo: :class:`tencentcloud.cdwch.v20200915.models.CkUserAlterInfo`
        :param ApiType: api接口类型，
AddSystemUser新增用户，UpdateSystemUser，修改用户
        :type ApiType: str
        """
        self.UserInfo = None
        self.ApiType = None


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self.UserInfo = CkUserAlterInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        self.ApiType = params.get("ApiType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionAlterCkUserResponse(AbstractModel):
    """ActionAlterCkUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class AttachCBSSpec(AbstractModel):
    """集群内节点的规格磁盘规格描述

    """

    def __init__(self):
        r"""
        :param DiskType: 节点磁盘类型，例如“CLOUD_SSD”\"CLOUD_PREMIUM"
        :type DiskType: str
        :param DiskSize: 磁盘容量，单位G
        :type DiskSize: int
        :param DiskCount: 磁盘总数
        :type DiskCount: int
        :param DiskDesc: 描述
        :type DiskDesc: str
        """
        self.DiskType = None
        self.DiskSize = None
        self.DiskCount = None
        self.DiskDesc = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.DiskCount = params.get("DiskCount")
        self.DiskDesc = params.get("DiskDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupTableContent(AbstractModel):
    """备份表信息

    """

    def __init__(self):
        r"""
        :param Database: 数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param Table: 表
注意：此字段可能返回 null，表示取不到有效值。
        :type Table: str
        :param TotalBytes: 表总字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalBytes: int
        :param VCluster: 虚拟cluster
注意：此字段可能返回 null，表示取不到有效值。
        :type VCluster: str
        :param Ips: 表ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Ips: str
        :param ZooPath: zk路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ZooPath: str
        :param Rip: cvm的ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Rip: str
        """
        self.Database = None
        self.Table = None
        self.TotalBytes = None
        self.VCluster = None
        self.Ips = None
        self.ZooPath = None
        self.Rip = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.TotalBytes = params.get("TotalBytes")
        self.VCluster = params.get("VCluster")
        self.Ips = params.get("Ips")
        self.ZooPath = params.get("ZooPath")
        self.Rip = params.get("Rip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Charge(AbstractModel):
    """集群计费相关信息

    """

    def __init__(self):
        r"""
        :param ChargeType: 计费类型，“PREPAID” 预付费，“POSTPAID_BY_HOUR” 后付费
        :type ChargeType: str
        :param RenewFlag: PREPAID需要传递，是否自动续费，1表示自动续费开启
        :type RenewFlag: int
        :param TimeSpan: 预付费需要传递，计费时间长度，多少个月
        :type TimeSpan: int
        """
        self.ChargeType = None
        self.RenewFlag = None
        self.TimeSpan = None


    def _deserialize(self, params):
        self.ChargeType = params.get("ChargeType")
        self.RenewFlag = params.get("RenewFlag")
        self.TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkUserAlterInfo(AbstractModel):
    """新增或是修改ck用户

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例id
        :type InstanceId: str
        :param UserName: 用户名
        :type UserName: str
        :param PassWord: 密码
        :type PassWord: str
        :param Describe: 描述
        :type Describe: str
        """
        self.InstanceId = None
        self.UserName = None
        self.PassWord = None
        self.Describe = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.PassWord = params.get("PassWord")
        self.Describe = params.get("Describe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterConfigsInfoFromEMR(AbstractModel):
    """用于返回XML格式的配置文件和内容以及其他配置文件有关的信息

    """

    def __init__(self):
        r"""
        :param FileName: 配置文件名称
        :type FileName: str
        :param FileConf: 配置文件对应的相关属性信息
        :type FileConf: str
        :param KeyConf: 配置文件对应的其他属性信息
        :type KeyConf: str
        :param OriParam: 配置文件的内容，base64编码
        :type OriParam: str
        :param NeedRestart: 用于表示当前配置文件是不是有过修改后没有重启，提醒用户需要重启
        :type NeedRestart: int
        :param FilePath: 保存配置文件的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        """
        self.FileName = None
        self.FileConf = None
        self.KeyConf = None
        self.OriParam = None
        self.NeedRestart = None
        self.FilePath = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileConf = params.get("FileConf")
        self.KeyConf = params.get("KeyConf")
        self.OriParam = params.get("OriParam")
        self.NeedRestart = params.get("NeedRestart")
        self.FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInfo(AbstractModel):
    """clickhouse vcluster信息

    """

    def __init__(self):
        r"""
        :param ClusterName: vcluster名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NodeIps: 当前cluster的IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeIps: list of str
        """
        self.ClusterName = None
        self.NodeIps = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.NodeIps = params.get("NodeIps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigSubmitContext(AbstractModel):
    """配置文件修改信息

    """

    def __init__(self):
        r"""
        :param FileName: 配置文件名称
        :type FileName: str
        :param OldConfValue: 配置文件旧内容，base64编码
        :type OldConfValue: str
        :param NewConfValue: 配置文件新内容，base64编码
        :type NewConfValue: str
        :param FilePath: 保存配置文件的路径
        :type FilePath: str
        """
        self.FileName = None
        self.OldConfValue = None
        self.NewConfValue = None
        self.FilePath = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.OldConfValue = params.get("OldConfValue")
        self.NewConfValue = params.get("NewConfValue")
        self.FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackUpScheduleRequest(AbstractModel):
    """CreateBackUpSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScheduleId: 编辑时需要传
        :type ScheduleId: int
        :param WeekDays: 选择的星期 逗号分隔，例如 2 代表周二
        :type WeekDays: str
        :param ExecuteHour: 执行小时
        :type ExecuteHour: int
        :param BackUpTables: 备份表列表
        :type BackUpTables: list of BackupTableContent
        """
        self.ScheduleId = None
        self.WeekDays = None
        self.ExecuteHour = None
        self.BackUpTables = None


    def _deserialize(self, params):
        self.ScheduleId = params.get("ScheduleId")
        self.WeekDays = params.get("WeekDays")
        self.ExecuteHour = params.get("ExecuteHour")
        if params.get("BackUpTables") is not None:
            self.BackUpTables = []
            for item in params.get("BackUpTables"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self.BackUpTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackUpScheduleResponse(AbstractModel):
    """CreateBackUpSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateInstanceNewRequest(AbstractModel):
    """CreateInstanceNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区
        :type Zone: str
        :param HaFlag: 是否高可用
        :type HaFlag: bool
        :param UserVPCId: 私有网络
        :type UserVPCId: str
        :param UserSubnetId: 子网
        :type UserSubnetId: str
        :param ProductVersion: 版本
        :type ProductVersion: str
        :param ChargeProperties: 计费方式
        :type ChargeProperties: :class:`tencentcloud.cdwch.v20200915.models.Charge`
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param DataSpec: 数据节点
        :type DataSpec: :class:`tencentcloud.cdwch.v20200915.models.NodeSpec`
        :param Tags: 标签列表
        :type Tags: :class:`tencentcloud.cdwch.v20200915.models.Tag`
        :param ClsLogSetId: 日志主题ID
        :type ClsLogSetId: str
        :param CosBucketName: COS桶名称
        :type CosBucketName: str
        :param MountDiskType: 是否是裸盘挂载
        :type MountDiskType: int
        :param HAZk: 是否是ZK高可用
        :type HAZk: bool
        :param CommonSpec: ZK节点
        :type CommonSpec: :class:`tencentcloud.cdwch.v20200915.models.NodeSpec`
        """
        self.Zone = None
        self.HaFlag = None
        self.UserVPCId = None
        self.UserSubnetId = None
        self.ProductVersion = None
        self.ChargeProperties = None
        self.InstanceName = None
        self.DataSpec = None
        self.Tags = None
        self.ClsLogSetId = None
        self.CosBucketName = None
        self.MountDiskType = None
        self.HAZk = None
        self.CommonSpec = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.HaFlag = params.get("HaFlag")
        self.UserVPCId = params.get("UserVPCId")
        self.UserSubnetId = params.get("UserSubnetId")
        self.ProductVersion = params.get("ProductVersion")
        if params.get("ChargeProperties") is not None:
            self.ChargeProperties = Charge()
            self.ChargeProperties._deserialize(params.get("ChargeProperties"))
        self.InstanceName = params.get("InstanceName")
        if params.get("DataSpec") is not None:
            self.DataSpec = NodeSpec()
            self.DataSpec._deserialize(params.get("DataSpec"))
        if params.get("Tags") is not None:
            self.Tags = Tag()
            self.Tags._deserialize(params.get("Tags"))
        self.ClsLogSetId = params.get("ClsLogSetId")
        self.CosBucketName = params.get("CosBucketName")
        self.MountDiskType = params.get("MountDiskType")
        self.HAZk = params.get("HAZk")
        if params.get("CommonSpec") is not None:
            self.CommonSpec = NodeSpec()
            self.CommonSpec._deserialize(params.get("CommonSpec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceNewResponse(AbstractModel):
    """CreateInstanceNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.InstanceId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InstanceId = params.get("InstanceId")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class DescribeBackUpScheduleRequest(AbstractModel):
    """DescribeBackUpSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群id
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
        


class DescribeBackUpScheduleResponse(AbstractModel):
    """DescribeBackUpSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param BackUpOpened: 备份是否开启
        :type BackUpOpened: bool
        :param MetaStrategy: 元数据备份策略
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaStrategy: :class:`tencentcloud.cdwch.v20200915.models.ScheduleStrategy`
        :param DataStrategy: 表数据备份策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DataStrategy: :class:`tencentcloud.cdwch.v20200915.models.ScheduleStrategy`
        :param BackUpContents: 备份表列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BackUpContents: list of BackupTableContent
        :param BackUpStatus: 备份的状态
        :type BackUpStatus: int
        :param ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BackUpOpened = None
        self.MetaStrategy = None
        self.DataStrategy = None
        self.BackUpContents = None
        self.BackUpStatus = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackUpOpened = params.get("BackUpOpened")
        if params.get("MetaStrategy") is not None:
            self.MetaStrategy = ScheduleStrategy()
            self.MetaStrategy._deserialize(params.get("MetaStrategy"))
        if params.get("DataStrategy") is not None:
            self.DataStrategy = ScheduleStrategy()
            self.DataStrategy._deserialize(params.get("DataStrategy"))
        if params.get("BackUpContents") is not None:
            self.BackUpContents = []
            for item in params.get("BackUpContents"):
                obj = BackupTableContent()
                obj._deserialize(item)
                self.BackUpContents.append(obj)
        self.BackUpStatus = params.get("BackUpStatus")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class DescribeCkSqlApisRequest(AbstractModel):
    """DescribeCkSqlApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param ApiType: api接口名称,GetClusters:获取集群cluster列表
GetSystemUsers:获取系统用户列表
CheckNodeCluster: 检查节点是否隶属一个cluster
GetClusterDatabases: 获取一个cluster下的数据库列表
GetClusterTables: 获取一个cluster下的数据库表列表
GetPrivilegeUsers: 获取授权的用户列表
GET_USER_CLUSTER_PRIVILEGES:获取用户cluster下的权限   
GetUserClusterNewPrivileges:获取用户cluster下的权限 (新版）
RevokeClusterUser:解绑cluster用户
DeleteSystemUser:删除系统用户 —— 必须所有cluster先解绑
GetUserOptionMessages:获取用户配置备注信息
GET_USER_CONFIGS:获取用户配置列表  QUOTA、PROFILE、POLICY
        :type ApiType: str
        :param Cluster: 集群名称，GET_SYSTEM_USERS，GET_PRIVILEGE_USERS，GET_CLUSTER_DATABASES，GET_CLUSTER_TABLES 必填
        :type Cluster: str
        :param UserName: 用户名称，api与user相关的必填
        :type UserName: str
        """
        self.InstanceId = None
        self.ApiType = None
        self.Cluster = None
        self.UserName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ApiType = params.get("ApiType")
        self.Cluster = params.get("Cluster")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCkSqlApisResponse(AbstractModel):
    """DescribeCkSqlApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReturnData: 返回的查询数据，大部分情况是list，也可能是bool
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReturnData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnData = params.get("ReturnData")
        self.RequestId = params.get("RequestId")


class DescribeClusterConfigsRequest(AbstractModel):
    """DescribeClusterConfigs请求参数结构体

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
        


class DescribeClusterConfigsResponse(AbstractModel):
    """DescribeClusterConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterConfList: 返回实例的配置文件相关的信息
        :type ClusterConfList: list of ClusterConfigsInfoFromEMR
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterConfList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterConfList") is not None:
            self.ClusterConfList = []
            for item in params.get("ClusterConfList"):
                obj = ClusterConfigsInfoFromEMR()
                obj._deserialize(item)
                self.ClusterConfList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceClustersRequest(AbstractModel):
    """DescribeInstanceClusters请求参数结构体

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
        


class DescribeInstanceClustersResponse(AbstractModel):
    """DescribeInstanceClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param Clusters: cluster列表
        :type Clusters: list of ClusterInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Clusters = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Clusters") is not None:
            self.Clusters = []
            for item in params.get("Clusters"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceKeyValConfigsRequest(AbstractModel):
    """DescribeInstanceKeyValConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例ID
        :type InstanceId: str
        :param SearchConfigName: 搜索的配置项名称
        :type SearchConfigName: str
        """
        self.InstanceId = None
        self.SearchConfigName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchConfigName = params.get("SearchConfigName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceKeyValConfigsResponse(AbstractModel):
    """DescribeInstanceKeyValConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param ConfigItems: 参数列表
        :type ConfigItems: list of InstanceConfigInfo
        :param UnConfigItems: 未配置的参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UnConfigItems: list of InstanceConfigInfo
        :param MapConfigItems: 配置的多层级参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MapConfigItems: list of MapConfigItem
        :param ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConfigItems = None
        self.UnConfigItems = None
        self.MapConfigItems = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ConfigItems") is not None:
            self.ConfigItems = []
            for item in params.get("ConfigItems"):
                obj = InstanceConfigInfo()
                obj._deserialize(item)
                self.ConfigItems.append(obj)
        if params.get("UnConfigItems") is not None:
            self.UnConfigItems = []
            for item in params.get("UnConfigItems"):
                obj = InstanceConfigInfo()
                obj._deserialize(item)
                self.UnConfigItems.append(obj)
        if params.get("MapConfigItems") is not None:
            self.MapConfigItems = []
            for item in params.get("MapConfigItems"):
                obj = MapConfigItem()
                obj._deserialize(item)
                self.MapConfigItems.append(obj)
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例ID
        :type InstanceId: str
        :param IsOpenApi: 是否是open api查询
        :type IsOpenApi: bool
        """
        self.InstanceId = None
        self.IsOpenApi = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IsOpenApi = params.get("IsOpenApi")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceResponse(AbstractModel):
    """DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceInfo: 实例描述信息
        :type InstanceInfo: :class:`tencentcloud.cdwch.v20200915.models.InstanceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceInfo") is not None:
            self.InstanceInfo = InstanceInfo()
            self.InstanceInfo._deserialize(params.get("InstanceInfo"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceShardsRequest(AbstractModel):
    """DescribeInstanceShards请求参数结构体

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
        


class DescribeInstanceShardsResponse(AbstractModel):
    """DescribeInstanceShards返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceShardsList: 实例shard信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceShardsList: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceShardsList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceShardsList = params.get("InstanceShardsList")
        self.RequestId = params.get("RequestId")


class DescribeInstanceStateRequest(AbstractModel):
    """DescribeInstanceState请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例名称
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
        


class DescribeInstanceStateResponse(AbstractModel):
    """DescribeInstanceState返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceState: 集群状态，例如：Serving
        :type InstanceState: str
        :param FlowCreateTime: 集群操作创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowCreateTime: str
        :param FlowName: 集群操作名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowName: str
        :param FlowProgress: 集群操作进度
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowProgress: float
        :param InstanceStateDesc: 集群状态描述，例如：运行中
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStateDesc: str
        :param FlowMsg: 集群流程错误信息，例如：“创建失败，资源不足”
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceState = None
        self.FlowCreateTime = None
        self.FlowName = None
        self.FlowProgress = None
        self.InstanceStateDesc = None
        self.FlowMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceState = params.get("InstanceState")
        self.FlowCreateTime = params.get("FlowCreateTime")
        self.FlowName = params.get("FlowName")
        self.FlowProgress = params.get("FlowProgress")
        self.InstanceStateDesc = params.get("InstanceStateDesc")
        self.FlowMsg = params.get("FlowMsg")
        self.RequestId = params.get("RequestId")


class DescribeInstancesNewRequest(AbstractModel):
    """DescribeInstancesNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param SearchInstanceId: 搜索的集群id名称
        :type SearchInstanceId: str
        :param SearchInstanceName: 搜索的集群name
        :type SearchInstanceName: str
        :param Offset: 分页参数，第一页为0，第二页为10
        :type Offset: int
        :param Limit: 分页参数，分页步长，默认为10
        :type Limit: int
        :param SearchTags: 搜索标签列表
        :type SearchTags: list of SearchTags
        :param IsSimple: 信息详细与否
        :type IsSimple: bool
        """
        self.SearchInstanceId = None
        self.SearchInstanceName = None
        self.Offset = None
        self.Limit = None
        self.SearchTags = None
        self.IsSimple = None


    def _deserialize(self, params):
        self.SearchInstanceId = params.get("SearchInstanceId")
        self.SearchInstanceName = params.get("SearchInstanceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("SearchTags") is not None:
            self.SearchTags = []
            for item in params.get("SearchTags"):
                obj = SearchTags()
                obj._deserialize(item)
                self.SearchTags.append(obj)
        self.IsSimple = params.get("IsSimple")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesNewResponse(AbstractModel):
    """DescribeInstancesNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 实例总数
        :type TotalCount: int
        :param InstancesList: 实例数组
        :type InstancesList: list of InstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstancesList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstancesList") is not None:
            self.InstancesList = []
            for item in params.get("InstancesList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.InstancesList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSpecRequest(AbstractModel):
    """DescribeSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 地域信息，例如"ap-guangzhou-1"
        :type Zone: str
        :param PayMode: 计费类型，PREPAID 包年包月，POSTPAID_BY_HOUR 按量计费
        :type PayMode: str
        :param IsElastic: 是否弹性ck
        :type IsElastic: bool
        """
        self.Zone = None
        self.PayMode = None
        self.IsElastic = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.PayMode = params.get("PayMode")
        self.IsElastic = params.get("IsElastic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecResponse(AbstractModel):
    """DescribeSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param CommonSpec: zookeeper节点规格描述
        :type CommonSpec: list of ResourceSpec
        :param DataSpec: 数据节点规格描述
        :type DataSpec: list of ResourceSpec
        :param AttachCBSSpec: 云盘列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachCBSSpec: list of DiskSpec
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CommonSpec = None
        self.DataSpec = None
        self.AttachCBSSpec = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CommonSpec") is not None:
            self.CommonSpec = []
            for item in params.get("CommonSpec"):
                obj = ResourceSpec()
                obj._deserialize(item)
                self.CommonSpec.append(obj)
        if params.get("DataSpec") is not None:
            self.DataSpec = []
            for item in params.get("DataSpec"):
                obj = ResourceSpec()
                obj._deserialize(item)
                self.DataSpec.append(obj)
        if params.get("AttachCBSSpec") is not None:
            self.AttachCBSSpec = []
            for item in params.get("AttachCBSSpec"):
                obj = DiskSpec()
                obj._deserialize(item)
                self.AttachCBSSpec.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyInstanceRequest(AbstractModel):
    """DestroyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群id
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
        


class DestroyInstanceResponse(AbstractModel):
    """DestroyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowID: 作业id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowID: str
        :param InstanceID: 集群id
        :type InstanceID: str
        :param ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowID = None
        self.InstanceID = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowID = params.get("FlowID")
        self.InstanceID = params.get("InstanceID")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class DiskSpec(AbstractModel):
    """磁盘规格描述

    """

    def __init__(self):
        r"""
        :param DiskType: 磁盘类型，例如“CLOUD_SSD", "LOCAL_SSD"等
        :type DiskType: str
        :param DiskDesc: 磁盘类型说明，例如"云SSD", "本地SSD"等
        :type DiskDesc: str
        :param MinDiskSize: 磁盘最小规格大小，单位G
        :type MinDiskSize: int
        :param MaxDiskSize: 磁盘最大规格大小，单位G
        :type MaxDiskSize: int
        :param DiskCount: 磁盘数目
        :type DiskCount: int
        """
        self.DiskType = None
        self.DiskDesc = None
        self.MinDiskSize = None
        self.MaxDiskSize = None
        self.DiskCount = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskDesc = params.get("DiskDesc")
        self.MinDiskSize = params.get("MinDiskSize")
        self.MaxDiskSize = params.get("MaxDiskSize")
        self.DiskCount = params.get("DiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfigInfo(AbstractModel):
    """集群配置信息

    """

    def __init__(self):
        r"""
        :param ConfKey: 配置项名称
        :type ConfKey: str
        :param ConfValue: 配置项内容
        :type ConfValue: str
        :param DefaultValue: 默认值
        :type DefaultValue: str
        :param NeedRestart: 是否需要重启
        :type NeedRestart: bool
        :param Editable: 是否可编辑
        :type Editable: bool
        :param ConfDesc: 配置项解释
        :type ConfDesc: str
        :param FileName: 文件名称
        :type FileName: str
        :param ModifyRuleType: 规则名称类型
        :type ModifyRuleType: str
        :param ModifyRuleValue: 规则名称内容
        :type ModifyRuleValue: str
        :param Uin: 修改人的uin
        :type Uin: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.ConfKey = None
        self.ConfValue = None
        self.DefaultValue = None
        self.NeedRestart = None
        self.Editable = None
        self.ConfDesc = None
        self.FileName = None
        self.ModifyRuleType = None
        self.ModifyRuleValue = None
        self.Uin = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.ConfKey = params.get("ConfKey")
        self.ConfValue = params.get("ConfValue")
        self.DefaultValue = params.get("DefaultValue")
        self.NeedRestart = params.get("NeedRestart")
        self.Editable = params.get("Editable")
        self.ConfDesc = params.get("ConfDesc")
        self.FileName = params.get("FileName")
        self.ModifyRuleType = params.get("ModifyRuleType")
        self.ModifyRuleValue = params.get("ModifyRuleValue")
        self.Uin = params.get("Uin")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfigItem(AbstractModel):
    """KV配置

    """

    def __init__(self):
        r"""
        :param ConfKey: key
        :type ConfKey: str
        :param ConfValue: value
        :type ConfValue: str
        """
        self.ConfKey = None
        self.ConfValue = None


    def _deserialize(self, params):
        self.ConfKey = params.get("ConfKey")
        self.ConfValue = params.get("ConfValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """实例描述信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群实例ID, "cdw-xxxx" 字符串类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 集群实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param Status: 状态,
Init 创建中; Serving 运行中； 
Deleted已销毁；Deleting 销毁中；
Modify 集群变更中；
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Version: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param Region: 地域, ap-guangzhou
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Zone: 可用区， ap-guangzhou-3
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param VpcId: 私有网络名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子网名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param PayMode: 付费类型，"hour", "prepay"
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param MasterSummary: 数据节点描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterSummary: :class:`tencentcloud.cdwch.v20200915.models.NodesSummary`
        :param CommonSummary: zookeeper节点描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonSummary: :class:`tencentcloud.cdwch.v20200915.models.NodesSummary`
        :param HA: 高可用，“true" "false"
注意：此字段可能返回 null，表示取不到有效值。
        :type HA: str
        :param AccessInfo: 访问地址，例如 "10.0.0.1:9000"
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessInfo: str
        :param Id: 记录ID，数值型
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param RegionId: regionId, 表示地域
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param ZoneDesc: 可用区说明，例如 "广州二区"
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneDesc: str
        :param FlowMsg: 错误流程说明信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMsg: str
        :param StatusDesc: 状态描述，例如“运行中”等
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param RenewFlag: 自动续费标记
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: bool
        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Monitor: 监控信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Monitor: str
        :param HasClsTopic: 是否开通日志
注意：此字段可能返回 null，表示取不到有效值。
        :type HasClsTopic: bool
        :param ClsTopicId: 日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsTopicId: str
        :param ClsLogSetId: 日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClsLogSetId: str
        :param EnableXMLConfig: 是否支持xml配置管理
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableXMLConfig: int
        :param RegionDesc: 区域
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionDesc: str
        :param Eip: 弹性网卡地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Eip: str
        :param CosMoveFactor: 冷热分层系数
注意：此字段可能返回 null，表示取不到有效值。
        :type CosMoveFactor: int
        :param Kind: external/local/yunti
注意：此字段可能返回 null，表示取不到有效值。
        :type Kind: str
        :param IsElastic: 是否弹性ck
注意：此字段可能返回 null，表示取不到有效值。
        :type IsElastic: bool
        :param InstanceStateInfo: 集群详细状态
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStateInfo: :class:`tencentcloud.cdwch.v20200915.models.InstanceStateInfo`
        :param HAZk: ZK高可用
注意：此字段可能返回 null，表示取不到有效值。
        :type HAZk: bool
        :param MountDiskType: 挂载盘,默认0:没有类型；1:裸盘;2:lvm
注意：此字段可能返回 null，表示取不到有效值。
        :type MountDiskType: int
        :param CHProxyVip: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type CHProxyVip: str
        :param CosBucketName: cos buket的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type CosBucketName: str
        :param CanAttachCbs: 是否可以挂载云盘
注意：此字段可能返回 null，表示取不到有效值。
        :type CanAttachCbs: bool
        :param CanAttachCbsLvm: 是否可以挂载云盘阵列
注意：此字段可能返回 null，表示取不到有效值。
        :type CanAttachCbsLvm: bool
        :param CanAttachCos: 是否可以挂载cos
注意：此字段可能返回 null，表示取不到有效值。
        :type CanAttachCos: bool
        :param Components: 服务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Components: list of ServiceInfo
        :param UpgradeVersions: 可升级的内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeVersions: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Status = None
        self.Version = None
        self.Region = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.PayMode = None
        self.CreateTime = None
        self.ExpireTime = None
        self.MasterSummary = None
        self.CommonSummary = None
        self.HA = None
        self.AccessInfo = None
        self.Id = None
        self.RegionId = None
        self.ZoneDesc = None
        self.FlowMsg = None
        self.StatusDesc = None
        self.RenewFlag = None
        self.Tags = None
        self.Monitor = None
        self.HasClsTopic = None
        self.ClsTopicId = None
        self.ClsLogSetId = None
        self.EnableXMLConfig = None
        self.RegionDesc = None
        self.Eip = None
        self.CosMoveFactor = None
        self.Kind = None
        self.IsElastic = None
        self.InstanceStateInfo = None
        self.HAZk = None
        self.MountDiskType = None
        self.CHProxyVip = None
        self.CosBucketName = None
        self.CanAttachCbs = None
        self.CanAttachCbsLvm = None
        self.CanAttachCos = None
        self.Components = None
        self.UpgradeVersions = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Status = params.get("Status")
        self.Version = params.get("Version")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PayMode = params.get("PayMode")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        if params.get("MasterSummary") is not None:
            self.MasterSummary = NodesSummary()
            self.MasterSummary._deserialize(params.get("MasterSummary"))
        if params.get("CommonSummary") is not None:
            self.CommonSummary = NodesSummary()
            self.CommonSummary._deserialize(params.get("CommonSummary"))
        self.HA = params.get("HA")
        self.AccessInfo = params.get("AccessInfo")
        self.Id = params.get("Id")
        self.RegionId = params.get("RegionId")
        self.ZoneDesc = params.get("ZoneDesc")
        self.FlowMsg = params.get("FlowMsg")
        self.StatusDesc = params.get("StatusDesc")
        self.RenewFlag = params.get("RenewFlag")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Monitor = params.get("Monitor")
        self.HasClsTopic = params.get("HasClsTopic")
        self.ClsTopicId = params.get("ClsTopicId")
        self.ClsLogSetId = params.get("ClsLogSetId")
        self.EnableXMLConfig = params.get("EnableXMLConfig")
        self.RegionDesc = params.get("RegionDesc")
        self.Eip = params.get("Eip")
        self.CosMoveFactor = params.get("CosMoveFactor")
        self.Kind = params.get("Kind")
        self.IsElastic = params.get("IsElastic")
        if params.get("InstanceStateInfo") is not None:
            self.InstanceStateInfo = InstanceStateInfo()
            self.InstanceStateInfo._deserialize(params.get("InstanceStateInfo"))
        self.HAZk = params.get("HAZk")
        self.MountDiskType = params.get("MountDiskType")
        self.CHProxyVip = params.get("CHProxyVip")
        self.CosBucketName = params.get("CosBucketName")
        self.CanAttachCbs = params.get("CanAttachCbs")
        self.CanAttachCbsLvm = params.get("CanAttachCbsLvm")
        self.CanAttachCos = params.get("CanAttachCos")
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = ServiceInfo()
                obj._deserialize(item)
                self.Components.append(obj)
        self.UpgradeVersions = params.get("UpgradeVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStateInfo(AbstractModel):
    """集群状态抽象后的结构体

    """

    def __init__(self):
        r"""
        :param InstanceState: 集群状态，例如：Serving
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceState: str
        :param FlowCreateTime: 集群操作创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowCreateTime: str
        :param FlowName: 集群操作名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowName: str
        :param FlowProgress: 集群操作进度
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowProgress: int
        :param InstanceStateDesc: 集群状态描述，例如：运行中
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStateDesc: str
        :param FlowMsg: 集群流程错误信息，例如：“创建失败，资源不足”
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMsg: str
        :param ProcessName: 当前步骤的名称，例如：”购买资源中“
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessName: str
        :param RequestId: 请求id
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestId: str
        """
        self.InstanceState = None
        self.FlowCreateTime = None
        self.FlowName = None
        self.FlowProgress = None
        self.InstanceStateDesc = None
        self.FlowMsg = None
        self.ProcessName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceState = params.get("InstanceState")
        self.FlowCreateTime = params.get("FlowCreateTime")
        self.FlowName = params.get("FlowName")
        self.FlowProgress = params.get("FlowProgress")
        self.InstanceStateDesc = params.get("InstanceStateDesc")
        self.FlowMsg = params.get("FlowMsg")
        self.ProcessName = params.get("ProcessName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MapConfigItem(AbstractModel):
    """kv配置，多层级item

    """

    def __init__(self):
        r"""
        :param ConfKey: key
        :type ConfKey: str
        :param Items: 列表
        :type Items: list of InstanceConfigInfo
        """
        self.ConfKey = None
        self.Items = None


    def _deserialize(self, params):
        self.ConfKey = params.get("ConfKey")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceConfigInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterConfigsRequest(AbstractModel):
    """ModifyClusterConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群ID，例如cdwch-xxxx
        :type InstanceId: str
        :param ModifyConfContext: 配置文件修改信息
        :type ModifyConfContext: list of ConfigSubmitContext
        :param Remark: 修改原因
        :type Remark: str
        """
        self.InstanceId = None
        self.ModifyConfContext = None
        self.Remark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("ModifyConfContext") is not None:
            self.ModifyConfContext = []
            for item in params.get("ModifyConfContext"):
                obj = ConfigSubmitContext()
                obj._deserialize(item)
                self.ModifyConfContext.append(obj)
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterConfigsResponse(AbstractModel):
    """ModifyClusterConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程相关信息
        :type FlowId: int
        :param ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class ModifyInstanceKeyValConfigsRequest(AbstractModel):
    """ModifyInstanceKeyValConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param AddItems: 新增配置列表
        :type AddItems: list of InstanceConfigItem
        :param UpdateItems: 更新配置列表
        :type UpdateItems: list of InstanceConfigItem
        :param DeleteItems: 删除配置列表
        :type DeleteItems: :class:`tencentcloud.cdwch.v20200915.models.InstanceConfigItem`
        :param DelItems: 删除配置列表
        :type DelItems: list of InstanceConfigItem
        :param Remark: 备注
        :type Remark: str
        """
        self.InstanceId = None
        self.AddItems = None
        self.UpdateItems = None
        self.DeleteItems = None
        self.DelItems = None
        self.Remark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("AddItems") is not None:
            self.AddItems = []
            for item in params.get("AddItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self.AddItems.append(obj)
        if params.get("UpdateItems") is not None:
            self.UpdateItems = []
            for item in params.get("UpdateItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self.UpdateItems.append(obj)
        if params.get("DeleteItems") is not None:
            self.DeleteItems = InstanceConfigItem()
            self.DeleteItems._deserialize(params.get("DeleteItems"))
        if params.get("DelItems") is not None:
            self.DelItems = []
            for item in params.get("DelItems"):
                obj = InstanceConfigItem()
                obj._deserialize(item)
                self.DelItems.append(obj)
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceKeyValConfigsResponse(AbstractModel):
    """ModifyInstanceKeyValConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param FlowId: ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorMsg = None
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorMsg = params.get("ErrorMsg")
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyUserNewPrivilegeRequest(AbstractModel):
    """ModifyUserNewPrivilege请求参数结构体

    """


class ModifyUserNewPrivilegeResponse(AbstractModel):
    """ModifyUserNewPrivilege返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NodeSpec(AbstractModel):
    """创建集群时的规格

    """

    def __init__(self):
        r"""
        :param SpecName: 规格名称
        :type SpecName: str
        :param Count: 数量
        :type Count: int
        :param DiskSize: 云盘大小
        :type DiskSize: int
        """
        self.SpecName = None
        self.Count = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.SpecName = params.get("SpecName")
        self.Count = params.get("Count")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodesSummary(AbstractModel):
    """节点角色描述信息

    """

    def __init__(self):
        r"""
        :param Spec: 机型，如 S1
        :type Spec: str
        :param NodeSize: 节点数目
        :type NodeSize: int
        :param Core: cpu核数，单位个
        :type Core: int
        :param Memory: 内存大小，单位G
        :type Memory: int
        :param Disk: 磁盘大小，单位G
        :type Disk: int
        :param DiskType: 磁盘类型
        :type DiskType: str
        :param DiskDesc: 磁盘描述
        :type DiskDesc: str
        :param AttachCBSSpec: 挂载云盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachCBSSpec: :class:`tencentcloud.cdwch.v20200915.models.AttachCBSSpec`
        :param SubProductType: 子产品类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductType: str
        :param SpecCore: 规格对应的核数
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecCore: int
        :param SpecMemory: 规格对应的内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecMemory: int
        :param DiskCount: 磁盘的数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskCount: int
        :param MaxDiskSize: 磁盘的最大大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDiskSize: int
        :param Encrypt: 是否为加密云盘
注意：此字段可能返回 null，表示取不到有效值。
        :type Encrypt: int
        """
        self.Spec = None
        self.NodeSize = None
        self.Core = None
        self.Memory = None
        self.Disk = None
        self.DiskType = None
        self.DiskDesc = None
        self.AttachCBSSpec = None
        self.SubProductType = None
        self.SpecCore = None
        self.SpecMemory = None
        self.DiskCount = None
        self.MaxDiskSize = None
        self.Encrypt = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.NodeSize = params.get("NodeSize")
        self.Core = params.get("Core")
        self.Memory = params.get("Memory")
        self.Disk = params.get("Disk")
        self.DiskType = params.get("DiskType")
        self.DiskDesc = params.get("DiskDesc")
        if params.get("AttachCBSSpec") is not None:
            self.AttachCBSSpec = AttachCBSSpec()
            self.AttachCBSSpec._deserialize(params.get("AttachCBSSpec"))
        self.SubProductType = params.get("SubProductType")
        self.SpecCore = params.get("SpecCore")
        self.SpecMemory = params.get("SpecMemory")
        self.DiskCount = params.get("DiskCount")
        self.MaxDiskSize = params.get("MaxDiskSize")
        self.Encrypt = params.get("Encrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBackUpRequest(AbstractModel):
    """OpenBackUp请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 集群id
        :type InstanceId: str
        :param OperationType: OPEN 或者CLOSE
        :type OperationType: str
        :param CosBucketName: 桶名字
        :type CosBucketName: str
        """
        self.InstanceId = None
        self.OperationType = None
        self.CosBucketName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OperationType = params.get("OperationType")
        self.CosBucketName = params.get("CosBucketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBackUpResponse(AbstractModel):
    """OpenBackUp返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResizeDiskRequest(AbstractModel):
    """ResizeDisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例唯一ID
        :type InstanceId: str
        :param Type: 节点类型，DATA：clickhouse节点，COMMON：为zookeeper节点
        :type Type: str
        :param DiskSize: 磁盘扩容后容量，不能小于原有用量。clickhouse最小200，且为100的整数倍。 zk最小100，且为10的整数倍；
        :type DiskSize: int
        """
        self.InstanceId = None
        self.Type = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeDiskResponse(AbstractModel):
    """ResizeDisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.InstanceId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InstanceId = params.get("InstanceId")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class ResourceSpec(AbstractModel):
    """资源规格描述信息

    """

    def __init__(self):
        r"""
        :param Name: 规格名称，例如“SCH1"
        :type Name: str
        :param Cpu: cpu核数
        :type Cpu: int
        :param Mem: 内存大小，单位G
        :type Mem: int
        :param Type: 分类标记，STANDARD/BIGDATA/HIGHIO分别表示标准型/大数据型/高IO
        :type Type: str
        :param SystemDisk: 系统盘描述信息
        :type SystemDisk: :class:`tencentcloud.cdwch.v20200915.models.DiskSpec`
        :param DataDisk: 数据盘描述信息
        :type DataDisk: :class:`tencentcloud.cdwch.v20200915.models.DiskSpec`
        :param MaxNodeSize: 最大节点数目限制
        :type MaxNodeSize: int
        :param Available: 是否可用，false代表售罄
注意：此字段可能返回 null，表示取不到有效值。
        :type Available: bool
        :param ComputeSpecDesc: 规格描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ComputeSpecDesc: str
        :param DisplayName: 规格名
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param InstanceQuota: 库存数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceQuota: int
        """
        self.Name = None
        self.Cpu = None
        self.Mem = None
        self.Type = None
        self.SystemDisk = None
        self.DataDisk = None
        self.MaxNodeSize = None
        self.Available = None
        self.ComputeSpecDesc = None
        self.DisplayName = None
        self.InstanceQuota = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.Type = params.get("Type")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = DiskSpec()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisk") is not None:
            self.DataDisk = DiskSpec()
            self.DataDisk._deserialize(params.get("DataDisk"))
        self.MaxNodeSize = params.get("MaxNodeSize")
        self.Available = params.get("Available")
        self.ComputeSpecDesc = params.get("ComputeSpecDesc")
        self.DisplayName = params.get("DisplayName")
        self.InstanceQuota = params.get("InstanceQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例唯一ID
        :type InstanceId: str
        :param Type: 节点类型，DATA：clickhouse节点，COMMON：为zookeeper节点
        :type Type: str
        :param NodeCount: 调整clickhouse节点数量
        :type NodeCount: int
        :param ScaleOutCluster: v_cluster分组，	
新增扩容节点将加入到已选择的v_cluster分组中，提交同步VIP生效.
        :type ScaleOutCluster: str
        :param UserSubnetIPNum: 子网剩余ip数量，用于判断当前实例子网剩余ip数是否能扩容。需要根据实际填写
        :type UserSubnetIPNum: int
        :param ScaleOutNodeIp: 同步元数据节点IP （uip），扩容的时候必填
        :type ScaleOutNodeIp: str
        :param ReduceShardInfo: 缩容节点shard的节点IP （uip），其中ha集群需要主副节点ip都传入以逗号分隔，缩容的时候必填
        :type ReduceShardInfo: list of str
        """
        self.InstanceId = None
        self.Type = None
        self.NodeCount = None
        self.ScaleOutCluster = None
        self.UserSubnetIPNum = None
        self.ScaleOutNodeIp = None
        self.ReduceShardInfo = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.NodeCount = params.get("NodeCount")
        self.ScaleOutCluster = params.get("ScaleOutCluster")
        self.UserSubnetIPNum = params.get("UserSubnetIPNum")
        self.ScaleOutNodeIp = params.get("ScaleOutNodeIp")
        self.ReduceShardInfo = params.get("ReduceShardInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.InstanceId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InstanceId = params.get("InstanceId")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class ScaleUpInstanceRequest(AbstractModel):
    """ScaleUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例唯一ID
        :type InstanceId: str
        :param Type: 节点类型，DATA：clickhouse节点，COMMON：为zookeeper节点
        :type Type: str
        :param SpecName: clickhouse节点规格。
        :type SpecName: str
        :param ScaleUpEnableRolling: 是否滚动重启，false为不滚动重启，true为滚动重启
        :type ScaleUpEnableRolling: bool
        """
        self.InstanceId = None
        self.Type = None
        self.SpecName = None
        self.ScaleUpEnableRolling = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.SpecName = params.get("SpecName")
        self.ScaleUpEnableRolling = params.get("ScaleUpEnableRolling")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpInstanceResponse(AbstractModel):
    """ScaleUpInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.InstanceId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InstanceId = params.get("InstanceId")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class ScheduleStrategy(AbstractModel):
    """策略详情

    """

    def __init__(self):
        r"""
        :param CosBucketName: 备份桶列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CosBucketName: str
        :param RetainDays: 备份保留天数
        :type RetainDays: int
        :param WeekDays: 备份的天
        :type WeekDays: str
        :param ExecuteHour: 备份小时
        :type ExecuteHour: int
        :param ScheduleId: 策略id
        :type ScheduleId: int
        :param NextBackupTime: 下次备份时间
注意：此字段可能返回 null，表示取不到有效值。
        :type NextBackupTime: str
        """
        self.CosBucketName = None
        self.RetainDays = None
        self.WeekDays = None
        self.ExecuteHour = None
        self.ScheduleId = None
        self.NextBackupTime = None


    def _deserialize(self, params):
        self.CosBucketName = params.get("CosBucketName")
        self.RetainDays = params.get("RetainDays")
        self.WeekDays = params.get("WeekDays")
        self.ExecuteHour = params.get("ExecuteHour")
        self.ScheduleId = params.get("ScheduleId")
        self.NextBackupTime = params.get("NextBackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchTags(AbstractModel):
    """列表页搜索的标记列表

    """

    def __init__(self):
        r"""
        :param TagKey: 标签的键
        :type TagKey: str
        :param TagValue: 标签的值
        :type TagValue: str
        :param AllValue: 1表示只输入标签的键，没有输入值；0表示输入键时且输入值
        :type AllValue: int
        """
        self.TagKey = None
        self.TagValue = None
        self.AllValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.AllValue = params.get("AllValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceInfo(AbstractModel):
    """服务详细信息描述。

    """

    def __init__(self):
        r"""
        :param Name: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Version: 服务的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self.Name = None
        self.Version = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签描述

    """

    def __init__(self):
        r"""
        :param TagKey: 标签的键
        :type TagKey: str
        :param TagValue: 标签的值
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
        