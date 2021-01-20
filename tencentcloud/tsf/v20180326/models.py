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
        :param OsCustomizeType: 镜像定制类型
        :type OsCustomizeType: str
        :param FeatureIdList: 镜像特征ID列表
        :type FeatureIdList: list of str
        :param InstanceAdvancedSettings: 实例额外需要设置参数信息
        :type InstanceAdvancedSettings: :class:`tencentcloud.tsf.v20180326.models.InstanceAdvancedSettings`
        :param SecurityGroupIds: 部署组ID
        :type SecurityGroupIds: list of str
        """
        self.ClusterId = None
        self.InstanceIdList = None
        self.OsName = None
        self.ImageId = None
        self.Password = None
        self.KeyId = None
        self.SgId = None
        self.InstanceImportMode = None
        self.OsCustomizeType = None
        self.FeatureIdList = None
        self.InstanceAdvancedSettings = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        self.OsName = params.get("OsName")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        self.KeyId = params.get("KeyId")
        self.SgId = params.get("SgId")
        self.InstanceImportMode = params.get("InstanceImportMode")
        self.OsCustomizeType = params.get("OsCustomizeType")
        self.FeatureIdList = params.get("FeatureIdList")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")


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
        :param FailedReasons: 失败的节点的失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReasons: list of str
        """
        self.FailedInstanceIds = None
        self.SuccInstanceIds = None
        self.TimeoutInstanceIds = None
        self.FailedReasons = None


    def _deserialize(self, params):
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.TimeoutInstanceIds = params.get("TimeoutInstanceIds")
        self.FailedReasons = params.get("FailedReasons")


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


class AdvanceSettings(AbstractModel):
    """高级选项设置

    """

    def __init__(self):
        """
        :param SubTaskConcurrency: 子任务单机并发数限制，默认值为2
        :type SubTaskConcurrency: int
        """
        self.SubTaskConcurrency = None


    def _deserialize(self, params):
        self.SubTaskConcurrency = params.get("SubTaskConcurrency")


class ApiDefinitionDescr(AbstractModel):
    """API 对象类型描述

    """

    def __init__(self):
        """
        :param Name: 对象名称
        :type Name: str
        :param Properties: 对象属性列表
        :type Properties: list of PropertyField
        """
        self.Name = None
        self.Properties = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = PropertyField()
                obj._deserialize(item)
                self.Properties.append(obj)


class ApiDetailInfo(AbstractModel):
    """API 明细

    """

    def __init__(self):
        """
        :param ApiId: API ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param MicroserviceId: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceId: str
        :param MicroserviceName: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceName: str
        :param Path: API 请求路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param PathMapping: Api 映射路径
注意：此字段可能返回 null，表示取不到有效值。
        :type PathMapping: str
        :param Method: 请求方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param GroupId: 所属分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param UsableStatus: 是否禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type UsableStatus: str
        :param ReleaseStatus: 发布状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseStatus: str
        :param RateLimitStatus: 开启限流
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitStatus: str
        :param MockStatus: 是否开启mock
注意：此字段可能返回 null，表示取不到有效值。
        :type MockStatus: str
        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param UpdatedTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        :param ReleasedTime: 发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleasedTime: str
        :param GroupName: 所属分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param Timeout: API 超时，单位毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param Host: Api所在服务host
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param ApiType: API类型。 ms ： 微服务API； external :外部服务Api
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiType: str
        :param Description: Api描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self.ApiId = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.MicroserviceId = None
        self.MicroserviceName = None
        self.Path = None
        self.PathMapping = None
        self.Method = None
        self.GroupId = None
        self.UsableStatus = None
        self.ReleaseStatus = None
        self.RateLimitStatus = None
        self.MockStatus = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.ReleasedTime = None
        self.GroupName = None
        self.Timeout = None
        self.Host = None
        self.ApiType = None
        self.Description = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.MicroserviceId = params.get("MicroserviceId")
        self.MicroserviceName = params.get("MicroserviceName")
        self.Path = params.get("Path")
        self.PathMapping = params.get("PathMapping")
        self.Method = params.get("Method")
        self.GroupId = params.get("GroupId")
        self.UsableStatus = params.get("UsableStatus")
        self.ReleaseStatus = params.get("ReleaseStatus")
        self.RateLimitStatus = params.get("RateLimitStatus")
        self.MockStatus = params.get("MockStatus")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.ReleasedTime = params.get("ReleasedTime")
        self.GroupName = params.get("GroupName")
        self.Timeout = params.get("Timeout")
        self.Host = params.get("Host")
        self.ApiType = params.get("ApiType")
        self.Description = params.get("Description")


class ApiDetailResponse(AbstractModel):
    """ApiDetailResponse描述

    """

    def __init__(self):
        """
        :param Request: API 请求参数
        :type Request: list of ApiRequestDescr
        :param Response: API 响应参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Response: list of ApiResponseDescr
        :param Definitions: API 复杂结构定义
        :type Definitions: list of ApiDefinitionDescr
        :param RequestContentType: API 的 content type
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestContentType: str
        :param CanRun: API  能否调试
注意：此字段可能返回 null，表示取不到有效值。
        :type CanRun: bool
        :param Status: API 状态 0:离线 1:在线，默认0
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Description: API 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self.Request = None
        self.Response = None
        self.Definitions = None
        self.RequestContentType = None
        self.CanRun = None
        self.Status = None
        self.Description = None


    def _deserialize(self, params):
        if params.get("Request") is not None:
            self.Request = []
            for item in params.get("Request"):
                obj = ApiRequestDescr()
                obj._deserialize(item)
                self.Request.append(obj)
        if params.get("Response") is not None:
            self.Response = []
            for item in params.get("Response"):
                obj = ApiResponseDescr()
                obj._deserialize(item)
                self.Response.append(obj)
        if params.get("Definitions") is not None:
            self.Definitions = []
            for item in params.get("Definitions"):
                obj = ApiDefinitionDescr()
                obj._deserialize(item)
                self.Definitions.append(obj)
        self.RequestContentType = params.get("RequestContentType")
        self.CanRun = params.get("CanRun")
        self.Status = params.get("Status")
        self.Description = params.get("Description")


class ApiGroupInfo(AbstractModel):
    """API分组信息

    """

    def __init__(self):
        """
        :param GroupId: Api Group Id
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: Api Group 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param GroupContext: 分组上下文
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupContext: str
        :param AuthType: 鉴权类型。 secret： 密钥鉴权； none:无鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param Status: 发布状态, drafted: 未发布。 released: 发布
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param CreatedTime: 分组创建时间 如:2019-06-20 15:51:28
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param UpdatedTime: 分组更新时间 如:2019-06-20 15:51:28
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        :param BindedGatewayDeployGroups: api分组已绑定的网关部署组
注意：此字段可能返回 null，表示取不到有效值。
        :type BindedGatewayDeployGroups: list of GatewayDeployGroup
        :param ApiCount: api 个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiCount: int
        :param AclMode: 访问group的ACL类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AclMode: str
        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param GroupType: 分组类型。 ms： 微服务分组； external:外部Api分组
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupType: str
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupContext = None
        self.AuthType = None
        self.Status = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.BindedGatewayDeployGroups = None
        self.ApiCount = None
        self.AclMode = None
        self.Description = None
        self.GroupType = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupContext = params.get("GroupContext")
        self.AuthType = params.get("AuthType")
        self.Status = params.get("Status")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        if params.get("BindedGatewayDeployGroups") is not None:
            self.BindedGatewayDeployGroups = []
            for item in params.get("BindedGatewayDeployGroups"):
                obj = GatewayDeployGroup()
                obj._deserialize(item)
                self.BindedGatewayDeployGroups.append(obj)
        self.ApiCount = params.get("ApiCount")
        self.AclMode = params.get("AclMode")
        self.Description = params.get("Description")
        self.GroupType = params.get("GroupType")


class ApiInfo(AbstractModel):
    """微服务网关API信息

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间Id，若为外部API,为固定值："namespace-external"
        :type NamespaceId: str
        :param MicroserviceId: 服务Id，若为外部API,为固定值："ms-external"
        :type MicroserviceId: str
        :param Path: API path
        :type Path: str
        :param Method: Api 请求
        :type Method: str
        :param PathMapping: 请求映射
        :type PathMapping: str
        :param Host: api所在服务host,限定外部Api填写。格式: `http://127.0.0.1:8080`
        :type Host: str
        :param Description: api描述信息
        :type Description: str
        """
        self.NamespaceId = None
        self.MicroserviceId = None
        self.Path = None
        self.Method = None
        self.PathMapping = None
        self.Host = None
        self.Description = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.MicroserviceId = params.get("MicroserviceId")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.PathMapping = params.get("PathMapping")
        self.Host = params.get("Host")
        self.Description = params.get("Description")


class ApiRateLimitRule(AbstractModel):
    """微服务网关API限流规则

    """

    def __init__(self):
        """
        :param RuleId: rule Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param ApiId: API ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param RuleName: 限流名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param MaxQps: 最大限流qps
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxQps: int
        :param UsableStatus: 生效/禁用, enabled/disabled
注意：此字段可能返回 null，表示取不到有效值。
        :type UsableStatus: str
        :param RuleContent: 规则内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleContent: str
        :param TsfRuleId: Tsf Rule ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TsfRuleId: str
        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param UpdatedTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        """
        self.RuleId = None
        self.ApiId = None
        self.RuleName = None
        self.MaxQps = None
        self.UsableStatus = None
        self.RuleContent = None
        self.TsfRuleId = None
        self.Description = None
        self.CreatedTime = None
        self.UpdatedTime = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ApiId = params.get("ApiId")
        self.RuleName = params.get("RuleName")
        self.MaxQps = params.get("MaxQps")
        self.UsableStatus = params.get("UsableStatus")
        self.RuleContent = params.get("RuleContent")
        self.TsfRuleId = params.get("TsfRuleId")
        self.Description = params.get("Description")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")


class ApiRequestDescr(AbstractModel):
    """ApiRequestDescr

    """

    def __init__(self):
        """
        :param Name: 参数名称
        :type Name: str
        :param Type: 参数类型
        :type Type: str
        :param In: 参数位置
        :type In: str
        :param Description: 参数描述
        :type Description: str
        :param Required: 参数是否必须
        :type Required: bool
        :param DefaultValue: 参数的默认值
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        """
        self.Name = None
        self.Type = None
        self.In = None
        self.Description = None
        self.Required = None
        self.DefaultValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.In = params.get("In")
        self.Description = params.get("Description")
        self.Required = params.get("Required")
        self.DefaultValue = params.get("DefaultValue")


class ApiResponseDescr(AbstractModel):
    """API 响应的参数结构描述

    """

    def __init__(self):
        """
        :param Name: 参数描述
        :type Name: str
        :param Type: 参数类型
        :type Type: str
        :param Description: 参数描述
        :type Description: str
        """
        self.Name = None
        self.Type = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Description = params.get("Description")


class ApiUseStatisticsEntity(AbstractModel):
    """API 日统计数据点

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Count: 次数
        :type Count: str
        :param Ratio: 比率
        :type Ratio: str
        """
        self.Name = None
        self.Count = None
        self.Ratio = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Count = params.get("Count")
        self.Ratio = params.get("Ratio")


class ApiVersionArray(AbstractModel):
    """API版本数组

    """

    def __init__(self):
        """
        :param ApplicationId: App ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: App 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param PkgVersion: App 包版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgVersion: str
        """
        self.ApplicationId = None
        self.ApplicationName = None
        self.PkgVersion = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.PkgVersion = params.get("PkgVersion")


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
        :param ApplicationRemarkName: 应用备注名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationRemarkName: str
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
        self.ApplicationRemarkName = None


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
        self.ApplicationRemarkName = params.get("ApplicationRemarkName")


class BindApiGroupRequest(AbstractModel):
    """BindApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupGatewayList: 分组绑定网关列表
        :type GroupGatewayList: list of GatewayGroupIds
        """
        self.GroupGatewayList = None


    def _deserialize(self, params):
        if params.get("GroupGatewayList") is not None:
            self.GroupGatewayList = []
            for item in params.get("GroupGatewayList"):
                obj = GatewayGroupIds()
                obj._deserialize(item)
                self.GroupGatewayList.append(obj)


class BindApiGroupResponse(AbstractModel):
    """BindApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，成功失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ChangeApiUsableStatusRequest(AbstractModel):
    """ChangeApiUsableStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ApiId: API ID
        :type ApiId: str
        :param UsableStatus: 切换状态，enabled/disabled
        :type UsableStatus: str
        """
        self.ApiId = None
        self.UsableStatus = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.UsableStatus = params.get("UsableStatus")


