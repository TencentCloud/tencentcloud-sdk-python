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
        :param KeyId: 重装系统，关联秘钥设置
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
        """
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationDesc = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ProgLang = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationDesc = params.get("ApplicationDesc")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ProgLang = params.get("ProgLang")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


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
        :param ApplicationType: 应用类型
        :type ApplicationType: str
        :param ApplicationDesc: 应用描述
        :type ApplicationDesc: str
        :param ApplicationLogConfig: 应用日志配置项，废弃参数
        :type ApplicationLogConfig: str
        :param MicroserviceType: 应用微服务类型
        :type MicroserviceType: str
        """
        self.ApplicationName = None
        self.ApplicationType = None
        self.ApplicationDesc = None
        self.ApplicationLogConfig = None
        self.MicroserviceType = None


    def _deserialize(self, params):
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.ApplicationDesc = params.get("ApplicationDesc")
        self.ApplicationLogConfig = params.get("ApplicationLogConfig")
        self.MicroserviceType = params.get("MicroserviceType")


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
        """
        self.ClusterName = None
        self.ClusterType = None
        self.VpcId = None
        self.ClusterCIDR = None
        self.ClusterDesc = None
        self.TsfRegionId = None
        self.TsfZoneId = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.ClusterType = params.get("ClusterType")
        self.VpcId = params.get("VpcId")
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.ClusterDesc = params.get("ClusterDesc")
        self.TsfRegionId = params.get("TsfRegionId")
        self.TsfZoneId = params.get("TsfZoneId")


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建集群操作是否成功。
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
        """
        self.ApplicationId = None
        self.NamespaceId = None
        self.GroupName = None
        self.ClusterId = None
        self.GroupDesc = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupName = params.get("GroupName")
        self.ClusterId = params.get("ClusterId")
        self.GroupDesc = params.get("GroupDesc")


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
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param NamespaceDesc: 命名空间描述
        :type NamespaceDesc: str
        """
        self.ClusterId = None
        self.NamespaceName = None
        self.NamespaceDesc = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceName = params.get("NamespaceName")
        self.NamespaceDesc = params.get("NamespaceDesc")


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建命名空间是否成功。
true：创建成功。
false：创建失败。
        :type Result: bool
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
        :param CpuLimit: 最大的 CPU 核数，对应 K8S 的 limit；不填时默认为 request 的 2 倍
        :type CpuLimit: str
        :param MemLimit: 最大的内存 MiB 数，对应 K8S 的 limit；不填时默认为 request 的 2 倍
        :type MemLimit: str
        :param JvmOpts: jvm参数
        :type JvmOpts: str
        :param CpuRequest: 分配的 CPU 核数，对应 K8S 的 request
        :type CpuRequest: str
        :param MemRequest: 分配的内存 MiB 数，对应 K8S 的 request
        :type MemRequest: str
        :param DoNotStart: 是否不立即启动
        :type DoNotStart: bool
        :param RepoName: （优先使用）新版镜像名，如/tsf/nginx
        :type RepoName: str
        :param UpdateType: 更新方式：0:快速更新 1:滚动更新
        :type UpdateType: int
        :param UpdateIvl: 滚动更新必填，更新间隔
        :type UpdateIvl: int
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
        """
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.ApplicationType = None
        self.MicroserviceType = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")


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
        """
        self.ApplicationId = None
        self.Offset = None
        self.Limit = None
        self.QueryImageIdFlag = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.QueryImageIdFlag = params.get("QueryImageIdFlag")


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
        """
        self.ApplicationIdList = None
        self.ApplicationType = None
        self.Limit = None
        self.Offset = None
        self.MicroserviceType = None


    def _deserialize(self, params):
        self.ApplicationIdList = params.get("ApplicationIdList")
        self.ApplicationType = params.get("ApplicationType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.MicroserviceType = params.get("MicroserviceType")


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
        """
        self.ClusterIdList = None
        self.ClusterType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterIdList = params.get("ClusterIdList")
        self.ClusterType = params.get("ClusterType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


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
        """
        self.GroupIdList = None
        self.ApplicationId = None
        self.ClusterId = None
        self.NamespaceId = None
        self.Limit = None
        self.Offset = None
        self.GroupId = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.GroupIdList = params.get("GroupIdList")
        self.ApplicationId = params.get("ApplicationId")
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.GroupId = params.get("GroupId")
        self.SearchWord = params.get("SearchWord")


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
        """
        self.NamespaceIdList = None
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.NamespaceIdList = params.get("NamespaceIdList")
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NamespaceId = params.get("NamespaceId")


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
        """
        self.Protocol = None
        self.Port = None
        self.TargetPort = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.TargetPort = params.get("TargetPort")


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
        """
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationType = None
        self.MicroserviceType = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")


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