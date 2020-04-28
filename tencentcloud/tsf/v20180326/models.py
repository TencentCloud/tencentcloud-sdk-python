# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AddClusterInstancesRequest(AbstractModel):
    """AddClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdList: 云主机ID列表
        :type InstanceIdList: list of str
        :param OsName: 操作系统名称
        :type OsName: str
        :param ImageId: 操作系统镜像ID
        :type ImageId: str
        :param Password: 重装系统密码设置
        :type Password: str
        :param KeyId: 重装系统，关联密钥设置
        :type KeyId: str
        :param SgId: 安全组设置
        :type SgId: str
        :param InstanceImportMode: 云主机导入方式，虚拟机集群必填，容器集群不填写此字段，R：重装TSF系统镜像，M：手动安装agent
        :type InstanceImportMode: str
        """
        self.ClusterId = None
        self.InstanceIdList = None
        self.OsName = None
        self.ImageId = None
        self.Password = None
        self.KeyId = None
        self.SgId = None
        self.InstanceImportMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        self.OsName = params.get("OsName")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        self.KeyId = params.get("KeyId")
        self.SgId = params.get("SgId")
        self.InstanceImportMode = params.get("InstanceImportMode")


class AddClusterInstancesResponse(AbstractModel):
    """AddClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 添加云主机的返回列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.AddInstanceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AddInstanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class AddInstanceResult(AbstractModel):
    """添加实例到集群的结果

    """

    def __init__(self):
        """
        :param FailedInstanceIds: 添加集群失败的节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedInstanceIds: list of str
        :param SuccInstanceIds: 添加集群成功的节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccInstanceIds: list of str
        :param TimeoutInstanceIds: 添加集群超时的节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutInstanceIds: list of str
        """
        self.FailedInstanceIds = None
        self.SuccInstanceIds = None
        self.TimeoutInstanceIds = None


    def _deserialize(self, params):
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.TimeoutInstanceIds = params.get("TimeoutInstanceIds")


class AddInstancesRequest(AbstractModel):
    """AddInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdList: 云主机ID列表
        :type InstanceIdList: list of str
        :param OsName: 操作系统名称
        :type OsName: str
        :param ImageId: 操作系统镜像ID
        :type ImageId: str
        :param Password: 重装系统密码设置
        :type Password: str
        :param KeyId: 重装系统，关联密钥设置
        :type KeyId: str
        :param SgId: 安全组设置
        :type SgId: str
        :param InstanceImportMode: 云主机导入方式，虚拟机集群必填，容器集群不填写此字段，R：重装TSF系统镜像，M：手动安装agent
        :type InstanceImportMode: str
        """
        self.ClusterId = None
        self.InstanceIdList = None
        self.OsName = None
        self.ImageId = None
        self.Password = None
        self.KeyId = None
        self.SgId = None
        self.InstanceImportMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        self.OsName = params.get("OsName")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        self.KeyId = params.get("KeyId")
        self.SgId = params.get("SgId")
        self.InstanceImportMode = params.get("InstanceImportMode")


class AddInstancesResponse(AbstractModel):
    """AddInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 添加云主机是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ApplicationAttribute(AbstractModel):
    """应用列表其它字段

    """

    def __init__(self):
        """
        :param InstanceCount: 总实例个数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param RunInstanceCount: 运行实例个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RunInstanceCount: int
        :param GroupCount: 应用下部署组个数
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupCount: int
        """
        self.InstanceCount = None
        self.RunInstanceCount = None
        self.GroupCount = None


    def _deserialize(self, params):
        self.InstanceCount = params.get("InstanceCount")
        self.RunInstanceCount = params.get("RunInstanceCount")
        self.GroupCount = params.get("GroupCount")


class ApplicationForPage(AbstractModel):
    """分页的应用描述信息字段

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ApplicationDesc: 应用描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationDesc: str
        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param MicroserviceType: 微服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param ProgLang: 编程语言
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgLang: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ApplicationResourceType: 应用资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationResourceType: str
        :param ApplicationRuntimeType: 应用runtime类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationRuntimeType: str
        :param ApigatewayServiceId: Apigateway的serviceId
注意：此字段可能返回 null，表示取不到有效值。
        :type ApigatewayServiceId: str
        """
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationDesc = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ProgLang = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ApplicationResourceType = None
        self.ApplicationRuntimeType = None
        self.ApigatewayServiceId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationDesc = params.get("ApplicationDesc")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ProgLang = params.get("ProgLang")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ApplicationResourceType = params.get("ApplicationResourceType")
        self.ApplicationRuntimeType = params.get("ApplicationRuntimeType")
        self.ApigatewayServiceId = params.get("ApigatewayServiceId")


class Cluster(AbstractModel):
    """集群

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ClusterDesc: 集群描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterDesc: str
        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param VpcId: 集群所属私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param ClusterStatus: 集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStatus: str
        :param ClusterCIDR: 集群CIDR
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterCIDR: str
        :param ClusterTotalCpu: 集群总CPU，单位: 核
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterTotalCpu: float
        :param ClusterTotalMem: 集群总内存，单位: G
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterTotalMem: float
        :param ClusterUsedCpu: 集群已使用CPU，单位: 核
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterUsedCpu: float
        :param ClusterUsedMem: 集群已使用内存，单位: G
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterUsedMem: float
        :param InstanceCount: 集群机器实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param RunInstanceCount: 集群可用的机器实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RunInstanceCount: int
        :param NormalInstanceCount: 集群正常状态的机器实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalInstanceCount: int
        :param DeleteFlag: 删除标记：true：可以删除；false：不可删除
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteFlag: bool
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param TsfRegionId: 集群所属TSF地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TsfRegionId: str
        :param TsfRegionName: 集群所属TSF地域名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TsfRegionName: str
        :param TsfZoneId: 集群所属TSF可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TsfZoneId: str
        :param TsfZoneName: 集群所属TSF可用区名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TsfZoneName: str
        :param DeleteFlagReason: 集群不可删除的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteFlagReason: str
        :param ClusterLimitCpu: 集群最大CPU限制，单位：核
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterLimitCpu: float
        :param ClusterLimitMem: 集群最大内存限制，单位：G
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterLimitMem: float
        :param RunServiceInstanceCount: 集群可用的服务实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RunServiceInstanceCount: int
        :param SubnetId: 集群所属子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param OperationInfo: 返回给前端的控制信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationInfo: :class:`tencentcloud.tsf.v20180326.models.OperationInfo`
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.ClusterType = None
        self.VpcId = None
        self.ClusterStatus = None
        self.ClusterCIDR = None
        self.ClusterTotalCpu = None
        self.ClusterTotalMem = None
        self.ClusterUsedCpu = None
        self.ClusterUsedMem = None
        self.InstanceCount = None
        self.RunInstanceCount = None
        self.NormalInstanceCount = None
        self.DeleteFlag = None
        self.CreateTime = None
        self.UpdateTime = None
        self.TsfRegionId = None
        self.TsfRegionName = None
        self.TsfZoneId = None
        self.TsfZoneName = None
        self.DeleteFlagReason = None
        self.ClusterLimitCpu = None
        self.ClusterLimitMem = None
        self.RunServiceInstanceCount = None
        self.SubnetId = None
        self.OperationInfo = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.ClusterType = params.get("ClusterType")
        self.VpcId = params.get("VpcId")
        self.ClusterStatus = params.get("ClusterStatus")
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.ClusterTotalCpu = params.get("ClusterTotalCpu")
        self.ClusterTotalMem = params.get("ClusterTotalMem")
        self.ClusterUsedCpu = params.get("ClusterUsedCpu")
        self.ClusterUsedMem = params.get("ClusterUsedMem")
        self.InstanceCount = params.get("InstanceCount")
        self.RunInstanceCount = params.get("RunInstanceCount")
        self.NormalInstanceCount = params.get("NormalInstanceCount")
        self.DeleteFlag = params.get("DeleteFlag")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TsfRegionId = params.get("TsfRegionId")
        self.TsfRegionName = params.get("TsfRegionName")
        self.TsfZoneId = params.get("TsfZoneId")
        self.TsfZoneName = params.get("TsfZoneName")
        self.DeleteFlagReason = params.get("DeleteFlagReason")
        self.ClusterLimitCpu = params.get("ClusterLimitCpu")
        self.ClusterLimitMem = params.get("ClusterLimitMem")
        self.RunServiceInstanceCount = params.get("RunServiceInstanceCount")
        self.SubnetId = params.get("SubnetId")
        if params.get("OperationInfo") is not None:
            self.OperationInfo = OperationInfo()
            self.OperationInfo._deserialize(params.get("OperationInfo"))


class Config(AbstractModel):
    """配置项

    """

    def __init__(self):
        """
        :param ConfigId: 配置项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param ConfigName: 配置项名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigName: str
        :param ConfigVersion: 配置项版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param ConfigVersionDesc: 配置项版本描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigVersionDesc: str
        :param ConfigValue: 配置项值
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigValue: str
        :param ConfigType: 配置项类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigType: str
        :param CreationTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param DeleteFlag: 删除标识，true：可以删除；false：不可删除
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteFlag: bool
        :param LastUpdateTime: 最后更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param ConfigVersionCount: 配置项版本数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigVersionCount: int
        """
        self.ConfigId = None
        self.ConfigName = None
        self.ConfigVersion = None
        self.ConfigVersionDesc = None
        self.ConfigValue = None
        self.ConfigType = None
        self.CreationTime = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.DeleteFlag = None
        self.LastUpdateTime = None
        self.ConfigVersionCount = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ConfigVersionDesc = params.get("ConfigVersionDesc")
        self.ConfigValue = params.get("ConfigValue")
        self.ConfigType = params.get("ConfigType")
        self.CreationTime = params.get("CreationTime")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.DeleteFlag = params.get("DeleteFlag")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.ConfigVersionCount = params.get("ConfigVersionCount")


class ConfigRelease(AbstractModel):
    """配置项发布信息

    """

    def __init__(self):
        """
        :param ConfigReleaseId: 配置项发布ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigReleaseId: str
        :param ConfigId: 配置项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param ConfigName: 配置项名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigName: str
        :param ConfigVersion: 配置项版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param ReleaseTime: 发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ReleaseDesc: 发布描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseDesc: str
        """
        self.ConfigReleaseId = None
        self.ConfigId = None
        self.ConfigName = None
        self.ConfigVersion = None
        self.ReleaseTime = None
        self.GroupId = None
        self.GroupName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.ClusterId = None
        self.ClusterName = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigReleaseId = params.get("ConfigReleaseId")
        self.ConfigId = params.get("ConfigId")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ReleaseTime = params.get("ReleaseTime")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ReleaseDesc = params.get("ReleaseDesc")


class ConfigReleaseLog(AbstractModel):
    """配置项发布日志

    """

    def __init__(self):
        """
        :param ConfigReleaseLogId: 配置项发布日志ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigReleaseLogId: str
        :param ConfigId: 配置项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param ConfigName: 配置项名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigName: str
        :param ConfigVersion: 配置项版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ReleaseTime: 发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param ReleaseDesc: 发布描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseDesc: str
        :param ReleaseStatus: 发布状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseStatus: str
        :param LastConfigId: 上次发布的配置项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LastConfigId: str
        :param LastConfigName: 上次发布的配置项名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LastConfigName: str
        :param LastConfigVersion: 上次发布的配置项版本
注意：此字段可能返回 null，表示取不到有效值。
        :type LastConfigVersion: str
        :param RollbackFlag: 回滚标识