class ChangeApiUsableStatusResponse(AbstractModel):
    """ChangeApiUsableStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API 信息
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApiDetailInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiDetailInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


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
        :param ClusterVersion: 集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterVersion: str
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
        self.ClusterVersion = None


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
        self.ClusterVersion = params.get("ClusterVersion")


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
        :param MaxSurge: kubernetes滚动更新策略的MaxSurge参数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSurge: str
        :param MaxUnavailable: kubernetes滚动更新策略的MaxUnavailable参数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxUnavailable: str
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
        self.MaxSurge = None
        self.MaxUnavailable = None


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
        self.MaxSurge = params.get("MaxSurge")
        self.MaxUnavailable = params.get("MaxUnavailable")


class ContinueRunFailedTaskBatchRequest(AbstractModel):
    """ContinueRunFailedTaskBatch请求参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 批次ID。
        :type BatchId: str
        """
        self.BatchId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")


class ContinueRunFailedTaskBatchResponse(AbstractModel):
    """ContinueRunFailedTaskBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功或失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


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


class CreateAllGatewayApiAsyncRequest(AbstractModel):
    """CreateAllGatewayApiAsync请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: API分组ID
        :type GroupId: str
        :param MicroserviceId: 微服务ID
        :type MicroserviceId: str
        """
        self.GroupId = None
        self.MicroserviceId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.MicroserviceId = params.get("MicroserviceId")


class CreateAllGatewayApiAsyncResponse(AbstractModel):
    """CreateAllGatewayApiAsync返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateApiGroupRequest(AbstractModel):
    """CreateApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 分组名称, 不能包含中文
        :type GroupName: str
        :param GroupContext: 分组上下文
        :type GroupContext: str
        :param AuthType: 鉴权类型。secret： 密钥鉴权； none:无鉴权
        :type AuthType: str
        :param Description: 备注
        :type Description: str
        :param GroupType: 分组类型,默认ms。 ms： 微服务分组； external:外部Api分组
        :type GroupType: str
        """
        self.GroupName = None
        self.GroupContext = None
        self.AuthType = None
        self.Description = None
        self.GroupType = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupContext = params.get("GroupContext")
        self.AuthType = params.get("AuthType")
        self.Description = params.get("Description")
        self.GroupType = params.get("GroupType")


class CreateApiGroupResponse(AbstractModel):
    """CreateApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API分组ID
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


class CreateApiRateLimitRuleRequest(AbstractModel):
    """CreateApiRateLimitRule请求参数结构体

    """

    def __init__(self):
        """
        :param ApiId: Api Id
        :type ApiId: str
        :param MaxQps: qps值
        :type MaxQps: int
        :param UsableStatus: 开启/禁用，enabled/disabled, 不传默认开启
        :type UsableStatus: str
        """
        self.ApiId = None
        self.MaxQps = None
        self.UsableStatus = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.MaxQps = params.get("MaxQps")
        self.UsableStatus = params.get("UsableStatus")


class CreateApiRateLimitRuleResponse(AbstractModel):
    """CreateApiRateLimitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


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
        :param ProgramId: 需要绑定的数据集ID
        :type ProgramId: str
        """
        self.ApplicationName = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ApplicationDesc = None
        self.ApplicationLogConfig = None
        self.ApplicationResourceType = None
        self.ApplicationRuntimeType = None
        self.ProgramId = None


    def _deserialize(self, params):
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationDesc = params.get("ApplicationDesc")
        self.ApplicationLogConfig = params.get("ApplicationLogConfig")
        self.ApplicationResourceType = params.get("ApplicationResourceType")
        self.ApplicationRuntimeType = params.get("ApplicationRuntimeType")
        self.ProgramId = params.get("ProgramId")


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
        :param ClusterVersion: 集群版本
        :type ClusterVersion: str
        :param MaxNodePodNum: 集群中每个Node上最大的Pod数量。取值范围4～256。不为2的幂值时会向上取最接近的2的幂值。
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: 集群最大的service数量。取值范围32～32768，不为2的幂值时会向上取最接近的2的幂值。
        :type MaxClusterServiceNum: int
        :param ProgramId: 需要绑定的数据集ID
        :type ProgramId: str
        """
        self.ClusterName = None
        self.ClusterType = None
        self.VpcId = None
        self.ClusterCIDR = None
        self.ClusterDesc = None
        self.TsfRegionId = None
        self.TsfZoneId = None
        self.SubnetId = None
        self.ClusterVersion = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.ProgramId = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.ClusterType = params.get("ClusterType")
        self.VpcId = params.get("VpcId")
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.ClusterDesc = params.get("ClusterDesc")
        self.TsfRegionId = params.get("TsfRegionId")
        self.TsfZoneId = params.get("TsfZoneId")
        self.SubnetId = params.get("SubnetId")
        self.ClusterVersion = params.get("ClusterVersion")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.ProgramId = params.get("ProgramId")


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


class CreateGatewayApiRequest(AbstractModel):
    """CreateGatewayApi请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: API 分组ID
        :type GroupId: str
        :param ApiList: Api信息
        :type ApiList: list of ApiInfo
        """
        self.GroupId = None
        self.ApiList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        if params.get("ApiList") is not None:
            self.ApiList = []
            for item in params.get("ApiList"):
                obj = ApiInfo()
                obj._deserialize(item)
                self.ApiList.append(obj)


class CreateGatewayApiResponse(AbstractModel):
    """CreateGatewayApi返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
        :type Result: bool
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


class CreateLaneRequest(AbstractModel):
    """CreateLane请求参数结构体

    """

    def __init__(self):
        """
        :param LaneName: 泳道名称
        :type LaneName: str
        :param Remark: 泳道备注
        :type Remark: str
        :param LaneGroupList: 泳道部署组信息
        :type LaneGroupList: list of LaneGroup
        """
        self.LaneName = None
        self.Remark = None
        self.LaneGroupList = None


    def _deserialize(self, params):
        self.LaneName = params.get("LaneName")
        self.Remark = params.get("Remark")
        if params.get("LaneGroupList") is not None:
            self.LaneGroupList = []
            for item in params.get("LaneGroupList"):
                obj = LaneGroup()
                obj._deserialize(item)
                self.LaneGroupList.append(obj)


class CreateLaneResponse(AbstractModel):
    """CreateLane返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 泳道ID
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


class CreateLaneRuleRequest(AbstractModel):
    """CreateLaneRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 泳道规则名称
        :type RuleName: str
        :param Remark: 泳道规则备注
        :type Remark: str
        :param RuleTagList: 泳道规则标签列表
        :type RuleTagList: list of LaneRuleTag
        :param RuleTagRelationship: 泳道规则标签关系
        :type RuleTagRelationship: str
        :param LaneId: 泳道Id
        :type LaneId: str
        """
        self.RuleName = None
        self.Remark = None
        self.RuleTagList = None
        self.RuleTagRelationship = None
        self.LaneId = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Remark = params.get("Remark")
        if params.get("RuleTagList") is not None:
            self.RuleTagList = []
            for item in params.get("RuleTagList"):
                obj = LaneRuleTag()
                obj._deserialize(item)
                self.RuleTagList.append(obj)
        self.RuleTagRelationship = params.get("RuleTagRelationship")
        self.LaneId = params.get("LaneId")


class CreateLaneRuleResponse(AbstractModel):
    """CreateLaneRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 泳道规则Id
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
        :param IsHaEnable: 是否开启高可用
        :type IsHaEnable: str
        :param ProgramId: 需要绑定的数据集ID
        :type ProgramId: str
        """
        self.NamespaceName = None
        self.ClusterId = None
        self.NamespaceDesc = None
        self.NamespaceResourceType = None
        self.NamespaceType = None
        self.NamespaceId = None
        self.IsHaEnable = None
        self.ProgramId = None


    def _deserialize(self, params):
        self.NamespaceName = params.get("NamespaceName")
        self.ClusterId = params.get("ClusterId")
        self.NamespaceDesc = params.get("NamespaceDesc")
        self.NamespaceResourceType = params.get("NamespaceResourceType")
        self.NamespaceType = params.get("NamespaceType")
        self.NamespaceId = params.get("NamespaceId")
        self.IsHaEnable = params.get("IsHaEnable")
        self.ProgramId = params.get("ProgramId")


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


class CreatePathRewritesRequest(AbstractModel):
    """CreatePathRewrites请求参数结构体

    """

    def __init__(self):
        """
        :param PathRewrites: 路径重写列表
        :type PathRewrites: :class:`tencentcloud.tsf.v20180326.models.PathRewriteCreateObject`
        """
        self.PathRewrites = None


    def _deserialize(self, params):
        if params.get("PathRewrites") is not None:
            self.PathRewrites = PathRewriteCreateObject()
            self.PathRewrites._deserialize(params.get("PathRewrites"))


class CreatePathRewritesResponse(AbstractModel):
    """CreatePathRewrites返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true/false
        :type Result: bool
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


class CreateRepositoryRequest(AbstractModel):
    """CreateRepository请求参数结构体

    """

    def __init__(self):
        """
        :param RepositoryName: 仓库名称
        :type RepositoryName: str
        :param RepositoryType: 仓库类型（默认仓库：default，私有仓库：private）
        :type RepositoryType: str
        :param BucketName: 仓库所在桶名称
        :type BucketName: str
        :param BucketRegion: 仓库所在桶地域
        :type BucketRegion: str
        :param Directory: 目录
        :type Directory: str
        :param RepositoryDesc: 仓库描述
        :type RepositoryDesc: str
        """
        self.RepositoryName = None
        self.RepositoryType = None
        self.BucketName = None
        self.BucketRegion = None
        self.Directory = None
        self.RepositoryDesc = None


    def _deserialize(self, params):
        self.RepositoryName = params.get("RepositoryName")
        self.RepositoryType = params.get("RepositoryType")
        self.BucketName = params.get("BucketName")
        self.BucketRegion = params.get("BucketRegion")
        self.Directory = params.get("Directory")
        self.RepositoryDesc = params.get("RepositoryDesc")


