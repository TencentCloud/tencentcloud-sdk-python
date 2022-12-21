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


class BackupTableContent(AbstractModel):
    """备份表信息

    """

    def __init__(self):
        r"""
        :param Database: 数据库
        :type Database: str
        :param Table: 表
        :type Table: str
        :param TotalBytes: 表总字节数
        :type TotalBytes: int
        :param VCluster: 虚拟cluster
        :type VCluster: str
        :param Ips: 表ip
        :type Ips: str
        """
        self.Database = None
        self.Table = None
        self.TotalBytes = None
        self.VCluster = None
        self.Ips = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.TotalBytes = params.get("TotalBytes")
        self.VCluster = params.get("VCluster")
        self.Ips = params.get("Ips")
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


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体

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
        """
        self.Spec = None
        self.NodeSize = None
        self.Core = None
        self.Memory = None
        self.Disk = None
        self.DiskType = None
        self.DiskDesc = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.NodeSize = params.get("NodeSize")
        self.Core = params.get("Core")
        self.Memory = params.get("Memory")
        self.Disk = params.get("Disk")
        self.DiskType = params.get("DiskType")
        self.DiskDesc = params.get("DiskDesc")
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
        