注意：此字段可能返回 null，表示取不到有效值。
        :type RollbackFlag: bool
        """
        self.ConfigReleaseLogId = None
        self.ConfigId = None
        self.ConfigName = None
        self.ConfigVersion = None
        self.GroupId = None
        self.GroupName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.ClusterId = None
        self.ClusterName = None
        self.ReleaseTime = None
        self.ReleaseDesc = None
        self.ReleaseStatus = None
        self.LastConfigId = None
        self.LastConfigName = None
        self.LastConfigVersion = None
        self.RollbackFlag = None


    def _deserialize(self, params):
        self.ConfigReleaseLogId = params.get("ConfigReleaseLogId")
        self.ConfigId = params.get("ConfigId")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ReleaseTime = params.get("ReleaseTime")
        self.ReleaseDesc = params.get("ReleaseDesc")
        self.ReleaseStatus = params.get("ReleaseStatus")
        self.LastConfigId = params.get("LastConfigId")
        self.LastConfigName = params.get("LastConfigName")
        self.LastConfigVersion = params.get("LastConfigVersion")
        self.RollbackFlag = params.get("RollbackFlag")


class ContainGroup(AbstractModel):
    """部署组列表（应用下钻界面的）

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Server: 镜像server
注意：此字段可能返回 null，表示取不到有效值。
        :type Server: str
        :param RepoName: 镜像名，如/tsf/nginx
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoName: str
        :param TagName: 镜像版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param CpuRequest: 初始分配的 CPU 核数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuRequest: str
        :param CpuLimit: 最大分配的 CPU 核数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuLimit: str
        :param MemRequest: 初始分配的内存 MiB 数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。
        :type MemRequest: str
        :param MemLimit: 最大分配的内存 MiB 数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。
        :type MemLimit: str
        """
        self.GroupId = None
        self.GroupName = None
        self.CreateTime = None
        self.Server = None
        self.RepoName = None
        self.TagName = None
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.CpuRequest = None
        self.CpuLimit = None
        self.MemRequest = None
        self.MemLimit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.CreateTime = params.get("CreateTime")
        self.Server = params.get("Server")
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.CpuRequest = params.get("CpuRequest")
        self.CpuLimit = params.get("CpuLimit")
        self.MemRequest = params.get("MemRequest")
        self.MemLimit = params.get("MemLimit")


class ContainGroupResult(AbstractModel):
    """部署组列表（应用下钻）

    """

    def __init__(self):
        """
        :param Content: 部署组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of ContainGroup
        :param TotalCount: 总记录数
        :type TotalCount: int
        """
        self.Content = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ContainGroup()
                obj._deserialize(item)
                self.Content.append(obj)
        self.TotalCount = params.get("TotalCount")


class ContainerGroupDetail(AbstractModel):
    """容器部署组详情

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param InstanceNum: 实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceNum: int
        :param CurrentNum: 已启动实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentNum: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Server: 镜像server
注意：此字段可能返回 null，表示取不到有效值。
        :type Server: str
        :param Reponame: 镜像名，如/tsf/nginx
注意：此字段可能返回 null，表示取不到有效值。
        :type Reponame: str
        :param TagName: 镜像版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param LbIp: 负载均衡ip