class CreateRepositoryResponse(AbstractModel):
    """CreateRepository返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建仓库是否成功
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


class CreateTaskFlowRequest(AbstractModel):
    """CreateTaskFlow请求参数结构体

    """

    def __init__(self):
        """
        :param FlowName: 工作流名称
        :type FlowName: str
        :param TriggerRule: 触发方式
        :type TriggerRule: :class:`tencentcloud.tsf.v20180326.models.TaskRule`
        :param FlowEdges: 工作流任务节点列表
        :type FlowEdges: list of TaskFlowEdge
        :param TimeOut: 工作流执行超时时间
        :type TimeOut: int
        """
        self.FlowName = None
        self.TriggerRule = None
        self.FlowEdges = None
        self.TimeOut = None


    def _deserialize(self, params):
        self.FlowName = params.get("FlowName")
        if params.get("TriggerRule") is not None:
            self.TriggerRule = TaskRule()
            self.TriggerRule._deserialize(params.get("TriggerRule"))
        if params.get("FlowEdges") is not None:
            self.FlowEdges = []
            for item in params.get("FlowEdges"):
                obj = TaskFlowEdge()
                obj._deserialize(item)
                self.FlowEdges.append(obj)
        self.TimeOut = params.get("TimeOut")


class CreateTaskFlowResponse(AbstractModel):
    """CreateTaskFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 工作流 ID
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskName: 任务名称，任务长度64字符
        :type TaskName: str
        :param TaskContent: 任务内容，长度限制65536个字节
        :type TaskContent: str
        :param ExecuteType: 执行类型，UNICAST/BROADCAST
        :type ExecuteType: str
        :param TaskType: 任务类型
        :type TaskType: str
        :param TimeOut: 任务超时时间， 时间单位 ms
        :type TimeOut: int
        :param GroupId: 部署组ID
        :type GroupId: str
        :param TaskRule: 触发规则
        :type TaskRule: :class:`tencentcloud.tsf.v20180326.models.TaskRule`
        :param RetryCount: 重试次数，0 <= RetryCount<= 10
        :type RetryCount: int
        :param RetryInterval: 重试间隔， 0 <= RetryInterval <= 600000， 时间单位 ms
        :type RetryInterval: int
        :param ShardCount: 分片数量
        :type ShardCount: int
        :param ShardArguments: 分片参数
        :type ShardArguments: list of ShardArgument
        :param SuccessOperator: 判断任务成功的操作符
        :type SuccessOperator: str
        :param SuccessRatio: 判断任务成功率的阈值，如99.99
        :type SuccessRatio: str
        :param AdvanceSettings: 高级设置
        :type AdvanceSettings: :class:`tencentcloud.tsf.v20180326.models.AdvanceSettings`
        :param TaskArgument: 任务参数，长度限制10000个字符
        :type TaskArgument: str
        """
        self.TaskName = None
        self.TaskContent = None
        self.ExecuteType = None
        self.TaskType = None
        self.TimeOut = None
        self.GroupId = None
        self.TaskRule = None
        self.RetryCount = None
        self.RetryInterval = None
        self.ShardCount = None
        self.ShardArguments = None
        self.SuccessOperator = None
        self.SuccessRatio = None
        self.AdvanceSettings = None
        self.TaskArgument = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskContent = params.get("TaskContent")
        self.ExecuteType = params.get("ExecuteType")
        self.TaskType = params.get("TaskType")
        self.TimeOut = params.get("TimeOut")
        self.GroupId = params.get("GroupId")
        if params.get("TaskRule") is not None:
            self.TaskRule = TaskRule()
            self.TaskRule._deserialize(params.get("TaskRule"))
        self.RetryCount = params.get("RetryCount")
        self.RetryInterval = params.get("RetryInterval")
        self.ShardCount = params.get("ShardCount")
        if params.get("ShardArguments") is not None:
            self.ShardArguments = []
            for item in params.get("ShardArguments"):
                obj = ShardArgument()
                obj._deserialize(item)
                self.ShardArguments.append(obj)
        self.SuccessOperator = params.get("SuccessOperator")
        self.SuccessRatio = params.get("SuccessRatio")
        if params.get("AdvanceSettings") is not None:
            self.AdvanceSettings = AdvanceSettings()
            self.AdvanceSettings._deserialize(params.get("AdvanceSettings"))
        self.TaskArgument = params.get("TaskArgument")


class CreateTaskResponse(AbstractModel):
    """CreateTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApiGroupRequest(AbstractModel):
    """DeleteApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: API 分组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteApiGroupResponse(AbstractModel):
    """DeleteApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功失败
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


class DeleteLaneRequest(AbstractModel):
    """DeleteLane请求参数结构体

    """

    def __init__(self):
        """
        :param LaneId: 泳道Idl
        :type LaneId: str
        """
        self.LaneId = None


    def _deserialize(self, params):
        self.LaneId = params.get("LaneId")


class DeleteLaneResponse(AbstractModel):
    """DeleteLane返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true / false
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


class DeletePathRewritesRequest(AbstractModel):
    """DeletePathRewrites请求参数结构体

    """

    def __init__(self):
        """
        :param PathRewriteIds: 路径重写规则IDs
        :type PathRewriteIds: list of str
        """
        self.PathRewriteIds = None


    def _deserialize(self, params):
        self.PathRewriteIds = params.get("PathRewriteIds")


class DeletePathRewritesResponse(AbstractModel):
    """DeletePathRewrites返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true/false
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
        :param RepositoryType: 程序包仓库类型
        :type RepositoryType: str
        :param RepositoryId: 程序包仓库id
        :type RepositoryId: str
        """
        self.ApplicationId = None
        self.PkgIds = None
        self.RepositoryType = None
        self.RepositoryId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgIds = params.get("PkgIds")
        self.RepositoryType = params.get("RepositoryType")
        self.RepositoryId = params.get("RepositoryId")


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


class DeleteRepositoryRequest(AbstractModel):
    """DeleteRepository请求参数结构体

    """

    def __init__(self):
        """
        :param RepositoryId: 仓库ID
        :type RepositoryId: str
        """
        self.RepositoryId = None


    def _deserialize(self, params):
        self.RepositoryId = params.get("RepositoryId")


class DeleteRepositoryResponse(AbstractModel):
    """DeleteRepository返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除仓库是否成功
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


class DeleteTaskRequest(AbstractModel):
    """DeleteTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DeleteTaskResponse(AbstractModel):
    """DeleteTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除成功or失败
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
        :param TagName: 镜像版本名称,如v1
        :type TagName: str
        :param InstanceNum: 实例数量
        :type InstanceNum: int
        :param Server: 镜像server
        :type Server: str
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
        :param MaxSurge: kubernetes滚动更新策略的MaxSurge参数
        :type MaxSurge: str
        :param MaxUnavailable: kubernetes滚动更新策略的MaxUnavailable参数
        :type MaxUnavailable: str
        :param HealthCheckSettings: 健康检查配置信息，若不指定该参数，则默认不设置健康检查。
        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`
        :param Envs: 部署组应用运行的环境变量。若不指定该参数，则默认不设置额外的环境变量。
        :type Envs: list of Env
        :param ServiceSetting: 容器部署组的网络设置。
        :type ServiceSetting: :class:`tencentcloud.tsf.v20180326.models.ServiceSetting`
        :param DeployAgent: 是否部署 agent 容器。若不指定该参数，则默认不部署 agent 容器。
        :type DeployAgent: bool
        :param SchedulingStrategy: 节点调度策略。若不指定改参数，则默认不使用节点调度策略。
        :type SchedulingStrategy: :class:`tencentcloud.tsf.v20180326.models.SchedulingStrategy`
        """
        self.GroupId = None
        self.TagName = None
        self.InstanceNum = None
        self.Server = None
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
        self.MaxSurge = None
        self.MaxUnavailable = None
        self.HealthCheckSettings = None
        self.Envs = None
        self.ServiceSetting = None
        self.DeployAgent = None
        self.SchedulingStrategy = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.TagName = params.get("TagName")
        self.InstanceNum = params.get("InstanceNum")
        self.Server = params.get("Server")
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
        self.MaxSurge = params.get("MaxSurge")
        self.MaxUnavailable = params.get("MaxUnavailable")
        if params.get("HealthCheckSettings") is not None:
            self.HealthCheckSettings = HealthCheckSettings()
            self.HealthCheckSettings._deserialize(params.get("HealthCheckSettings"))
        if params.get("Envs") is not None:
            self.Envs = []
            for item in params.get("Envs"):
                obj = Env()
                obj._deserialize(item)
                self.Envs.append(obj)
        if params.get("ServiceSetting") is not None:
            self.ServiceSetting = ServiceSetting()
            self.ServiceSetting._deserialize(params.get("ServiceSetting"))
        self.DeployAgent = params.get("DeployAgent")
        if params.get("SchedulingStrategy") is not None:
            self.SchedulingStrategy = SchedulingStrategy()
            self.SchedulingStrategy._deserialize(params.get("SchedulingStrategy"))


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
        :param DeployDesc: 部署应用描述信息
        :type DeployDesc: str
        :param ForceStart: 是否允许强制启动
        :type ForceStart: bool
        :param EnableHealthCheck: 是否开启健康检查
        :type EnableHealthCheck: bool
        :param HealthCheckSettings: 开启健康检查时，配置健康检查
        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`
        :param UpdateType: 部署方式，0表示快速更新，1表示滚动更新
        :type UpdateType: int
        :param DeployBetaEnable: 是否启用beta批次
        :type DeployBetaEnable: bool
        :param DeployBatch: 滚动发布每个批次参与的实例比率
        :type DeployBatch: list of float
        :param DeployExeMode: 滚动发布的执行方式
        :type DeployExeMode: str
        :param DeployWaitTime: 滚动发布每个批次的时间间隔
        :type DeployWaitTime: int
        """
        self.GroupId = None
        self.PkgId = None
        self.StartupParameters = None
        self.DeployDesc = None
        self.ForceStart = None
        self.EnableHealthCheck = None
        self.HealthCheckSettings = None
        self.UpdateType = None
        self.DeployBetaEnable = None
        self.DeployBatch = None
        self.DeployExeMode = None
        self.DeployWaitTime = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PkgId = params.get("PkgId")
        self.StartupParameters = params.get("StartupParameters")
        self.DeployDesc = params.get("DeployDesc")
        self.ForceStart = params.get("ForceStart")
        self.EnableHealthCheck = params.get("EnableHealthCheck")
        if params.get("HealthCheckSettings") is not None:
            self.HealthCheckSettings = HealthCheckSettings()
            self.HealthCheckSettings._deserialize(params.get("HealthCheckSettings"))
        self.UpdateType = params.get("UpdateType")
        self.DeployBetaEnable = params.get("DeployBetaEnable")
        self.DeployBatch = params.get("DeployBatch")
        self.DeployExeMode = params.get("DeployExeMode")
        self.DeployWaitTime = params.get("DeployWaitTime")


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


class DescribeApiDetailRequest(AbstractModel):
    """DescribeApiDetail请求参数结构体

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服务id
        :type MicroserviceId: str
        :param Path: 请求路径
        :type Path: str
        :param Method: 请求方法
        :type Method: str
        :param PkgVersion: 包版本
        :type PkgVersion: str
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        """
        self.MicroserviceId = None
        self.Path = None
        self.Method = None
        self.PkgVersion = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.PkgVersion = params.get("PkgVersion")
        self.ApplicationId = params.get("ApplicationId")


class DescribeApiDetailResponse(AbstractModel):
    """DescribeApiDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API 详情
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApiDetailResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiDetailResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiGroupRequest(AbstractModel):
    """DescribeApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: API 分组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeApiGroupResponse(AbstractModel):
    """DescribeApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API分组信息
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApiGroupInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiGroupInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiGroupsRequest(AbstractModel):
    """DescribeApiGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 每页条数，默认为20
        :type Limit: int
        :param GroupType: 分组类型。 ms： 微服务分组； external:外部Api分组
        :type GroupType: str
        :param AuthType: 鉴权类型。 secret： 秘钥鉴权； none:无鉴权
        :type AuthType: str
        :param Status: 发布状态, drafted: 未发布。 released: 发布
        :type Status: str
        :param OrderBy: 排序字段："created_time"或"group_context"
        :type OrderBy: str
        :param OrderType: 排序类型：0(ASC)或1(DESC)
        :type OrderType: int
        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.GroupType = None
        self.AuthType = None
        self.Status = None
        self.OrderBy = None
        self.OrderType = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupType = params.get("GroupType")
        self.AuthType = params.get("AuthType")
        self.Status = params.get("Status")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")


class DescribeApiGroupsResponse(AbstractModel):
    """DescribeApiGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 翻页结构体
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageApiGroupInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageApiGroupInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiRateLimitRulesRequest(AbstractModel):
    """DescribeApiRateLimitRules请求参数结构体

    """

    def __init__(self):
        """
        :param ApiId: Api ID
        :type ApiId: str
        """
        self.ApiId = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")


class DescribeApiRateLimitRulesResponse(AbstractModel):
    """DescribeApiRateLimitRules返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 限流结果
        :type Result: list of ApiRateLimitRule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = ApiRateLimitRule()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeApiUseDetailRequest(AbstractModel):
    """DescribeApiUseDetail请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayDeployGroupId: 网关部署组ID
        :type GatewayDeployGroupId: str
        :param ApiId: 网关分组Api ID
        :type ApiId: str
        :param StartTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss
        :type StartTime: str
        :param EndTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss
        :type EndTime: str
        """
        self.GatewayDeployGroupId = None
        self.ApiId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.ApiId = params.get("ApiId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeApiUseDetailResponse(AbstractModel):
    """DescribeApiUseDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 日使用统计对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.GroupApiUseStatistics`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupApiUseStatistics()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiVersionsRequest(AbstractModel):
    """DescribeApiVersions请求参数结构体

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服务ID
        :type MicroserviceId: str
        :param Path: API 请求路径
        :type Path: str
        :param Method: 请求方法
        :type Method: str
        """
        self.MicroserviceId = None
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.Path = params.get("Path")
        self.Method = params.get("Method")


class DescribeApiVersionsResponse(AbstractModel):
    """DescribeApiVersions返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API版本列表
        :type Result: list of ApiVersionArray
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = ApiVersionArray()
                obj._deserialize(item)
                self.Result.append(obj)
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


class DescribeBasicResourceUsageRequest(AbstractModel):
    """DescribeBasicResourceUsage请求参数结构体

    """


class DescribeBasicResourceUsageResponse(AbstractModel):
    """DescribeBasicResourceUsage返回参数结构体

    """

    def __init__(self):
        """
        :param Result: TSF基本资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.OverviewBasicResourceUsage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = OverviewBasicResourceUsage()
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


class DescribeCreateGatewayApiStatusRequest(AbstractModel):
    """DescribeCreateGatewayApiStatus请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 请求方法
        :type GroupId: str
        :param MicroserviceId: 微服务ID
        :type MicroserviceId: str
        """
        self.GroupId = None
        self.MicroserviceId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.MicroserviceId = params.get("MicroserviceId")


class DescribeCreateGatewayApiStatusResponse(AbstractModel):
    """DescribeCreateGatewayApiStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否已完成导入任务
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
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
        :param RepositoryId: 程序包仓库ID
        :type RepositoryId: str
        :param RepositoryType: 程序包仓库类型
        :type RepositoryType: str
        """
        self.ApplicationId = None
        self.PkgId = None
        self.RepositoryId = None
        self.RepositoryType = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgId = params.get("PkgId")
        self.RepositoryId = params.get("RepositoryId")
        self.RepositoryType = params.get("RepositoryType")


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


class DescribeFlowLastBatchStateRequest(AbstractModel):
    """DescribeFlowLastBatchState请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 工作流 ID
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class DescribeFlowLastBatchStateResponse(AbstractModel):
    """DescribeFlowLastBatchState返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 工作流批次最新状态
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskFlowLastBatchState`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskFlowLastBatchState()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGatewayAllGroupApisRequest(AbstractModel):
    """DescribeGatewayAllGroupApis请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayDeployGroupId: 网关部署组ID
        :type GatewayDeployGroupId: str
        :param SearchWord: 搜索关键字，支持分组名称或API Path
        :type SearchWord: str
        """
        self.GatewayDeployGroupId = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.SearchWord = params.get("SearchWord")


class DescribeGatewayAllGroupApisResponse(AbstractModel):
    """DescribeGatewayAllGroupApis返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 网关分组和API列表信息
        :type Result: :class:`tencentcloud.tsf.v20180326.models.GatewayVo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GatewayVo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGatewayMonitorOverviewRequest(AbstractModel):
    """DescribeGatewayMonitorOverview请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayDeployGroupId: 网关部署组ID
        :type GatewayDeployGroupId: str
        """
        self.GatewayDeployGroupId = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")


class DescribeGatewayMonitorOverviewResponse(AbstractModel):
    """DescribeGatewayMonitorOverview返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 监控概览对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.MonitorOverview`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = MonitorOverview()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupBindedGatewaysRequest(AbstractModel):
    """DescribeGroupBindedGateways请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: API 分组ID
        :type GroupId: str
        :param Offset: 翻页查询偏移量
        :type Offset: int
        :param Limit: 翻页查询每页记录数
        :type Limit: int
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")


class DescribeGroupBindedGatewaysResponse(AbstractModel):
    """DescribeGroupBindedGateways返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 翻页结构体
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageGatewayDeployGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageGatewayDeployGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupGatewaysRequest(AbstractModel):
    """DescribeGroupGateways请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayDeployGroupId: 网关部署组ID
        :type GatewayDeployGroupId: str
        :param Offset: 翻页查询偏移量
        :type Offset: int
        :param Limit: 翻页查询每页记录数
        :type Limit: int
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        """
        self.GatewayDeployGroupId = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")


class DescribeGroupGatewaysResponse(AbstractModel):
    """DescribeGroupGateways返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API分组信息
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageApiGroupInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageApiGroupInfo()
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


class DescribeGroupUseDetailRequest(AbstractModel):
    """DescribeGroupUseDetail请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayDeployGroupId: 网关部署组ID
        :type GatewayDeployGroupId: str
        :param GroupId: 网关分组ID
        :type GroupId: str
        :param StartTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss
        :type StartTime: str
        :param EndTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss
        :type EndTime: str
        :param Count: 指定top的条数,默认为10
        :type Count: int
        """
        self.GatewayDeployGroupId = None
        self.GroupId = None
        self.StartTime = None
        self.EndTime = None
        self.Count = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.GroupId = params.get("GroupId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Count = params.get("Count")


class DescribeGroupUseDetailResponse(AbstractModel):
    """DescribeGroupUseDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 日使用统计对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.GroupDailyUseStatistics`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupDailyUseStatistics()
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
        :param Status: 部署组状态过滤字段
        :type Status: str
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
        self.Status = None


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
        self.Status = params.get("Status")


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


class DescribeImageRepositoryRequest(AbstractModel):
    """DescribeImageRepository请求参数结构体

    """

    def __init__(self):
        """
        :param SearchWord: 仓库名，搜索关键字,不带命名空间的
        :type SearchWord: str
        :param Offset: 偏移量，取值从0开始
        :type Offset: int
        :param Limit: 分页个数，默认为20， 取值应为1~100
        :type Limit: int
        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeImageRepositoryResponse(AbstractModel):
    """DescribeImageRepository返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询的权限数据对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ImageRepositoryResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ImageRepositoryResult()
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


class DescribeLaneRulesRequest(AbstractModel):
    """DescribeLaneRules请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 每页展示的条数
        :type Limit: int
        :param Offset: 翻页偏移量
        :type Offset: int
        :param SearchWord: 搜索关键词
        :type SearchWord: str
        :param RuleId: 泳道规则ID（用于精确搜索）
        :type RuleId: str
        """
        self.Limit = None
        self.Offset = None
        self.SearchWord = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SearchWord = params.get("SearchWord")
        self.RuleId = params.get("RuleId")


class DescribeLaneRulesResponse(AbstractModel):
    """DescribeLaneRules返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 泳道规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.LaneRules`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = LaneRules()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeLanesRequest(AbstractModel):
    """DescribeLanes请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 每页展示的条数
        :type Limit: int
        :param Offset: 翻页偏移量
        :type Offset: int
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        """
        self.Limit = None
        self.Offset = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SearchWord = params.get("SearchWord")


class DescribeLanesResponse(AbstractModel):
    """DescribeLanes返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 泳道列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.LaneInfos`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = LaneInfos()
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
        :param Status: 状态过滤，online、offline、single_online
        :type Status: list of str
        """
        self.NamespaceId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.Status = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")


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


class DescribeMsApiListRequest(AbstractModel):
    """DescribeMsApiList请求参数结构体

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服务ID
        :type MicroserviceId: str
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        :param Limit: 每页的数量
        :type Limit: int
        :param Offset: 翻页偏移量
        :type Offset: int
        """
        self.MicroserviceId = None
        self.SearchWord = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.SearchWord = params.get("SearchWord")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeMsApiListResponse(AbstractModel):
    """DescribeMsApiList返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 相应结果
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfApiListResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfApiListResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePathRewriteRequest(AbstractModel):
    """DescribePathRewrite请求参数结构体

    """

    def __init__(self):
        """
        :param PathRewriteId: 路径重写规则ID
        :type PathRewriteId: str
        """
        self.PathRewriteId = None


    def _deserialize(self, params):
        self.PathRewriteId = params.get("PathRewriteId")


class DescribePathRewriteResponse(AbstractModel):
    """DescribePathRewrite返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 路径重写规则对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.PathRewrite`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = PathRewrite()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePathRewritesRequest(AbstractModel):
    """DescribePathRewrites请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayGroupId: 网关部署组ID
        :type GatewayGroupId: str
        :param SearchWord: 根据正则表达式或替换的内容模糊查询
        :type SearchWord: str
        :param Limit: 每页数量
        :type Limit: int
        :param Offset: 起始偏移量
        :type Offset: int
        """
        self.GatewayGroupId = None
        self.SearchWord = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.GatewayGroupId = params.get("GatewayGroupId")
        self.SearchWord = params.get("SearchWord")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribePathRewritesResponse(AbstractModel):
    """DescribePathRewrites返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 路径重写翻页对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.PathRewritePage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = PathRewritePage()
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
        :param RepositoryType: 程序包仓库类型
        :type RepositoryType: str
        :param RepositoryId: 程序包仓库id
        :type RepositoryId: str
        """
        self.ApplicationId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.RepositoryType = None
        self.RepositoryId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.RepositoryType = params.get("RepositoryType")
        self.RepositoryId = params.get("RepositoryId")


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


class DescribeRepositoriesRequest(AbstractModel):
    """DescribeRepositories请求参数结构体

    """

    def __init__(self):
        """
        :param SearchWord: 查询关键字（按照仓库名称搜索）
        :type SearchWord: str
        :param Offset: 查询起始偏移
        :type Offset: int
        :param Limit: 返回数量限制
        :type Limit: int
        :param RepositoryType: 仓库类型（默认仓库：default，私有仓库：private）
        :type RepositoryType: str
        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.RepositoryType = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.RepositoryType = params.get("RepositoryType")


class DescribeRepositoriesResponse(AbstractModel):
    """DescribeRepositories返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 符合查询仓库信息列表
        :type Result: :class:`tencentcloud.tsf.v20180326.models.RepositoryList`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = RepositoryList()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeRepositoryRequest(AbstractModel):
    """DescribeRepository请求参数结构体

    """

    def __init__(self):
        """
        :param RepositoryId: 仓库ID
        :type RepositoryId: str
        """
        self.RepositoryId = None


    def _deserialize(self, params):
        self.RepositoryId = params.get("RepositoryId")


class DescribeRepositoryResponse(AbstractModel):
    """DescribeRepository返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询的仓库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.RepositoryInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = RepositoryInfo()
            self.Result._deserialize(params.get("Result"))
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
        :param AppMicroServiceType: 部署组类型，精确过滤字段，M：service mesh, P：原生应用， G：网关应用
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


class DescribeTaskLastStatusRequest(AbstractModel):
    """DescribeTaskLastStatus请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskLastStatusResponse(AbstractModel):
    """DescribeTaskLastStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务上一次执行状态
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskLastExecuteStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskLastExecuteStatus()
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
        :param RepositoryType: 程序包仓库类型
        :type RepositoryType: str
        :param RepositoryId: 程序包仓库id
        :type RepositoryId: str
        """
        self.ApplicationId = None
        self.PkgName = None
        self.PkgVersion = None
        self.PkgType = None
        self.PkgDesc = None
        self.RepositoryType = None
        self.RepositoryId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgName = params.get("PkgName")
        self.PkgVersion = params.get("PkgVersion")
        self.PkgType = params.get("PkgType")
        self.PkgDesc = params.get("PkgDesc")
        self.RepositoryType = params.get("RepositoryType")
        self.RepositoryId = params.get("RepositoryId")


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


class DisableTaskFlowRequest(AbstractModel):
    """DisableTaskFlow请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 工作流 ID
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class DisableTaskFlowResponse(AbstractModel):
    """DisableTaskFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true成功，false: 失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableTaskRequest(AbstractModel):
    """DisableTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DisableTaskResponse(AbstractModel):
    """DisableTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作成功 or 失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DraftApiGroupRequest(AbstractModel):
    """DraftApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: Api 分组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DraftApiGroupResponse(AbstractModel):
    """DraftApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true: 成功, false: 失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class EnableTaskFlowRequest(AbstractModel):
    """EnableTaskFlow请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 工作流 ID
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class EnableTaskFlowResponse(AbstractModel):
    """EnableTaskFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true成功，false: 失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class EnableTaskRequest(AbstractModel):
    """EnableTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 启用任务
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class EnableTaskResponse(AbstractModel):
    """EnableTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作成功or失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
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


class ExecuteTaskFlowRequest(AbstractModel):
    """ExecuteTaskFlow请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 工作流 ID
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class ExecuteTaskFlowResponse(AbstractModel):
    """ExecuteTaskFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 工作流批次ID
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ExecuteTaskRequest(AbstractModel):
    """ExecuteTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class ExecuteTaskResponse(AbstractModel):
    """ExecuteTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功/失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


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