注意：此字段可能返回 null，表示取不到有效值。
        :type LbIp: str
        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param ClusterIp: Service ip
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIp: str
        :param NodePort: NodePort端口，只有公网和NodePort访问方式才有值
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePort: int
        :param CpuLimit: 最大分配的 CPU 核数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuLimit: str
        :param MemLimit: 最大分配的内存 MiB 数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。
        :type MemLimit: str
        :param AccessType: 0:公网 1:集群内访问 2：NodePort
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessType: int
        :param UpdateType: 更新方式：0:快速更新 1:滚动更新
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateType: int
        :param UpdateIvl: 更新间隔,单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateIvl: int
        :param ProtocolPorts: 端口数组对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolPorts: list of ProtocolPort
        :param Envs: 环境变量数组对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Envs: list of Env
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param Message: pod错误信息描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Status: 部署组状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param MicroserviceType: 服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param CpuRequest: 初始分配的 CPU 核数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuRequest: str
        :param MemRequest: 初始分配的内存 MiB 数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。
        :type MemRequest: str
        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param GroupResourceType: 部署组资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupResourceType: str
        :param InstanceCount: 部署组实例个数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param UpdatedTime: 部署组更新时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: int
        """
        self.GroupId = None
        self.GroupName = None
        self.InstanceNum = None
        self.CurrentNum = None
        self.CreateTime = None
        self.Server = None
        self.Reponame = None
        self.TagName = None
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.ApplicationId = None
        self.LbIp = None
        self.ApplicationType = None
        self.ClusterIp = None
        self.NodePort = None
        self.CpuLimit = None
        self.MemLimit = None
        self.AccessType = None
        self.UpdateType = None
        self.UpdateIvl = None
        self.ProtocolPorts = None
        self.Envs = None
        self.ApplicationName = None
        self.Message = None
        self.Status = None
        self.MicroserviceType = None
        self.CpuRequest = None
        self.MemRequest = None
        self.SubnetId = None
        self.GroupResourceType = None
        self.InstanceCount = None
        self.UpdatedTime = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.InstanceNum = params.get("InstanceNum")
        self.CurrentNum = params.get("CurrentNum")
        self.CreateTime = params.get("CreateTime")
        self.Server = params.get("Server")
        self.Reponame = params.get("Reponame")
        self.TagName = params.get("TagName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.ApplicationId = params.get("ApplicationId")
        self.LbIp = params.get("LbIp")
        self.ApplicationType = params.get("ApplicationType")
        self.ClusterIp = params.get("ClusterIp")
        self.NodePort = params.get("NodePort")
        self.CpuLimit = params.get("CpuLimit")
        self.MemLimit = params.get("MemLimit")
        self.AccessType = params.get("AccessType")
        self.UpdateType = params.get("UpdateType")
        self.UpdateIvl = params.get("UpdateIvl")
        if params.get("ProtocolPorts") is not None:
            self.ProtocolPorts = []
            for item in params.get("ProtocolPorts"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPorts.append(obj)
        if params.get("Envs") is not None:
            self.Envs = []
            for item in params.get("Envs"):
                obj = Env()
                obj._deserialize(item)
                self.Envs.append(obj)
        self.ApplicationName = params.get("ApplicationName")
        self.Message = params.get("Message")
        self.Status = params.get("Status")
        self.MicroserviceType = params.get("MicroserviceType")
        self.CpuRequest = params.get("CpuRequest")
        self.MemRequest = params.get("MemRequest")
        self.SubnetId = params.get("SubnetId")
        self.GroupResourceType = params.get("GroupResourceType")
        self.InstanceCount = params.get("InstanceCount")
        self.UpdatedTime = params.get("UpdatedTime")


class CosCredentials(AbstractModel):
    """cos临时帐号信息

    """

    def __init__(self):
        """
        :param SessionToken: 会话Token
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionToken: str
        :param TmpAppId: 临时应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpAppId: str
        :param TmpSecretId: 临时调用者身份ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretId: str
        :param TmpSecretKey: 临时密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretKey: str
        :param ExpiredTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: int
        :param Domain: 所在域
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        """
        self.SessionToken = None
        self.TmpAppId = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.ExpiredTime = None
        self.Domain = None


    def _deserialize(self, params):
        self.SessionToken = params.get("SessionToken")
        self.TmpAppId = params.get("TmpAppId")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.ExpiredTime = params.get("ExpiredTime")
        self.Domain = params.get("Domain")


class CosDownloadInfo(AbstractModel):
    """Cos下载所需信息

    """

    def __init__(self):
        """
        :param Bucket: 桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Path: 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Credentials: 鉴权信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Credentials: :class:`tencentcloud.tsf.v20180326.models.CosCredentials`
        """
        self.Bucket = None
        self.Region = None
        self.Path = None
        self.Credentials = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Path = params.get("Path")
        if params.get("Credentials") is not None:
            self.Credentials = CosCredentials()
            self.Credentials._deserialize(params.get("Credentials"))


class CosUploadInfo(AbstractModel):
    """cos上传所需信息

    """

    def __init__(self):
        """
        :param PkgId: 程序包ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param Bucket: 桶
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param Region: 目标地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Path: 存储路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Credentials: 鉴权信息
        :type Credentials: :class:`tencentcloud.tsf.v20180326.models.CosCredentials`
        """
        self.PkgId = None
        self.Bucket = None
        self.Region = None
        self.Path = None
        self.Credentials = None


    def _deserialize(self, params):
        self.PkgId = params.get("PkgId")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Path = params.get("Path")
        if params.get("Credentials") is not None:
            self.Credentials = CosCredentials()
            self.Credentials._deserialize(params.get("Credentials"))


class CreateApplicationRequest(AbstractModel):
    """CreateApplication请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationName: 应用名称
        :type ApplicationName: str
        :param ApplicationType: 应用类型，V：虚拟机应用；C：容器应用；S：serverless应用
        :type ApplicationType: str
        :param MicroserviceType: 应用微服务类型，M：service mesh应用；N：普通应用；G：网关应用
        :type MicroserviceType: str
        :param ApplicationDesc: 应用描述
        :type ApplicationDesc: str
        :param ApplicationLogConfig: 应用日志配置项，废弃参数
        :type ApplicationLogConfig: str
        :param ApplicationResourceType: 应用资源类型，废弃参数
        :type ApplicationResourceType: str
        :param ApplicationRuntimeType: 应用runtime类型
        :type ApplicationRuntimeType: str
        """
        self.ApplicationName = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ApplicationDesc = None
        self.ApplicationLogConfig = None
        self.ApplicationResourceType = None
        self.ApplicationRuntimeType = None


    def _deserialize(self, params):
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationDesc = params.get("ApplicationDesc")
        self.ApplicationLogConfig = params.get("ApplicationLogConfig")
        self.ApplicationResourceType = params.get("ApplicationResourceType")
        self.ApplicationRuntimeType = params.get("ApplicationRuntimeType")


class CreateApplicationResponse(AbstractModel):
    """CreateApplication返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param ClusterType: 集群类型
        :type ClusterType: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param ClusterCIDR: 分配给集群容器和服务IP的CIDR
        :type ClusterCIDR: str
        :param ClusterDesc: 集群备注
        :type ClusterDesc: str
        :param TsfRegionId: 集群所属TSF地域
        :type TsfRegionId: str
        :param TsfZoneId: 集群所属TSF可用区
        :type TsfZoneId: str
        :param SubnetId: 私有网络子网ID
        :type SubnetId: str
        """
        self.ClusterName = None
        self.ClusterType = None
        self.VpcId = None
        self.ClusterCIDR = None
        self.ClusterDesc = None
        self.TsfRegionId = None
        self.TsfZoneId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.ClusterType = params.get("ClusterType")
        self.VpcId = params.get("VpcId")
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.ClusterDesc = params.get("ClusterDesc")
        self.TsfRegionId = params.get("TsfRegionId")
        self.TsfZoneId = params.get("TsfZoneId")
        self.SubnetId = params.get("SubnetId")


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 集群ID
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateConfigRequest(AbstractModel):
    """CreateConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigName: 配置项名称
        :type ConfigName: str
        :param ConfigVersion: 配置项版本
        :type ConfigVersion: str
        :param ConfigValue: 配置项值
        :type ConfigValue: str
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param ConfigVersionDesc: 配置项版本描述
        :type ConfigVersionDesc: str
        :param ConfigType: 配置项值类型
        :type ConfigType: str
        :param EncodeWithBase64: Base64编码的配置项
        :type EncodeWithBase64: bool
        """
        self.ConfigName = None
        self.ConfigVersion = None
        self.ConfigValue = None
        self.ApplicationId = None
        self.ConfigVersionDesc = None
        self.ConfigType = None
        self.EncodeWithBase64 = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ConfigValue = params.get("ConfigValue")
        self.ApplicationId = params.get("ApplicationId")
        self.ConfigVersionDesc = params.get("ConfigVersionDesc")
        self.ConfigType = params.get("ConfigType")
        self.EncodeWithBase64 = params.get("EncodeWithBase64")


class CreateConfigResponse(AbstractModel):
    """CreateConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：创建成功；false：创建失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateContainGroupRequest(AbstractModel):
    """CreateContainGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 分组所属应用ID
        :type ApplicationId: str
        :param NamespaceId: 分组所属命名空间ID
        :type NamespaceId: str
        :param GroupName: 分组名称字段，长度1~60，字母或下划线开头，可包含字母数字下划线
        :type GroupName: str
        :param InstanceNum: 实例数量
        :type InstanceNum: int
        :param AccessType: 0:公网 1:集群内访问 2：NodePort
        :type AccessType: int
        :param ProtocolPorts: 数组对象，见下方定义
        :type ProtocolPorts: list of ProtocolPort
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param CpuLimit: 最大分配 CPU 核数，对应 K8S limit
        :type CpuLimit: str
        :param MemLimit: 最大分配内存 MiB 数，对应 K8S limit
        :type MemLimit: str
        :param GroupComment: 分组备注字段，长度应不大于200字符
        :type GroupComment: str
        :param UpdateType: 更新方式：0:快速更新 1:滚动更新
        :type UpdateType: int
        :param UpdateIvl: 滚动更新必填，更新间隔
        :type UpdateIvl: int
        :param CpuRequest: 初始分配的 CPU 核数，对应 K8S request
        :type CpuRequest: str
        :param MemRequest: 初始分配的内存 MiB 数，对应 K8S request
        :type MemRequest: str
        :param GroupResourceType: 部署组资源类型
        :type GroupResourceType: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param AgentCpuRequest: agent 容器分配的 CPU 核数，对应 K8S 的 request
        :type AgentCpuRequest: str
        :param AgentCpuLimit: agent 容器最大的 CPU 核数，对应 K8S 的 limit
        :type AgentCpuLimit: str
        :param AgentMemRequest: agent 容器分配的内存 MiB 数，对应 K8S 的 request
        :type AgentMemRequest: str
        :param AgentMemLimit: agent 容器最大的内存 MiB 数，对应 K8S 的 limit
        :type AgentMemLimit: str
        :param IstioCpuRequest: istioproxy 容器分配的 CPU 核数，对应 K8S 的 request
        :type IstioCpuRequest: str
        :param IstioCpuLimit: istioproxy 容器最大的 CPU 核数，对应 K8S 的 limit
        :type IstioCpuLimit: str
        :param IstioMemRequest: istioproxy 容器分配的内存 MiB 数，对应 K8S 的 request
        :type IstioMemRequest: str
        :param IstioMemLimit: istioproxy 容器最大的内存 MiB 数，对应 K8S 的 limit
        :type IstioMemLimit: str
        """
        self.ApplicationId = None
        self.NamespaceId = None
        self.GroupName = None
        self.InstanceNum = None
        self.AccessType = None
        self.ProtocolPorts = None
        self.ClusterId = None
        self.CpuLimit = None
        self.MemLimit = None
        self.GroupComment = None
        self.UpdateType = None
        self.UpdateIvl = None
        self.CpuRequest = None
        self.MemRequest = None
        self.GroupResourceType = None
        self.SubnetId = None
        self.AgentCpuRequest = None
        self.AgentCpuLimit = None
        self.AgentMemRequest = None
        self.AgentMemLimit = None
        self.IstioCpuRequest = None
        self.IstioCpuLimit = None
        self.IstioMemRequest = None
        self.IstioMemLimit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupName = params.get("GroupName")
        self.InstanceNum = params.get("InstanceNum")
        self.AccessType = params.get("AccessType")
        if params.get("ProtocolPorts") is not None:
            self.ProtocolPorts = []
            for item in params.get("ProtocolPorts"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPorts.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.CpuLimit = params.get("CpuLimit")
        self.MemLimit = params.get("MemLimit")
        self.GroupComment = params.get("GroupComment")
        self.UpdateType = params.get("UpdateType")
        self.UpdateIvl = params.get("UpdateIvl")
        self.CpuRequest = params.get("CpuRequest")
        self.MemRequest = params.get("MemRequest")
        self.GroupResourceType = params.get("GroupResourceType")
        self.SubnetId = params.get("SubnetId")
        self.AgentCpuRequest = params.get("AgentCpuRequest")
        self.AgentCpuLimit = params.get("AgentCpuLimit")
        self.AgentMemRequest = params.get("AgentMemRequest")
        self.AgentMemLimit = params.get("AgentMemLimit")
        self.IstioCpuRequest = params.get("IstioCpuRequest")
        self.IstioCpuLimit = params.get("IstioCpuLimit")
        self.IstioMemRequest = params.get("IstioMemRequest")
        self.IstioMemLimit = params.get("IstioMemLimit")


class CreateContainGroupResponse(AbstractModel):
    """CreateContainGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回创建成功的部署组ID，返回null表示失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 部署组所属的应用ID
        :type ApplicationId: str
        :param NamespaceId: 部署组所属命名空间ID
        :type NamespaceId: str
        :param GroupName: 部署组名称
        :type GroupName: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param GroupDesc: 部署组描述
        :type GroupDesc: str
        :param GroupResourceType: 部署组资源类型
        :type GroupResourceType: str
        """
        self.ApplicationId = None
        self.NamespaceId = None
        self.GroupName = None
        self.ClusterId = None
        self.GroupDesc = None
        self.GroupResourceType = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupName = params.get("GroupName")
        self.ClusterId = params.get("ClusterId")
        self.GroupDesc = params.get("GroupDesc")
        self.GroupResourceType = params.get("GroupResourceType")


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: groupId， null表示创建失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateMicroserviceRequest(AbstractModel):
    """CreateMicroservice请求参数结构体

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param MicroserviceName: 微服务名称
        :type MicroserviceName: str
        :param MicroserviceDesc: 微服务描述信息
        :type MicroserviceDesc: str
        """
        self.NamespaceId = None
        self.MicroserviceName = None
        self.MicroserviceDesc = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.MicroserviceName = params.get("MicroserviceName")
        self.MicroserviceDesc = params.get("MicroserviceDesc")


class CreateMicroserviceResponse(AbstractModel):
    """CreateMicroservice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 新增微服务是否成功。
true：操作成功。
false：操作失败。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceDesc: 命名空间描述
        :type NamespaceDesc: str
        :param NamespaceResourceType: 命名空间资源类型(默认值为DEF)
        :type NamespaceResourceType: str
        :param NamespaceType: 是否是全局命名空间(默认是DEF，表示普通命名空间；GLOBAL表示全局命名空间)
        :type NamespaceType: str
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        """
        self.NamespaceName = None
        self.ClusterId = None
        self.NamespaceDesc = None
        self.NamespaceResourceType = None
        self.NamespaceType = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.NamespaceName = params.get("NamespaceName")
        self.ClusterId = params.get("ClusterId")
        self.NamespaceDesc = params.get("NamespaceDesc")
        self.NamespaceResourceType = params.get("NamespaceResourceType")
        self.NamespaceType = params.get("NamespaceType")
        self.NamespaceId = params.get("NamespaceId")


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功时为命名空间ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreatePublicConfigRequest(AbstractModel):
    """CreatePublicConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigName: 配置项名称
        :type ConfigName: str
        :param ConfigVersion: 配置项版本
        :type ConfigVersion: str
        :param ConfigValue: 配置项值，总是接收yaml格式的内容
        :type ConfigValue: str
        :param ConfigVersionDesc: 配置项版本描述
        :type ConfigVersionDesc: str
        :param ConfigType: 配置项类型
        :type ConfigType: str
        :param EncodeWithBase64: Base64编码的配置项
        :type EncodeWithBase64: bool
        """
        self.ConfigName = None
        self.ConfigVersion = None
        self.ConfigValue = None
        self.ConfigVersionDesc = None
        self.ConfigType = None
        self.EncodeWithBase64 = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ConfigValue = params.get("ConfigValue")
        self.ConfigVersionDesc = params.get("ConfigVersionDesc")
        self.ConfigType = params.get("ConfigType")
        self.EncodeWithBase64 = params.get("EncodeWithBase64")


class CreatePublicConfigResponse(AbstractModel):
    """CreatePublicConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：创建成功；false：创建失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateServerlessGroupRequest(AbstractModel):
    """CreateServerlessGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 分组所属应用ID
        :type ApplicationId: str
        :param GroupName: 分组名称字段，长度1~60，字母或下划线开头，可包含字母数字下划线
        :type GroupName: str
        :param NamespaceId: 分组所属名字空间ID
        :type NamespaceId: str
        :param ClusterId: 分组所属集群ID
        :type ClusterId: str
        """
        self.ApplicationId = None
        self.GroupName = None
        self.NamespaceId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.GroupName = params.get("GroupName")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")


class CreateServerlessGroupResponse(AbstractModel):
    """CreateServerlessGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建成功的部署组ID，返回null表示失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApplicationRequest(AbstractModel):
    """DeleteApplication请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")


class DeleteApplicationResponse(AbstractModel):
    """DeleteApplication返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除应用操作是否成功。
true：操作成功。
false：操作失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteConfigRequest(AbstractModel):
    """DeleteConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置项ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DeleteConfigResponse(AbstractModel):
    """DeleteConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：删除成功；false：删除失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteContainerGroupRequest(AbstractModel):
    """DeleteContainerGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID，分组唯一标识
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteContainerGroupResponse(AbstractModel):
    """DeleteContainerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除操作是否成功：
true：成功
false：失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除部署组操作是否成功。
true：操作成功。
false：操作失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteImageTag(AbstractModel):
    """需要删除的镜像版本

    """

    def __init__(self):
        """
        :param RepoName: 仓库名，如/tsf/nginx
        :type RepoName: str
        :param TagName: 版本号:如V1
        :type TagName: str
        """
        self.RepoName = None
        self.TagName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")


class DeleteImageTagsRequest(AbstractModel):
    """DeleteImageTags请求参数结构体

    """

    def __init__(self):
        """
        :param ImageTags: 镜像版本数组
        :type ImageTags: list of DeleteImageTag
        """
        self.ImageTags = None


    def _deserialize(self, params):
        if params.get("ImageTags") is not None:
            self.ImageTags = []
            for item in params.get("ImageTags"):
                obj = DeleteImageTag()
                obj._deserialize(item)
                self.ImageTags.append(obj)


class DeleteImageTagsResponse(AbstractModel):
    """DeleteImageTags返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 批量删除操作是否成功。
true：成功。
false：失败。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteMicroserviceRequest(AbstractModel):
    """DeleteMicroservice请求参数结构体

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服务ID
        :type MicroserviceId: str
        """
        self.MicroserviceId = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")


class DeleteMicroserviceResponse(AbstractModel):
    """DeleteMicroservice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除微服务是否成功。
true：操作成功。
false：操作失败。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.NamespaceId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除命名空间是否成功。
true：删除成功。
false：删除失败。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeletePkgsRequest(AbstractModel):
    """DeletePkgs请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param PkgIds: 需要删除的程序包ID列表
        :type PkgIds: list of str
        """
        self.ApplicationId = None
        self.PkgIds = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgIds = params.get("PkgIds")


class DeletePkgsResponse(AbstractModel):
    """DeletePkgs返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePublicConfigRequest(AbstractModel):
    """DeletePublicConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置项ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DeletePublicConfigResponse(AbstractModel):
    """DeletePublicConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：删除成功；false：删除失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteServerlessGroupRequest(AbstractModel):
    """DeleteServerlessGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: groupId，分组唯一标识
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteServerlessGroupResponse(AbstractModel):
    """DeleteServerlessGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果true：成功；false：失败。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeployContainerGroupRequest(AbstractModel):
    """DeployContainerGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID，分组唯一标识
        :type GroupId: str
        :param Server: 镜像server
        :type Server: str
        :param TagName: 镜像版本名称,如v1
        :type TagName: str
        :param InstanceNum: 实例数量
        :type InstanceNum: int
        :param Reponame: 旧版镜像名，如/tsf/nginx
        :type Reponame: str
        :param CpuLimit: 业务容器最大的 CPU 核数，对应 K8S 的 limit；不填时默认为 request 的 2 倍
        :type CpuLimit: str
        :param MemLimit: 业务容器最大的内存 MiB 数，对应 K8S 的 limit；不填时默认为 request 的 2 倍
        :type MemLimit: str
        :param JvmOpts: jvm参数
        :type JvmOpts: str
        :param CpuRequest: 业务容器分配的 CPU 核数，对应 K8S 的 request
        :type CpuRequest: str
        :param MemRequest: 业务容器分配的内存 MiB 数，对应 K8S 的 request
        :type MemRequest: str
        :param DoNotStart: 是否不立即启动
        :type DoNotStart: bool
        :param RepoName: （优先使用）新版镜像名，如/tsf/nginx
        :type RepoName: str
        :param UpdateType: 更新方式：0:快速更新 1:滚动更新
        :type UpdateType: int
        :param UpdateIvl: 滚动更新必填，更新间隔
        :type UpdateIvl: int
        :param AgentCpuRequest: agent 容器分配的 CPU 核数，对应 K8S 的 request
        :type AgentCpuRequest: str
        :param AgentCpuLimit: agent 容器最大的 CPU 核数，对应 K8S 的 limit
        :type AgentCpuLimit: str
        :param AgentMemRequest: agent 容器分配的内存 MiB 数，对应 K8S 的 request
        :type AgentMemRequest: str
        :param AgentMemLimit: agent 容器最大的内存 MiB 数，对应 K8S 的 limit
        :type AgentMemLimit: str
        :param IstioCpuRequest: istioproxy 容器分配的 CPU 核数，对应 K8S 的 request
        :type IstioCpuRequest: str
        :param IstioCpuLimit: istioproxy 容器最大的 CPU 核数，对应 K8S 的 limit
        :type IstioCpuLimit: str
        :param IstioMemRequest: istioproxy 容器分配的内存 MiB 数，对应 K8S 的 request
        :type IstioMemRequest: str
        :param IstioMemLimit: istioproxy 容器最大的内存 MiB 数，对应 K8S 的 limit
        :type IstioMemLimit: str
        """
        self.GroupId = None
        self.Server = None
        self.TagName = None
        self.InstanceNum = None
        self.Reponame = None
        self.CpuLimit = None
        self.MemLimit = None
        self.JvmOpts = None
        self.CpuRequest = None
        self.MemRequest = None
        self.DoNotStart = None
        self.RepoName = None
        self.UpdateType = None
        self.UpdateIvl = None
        self.AgentCpuRequest = None
        self.AgentCpuLimit = None
        self.AgentMemRequest = None
        self.AgentMemLimit = None
        self.IstioCpuRequest = None
        self.IstioCpuLimit = None
        self.IstioMemRequest = None
        self.IstioMemLimit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Server = params.get("Server")
        self.TagName = params.get("TagName")
        self.InstanceNum = params.get("InstanceNum")
        self.Reponame = params.get("Reponame")
        self.CpuLimit = params.get("CpuLimit")
        self.MemLimit = params.get("MemLimit")
        self.JvmOpts = params.get("JvmOpts")
        self.CpuRequest = params.get("CpuRequest")
        self.MemRequest = params.get("MemRequest")
        self.DoNotStart = params.get("DoNotStart")
        self.RepoName = params.get("RepoName")
        self.UpdateType = params.get("UpdateType")
        self.UpdateIvl = params.get("UpdateIvl")
        self.AgentCpuRequest = params.get("AgentCpuRequest")
        self.AgentCpuLimit = params.get("AgentCpuLimit")
        self.AgentMemRequest = params.get("AgentMemRequest")
        self.AgentMemLimit = params.get("AgentMemLimit")
        self.IstioCpuRequest = params.get("IstioCpuRequest")
        self.IstioCpuLimit = params.get("IstioCpuLimit")
        self.IstioMemRequest = params.get("IstioMemRequest")
        self.IstioMemLimit = params.get("IstioMemLimit")


class DeployContainerGroupResponse(AbstractModel):
    """DeployContainerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 部署容器应用是否成功。
true：成功。
false：失败。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeployGroupRequest(AbstractModel):
    """DeployGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        :param PkgId: 程序包ID
        :type PkgId: str
        :param StartupParameters: 部署组启动参数
        :type StartupParameters: str
        """
        self.GroupId = None
        self.PkgId = None
        self.StartupParameters = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PkgId = params.get("PkgId")
        self.StartupParameters = params.get("StartupParameters")


class DeployGroupResponse(AbstractModel):
    """DeployGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeployServerlessGroupRequest(AbstractModel):
    """DeployServerlessGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        :param PkgId: 程序包ID
        :type PkgId: str
        :param Memory: 所需实例内存大小，取值为 1Gi 2Gi 4Gi 8Gi 16Gi，缺省为 1Gi，不传表示维持原态
        :type Memory: str
        :param InstanceRequest: 要求最小实例数，取值范围 [1, 4]，缺省为 1，不传表示维持原态
        :type InstanceRequest: int
        :param StartupParameters: 部署组启动参数，不传表示维持原态
        :type StartupParameters: str
        """
        self.GroupId = None
        self.PkgId = None
        self.Memory = None
        self.InstanceRequest = None
        self.StartupParameters = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PkgId = params.get("PkgId")
        self.Memory = params.get("Memory")
        self.InstanceRequest = params.get("InstanceRequest")
        self.StartupParameters = params.get("StartupParameters")


class DeployServerlessGroupResponse(AbstractModel):
    """DeployServerlessGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果true：成功；false：失败；
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeApplicationAttributeRequest(AbstractModel):
    """DescribeApplicationAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")


class DescribeApplicationAttributeResponse(AbstractModel):
    """DescribeApplicationAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 应用列表其它字段返回参数
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApplicationAttribute`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplicationAttribute()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationRequest(AbstractModel):
    """DescribeApplication请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")


class DescribeApplicationResponse(AbstractModel):
    """DescribeApplication返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 应用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApplicationForPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplicationForPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications请求参数结构体

    """

    def __init__(self):
        """
        :param SearchWord: 搜索字段
        :type SearchWord: str
        :param OrderBy: 排序字段
        :type OrderBy: str
        :param OrderType: 排序类型
        :type OrderType: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分页个数
        :type Limit: int
        :param ApplicationType: 应用类型
        :type ApplicationType: str
        :param MicroserviceType: 应用的微服务类型
        :type MicroserviceType: str
        :param ApplicationResourceTypeList: 应用资源类型数组
        :type ApplicationResourceTypeList: list of str
        """
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ApplicationResourceTypeList = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationResourceTypeList = params.get("ApplicationResourceTypeList")


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 应用分页列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageApplication`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageApplication()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SearchWord: 搜索字段
        :type SearchWord: str
        :param OrderBy: 排序字段
        :type OrderBy: str
        :param OrderType: 排序类型
        :type OrderType: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分页个数
        :type Limit: int
        """
        self.ClusterId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 集群机器实例分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageInstance`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageInstance()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigReleaseLogsRequest(AbstractModel):
    """DescribeConfigReleaseLogs请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID，不传入时查询全量
        :type GroupId: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 每页条数，默认为20
        :type Limit: int
        :param NamespaceId: 命名空间ID，不传入时查询全量
        :type NamespaceId: str
        :param ClusterId: 集群ID，不传入时查询全量
        :type ClusterId: str
        :param ApplicationId: 应用ID，不传入时查询全量
        :type ApplicationId: str
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None
        self.NamespaceId = None
        self.ClusterId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")
        self.ApplicationId = params.get("ApplicationId")


class DescribeConfigReleaseLogsResponse(AbstractModel):
    """DescribeConfigReleaseLogs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页的配置项发布历史列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigReleaseLog`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfigReleaseLog()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigReleasesRequest(AbstractModel):
    """DescribeConfigReleases请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigName: 配置项名称，不传入时查询全量
        :type ConfigName: str
        :param GroupId: 部署组ID，不传入时查询全量
        :type GroupId: str
        :param NamespaceId: 命名空间ID，不传入时查询全量
        :type NamespaceId: str
        :param ClusterId: 集群ID，不传入时查询全量
        :type ClusterId: str
        :param Limit: 每页条数
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param ConfigId: 配置ID，不传入时查询全量
        :type ConfigId: str
        :param ApplicationId: 应用ID，不传入时查询全量
        :type ApplicationId: str
        """
        self.ConfigName = None
        self.GroupId = None
        self.NamespaceId = None
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.ConfigId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.GroupId = params.get("GroupId")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ConfigId = params.get("ConfigId")
        self.ApplicationId = params.get("ApplicationId")


class DescribeConfigReleasesResponse(AbstractModel):
    """DescribeConfigReleases返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页的配置发布信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigRelease`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfigRelease()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置项ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.Config`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Config()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigSummaryRequest(AbstractModel):
    """DescribeConfigSummary请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID，不传入时查询全量
        :type ApplicationId: str
        :param SearchWord: 查询关键字，模糊查询：应用名称，配置项名称，不传入时查询全量
        :type SearchWord: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 每页条数，默认为20
        :type Limit: int
        """
        self.ApplicationId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeConfigSummaryResponse(AbstractModel):
    """DescribeConfigSummary返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 配置项分页对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigsRequest(AbstractModel):
    """DescribeConfigs请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID，不传入时查询全量
        :type ApplicationId: str
        :param ConfigId: 配置项ID，不传入时查询全量，高优先级
        :type ConfigId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每页条数
        :type Limit: int
        :param ConfigIdList: 配置项ID列表，不传入时查询全量，低优先级
        :type ConfigIdList: list of str
        :param ConfigName: 配置项名称，精确查询，不传入时查询全量
        :type ConfigName: str
        :param ConfigVersion: 配置项版本，精确查询，不传入时查询全量
        :type ConfigVersion: str
        """
        self.ApplicationId = None
        self.ConfigId = None
        self.Offset = None
        self.Limit = None
        self.ConfigIdList = None
        self.ConfigName = None
        self.ConfigVersion = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ConfigId = params.get("ConfigId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ConfigIdList = params.get("ConfigIdList")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")


class DescribeConfigsResponse(AbstractModel):
    """DescribeConfigs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页后的配置项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeContainerGroupDetailRequest(AbstractModel):
    """DescribeContainerGroupDetail请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 分组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeContainerGroupDetailResponse(AbstractModel):
    """DescribeContainerGroupDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 容器部署组详情
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ContainerGroupDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ContainerGroupDetail()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeContainerGroupsRequest(AbstractModel):
    """DescribeContainerGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SearchWord: 搜索字段，模糊搜索groupName字段
        :type SearchWord: str
        :param ApplicationId: 分组所属应用ID
        :type ApplicationId: str
        :param OrderBy: 排序字段，默认为 createTime字段，支持id， name， createTime
        :type OrderBy: str
        :param OrderType: 排序方式，默认为1：倒序排序，0：正序，1：倒序
        :type OrderType: int
        :param Offset: 偏移量，取值从0开始
        :type Offset: int
        :param Limit: 分页个数，默认为20， 取值应为1~50
        :type Limit: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空间 ID
        :type NamespaceId: str
        """
        self.SearchWord = None
        self.ApplicationId = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.ApplicationId = params.get("ApplicationId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")


class DescribeContainerGroupsResponse(AbstractModel):
    """DescribeContainerGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询的权限数据对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ContainGroupResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ContainGroupResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeDownloadInfoRequest(AbstractModel):
    """DescribeDownloadInfo请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param PkgId: 程序包ID
        :type PkgId: str
        """
        self.ApplicationId = None
        self.PkgId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgId = params.get("PkgId")


class DescribeDownloadInfoResponse(AbstractModel):
    """DescribeDownloadInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: COS鉴权信息
        :type Result: :class:`tencentcloud.tsf.v20180326.models.CosDownloadInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CosDownloadInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupInstancesRequest(AbstractModel):
    """DescribeGroupInstances请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        :param SearchWord: 搜索字段
        :type SearchWord: str
        :param OrderBy: 排序字段
        :type OrderBy: str
        :param OrderType: 排序类型
        :type OrderType: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分页个数
        :type Limit: int
        """
        self.GroupId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeGroupInstancesResponse(AbstractModel):
    """DescribeGroupInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 部署组机器信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageInstance`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageInstance()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 虚拟机部署组详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.VmGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = VmGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupsRequest(AbstractModel):
    """DescribeGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SearchWord: 搜索字段
        :type SearchWord: str
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param OrderBy: 排序字段
        :type OrderBy: str
        :param OrderType: 排序方式
        :type OrderType: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分页个数
        :type Limit: int
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param GroupResourceTypeList: 部署组资源类型列表
        :type GroupResourceTypeList: list of str
        """
        self.SearchWord = None
        self.ApplicationId = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.NamespaceId = None
        self.ClusterId = None
        self.GroupResourceTypeList = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.ApplicationId = params.get("ApplicationId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")
        self.GroupResourceTypeList = params.get("GroupResourceTypeList")


class DescribeGroupsResponse(AbstractModel):
    """DescribeGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 虚拟机部署组分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageVmGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageVmGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeImageTagsRequest(AbstractModel):
    """DescribeImageTags请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用Id
        :type ApplicationId: str
        :param Offset: 偏移量，取值从0开始
        :type Offset: int
        :param Limit: 分页个数，默认为20， 取值应为1~100
        :type Limit: int
        :param QueryImageIdFlag: 不填和0:查询 1:不查询
        :type QueryImageIdFlag: int
        :param SearchWord: 可用于搜索的 tag 名字
        :type SearchWord: str
        """
        self.ApplicationId = None
        self.Offset = None
        self.Limit = None
        self.QueryImageIdFlag = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.QueryImageIdFlag = params.get("QueryImageIdFlag")
        self.SearchWord = params.get("SearchWord")


class DescribeImageTagsResponse(AbstractModel):
    """DescribeImageTags返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询的权限数据对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ImageTagsResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ImageTagsResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeMicroserviceRequest(AbstractModel):
    """DescribeMicroservice请求参数结构体

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服务ID
        :type MicroserviceId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分页个数
        :type Limit: int
        """
        self.MicroserviceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMicroserviceResponse(AbstractModel):
    """DescribeMicroservice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 微服务详情实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageMsInstance`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageMsInstance()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeMicroservicesRequest(AbstractModel):
    """DescribeMicroservices请求参数结构体

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param SearchWord: 搜索字段
        :type SearchWord: str
        :param OrderBy: 排序字段
        :type OrderBy: str
        :param OrderType: 排序类型
        :type OrderType: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分页个数
        :type Limit: int
        """
        self.NamespaceId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMicroservicesResponse(AbstractModel):
    """DescribeMicroservices返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 微服务分页列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageMicroservice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageMicroservice()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePkgsRequest(AbstractModel):
    """DescribePkgs请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID（只传入应用ID，返回该应用下所有软件包信息）
        :type ApplicationId: str
        :param SearchWord: 查询关键字（支持根据包ID，包名，包版本号搜索）
        :type SearchWord: str
        :param OrderBy: 排序关键字（默认为"UploadTime"：上传时间）
        :type OrderBy: str
        :param OrderType: 升序：0/降序：1（默认降序）
        :type OrderType: int
        :param Offset: 查询起始偏移
        :type Offset: int
        :param Limit: 返回数量限制
        :type Limit: int
        """
        self.ApplicationId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePkgsResponse(AbstractModel):
    """DescribePkgs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 符合查询程序包信息列表
        :type Result: :class:`tencentcloud.tsf.v20180326.models.PkgList`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = PkgList()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePodInstancesRequest(AbstractModel):
    """DescribePodInstances请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 实例所属groupId
        :type GroupId: str
        :param Offset: 偏移量，取值从0开始
        :type Offset: int
        :param Limit: 分页个数，默认为20， 取值应为1~50
        :type Limit: int
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePodInstancesResponse(AbstractModel):
    """DescribePodInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询的权限数据对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.GroupPodResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupPodResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePublicConfigReleaseLogsRequest(AbstractModel):
    """DescribePublicConfigReleaseLogs请求参数结构体

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间ID，不传入时查询全量
        :type NamespaceId: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 每页条数，默认为20
        :type Limit: int
        """
        self.NamespaceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePublicConfigReleaseLogsResponse(AbstractModel):
    """DescribePublicConfigReleaseLogs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页后的公共配置项发布历史列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigReleaseLog`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfigReleaseLog()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePublicConfigReleasesRequest(AbstractModel):
    """DescribePublicConfigReleases请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigName: 配置项名称，不传入时查询全量
        :type ConfigName: str
        :param NamespaceId: 命名空间ID，不传入时查询全量
        :type NamespaceId: str
        :param Limit: 每页条数
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param ConfigId: 配置项ID，不传入时查询全量
        :type ConfigId: str
        """
        self.ConfigName = None
        self.NamespaceId = None
        self.Limit = None
        self.Offset = None
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.NamespaceId = params.get("NamespaceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ConfigId = params.get("ConfigId")


class DescribePublicConfigReleasesResponse(AbstractModel):
    """DescribePublicConfigReleases返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 公共配置发布信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigRelease`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfigRelease()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePublicConfigRequest(AbstractModel):
    """DescribePublicConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 需要查询的配置项ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DescribePublicConfigResponse(AbstractModel):
    """DescribePublicConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 全局配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.Config`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Config()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePublicConfigSummaryRequest(AbstractModel):
    """DescribePublicConfigSummary请求参数结构体

    """

    def __init__(self):
        """
        :param SearchWord: 查询关键字，模糊查询：配置项名称，不传入时查询全量
        :type SearchWord: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 每页条数，默认为20
        :type Limit: int
        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePublicConfigSummaryResponse(AbstractModel):
    """DescribePublicConfigSummary返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页的全局配置统计信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePublicConfigsRequest(AbstractModel):
    """DescribePublicConfigs请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置项ID，不传入时查询全量，高优先级
        :type ConfigId: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 每页条数，默认为20
        :type Limit: int
        :param ConfigIdList: 配置项ID列表，不传入时查询全量，低优先级
        :type ConfigIdList: list of str
        :param ConfigName: 配置项名称，精确查询，不传入时查询全量
        :type ConfigName: str
        :param ConfigVersion: 配置项版本，精确查询，不传入时查询全量
        :type ConfigVersion: str
        """
        self.ConfigId = None
        self.Offset = None
        self.Limit = None
        self.ConfigIdList = None
        self.ConfigName = None
        self.ConfigVersion = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ConfigIdList = params.get("ConfigIdList")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")


class DescribePublicConfigsResponse(AbstractModel):
    """DescribePublicConfigs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页后的全局配置项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeReleasedConfigRequest(AbstractModel):
    """DescribeReleasedConfig请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeReleasedConfigResponse(AbstractModel):
    """DescribeReleasedConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 已发布的配置内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeServerlessGroupRequest(AbstractModel):
    """DescribeServerlessGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeServerlessGroupResponse(AbstractModel):
    """DescribeServerlessGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ServerlessGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServerlessGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServerlessGroupsRequest(AbstractModel):
    """DescribeServerlessGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SearchWord: 搜索字段，模糊搜索groupName字段
        :type SearchWord: str
        :param ApplicationId: 分组所属应用ID
        :type ApplicationId: str
        :param OrderBy: 排序字段，默认为 createTime字段，支持id， name， createTime
        :type OrderBy: str
        :param OrderType: 排序方式，默认为1：倒序排序，0：正序，1：倒序
        :type OrderType: str
        :param Offset: 偏移量，取值从0开始
        :type Offset: int
        :param Limit: 分页个数，默认为20， 取值应为1~50
        :type Limit: int
        :param NamespaceId: 分组所属名字空间ID
        :type NamespaceId: str
        :param ClusterId: 分组所属集群ID
        :type ClusterId: str
        """
        self.SearchWord = None
        self.ApplicationId = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.NamespaceId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.ApplicationId = params.get("ApplicationId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")


class DescribeServerlessGroupsResponse(AbstractModel):
    """DescribeServerlessGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 数据列表对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ServerlessGroupPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServerlessGroupPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeSimpleApplicationsRequest(AbstractModel):
    """DescribeSimpleApplications请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationIdList: 应用ID列表
        :type ApplicationIdList: list of str
        :param ApplicationType: 应用类型
        :type ApplicationType: str
        :param Limit: 每页条数
        :type Limit: int
        :param Offset: 起始偏移量
        :type Offset: int
        :param MicroserviceType: 微服务类型
        :type MicroserviceType: str
        :param ApplicationResourceTypeList: 资源类型数组
        :type ApplicationResourceTypeList: list of str
        :param SearchWord: 通过id和name进行关键词过滤
        :type SearchWord: str
        """
        self.ApplicationIdList = None
        self.ApplicationType = None
        self.Limit = None
        self.Offset = None
        self.MicroserviceType = None
        self.ApplicationResourceTypeList = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.ApplicationIdList = params.get("ApplicationIdList")
        self.ApplicationType = params.get("ApplicationType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationResourceTypeList = params.get("ApplicationResourceTypeList")
        self.SearchWord = params.get("SearchWord")


class DescribeSimpleApplicationsResponse(AbstractModel):
    """DescribeSimpleApplications返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 简单应用分页对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageSimpleApplication`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageSimpleApplication()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeSimpleClustersRequest(AbstractModel):
    """DescribeSimpleClusters请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterIdList: 需要查询的集群ID列表，不填或不传入时查询所有内容
        :type ClusterIdList: list of str
        :param ClusterType: 需要查询的集群类型，不填或不传入时查询所有内容
        :type ClusterType: str
        :param Offset: 查询偏移量，默认为0
        :type Offset: int
        :param Limit: 分页个数，默认为20， 取值应为1~50
        :type Limit: int
        :param SearchWord: 对id和name进行关键词过滤
        :type SearchWord: str
        """
        self.ClusterIdList = None
        self.ClusterType = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.ClusterIdList = params.get("ClusterIdList")
        self.ClusterType = params.get("ClusterType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")


class DescribeSimpleClustersResponse(AbstractModel):
    """DescribeSimpleClusters返回参数结构体

    """

    def __init__(self):
        """
        :param Result: TSF集群分页对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageCluster`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageCluster()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeSimpleGroupsRequest(AbstractModel):
    """DescribeSimpleGroups请求参数结构体

    """

    def __init__(self):
        """
        :param GroupIdList: 部署组ID列表，不填写时查询全量
        :type GroupIdList: list of str
        :param ApplicationId: 应用ID，不填写时查询全量
        :type ApplicationId: str
        :param ClusterId: 集群ID，不填写时查询全量
        :type ClusterId: str
        :param NamespaceId: 命名空间ID，不填写时查询全量
        :type NamespaceId: str
        :param Limit: 每页条数
        :type Limit: int
        :param Offset: 起始偏移量
        :type Offset: int
        :param GroupId: 部署组ID，不填写时查询全量
        :type GroupId: str
        :param SearchWord: 模糊查询，部署组名称，不填写时查询全量
        :type SearchWord: str
        :param AppMicroServiceType: 部署组类型，精确过滤字段，M：service mesh, P：原生应用， M：网关应用
        :type AppMicroServiceType: str
        """
        self.GroupIdList = None
        self.ApplicationId = None
        self.ClusterId = None
        self.NamespaceId = None
        self.Limit = None
        self.Offset = None
        self.GroupId = None
        self.SearchWord = None
        self.AppMicroServiceType = None


    def _deserialize(self, params):
        self.GroupIdList = params.get("GroupIdList")
        self.ApplicationId = params.get("ApplicationId")
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.GroupId = params.get("GroupId")
        self.SearchWord = params.get("SearchWord")
        self.AppMicroServiceType = params.get("AppMicroServiceType")


class DescribeSimpleGroupsResponse(AbstractModel):
    """DescribeSimpleGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 简单部署组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageSimpleGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageSimpleGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeSimpleNamespacesRequest(AbstractModel):
    """DescribeSimpleNamespaces请求参数结构体

    """

    def __init__(self):
        """
        :param NamespaceIdList: 命名空间ID列表，不传入时查询全量
        :type NamespaceIdList: list of str
        :param ClusterId: 集群ID，不传入时查询全量
        :type ClusterId: str
        :param Limit: 每页条数
        :type Limit: int
        :param Offset: 起始偏移量
        :type Offset: int
        :param NamespaceId: 命名空间ID，不传入时查询全量
        :type NamespaceId: str
        :param NamespaceResourceTypeList: 查询资源类型列表
        :type NamespaceResourceTypeList: list of str
        :param SearchWord: 通过id和name进行过滤
        :type SearchWord: str
        :param NamespaceTypeList: 查询的命名空间类型列表
        :type NamespaceTypeList: list of str
        :param NamespaceName: 通过命名空间名精确过滤
        :type NamespaceName: str
        :param IsDefault: 通过是否是默认命名空间过滤，不传表示拉取全部命名空间。0：默认，命名空间。1：非默认命名空间
        :type IsDefault: str
        """
        self.NamespaceIdList = None
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.NamespaceId = None
        self.NamespaceResourceTypeList = None
        self.SearchWord = None
        self.NamespaceTypeList = None
        self.NamespaceName = None
        self.IsDefault = None


    def _deserialize(self, params):
        self.NamespaceIdList = params.get("NamespaceIdList")
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceResourceTypeList = params.get("NamespaceResourceTypeList")
        self.SearchWord = params.get("SearchWord")
        self.NamespaceTypeList = params.get("NamespaceTypeList")
        self.NamespaceName = params.get("NamespaceName")
        self.IsDefault = params.get("IsDefault")


class DescribeSimpleNamespacesResponse(AbstractModel):
    """DescribeSimpleNamespaces返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 命名空间分页列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageNamespace`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageNamespace()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUploadInfoRequest(AbstractModel):
    """DescribeUploadInfo请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param PkgName: 程序包名
        :type PkgName: str
        :param PkgVersion: 程序包版本
        :type PkgVersion: str
        :param PkgType: 程序包类型
        :type PkgType: str
        :param PkgDesc: 程序包介绍
        :type PkgDesc: str
        """
        self.ApplicationId = None
        self.PkgName = None
        self.PkgVersion = None
        self.PkgType = None
        self.PkgDesc = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgName = params.get("PkgName")
        self.PkgVersion = params.get("PkgVersion")
        self.PkgType = params.get("PkgType")
        self.PkgDesc = params.get("PkgDesc")


class DescribeUploadInfoResponse(AbstractModel):
    """DescribeUploadInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: COS上传信息
        :type Result: :class:`tencentcloud.tsf.v20180326.models.CosUploadInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CosUploadInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class Env(AbstractModel):
    """环境变量

    """

    def __init__(self):
        """
        :param Name: 环境变量名称
        :type Name: str
        :param Value: 服务端口
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class ExpandGroupRequest(AbstractModel):
    """ExpandGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        :param InstanceIdList: 扩容的机器实例ID列表
        :type InstanceIdList: list of str
        """
        self.GroupId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.InstanceIdList = params.get("InstanceIdList")


class ExpandGroupResponse(AbstractModel):
    """ExpandGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class GroupPod(AbstractModel):
    """部署组实例列表

    """

    def __init__(self):
        """
        :param PodName: 实例名称(对应到kubernetes的pod名称)
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        :param PodId: 实例ID(对应到kubernetes的pod id)
注意：此字段可能返回 null，表示取不到有效值。
        :type PodId: str
        :param Status: 实例状态，请参考后面的实例以及容器的状态定义
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Reason: 实例处于当前状态的原因，例如容器下载镜像失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param NodeIp: 主机IP
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeIp: str
        :param Ip: 实例IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param RestartCount: 实例中容器的重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param ReadyCount: 实例中已就绪容器的个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadyCount: int
        :param Runtime: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param CreatedAt: 实例启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param ServiceInstanceStatus: 服务实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceInstanceStatus: str
        :param InstanceAvailableStatus: 机器实例可使用状态
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAvailableStatus: str
        :param InstanceStatus: 机器实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStatus: str
        """
        self.PodName = None
        self.PodId = None
        self.Status = None
        self.Reason = None
        self.NodeIp = None
        self.Ip = None
        self.RestartCount = None
        self.ReadyCount = None
        self.Runtime = None
        self.CreatedAt = None
        self.ServiceInstanceStatus = None
        self.InstanceAvailableStatus = None
        self.InstanceStatus = None


    def _deserialize(self, params):
        self.PodName = params.get("PodName")
        self.PodId = params.get("PodId")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.NodeIp = params.get("NodeIp")
        self.Ip = params.get("Ip")
        self.RestartCount = params.get("RestartCount")
        self.ReadyCount = params.get("ReadyCount")
        self.Runtime = params.get("Runtime")
        self.CreatedAt = params.get("CreatedAt")
        self.ServiceInstanceStatus = params.get("ServiceInstanceStatus")
        self.InstanceAvailableStatus = params.get("InstanceAvailableStatus")
        self.InstanceStatus = params.get("InstanceStatus")


class GroupPodResult(AbstractModel):
    """部署组实例列表

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of GroupPod
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = GroupPod()
                obj._deserialize(item)
                self.Content.append(obj)


class ImageTag(AbstractModel):
    """列表信息

    """

    def __init__(self):
        """
        :param RepoName: 仓库名
        :type RepoName: str
        :param TagName: 版本名称
        :type TagName: str
        :param TagId: 版本ID
        :type TagId: str
        :param ImageId: 镜像ID
        :type ImageId: str
        :param Size: 大小
        :type Size: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Author: 镜像制作者
        :type Author: str
        :param Architecture: CPU架构
        :type Architecture: str
        :param DockerVersion: Docker客户端版本
        :type DockerVersion: str
        :param Os: 操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Os: str
        :param PushTime: push时间
        :type PushTime: str
        :param SizeByte: 单位为字节
        :type SizeByte: int
        """
        self.RepoName = None
        self.TagName = None
        self.TagId = None
        self.ImageId = None
        self.Size = None
        self.CreationTime = None
        self.UpdateTime = None
        self.Author = None
        self.Architecture = None
        self.DockerVersion = None
        self.Os = None
        self.PushTime = None
        self.SizeByte = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")
        self.TagId = params.get("TagId")
        self.ImageId = params.get("ImageId")
        self.Size = params.get("Size")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Author = params.get("Author")
        self.Architecture = params.get("Architecture")
        self.DockerVersion = params.get("DockerVersion")
        self.Os = params.get("Os")
        self.PushTime = params.get("PushTime")
        self.SizeByte = params.get("SizeByte")


class ImageTagsResult(AbstractModel):
    """镜像版本列表

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param RepoName: 仓库名,含命名空间,如tsf/ngin
        :type RepoName: str
        :param Server: 镜像服务器地址
        :type Server: str
        :param Content: 列表信息
        :type Content: list of ImageTag
        """
        self.TotalCount = None
        self.RepoName = None
        self.Server = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.RepoName = params.get("RepoName")
        self.Server = params.get("Server")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ImageTag()
                obj._deserialize(item)
                self.Content.append(obj)


class Instance(AbstractModel):
    """机器实例

    """

    def __init__(self):
        """
        :param InstanceId: 机器实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 机器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param LanIp: 机器内网地址IP
注意：此字段可能返回 null，表示取不到有效值。
        :type LanIp: str
        :param WanIp: 机器外网地址IP
注意：此字段可能返回 null，表示取不到有效值。
        :type WanIp: str
        :param InstanceDesc: 机器描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceDesc: str
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param InstanceStatus: VM的状态 虚机：虚机的状态 容器：Pod所在虚机的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStatus: str
        :param InstanceAvailableStatus: VM的可使用状态 虚机：虚机是否能够作为资源使用 容器：虚机是否能够作为资源部署POD
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAvailableStatus: str
        :param ServiceInstanceStatus: 服务下的服务实例的状态 虚机：应用是否可用 + Agent状态 容器：Pod状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceInstanceStatus: str
        :param CountInTsf: 标识此instance是否已添加在tsf中
注意：此字段可能返回 null，表示取不到有效值。
        :type CountInTsf: int
        :param GroupId: 机器所属部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param ApplicationId: 机器所属应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 机器所属应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param InstanceCreatedTime: 机器实例在CVM的创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCreatedTime: str
        :param InstanceExpiredTime: 机器实例在CVM的过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceExpiredTime: str
        :param InstanceChargeType: 机器实例在CVM的计费模式
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param InstanceTotalCpu: 机器实例总CPU信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTotalCpu: float
        :param InstanceTotalMem: 机器实例总内存信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTotalMem: float
        :param InstanceUsedCpu: 机器实例使用的CPU信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceUsedCpu: float
        :param InstanceUsedMem: 机器实例使用的内存信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceUsedMem: float
        :param InstanceLimitCpu: 机器实例Limit CPU信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceLimitCpu: float
        :param InstanceLimitMem: 机器实例Limit 内存信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceLimitMem: float
        :param InstancePkgVersion: 包版本
注意：此字段可能返回 null，表示取不到有效值。
        :type InstancePkgVersion: str
        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param RestrictState: 机器实例业务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RestrictState: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param OperationState: 实例执行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationState: int
        :param NamespaceId: NamespaceId
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param InstanceZoneId: InstanceZoneId
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceZoneId: str
        :param InstanceImportMode: InstanceImportMode
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceImportMode: str
        :param ApplicationType: ApplicationType
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param ApplicationResourceType: ApplicationResourceType
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationResourceType: str
        :param ServiceSidecarStatus: ServiceSidecarStatus
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceSidecarStatus: str
        :param GroupName: GroupName
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param NamespaceName: NamespaceName
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.LanIp = None
        self.WanIp = None
        self.InstanceDesc = None
        self.ClusterId = None
        self.ClusterName = None
        self.InstanceStatus = None
        self.InstanceAvailableStatus = None
        self.ServiceInstanceStatus = None
        self.CountInTsf = None
        self.GroupId = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.InstanceCreatedTime = None
        self.InstanceExpiredTime = None
        self.InstanceChargeType = None
        self.InstanceTotalCpu = None
        self.InstanceTotalMem = None
        self.InstanceUsedCpu = None
        self.InstanceUsedMem = None
        self.InstanceLimitCpu = None
        self.InstanceLimitMem = None
        self.InstancePkgVersion = None
        self.ClusterType = None
        self.RestrictState = None
        self.UpdateTime = None
        self.OperationState = None
        self.NamespaceId = None
        self.InstanceZoneId = None
        self.InstanceImportMode = None
        self.ApplicationType = None
        self.ApplicationResourceType = None
        self.ServiceSidecarStatus = None
        self.GroupName = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.LanIp = params.get("LanIp")
        self.WanIp = params.get("WanIp")
        self.InstanceDesc = params.get("InstanceDesc")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.InstanceStatus = params.get("InstanceStatus")
        self.InstanceAvailableStatus = params.get("InstanceAvailableStatus")
        self.ServiceInstanceStatus = params.get("ServiceInstanceStatus")
        self.CountInTsf = params.get("CountInTsf")
        self.GroupId = params.get("GroupId")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.InstanceCreatedTime = params.get("InstanceCreatedTime")
        self.InstanceExpiredTime = params.get("InstanceExpiredTime")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.InstanceTotalCpu = params.get("InstanceTotalCpu")
        self.InstanceTotalMem = params.get("InstanceTotalMem")
        self.InstanceUsedCpu = params.get("InstanceUsedCpu")
        self.InstanceUsedMem = params.get("InstanceUsedMem")
        self.InstanceLimitCpu = params.get("InstanceLimitCpu")
        self.InstanceLimitMem = params.get("InstanceLimitMem")
        self.InstancePkgVersion = params.get("InstancePkgVersion")
        self.ClusterType = params.get("ClusterType")
        self.RestrictState = params.get("RestrictState")
        self.UpdateTime = params.get("UpdateTime")
        self.OperationState = params.get("OperationState")
        self.NamespaceId = params.get("NamespaceId")
        self.InstanceZoneId = params.get("InstanceZoneId")
        self.InstanceImportMode = params.get("InstanceImportMode")
        self.ApplicationType = params.get("ApplicationType")
        self.ApplicationResourceType = params.get("ApplicationResourceType")
        self.ServiceSidecarStatus = params.get("ServiceSidecarStatus")
        self.GroupName = params.get("GroupName")
        self.NamespaceName = params.get("NamespaceName")


class Microservice(AbstractModel):
    """微服务

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceId: str
        :param MicroserviceName: 微服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceName: str
        :param MicroserviceDesc: 微服务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceDesc: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param RunInstanceCount: 微服务的运行实例数目
注意：此字段可能返回 null，表示取不到有效值。
        :type RunInstanceCount: int
        """
        self.MicroserviceId = None
        self.MicroserviceName = None
        self.MicroserviceDesc = None
        self.CreateTime = None
        self.UpdateTime = None
        self.NamespaceId = None
        self.RunInstanceCount = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.MicroserviceName = params.get("MicroserviceName")
        self.MicroserviceDesc = params.get("MicroserviceDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.NamespaceId = params.get("NamespaceId")
        self.RunInstanceCount = params.get("RunInstanceCount")


class ModifyContainerGroupRequest(AbstractModel):
    """ModifyContainerGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        :param AccessType: 0:公网 1:集群内访问 2：NodePort
        :type AccessType: int
        :param ProtocolPorts: ProtocolPorts数组
        :type ProtocolPorts: list of ProtocolPort
        :param UpdateType: 更新方式：0:快速更新 1:滚动更新
        :type UpdateType: int
        :param UpdateIvl: 更新间隔,单位秒
        :type UpdateIvl: int
        """
        self.GroupId = None
        self.AccessType = None
        self.ProtocolPorts = None
        self.UpdateType = None
        self.UpdateIvl = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.AccessType = params.get("AccessType")
        if params.get("ProtocolPorts") is not None:
            self.ProtocolPorts = []
            for item in params.get("ProtocolPorts"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPorts.append(obj)
        self.UpdateType = params.get("UpdateType")
        self.UpdateIvl = params.get("UpdateIvl")


class ModifyContainerGroupResponse(AbstractModel):
    """ModifyContainerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 更新部署组是否成功。
true：成功。
false：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyContainerReplicasRequest(AbstractModel):
    """ModifyContainerReplicas请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID，部署组唯一标识
        :type GroupId: str
        :param InstanceNum: 实例数量
        :type InstanceNum: int
        """
        self.GroupId = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.InstanceNum = params.get("InstanceNum")


class ModifyContainerReplicasResponse(AbstractModel):
    """ModifyContainerReplicas返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果true：成功；false：失败；
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyMicroserviceRequest(AbstractModel):
    """ModifyMicroservice请求参数结构体

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服务 ID
        :type MicroserviceId: str
        :param MicroserviceDesc: 微服务备注信息
        :type MicroserviceDesc: str
        """
        self.MicroserviceId = None
        self.MicroserviceDesc = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.MicroserviceDesc = params.get("MicroserviceDesc")


class ModifyMicroserviceResponse(AbstractModel):
    """ModifyMicroservice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 修改微服务详情是否成功。
true：操作成功。
false：操作失败。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyUploadInfoRequest(AbstractModel):
    """ModifyUploadInfo请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param PkgId: 调用DescribeUploadInfo接口时返回的软件包ID
        :type PkgId: str
        :param Result: COS返回上传结果（默认为0：成功，其他值表示失败）
        :type Result: int
        :param Md5: 程序包MD5
        :type Md5: str
        :param Size: 程序包大小（单位字节）
        :type Size: int
        """
        self.ApplicationId = None
        self.PkgId = None
        self.Result = None
        self.Md5 = None
        self.Size = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgId = params.get("PkgId")
        self.Result = params.get("Result")
        self.Md5 = params.get("Md5")
        self.Size = params.get("Size")


class ModifyUploadInfoResponse(AbstractModel):
    """ModifyUploadInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MsInstance(AbstractModel):
    """微服务实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 机器实例ID信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 机器实例名称信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param Port: 服务运行的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        :param LanIp: 机器实例内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type LanIp: str
        :param WanIp: 机器实例外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type WanIp: str
        :param InstanceAvailableStatus: 机器可用状态
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAvailableStatus: str
        :param ServiceInstanceStatus: 服务运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceInstanceStatus: str
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param InstanceStatus: 机器TSF可用状态
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStatus: str
        :param HealthCheckUrl: 健康检查URL
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckUrl: str
        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param ApplicationPackageVersion: 应用程序包版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationPackageVersion: str
        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Port = None
        self.LanIp = None
        self.WanIp = None
        self.InstanceAvailableStatus = None
        self.ServiceInstanceStatus = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.GroupId = None
        self.GroupName = None
        self.InstanceStatus = None
        self.HealthCheckUrl = None
        self.ClusterType = None
        self.ApplicationPackageVersion = None
        self.ApplicationType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Port = params.get("Port")
        self.LanIp = params.get("LanIp")
        self.WanIp = params.get("WanIp")
        self.InstanceAvailableStatus = params.get("InstanceAvailableStatus")
        self.ServiceInstanceStatus = params.get("ServiceInstanceStatus")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.InstanceStatus = params.get("InstanceStatus")
        self.HealthCheckUrl = params.get("HealthCheckUrl")
        self.ClusterType = params.get("ClusterType")
        self.ApplicationPackageVersion = params.get("ApplicationPackageVersion")
        self.ApplicationType = params.get("ApplicationType")


class Namespace(AbstractModel):
    """命名空间

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceCode: 命名空间编码
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceCode: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param NamespaceDesc: 命名空间描述
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceDesc: str
        :param IsDefault: 默认命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: str
        :param NamespaceStatus: 命名空间状态
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceStatus: str
        :param DeleteFlag: 删除标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteFlag: bool
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ClusterList: 集群数组，仅携带集群ID，集群名称，集群类型等基础信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterList: list of Cluster
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param NamespaceResourceType: 集群资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceResourceType: str
        :param NamespaceType: 命名空间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceType: str
        """
        self.NamespaceId = None
        self.NamespaceCode = None
        self.NamespaceName = None
        self.NamespaceDesc = None
        self.IsDefault = None
        self.NamespaceStatus = None
        self.DeleteFlag = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ClusterList = None
        self.ClusterId = None
        self.NamespaceResourceType = None
        self.NamespaceType = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceCode = params.get("NamespaceCode")
        self.NamespaceName = params.get("NamespaceName")
        self.NamespaceDesc = params.get("NamespaceDesc")
        self.IsDefault = params.get("IsDefault")
        self.NamespaceStatus = params.get("NamespaceStatus")
        self.DeleteFlag = params.get("DeleteFlag")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = Cluster()
                obj._deserialize(item)
                self.ClusterList.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.NamespaceResourceType = params.get("NamespaceResourceType")
        self.NamespaceType = params.get("NamespaceType")


class OperationInfo(AbstractModel):
    """提供给前端，控制按钮是否显示

    """

    def __init__(self):
        """
        :param Init: 初始化按钮的控制信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Init: :class:`tencentcloud.tsf.v20180326.models.OperationInfoDetail`
        :param AddInstance: 添加实例按钮的控制信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AddInstance: :class:`tencentcloud.tsf.v20180326.models.OperationInfoDetail`
        :param Destroy: 销毁机器的控制信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Destroy: :class:`tencentcloud.tsf.v20180326.models.OperationInfoDetail`
        """
        self.Init = None
        self.AddInstance = None
        self.Destroy = None


    def _deserialize(self, params):
        if params.get("Init") is not None:
            self.Init = OperationInfoDetail()
            self.Init._deserialize(params.get("Init"))
        if params.get("AddInstance") is not None:
            self.AddInstance = OperationInfoDetail()
            self.AddInstance._deserialize(params.get("AddInstance"))
        if params.get("Destroy") is not None:
            self.Destroy = OperationInfoDetail()
            self.Destroy._deserialize(params.get("Destroy"))


class OperationInfoDetail(AbstractModel):
    """提供给前端控制按钮显示逻辑的字段

    """

    def __init__(self):
        """
        :param DisabledReason: 不显示的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type DisabledReason: str
        :param Enabled: 该按钮是否可点击
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        :param Supported: 是否显示该按钮
注意：此字段可能返回 null，表示取不到有效值。
        :type Supported: bool
        """
        self.DisabledReason = None
        self.Enabled = None
        self.Supported = None


    def _deserialize(self, params):
        self.DisabledReason = params.get("DisabledReason")
        self.Enabled = params.get("Enabled")
        self.Supported = params.get("Supported")


class PkgInfo(AbstractModel):
    """包信息

    """

    def __init__(self):
        """
        :param PkgId: 程序包ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param PkgName: 程序包名
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgName: str
        :param PkgType: 程序包类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgType: str
        :param PkgVersion: 程序包版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgVersion: str
        :param PkgDesc: 程序包描述
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgDesc: str
        :param UploadTime: 上传时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadTime: str
        :param Md5: 程序包MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param PkgPubStatus: 程序包状态
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgPubStatus: int
        """
        self.PkgId = None
        self.PkgName = None
        self.PkgType = None
        self.PkgVersion = None
        self.PkgDesc = None
        self.UploadTime = None
        self.Md5 = None
        self.PkgPubStatus = None


    def _deserialize(self, params):
        self.PkgId = params.get("PkgId")
        self.PkgName = params.get("PkgName")
        self.PkgType = params.get("PkgType")
        self.PkgVersion = params.get("PkgVersion")
        self.PkgDesc = params.get("PkgDesc")
        self.UploadTime = params.get("UploadTime")
        self.Md5 = params.get("Md5")
        self.PkgPubStatus = params.get("PkgPubStatus")


class PkgList(AbstractModel):
    """包列表

    """

    def __init__(self):
        """
        :param TotalCount: 程序包总量
        :type TotalCount: int
        :param Content: 程序包信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of PkgInfo
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = PkgInfo()
                obj._deserialize(item)
                self.Content.append(obj)


class ProtocolPort(AbstractModel):
    """端口对象

    """

    def __init__(self):
        """
        :param Protocol: TCP UDP
        :type Protocol: str
        :param Port: 服务端口
        :type Port: int
        :param TargetPort: 容器端口
        :type TargetPort: int
        :param NodePort: 主机端口
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePort: int
        """
        self.Protocol = None
        self.Port = None
        self.TargetPort = None
        self.NodePort = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.TargetPort = params.get("TargetPort")
        self.NodePort = params.get("NodePort")


class ReleaseConfigRequest(AbstractModel):
    """ReleaseConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置ID
        :type ConfigId: str
        :param GroupId: 部署组ID
        :type GroupId: str
        :param ReleaseDesc: 发布描述
        :type ReleaseDesc: str
        """
        self.ConfigId = None
        self.GroupId = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.GroupId = params.get("GroupId")
        self.ReleaseDesc = params.get("ReleaseDesc")


class ReleaseConfigResponse(AbstractModel):
    """ReleaseConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：发布成功；false：发布失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ReleasePublicConfigRequest(AbstractModel):
    """ReleasePublicConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置ID
        :type ConfigId: str
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param ReleaseDesc: 发布描述
        :type ReleaseDesc: str
        """
        self.ConfigId = None
        self.NamespaceId = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.NamespaceId = params.get("NamespaceId")
        self.ReleaseDesc = params.get("ReleaseDesc")


class ReleasePublicConfigResponse(AbstractModel):
    """ReleasePublicConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：发布成功；false：发布失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RemoveInstancesRequest(AbstractModel):
    """RemoveInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID
        :type ClusterId: str
        :param InstanceIdList: 云主机 ID 列表
        :type InstanceIdList: list of str
        """
        self.ClusterId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")


class RemoveInstancesResponse(AbstractModel):
    """RemoveInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 集群移除机器是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RevocationConfigRequest(AbstractModel):
    """RevocationConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigReleaseId: 配置项发布ID
        :type ConfigReleaseId: str
        """
        self.ConfigReleaseId = None


    def _deserialize(self, params):
        self.ConfigReleaseId = params.get("ConfigReleaseId")


class RevocationConfigResponse(AbstractModel):
    """RevocationConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：回滚成功；false：回滚失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RevocationPublicConfigRequest(AbstractModel):
    """RevocationPublicConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigReleaseId: 配置项发布ID
        :type ConfigReleaseId: str
        """
        self.ConfigReleaseId = None


    def _deserialize(self, params):
        self.ConfigReleaseId = params.get("ConfigReleaseId")


class RevocationPublicConfigResponse(AbstractModel):
    """RevocationPublicConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：撤销成功；false：撤销失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RollbackConfigRequest(AbstractModel):
    """RollbackConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigReleaseLogId: 配置项发布历史ID
        :type ConfigReleaseLogId: str
        :param ReleaseDesc: 回滚描述
        :type ReleaseDesc: str
        """
        self.ConfigReleaseLogId = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigReleaseLogId = params.get("ConfigReleaseLogId")
        self.ReleaseDesc = params.get("ReleaseDesc")


class RollbackConfigResponse(AbstractModel):
    """RollbackConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：回滚成功；false：回滚失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ServerlessGroup(AbstractModel):
    """Serverless部署组信息

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Status: 服务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param PkgId: 程序包ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param PkgName: 程序包名
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgName: str
        :param ClusterId: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NamespaceId: 命名空间id
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param VpcId: vpc ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: vpc 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param PkgVersion: 程序包版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgVersion: str
        :param Memory: 所需实例内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: str
        :param InstanceRequest: 要求最小实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceRequest: int
        :param StartupParameters: 部署组启动参数
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupParameters: str
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param InstanceCount: 部署组实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: list of str
        """
        self.GroupId = None
        self.GroupName = None
        self.CreateTime = None
        self.Status = None
        self.PkgId = None
        self.PkgName = None
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.VpcId = None
        self.SubnetId = None
        self.PkgVersion = None
        self.Memory = None
        self.InstanceRequest = None
        self.StartupParameters = None
        self.ApplicationId = None
        self.InstanceCount = None
        self.ApplicationName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.PkgId = params.get("PkgId")
        self.PkgName = params.get("PkgName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PkgVersion = params.get("PkgVersion")
        self.Memory = params.get("Memory")
        self.InstanceRequest = params.get("InstanceRequest")
        self.StartupParameters = params.get("StartupParameters")
        self.ApplicationId = params.get("ApplicationId")
        self.InstanceCount = params.get("InstanceCount")
        self.ApplicationName = params.get("ApplicationName")


class ServerlessGroupPage(AbstractModel):
    """ServerlessGroup 翻页对象

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of ServerlessGroup
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ServerlessGroup()
                obj._deserialize(item)
                self.Content.append(obj)


class ShrinkGroupRequest(AbstractModel):
    """ShrinkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class ShrinkGroupResponse(AbstractModel):
    """ShrinkGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ShrinkInstancesRequest(AbstractModel):
    """ShrinkInstances请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        :param InstanceIdList: 下线机器实例ID列表
        :type InstanceIdList: list of str
        """
        self.GroupId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.InstanceIdList = params.get("InstanceIdList")


class ShrinkInstancesResponse(AbstractModel):
    """ShrinkInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class SimpleApplication(AbstractModel):
    """简单应用

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param MicroserviceType: 应用微服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param ApplicationDesc: ApplicationDesc
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationDesc: str
        :param ProgLang: ProgLang
注意：此字段可能返回 null，表示取不到有效值。
        :type ProgLang: str
        :param ApplicationResourceType: ApplicationResourceType
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationResourceType: str
        :param CreateTime: CreateTime
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: UpdateTime
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ApigatewayServiceId: ApigatewayServiceId
注意：此字段可能返回 null，表示取不到有效值。
        :type ApigatewayServiceId: str
        :param ApplicationRuntimeType: ApplicationRuntimeType
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationRuntimeType: str
        """
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ApplicationDesc = None
        self.ProgLang = None
        self.ApplicationResourceType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ApigatewayServiceId = None
        self.ApplicationRuntimeType = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationDesc = params.get("ApplicationDesc")
        self.ProgLang = params.get("ProgLang")
        self.ApplicationResourceType = params.get("ApplicationResourceType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ApigatewayServiceId = params.get("ApigatewayServiceId")
        self.ApplicationRuntimeType = params.get("ApplicationRuntimeType")


class SimpleGroup(AbstractModel):
    """部署组

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param StartupParameters: 启动参数
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupParameters: str
        :param GroupResourceType: 部署组资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupResourceType: str
        :param AppMicroServiceType: 应用微服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AppMicroServiceType: str
        """
        self.GroupId = None
        self.GroupName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationType = None
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterType = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.StartupParameters = None
        self.GroupResourceType = None
        self.AppMicroServiceType = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterType = params.get("ClusterType")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.StartupParameters = params.get("StartupParameters")
        self.GroupResourceType = params.get("GroupResourceType")
        self.AppMicroServiceType = params.get("AppMicroServiceType")


class StartContainerGroupRequest(AbstractModel):
    """StartContainerGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class StartContainerGroupResponse(AbstractModel):
    """StartContainerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 启动操作是否成功。
true：启动成功
false：启动失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class StartGroupRequest(AbstractModel):
    """StartGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class StartGroupResponse(AbstractModel):
    """StartGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class StopContainerGroupRequest(AbstractModel):
    """StopContainerGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class StopContainerGroupResponse(AbstractModel):
    """StopContainerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 停止操作是否成功。
true：停止成功
flase：停止失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class StopGroupRequest(AbstractModel):
    """StopGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class StopGroupResponse(AbstractModel):
    """StopGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class TaskId(AbstractModel):
    """任务id

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class TsfPageApplication(AbstractModel):
    """应用分页信息

    """

    def __init__(self):
        """
        :param TotalCount: 应用总数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 应用信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of ApplicationForPage
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ApplicationForPage()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageCluster(AbstractModel):
    """Tsf分页集群对象

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 集群列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of Cluster
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Cluster()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageConfig(AbstractModel):
    """TsfPage<Config>

    """

    def __init__(self):
        """
        :param TotalCount: TsfPageConfig
        :type TotalCount: int
        :param Content: 配置项列表
        :type Content: list of Config
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Config()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageConfigRelease(AbstractModel):
    """TSF配置项发布信息分页对象

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 配置项发布信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of ConfigRelease
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ConfigRelease()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageConfigReleaseLog(AbstractModel):
    """TSF配置项发布日志分页对象

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 配置项发布日志数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of ConfigReleaseLog
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ConfigReleaseLog()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageInstance(AbstractModel):
    """TSF机器实例分页对象

    """

    def __init__(self):
        """
        :param TotalCount: 机器实例总数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 机器实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of Instance
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Instance()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageMicroservice(AbstractModel):
    """微服务列表信息

    """

    def __init__(self):
        """
        :param TotalCount: 微服务总数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 微服务列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of Microservice
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Microservice()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageMsInstance(AbstractModel):
    """微服务实例的分页内容

    """

    def __init__(self):
        """
        :param TotalCount: 微服务实例总数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 微服务实例列表内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of MsInstance
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = MsInstance()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageNamespace(AbstractModel):
    """Tsf命名空间分页对象

    """

    def __init__(self):
        """
        :param TotalCount: 命名空间总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 命名空间列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of Namespace
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Namespace()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageSimpleApplication(AbstractModel):
    """TSF分页简单应用对象

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 简单应用列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of SimpleApplication
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = SimpleApplication()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageSimpleGroup(AbstractModel):
    """TSF简单部署组分页列表

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 简单部署组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of SimpleGroup
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = SimpleGroup()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageVmGroup(AbstractModel):
    """列表中部署组分页信息

    """

    def __init__(self):
        """
        :param TotalCount: 虚拟机部署组总数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 虚拟机部署组列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of VmGroupSimple
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = VmGroupSimple()
                obj._deserialize(item)
                self.Content.append(obj)


class VmGroup(AbstractModel):
    """虚拟机部署组信息

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param GroupStatus: 部署组状态
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupStatus: str
        :param PackageId: 程序包ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param PackageName: 程序包名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param PackageVersion: 程序包版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param InstanceCount: 部署组机器数目
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param RunInstanceCount: 部署组运行中机器数目
注意：此字段可能返回 null，表示取不到有效值。
        :type RunInstanceCount: int
        :param StartupParameters: 部署组启动参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupParameters: str
        :param CreateTime: 部署组创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 部署组更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param OffInstanceCount: 部署组停止机器数目
注意：此字段可能返回 null，表示取不到有效值。
        :type OffInstanceCount: int
        :param GroupDesc: 部署组描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupDesc: str
        :param MicroserviceType: 微服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param GroupResourceType: 部署组资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupResourceType: str
        :param UpdatedTime: 部署组更新时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: int
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupStatus = None
        self.PackageId = None
        self.PackageName = None
        self.PackageVersion = None
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.InstanceCount = None
        self.RunInstanceCount = None
        self.StartupParameters = None
        self.CreateTime = None
        self.UpdateTime = None
        self.OffInstanceCount = None
        self.GroupDesc = None
        self.MicroserviceType = None
        self.ApplicationType = None
        self.GroupResourceType = None
        self.UpdatedTime = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupStatus = params.get("GroupStatus")
        self.PackageId = params.get("PackageId")
        self.PackageName = params.get("PackageName")
        self.PackageVersion = params.get("PackageVersion")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.InstanceCount = params.get("InstanceCount")
        self.RunInstanceCount = params.get("RunInstanceCount")
        self.StartupParameters = params.get("StartupParameters")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.OffInstanceCount = params.get("OffInstanceCount")
        self.GroupDesc = params.get("GroupDesc")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationType = params.get("ApplicationType")
        self.GroupResourceType = params.get("GroupResourceType")
        self.UpdatedTime = params.get("UpdatedTime")


class VmGroupSimple(AbstractModel):
    """虚拟机部署组列表简要字段

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param GroupDesc: 部署组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupDesc: str
        :param UpdateTime: 部署组更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param StartupParameters: 部署组启动参数
注意：此字段可能返回 null，表示取不到有效值。
        :type StartupParameters: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param CreateTime: 部署组创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param MicroserviceType: 应用微服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param GroupResourceType: 部署组资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupResourceType: str
        :param UpdatedTime: 部署组更新时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: int
        """
        self.GroupId = None
        self.GroupName = None
        self.ApplicationType = None
        self.GroupDesc = None
        self.UpdateTime = None
        self.ClusterId = None
        self.StartupParameters = None
        self.NamespaceId = None
        self.CreateTime = None
        self.ClusterName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.NamespaceName = None
        self.MicroserviceType = None
        self.GroupResourceType = None
        self.UpdatedTime = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ApplicationType = params.get("ApplicationType")
        self.GroupDesc = params.get("GroupDesc")
        self.UpdateTime = params.get("UpdateTime")
        self.ClusterId = params.get("ClusterId")
        self.StartupParameters = params.get("StartupParameters")
        self.NamespaceId = params.get("NamespaceId")
        self.CreateTime = params.get("CreateTime")
        self.ClusterName = params.get("ClusterName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.NamespaceName = params.get("NamespaceName")
        self.MicroserviceType = params.get("MicroserviceType")
        self.GroupResourceType = params.get("GroupResourceType")
        self.UpdatedTime = params.get("UpdatedTime")