class GatewayApiGroupVo(AbstractModel):
    """网关分组简单信息

    """

    def __init__(self):
        """
        :param GroupId: 分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param GroupApiCount: 分组下API个数
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupApiCount: int
        :param GroupApis: 分组API列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupApis: list of GatewayGroupApiVo
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupApiCount = None
        self.GroupApis = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupApiCount = params.get("GroupApiCount")
        if params.get("GroupApis") is not None:
            self.GroupApis = []
            for item in params.get("GroupApis"):
                obj = GatewayGroupApiVo()
                obj._deserialize(item)
                self.GroupApis.append(obj)


class GatewayDeployGroup(AbstractModel):
    """api分组已绑定的网关部署组

    """

    def __init__(self):
        """
        :param DeployGroupId: 网关部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployGroupId: str
        :param DeployGroupName: 网关部署组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployGroupName: str
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ApplicationType: 应用分类：V：虚拟机应用，C：容器应用
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param GroupStatus: 部署组应用状态,取值: Running、Waiting、Paused、Updating、RollingBack、Abnormal、Unknown
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupStatus: str
        :param ClusterType: 集群类型，C ：容器，V：虚拟机
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        """
        self.DeployGroupId = None
        self.DeployGroupName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationType = None
        self.GroupStatus = None
        self.ClusterType = None


    def _deserialize(self, params):
        self.DeployGroupId = params.get("DeployGroupId")
        self.DeployGroupName = params.get("DeployGroupName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.GroupStatus = params.get("GroupStatus")
        self.ClusterType = params.get("ClusterType")


class GatewayGroupApiVo(AbstractModel):
    """网关API简单信息

    """

    def __init__(self):
        """
        :param ApiId: API ID
        :type ApiId: str
        :param Path: API 请求路径
        :type Path: str
        :param MicroserviceName: API 微服务名称
        :type MicroserviceName: str
        :param Method: API 请求方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        """
        self.ApiId = None
        self.Path = None
        self.MicroserviceName = None
        self.Method = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.Path = params.get("Path")
        self.MicroserviceName = params.get("MicroserviceName")
        self.Method = params.get("Method")
        self.NamespaceName = params.get("NamespaceName")


class GatewayGroupIds(AbstractModel):
    """网关部署组ID和网关API分组ID元组

    """

    def __init__(self):
        """
        :param GatewayDeployGroupId: 网关部署组ID
        :type GatewayDeployGroupId: str
        :param GroupId: 分组id
        :type GroupId: str
        """
        self.GatewayDeployGroupId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.GroupId = params.get("GroupId")


class GatewayVo(AbstractModel):
    """网关部署组、分组、API列表数据

    """

    def __init__(self):
        """
        :param GatewayDeployGroupId: 网关部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayDeployGroupId: str
        :param GatewayDeployGroupName: 网关部署组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayDeployGroupName: str
        :param GroupNum: API 分组个数
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupNum: int
        :param Groups: API 分组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of GatewayApiGroupVo
        """
        self.GatewayDeployGroupId = None
        self.GatewayDeployGroupName = None
        self.GroupNum = None
        self.Groups = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.GatewayDeployGroupName = params.get("GatewayDeployGroupName")
        self.GroupNum = params.get("GroupNum")
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = GatewayApiGroupVo()
                obj._deserialize(item)
                self.Groups.append(obj)


class GroupApiUseStatistics(AbstractModel):
    """API监控明细数据

    """

    def __init__(self):
        """
        :param TopStatusCode: 总调用数
注意：此字段可能返回 null，表示取不到有效值。
        :type TopStatusCode: list of ApiUseStatisticsEntity
        :param TopTimeCost: 平均错误率
注意：此字段可能返回 null，表示取不到有效值。
        :type TopTimeCost: list of ApiUseStatisticsEntity
        :param Quantile: 分位值对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Quantile: :class:`tencentcloud.tsf.v20180326.models.QuantileEntity`
        """
        self.TopStatusCode = None
        self.TopTimeCost = None
        self.Quantile = None


    def _deserialize(self, params):
        if params.get("TopStatusCode") is not None:
            self.TopStatusCode = []
            for item in params.get("TopStatusCode"):
                obj = ApiUseStatisticsEntity()
                obj._deserialize(item)
                self.TopStatusCode.append(obj)
        if params.get("TopTimeCost") is not None:
            self.TopTimeCost = []
            for item in params.get("TopTimeCost"):
                obj = ApiUseStatisticsEntity()
                obj._deserialize(item)
                self.TopTimeCost.append(obj)
        if params.get("Quantile") is not None:
            self.Quantile = QuantileEntity()
            self.Quantile._deserialize(params.get("Quantile"))


class GroupDailyUseStatistics(AbstractModel):
    """分组日使用统计对象

    """

    def __init__(self):
        """
        :param TopReqAmount: 总调用数
        :type TopReqAmount: list of GroupUseStatisticsEntity
        :param TopFailureRate: 平均错误率
        :type TopFailureRate: list of GroupUseStatisticsEntity
        :param TopAvgTimeCost: 平均响应耗时
        :type TopAvgTimeCost: list of GroupUseStatisticsEntity
        """
        self.TopReqAmount = None
        self.TopFailureRate = None
        self.TopAvgTimeCost = None


    def _deserialize(self, params):
        if params.get("TopReqAmount") is not None:
            self.TopReqAmount = []
            for item in params.get("TopReqAmount"):
                obj = GroupUseStatisticsEntity()
                obj._deserialize(item)
                self.TopReqAmount.append(obj)
        if params.get("TopFailureRate") is not None:
            self.TopFailureRate = []
            for item in params.get("TopFailureRate"):
                obj = GroupUseStatisticsEntity()
                obj._deserialize(item)
                self.TopFailureRate.append(obj)
        if params.get("TopAvgTimeCost") is not None:
            self.TopAvgTimeCost = []
            for item in params.get("TopAvgTimeCost"):
                obj = GroupUseStatisticsEntity()
                obj._deserialize(item)
                self.TopAvgTimeCost.append(obj)


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
        :param NodeInstanceId: 节点实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInstanceId: str
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
        self.NodeInstanceId = None


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
        self.NodeInstanceId = params.get("NodeInstanceId")


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


class GroupUseStatisticsEntity(AbstractModel):
    """API分组日使用统计对象数据点

    """

    def __init__(self):
        """
        :param ApiPath: API 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiPath: str
        :param ServiceName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param Value: 统计值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param ApiId: API ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        """
        self.ApiPath = None
        self.ServiceName = None
        self.Value = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ApiPath = params.get("ApiPath")
        self.ServiceName = params.get("ServiceName")
        self.Value = params.get("Value")
        self.ApiId = params.get("ApiId")


class HealthCheckSetting(AbstractModel):
    """健康检查配置信息，若不指定该参数，则默认不设置健康检查。

    """

    def __init__(self):
        """
        :param ActionType: 健康检查方法。HTTP：通过 HTTP 接口检查；CMD：通过执行命令检查；TCP：通过建立 TCP 连接检查。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionType: str
        :param InitialDelaySeconds: 容器延时启动健康检查的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param TimeoutSeconds: 每次健康检查响应的最大超时时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutSeconds: int
        :param PeriodSeconds: 进行健康检查的时间间隔。
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodSeconds: int
        :param SuccessThreshold: 表示后端容器从失败到成功的连续健康检查成功次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessThreshold: int
        :param FailureThreshold: 表示后端容器从成功到失败的连续健康检查成功次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureThreshold: int
        :param Scheme: HTTP 健康检查方法使用的检查协议。支持HTTP、HTTPS。
注意：此字段可能返回 null，表示取不到有效值。
        :type Scheme: str
        :param Port: 健康检查端口，范围 1~65535 。
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param Path: HTTP 健康检查接口的请求路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Command: 执行命令检查方式，执行的命令。
注意：此字段可能返回 null，表示取不到有效值。
        :type Command: list of str
        :param Type: TSF_DEFAULT：tsf 默认就绪探针。K8S_NATIVE：k8s 原生探针。不填默认为 k8s 原生探针。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.ActionType = None
        self.InitialDelaySeconds = None
        self.TimeoutSeconds = None
        self.PeriodSeconds = None
        self.SuccessThreshold = None
        self.FailureThreshold = None
        self.Scheme = None
        self.Port = None
        self.Path = None
        self.Command = None
        self.Type = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        self.TimeoutSeconds = params.get("TimeoutSeconds")
        self.PeriodSeconds = params.get("PeriodSeconds")
        self.SuccessThreshold = params.get("SuccessThreshold")
        self.FailureThreshold = params.get("FailureThreshold")
        self.Scheme = params.get("Scheme")
        self.Port = params.get("Port")
        self.Path = params.get("Path")
        self.Command = params.get("Command")
        self.Type = params.get("Type")


class HealthCheckSettings(AbstractModel):
    """健康检查参数

    """

    def __init__(self):
        """
        :param LivenessProbe: 存活健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessProbe: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSetting`
        :param ReadinessProbe: 就绪健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadinessProbe: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSetting`
        """
        self.LivenessProbe = None
        self.ReadinessProbe = None


    def _deserialize(self, params):
        if params.get("LivenessProbe") is not None:
            self.LivenessProbe = HealthCheckSetting()
            self.LivenessProbe._deserialize(params.get("LivenessProbe"))
        if params.get("ReadinessProbe") is not None:
            self.ReadinessProbe = HealthCheckSetting()
            self.ReadinessProbe._deserialize(params.get("ReadinessProbe"))


class ImageRepository(AbstractModel):
    """镜像仓库

    """

    def __init__(self):
        """
        :param Reponame: 仓库名,含命名空间,如tsf/nginx
注意：此字段可能返回 null，表示取不到有效值。
        :type Reponame: str
        :param Repotype: 仓库类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Repotype: str
        :param TagCount: 镜像版本数
注意：此字段可能返回 null，表示取不到有效值。
        :type TagCount: int
        :param IsPublic: 是否公共,1:公有,0:私有
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublic: int
        :param IsUserFavor: 是否被用户收藏。true：是，false：否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUserFavor: bool
        :param IsQcloudOfficial: 是否是腾讯云官方仓库。 是否是腾讯云官方仓库。true：是，false：否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQcloudOfficial: bool
        :param FavorCount: 被所有用户收藏次数
注意：此字段可能返回 null，表示取不到有效值。
        :type FavorCount: int
        :param PullCount: 拉取次数
注意：此字段可能返回 null，表示取不到有效值。
        :type PullCount: int
        :param Description: 描述内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreationTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Reponame = None
        self.Repotype = None
        self.TagCount = None
        self.IsPublic = None
        self.IsUserFavor = None
        self.IsQcloudOfficial = None
        self.FavorCount = None
        self.PullCount = None
        self.Description = None
        self.CreationTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Reponame = params.get("Reponame")
        self.Repotype = params.get("Repotype")
        self.TagCount = params.get("TagCount")
        self.IsPublic = params.get("IsPublic")
        self.IsUserFavor = params.get("IsUserFavor")
        self.IsQcloudOfficial = params.get("IsQcloudOfficial")
        self.FavorCount = params.get("FavorCount")
        self.PullCount = params.get("PullCount")
        self.Description = params.get("Description")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")


class ImageRepositoryResult(AbstractModel):
    """镜像仓库列表

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Server: 镜像服务器地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Server: str
        :param Content: 列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of ImageRepository
        """
        self.TotalCount = None
        self.Server = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Server = params.get("Server")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ImageRepository()
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
        :param NamespaceId: NamespaceId Ns ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param InstanceZoneId: InstanceZoneId 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceZoneId: str
        :param InstanceImportMode: InstanceImportMode 导入模式
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceImportMode: str
        :param ApplicationType: ApplicationType应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param ApplicationResourceType: ApplicationResourceType 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationResourceType: str
        :param ServiceSidecarStatus: sidecar状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceSidecarStatus: str
        :param GroupName: 部署组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param NamespaceName: NS名
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param Reason: 健康检查原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
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
        self.Reason = None


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
        self.Reason = params.get("Reason")


class InstanceAdvancedSettings(AbstractModel):
    """容器导入实例高级设置

    """

    def __init__(self):
        """
        :param MountTarget: 数据盘挂载点, 默认不挂载数据盘. 已格式化的 ext3，ext4，xfs 文件系统的数据盘将直接挂载，其他文件系统或未格式化的数据盘将自动格式化为ext4 并挂载，请注意备份数据! 无数据盘或有多块数据盘的云主机此设置不生效。
注意，注意，多盘场景请使用下方的DataDisks数据结构，设置对应的云盘类型、云盘大小、挂载路径、是否格式化等信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MountTarget: str
        :param DockerGraphPath: dockerd --graph 指定值, 默认为 /var/lib/docker
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerGraphPath: str
        """
        self.MountTarget = None
        self.DockerGraphPath = None


    def _deserialize(self, params):
        self.MountTarget = params.get("MountTarget")
        self.DockerGraphPath = params.get("DockerGraphPath")


class LaneGroup(AbstractModel):
    """泳道部署组

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param Entrance: 是否入口应用
注意：此字段可能返回 null，表示取不到有效值。
        :type Entrance: bool
        :param LaneGroupId: 泳道部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LaneGroupId: str
        :param LaneId: 泳道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LaneId: str
        :param GroupName: 部署组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        """
        self.GroupId = None
        self.Entrance = None
        self.LaneGroupId = None
        self.LaneId = None
        self.GroupName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ClusterType = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Entrance = params.get("Entrance")
        self.LaneGroupId = params.get("LaneGroupId")
        self.LaneId = params.get("LaneId")
        self.GroupName = params.get("GroupName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ClusterType = params.get("ClusterType")


class LaneInfo(AbstractModel):
    """泳道

    """

    def __init__(self):
        """
        :param LaneId: 泳道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LaneId: str
        :param LaneName: 泳道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LaneName: str
        :param Remark: 泳道备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param LaneGroupList: 泳道部署组
注意：此字段可能返回 null，表示取不到有效值。
        :type LaneGroupList: list of LaneGroup
        :param Entrance: 是否入口应用
注意：此字段可能返回 null，表示取不到有效值。
        :type Entrance: bool
        :param NamespaceIdList: 泳道已经关联部署组的命名空间列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceIdList: list of str
        """
        self.LaneId = None
        self.LaneName = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None
        self.LaneGroupList = None
        self.Entrance = None
        self.NamespaceIdList = None


    def _deserialize(self, params):
        self.LaneId = params.get("LaneId")
        self.LaneName = params.get("LaneName")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("LaneGroupList") is not None:
            self.LaneGroupList = []
            for item in params.get("LaneGroupList"):
                obj = LaneGroup()
                obj._deserialize(item)
                self.LaneGroupList.append(obj)
        self.Entrance = params.get("Entrance")
        self.NamespaceIdList = params.get("NamespaceIdList")


class LaneInfos(AbstractModel):
    """泳道分页查询

    """

    def __init__(self):
        """
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 泳道信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of LaneInfo
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = LaneInfo()
                obj._deserialize(item)
                self.Content.append(obj)


class LaneRule(AbstractModel):
    """泳道规则

    """

    def __init__(self):
        """
        :param RuleId: 泳道规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param RuleName: 泳道规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param Priority: 优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param RuleTagList: 泳道规则标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTagList: list of LaneRuleTag
        :param RuleTagRelationship: 泳道规则标签关系
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTagRelationship: str
        :param LaneId: 泳道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LaneId: str
        :param Enable: 开启状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: bool
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        """
        self.RuleId = None
        self.RuleName = None
        self.Priority = None
        self.Remark = None
        self.RuleTagList = None
        self.RuleTagRelationship = None
        self.LaneId = None
        self.Enable = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.Priority = params.get("Priority")
        self.Remark = params.get("Remark")
        if params.get("RuleTagList") is not None:
            self.RuleTagList = []
            for item in params.get("RuleTagList"):
                obj = LaneRuleTag()
                obj._deserialize(item)
                self.RuleTagList.append(obj)
        self.RuleTagRelationship = params.get("RuleTagRelationship")
        self.LaneId = params.get("LaneId")
        self.Enable = params.get("Enable")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class LaneRuleTag(AbstractModel):
    """泳道规则标签

    """

    def __init__(self):
        """
        :param TagId: 标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TagId: str
        :param TagName: 标签名
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param TagOperator: 标签操作符
注意：此字段可能返回 null，表示取不到有效值。
        :type TagOperator: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        :param LaneRuleId: 泳道规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LaneRuleId: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        """
        self.TagId = None
        self.TagName = None
        self.TagOperator = None
        self.TagValue = None
        self.LaneRuleId = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TagId = params.get("TagId")
        self.TagName = params.get("TagName")
        self.TagOperator = params.get("TagOperator")
        self.TagValue = params.get("TagValue")
        self.LaneRuleId = params.get("LaneRuleId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class LaneRules(AbstractModel):
    """泳道规则分页查询

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param Content: 泳道规则列表
        :type Content: list of LaneRule
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = LaneRule()
                obj._deserialize(item)
                self.Content.append(obj)


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
        :param CriticalInstanceCount: 微服务的离线实例数目
注意：此字段可能返回 null，表示取不到有效值。
        :type CriticalInstanceCount: int
        """
        self.MicroserviceId = None
        self.MicroserviceName = None
        self.MicroserviceDesc = None
        self.CreateTime = None
        self.UpdateTime = None
        self.NamespaceId = None
        self.RunInstanceCount = None
        self.CriticalInstanceCount = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.MicroserviceName = params.get("MicroserviceName")
        self.MicroserviceDesc = params.get("MicroserviceDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.NamespaceId = params.get("NamespaceId")
        self.RunInstanceCount = params.get("RunInstanceCount")
        self.CriticalInstanceCount = params.get("CriticalInstanceCount")


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
        :param SubnetId: 子网ID
        :type SubnetId: str
        """
        self.GroupId = None
        self.AccessType = None
        self.ProtocolPorts = None
        self.UpdateType = None
        self.UpdateIvl = None
        self.SubnetId = None


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
        self.SubnetId = params.get("SubnetId")


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


class ModifyLaneRequest(AbstractModel):
    """ModifyLane请求参数结构体

    """

    def __init__(self):
        """
        :param LaneId: 泳道ID
        :type LaneId: str
        :param LaneName: 泳道名称
        :type LaneName: str
        :param Remark: 备注
        :type Remark: str
        """
        self.LaneId = None
        self.LaneName = None
        self.Remark = None


    def _deserialize(self, params):
        self.LaneId = params.get("LaneId")
        self.LaneName = params.get("LaneName")
        self.Remark = params.get("Remark")


class ModifyLaneResponse(AbstractModel):
    """ModifyLane返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作状态
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyLaneRuleRequest(AbstractModel):
    """ModifyLaneRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 泳道规则ID
        :type RuleId: str
        :param RuleName: 泳道规则名称
        :type RuleName: str
        :param Remark: 泳道规则备注
        :type Remark: str
        :param RuleTagList: 泳道规则标签列表
        :type RuleTagList: list of LaneRuleTag
        :param RuleTagRelationship: 泳道规则标签关系
        :type RuleTagRelationship: str
        :param LaneId: 泳道ID
        :type LaneId: str
        :param Enable: 开启状态
        :type Enable: bool
        """
        self.RuleId = None
        self.RuleName = None
        self.Remark = None
        self.RuleTagList = None
        self.RuleTagRelationship = None
        self.LaneId = None
        self.Enable = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.Remark = params.get("Remark")
        if params.get("RuleTagList") is not None:
            self.RuleTagList = []
            for item in params.get("RuleTagList"):
                obj = LaneRuleTag()
                obj._deserialize(item)
                self.RuleTagList.append(obj)
        self.RuleTagRelationship = params.get("RuleTagRelationship")
        self.LaneId = params.get("LaneId")
        self.Enable = params.get("Enable")


class ModifyLaneRuleResponse(AbstractModel):
    """ModifyLaneRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作状态
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


class ModifyPathRewriteRequest(AbstractModel):
    """ModifyPathRewrite请求参数结构体

    """

    def __init__(self):
        """
        :param PathRewriteId: 路径重写规则ID
        :type PathRewriteId: str
        :param Regex: 正则表达式
        :type Regex: str
        :param Replacement: 替换的内容
        :type Replacement: str
        :param Blocked: 是否屏蔽映射后路径，Y: 是 N: 否
        :type Blocked: str
        :param Order: 规则顺序，越小优先级越高
        :type Order: int
        """
        self.PathRewriteId = None
        self.Regex = None
        self.Replacement = None
        self.Blocked = None
        self.Order = None


    def _deserialize(self, params):
        self.PathRewriteId = params.get("PathRewriteId")
        self.Regex = params.get("Regex")
        self.Replacement = params.get("Replacement")
        self.Blocked = params.get("Blocked")
        self.Order = params.get("Order")


class ModifyPathRewriteResponse(AbstractModel):
    """ModifyPathRewrite返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true/false
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyTaskRequest(AbstractModel):
    """ModifyTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        :param TaskName: 任务名称
        :type TaskName: str
        :param TaskType: 任务类型
        :type TaskType: str
        :param TaskContent: 任务内容
        :type TaskContent: str
        :param ExecuteType: 任务执行类型
        :type ExecuteType: str
        :param TaskRule: 触发规则
        :type TaskRule: :class:`tencentcloud.tsf.v20180326.models.TaskRule`
        :param TimeOut: 超时时间，单位 ms
        :type TimeOut: int
        :param GroupId: 分组ID
        :type GroupId: str
        :param ShardCount: 分片数量
        :type ShardCount: int
        :param ShardArguments: 分片参数
        :type ShardArguments: :class:`tencentcloud.tsf.v20180326.models.ShardArgument`
        :param AdvanceSettings: 高级设置
        :type AdvanceSettings: :class:`tencentcloud.tsf.v20180326.models.AdvanceSettings`
        :param SuccessOperator: 判断任务成功的操作符 GT/GTE
        :type SuccessOperator: str
        :param SuccessRatio: 判断任务成功率的阈值
        :type SuccessRatio: int
        :param RetryCount: 重试次数
        :type RetryCount: int
        :param RetryInterval: 重试间隔
        :type RetryInterval: int
        :param TaskArgument: 任务参数，长度限制10000个字符
        :type TaskArgument: str
        """
        self.TaskId = None
        self.TaskName = None
        self.TaskType = None
        self.TaskContent = None
        self.ExecuteType = None
        self.TaskRule = None
        self.TimeOut = None
        self.GroupId = None
        self.ShardCount = None
        self.ShardArguments = None
        self.AdvanceSettings = None
        self.SuccessOperator = None
        self.SuccessRatio = None
        self.RetryCount = None
        self.RetryInterval = None
        self.TaskArgument = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.TaskType = params.get("TaskType")
        self.TaskContent = params.get("TaskContent")
        self.ExecuteType = params.get("ExecuteType")
        if params.get("TaskRule") is not None:
            self.TaskRule = TaskRule()
            self.TaskRule._deserialize(params.get("TaskRule"))
        self.TimeOut = params.get("TimeOut")
        self.GroupId = params.get("GroupId")
        self.ShardCount = params.get("ShardCount")
        if params.get("ShardArguments") is not None:
            self.ShardArguments = ShardArgument()
            self.ShardArguments._deserialize(params.get("ShardArguments"))
        if params.get("AdvanceSettings") is not None:
            self.AdvanceSettings = AdvanceSettings()
            self.AdvanceSettings._deserialize(params.get("AdvanceSettings"))
        self.SuccessOperator = params.get("SuccessOperator")
        self.SuccessRatio = params.get("SuccessRatio")
        self.RetryCount = params.get("RetryCount")
        self.RetryInterval = params.get("RetryInterval")
        self.TaskArgument = params.get("TaskArgument")


class ModifyTaskResponse(AbstractModel):
    """ModifyTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 更新是否成功
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
        :param RepositoryType: 程序包仓库类型
        :type RepositoryType: str
        :param RepositoryId: 程序包仓库id
        :type RepositoryId: str
        """
        self.ApplicationId = None
        self.PkgId = None
        self.Result = None
        self.Md5 = None
        self.Size = None
        self.RepositoryType = None
        self.RepositoryId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgId = params.get("PkgId")
        self.Result = params.get("Result")
        self.Md5 = params.get("Md5")
        self.Size = params.get("Size")
        self.RepositoryType = params.get("RepositoryType")
        self.RepositoryId = params.get("RepositoryId")


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


class MonitorOverview(AbstractModel):
    """监控概览对象

    """

    def __init__(self):
        """
        :param InvocationCountOfDay: 近24小时调用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationCountOfDay: str
        :param InvocationCount: 总调用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationCount: str
        :param ErrorCountOfDay: 近24小时调用错误数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCountOfDay: str
        :param ErrorCount: 总调用错误数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCount: str
        :param SuccessRatioOfDay: 近24小时调用成功率
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessRatioOfDay: str
        :param SuccessRatio: 总调用成功率
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessRatio: str
        """
        self.InvocationCountOfDay = None
        self.InvocationCount = None
        self.ErrorCountOfDay = None
        self.ErrorCount = None
        self.SuccessRatioOfDay = None
        self.SuccessRatio = None


    def _deserialize(self, params):
        self.InvocationCountOfDay = params.get("InvocationCountOfDay")
        self.InvocationCount = params.get("InvocationCount")
        self.ErrorCountOfDay = params.get("ErrorCountOfDay")
        self.ErrorCount = params.get("ErrorCount")
        self.SuccessRatioOfDay = params.get("SuccessRatioOfDay")
        self.SuccessRatio = params.get("SuccessRatio")


class MsApiArray(AbstractModel):
    """微服务API数组

    """

    def __init__(self):
        """
        :param Path: API 请求路径
        :type Path: str
        :param Method: 请求方法
        :type Method: str
        :param Description: 方法描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Status: API状态 0:离线 1:在线
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.Path = None
        self.Method = None
        self.Description = None
        self.Status = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.Description = params.get("Description")
        self.Status = params.get("Status")


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
        :param ServiceStatus: 服务状态，passing 在线，critical 离线
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceStatus: str
        :param RegistrationTime: 注册时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistrationTime: int
        :param LastHeartbeatTime: 上次心跳时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastHeartbeatTime: int
        :param RegistrationId: 实例注册id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistrationId: str
        :param HiddenStatus: 屏蔽状态，hidden 为屏蔽，unhidden 为未屏蔽
注意：此字段可能返回 null，表示取不到有效值。
        :type HiddenStatus: str
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
        self.ServiceStatus = None
        self.RegistrationTime = None
        self.LastHeartbeatTime = None
        self.RegistrationId = None
        self.HiddenStatus = None


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
        self.ServiceStatus = params.get("ServiceStatus")
        self.RegistrationTime = params.get("RegistrationTime")
        self.LastHeartbeatTime = params.get("LastHeartbeatTime")
        self.RegistrationId = params.get("RegistrationId")
        self.HiddenStatus = params.get("HiddenStatus")


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
        :param IsHaEnable: 是否开启高可用
注意：此字段可能返回 null，表示取不到有效值。
        :type IsHaEnable: str
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
        self.IsHaEnable = None


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
        self.IsHaEnable = params.get("IsHaEnable")


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


class OverviewBasicResourceUsage(AbstractModel):
    """TSF基本资源信息概览

    """

    def __init__(self):
        """
        :param ApplicationCount: 应用总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationCount: int
        :param NamespaceCount: 命名空间总数
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceCount: int
        :param GroupCount: 部署组个数
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupCount: int
        :param PackageSpaceUsed: 程序包存储空间用量，单位字节
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageSpaceUsed: int
        :param ConsulInstanceCount: 已注册实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsulInstanceCount: int
        """
        self.ApplicationCount = None
        self.NamespaceCount = None
        self.GroupCount = None
        self.PackageSpaceUsed = None
        self.ConsulInstanceCount = None


    def _deserialize(self, params):
        self.ApplicationCount = params.get("ApplicationCount")
        self.NamespaceCount = params.get("NamespaceCount")
        self.GroupCount = params.get("GroupCount")
        self.PackageSpaceUsed = params.get("PackageSpaceUsed")
        self.ConsulInstanceCount = params.get("ConsulInstanceCount")


class PathRewrite(AbstractModel):
    """路径重写

    """

    def __init__(self):
        """
        :param PathRewriteId: 路径重写规则ID
        :type PathRewriteId: str
        :param GatewayGroupId: 网关部署组ID
        :type GatewayGroupId: str
        :param Regex: 正则表达式
        :type Regex: str
        :param Replacement: 替换的内容
        :type Replacement: str
        :param Blocked: 是否屏蔽映射后路径，Y: 是 N: 否
        :type Blocked: str
        :param Order: 规则顺序，越小优先级越高
        :type Order: int
        """
        self.PathRewriteId = None
        self.GatewayGroupId = None
        self.Regex = None
        self.Replacement = None
        self.Blocked = None
        self.Order = None


    def _deserialize(self, params):
        self.PathRewriteId = params.get("PathRewriteId")
        self.GatewayGroupId = params.get("GatewayGroupId")
        self.Regex = params.get("Regex")
        self.Replacement = params.get("Replacement")
        self.Blocked = params.get("Blocked")
        self.Order = params.get("Order")


class PathRewriteCreateObject(AbstractModel):
    """路径重写创建对象

    """

    def __init__(self):
        """
        :param GatewayGroupId: 网关部署组ID
        :type GatewayGroupId: str
        :param Regex: 正则表达式
        :type Regex: str
        :param Replacement: 替换的内容
        :type Replacement: str
        :param Blocked: 是否屏蔽映射后路径，Y: 是 N: 否
        :type Blocked: str
        :param Order: 规则顺序，越小优先级越高
        :type Order: int
        """
        self.GatewayGroupId = None
        self.Regex = None
        self.Replacement = None
        self.Blocked = None
        self.Order = None


    def _deserialize(self, params):
        self.GatewayGroupId = params.get("GatewayGroupId")
        self.Regex = params.get("Regex")
        self.Replacement = params.get("Replacement")
        self.Blocked = params.get("Blocked")
        self.Order = params.get("Order")


class PathRewritePage(AbstractModel):
    """路径重写翻页对象

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param Content: 路径重写规则列表
        :type Content: list of PathRewrite
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = PathRewrite()
                obj._deserialize(item)
                self.Content.append(obj)


class PkgBind(AbstractModel):
    """描述程序包关联信息

    """

    def __init__(self):
        """
        :param ApplicationId: 应用id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param GroupId: 部署组id
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        """
        self.ApplicationId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.GroupId = params.get("GroupId")


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
        :param PkgBindInfo: 程序包关联关系
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgBindInfo: list of PkgBind
        """
        self.PkgId = None
        self.PkgName = None
        self.PkgType = None
        self.PkgVersion = None
        self.PkgDesc = None
        self.UploadTime = None
        self.Md5 = None
        self.PkgPubStatus = None
        self.PkgBindInfo = None


    def _deserialize(self, params):
        self.PkgId = params.get("PkgId")
        self.PkgName = params.get("PkgName")
        self.PkgType = params.get("PkgType")
        self.PkgVersion = params.get("PkgVersion")
        self.PkgDesc = params.get("PkgDesc")
        self.UploadTime = params.get("UploadTime")
        self.Md5 = params.get("Md5")
        self.PkgPubStatus = params.get("PkgPubStatus")
        if params.get("PkgBindInfo") is not None:
            self.PkgBindInfo = []
            for item in params.get("PkgBindInfo"):
                obj = PkgBind()
                obj._deserialize(item)
                self.PkgBindInfo.append(obj)


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
        :param RepositoryId: 程序包仓库id
注意：此字段可能返回 null，表示取不到有效值。
        :type RepositoryId: str
        :param RepositoryType: 程序包仓库类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RepositoryType: str
        :param RepositoryName: 程序包仓库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RepositoryName: str
        """
        self.TotalCount = None
        self.Content = None
        self.RepositoryId = None
        self.RepositoryType = None
        self.RepositoryName = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = PkgInfo()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RepositoryId = params.get("RepositoryId")
        self.RepositoryType = params.get("RepositoryType")
        self.RepositoryName = params.get("RepositoryName")


class PropertyField(AbstractModel):
    """属性字段

    """

    def __init__(self):
        """
        :param Name: 属性名称
        :type Name: str
        :param Type: 属性类型
        :type Type: str
        :param Description: 属性描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self.Name = None
        self.Type = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Description = params.get("Description")


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


class QuantileEntity(AbstractModel):
    """分位数据模型

    """

    def __init__(self):
        """
        :param MaxValue: 最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxValue: str
        :param MinValue: 最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type MinValue: str
        :param FifthPositionValue: 五分位值
注意：此字段可能返回 null，表示取不到有效值。
        :type FifthPositionValue: str
        :param NinthPositionValue: 九分位值
注意：此字段可能返回 null，表示取不到有效值。
        :type NinthPositionValue: str
        """
        self.MaxValue = None
        self.MinValue = None
        self.FifthPositionValue = None
        self.NinthPositionValue = None


    def _deserialize(self, params):
        self.MaxValue = params.get("MaxValue")
        self.MinValue = params.get("MinValue")
        self.FifthPositionValue = params.get("FifthPositionValue")
        self.NinthPositionValue = params.get("NinthPositionValue")


class RedoTaskBatchRequest(AbstractModel):
    """RedoTaskBatch请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        :param BatchId: 批次ID
        :type BatchId: str
        """
        self.TaskId = None
        self.BatchId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.BatchId = params.get("BatchId")


class RedoTaskBatchResponse(AbstractModel):
    """RedoTaskBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 批次ID
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RedoTaskExecuteRequest(AbstractModel):
    """RedoTaskExecute请求参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 任务批次ID
        :type BatchId: str
        :param ExecuteId: 任务执行ID
        :type ExecuteId: str
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.BatchId = None
        self.ExecuteId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.ExecuteId = params.get("ExecuteId")
        self.TaskId = params.get("TaskId")


class RedoTaskExecuteResponse(AbstractModel):
    """RedoTaskExecute返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RedoTaskFlowBatchRequest(AbstractModel):
    """RedoTaskFlowBatch请求参数结构体

    """

    def __init__(self):
        """
        :param FlowBatchId: 工作流批次 ID
        :type FlowBatchId: str
        """
        self.FlowBatchId = None


    def _deserialize(self, params):
        self.FlowBatchId = params.get("FlowBatchId")


class RedoTaskFlowBatchResponse(AbstractModel):
    """RedoTaskFlowBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 工作流批次历史 ID
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RedoTaskRequest(AbstractModel):
    """RedoTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class RedoTaskResponse(AbstractModel):
    """RedoTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作成功or失败
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ReleaseApiGroupRequest(AbstractModel):
    """ReleaseApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: Api 分组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class ReleaseApiGroupResponse(AbstractModel):
    """ReleaseApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功/失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


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


class RepositoryInfo(AbstractModel):
    """仓库信息

    """

    def __init__(self):
        """
        :param RepositoryId: 仓库ID
        :type RepositoryId: str
        :param RepositoryName: 仓库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RepositoryName: str
        :param RepositoryType: 仓库类型（默认仓库：default，私有仓库：private）
注意：此字段可能返回 null，表示取不到有效值。
        :type RepositoryType: str
        :param RepositoryDesc: 仓库描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RepositoryDesc: str
        :param IsUsed: 仓库是否正在被使用
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUsed: bool
        :param CreateTime: 仓库创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param BucketName: 仓库桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketName: str
        :param BucketRegion: 仓库桶所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketRegion: str
        :param Directory: 仓库目录
注意：此字段可能返回 null，表示取不到有效值。
        :type Directory: str
        """
        self.RepositoryId = None
        self.RepositoryName = None
        self.RepositoryType = None
        self.RepositoryDesc = None
        self.IsUsed = None
        self.CreateTime = None
        self.BucketName = None
        self.BucketRegion = None
        self.Directory = None


    def _deserialize(self, params):
        self.RepositoryId = params.get("RepositoryId")
        self.RepositoryName = params.get("RepositoryName")
        self.RepositoryType = params.get("RepositoryType")
        self.RepositoryDesc = params.get("RepositoryDesc")
        self.IsUsed = params.get("IsUsed")
        self.CreateTime = params.get("CreateTime")
        self.BucketName = params.get("BucketName")
        self.BucketRegion = params.get("BucketRegion")
        self.Directory = params.get("Directory")


class RepositoryList(AbstractModel):
    """仓库列表

    """

    def __init__(self):
        """
        :param TotalCount: 仓库总量
        :type TotalCount: int
        :param Content: 仓库信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of RepositoryInfo
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = RepositoryInfo()
                obj._deserialize(item)
                self.Content.append(obj)


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


class SchedulingStrategy(AbstractModel):
    """tsf 容器集群节点调度策略

    """

    def __init__(self):
        """
        :param Type: NONE：不使用调度策略；CROSS_AZ：跨可用区部署
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")


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


class ServiceSetting(AbstractModel):
    """容器网络设置。

    """

    def __init__(self):
        """
        :param AccessType: 0:公网 1:集群内访问 2：NodePort
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessType: int
        :param ProtocolPorts: 容器端口映射
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolPorts: list of ProtocolPort
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self.AccessType = None
        self.ProtocolPorts = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.AccessType = params.get("AccessType")
        if params.get("ProtocolPorts") is not None:
            self.ProtocolPorts = []
            for item in params.get("ProtocolPorts"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPorts.append(obj)
        self.SubnetId = params.get("SubnetId")


class ShardArgument(AbstractModel):
    """分片参数

    """

    def __init__(self):
        """
        :param ShardKey: 分片参数 KEY，整形
        :type ShardKey: int
        :param ShardValue: 分片参数 VALUE
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardValue: str
        """
        self.ShardKey = None
        self.ShardValue = None


    def _deserialize(self, params):
        self.ShardKey = params.get("ShardKey")
        self.ShardValue = params.get("ShardValue")


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
false：停止失败
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


class StopTaskBatchRequest(AbstractModel):
    """StopTaskBatch请求参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 批次ID
        :type BatchId: str
        :param TaskId: 参数ID
        :type TaskId: str
        """
        self.BatchId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.TaskId = params.get("TaskId")


class StopTaskBatchResponse(AbstractModel):
    """StopTaskBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作成功 or 失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class StopTaskExecuteRequest(AbstractModel):
    """StopTaskExecute请求参数结构体

    """

    def __init__(self):
        """
        :param ExecuteId: 任务执行ID
        :type ExecuteId: str
        :param BatchId: 任务批次ID
        :type BatchId: str
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.ExecuteId = None
        self.BatchId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ExecuteId = params.get("ExecuteId")
        self.BatchId = params.get("BatchId")
        self.TaskId = params.get("TaskId")


class StopTaskExecuteResponse(AbstractModel):
    """StopTaskExecute返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作成功 or 失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class TaskFlowEdge(AbstractModel):
    """工作流图中的边

    """

    def __init__(self):
        """
        :param NodeId: 节点 ID
        :type NodeId: str
        :param ChildNodeId: 子节点 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildNodeId: str
        :param CoreNode: 是否核心任务,Y/N
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreNode: str
        :param EdgeType: 边类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EdgeType: str
        :param NodeType: 任务节点类型
        :type NodeType: str
        :param PositionX: X轴坐标位置
注意：此字段可能返回 null，表示取不到有效值。
        :type PositionX: str
        :param PositionY: Y轴坐标位置
注意：此字段可能返回 null，表示取不到有效值。
        :type PositionY: str
        :param GraphId: 图 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GraphId: str
        :param FlowId: 工作流 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param NodeName: 节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TaskLogId: 任务历史ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskLogId: str
        """
        self.NodeId = None
        self.ChildNodeId = None
        self.CoreNode = None
        self.EdgeType = None
        self.NodeType = None
        self.PositionX = None
        self.PositionY = None
        self.GraphId = None
        self.FlowId = None
        self.NodeName = None
        self.TaskId = None
        self.TaskLogId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.ChildNodeId = params.get("ChildNodeId")
        self.CoreNode = params.get("CoreNode")
        self.EdgeType = params.get("EdgeType")
        self.NodeType = params.get("NodeType")
        self.PositionX = params.get("PositionX")
        self.PositionY = params.get("PositionY")
        self.GraphId = params.get("GraphId")
        self.FlowId = params.get("FlowId")
        self.NodeName = params.get("NodeName")
        self.TaskId = params.get("TaskId")
        self.TaskLogId = params.get("TaskLogId")


class TaskFlowLastBatchState(AbstractModel):
    """工作流最近批次的状态

    """

    def __init__(self):
        """
        :param FlowBatchId: 批次ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowBatchId: str
        :param FlowBatchLogId: 批次历史ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowBatchLogId: str
        :param State: 状态,WAITING/SUCCESS/FAILED/RUNNING/TERMINATING
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        """
        self.FlowBatchId = None
        self.FlowBatchLogId = None
        self.State = None


    def _deserialize(self, params):
        self.FlowBatchId = params.get("FlowBatchId")
        self.FlowBatchLogId = params.get("FlowBatchLogId")
        self.State = params.get("State")


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


class TaskLastExecuteStatus(AbstractModel):
    """任务最近一次执行状态

    """

    def __init__(self):
        """
        :param BatchId: 批次ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param State: 运行状态，RUNNING/SUCCESS/FAIL/HALF/TERMINATED
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param BatchLogId: 批次历史ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchLogId: str
        """
        self.BatchId = None
        self.State = None
        self.BatchLogId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.State = params.get("State")
        self.BatchLogId = params.get("BatchLogId")


class TaskRule(AbstractModel):
    """任务规则

    """

    def __init__(self):
        """
        :param RuleType: 触发规则类型, Cron/Repeat
        :type RuleType: str
        :param Expression: Cron类型规则，cron表达式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Expression: str
        :param RepeatInterval: 时间间隔， 单位毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type RepeatInterval: int
        """
        self.RuleType = None
        self.Expression = None
        self.RepeatInterval = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.Expression = params.get("Expression")
        self.RepeatInterval = params.get("RepeatInterval")


class TerminateTaskFlowBatchRequest(AbstractModel):
    """TerminateTaskFlowBatch请求参数结构体

    """

    def __init__(self):
        """
        :param FlowBatchId: 工作流批次 ID
        :type FlowBatchId: str
        """
        self.FlowBatchId = None


    def _deserialize(self, params):
        self.FlowBatchId = params.get("FlowBatchId")


class TerminateTaskFlowBatchResponse(AbstractModel):
    """TerminateTaskFlowBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否停止成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class TsfApiListResponse(AbstractModel):
    """TsfApiListResponse

    """

    def __init__(self):
        """
        :param TotalCount: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: API 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of MsApiArray
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = MsApiArray()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageApiGroupInfo(AbstractModel):
    """ApiGroupInfo翻页结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param Content: API分组信息
        :type Content: list of ApiGroupInfo
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ApiGroupInfo()
                obj._deserialize(item)
                self.Content.append(obj)


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


class TsfPageGatewayDeployGroup(AbstractModel):
    """GatewayDeployGroup 翻页对象

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param Content: 记录实体列表
        :type Content: list of GatewayDeployGroup
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = GatewayDeployGroup()
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


class UnbindApiGroupRequest(AbstractModel):
    """UnbindApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupGatewayList: 分组网关id列表
        :type GroupGatewayList: list of GatewayGroupIds
        """
        self.GroupGatewayList = None


    def _deserialize(self, params):
        if params.get("GroupGatewayList") is not None:
            self.GroupGatewayList = []
            for item in params.get("GroupGatewayList"):
                obj = GatewayGroupIds()
                obj._deserialize(item)
                self.GroupGatewayList.append(obj)


class UnbindApiGroupResponse(AbstractModel):
    """UnbindApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，成功失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateApiGroupRequest(AbstractModel):
    """UpdateApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: Api 分组ID
        :type GroupId: str
        :param GroupName: Api 分组名称
        :type GroupName: str
        :param Description: Api 分组描述
        :type Description: str
        :param AuthType: 鉴权类型
        :type AuthType: str
        :param GroupContext: 分组上下文
        :type GroupContext: str
        """
        self.GroupId = None
        self.GroupName = None
        self.Description = None
        self.AuthType = None
        self.GroupContext = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Description = params.get("Description")
        self.AuthType = params.get("AuthType")
        self.GroupContext = params.get("GroupContext")


class UpdateApiGroupResponse(AbstractModel):
    """UpdateApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，true: 成功, false: 失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateApiRateLimitRuleRequest(AbstractModel):
    """UpdateApiRateLimitRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 限流规则ID
        :type RuleId: str
        :param UsableStatus: 开启/禁用，enabled/disabled
        :type UsableStatus: str
        :param MaxQps: qps值，开启限流规则时，必填
        :type MaxQps: int
        """
        self.RuleId = None
        self.UsableStatus = None
        self.MaxQps = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.UsableStatus = params.get("UsableStatus")
        self.MaxQps = params.get("MaxQps")


class UpdateApiRateLimitRuleResponse(AbstractModel):
    """UpdateApiRateLimitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateApiRateLimitRulesRequest(AbstractModel):
    """UpdateApiRateLimitRules请求参数结构体

    """

    def __init__(self):
        """
        :param ApiIds: API ID 列表
        :type ApiIds: list of str
        :param UsableStatus: 开启/禁用，enabled/disabled
        :type UsableStatus: str
        :param MaxQps: QPS值。开启限流规则时，必填
        :type MaxQps: int
        """
        self.ApiIds = None
        self.UsableStatus = None
        self.MaxQps = None


    def _deserialize(self, params):
        self.ApiIds = params.get("ApiIds")
        self.UsableStatus = params.get("UsableStatus")
        self.MaxQps = params.get("MaxQps")


class UpdateApiRateLimitRulesResponse(AbstractModel):
    """UpdateApiRateLimitRules返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateGatewayApiRequest(AbstractModel):
    """UpdateGatewayApi请求参数结构体

    """

    def __init__(self):
        """
        :param ApiId: API ID
        :type ApiId: str
        :param Path: API 路径
        :type Path: str
        :param Method: Api 请求方法
        :type Method: str
        :param PathMapping: 请求映射
        :type PathMapping: str
        :param Host: api所在服务host
        :type Host: str
        :param Description: api描述信息
        :type Description: str
        """
        self.ApiId = None
        self.Path = None
        self.Method = None
        self.PathMapping = None
        self.Host = None
        self.Description = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.PathMapping = params.get("PathMapping")
        self.Host = params.get("Host")
        self.Description = params.get("Description")


class UpdateGatewayApiResponse(AbstractModel):
    """UpdateGatewayApi返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，成功失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateHealthCheckSettingsRequest(AbstractModel):
    """UpdateHealthCheckSettings请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
        :type GroupId: str
        :param EnableHealthCheck: 是否能使健康检查
        :type EnableHealthCheck: bool
        :param HealthCheckSettings: 健康检查配置
        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`
        """
        self.GroupId = None
        self.EnableHealthCheck = None
        self.HealthCheckSettings = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.EnableHealthCheck = params.get("EnableHealthCheck")
        if params.get("HealthCheckSettings") is not None:
            self.HealthCheckSettings = HealthCheckSettings()
            self.HealthCheckSettings._deserialize(params.get("HealthCheckSettings"))


class UpdateHealthCheckSettingsResponse(AbstractModel):
    """UpdateHealthCheckSettings返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 更新健康检查配置操作是否成功。
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


class UpdateRepositoryRequest(AbstractModel):
    """UpdateRepository请求参数结构体

    """

    def __init__(self):
        """
        :param RepositoryId: 仓库ID
        :type RepositoryId: str
        :param RepositoryDesc: 仓库描述
        :type RepositoryDesc: str
        """
        self.RepositoryId = None
        self.RepositoryDesc = None


    def _deserialize(self, params):
        self.RepositoryId = params.get("RepositoryId")
        self.RepositoryDesc = params.get("RepositoryDesc")


class UpdateRepositoryResponse(AbstractModel):
    """UpdateRepository返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 更新仓库是否成功
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
        :param DeployDesc: 部署应用描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployDesc: str
        :param UpdateType: 滚动发布的更新方式
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateType: int
        :param DeployBetaEnable: 发布是否启用beta批次
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployBetaEnable: bool
        :param DeployBatch: 滚动发布的批次比例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployBatch: list of float
        :param DeployExeMode: 滚动发布的批次执行方式
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployExeMode: str
        :param DeployWaitTime: 滚动发布的每个批次的等待时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployWaitTime: int
        :param EnableHealthCheck: 是否开启了健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableHealthCheck: bool
        :param HealthCheckSettings: 健康检查配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`
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
        self.DeployDesc = None
        self.UpdateType = None
        self.DeployBetaEnable = None
        self.DeployBatch = None
        self.DeployExeMode = None
        self.DeployWaitTime = None
        self.EnableHealthCheck = None
        self.HealthCheckSettings = None


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
        self.DeployDesc = params.get("DeployDesc")
        self.UpdateType = params.get("UpdateType")
        self.DeployBetaEnable = params.get("DeployBetaEnable")
        self.DeployBatch = params.get("DeployBatch")
        self.DeployExeMode = params.get("DeployExeMode")
        self.DeployWaitTime = params.get("DeployWaitTime")
        self.EnableHealthCheck = params.get("EnableHealthCheck")
        if params.get("HealthCheckSettings") is not None:
            self.HealthCheckSettings = HealthCheckSettings()
            self.HealthCheckSettings._deserialize(params.get("HealthCheckSettings"))


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
        :param DeployDesc: 部署应用描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployDesc: str
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
        self.DeployDesc = None


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
        self.DeployDesc = params.get("DeployDesc")