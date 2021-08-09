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


class AddClusterInstancesRequest(AbstractModel):
    """AddClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param InstanceIdList: 云主机ID列表\n        :type InstanceIdList: list of str\n        :param OsName: 操作系统名称\n        :type OsName: str\n        :param ImageId: 操作系统镜像ID\n        :type ImageId: str\n        :param Password: 重装系统密码设置\n        :type Password: str\n        :param KeyId: 重装系统，关联密钥设置\n        :type KeyId: str\n        :param SgId: 安全组设置\n        :type SgId: str\n        :param InstanceImportMode: 云主机导入方式，虚拟机集群必填，容器集群不填写此字段，R：重装TSF系统镜像，M：手动安装agent\n        :type InstanceImportMode: str\n        :param OsCustomizeType: 镜像定制类型\n        :type OsCustomizeType: str\n        :param FeatureIdList: 镜像特征ID列表\n        :type FeatureIdList: list of str\n        :param InstanceAdvancedSettings: 实例额外需要设置参数信息\n        :type InstanceAdvancedSettings: :class:`tencentcloud.tsf.v20180326.models.InstanceAdvancedSettings`\n        :param SecurityGroupIds: 安全组 ID 列表\n        :type SecurityGroupIds: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddClusterInstancesResponse(AbstractModel):
    """AddClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 添加云主机的返回列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.AddInstanceResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailedInstanceIds: list of str\n        :param SuccInstanceIds: 添加集群成功的节点列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccInstanceIds: list of str\n        :param TimeoutInstanceIds: 添加集群超时的节点列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeoutInstanceIds: list of str\n        :param FailedReasons: 失败的节点的失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailedReasons: list of str\n        """
        self.FailedInstanceIds = None
        self.SuccInstanceIds = None
        self.TimeoutInstanceIds = None
        self.FailedReasons = None


    def _deserialize(self, params):
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.TimeoutInstanceIds = params.get("TimeoutInstanceIds")
        self.FailedReasons = params.get("FailedReasons")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddInstancesRequest(AbstractModel):
    """AddInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param InstanceIdList: 云主机ID列表\n        :type InstanceIdList: list of str\n        :param OsName: 操作系统名称\n        :type OsName: str\n        :param ImageId: 操作系统镜像ID\n        :type ImageId: str\n        :param Password: 重装系统密码设置\n        :type Password: str\n        :param KeyId: 重装系统，关联密钥设置\n        :type KeyId: str\n        :param SgId: 安全组设置\n        :type SgId: str\n        :param InstanceImportMode: 云主机导入方式，虚拟机集群必填，容器集群不填写此字段，R：重装TSF系统镜像，M：手动安装agent\n        :type InstanceImportMode: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddInstancesResponse(AbstractModel):
    """AddInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 添加云主机是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SubTaskConcurrency: 子任务单机并发数限制，默认值为2\n        :type SubTaskConcurrency: int\n        """
        self.SubTaskConcurrency = None


    def _deserialize(self, params):
        self.SubTaskConcurrency = params.get("SubTaskConcurrency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiDefinitionDescr(AbstractModel):
    """API 对象类型描述

    """

    def __init__(self):
        """
        :param Name: 对象名称\n        :type Name: str\n        :param Properties: 对象属性列表\n        :type Properties: list of PropertyField\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiDetailInfo(AbstractModel):
    """API 明细

    """

    def __init__(self):
        """
        :param ApiId: API ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiId: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param MicroserviceId: 服务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroserviceId: str\n        :param MicroserviceName: 服务名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroserviceName: str\n        :param Path: API 请求路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        :param PathMapping: Api 映射路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type PathMapping: str\n        :param Method: 请求方法
注意：此字段可能返回 null，表示取不到有效值。\n        :type Method: str\n        :param GroupId: 所属分组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param UsableStatus: 是否禁用
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsableStatus: str\n        :param ReleaseStatus: 发布状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleaseStatus: str\n        :param RateLimitStatus: 开启限流
注意：此字段可能返回 null，表示取不到有效值。\n        :type RateLimitStatus: str\n        :param MockStatus: 是否开启mock
注意：此字段可能返回 null，表示取不到有效值。\n        :type MockStatus: str\n        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param UpdatedTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdatedTime: str\n        :param ReleasedTime: 发布时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleasedTime: str\n        :param GroupName: 所属分组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param Timeout: API 超时，单位毫秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type Timeout: int\n        :param Host: Api所在服务host
注意：此字段可能返回 null，表示取不到有效值。\n        :type Host: str\n        :param ApiType: API类型。 ms ： 微服务API； external :外部服务Api
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiType: str\n        :param Description: Api描述信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiDetailResponse(AbstractModel):
    """ApiDetailResponse描述

    """

    def __init__(self):
        """
        :param Request: API 请求参数\n        :type Request: list of ApiRequestDescr\n        :param Response: API 响应参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Response: list of ApiResponseDescr\n        :param Definitions: API 复杂结构定义\n        :type Definitions: list of ApiDefinitionDescr\n        :param RequestContentType: API 的 content type
注意：此字段可能返回 null，表示取不到有效值。\n        :type RequestContentType: str\n        :param CanRun: API  能否调试
注意：此字段可能返回 null，表示取不到有效值。\n        :type CanRun: bool\n        :param Status: API 状态 0:离线 1:在线，默认0
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param Description: API 描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiGroupInfo(AbstractModel):
    """API分组信息

    """

    def __init__(self):
        """
        :param GroupId: Api Group Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: Api Group 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param GroupContext: 分组上下文
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupContext: str\n        :param AuthType: 鉴权类型。 secret： 密钥鉴权； none:无鉴权
注意：此字段可能返回 null，表示取不到有效值。\n        :type AuthType: str\n        :param Status: 发布状态, drafted: 未发布。 released: 发布
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param CreatedTime: 分组创建时间 如:2019-06-20 15:51:28
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param UpdatedTime: 分组更新时间 如:2019-06-20 15:51:28
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdatedTime: str\n        :param BindedGatewayDeployGroups: api分组已绑定的网关部署组
注意：此字段可能返回 null，表示取不到有效值。\n        :type BindedGatewayDeployGroups: list of GatewayDeployGroup\n        :param ApiCount: api 个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiCount: int\n        :param AclMode: 访问group的ACL类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type AclMode: str\n        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param GroupType: 分组类型。 ms： 微服务分组； external:外部Api分组
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupType: str\n        :param GatewayInstanceType: 网关实例的类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type GatewayInstanceType: str\n        :param GatewayInstanceId: 网关实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GatewayInstanceId: str\n        """
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
        self.GatewayInstanceType = None
        self.GatewayInstanceId = None


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
        self.GatewayInstanceType = params.get("GatewayInstanceType")
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiInfo(AbstractModel):
    """微服务网关API信息

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间Id，若为外部API,为固定值："namespace-external"\n        :type NamespaceId: str\n        :param MicroserviceId: 服务Id，若为外部API,为固定值："ms-external"\n        :type MicroserviceId: str\n        :param Path: API path\n        :type Path: str\n        :param Method: Api 请求\n        :type Method: str\n        :param PathMapping: 请求映射\n        :type PathMapping: str\n        :param Host: api所在服务host,限定外部Api填写。格式: `http://127.0.0.1:8080`\n        :type Host: str\n        :param Description: api描述信息\n        :type Description: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiRateLimitRule(AbstractModel):
    """微服务网关API限流规则

    """

    def __init__(self):
        """
        :param RuleId: rule Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleId: str\n        :param ApiId: API ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiId: str\n        :param RuleName: 限流名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleName: str\n        :param MaxQps: 最大限流qps
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxQps: int\n        :param UsableStatus: 生效/禁用, enabled/disabled
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsableStatus: str\n        :param RuleContent: 规则内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleContent: str\n        :param TsfRuleId: Tsf Rule ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TsfRuleId: str\n        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param UpdatedTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdatedTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiRequestDescr(AbstractModel):
    """ApiRequestDescr

    """

    def __init__(self):
        """
        :param Name: 参数名称\n        :type Name: str\n        :param Type: 参数类型\n        :type Type: str\n        :param In: 参数位置\n        :type In: str\n        :param Description: 参数描述\n        :type Description: str\n        :param Required: 参数是否必须\n        :type Required: bool\n        :param DefaultValue: 参数的默认值
注意：此字段可能返回 null，表示取不到有效值。\n        :type DefaultValue: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiResponseDescr(AbstractModel):
    """API 响应的参数结构描述

    """

    def __init__(self):
        """
        :param Name: 参数描述\n        :type Name: str\n        :param Type: 参数类型\n        :type Type: str\n        :param Description: 参数描述\n        :type Description: str\n        """
        self.Name = None
        self.Type = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiUseStatisticsEntity(AbstractModel):
    """API 日统计数据点

    """

    def __init__(self):
        """
        :param Name: 名称\n        :type Name: str\n        :param Count: 次数\n        :type Count: str\n        :param Ratio: 比率\n        :type Ratio: str\n        """
        self.Name = None
        self.Count = None
        self.Ratio = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Count = params.get("Count")
        self.Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiVersionArray(AbstractModel):
    """API版本数组

    """

    def __init__(self):
        """
        :param ApplicationId: App ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: App 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param PkgVersion: App 包版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgVersion: str\n        """
        self.ApplicationId = None
        self.ApplicationName = None
        self.PkgVersion = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.PkgVersion = params.get("PkgVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationAttribute(AbstractModel):
    """应用列表其它字段

    """

    def __init__(self):
        """
        :param InstanceCount: 总实例个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceCount: int\n        :param RunInstanceCount: 运行实例个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type RunInstanceCount: int\n        :param GroupCount: 应用下部署组个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupCount: int\n        """
        self.InstanceCount = None
        self.RunInstanceCount = None
        self.GroupCount = None


    def _deserialize(self, params):
        self.InstanceCount = params.get("InstanceCount")
        self.RunInstanceCount = params.get("RunInstanceCount")
        self.GroupCount = params.get("GroupCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationForPage(AbstractModel):
    """分页的应用描述信息字段

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param ApplicationDesc: 应用描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationDesc: str\n        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationType: str\n        :param MicroserviceType: 微服务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroserviceType: str\n        :param ProgLang: 编程语言
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProgLang: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param ApplicationResourceType: 应用资源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationResourceType: str\n        :param ApplicationRuntimeType: 应用runtime类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationRuntimeType: str\n        :param ApigatewayServiceId: Apigateway的serviceId
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApigatewayServiceId: str\n        :param ApplicationRemarkName: 应用备注名
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationRemarkName: str\n        :param ServiceConfigList: 服务配置信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceConfigList: list of ServiceConfig\n        """
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
        self.ServiceConfigList = None


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
        if params.get("ServiceConfigList") is not None:
            self.ServiceConfigList = []
            for item in params.get("ServiceConfigList"):
                obj = ServiceConfig()
                obj._deserialize(item)
                self.ServiceConfigList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindApiGroupRequest(AbstractModel):
    """BindApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupGatewayList: 分组绑定网关列表\n        :type GroupGatewayList: list of GatewayGroupIds\n        """
        self.GroupGatewayList = None


    def _deserialize(self, params):
        if params.get("GroupGatewayList") is not None:
            self.GroupGatewayList = []
            for item in params.get("GroupGatewayList"):
                obj = GatewayGroupIds()
                obj._deserialize(item)
                self.GroupGatewayList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindApiGroupResponse(AbstractModel):
    """BindApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，成功失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindPluginRequest(AbstractModel):
    """BindPlugin请求参数结构体

    """

    def __init__(self):
        """
        :param PluginInstanceList: 分组/API绑定插件列表\n        :type PluginInstanceList: list of GatewayPluginBoundParam\n        """
        self.PluginInstanceList = None


    def _deserialize(self, params):
        if params.get("PluginInstanceList") is not None:
            self.PluginInstanceList = []
            for item in params.get("PluginInstanceList"):
                obj = GatewayPluginBoundParam()
                obj._deserialize(item)
                self.PluginInstanceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindPluginResponse(AbstractModel):
    """BindPlugin返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，成功失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BusinessLogV2(AbstractModel):
    """业务日志

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param Content: 日志内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: str\n        :param Timestamp: 日志时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type Timestamp: int\n        :param InstanceIp: 实例IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceIp: str\n        :param LogId: 日志ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogId: str\n        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        """
        self.InstanceId = None
        self.Content = None
        self.Timestamp = None
        self.InstanceIp = None
        self.LogId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Content = params.get("Content")
        self.Timestamp = params.get("Timestamp")
        self.InstanceIp = params.get("InstanceIp")
        self.LogId = params.get("LogId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeApiUsableStatusRequest(AbstractModel):
    """ChangeApiUsableStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ApiId: API ID\n        :type ApiId: str\n        :param UsableStatus: 切换状态，enabled/disabled\n        :type UsableStatus: str\n        """
        self.ApiId = None
        self.UsableStatus = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.UsableStatus = params.get("UsableStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeApiUsableStatusResponse(AbstractModel):
    """ChangeApiUsableStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API 信息\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApiDetailInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param ClusterDesc: 集群描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterDesc: str\n        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterType: str\n        :param VpcId: 集群所属私有网络ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param ClusterStatus: 集群状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterStatus: str\n        :param ClusterCIDR: 集群CIDR
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterCIDR: str\n        :param ClusterTotalCpu: 集群总CPU，单位: 核
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterTotalCpu: float\n        :param ClusterTotalMem: 集群总内存，单位: G
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterTotalMem: float\n        :param ClusterUsedCpu: 集群已使用CPU，单位: 核
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterUsedCpu: float\n        :param ClusterUsedMem: 集群已使用内存，单位: G
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterUsedMem: float\n        :param InstanceCount: 集群机器实例数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceCount: int\n        :param RunInstanceCount: 集群可用的机器实例数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type RunInstanceCount: int\n        :param NormalInstanceCount: 集群正常状态的机器实例数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type NormalInstanceCount: int\n        :param DeleteFlag: 删除标记：true：可以删除；false：不可删除
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeleteFlag: bool\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param TsfRegionId: 集群所属TSF地域ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TsfRegionId: str\n        :param TsfRegionName: 集群所属TSF地域名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TsfRegionName: str\n        :param TsfZoneId: 集群所属TSF可用区ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TsfZoneId: str\n        :param TsfZoneName: 集群所属TSF可用区名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TsfZoneName: str\n        :param DeleteFlagReason: 集群不可删除的原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeleteFlagReason: str\n        :param ClusterLimitCpu: 集群最大CPU限制，单位：核
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterLimitCpu: float\n        :param ClusterLimitMem: 集群最大内存限制，单位：G
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterLimitMem: float\n        :param RunServiceInstanceCount: 集群可用的服务实例数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type RunServiceInstanceCount: int\n        :param SubnetId: 集群所属子网ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: str\n        :param OperationInfo: 返回给前端的控制信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type OperationInfo: :class:`tencentcloud.tsf.v20180326.models.OperationInfo`\n        :param ClusterVersion: 集群版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterVersion: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Config(AbstractModel):
    """配置项

    """

    def __init__(self):
        """
        :param ConfigId: 配置项ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigId: str\n        :param ConfigName: 配置项名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigName: str\n        :param ConfigVersion: 配置项版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigVersion: str\n        :param ConfigVersionDesc: 配置项版本描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigVersionDesc: str\n        :param ConfigValue: 配置项值
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigValue: str\n        :param ConfigType: 配置项类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigType: str\n        :param CreationTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreationTime: str\n        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param DeleteFlag: 删除标识，true：可以删除；false：不可删除
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeleteFlag: bool\n        :param LastUpdateTime: 最后更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastUpdateTime: str\n        :param ConfigVersionCount: 配置项版本数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigVersionCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigRelease(AbstractModel):
    """配置项发布信息

    """

    def __init__(self):
        """
        :param ConfigReleaseId: 配置项发布ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigReleaseId: str\n        :param ConfigId: 配置项ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigId: str\n        :param ConfigName: 配置项名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigName: str\n        :param ConfigVersion: 配置项版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigVersion: str\n        :param ReleaseTime: 发布时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleaseTime: str\n        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param ReleaseDesc: 发布描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleaseDesc: str\n        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        """
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
        self.ApplicationId = None


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
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigReleaseLog(AbstractModel):
    """配置项发布日志

    """

    def __init__(self):
        """
        :param ConfigReleaseLogId: 配置项发布日志ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigReleaseLogId: str\n        :param ConfigId: 配置项ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigId: str\n        :param ConfigName: 配置项名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigName: str\n        :param ConfigVersion: 配置项版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigVersion: str\n        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param ReleaseTime: 发布时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleaseTime: str\n        :param ReleaseDesc: 发布描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleaseDesc: str\n        :param ReleaseStatus: 发布状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleaseStatus: str\n        :param LastConfigId: 上次发布的配置项ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastConfigId: str\n        :param LastConfigName: 上次发布的配置项名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastConfigName: str\n        :param LastConfigVersion: 上次发布的配置项版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastConfigVersion: str\n        :param RollbackFlag: 回滚标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type RollbackFlag: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainGroup(AbstractModel):
    """部署组列表（应用下钻界面的）

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param Server: 镜像server
注意：此字段可能返回 null，表示取不到有效值。\n        :type Server: str\n        :param RepoName: 镜像名，如/tsf/nginx
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepoName: str\n        :param TagName: 镜像版本名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagName: str\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param CpuRequest: 初始分配的 CPU 核数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。\n        :type CpuRequest: str\n        :param CpuLimit: 最大分配的 CPU 核数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。\n        :type CpuLimit: str\n        :param MemRequest: 初始分配的内存 MiB 数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemRequest: str\n        :param MemLimit: 最大分配的内存 MiB 数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemLimit: str\n        :param Alias: 部署组备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: str\n        """
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
        self.Alias = None


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
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainGroupResult(AbstractModel):
    """部署组列表（应用下钻）

    """

    def __init__(self):
        """
        :param Content: 部署组列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of ContainGroup\n        :param TotalCount: 总记录数\n        :type TotalCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerEvent(AbstractModel):
    """返回容器的事件，比如 k8s deployment 或者 pod 的 events

    """

    def __init__(self):
        """
        :param FirstTimestamp: 第一次出现的时间，以 ms 为单位的时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirstTimestamp: int\n        :param LastTimestamp: 最后一次出现的时间，以 ms 为单位的时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastTimestamp: int\n        :param Type: 级别
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Kind: 资源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Kind: str\n        :param Name: 资源名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Reason: 内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Reason: str\n        :param Message: 详细描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Message: str\n        :param Count: 出现次数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Count: int\n        """
        self.FirstTimestamp = None
        self.LastTimestamp = None
        self.Type = None
        self.Kind = None
        self.Name = None
        self.Reason = None
        self.Message = None
        self.Count = None


    def _deserialize(self, params):
        self.FirstTimestamp = params.get("FirstTimestamp")
        self.LastTimestamp = params.get("LastTimestamp")
        self.Type = params.get("Type")
        self.Kind = params.get("Kind")
        self.Name = params.get("Name")
        self.Reason = params.get("Reason")
        self.Message = params.get("Message")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerGroupDetail(AbstractModel):
    """容器部署组详情

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param InstanceNum: 实例总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceNum: int\n        :param CurrentNum: 已启动实例总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type CurrentNum: int\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param Server: 镜像server
注意：此字段可能返回 null，表示取不到有效值。\n        :type Server: str\n        :param Reponame: 镜像名，如/tsf/nginx
注意：此字段可能返回 null，表示取不到有效值。\n        :type Reponame: str\n        :param TagName: 镜像版本名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagName: str\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param LbIp: 负载均衡ip
注意：此字段可能返回 null，表示取不到有效值。\n        :type LbIp: str\n        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationType: str\n        :param ClusterIp: Service ip
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterIp: str\n        :param NodePort: NodePort端口，只有公网和NodePort访问方式才有值
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodePort: int\n        :param CpuLimit: 最大分配的 CPU 核数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。\n        :type CpuLimit: str\n        :param MemLimit: 最大分配的内存 MiB 数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemLimit: str\n        :param AccessType: 0:公网 1:集群内访问 2：NodePort
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessType: int\n        :param UpdateType: 更新方式：0:快速更新 1:滚动更新
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateType: int\n        :param UpdateIvl: 更新间隔,单位秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateIvl: int\n        :param ProtocolPorts: 端口数组对象
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProtocolPorts: list of ProtocolPort\n        :param Envs: 环境变量数组对象
注意：此字段可能返回 null，表示取不到有效值。\n        :type Envs: list of Env\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param Message: pod错误信息描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Message: str\n        :param Status: 部署组状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param MicroserviceType: 服务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroserviceType: str\n        :param CpuRequest: 初始分配的 CPU 核数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。\n        :type CpuRequest: str\n        :param MemRequest: 初始分配的内存 MiB 数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemRequest: str\n        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: str\n        :param GroupResourceType: 部署组资源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupResourceType: str\n        :param InstanceCount: 部署组实例个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceCount: int\n        :param UpdatedTime: 部署组更新时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdatedTime: int\n        :param MaxSurge: kubernetes滚动更新策略的MaxSurge参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxSurge: str\n        :param MaxUnavailable: kubernetes滚动更新策略的MaxUnavailable参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxUnavailable: str\n        :param HealthCheckSettings: 部署组健康检查设置
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`\n        """
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
        self.HealthCheckSettings = None


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
        if params.get("HealthCheckSettings") is not None:
            self.HealthCheckSettings = HealthCheckSettings()
            self.HealthCheckSettings._deserialize(params.get("HealthCheckSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueRunFailedTaskBatchRequest(AbstractModel):
    """ContinueRunFailedTaskBatch请求参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 批次ID。\n        :type BatchId: str\n        """
        self.BatchId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContinueRunFailedTaskBatchResponse(AbstractModel):
    """ContinueRunFailedTaskBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功或失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type SessionToken: str\n        :param TmpAppId: 临时应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TmpAppId: str\n        :param TmpSecretId: 临时调用者身份ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TmpSecretId: str\n        :param TmpSecretKey: 临时密钥
注意：此字段可能返回 null，表示取不到有效值。\n        :type TmpSecretKey: str\n        :param ExpiredTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpiredTime: int\n        :param Domain: 所在域
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosDownloadInfo(AbstractModel):
    """Cos下载所需信息

    """

    def __init__(self):
        """
        :param Bucket: 桶名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bucket: str\n        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param Path: 路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        :param Credentials: 鉴权信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Credentials: :class:`tencentcloud.tsf.v20180326.models.CosCredentials`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosUploadInfo(AbstractModel):
    """cos上传所需信息

    """

    def __init__(self):
        """
        :param PkgId: 程序包ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgId: str\n        :param Bucket: 桶
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bucket: str\n        :param Region: 目标地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param Path: 存储路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        :param Credentials: 鉴权信息\n        :type Credentials: :class:`tencentcloud.tsf.v20180326.models.CosCredentials`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAllGatewayApiAsyncRequest(AbstractModel):
    """CreateAllGatewayApiAsync请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: API分组ID\n        :type GroupId: str\n        :param MicroserviceId: 微服务ID\n        :type MicroserviceId: str\n        """
        self.GroupId = None
        self.MicroserviceId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.MicroserviceId = params.get("MicroserviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAllGatewayApiAsyncResponse(AbstractModel):
    """CreateAllGatewayApiAsync返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupName: 分组名称, 不能包含中文\n        :type GroupName: str\n        :param GroupContext: 分组上下文\n        :type GroupContext: str\n        :param AuthType: 鉴权类型。secret： 密钥鉴权； none:无鉴权\n        :type AuthType: str\n        :param Description: 备注\n        :type Description: str\n        :param GroupType: 分组类型,默认ms。 ms： 微服务分组； external:外部Api分组\n        :type GroupType: str\n        :param GatewayInstanceId: 网关实体ID\n        :type GatewayInstanceId: str\n        """
        self.GroupName = None
        self.GroupContext = None
        self.AuthType = None
        self.Description = None
        self.GroupType = None
        self.GatewayInstanceId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupContext = params.get("GroupContext")
        self.AuthType = params.get("AuthType")
        self.Description = params.get("Description")
        self.GroupType = params.get("GroupType")
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiGroupResponse(AbstractModel):
    """CreateApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API分组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApiId: Api Id\n        :type ApiId: str\n        :param MaxQps: qps值\n        :type MaxQps: int\n        :param UsableStatus: 开启/禁用，enabled/disabled, 不传默认开启\n        :type UsableStatus: str\n        """
        self.ApiId = None
        self.MaxQps = None
        self.UsableStatus = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.MaxQps = params.get("MaxQps")
        self.UsableStatus = params.get("UsableStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiRateLimitRuleResponse(AbstractModel):
    """CreateApiRateLimitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationName: 应用名称\n        :type ApplicationName: str\n        :param ApplicationType: 应用类型，V：虚拟机应用；C：容器应用；S：serverless应用\n        :type ApplicationType: str\n        :param MicroserviceType: 应用微服务类型，M：service mesh应用；N：普通应用；G：网关应用\n        :type MicroserviceType: str\n        :param ApplicationDesc: 应用描述\n        :type ApplicationDesc: str\n        :param ApplicationLogConfig: 应用日志配置项，废弃参数\n        :type ApplicationLogConfig: str\n        :param ApplicationResourceType: 应用资源类型，废弃参数\n        :type ApplicationResourceType: str\n        :param ApplicationRuntimeType: 应用runtime类型\n        :type ApplicationRuntimeType: str\n        :param ProgramId: 需要绑定的数据集ID\n        :type ProgramId: str\n        :param ServiceConfigList: 服务配置信息列表\n        :type ServiceConfigList: list of ServiceConfig\n        """
        self.ApplicationName = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ApplicationDesc = None
        self.ApplicationLogConfig = None
        self.ApplicationResourceType = None
        self.ApplicationRuntimeType = None
        self.ProgramId = None
        self.ServiceConfigList = None


    def _deserialize(self, params):
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationDesc = params.get("ApplicationDesc")
        self.ApplicationLogConfig = params.get("ApplicationLogConfig")
        self.ApplicationResourceType = params.get("ApplicationResourceType")
        self.ApplicationRuntimeType = params.get("ApplicationRuntimeType")
        self.ProgramId = params.get("ProgramId")
        if params.get("ServiceConfigList") is not None:
            self.ServiceConfigList = []
            for item in params.get("ServiceConfigList"):
                obj = ServiceConfig()
                obj._deserialize(item)
                self.ServiceConfigList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationResponse(AbstractModel):
    """CreateApplication返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param ClusterType: 集群类型\n        :type ClusterType: str\n        :param VpcId: 私有网络ID\n        :type VpcId: str\n        :param ClusterCIDR: 分配给集群容器和服务IP的CIDR\n        :type ClusterCIDR: str\n        :param ClusterDesc: 集群备注\n        :type ClusterDesc: str\n        :param TsfRegionId: 集群所属TSF地域\n        :type TsfRegionId: str\n        :param TsfZoneId: 集群所属TSF可用区\n        :type TsfZoneId: str\n        :param SubnetId: 私有网络子网ID\n        :type SubnetId: str\n        :param ClusterVersion: 集群版本\n        :type ClusterVersion: str\n        :param MaxNodePodNum: 集群中每个Node上最大的Pod数量。取值范围4～256。不为2的幂值时会向上取最接近的2的幂值。\n        :type MaxNodePodNum: int\n        :param MaxClusterServiceNum: 集群最大的service数量。取值范围32～32768，不为2的幂值时会向上取最接近的2的幂值。\n        :type MaxClusterServiceNum: int\n        :param ProgramId: 需要绑定的数据集ID\n        :type ProgramId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 集群ID\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigName: 配置项名称\n        :type ConfigName: str\n        :param ConfigVersion: 配置项版本\n        :type ConfigVersion: str\n        :param ConfigValue: 配置项值\n        :type ConfigValue: str\n        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        :param ConfigVersionDesc: 配置项版本描述\n        :type ConfigVersionDesc: str\n        :param ConfigType: 配置项值类型\n        :type ConfigType: str\n        :param EncodeWithBase64: Base64编码的配置项\n        :type EncodeWithBase64: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigResponse(AbstractModel):
    """CreateConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：创建成功；false：创建失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 分组所属应用ID\n        :type ApplicationId: str\n        :param NamespaceId: 分组所属命名空间ID\n        :type NamespaceId: str\n        :param GroupName: 分组名称字段，长度1~60，字母或下划线开头，可包含字母数字下划线\n        :type GroupName: str\n        :param InstanceNum: 实例数量\n        :type InstanceNum: int\n        :param AccessType: 0:公网 1:集群内访问 2：NodePort\n        :type AccessType: int\n        :param ProtocolPorts: 数组对象，见下方定义\n        :type ProtocolPorts: list of ProtocolPort\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param CpuLimit: 最大分配 CPU 核数，对应 K8S limit\n        :type CpuLimit: str\n        :param MemLimit: 最大分配内存 MiB 数，对应 K8S limit\n        :type MemLimit: str\n        :param GroupComment: 分组备注字段，长度应不大于200字符\n        :type GroupComment: str\n        :param UpdateType: 更新方式：0:快速更新 1:滚动更新\n        :type UpdateType: int\n        :param UpdateIvl: 滚动更新必填，更新间隔\n        :type UpdateIvl: int\n        :param CpuRequest: 初始分配的 CPU 核数，对应 K8S request\n        :type CpuRequest: str\n        :param MemRequest: 初始分配的内存 MiB 数，对应 K8S request\n        :type MemRequest: str\n        :param GroupResourceType: 部署组资源类型\n        :type GroupResourceType: str\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        :param AgentCpuRequest: agent 容器分配的 CPU 核数，对应 K8S 的 request\n        :type AgentCpuRequest: str\n        :param AgentCpuLimit: agent 容器最大的 CPU 核数，对应 K8S 的 limit\n        :type AgentCpuLimit: str\n        :param AgentMemRequest: agent 容器分配的内存 MiB 数，对应 K8S 的 request\n        :type AgentMemRequest: str\n        :param AgentMemLimit: agent 容器最大的内存 MiB 数，对应 K8S 的 limit\n        :type AgentMemLimit: str\n        :param IstioCpuRequest: istioproxy 容器分配的 CPU 核数，对应 K8S 的 request\n        :type IstioCpuRequest: str\n        :param IstioCpuLimit: istioproxy 容器最大的 CPU 核数，对应 K8S 的 limit\n        :type IstioCpuLimit: str\n        :param IstioMemRequest: istioproxy 容器分配的内存 MiB 数，对应 K8S 的 request\n        :type IstioMemRequest: str\n        :param IstioMemLimit: istioproxy 容器最大的内存 MiB 数，对应 K8S 的 limit\n        :type IstioMemLimit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContainGroupResponse(AbstractModel):
    """CreateContainGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回创建成功的部署组ID，返回null表示失败\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateFileConfigRequest(AbstractModel):
    """CreateFileConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigName: 配置项名称\n        :type ConfigName: str\n        :param ConfigVersion: 配置项版本\n        :type ConfigVersion: str\n        :param ConfigFileName: 配置项文件名\n        :type ConfigFileName: str\n        :param ConfigFileValue: 配置项文件内容（原始内容编码需要 utf-8 格式，如果 ConfigFileCode 为 gbk，后台会进行转换）\n        :type ConfigFileValue: str\n        :param ApplicationId: 配置项关联应用ID\n        :type ApplicationId: str\n        :param ConfigFilePath: 发布路径\n        :type ConfigFilePath: str\n        :param ConfigVersionDesc: 配置项版本描述\n        :type ConfigVersionDesc: str\n        :param ConfigFileCode: 配置项文件编码，utf-8 或 gbk。注：如果选择 gbk，需要新版本 tsf-consul-template （公有云虚拟机需要使用 1.32 tsf-agent，容器需要从文档中获取最新的 tsf-consul-template-docker.tar.gz）的支持\n        :type ConfigFileCode: str\n        :param ConfigPostCmd: 后置命令\n        :type ConfigPostCmd: str\n        :param EncodeWithBase64: Base64编码的配置项\n        :type EncodeWithBase64: bool\n        """
        self.ConfigName = None
        self.ConfigVersion = None
        self.ConfigFileName = None
        self.ConfigFileValue = None
        self.ApplicationId = None
        self.ConfigFilePath = None
        self.ConfigVersionDesc = None
        self.ConfigFileCode = None
        self.ConfigPostCmd = None
        self.EncodeWithBase64 = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ConfigFileName = params.get("ConfigFileName")
        self.ConfigFileValue = params.get("ConfigFileValue")
        self.ApplicationId = params.get("ApplicationId")
        self.ConfigFilePath = params.get("ConfigFilePath")
        self.ConfigVersionDesc = params.get("ConfigVersionDesc")
        self.ConfigFileCode = params.get("ConfigFileCode")
        self.ConfigPostCmd = params.get("ConfigPostCmd")
        self.EncodeWithBase64 = params.get("EncodeWithBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileConfigResponse(AbstractModel):
    """CreateFileConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：创建成功；false：创建失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: API 分组ID\n        :type GroupId: str\n        :param ApiList: Api信息\n        :type ApiList: list of ApiInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGatewayApiResponse(AbstractModel):
    """CreateGatewayApi返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 部署组所属的应用ID\n        :type ApplicationId: str\n        :param NamespaceId: 部署组所属命名空间ID\n        :type NamespaceId: str\n        :param GroupName: 部署组名称\n        :type GroupName: str\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param GroupDesc: 部署组描述\n        :type GroupDesc: str\n        :param GroupResourceType: 部署组资源类型\n        :type GroupResourceType: str\n        :param Alias: 部署组备注\n        :type Alias: str\n        """
        self.ApplicationId = None
        self.NamespaceId = None
        self.GroupName = None
        self.ClusterId = None
        self.GroupDesc = None
        self.GroupResourceType = None
        self.Alias = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupName = params.get("GroupName")
        self.ClusterId = params.get("ClusterId")
        self.GroupDesc = params.get("GroupDesc")
        self.GroupResourceType = params.get("GroupResourceType")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: groupId， null表示创建失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param LaneName: 泳道名称\n        :type LaneName: str\n        :param Remark: 泳道备注\n        :type Remark: str\n        :param LaneGroupList: 泳道部署组信息\n        :type LaneGroupList: list of LaneGroup\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLaneResponse(AbstractModel):
    """CreateLane返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 泳道ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleName: 泳道规则名称\n        :type RuleName: str\n        :param Remark: 泳道规则备注\n        :type Remark: str\n        :param RuleTagList: 泳道规则标签列表\n        :type RuleTagList: list of LaneRuleTag\n        :param RuleTagRelationship: 泳道规则标签关系\n        :type RuleTagRelationship: str\n        :param LaneId: 泳道Id\n        :type LaneId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLaneRuleResponse(AbstractModel):
    """CreateLaneRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 泳道规则Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param NamespaceId: 命名空间ID\n        :type NamespaceId: str\n        :param MicroserviceName: 微服务名称\n        :type MicroserviceName: str\n        :param MicroserviceDesc: 微服务描述信息\n        :type MicroserviceDesc: str\n        """
        self.NamespaceId = None
        self.MicroserviceName = None
        self.MicroserviceDesc = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.MicroserviceName = params.get("MicroserviceName")
        self.MicroserviceDesc = params.get("MicroserviceDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMicroserviceResponse(AbstractModel):
    """CreateMicroservice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 新增微服务是否成功。
true：操作成功。
false：操作失败。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param NamespaceName: 命名空间名称\n        :type NamespaceName: str\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param NamespaceDesc: 命名空间描述\n        :type NamespaceDesc: str\n        :param NamespaceResourceType: 命名空间资源类型(默认值为DEF)\n        :type NamespaceResourceType: str\n        :param NamespaceType: 是否是全局命名空间(默认是DEF，表示普通命名空间；GLOBAL表示全局命名空间)\n        :type NamespaceType: str\n        :param NamespaceId: 命名空间ID\n        :type NamespaceId: str\n        :param IsHaEnable: 是否开启高可用\n        :type IsHaEnable: str\n        :param ProgramId: 需要绑定的数据集ID\n        :type ProgramId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功时为命名空间ID，失败为null
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param PathRewrites: 路径重写列表\n        :type PathRewrites: :class:`tencentcloud.tsf.v20180326.models.PathRewriteCreateObject`\n        """
        self.PathRewrites = None


    def _deserialize(self, params):
        if params.get("PathRewrites") is not None:
            self.PathRewrites = PathRewriteCreateObject()
            self.PathRewrites._deserialize(params.get("PathRewrites"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePathRewritesResponse(AbstractModel):
    """CreatePathRewrites返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true/false\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigName: 配置项名称\n        :type ConfigName: str\n        :param ConfigVersion: 配置项版本\n        :type ConfigVersion: str\n        :param ConfigValue: 配置项值，总是接收yaml格式的内容\n        :type ConfigValue: str\n        :param ConfigVersionDesc: 配置项版本描述\n        :type ConfigVersionDesc: str\n        :param ConfigType: 配置项类型\n        :type ConfigType: str\n        :param EncodeWithBase64: Base64编码的配置项\n        :type EncodeWithBase64: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePublicConfigResponse(AbstractModel):
    """CreatePublicConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：创建成功；false：创建失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RepositoryName: 仓库名称\n        :type RepositoryName: str\n        :param RepositoryType: 仓库类型（默认仓库：default，私有仓库：private）\n        :type RepositoryType: str\n        :param BucketName: 仓库所在桶名称\n        :type BucketName: str\n        :param BucketRegion: 仓库所在桶地域\n        :type BucketRegion: str\n        :param Directory: 目录\n        :type Directory: str\n        :param RepositoryDesc: 仓库描述\n        :type RepositoryDesc: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRepositoryResponse(AbstractModel):
    """CreateRepository返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建仓库是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 分组所属应用ID\n        :type ApplicationId: str\n        :param GroupName: 分组名称字段，长度1~60，字母或下划线开头，可包含字母数字下划线\n        :type GroupName: str\n        :param NamespaceId: 分组所属名字空间ID\n        :type NamespaceId: str\n        :param ClusterId: 分组所属集群ID\n        :type ClusterId: str\n        """
        self.ApplicationId = None
        self.GroupName = None
        self.NamespaceId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.GroupName = params.get("GroupName")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerlessGroupResponse(AbstractModel):
    """CreateServerlessGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建成功的部署组ID，返回null表示失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param FlowName: 工作流名称\n        :type FlowName: str\n        :param TriggerRule: 触发方式\n        :type TriggerRule: :class:`tencentcloud.tsf.v20180326.models.TaskRule`\n        :param FlowEdges: 工作流任务节点列表\n        :type FlowEdges: list of TaskFlowEdge\n        :param TimeOut: 工作流执行超时时间\n        :type TimeOut: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFlowResponse(AbstractModel):
    """CreateTaskFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 工作流 ID\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TaskName: 任务名称，任务长度64字符\n        :type TaskName: str\n        :param TaskContent: 任务内容，长度限制65536个字节\n        :type TaskContent: str\n        :param ExecuteType: 执行类型，unicast/broadcast\n        :type ExecuteType: str\n        :param TaskType: 任务类型,java\n        :type TaskType: str\n        :param TimeOut: 任务超时时间， 时间单位 ms\n        :type TimeOut: int\n        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param TaskRule: 触发规则\n        :type TaskRule: :class:`tencentcloud.tsf.v20180326.models.TaskRule`\n        :param RetryCount: 重试次数，0 <= RetryCount<= 10\n        :type RetryCount: int\n        :param RetryInterval: 重试间隔， 0 <= RetryInterval <= 600000， 时间单位 ms\n        :type RetryInterval: int\n        :param ShardCount: 分片数量\n        :type ShardCount: int\n        :param ShardArguments: 分片参数\n        :type ShardArguments: list of ShardArgument\n        :param SuccessOperator: 判断任务成功的操作符\n        :type SuccessOperator: str\n        :param SuccessRatio: 判断任务成功率的阈值，如100\n        :type SuccessRatio: str\n        :param AdvanceSettings: 高级设置\n        :type AdvanceSettings: :class:`tencentcloud.tsf.v20180326.models.AdvanceSettings`\n        :param TaskArgument: 任务参数，长度限制10000个字符\n        :type TaskArgument: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    """CreateTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateUnitRuleRequest(AbstractModel):
    """CreateUnitRule请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayInstanceId: 网关实体ID\n        :type GatewayInstanceId: str\n        :param Name: 规则名称\n        :type Name: str\n        :param Description: 规则描述\n        :type Description: str\n        :param UnitRuleItemList: 规则项列表\n        :type UnitRuleItemList: list of UnitRuleItem\n        """
        self.GatewayInstanceId = None
        self.Name = None
        self.Description = None
        self.UnitRuleItemList = None


    def _deserialize(self, params):
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("UnitRuleItemList") is not None:
            self.UnitRuleItemList = []
            for item in params.get("UnitRuleItemList"):
                obj = UnitRuleItem()
                obj._deserialize(item)
                self.UnitRuleItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUnitRuleResponse(AbstractModel):
    """CreateUnitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: API 分组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiGroupResponse(AbstractModel):
    """DeleteApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationResponse(AbstractModel):
    """DeleteApplication返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除应用操作是否成功。
true：操作成功。
false：操作失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigId: 配置项ID\n        :type ConfigId: str\n        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigResponse(AbstractModel):
    """DeleteConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：删除成功；false：删除失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID，分组唯一标识\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteContainerGroupResponse(AbstractModel):
    """DeleteContainerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除操作是否成功：
true：成功
false：失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除部署组操作是否成功。
true：操作成功。
false：操作失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RepoName: 仓库名，如/tsf/nginx\n        :type RepoName: str\n        :param TagName: 版本号:如V1\n        :type TagName: str\n        """
        self.RepoName = None
        self.TagName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageTagsRequest(AbstractModel):
    """DeleteImageTags请求参数结构体

    """

    def __init__(self):
        """
        :param ImageTags: 镜像版本数组\n        :type ImageTags: list of DeleteImageTag\n        """
        self.ImageTags = None


    def _deserialize(self, params):
        if params.get("ImageTags") is not None:
            self.ImageTags = []
            for item in params.get("ImageTags"):
                obj = DeleteImageTag()
                obj._deserialize(item)
                self.ImageTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageTagsResponse(AbstractModel):
    """DeleteImageTags返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 批量删除操作是否成功。
true：成功。
false：失败。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param LaneId: 泳道Idl\n        :type LaneId: str\n        """
        self.LaneId = None


    def _deserialize(self, params):
        self.LaneId = params.get("LaneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaneResponse(AbstractModel):
    """DeleteLane返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true / false\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param MicroserviceId: 微服务ID\n        :type MicroserviceId: str\n        """
        self.MicroserviceId = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMicroserviceResponse(AbstractModel):
    """DeleteMicroservice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除微服务是否成功。
true：操作成功。
false：操作失败。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param NamespaceId: 命名空间ID\n        :type NamespaceId: str\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.NamespaceId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除命名空间是否成功。
true：删除成功。
false：删除失败。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param PathRewriteIds: 路径重写规则IDs\n        :type PathRewriteIds: list of str\n        """
        self.PathRewriteIds = None


    def _deserialize(self, params):
        self.PathRewriteIds = params.get("PathRewriteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePathRewritesResponse(AbstractModel):
    """DeletePathRewrites返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true/false\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        :param PkgIds: 需要删除的程序包ID列表\n        :type PkgIds: list of str\n        :param RepositoryType: 程序包仓库类型\n        :type RepositoryType: str\n        :param RepositoryId: 程序包仓库id\n        :type RepositoryId: str\n        """
        self.ApplicationId = None
        self.PkgIds = None
        self.RepositoryType = None
        self.RepositoryId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgIds = params.get("PkgIds")
        self.RepositoryType = params.get("RepositoryType")
        self.RepositoryId = params.get("RepositoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePkgsResponse(AbstractModel):
    """DeletePkgs返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePublicConfigRequest(AbstractModel):
    """DeletePublicConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置项ID\n        :type ConfigId: str\n        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePublicConfigResponse(AbstractModel):
    """DeletePublicConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：删除成功；false：删除失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RepositoryId: 仓库ID\n        :type RepositoryId: str\n        """
        self.RepositoryId = None


    def _deserialize(self, params):
        self.RepositoryId = params.get("RepositoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRepositoryResponse(AbstractModel):
    """DeleteRepository返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除仓库是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: groupId，分组唯一标识\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServerlessGroupResponse(AbstractModel):
    """DeleteServerlessGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果true：成功；false：失败。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TaskId: 任务ID\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskResponse(AbstractModel):
    """DeleteTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除成功or失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteUnitNamespacesRequest(AbstractModel):
    """DeleteUnitNamespaces请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayInstanceId: 网关实体ID\n        :type GatewayInstanceId: str\n        :param UnitNamespaceList: 单元化命名空间ID数组\n        :type UnitNamespaceList: list of str\n        """
        self.GatewayInstanceId = None
        self.UnitNamespaceList = None


    def _deserialize(self, params):
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        self.UnitNamespaceList = params.get("UnitNamespaceList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUnitNamespacesResponse(AbstractModel):
    """DeleteUnitNamespaces返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteUnitRuleRequest(AbstractModel):
    """DeleteUnitRule请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 规则ID\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUnitRuleResponse(AbstractModel):
    """DeleteUnitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID，分组唯一标识\n        :type GroupId: str\n        :param TagName: 镜像版本名称,如v1\n        :type TagName: str\n        :param InstanceNum: 实例数量\n        :type InstanceNum: int\n        :param Server: 镜像server\n        :type Server: str\n        :param Reponame: 旧版镜像名，如/tsf/nginx\n        :type Reponame: str\n        :param CpuLimit: 业务容器最大的 CPU 核数，对应 K8S 的 limit；不填时默认为 request 的 2 倍\n        :type CpuLimit: str\n        :param MemLimit: 业务容器最大的内存 MiB 数，对应 K8S 的 limit；不填时默认为 request 的 2 倍\n        :type MemLimit: str\n        :param JvmOpts: jvm参数\n        :type JvmOpts: str\n        :param CpuRequest: 业务容器分配的 CPU 核数，对应 K8S 的 request\n        :type CpuRequest: str\n        :param MemRequest: 业务容器分配的内存 MiB 数，对应 K8S 的 request\n        :type MemRequest: str\n        :param DoNotStart: 是否不立即启动\n        :type DoNotStart: bool\n        :param RepoName: （优先使用）新版镜像名，如/tsf/nginx\n        :type RepoName: str\n        :param UpdateType: 更新方式：0:快速更新 1:滚动更新\n        :type UpdateType: int\n        :param UpdateIvl: 滚动更新必填，更新间隔\n        :type UpdateIvl: int\n        :param AgentCpuRequest: agent 容器分配的 CPU 核数，对应 K8S 的 request\n        :type AgentCpuRequest: str\n        :param AgentCpuLimit: agent 容器最大的 CPU 核数，对应 K8S 的 limit\n        :type AgentCpuLimit: str\n        :param AgentMemRequest: agent 容器分配的内存 MiB 数，对应 K8S 的 request\n        :type AgentMemRequest: str\n        :param AgentMemLimit: agent 容器最大的内存 MiB 数，对应 K8S 的 limit\n        :type AgentMemLimit: str\n        :param IstioCpuRequest: istioproxy 容器分配的 CPU 核数，对应 K8S 的 request\n        :type IstioCpuRequest: str\n        :param IstioCpuLimit: istioproxy 容器最大的 CPU 核数，对应 K8S 的 limit\n        :type IstioCpuLimit: str\n        :param IstioMemRequest: istioproxy 容器分配的内存 MiB 数，对应 K8S 的 request\n        :type IstioMemRequest: str\n        :param IstioMemLimit: istioproxy 容器最大的内存 MiB 数，对应 K8S 的 limit\n        :type IstioMemLimit: str\n        :param MaxSurge: kubernetes滚动更新策略的MaxSurge参数\n        :type MaxSurge: str\n        :param MaxUnavailable: kubernetes滚动更新策略的MaxUnavailable参数\n        :type MaxUnavailable: str\n        :param HealthCheckSettings: 健康检查配置信息，若不指定该参数，则默认不设置健康检查。\n        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`\n        :param Envs: 部署组应用运行的环境变量。若不指定该参数，则默认不设置额外的环境变量。\n        :type Envs: list of Env\n        :param ServiceSetting: 容器部署组的网络设置。\n        :type ServiceSetting: :class:`tencentcloud.tsf.v20180326.models.ServiceSetting`\n        :param DeployAgent: 是否部署 agent 容器。若不指定该参数，则默认不部署 agent 容器。\n        :type DeployAgent: bool\n        :param SchedulingStrategy: 节点调度策略。若不指定改参数，则默认不使用节点调度策略。\n        :type SchedulingStrategy: :class:`tencentcloud.tsf.v20180326.models.SchedulingStrategy`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployContainerGroupResponse(AbstractModel):
    """DeployContainerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 部署容器应用是否成功。
true：成功。
false：失败。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param PkgId: 程序包ID\n        :type PkgId: str\n        :param StartupParameters: 部署组启动参数\n        :type StartupParameters: str\n        :param DeployDesc: 部署应用描述信息\n        :type DeployDesc: str\n        :param ForceStart: 是否允许强制启动\n        :type ForceStart: bool\n        :param EnableHealthCheck: 是否开启健康检查\n        :type EnableHealthCheck: bool\n        :param HealthCheckSettings: 开启健康检查时，配置健康检查\n        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`\n        :param UpdateType: 部署方式，0表示快速更新，1表示滚动更新\n        :type UpdateType: int\n        :param DeployBetaEnable: 是否启用beta批次\n        :type DeployBetaEnable: bool\n        :param DeployBatch: 滚动发布每个批次参与的实例比率\n        :type DeployBatch: list of float\n        :param DeployExeMode: 滚动发布的执行方式\n        :type DeployExeMode: str\n        :param DeployWaitTime: 滚动发布每个批次的时间间隔\n        :type DeployWaitTime: int\n        :param StartScript: 启动脚本 base64编码\n        :type StartScript: str\n        :param StopScript: 停止脚本 base64编码\n        :type StopScript: str\n        """
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
        self.StartScript = None
        self.StopScript = None


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
        self.StartScript = params.get("StartScript")
        self.StopScript = params.get("StopScript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployGroupResponse(AbstractModel):
    """DeployGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param PkgId: 程序包ID\n        :type PkgId: str\n        :param Memory: 所需实例内存大小，取值为 1Gi 2Gi 4Gi 8Gi 16Gi，缺省为 1Gi，不传表示维持原态\n        :type Memory: str\n        :param InstanceRequest: 要求最小实例数，取值范围 [1, 4]，缺省为 1，不传表示维持原态\n        :type InstanceRequest: int\n        :param StartupParameters: 部署组启动参数，不传表示维持原态\n        :type StartupParameters: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployServerlessGroupResponse(AbstractModel):
    """DeployServerlessGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果true：成功；false：失败；\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param MicroserviceId: 微服务id\n        :type MicroserviceId: str\n        :param Path: 请求路径\n        :type Path: str\n        :param Method: 请求方法\n        :type Method: str\n        :param PkgVersion: 包版本\n        :type PkgVersion: str\n        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiDetailResponse(AbstractModel):
    """DescribeApiDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API 详情\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApiDetailResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: API 分组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiGroupResponse(AbstractModel):
    """DescribeApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API分组信息\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApiGroupInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SearchWord: 搜索关键字\n        :type SearchWord: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 每页条数，默认为20\n        :type Limit: int\n        :param GroupType: 分组类型。 ms： 微服务分组； external:外部Api分组\n        :type GroupType: str\n        :param AuthType: 鉴权类型。 secret： 秘钥鉴权； none:无鉴权\n        :type AuthType: str\n        :param Status: 发布状态, drafted: 未发布。 released: 发布\n        :type Status: str\n        :param OrderBy: 排序字段："created_time"或"group_context"\n        :type OrderBy: str\n        :param OrderType: 排序类型：0(ASC)或1(DESC)\n        :type OrderType: int\n        :param GatewayInstanceId: 网关实体ID\n        :type GatewayInstanceId: str\n        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.GroupType = None
        self.AuthType = None
        self.Status = None
        self.OrderBy = None
        self.OrderType = None
        self.GatewayInstanceId = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupType = params.get("GroupType")
        self.AuthType = params.get("AuthType")
        self.Status = params.get("Status")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiGroupsResponse(AbstractModel):
    """DescribeApiGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 翻页结构体\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageApiGroupInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApiId: Api ID\n        :type ApiId: str\n        """
        self.ApiId = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiRateLimitRulesResponse(AbstractModel):
    """DescribeApiRateLimitRules返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 限流结果\n        :type Result: list of ApiRateLimitRule\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GatewayDeployGroupId: 网关部署组ID\n        :type GatewayDeployGroupId: str\n        :param ApiId: 网关分组Api ID\n        :type ApiId: str\n        :param StartTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss\n        :type StartTime: str\n        :param EndTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss\n        :type EndTime: str\n        """
        self.GatewayDeployGroupId = None
        self.ApiId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.ApiId = params.get("ApiId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiUseDetailResponse(AbstractModel):
    """DescribeApiUseDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 日使用统计对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.GroupApiUseStatistics`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param MicroserviceId: 微服务ID\n        :type MicroserviceId: str\n        :param Path: API 请求路径\n        :type Path: str\n        :param Method: 请求方法\n        :type Method: str\n        """
        self.MicroserviceId = None
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiVersionsResponse(AbstractModel):
    """DescribeApiVersions返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API版本列表\n        :type Result: list of ApiVersionArray\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationAttributeResponse(AbstractModel):
    """DescribeApplicationAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 应用列表其它字段返回参数\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApplicationAttribute`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationResponse(AbstractModel):
    """DescribeApplication返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 应用信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApplicationForPage`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SearchWord: 搜索字段\n        :type SearchWord: str\n        :param OrderBy: 排序字段\n        :type OrderBy: str\n        :param OrderType: 排序类型\n        :type OrderType: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 分页个数\n        :type Limit: int\n        :param ApplicationType: 应用类型\n        :type ApplicationType: str\n        :param MicroserviceType: 应用的微服务类型\n        :type MicroserviceType: str\n        :param ApplicationResourceTypeList: 应用资源类型数组\n        :type ApplicationResourceTypeList: list of str\n        :param ApplicationIdList: IdList\n        :type ApplicationIdList: list of str\n        """
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ApplicationResourceTypeList = None
        self.ApplicationIdList = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationResourceTypeList = params.get("ApplicationResourceTypeList")
        self.ApplicationIdList = params.get("ApplicationIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 应用分页列表信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageApplication`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.OverviewBasicResourceUsage`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param SearchWord: 搜索字段\n        :type SearchWord: str\n        :param OrderBy: 排序字段\n        :type OrderBy: str\n        :param OrderType: 排序类型\n        :type OrderType: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 分页个数\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 集群机器实例分页信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageInstance`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID，不传入时查询全量\n        :type GroupId: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 每页条数，默认为20\n        :type Limit: int\n        :param NamespaceId: 命名空间ID，不传入时查询全量\n        :type NamespaceId: str\n        :param ClusterId: 集群ID，不传入时查询全量\n        :type ClusterId: str\n        :param ApplicationId: 应用ID，不传入时查询全量\n        :type ApplicationId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigReleaseLogsResponse(AbstractModel):
    """DescribeConfigReleaseLogs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页的配置项发布历史列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigReleaseLog`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigName: 配置项名称，不传入时查询全量\n        :type ConfigName: str\n        :param GroupId: 部署组ID，不传入时查询全量\n        :type GroupId: str\n        :param NamespaceId: 命名空间ID，不传入时查询全量\n        :type NamespaceId: str\n        :param ClusterId: 集群ID，不传入时查询全量\n        :type ClusterId: str\n        :param Limit: 每页条数\n        :type Limit: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param ConfigId: 配置ID，不传入时查询全量\n        :type ConfigId: str\n        :param ApplicationId: 应用ID，不传入时查询全量\n        :type ApplicationId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigReleasesResponse(AbstractModel):
    """DescribeConfigReleases返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页的配置发布信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigRelease`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigId: 配置项ID\n        :type ConfigId: str\n        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 配置项
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.Config`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用ID，不传入时查询全量\n        :type ApplicationId: str\n        :param SearchWord: 查询关键字，模糊查询：应用名称，配置项名称，不传入时查询全量\n        :type SearchWord: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 每页条数，默认为20\n        :type Limit: int\n        :param OrderBy: 按时间排序：creation_time；按名称排序：config_name\n        :type OrderBy: str\n        :param OrderType: 升序传 0，降序传 1\n        :type OrderType: int\n        """
        self.ApplicationId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderType = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigSummaryResponse(AbstractModel):
    """DescribeConfigSummary返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 配置项分页对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用ID，不传入时查询全量\n        :type ApplicationId: str\n        :param ConfigId: 配置项ID，不传入时查询全量，高优先级\n        :type ConfigId: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 每页条数\n        :type Limit: int\n        :param ConfigIdList: 配置项ID列表，不传入时查询全量，低优先级\n        :type ConfigIdList: list of str\n        :param ConfigName: 配置项名称，精确查询，不传入时查询全量\n        :type ConfigName: str\n        :param ConfigVersion: 配置项版本，精确查询，不传入时查询全量\n        :type ConfigVersion: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigsResponse(AbstractModel):
    """DescribeConfigs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页后的配置项列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeContainerEventsRequest(AbstractModel):
    """DescribeContainerEvents请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceType: event 的资源类型, group 或者 instance\n        :type ResourceType: str\n        :param ResourceId: event 的资源 id\n        :type ResourceId: str\n        :param Offset: 偏移量，取值从0开始\n        :type Offset: int\n        :param Limit: 分页个数，默认为20， 取值应为1~50\n        :type Limit: int\n        :param GroupId: 当类型是 instance 时需要\n        :type GroupId: str\n        """
        self.ResourceType = None
        self.ResourceId = None
        self.Offset = None
        self.Limit = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerEventsResponse(AbstractModel):
    """DescribeContainerEvents返回参数结构体

    """

    def __init__(self):
        """
        :param Result: events 分页列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageContainerEvent`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageContainerEvent()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeContainerGroupDetailRequest(AbstractModel):
    """DescribeContainerGroupDetail请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 分组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerGroupDetailResponse(AbstractModel):
    """DescribeContainerGroupDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 容器部署组详情\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ContainerGroupDetail`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SearchWord: 搜索字段，模糊搜索groupName字段\n        :type SearchWord: str\n        :param ApplicationId: 分组所属应用ID\n        :type ApplicationId: str\n        :param OrderBy: 排序字段，默认为 createTime字段，支持id， name， createTime\n        :type OrderBy: str\n        :param OrderType: 排序方式，默认为1：倒序排序，0：正序，1：倒序\n        :type OrderType: int\n        :param Offset: 偏移量，取值从0开始\n        :type Offset: int\n        :param Limit: 分页个数，默认为20， 取值应为1~50\n        :type Limit: int\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param NamespaceId: 命名空间 ID\n        :type NamespaceId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerGroupsResponse(AbstractModel):
    """DescribeContainerGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询的权限数据对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ContainGroupResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 请求方法\n        :type GroupId: str\n        :param MicroserviceId: 微服务ID\n        :type MicroserviceId: str\n        """
        self.GroupId = None
        self.MicroserviceId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.MicroserviceId = params.get("MicroserviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCreateGatewayApiStatusResponse(AbstractModel):
    """DescribeCreateGatewayApiStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否已完成导入任务\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        :param PkgId: 程序包ID\n        :type PkgId: str\n        :param RepositoryId: 程序包仓库ID\n        :type RepositoryId: str\n        :param RepositoryType: 程序包仓库类型\n        :type RepositoryType: str\n        """
        self.ApplicationId = None
        self.PkgId = None
        self.RepositoryId = None
        self.RepositoryType = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgId = params.get("PkgId")
        self.RepositoryId = params.get("RepositoryId")
        self.RepositoryType = params.get("RepositoryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDownloadInfoResponse(AbstractModel):
    """DescribeDownloadInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: COS鉴权信息\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.CosDownloadInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CosDownloadInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeEnabledUnitRuleRequest(AbstractModel):
    """DescribeEnabledUnitRule请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayInstanceId: 网关实体ID\n        :type GatewayInstanceId: str\n        """
        self.GatewayInstanceId = None


    def _deserialize(self, params):
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnabledUnitRuleResponse(AbstractModel):
    """DescribeEnabledUnitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 单元化规则对象
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.UnitRule`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UnitRule()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeFileConfigsRequest(AbstractModel):
    """DescribeFileConfigs请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置项ID\n        :type ConfigId: str\n        :param ConfigIdList: 配置项ID列表\n        :type ConfigIdList: list of str\n        :param ConfigName: 配置项名称\n        :type ConfigName: str\n        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 每页条数\n        :type Limit: int\n        :param ConfigVersion: 配置项版本\n        :type ConfigVersion: str\n        """
        self.ConfigId = None
        self.ConfigIdList = None
        self.ConfigName = None
        self.ApplicationId = None
        self.Offset = None
        self.Limit = None
        self.ConfigVersion = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.ConfigIdList = params.get("ConfigIdList")
        self.ConfigName = params.get("ConfigName")
        self.ApplicationId = params.get("ApplicationId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ConfigVersion = params.get("ConfigVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileConfigsResponse(AbstractModel):
    """DescribeFileConfigs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 文件配置项列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageFileConfig`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageFileConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeFlowLastBatchStateRequest(AbstractModel):
    """DescribeFlowLastBatchState请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 工作流 ID\n        :type FlowId: str\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowLastBatchStateResponse(AbstractModel):
    """DescribeFlowLastBatchState返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 工作流批次最新状态\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskFlowLastBatchState`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GatewayDeployGroupId: 网关部署组ID\n        :type GatewayDeployGroupId: str\n        :param SearchWord: 搜索关键字，支持分组名称或API Path\n        :type SearchWord: str\n        """
        self.GatewayDeployGroupId = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayAllGroupApisResponse(AbstractModel):
    """DescribeGatewayAllGroupApis返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 网关分组和API列表信息\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.GatewayVo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GatewayDeployGroupId: 网关部署组ID\n        :type GatewayDeployGroupId: str\n        """
        self.GatewayDeployGroupId = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayMonitorOverviewResponse(AbstractModel):
    """DescribeGatewayMonitorOverview返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 监控概览对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.MonitorOverview`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: API 分组ID\n        :type GroupId: str\n        :param Offset: 翻页查询偏移量\n        :type Offset: int\n        :param Limit: 翻页查询每页记录数\n        :type Limit: int\n        :param SearchWord: 搜索关键字\n        :type SearchWord: str\n        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupBindedGatewaysResponse(AbstractModel):
    """DescribeGroupBindedGateways返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 翻页结构体\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageGatewayDeployGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GatewayDeployGroupId: 网关部署组ID\n        :type GatewayDeployGroupId: str\n        :param Offset: 翻页查询偏移量\n        :type Offset: int\n        :param Limit: 翻页查询每页记录数\n        :type Limit: int\n        :param SearchWord: 搜索关键字\n        :type SearchWord: str\n        """
        self.GatewayDeployGroupId = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupGatewaysResponse(AbstractModel):
    """DescribeGroupGateways返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API分组信息\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageApiGroupInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param SearchWord: 搜索字段\n        :type SearchWord: str\n        :param OrderBy: 排序字段\n        :type OrderBy: str\n        :param OrderType: 排序类型\n        :type OrderType: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 分页个数\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInstancesResponse(AbstractModel):
    """DescribeGroupInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 部署组机器信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageInstance`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 虚拟机部署组详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.VmGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GatewayDeployGroupId: 网关部署组ID\n        :type GatewayDeployGroupId: str\n        :param GroupId: 网关分组ID\n        :type GroupId: str\n        :param StartTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss\n        :type StartTime: str\n        :param EndTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss\n        :type EndTime: str\n        :param Count: 指定top的条数,默认为10\n        :type Count: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupUseDetailResponse(AbstractModel):
    """DescribeGroupUseDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 日使用统计对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.GroupDailyUseStatistics`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SearchWord: 搜索字段\n        :type SearchWord: str\n        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        :param OrderBy: 排序字段\n        :type OrderBy: str\n        :param OrderType: 排序方式\n        :type OrderType: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 分页个数\n        :type Limit: int\n        :param NamespaceId: 命名空间ID\n        :type NamespaceId: str\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param GroupResourceTypeList: 部署组资源类型列表\n        :type GroupResourceTypeList: list of str\n        :param Status: 部署组状态过滤字段\n        :type Status: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupsResponse(AbstractModel):
    """DescribeGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 虚拟机部署组分页信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageVmGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageVmGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupsWithPluginRequest(AbstractModel):
    """DescribeGroupsWithPlugin请求参数结构体

    """

    def __init__(self):
        """
        :param PluginId: 插件ID\n        :type PluginId: str\n        :param Bound: 绑定/未绑定: true / false\n        :type Bound: bool\n        :param Offset: 翻页偏移量\n        :type Offset: int\n        :param Limit: 每页记录数量\n        :type Limit: int\n        :param SearchWord: 搜索关键字\n        :type SearchWord: str\n        :param GatewayInstanceId: 网关实体ID\n        :type GatewayInstanceId: str\n        """
        self.PluginId = None
        self.Bound = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None
        self.GatewayInstanceId = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.Bound = params.get("Bound")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupsWithPluginResponse(AbstractModel):
    """DescribeGroupsWithPlugin返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API分组信息列表\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageApiGroupInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageApiGroupInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeImageRepositoryRequest(AbstractModel):
    """DescribeImageRepository请求参数结构体

    """

    def __init__(self):
        """
        :param SearchWord: 仓库名，搜索关键字,不带命名空间的\n        :type SearchWord: str\n        :param Offset: 偏移量，取值从0开始\n        :type Offset: int\n        :param Limit: 分页个数，默认为20， 取值应为1~100\n        :type Limit: int\n        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageRepositoryResponse(AbstractModel):
    """DescribeImageRepository返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询的权限数据对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ImageRepositoryResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用Id\n        :type ApplicationId: str\n        :param Offset: 偏移量，取值从0开始\n        :type Offset: int\n        :param Limit: 分页个数，默认为20， 取值应为1~100\n        :type Limit: int\n        :param QueryImageIdFlag: 不填和0:查询 1:不查询\n        :type QueryImageIdFlag: int\n        :param SearchWord: 可用于搜索的 tag 名字\n        :type SearchWord: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageTagsResponse(AbstractModel):
    """DescribeImageTags返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询的权限数据对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ImageTagsResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Limit: 每页展示的条数\n        :type Limit: int\n        :param Offset: 翻页偏移量\n        :type Offset: int\n        :param SearchWord: 搜索关键词\n        :type SearchWord: str\n        :param RuleId: 泳道规则ID（用于精确搜索）\n        :type RuleId: str\n        """
        self.Limit = None
        self.Offset = None
        self.SearchWord = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SearchWord = params.get("SearchWord")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLaneRulesResponse(AbstractModel):
    """DescribeLaneRules返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 泳道规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.LaneRules`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Limit: 每页展示的条数\n        :type Limit: int\n        :param Offset: 翻页偏移量\n        :type Offset: int\n        :param SearchWord: 搜索关键字\n        :type SearchWord: str\n        """
        self.Limit = None
        self.Offset = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLanesResponse(AbstractModel):
    """DescribeLanes返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 泳道列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.LaneInfos`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param MicroserviceId: 微服务ID\n        :type MicroserviceId: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 分页个数\n        :type Limit: int\n        :param GroupIds: 可选，根据部署组ID进行过滤\n        :type GroupIds: list of str\n        """
        self.MicroserviceId = None
        self.Offset = None
        self.Limit = None
        self.GroupIds = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMicroserviceResponse(AbstractModel):
    """DescribeMicroservice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 微服务详情实例列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageMsInstance`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param NamespaceId: 命名空间ID\n        :type NamespaceId: str\n        :param SearchWord: 搜索字段\n        :type SearchWord: str\n        :param OrderBy: 排序字段\n        :type OrderBy: str\n        :param OrderType: 排序类型\n        :type OrderType: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 分页个数\n        :type Limit: int\n        :param Status: 状态过滤，online、offline、single_online\n        :type Status: list of str\n        :param MicroserviceIdList: IdList\n        :type MicroserviceIdList: list of str\n        """
        self.NamespaceId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.MicroserviceIdList = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.MicroserviceIdList = params.get("MicroserviceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMicroservicesResponse(AbstractModel):
    """DescribeMicroservices返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 微服务分页列表信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageMicroservice`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param MicroserviceId: 微服务ID\n        :type MicroserviceId: str\n        :param SearchWord: 搜索关键字\n        :type SearchWord: str\n        :param Limit: 每页的数量\n        :type Limit: int\n        :param Offset: 翻页偏移量\n        :type Offset: int\n        """
        self.MicroserviceId = None
        self.SearchWord = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.SearchWord = params.get("SearchWord")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMsApiListResponse(AbstractModel):
    """DescribeMsApiList返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 相应结果\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfApiListResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param PathRewriteId: 路径重写规则ID\n        :type PathRewriteId: str\n        """
        self.PathRewriteId = None


    def _deserialize(self, params):
        self.PathRewriteId = params.get("PathRewriteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePathRewriteResponse(AbstractModel):
    """DescribePathRewrite返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 路径重写规则对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.PathRewrite`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GatewayGroupId: 网关部署组ID\n        :type GatewayGroupId: str\n        :param SearchWord: 根据正则表达式或替换的内容模糊查询\n        :type SearchWord: str\n        :param Limit: 每页数量\n        :type Limit: int\n        :param Offset: 起始偏移量\n        :type Offset: int\n        """
        self.GatewayGroupId = None
        self.SearchWord = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.GatewayGroupId = params.get("GatewayGroupId")
        self.SearchWord = params.get("SearchWord")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePathRewritesResponse(AbstractModel):
    """DescribePathRewrites返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 路径重写翻页对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.PathRewritePage`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用ID（只传入应用ID，返回该应用下所有软件包信息）\n        :type ApplicationId: str\n        :param SearchWord: 查询关键字（支持根据包ID，包名，包版本号搜索）\n        :type SearchWord: str\n        :param OrderBy: 排序关键字（默认为"UploadTime"：上传时间）\n        :type OrderBy: str\n        :param OrderType: 升序：0/降序：1（默认降序）\n        :type OrderType: int\n        :param Offset: 查询起始偏移\n        :type Offset: int\n        :param Limit: 返回数量限制\n        :type Limit: int\n        :param RepositoryType: 程序包仓库类型\n        :type RepositoryType: str\n        :param RepositoryId: 程序包仓库id\n        :type RepositoryId: str\n        :param PackageTypeList: 程序包类型数组支持（fatjar jar war tar.gz zip）\n        :type PackageTypeList: list of str\n        """
        self.ApplicationId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.RepositoryType = None
        self.RepositoryId = None
        self.PackageTypeList = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.RepositoryType = params.get("RepositoryType")
        self.RepositoryId = params.get("RepositoryId")
        self.PackageTypeList = params.get("PackageTypeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePkgsResponse(AbstractModel):
    """DescribePkgs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 符合查询程序包信息列表\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.PkgList`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = PkgList()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePluginInstancesRequest(AbstractModel):
    """DescribePluginInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ScopeValue: 分组或者API的ID\n        :type ScopeValue: str\n        :param Bound: 绑定: true; 未绑定: false\n        :type Bound: bool\n        :param Offset: 翻页偏移量\n        :type Offset: int\n        :param Limit: 每页展示的条数\n        :type Limit: int\n        :param Type: 插件类型\n        :type Type: str\n        :param SearchWord: 搜索关键字\n        :type SearchWord: str\n        """
        self.ScopeValue = None
        self.Bound = None
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.ScopeValue = params.get("ScopeValue")
        self.Bound = params.get("Bound")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginInstancesResponse(AbstractModel):
    """DescribePluginInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 插件信息列表\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageGatewayPlugin`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageGatewayPlugin()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePodInstancesRequest(AbstractModel):
    """DescribePodInstances请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 实例所属groupId\n        :type GroupId: str\n        :param Offset: 偏移量，取值从0开始\n        :type Offset: int\n        :param Limit: 分页个数，默认为20， 取值应为1~50\n        :type Limit: int\n        :param PodNameList: 过滤字段\n        :type PodNameList: list of str\n        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None
        self.PodNameList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PodNameList = params.get("PodNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePodInstancesResponse(AbstractModel):
    """DescribePodInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询的权限数据对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.GroupPodResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param NamespaceId: 命名空间ID，不传入时查询全量\n        :type NamespaceId: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 每页条数，默认为20\n        :type Limit: int\n        """
        self.NamespaceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicConfigReleaseLogsResponse(AbstractModel):
    """DescribePublicConfigReleaseLogs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页后的公共配置项发布历史列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigReleaseLog`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigName: 配置项名称，不传入时查询全量\n        :type ConfigName: str\n        :param NamespaceId: 命名空间ID，不传入时查询全量\n        :type NamespaceId: str\n        :param Limit: 每页条数\n        :type Limit: int\n        :param Offset: 偏移量\n        :type Offset: int\n        :param ConfigId: 配置项ID，不传入时查询全量\n        :type ConfigId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicConfigReleasesResponse(AbstractModel):
    """DescribePublicConfigReleases返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 公共配置发布信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigRelease`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigId: 需要查询的配置项ID\n        :type ConfigId: str\n        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicConfigResponse(AbstractModel):
    """DescribePublicConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 全局配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.Config`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SearchWord: 查询关键字，模糊查询：配置项名称，不传入时查询全量\n        :type SearchWord: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 每页条数，默认为20\n        :type Limit: int\n        :param OrderBy: 按时间排序：creation_time；按名称排序：config_name\n        :type OrderBy: str\n        :param OrderType: 升序传 0，降序传 1\n        :type OrderType: int\n        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderType = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicConfigSummaryResponse(AbstractModel):
    """DescribePublicConfigSummary返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页的全局配置统计信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigId: 配置项ID，不传入时查询全量，高优先级\n        :type ConfigId: str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 每页条数，默认为20\n        :type Limit: int\n        :param ConfigIdList: 配置项ID列表，不传入时查询全量，低优先级\n        :type ConfigIdList: list of str\n        :param ConfigName: 配置项名称，精确查询，不传入时查询全量\n        :type ConfigName: str\n        :param ConfigVersion: 配置项版本，精确查询，不传入时查询全量\n        :type ConfigVersion: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicConfigsResponse(AbstractModel):
    """DescribePublicConfigs返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页后的全局配置项列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleasedConfigResponse(AbstractModel):
    """DescribeReleasedConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 已发布的配置内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SearchWord: 查询关键字（按照仓库名称搜索）\n        :type SearchWord: str\n        :param Offset: 查询起始偏移\n        :type Offset: int\n        :param Limit: 返回数量限制\n        :type Limit: int\n        :param RepositoryType: 仓库类型（默认仓库：default，私有仓库：private）\n        :type RepositoryType: str\n        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.RepositoryType = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.RepositoryType = params.get("RepositoryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoriesResponse(AbstractModel):
    """DescribeRepositories返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 符合查询仓库信息列表\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.RepositoryList`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RepositoryId: 仓库ID\n        :type RepositoryId: str\n        """
        self.RepositoryId = None


    def _deserialize(self, params):
        self.RepositoryId = params.get("RepositoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRepositoryResponse(AbstractModel):
    """DescribeRepository返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询的仓库信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.RepositoryInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerlessGroupResponse(AbstractModel):
    """DescribeServerlessGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ServerlessGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SearchWord: 搜索字段，模糊搜索groupName字段\n        :type SearchWord: str\n        :param ApplicationId: 分组所属应用ID\n        :type ApplicationId: str\n        :param OrderBy: 排序字段，默认为 createTime字段，支持id， name， createTime\n        :type OrderBy: str\n        :param OrderType: 排序方式，默认为1：倒序排序，0：正序，1：倒序\n        :type OrderType: str\n        :param Offset: 偏移量，取值从0开始\n        :type Offset: int\n        :param Limit: 分页个数，默认为20， 取值应为1~50\n        :type Limit: int\n        :param NamespaceId: 分组所属名字空间ID\n        :type NamespaceId: str\n        :param ClusterId: 分组所属集群ID\n        :type ClusterId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerlessGroupsResponse(AbstractModel):
    """DescribeServerlessGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 数据列表对象
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.ServerlessGroupPage`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationIdList: 应用ID列表\n        :type ApplicationIdList: list of str\n        :param ApplicationType: 应用类型\n        :type ApplicationType: str\n        :param Limit: 每页条数\n        :type Limit: int\n        :param Offset: 起始偏移量\n        :type Offset: int\n        :param MicroserviceType: 微服务类型\n        :type MicroserviceType: str\n        :param ApplicationResourceTypeList: 资源类型数组\n        :type ApplicationResourceTypeList: list of str\n        :param SearchWord: 通过id和name进行关键词过滤\n        :type SearchWord: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSimpleApplicationsResponse(AbstractModel):
    """DescribeSimpleApplications返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 简单应用分页对象
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageSimpleApplication`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ClusterIdList: 需要查询的集群ID列表，不填或不传入时查询所有内容\n        :type ClusterIdList: list of str\n        :param ClusterType: 需要查询的集群类型，不填或不传入时查询所有内容\n        :type ClusterType: str\n        :param Offset: 查询偏移量，默认为0\n        :type Offset: int\n        :param Limit: 分页个数，默认为20， 取值应为1~50\n        :type Limit: int\n        :param SearchWord: 对id和name进行关键词过滤\n        :type SearchWord: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSimpleClustersResponse(AbstractModel):
    """DescribeSimpleClusters返回参数结构体

    """

    def __init__(self):
        """
        :param Result: TSF集群分页对象
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageCluster`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupIdList: 部署组ID列表，不填写时查询全量\n        :type GroupIdList: list of str\n        :param ApplicationId: 应用ID，不填写时查询全量\n        :type ApplicationId: str\n        :param ClusterId: 集群ID，不填写时查询全量\n        :type ClusterId: str\n        :param NamespaceId: 命名空间ID，不填写时查询全量\n        :type NamespaceId: str\n        :param Limit: 每页条数\n        :type Limit: int\n        :param Offset: 起始偏移量\n        :type Offset: int\n        :param GroupId: 部署组ID，不填写时查询全量\n        :type GroupId: str\n        :param SearchWord: 模糊查询，部署组名称，不填写时查询全量\n        :type SearchWord: str\n        :param AppMicroServiceType: 部署组类型，精确过滤字段，M：service mesh, P：原生应用， G：网关应用\n        :type AppMicroServiceType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSimpleGroupsResponse(AbstractModel):
    """DescribeSimpleGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 简单部署组列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageSimpleGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param NamespaceIdList: 命名空间ID列表，不传入时查询全量\n        :type NamespaceIdList: list of str\n        :param ClusterId: 集群ID，不传入时查询全量\n        :type ClusterId: str\n        :param Limit: 每页条数\n        :type Limit: int\n        :param Offset: 起始偏移量\n        :type Offset: int\n        :param NamespaceId: 命名空间ID，不传入时查询全量\n        :type NamespaceId: str\n        :param NamespaceResourceTypeList: 查询资源类型列表\n        :type NamespaceResourceTypeList: list of str\n        :param SearchWord: 通过id和name进行过滤\n        :type SearchWord: str\n        :param NamespaceTypeList: 查询的命名空间类型列表\n        :type NamespaceTypeList: list of str\n        :param NamespaceName: 通过命名空间名精确过滤\n        :type NamespaceName: str\n        :param IsDefault: 通过是否是默认命名空间过滤，不传表示拉取全部命名空间。0：默认，命名空间。1：非默认命名空间\n        :type IsDefault: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSimpleNamespacesResponse(AbstractModel):
    """DescribeSimpleNamespaces返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 命名空间分页列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageNamespace`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageNamespace()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: str\n        :param TaskLogId: 任务历史ID\n        :type TaskLogId: str\n        """
        self.TaskId = None
        self.TaskLogId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskLogId = params.get("TaskLogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务详情\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskRecord`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskRecord()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTaskLastStatusRequest(AbstractModel):
    """DescribeTaskLastStatus请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLastStatusResponse(AbstractModel):
    """DescribeTaskLastStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务上一次执行状态\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskLastExecuteStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskLastExecuteStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTaskRecordsRequest(AbstractModel):
    """DescribeTaskRecords请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 翻页偏移量。\n        :type Offset: int\n        :param Limit: 翻页查询单页数量。\n        :type Limit: int\n        :param SearchWord: 模糊查询关键字，支持任务ID和任务名称。\n        :type SearchWord: str\n        :param TaskState: 任务启用状态。enabled/disabled\n        :type TaskState: str\n        :param GroupId: 分组ID。\n        :type GroupId: str\n        :param TaskType: 任务类型。\n        :type TaskType: str\n        :param ExecuteType: 任务触发类型，UNICAST、BROADCAST。\n        :type ExecuteType: str\n        """
        self.Offset = None
        self.Limit = None
        self.SearchWord = None
        self.TaskState = None
        self.GroupId = None
        self.TaskType = None
        self.ExecuteType = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        self.TaskState = params.get("TaskState")
        self.GroupId = params.get("GroupId")
        self.TaskType = params.get("TaskType")
        self.ExecuteType = params.get("ExecuteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskRecordsResponse(AbstractModel):
    """DescribeTaskRecords返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务记录列表\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskRecordPage`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskRecordPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUnitApiUseDetailRequest(AbstractModel):
    """DescribeUnitApiUseDetail请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayDeployGroupId: 网关部署组ID\n        :type GatewayDeployGroupId: str\n        :param ApiId: 网关分组Api ID\n        :type ApiId: str\n        :param StartTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss\n        :type StartTime: str\n        :param EndTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss\n        :type EndTime: str\n        :param GatewayInstanceId: 网关实例ID\n        :type GatewayInstanceId: str\n        :param GroupId: 网关分组ID\n        :type GroupId: str\n        :param Offset: 翻页查询偏移量\n        :type Offset: int\n        :param Limit: 翻页查询每页记录数\n        :type Limit: int\n        :param Period: 监控统计数据粒度\n        :type Period: int\n        """
        self.GatewayDeployGroupId = None
        self.ApiId = None
        self.StartTime = None
        self.EndTime = None
        self.GatewayInstanceId = None
        self.GroupId = None
        self.Offset = None
        self.Limit = None
        self.Period = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.ApiId = params.get("ApiId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnitApiUseDetailResponse(AbstractModel):
    """DescribeUnitApiUseDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 单元化使用统计对象\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.GroupUnitApiUseStatistics`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupUnitApiUseStatistics()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUnitNamespacesRequest(AbstractModel):
    """DescribeUnitNamespaces请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayInstanceId: 网关实体ID\n        :type GatewayInstanceId: str\n        :param SearchWord: 根据命名空间名或ID模糊查询\n        :type SearchWord: str\n        :param Offset: 翻页查询偏移量\n        :type Offset: int\n        :param Limit: 翻页查询每页记录数\n        :type Limit: int\n        """
        self.GatewayInstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnitNamespacesResponse(AbstractModel):
    """DescribeUnitNamespaces返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 单元化命名空间对象列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageUnitNamespace`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageUnitNamespace()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUnitRuleRequest(AbstractModel):
    """DescribeUnitRule请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 单元化规则ID\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnitRuleResponse(AbstractModel):
    """DescribeUnitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 单元化规则对象
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.UnitRule`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UnitRule()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUnitRulesRequest(AbstractModel):
    """DescribeUnitRules请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayInstanceId: 网关实体ID\n        :type GatewayInstanceId: str\n        :param SearchWord: 根据规则名或备注内容模糊查询\n        :type SearchWord: str\n        :param Status: 启用状态, disabled: 未发布， enabled: 发布\n        :type Status: str\n        :param Offset: 翻页查询偏移量\n        :type Offset: int\n        :param Limit: 翻页查询每页记录数\n        :type Limit: int\n        """
        self.GatewayInstanceId = None
        self.SearchWord = None
        self.Status = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnitRulesResponse(AbstractModel):
    """DescribeUnitRules返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分页列表信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: list of TsfPageUnitRule\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = TsfPageUnitRule()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUploadInfoRequest(AbstractModel):
    """DescribeUploadInfo请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        :param PkgName: 程序包名\n        :type PkgName: str\n        :param PkgVersion: 程序包版本\n        :type PkgVersion: str\n        :param PkgType: 程序包类型\n        :type PkgType: str\n        :param PkgDesc: 程序包介绍\n        :type PkgDesc: str\n        :param RepositoryType: 程序包仓库类型\n        :type RepositoryType: str\n        :param RepositoryId: 程序包仓库id\n        :type RepositoryId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadInfoResponse(AbstractModel):
    """DescribeUploadInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: COS上传信息\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.CosUploadInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CosUploadInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsableUnitNamespacesRequest(AbstractModel):
    """DescribeUsableUnitNamespaces请求参数结构体

    """

    def __init__(self):
        """
        :param SearchWord: 根据命名空间名或ID模糊查询\n        :type SearchWord: str\n        :param Offset: 翻页查询偏移量\n        :type Offset: int\n        :param Limit: 翻页查询每页记录数\n        :type Limit: int\n        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsableUnitNamespacesResponse(AbstractModel):
    """DescribeUsableUnitNamespaces返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 单元化命名空间对象列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageUnitNamespace`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageUnitNamespace()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DisableTaskFlowRequest(AbstractModel):
    """DisableTaskFlow请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 工作流 ID\n        :type FlowId: str\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableTaskFlowResponse(AbstractModel):
    """DisableTaskFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true成功，false: 失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TaskId: 任务ID\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableTaskResponse(AbstractModel):
    """DisableTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作成功 or 失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableUnitRouteRequest(AbstractModel):
    """DisableUnitRoute请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 网关实体ID\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableUnitRouteResponse(AbstractModel):
    """DisableUnitRoute返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，成功失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableUnitRuleRequest(AbstractModel):
    """DisableUnitRule请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 规则ID\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableUnitRuleResponse(AbstractModel):
    """DisableUnitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: Api 分组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DraftApiGroupResponse(AbstractModel):
    """DraftApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true: 成功, false: 失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param FlowId: 工作流 ID\n        :type FlowId: str\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableTaskFlowResponse(AbstractModel):
    """EnableTaskFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true成功，false: 失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TaskId: 启用任务\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableTaskResponse(AbstractModel):
    """EnableTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作成功or失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class EnableUnitRouteRequest(AbstractModel):
    """EnableUnitRoute请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 网关实体ID\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableUnitRouteResponse(AbstractModel):
    """EnableUnitRoute返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，成功失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class EnableUnitRuleRequest(AbstractModel):
    """EnableUnitRule请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 规则ID\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableUnitRuleResponse(AbstractModel):
    """EnableUnitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Name: 环境变量名称\n        :type Name: str\n        :param Value: 环境变量值\n        :type Value: str\n        :param ValueFrom: k8s ValueFrom
注意：此字段可能返回 null，表示取不到有效值。\n        :type ValueFrom: :class:`tencentcloud.tsf.v20180326.models.ValueFrom`\n        """
        self.Name = None
        self.Value = None
        self.ValueFrom = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("ValueFrom") is not None:
            self.ValueFrom = ValueFrom()
            self.ValueFrom._deserialize(params.get("ValueFrom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteTaskFlowRequest(AbstractModel):
    """ExecuteTaskFlow请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 工作流 ID\n        :type FlowId: str\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteTaskFlowResponse(AbstractModel):
    """ExecuteTaskFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 工作流批次ID\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TaskId: 任务 ID。\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteTaskResponse(AbstractModel):
    """ExecuteTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功/失败\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param InstanceIdList: 扩容的机器实例ID列表\n        :type InstanceIdList: list of str\n        """
        self.GroupId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandGroupResponse(AbstractModel):
    """ExpandGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class FieldRef(AbstractModel):
    """容器 env 的 FieldRef

    """

    def __init__(self):
        """
        :param FieldPath: k8s 的 FieldPath
注意：此字段可能返回 null，表示取不到有效值。\n        :type FieldPath: str\n        """
        self.FieldPath = None


    def _deserialize(self, params):
        self.FieldPath = params.get("FieldPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileConfig(AbstractModel):
    """文件配置项

    """

    def __init__(self):
        """
        :param ConfigId: 配置项ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigId: str\n        :param ConfigName: 配置项名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigName: str\n        :param ConfigVersion: 配置项版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigVersion: str\n        :param ConfigVersionDesc: 配置项版本描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigVersionDesc: str\n        :param ConfigFileName: 配置项文件名
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigFileName: str\n        :param ConfigFileValue: 配置项文件内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigFileValue: str\n        :param ConfigFileCode: 配置项文件编码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigFileCode: str\n        :param CreationTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreationTime: str\n        :param ApplicationId: 配置项归属应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param DeleteFlag: 删除标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeleteFlag: bool\n        :param ConfigVersionCount: 配置项版本数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigVersionCount: int\n        :param LastUpdateTime: 配置项最后更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastUpdateTime: str\n        :param ConfigFilePath: 发布路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigFilePath: str\n        :param ConfigPostCmd: 后置命令
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigPostCmd: str\n        :param ConfigFileValueLength: 配置项文件长度
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConfigFileValueLength: int\n        """
        self.ConfigId = None
        self.ConfigName = None
        self.ConfigVersion = None
        self.ConfigVersionDesc = None
        self.ConfigFileName = None
        self.ConfigFileValue = None
        self.ConfigFileCode = None
        self.CreationTime = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.DeleteFlag = None
        self.ConfigVersionCount = None
        self.LastUpdateTime = None
        self.ConfigFilePath = None
        self.ConfigPostCmd = None
        self.ConfigFileValueLength = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ConfigVersionDesc = params.get("ConfigVersionDesc")
        self.ConfigFileName = params.get("ConfigFileName")
        self.ConfigFileValue = params.get("ConfigFileValue")
        self.ConfigFileCode = params.get("ConfigFileCode")
        self.CreationTime = params.get("CreationTime")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.DeleteFlag = params.get("DeleteFlag")
        self.ConfigVersionCount = params.get("ConfigVersionCount")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.ConfigFilePath = params.get("ConfigFilePath")
        self.ConfigPostCmd = params.get("ConfigPostCmd")
        self.ConfigFileValueLength = params.get("ConfigFileValueLength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayApiGroupVo(AbstractModel):
    """网关分组简单信息

    """

    def __init__(self):
        """
        :param GroupId: 分组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param GroupApiCount: 分组下API个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupApiCount: int\n        :param GroupApis: 分组API列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupApis: list of GatewayGroupApiVo\n        :param GatewayInstanceType: 网关实例的类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type GatewayInstanceType: str\n        :param GatewayInstanceId: 网关实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GatewayInstanceId: str\n        """
        self.GroupId = None
        self.GroupName = None
        self.GroupApiCount = None
        self.GroupApis = None
        self.GatewayInstanceType = None
        self.GatewayInstanceId = None


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
        self.GatewayInstanceType = params.get("GatewayInstanceType")
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayDeployGroup(AbstractModel):
    """api分组已绑定的网关部署组

    """

    def __init__(self):
        """
        :param DeployGroupId: 网关部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployGroupId: str\n        :param DeployGroupName: 网关部署组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployGroupName: str\n        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param ApplicationType: 应用分类：V：虚拟机应用，C：容器应用
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationType: str\n        :param GroupStatus: 部署组应用状态,取值: Running、Waiting、Paused、Updating、RollingBack、Abnormal、Unknown
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupStatus: str\n        :param ClusterType: 集群类型，C ：容器，V：虚拟机
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayGroupApiVo(AbstractModel):
    """网关API简单信息

    """

    def __init__(self):
        """
        :param ApiId: API ID\n        :type ApiId: str\n        :param Path: API 请求路径\n        :type Path: str\n        :param MicroserviceName: API 微服务名称\n        :type MicroserviceName: str\n        :param Method: API 请求方法
注意：此字段可能返回 null，表示取不到有效值。\n        :type Method: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayGroupIds(AbstractModel):
    """网关部署组ID和网关API分组ID元组

    """

    def __init__(self):
        """
        :param GatewayDeployGroupId: 网关部署组ID\n        :type GatewayDeployGroupId: str\n        :param GroupId: 分组id\n        :type GroupId: str\n        """
        self.GatewayDeployGroupId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayPlugin(AbstractModel):
    """微服务网关插件实例对象

    """

    def __init__(self):
        """
        :param Id: 网关插件id
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        :param Name: 插件名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Type: 插件类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Description: 插件描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param UpdatedTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdatedTime: str\n        :param Status: 发布状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.Description = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Description = params.get("Description")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayPluginBoundParam(AbstractModel):
    """微服务网关插件绑定对象

    """

    def __init__(self):
        """
        :param PluginId: 插件id\n        :type PluginId: str\n        :param ScopeType: 插件绑定到的对象类型:group/api\n        :type ScopeType: str\n        :param ScopeValue: 插件绑定到的对象主键值，例如分组的ID/API的ID\n        :type ScopeValue: str\n        """
        self.PluginId = None
        self.ScopeType = None
        self.ScopeValue = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.ScopeType = params.get("ScopeType")
        self.ScopeValue = params.get("ScopeValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayVo(AbstractModel):
    """网关部署组、分组、API列表数据

    """

    def __init__(self):
        """
        :param GatewayDeployGroupId: 网关部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GatewayDeployGroupId: str\n        :param GatewayDeployGroupName: 网关部署组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GatewayDeployGroupName: str\n        :param GroupNum: API 分组个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupNum: int\n        :param Groups: API 分组列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Groups: list of GatewayApiGroupVo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupApiUseStatistics(AbstractModel):
    """API监控明细数据

    """

    def __init__(self):
        """
        :param TopStatusCode: 总调用数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopStatusCode: list of ApiUseStatisticsEntity\n        :param TopTimeCost: 平均错误率
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopTimeCost: list of ApiUseStatisticsEntity\n        :param Quantile: 分位值对象
注意：此字段可能返回 null，表示取不到有效值。\n        :type Quantile: :class:`tencentcloud.tsf.v20180326.models.QuantileEntity`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupDailyUseStatistics(AbstractModel):
    """分组日使用统计对象

    """

    def __init__(self):
        """
        :param TopReqAmount: 总调用数\n        :type TopReqAmount: list of GroupUseStatisticsEntity\n        :param TopFailureRate: 平均错误率\n        :type TopFailureRate: list of GroupUseStatisticsEntity\n        :param TopAvgTimeCost: 平均响应耗时\n        :type TopAvgTimeCost: list of GroupUseStatisticsEntity\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupPod(AbstractModel):
    """部署组实例列表

    """

    def __init__(self):
        """
        :param PodName: 实例名称(对应到kubernetes的pod名称)
注意：此字段可能返回 null，表示取不到有效值。\n        :type PodName: str\n        :param PodId: 实例ID(对应到kubernetes的pod id)
注意：此字段可能返回 null，表示取不到有效值。\n        :type PodId: str\n        :param Status: 实例状态，请参考后面的实例以及容器的状态定义
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Reason: 实例处于当前状态的原因，例如容器下载镜像失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Reason: str\n        :param NodeIp: 主机IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodeIp: str\n        :param Ip: 实例IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ip: str\n        :param RestartCount: 实例中容器的重启次数
注意：此字段可能返回 null，表示取不到有效值。\n        :type RestartCount: int\n        :param ReadyCount: 实例中已就绪容器的个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReadyCount: int\n        :param Runtime: 运行时长
注意：此字段可能返回 null，表示取不到有效值。\n        :type Runtime: str\n        :param CreatedAt: 实例启动时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedAt: str\n        :param ServiceInstanceStatus: 服务实例状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceInstanceStatus: str\n        :param InstanceAvailableStatus: 机器实例可使用状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceAvailableStatus: str\n        :param InstanceStatus: 机器实例状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceStatus: str\n        :param NodeInstanceId: 节点实例id
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodeInstanceId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupPodResult(AbstractModel):
    """部署组实例列表

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 列表信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of GroupPod\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupUnitApiDailyUseStatistics(AbstractModel):
    """单元化API使用详情统计对象列表

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间ID\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称\n        :type NamespaceName: str\n        :param SumReqAmount: 该API在该命名空间下的总调用次数\n        :type SumReqAmount: str\n        :param AvgFailureRate: 该API在该命名空间下的平均错误率\n        :type AvgFailureRate: str\n        :param AvgTimeCost: 该API在该命名空间下的平均响应时间\n        :type AvgTimeCost: str\n        :param MetricDataPointMap: 监控数据曲线点位图Map集合\n        :type MetricDataPointMap: :class:`tencentcloud.tsf.v20180326.models.MetricDataPointMap`\n        :param TopStatusCode: 状态码分布详情\n        :type TopStatusCode: list of ApiUseStatisticsEntity\n        :param TopTimeCost: 耗时分布详情\n        :type TopTimeCost: list of ApiUseStatisticsEntity\n        :param Quantile: 分位值对象\n        :type Quantile: :class:`tencentcloud.tsf.v20180326.models.QuantileEntity`\n        """
        self.NamespaceId = None
        self.NamespaceName = None
        self.SumReqAmount = None
        self.AvgFailureRate = None
        self.AvgTimeCost = None
        self.MetricDataPointMap = None
        self.TopStatusCode = None
        self.TopTimeCost = None
        self.Quantile = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.SumReqAmount = params.get("SumReqAmount")
        self.AvgFailureRate = params.get("AvgFailureRate")
        self.AvgTimeCost = params.get("AvgTimeCost")
        if params.get("MetricDataPointMap") is not None:
            self.MetricDataPointMap = MetricDataPointMap()
            self.MetricDataPointMap._deserialize(params.get("MetricDataPointMap"))
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupUnitApiUseStatistics(AbstractModel):
    """查询网关API监控明细数据（单元化网关使用详情）

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param Content: 查询网关API监控明细对象集合\n        :type Content: list of GroupUnitApiDailyUseStatistics\n        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = GroupUnitApiDailyUseStatistics()
                obj._deserialize(item)
                self.Content.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupUseStatisticsEntity(AbstractModel):
    """API分组日使用统计对象数据点

    """

    def __init__(self):
        """
        :param ApiPath: API 路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiPath: str\n        :param ServiceName: 服务名
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceName: str\n        :param Value: 统计值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param ApiId: API ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiId: str\n        """
        self.ApiPath = None
        self.ServiceName = None
        self.Value = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ApiPath = params.get("ApiPath")
        self.ServiceName = params.get("ServiceName")
        self.Value = params.get("Value")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckConfig(AbstractModel):
    """健康检查配置

    """

    def __init__(self):
        """
        :param Path: 健康检查路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        """
        self.Path = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckSetting(AbstractModel):
    """健康检查配置信息，若不指定该参数，则默认不设置健康检查。

    """

    def __init__(self):
        """
        :param ActionType: 健康检查方法。HTTP：通过 HTTP 接口检查；CMD：通过执行命令检查；TCP：通过建立 TCP 连接检查。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActionType: str\n        :param InitialDelaySeconds: 容器延时启动健康检查的时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InitialDelaySeconds: int\n        :param TimeoutSeconds: 每次健康检查响应的最大超时时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeoutSeconds: int\n        :param PeriodSeconds: 进行健康检查的时间间隔。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PeriodSeconds: int\n        :param SuccessThreshold: 表示后端容器从失败到成功的连续健康检查成功次数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessThreshold: int\n        :param FailureThreshold: 表示后端容器从成功到失败的连续健康检查成功次数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailureThreshold: int\n        :param Scheme: HTTP 健康检查方法使用的检查协议。支持HTTP、HTTPS。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Scheme: str\n        :param Port: 健康检查端口，范围 1~65535 。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param Path: HTTP 健康检查接口的请求路径。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        :param Command: 执行命令检查方式，执行的命令。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Command: list of str\n        :param Type: TSF_DEFAULT：tsf 默认就绪探针。K8S_NATIVE：k8s 原生探针。不填默认为 k8s 原生探针。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckSettings(AbstractModel):
    """健康检查参数

    """

    def __init__(self):
        """
        :param LivenessProbe: 存活健康检查
注意：此字段可能返回 null，表示取不到有效值。\n        :type LivenessProbe: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSetting`\n        :param ReadinessProbe: 就绪健康检查
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReadinessProbe: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSetting`\n        """
        self.LivenessProbe = None
        self.ReadinessProbe = None


    def _deserialize(self, params):
        if params.get("LivenessProbe") is not None:
            self.LivenessProbe = HealthCheckSetting()
            self.LivenessProbe._deserialize(params.get("LivenessProbe"))
        if params.get("ReadinessProbe") is not None:
            self.ReadinessProbe = HealthCheckSetting()
            self.ReadinessProbe._deserialize(params.get("ReadinessProbe"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRepository(AbstractModel):
    """镜像仓库

    """

    def __init__(self):
        """
        :param Reponame: 仓库名,含命名空间,如tsf/nginx
注意：此字段可能返回 null，表示取不到有效值。\n        :type Reponame: str\n        :param Repotype: 仓库类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Repotype: str\n        :param TagCount: 镜像版本数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagCount: int\n        :param IsPublic: 是否公共,1:公有,0:私有
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsPublic: int\n        :param IsUserFavor: 是否被用户收藏。true：是，false：否
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsUserFavor: bool\n        :param IsQcloudOfficial: 是否是腾讯云官方仓库。 是否是腾讯云官方仓库。true：是，false：否
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsQcloudOfficial: bool\n        :param FavorCount: 被所有用户收藏次数
注意：此字段可能返回 null，表示取不到有效值。\n        :type FavorCount: int\n        :param PullCount: 拉取次数
注意：此字段可能返回 null，表示取不到有效值。\n        :type PullCount: int\n        :param Description: 描述内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param CreationTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreationTime: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRepositoryResult(AbstractModel):
    """镜像仓库列表

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Server: 镜像服务器地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Server: str\n        :param Content: 列表信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of ImageRepository\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTag(AbstractModel):
    """列表信息

    """

    def __init__(self):
        """
        :param RepoName: 仓库名\n        :type RepoName: str\n        :param TagName: 版本名称\n        :type TagName: str\n        :param TagId: 版本ID\n        :type TagId: str\n        :param ImageId: 镜像ID\n        :type ImageId: str\n        :param Size: 大小\n        :type Size: str\n        :param CreationTime: 创建时间\n        :type CreationTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param Author: 镜像制作者\n        :type Author: str\n        :param Architecture: CPU架构\n        :type Architecture: str\n        :param DockerVersion: Docker客户端版本\n        :type DockerVersion: str\n        :param Os: 操作系统
注意：此字段可能返回 null，表示取不到有效值。\n        :type Os: str\n        :param PushTime: push时间\n        :type PushTime: str\n        :param SizeByte: 单位为字节\n        :type SizeByte: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTagsResult(AbstractModel):
    """镜像版本列表

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param RepoName: 仓库名,含命名空间,如tsf/ngin\n        :type RepoName: str\n        :param Server: 镜像服务器地址\n        :type Server: str\n        :param Content: 列表信息\n        :type Content: list of ImageTag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """机器实例

    """

    def __init__(self):
        """
        :param InstanceId: 机器实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param InstanceName: 机器名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param LanIp: 机器内网地址IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type LanIp: str\n        :param WanIp: 机器外网地址IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type WanIp: str\n        :param InstanceDesc: 机器描述信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceDesc: str\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param InstanceStatus: VM的状态 虚机：虚机的状态 容器：Pod所在虚机的状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceStatus: str\n        :param InstanceAvailableStatus: VM的可使用状态 虚机：虚机是否能够作为资源使用 容器：虚机是否能够作为资源部署POD
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceAvailableStatus: str\n        :param ServiceInstanceStatus: 服务下的服务实例的状态 虚机：应用是否可用 + Agent状态 容器：Pod状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceInstanceStatus: str\n        :param CountInTsf: 标识此instance是否已添加在tsf中
注意：此字段可能返回 null，表示取不到有效值。\n        :type CountInTsf: int\n        :param GroupId: 机器所属部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param ApplicationId: 机器所属应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 机器所属应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param InstanceCreatedTime: 机器实例在CVM的创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceCreatedTime: str\n        :param InstanceExpiredTime: 机器实例在CVM的过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceExpiredTime: str\n        :param InstanceChargeType: 机器实例在CVM的计费模式
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceChargeType: str\n        :param InstanceTotalCpu: 机器实例总CPU信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceTotalCpu: float\n        :param InstanceTotalMem: 机器实例总内存信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceTotalMem: float\n        :param InstanceUsedCpu: 机器实例使用的CPU信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceUsedCpu: float\n        :param InstanceUsedMem: 机器实例使用的内存信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceUsedMem: float\n        :param InstanceLimitCpu: 机器实例Limit CPU信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceLimitCpu: float\n        :param InstanceLimitMem: 机器实例Limit 内存信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceLimitMem: float\n        :param InstancePkgVersion: 包版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstancePkgVersion: str\n        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterType: str\n        :param RestrictState: 机器实例业务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type RestrictState: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param OperationState: 实例执行状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type OperationState: int\n        :param NamespaceId: NamespaceId Ns ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param InstanceZoneId: InstanceZoneId 可用区ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceZoneId: str\n        :param InstanceImportMode: InstanceImportMode 导入模式
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceImportMode: str\n        :param ApplicationType: ApplicationType应用类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationType: str\n        :param ApplicationResourceType: ApplicationResourceType 资源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationResourceType: str\n        :param ServiceSidecarStatus: sidecar状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceSidecarStatus: str\n        :param GroupName: 部署组名
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param NamespaceName: NS名
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param Reason: 健康检查原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type Reason: str\n        :param AgentVersion: agent版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type AgentVersion: str\n        """
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
        self.AgentVersion = None


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
        self.AgentVersion = params.get("AgentVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAdvancedSettings(AbstractModel):
    """容器导入实例高级设置

    """

    def __init__(self):
        """
        :param MountTarget: 数据盘挂载点, 默认不挂载数据盘. 已格式化的 ext3，ext4，xfs 文件系统的数据盘将直接挂载，其他文件系统或未格式化的数据盘将自动格式化为ext4 并挂载，请注意备份数据! 无数据盘或有多块数据盘的云主机此设置不生效。
注意，注意，多盘场景请使用下方的DataDisks数据结构，设置对应的云盘类型、云盘大小、挂载路径、是否格式化等信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MountTarget: str\n        :param DockerGraphPath: dockerd --graph 指定值, 默认为 /var/lib/docker
注意：此字段可能返回 null，表示取不到有效值。\n        :type DockerGraphPath: str\n        """
        self.MountTarget = None
        self.DockerGraphPath = None


    def _deserialize(self, params):
        self.MountTarget = params.get("MountTarget")
        self.DockerGraphPath = params.get("DockerGraphPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaneGroup(AbstractModel):
    """泳道部署组

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param Entrance: 是否入口应用
注意：此字段可能返回 null，表示取不到有效值。\n        :type Entrance: bool\n        :param LaneGroupId: 泳道部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type LaneGroupId: str\n        :param LaneId: 泳道ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type LaneId: str\n        :param GroupName: 部署组名
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 应用名
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: int\n        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaneInfo(AbstractModel):
    """泳道

    """

    def __init__(self):
        """
        :param LaneId: 泳道ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type LaneId: str\n        :param LaneName: 泳道名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type LaneName: str\n        :param Remark: 泳道备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: int\n        :param LaneGroupList: 泳道部署组
注意：此字段可能返回 null，表示取不到有效值。\n        :type LaneGroupList: list of LaneGroup\n        :param Entrance: 是否入口应用
注意：此字段可能返回 null，表示取不到有效值。\n        :type Entrance: bool\n        :param NamespaceIdList: 泳道已经关联部署组的命名空间列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceIdList: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaneInfos(AbstractModel):
    """泳道分页查询

    """

    def __init__(self):
        """
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 泳道信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of LaneInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaneRule(AbstractModel):
    """泳道规则

    """

    def __init__(self):
        """
        :param RuleId: 泳道规则ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleId: str\n        :param RuleName: 泳道规则名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleName: str\n        :param Priority: 优先级
注意：此字段可能返回 null，表示取不到有效值。\n        :type Priority: int\n        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param RuleTagList: 泳道规则标签列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleTagList: list of LaneRuleTag\n        :param RuleTagRelationship: 泳道规则标签关系
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleTagRelationship: str\n        :param LaneId: 泳道ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type LaneId: str\n        :param Enable: 开启状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Enable: bool\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaneRuleTag(AbstractModel):
    """泳道规则标签

    """

    def __init__(self):
        """
        :param TagId: 标签ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagId: str\n        :param TagName: 标签名
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagName: str\n        :param TagOperator: 标签操作符
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagOperator: str\n        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagValue: str\n        :param LaneRuleId: 泳道规则ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type LaneRuleId: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaneRules(AbstractModel):
    """泳道规则分页查询

    """

    def __init__(self):
        """
        :param TotalCount: 总数\n        :type TotalCount: int\n        :param Content: 泳道规则列表\n        :type Content: list of LaneRule\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDataPoint(AbstractModel):
    """监控统计数据点

    """

    def __init__(self):
        """
        :param Key: 数据点键
注意：此字段可能返回 null，表示取不到有效值。\n        :type Key: str\n        :param Value: 数据点值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param Tag: 数据点标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tag: str\n        """
        self.Key = None
        self.Value = None
        self.Tag = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDataPointMap(AbstractModel):
    """监控统计数据点Map集合（单元化网关使用）

    """

    def __init__(self):
        """
        :param SumReqAmount: 总调用次数监控数据点集合\n        :type SumReqAmount: list of MetricDataPoint\n        :param AvgFailureRate: 平均错误率监控数据点集合\n        :type AvgFailureRate: list of MetricDataPoint\n        :param AvgTimeCost: 平均响应时间监控数据点集合\n        :type AvgTimeCost: list of MetricDataPoint\n        """
        self.SumReqAmount = None
        self.AvgFailureRate = None
        self.AvgTimeCost = None


    def _deserialize(self, params):
        if params.get("SumReqAmount") is not None:
            self.SumReqAmount = []
            for item in params.get("SumReqAmount"):
                obj = MetricDataPoint()
                obj._deserialize(item)
                self.SumReqAmount.append(obj)
        if params.get("AvgFailureRate") is not None:
            self.AvgFailureRate = []
            for item in params.get("AvgFailureRate"):
                obj = MetricDataPoint()
                obj._deserialize(item)
                self.AvgFailureRate.append(obj)
        if params.get("AvgTimeCost") is not None:
            self.AvgTimeCost = []
            for item in params.get("AvgTimeCost"):
                obj = MetricDataPoint()
                obj._deserialize(item)
                self.AvgTimeCost.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Microservice(AbstractModel):
    """微服务

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroserviceId: str\n        :param MicroserviceName: 微服务名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroserviceName: str\n        :param MicroserviceDesc: 微服务描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroserviceDesc: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: int\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param RunInstanceCount: 微服务的运行实例数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type RunInstanceCount: int\n        :param CriticalInstanceCount: 微服务的离线实例数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type CriticalInstanceCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyContainerGroupRequest(AbstractModel):
    """ModifyContainerGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param AccessType: 0:公网 1:集群内访问 2：NodePort\n        :type AccessType: int\n        :param ProtocolPorts: ProtocolPorts数组\n        :type ProtocolPorts: list of ProtocolPort\n        :param UpdateType: 更新方式：0:快速更新 1:滚动更新\n        :type UpdateType: int\n        :param UpdateIvl: 更新间隔,单位秒\n        :type UpdateIvl: int\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        :param Alias: 部署组备注\n        :type Alias: str\n        """
        self.GroupId = None
        self.AccessType = None
        self.ProtocolPorts = None
        self.UpdateType = None
        self.UpdateIvl = None
        self.SubnetId = None
        self.Alias = None


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
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyContainerGroupResponse(AbstractModel):
    """ModifyContainerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 更新部署组是否成功。
true：成功。
false：失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID，部署组唯一标识\n        :type GroupId: str\n        :param InstanceNum: 实例数量\n        :type InstanceNum: int\n        """
        self.GroupId = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyContainerReplicasResponse(AbstractModel):
    """ModifyContainerReplicas返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果true：成功；false：失败；\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param LaneId: 泳道ID\n        :type LaneId: str\n        :param LaneName: 泳道名称\n        :type LaneName: str\n        :param Remark: 备注\n        :type Remark: str\n        """
        self.LaneId = None
        self.LaneName = None
        self.Remark = None


    def _deserialize(self, params):
        self.LaneId = params.get("LaneId")
        self.LaneName = params.get("LaneName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLaneResponse(AbstractModel):
    """ModifyLane返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作状态\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleId: 泳道规则ID\n        :type RuleId: str\n        :param RuleName: 泳道规则名称\n        :type RuleName: str\n        :param Remark: 泳道规则备注\n        :type Remark: str\n        :param RuleTagList: 泳道规则标签列表\n        :type RuleTagList: list of LaneRuleTag\n        :param RuleTagRelationship: 泳道规则标签关系\n        :type RuleTagRelationship: str\n        :param LaneId: 泳道ID\n        :type LaneId: str\n        :param Enable: 开启状态\n        :type Enable: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLaneRuleResponse(AbstractModel):
    """ModifyLaneRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param MicroserviceId: 微服务 ID\n        :type MicroserviceId: str\n        :param MicroserviceDesc: 微服务备注信息\n        :type MicroserviceDesc: str\n        """
        self.MicroserviceId = None
        self.MicroserviceDesc = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.MicroserviceDesc = params.get("MicroserviceDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMicroserviceResponse(AbstractModel):
    """ModifyMicroservice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 修改微服务详情是否成功。
true：操作成功。
false：操作失败。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param PathRewriteId: 路径重写规则ID\n        :type PathRewriteId: str\n        :param Regex: 正则表达式\n        :type Regex: str\n        :param Replacement: 替换的内容\n        :type Replacement: str\n        :param Blocked: 是否屏蔽映射后路径，Y: 是 N: 否\n        :type Blocked: str\n        :param Order: 规则顺序，越小优先级越高\n        :type Order: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPathRewriteResponse(AbstractModel):
    """ModifyPathRewrite返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true/false\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TaskId: 任务ID\n        :type TaskId: str\n        :param TaskName: 任务名称\n        :type TaskName: str\n        :param TaskType: 任务类型\n        :type TaskType: str\n        :param TaskContent: 任务内容\n        :type TaskContent: str\n        :param ExecuteType: 任务执行类型\n        :type ExecuteType: str\n        :param TaskRule: 触发规则\n        :type TaskRule: :class:`tencentcloud.tsf.v20180326.models.TaskRule`\n        :param TimeOut: 超时时间，单位 ms\n        :type TimeOut: int\n        :param GroupId: 分组ID\n        :type GroupId: str\n        :param ShardCount: 分片数量\n        :type ShardCount: int\n        :param ShardArguments: 分片参数\n        :type ShardArguments: list of ShardArgument\n        :param AdvanceSettings: 高级设置\n        :type AdvanceSettings: :class:`tencentcloud.tsf.v20180326.models.AdvanceSettings`\n        :param SuccessOperator: 判断任务成功的操作符 GT/GTE\n        :type SuccessOperator: str\n        :param SuccessRatio: 判断任务成功率的阈值\n        :type SuccessRatio: int\n        :param RetryCount: 重试次数\n        :type RetryCount: int\n        :param RetryInterval: 重试间隔\n        :type RetryInterval: int\n        :param TaskArgument: 任务参数，长度限制10000个字符\n        :type TaskArgument: str\n        """
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
            self.ShardArguments = []
            for item in params.get("ShardArguments"):
                obj = ShardArgument()
                obj._deserialize(item)
                self.ShardArguments.append(obj)
        if params.get("AdvanceSettings") is not None:
            self.AdvanceSettings = AdvanceSettings()
            self.AdvanceSettings._deserialize(params.get("AdvanceSettings"))
        self.SuccessOperator = params.get("SuccessOperator")
        self.SuccessRatio = params.get("SuccessRatio")
        self.RetryCount = params.get("RetryCount")
        self.RetryInterval = params.get("RetryInterval")
        self.TaskArgument = params.get("TaskArgument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskResponse(AbstractModel):
    """ModifyTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 更新是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用ID\n        :type ApplicationId: str\n        :param PkgId: 调用DescribeUploadInfo接口时返回的软件包ID\n        :type PkgId: str\n        :param Result: COS返回上传结果（默认为0：成功，其他值表示失败）\n        :type Result: int\n        :param Md5: 程序包MD5\n        :type Md5: str\n        :param Size: 程序包大小（单位字节）\n        :type Size: int\n        :param RepositoryType: 程序包仓库类型\n        :type RepositoryType: str\n        :param RepositoryId: 程序包仓库id\n        :type RepositoryId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUploadInfoResponse(AbstractModel):
    """ModifyUploadInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MonitorOverview(AbstractModel):
    """监控概览对象

    """

    def __init__(self):
        """
        :param InvocationCountOfDay: 近24小时调用数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvocationCountOfDay: str\n        :param InvocationCount: 总调用数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvocationCount: str\n        :param ErrorCountOfDay: 近24小时调用错误数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorCountOfDay: str\n        :param ErrorCount: 总调用错误数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorCount: str\n        :param SuccessRatioOfDay: 近24小时调用成功率
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessRatioOfDay: str\n        :param SuccessRatio: 总调用成功率
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessRatio: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsApiArray(AbstractModel):
    """微服务API数组

    """

    def __init__(self):
        """
        :param Path: API 请求路径\n        :type Path: str\n        :param Method: 请求方法\n        :type Method: str\n        :param Description: 方法描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param Status: API状态 0:离线 1:在线
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        """
        self.Path = None
        self.Method = None
        self.Description = None
        self.Status = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsInstance(AbstractModel):
    """微服务实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 机器实例ID信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param InstanceName: 机器实例名称信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param Port: 服务运行的端口号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: str\n        :param LanIp: 机器实例内网IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type LanIp: str\n        :param WanIp: 机器实例外网IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type WanIp: str\n        :param InstanceAvailableStatus: 机器可用状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceAvailableStatus: str\n        :param ServiceInstanceStatus: 服务运行状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceInstanceStatus: str\n        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param InstanceStatus: 机器TSF可用状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceStatus: str\n        :param HealthCheckUrl: 健康检查URL
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthCheckUrl: str\n        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterType: str\n        :param ApplicationPackageVersion: 应用程序包版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationPackageVersion: str\n        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationType: str\n        :param ServiceStatus: 服务状态，passing 在线，critical 离线
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceStatus: str\n        :param RegistrationTime: 注册时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegistrationTime: int\n        :param LastHeartbeatTime: 上次心跳时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastHeartbeatTime: int\n        :param RegistrationId: 实例注册id
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegistrationId: str\n        :param HiddenStatus: 屏蔽状态，hidden 为屏蔽，unhidden 为未屏蔽
注意：此字段可能返回 null，表示取不到有效值。\n        :type HiddenStatus: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Namespace(AbstractModel):
    """命名空间

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceCode: 命名空间编码
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceCode: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param NamespaceDesc: 命名空间描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceDesc: str\n        :param IsDefault: 默认命名空间
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDefault: str\n        :param NamespaceStatus: 命名空间状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceStatus: str\n        :param DeleteFlag: 删除标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeleteFlag: bool\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param ClusterList: 集群数组，仅携带集群ID，集群名称，集群类型等基础信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterList: list of Cluster\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param NamespaceResourceType: 集群资源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceResourceType: str\n        :param NamespaceType: 命名空间类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceType: str\n        :param IsHaEnable: 是否开启高可用
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsHaEnable: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationInfo(AbstractModel):
    """提供给前端，控制按钮是否显示

    """

    def __init__(self):
        """
        :param Init: 初始化按钮的控制信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Init: :class:`tencentcloud.tsf.v20180326.models.OperationInfoDetail`\n        :param AddInstance: 添加实例按钮的控制信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type AddInstance: :class:`tencentcloud.tsf.v20180326.models.OperationInfoDetail`\n        :param Destroy: 销毁机器的控制信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Destroy: :class:`tencentcloud.tsf.v20180326.models.OperationInfoDetail`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationInfoDetail(AbstractModel):
    """提供给前端控制按钮显示逻辑的字段

    """

    def __init__(self):
        """
        :param DisabledReason: 不显示的原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type DisabledReason: str\n        :param Enabled: 该按钮是否可点击
注意：此字段可能返回 null，表示取不到有效值。\n        :type Enabled: bool\n        :param Supported: 是否显示该按钮
注意：此字段可能返回 null，表示取不到有效值。\n        :type Supported: bool\n        """
        self.DisabledReason = None
        self.Enabled = None
        self.Supported = None


    def _deserialize(self, params):
        self.DisabledReason = params.get("DisabledReason")
        self.Enabled = params.get("Enabled")
        self.Supported = params.get("Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverviewBasicResourceUsage(AbstractModel):
    """TSF基本资源信息概览

    """

    def __init__(self):
        """
        :param ApplicationCount: 应用总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationCount: int\n        :param NamespaceCount: 命名空间总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceCount: int\n        :param GroupCount: 部署组个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupCount: int\n        :param PackageSpaceUsed: 程序包存储空间用量，单位字节
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageSpaceUsed: int\n        :param ConsulInstanceCount: 已注册实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsulInstanceCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathRewrite(AbstractModel):
    """路径重写

    """

    def __init__(self):
        """
        :param PathRewriteId: 路径重写规则ID\n        :type PathRewriteId: str\n        :param GatewayGroupId: 网关部署组ID\n        :type GatewayGroupId: str\n        :param Regex: 正则表达式\n        :type Regex: str\n        :param Replacement: 替换的内容\n        :type Replacement: str\n        :param Blocked: 是否屏蔽映射后路径，Y: 是 N: 否\n        :type Blocked: str\n        :param Order: 规则顺序，越小优先级越高\n        :type Order: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathRewriteCreateObject(AbstractModel):
    """路径重写创建对象

    """

    def __init__(self):
        """
        :param GatewayGroupId: 网关部署组ID\n        :type GatewayGroupId: str\n        :param Regex: 正则表达式\n        :type Regex: str\n        :param Replacement: 替换的内容\n        :type Replacement: str\n        :param Blocked: 是否屏蔽映射后路径，Y: 是 N: 否\n        :type Blocked: str\n        :param Order: 规则顺序，越小优先级越高\n        :type Order: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathRewritePage(AbstractModel):
    """路径重写翻页对象

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param Content: 路径重写规则列表\n        :type Content: list of PathRewrite\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PkgBind(AbstractModel):
    """描述程序包关联信息

    """

    def __init__(self):
        """
        :param ApplicationId: 应用id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param GroupId: 部署组id
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        """
        self.ApplicationId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PkgInfo(AbstractModel):
    """包信息

    """

    def __init__(self):
        """
        :param PkgId: 程序包ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgId: str\n        :param PkgName: 程序包名
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgName: str\n        :param PkgType: 程序包类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgType: str\n        :param PkgVersion: 程序包版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgVersion: str\n        :param PkgDesc: 程序包描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgDesc: str\n        :param UploadTime: 上传时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UploadTime: str\n        :param Md5: 程序包MD5
注意：此字段可能返回 null，表示取不到有效值。\n        :type Md5: str\n        :param PkgPubStatus: 程序包状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgPubStatus: int\n        :param PkgBindInfo: 程序包关联关系
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgBindInfo: list of PkgBind\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PkgList(AbstractModel):
    """包列表

    """

    def __init__(self):
        """
        :param TotalCount: 程序包总量\n        :type TotalCount: int\n        :param Content: 程序包信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of PkgInfo\n        :param RepositoryId: 程序包仓库id
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepositoryId: str\n        :param RepositoryType: 程序包仓库类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepositoryType: str\n        :param RepositoryName: 程序包仓库名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepositoryName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ports(AbstractModel):
    """服务端口

    """

    def __init__(self):
        """
        :param TargetPort: 服务端口\n        :type TargetPort: int\n        :param Protocol: 端口协议\n        :type Protocol: str\n        """
        self.TargetPort = None
        self.Protocol = None


    def _deserialize(self, params):
        self.TargetPort = params.get("TargetPort")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PropertyField(AbstractModel):
    """属性字段

    """

    def __init__(self):
        """
        :param Name: 属性名称\n        :type Name: str\n        :param Type: 属性类型\n        :type Type: str\n        :param Description: 属性描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        """
        self.Name = None
        self.Type = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolPort(AbstractModel):
    """端口对象

    """

    def __init__(self):
        """
        :param Protocol: TCP UDP\n        :type Protocol: str\n        :param Port: 服务端口\n        :type Port: int\n        :param TargetPort: 容器端口\n        :type TargetPort: int\n        :param NodePort: 主机端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodePort: int\n        """
        self.Protocol = None
        self.Port = None
        self.TargetPort = None
        self.NodePort = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.TargetPort = params.get("TargetPort")
        self.NodePort = params.get("NodePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuantileEntity(AbstractModel):
    """分位数据模型

    """

    def __init__(self):
        """
        :param MaxValue: 最大值
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxValue: str\n        :param MinValue: 最小值
注意：此字段可能返回 null，表示取不到有效值。\n        :type MinValue: str\n        :param FifthPositionValue: 五分位值
注意：此字段可能返回 null，表示取不到有效值。\n        :type FifthPositionValue: str\n        :param NinthPositionValue: 九分位值
注意：此字段可能返回 null，表示取不到有效值。\n        :type NinthPositionValue: str\n        """
        self.MaxValue = None
        self.MinValue = None
        self.FifthPositionValue = None
        self.NinthPositionValue = None


    def _deserialize(self, params):
        self.MaxValue = params.get("MaxValue")
        self.MinValue = params.get("MinValue")
        self.FifthPositionValue = params.get("FifthPositionValue")
        self.NinthPositionValue = params.get("NinthPositionValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedoTaskBatchRequest(AbstractModel):
    """RedoTaskBatch请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: str\n        :param BatchId: 批次ID\n        :type BatchId: str\n        """
        self.TaskId = None
        self.BatchId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedoTaskBatchResponse(AbstractModel):
    """RedoTaskBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 批次ID\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BatchId: 任务批次ID\n        :type BatchId: str\n        :param ExecuteId: 任务执行ID\n        :type ExecuteId: str\n        :param TaskId: 任务ID\n        :type TaskId: str\n        """
        self.BatchId = None
        self.ExecuteId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.ExecuteId = params.get("ExecuteId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedoTaskExecuteResponse(AbstractModel):
    """RedoTaskExecute返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功失败\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param FlowBatchId: 工作流批次 ID\n        :type FlowBatchId: str\n        """
        self.FlowBatchId = None


    def _deserialize(self, params):
        self.FlowBatchId = params.get("FlowBatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedoTaskFlowBatchResponse(AbstractModel):
    """RedoTaskFlowBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 工作流批次历史 ID\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TaskId: 任务ID\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedoTaskResponse(AbstractModel):
    """RedoTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作成功or失败\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: Api 分组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseApiGroupResponse(AbstractModel):
    """ReleaseApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功/失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigId: 配置ID\n        :type ConfigId: str\n        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param ReleaseDesc: 发布描述\n        :type ReleaseDesc: str\n        """
        self.ConfigId = None
        self.GroupId = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.GroupId = params.get("GroupId")
        self.ReleaseDesc = params.get("ReleaseDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseConfigResponse(AbstractModel):
    """ReleaseConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：发布成功；false：发布失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ReleaseFileConfigRequest(AbstractModel):
    """ReleaseFileConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置ID\n        :type ConfigId: str\n        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param ReleaseDesc: 发布描述\n        :type ReleaseDesc: str\n        """
        self.ConfigId = None
        self.GroupId = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.GroupId = params.get("GroupId")
        self.ReleaseDesc = params.get("ReleaseDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseFileConfigResponse(AbstractModel):
    """ReleaseFileConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 发布结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigId: 配置ID\n        :type ConfigId: str\n        :param NamespaceId: 命名空间ID\n        :type NamespaceId: str\n        :param ReleaseDesc: 发布描述\n        :type ReleaseDesc: str\n        """
        self.ConfigId = None
        self.NamespaceId = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.NamespaceId = params.get("NamespaceId")
        self.ReleaseDesc = params.get("ReleaseDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleasePublicConfigResponse(AbstractModel):
    """ReleasePublicConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：发布成功；false：发布失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ClusterId: 集群 ID\n        :type ClusterId: str\n        :param InstanceIdList: 云主机 ID 列表\n        :type InstanceIdList: list of str\n        """
        self.ClusterId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveInstancesResponse(AbstractModel):
    """RemoveInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 集群移除机器是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RepositoryId: 仓库ID\n        :type RepositoryId: str\n        :param RepositoryName: 仓库名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepositoryName: str\n        :param RepositoryType: 仓库类型（默认仓库：default，私有仓库：private）
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepositoryType: str\n        :param RepositoryDesc: 仓库描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepositoryDesc: str\n        :param IsUsed: 仓库是否正在被使用
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsUsed: bool\n        :param CreateTime: 仓库创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param BucketName: 仓库桶名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type BucketName: str\n        :param BucketRegion: 仓库桶所在地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type BucketRegion: str\n        :param Directory: 仓库目录
注意：此字段可能返回 null，表示取不到有效值。\n        :type Directory: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RepositoryList(AbstractModel):
    """仓库列表

    """

    def __init__(self):
        """
        :param TotalCount: 仓库总量\n        :type TotalCount: int\n        :param Content: 仓库信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of RepositoryInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceFieldRef(AbstractModel):
    """k8s env 的 ResourceFieldRef

    """

    def __init__(self):
        """
        :param Resource: k8s 的 Resource
注意：此字段可能返回 null，表示取不到有效值。\n        :type Resource: str\n        """
        self.Resource = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevocationConfigRequest(AbstractModel):
    """RevocationConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigReleaseId: 配置项发布ID\n        :type ConfigReleaseId: str\n        """
        self.ConfigReleaseId = None


    def _deserialize(self, params):
        self.ConfigReleaseId = params.get("ConfigReleaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevocationConfigResponse(AbstractModel):
    """RevocationConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：回滚成功；false：回滚失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigReleaseId: 配置项发布ID\n        :type ConfigReleaseId: str\n        """
        self.ConfigReleaseId = None


    def _deserialize(self, params):
        self.ConfigReleaseId = params.get("ConfigReleaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevocationPublicConfigResponse(AbstractModel):
    """RevocationPublicConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：撤销成功；false：撤销失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ConfigReleaseLogId: 配置项发布历史ID\n        :type ConfigReleaseLogId: str\n        :param ReleaseDesc: 回滚描述\n        :type ReleaseDesc: str\n        """
        self.ConfigReleaseLogId = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigReleaseLogId = params.get("ConfigReleaseLogId")
        self.ReleaseDesc = params.get("ReleaseDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackConfigResponse(AbstractModel):
    """RollbackConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true：回滚成功；false：回滚失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchBusinessLogRequest(AbstractModel):
    """SearchBusinessLog请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 日志配置项ID\n        :type ConfigId: str\n        :param InstanceIds: 机器实例ID，不传表示全部实例\n        :type InstanceIds: list of str\n        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Offset: 请求偏移量，取值范围大于等于0，默认值为0\n        :type Offset: int\n        :param Limit: 单页请求配置数量，取值范围[1, 200]，默认值为50\n        :type Limit: int\n        :param OrderBy: 排序规则，默认值"time"\n        :type OrderBy: str\n        :param OrderType: 排序方式，取值"asc"或"desc"，默认值"desc"\n        :type OrderType: str\n        :param SearchWords: 检索关键词\n        :type SearchWords: list of str\n        :param GroupIds: 部署组ID列表，不传表示全部部署组\n        :type GroupIds: list of str\n        :param SearchWordType: 检索类型，取值"LUCENE", "REGEXP", "NORMAL"\n        :type SearchWordType: str\n        :param BatchType: 批量请求类型，取值"page"或"scroll"\n        :type BatchType: str\n        :param ScrollId: 游标ID\n        :type ScrollId: str\n        """
        self.ConfigId = None
        self.InstanceIds = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderType = None
        self.SearchWords = None
        self.GroupIds = None
        self.SearchWordType = None
        self.BatchType = None
        self.ScrollId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.InstanceIds = params.get("InstanceIds")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.SearchWords = params.get("SearchWords")
        self.GroupIds = params.get("GroupIds")
        self.SearchWordType = params.get("SearchWordType")
        self.BatchType = params.get("BatchType")
        self.ScrollId = params.get("ScrollId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchBusinessLogResponse(AbstractModel):
    """SearchBusinessLog返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 业务日志列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageBusinessLogV2`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageBusinessLogV2()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class SearchStdoutLogRequest(AbstractModel):
    """SearchStdoutLog请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 机器实例ID\n        :type InstanceId: str\n        :param Limit: 单页请求配置数量，取值范围[1, 500]，默认值为100\n        :type Limit: int\n        :param SearchWords: 检索关键词\n        :type SearchWords: list of str\n        :param StartTime: 查询起始时间\n        :type StartTime: str\n        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param EndTime: 查询结束时间\n        :type EndTime: str\n        :param Offset: 请求偏移量，取值范围大于等于0，默认值为
0\n        :type Offset: int\n        :param OrderBy: 排序规则，默认值"time"\n        :type OrderBy: str\n        :param OrderType: 排序方式，取值"asc"或"desc"，默认
值"desc"\n        :type OrderType: str\n        :param SearchWordType: 检索类型，取值"LUCENE", "REGEXP",
"NORMAL"\n        :type SearchWordType: str\n        :param BatchType: 批量请求类型，取值"page"或"scroll"，默认
值"page"\n        :type BatchType: str\n        :param ScrollId: 游标ID\n        :type ScrollId: str\n        """
        self.InstanceId = None
        self.Limit = None
        self.SearchWords = None
        self.StartTime = None
        self.GroupId = None
        self.EndTime = None
        self.Offset = None
        self.OrderBy = None
        self.OrderType = None
        self.SearchWordType = None
        self.BatchType = None
        self.ScrollId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SearchWords = params.get("SearchWords")
        self.StartTime = params.get("StartTime")
        self.GroupId = params.get("GroupId")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.SearchWordType = params.get("SearchWordType")
        self.BatchType = params.get("BatchType")
        self.ScrollId = params.get("ScrollId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchStdoutLogResponse(AbstractModel):
    """SearchStdoutLog返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 标准输出日志列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageStdoutLogV2`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageStdoutLogV2()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ServerlessGroup(AbstractModel):
    """Serverless部署组信息

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param Status: 服务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param PkgId: 程序包ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgId: str\n        :param PkgName: 程序包名
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgName: str\n        :param ClusterId: 集群id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param NamespaceId: 命名空间id
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param VpcId: vpc ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param SubnetId: vpc 子网ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: str\n        :param PkgVersion: 程序包版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type PkgVersion: str\n        :param Memory: 所需实例内存大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type Memory: str\n        :param InstanceRequest: 要求最小实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceRequest: int\n        :param StartupParameters: 部署组启动参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartupParameters: str\n        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param InstanceCount: 部署组实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceCount: int\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessGroupPage(AbstractModel):
    """ServerlessGroup 翻页对象

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 列表信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of ServerlessGroup\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceConfig(AbstractModel):
    """服务配置

    """

    def __init__(self):
        """
        :param Name: 服务名\n        :type Name: str\n        :param Ports: 端口信息列表\n        :type Ports: list of Ports\n        :param HealthCheck: 健康检查配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthCheck: :class:`tencentcloud.tsf.v20180326.models.HealthCheckConfig`\n        """
        self.Name = None
        self.Ports = None
        self.HealthCheck = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Ports") is not None:
            self.Ports = []
            for item in params.get("Ports"):
                obj = Ports()
                obj._deserialize(item)
                self.Ports.append(obj)
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheckConfig()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSetting(AbstractModel):
    """容器网络设置。

    """

    def __init__(self):
        """
        :param AccessType: 0:公网, 1:集群内访问, 2：NodePort, 3: VPC 内网访问
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessType: int\n        :param ProtocolPorts: 容器端口映射
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProtocolPorts: list of ProtocolPort\n        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: str\n        :param DisableService: 是否创建 k8s service，默认为 false
注意：此字段可能返回 null，表示取不到有效值。\n        :type DisableService: bool\n        :param HeadlessService: service 是否为 headless 类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type HeadlessService: bool\n        :param AllowDeleteService: 当为 true 且 DisableService 也为 true 时，会删除之前创建的 service，请小心使用
注意：此字段可能返回 null，表示取不到有效值。\n        :type AllowDeleteService: bool\n        """
        self.AccessType = None
        self.ProtocolPorts = None
        self.SubnetId = None
        self.DisableService = None
        self.HeadlessService = None
        self.AllowDeleteService = None


    def _deserialize(self, params):
        self.AccessType = params.get("AccessType")
        if params.get("ProtocolPorts") is not None:
            self.ProtocolPorts = []
            for item in params.get("ProtocolPorts"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPorts.append(obj)
        self.SubnetId = params.get("SubnetId")
        self.DisableService = params.get("DisableService")
        self.HeadlessService = params.get("HeadlessService")
        self.AllowDeleteService = params.get("AllowDeleteService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardArgument(AbstractModel):
    """分片参数

    """

    def __init__(self):
        """
        :param ShardKey: 分片参数 KEY，整形, 范围 [1,1000]\n        :type ShardKey: int\n        :param ShardValue: 分片参数 VALUE
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShardValue: str\n        """
        self.ShardKey = None
        self.ShardValue = None


    def _deserialize(self, params):
        self.ShardKey = params.get("ShardKey")
        self.ShardValue = params.get("ShardValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShrinkGroupRequest(AbstractModel):
    """ShrinkGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShrinkGroupResponse(AbstractModel):
    """ShrinkGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param InstanceIdList: 下线机器实例ID列表\n        :type InstanceIdList: list of str\n        """
        self.GroupId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShrinkInstancesResponse(AbstractModel):
    """ShrinkInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationType: str\n        :param MicroserviceType: 应用微服务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroserviceType: str\n        :param ApplicationDesc: ApplicationDesc
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationDesc: str\n        :param ProgLang: ProgLang
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProgLang: str\n        :param ApplicationResourceType: ApplicationResourceType
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationResourceType: str\n        :param CreateTime: CreateTime
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: UpdateTime
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param ApigatewayServiceId: ApigatewayServiceId
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApigatewayServiceId: str\n        :param ApplicationRuntimeType: ApplicationRuntimeType
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationRuntimeType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleGroup(AbstractModel):
    """部署组

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationType: str\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterType: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param StartupParameters: 启动参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartupParameters: str\n        :param GroupResourceType: 部署组资源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupResourceType: str\n        :param AppMicroServiceType: 应用微服务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppMicroServiceType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartContainerGroupRequest(AbstractModel):
    """StartContainerGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartContainerGroupResponse(AbstractModel):
    """StartContainerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 启动操作是否成功。
true：启动成功
false：启动失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartGroupResponse(AbstractModel):
    """StartGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class StdoutLogV2(AbstractModel):
    """标准输出日志

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param Content: 日志内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: str\n        :param Timestamp: 日志时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type Timestamp: int\n        :param InstanceIp: 实例IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceIp: str\n        """
        self.InstanceId = None
        self.Content = None
        self.Timestamp = None
        self.InstanceIp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Content = params.get("Content")
        self.Timestamp = params.get("Timestamp")
        self.InstanceIp = params.get("InstanceIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopContainerGroupRequest(AbstractModel):
    """StopContainerGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopContainerGroupResponse(AbstractModel):
    """StopContainerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 停止操作是否成功。
true：停止成功
false：停止失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopGroupResponse(AbstractModel):
    """StopGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BatchId: 批次ID\n        :type BatchId: str\n        :param TaskId: 参数ID\n        :type TaskId: str\n        """
        self.BatchId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopTaskBatchResponse(AbstractModel):
    """StopTaskBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作成功 or 失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ExecuteId: 任务执行ID\n        :type ExecuteId: str\n        :param BatchId: 任务批次ID\n        :type BatchId: str\n        :param TaskId: 任务ID\n        :type TaskId: str\n        """
        self.ExecuteId = None
        self.BatchId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ExecuteId = params.get("ExecuteId")
        self.BatchId = params.get("BatchId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopTaskExecuteResponse(AbstractModel):
    """StopTaskExecute返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作成功 or 失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param NodeId: 节点 ID\n        :type NodeId: str\n        :param ChildNodeId: 子节点 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChildNodeId: str\n        :param CoreNode: 是否核心任务,Y/N
注意：此字段可能返回 null，表示取不到有效值。\n        :type CoreNode: str\n        :param EdgeType: 边类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type EdgeType: str\n        :param NodeType: 任务节点类型\n        :type NodeType: str\n        :param PositionX: X轴坐标位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type PositionX: str\n        :param PositionY: Y轴坐标位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type PositionY: str\n        :param GraphId: 图 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GraphId: str\n        :param FlowId: 工作流 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FlowId: str\n        :param NodeName: 节点名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodeName: str\n        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param TaskLogId: 任务历史ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskLogId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFlowLastBatchState(AbstractModel):
    """工作流最近批次的状态

    """

    def __init__(self):
        """
        :param FlowBatchId: 批次ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FlowBatchId: str\n        :param FlowBatchLogId: 批次历史ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FlowBatchLogId: str\n        :param State: 状态,WAITING/SUCCESS/FAILED/RUNNING/TERMINATING
注意：此字段可能返回 null，表示取不到有效值。\n        :type State: str\n        """
        self.FlowBatchId = None
        self.FlowBatchLogId = None
        self.State = None


    def _deserialize(self, params):
        self.FlowBatchId = params.get("FlowBatchId")
        self.FlowBatchLogId = params.get("FlowBatchLogId")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskId(AbstractModel):
    """任务id

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLastExecuteStatus(AbstractModel):
    """任务最近一次执行状态

    """

    def __init__(self):
        """
        :param BatchId: 批次ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type BatchId: str\n        :param State: 运行状态，RUNNING/SUCCESS/FAIL/HALF/TERMINATED
注意：此字段可能返回 null，表示取不到有效值。\n        :type State: str\n        :param BatchLogId: 批次历史ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type BatchLogId: str\n        """
        self.BatchId = None
        self.State = None
        self.BatchLogId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.State = params.get("State")
        self.BatchLogId = params.get("BatchLogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskRecord(AbstractModel):
    """任务定义

    """

    def __init__(self):
        """
        :param TaskName: 任务名称\n        :type TaskName: str\n        :param TaskType: 任务类型\n        :type TaskType: str\n        :param ExecuteType: 执行类型\n        :type ExecuteType: str\n        :param TaskContent: 任务内容，长度限制65535字节\n        :type TaskContent: str\n        :param GroupId: 分组ID\n        :type GroupId: str\n        :param TimeOut: 超时时间\n        :type TimeOut: int\n        :param RetryCount: 重试次数
注意：此字段可能返回 null，表示取不到有效值。\n        :type RetryCount: int\n        :param RetryInterval: 重试间隔
注意：此字段可能返回 null，表示取不到有效值。\n        :type RetryInterval: int\n        :param TaskRule: 触发规则\n        :type TaskRule: :class:`tencentcloud.tsf.v20180326.models.TaskRule`\n        :param TaskState: 是否启用任务,ENABLED/DISABLED\n        :type TaskState: str\n        :param TaskId: 任务ID\n        :type TaskId: str\n        :param SuccessOperator: 判断任务成功的操作符
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessOperator: str\n        :param SuccessRatio: 判断任务成功的阈值
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessRatio: int\n        :param ShardCount: 分片数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShardCount: int\n        :param AdvanceSettings: 高级设置
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdvanceSettings: :class:`tencentcloud.tsf.v20180326.models.AdvanceSettings`\n        :param ShardArguments: 分片参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShardArguments: list of ShardArgument\n        :param BelongFlowIds: 所属工作流ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type BelongFlowIds: list of str\n        :param TaskLogId: 任务历史ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskLogId: str\n        :param TriggerType: 触发类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type TriggerType: str\n        :param TaskArgument: 任务参数，长度限制10000个字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskArgument: str\n        """
        self.TaskName = None
        self.TaskType = None
        self.ExecuteType = None
        self.TaskContent = None
        self.GroupId = None
        self.TimeOut = None
        self.RetryCount = None
        self.RetryInterval = None
        self.TaskRule = None
        self.TaskState = None
        self.TaskId = None
        self.SuccessOperator = None
        self.SuccessRatio = None
        self.ShardCount = None
        self.AdvanceSettings = None
        self.ShardArguments = None
        self.BelongFlowIds = None
        self.TaskLogId = None
        self.TriggerType = None
        self.TaskArgument = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskType = params.get("TaskType")
        self.ExecuteType = params.get("ExecuteType")
        self.TaskContent = params.get("TaskContent")
        self.GroupId = params.get("GroupId")
        self.TimeOut = params.get("TimeOut")
        self.RetryCount = params.get("RetryCount")
        self.RetryInterval = params.get("RetryInterval")
        if params.get("TaskRule") is not None:
            self.TaskRule = TaskRule()
            self.TaskRule._deserialize(params.get("TaskRule"))
        self.TaskState = params.get("TaskState")
        self.TaskId = params.get("TaskId")
        self.SuccessOperator = params.get("SuccessOperator")
        self.SuccessRatio = params.get("SuccessRatio")
        self.ShardCount = params.get("ShardCount")
        if params.get("AdvanceSettings") is not None:
            self.AdvanceSettings = AdvanceSettings()
            self.AdvanceSettings._deserialize(params.get("AdvanceSettings"))
        if params.get("ShardArguments") is not None:
            self.ShardArguments = []
            for item in params.get("ShardArguments"):
                obj = ShardArgument()
                obj._deserialize(item)
                self.ShardArguments.append(obj)
        self.BelongFlowIds = params.get("BelongFlowIds")
        self.TaskLogId = params.get("TaskLogId")
        self.TriggerType = params.get("TriggerType")
        self.TaskArgument = params.get("TaskArgument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskRecordPage(AbstractModel):
    """翻页查询的任务记录返回

    """

    def __init__(self):
        """
        :param TotalCount: 总数量\n        :type TotalCount: int\n        :param Content: 任务记录列表\n        :type Content: list of TaskRecord\n        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TaskRecord()
                obj._deserialize(item)
                self.Content.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskRule(AbstractModel):
    """任务规则

    """

    def __init__(self):
        """
        :param RuleType: 触发规则类型, Cron/Repeat\n        :type RuleType: str\n        :param Expression: Cron类型规则，cron表达式。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Expression: str\n        :param RepeatInterval: 时间间隔， 单位毫秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type RepeatInterval: int\n        """
        self.RuleType = None
        self.Expression = None
        self.RepeatInterval = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.Expression = params.get("Expression")
        self.RepeatInterval = params.get("RepeatInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTaskFlowBatchRequest(AbstractModel):
    """TerminateTaskFlowBatch请求参数结构体

    """

    def __init__(self):
        """
        :param FlowBatchId: 工作流批次 ID\n        :type FlowBatchId: str\n        """
        self.FlowBatchId = None


    def _deserialize(self, params):
        self.FlowBatchId = params.get("FlowBatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTaskFlowBatchResponse(AbstractModel):
    """TerminateTaskFlowBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否停止成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: API 列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of MsApiArray\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageApiGroupInfo(AbstractModel):
    """ApiGroupInfo翻页结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param Content: API分组信息\n        :type Content: list of ApiGroupInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageApplication(AbstractModel):
    """应用分页信息

    """

    def __init__(self):
        """
        :param TotalCount: 应用总数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 应用信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of ApplicationForPage\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageBusinessLogV2(AbstractModel):
    """业务日志列表

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 业务日志列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of BusinessLogV2\n        :param ScrollId: 游标ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScrollId: str\n        :param Status: 查询状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        """
        self.TotalCount = None
        self.Content = None
        self.ScrollId = None
        self.Status = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = BusinessLogV2()
                obj._deserialize(item)
                self.Content.append(obj)
        self.ScrollId = params.get("ScrollId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageCluster(AbstractModel):
    """Tsf分页集群对象

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 集群列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of Cluster\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageConfig(AbstractModel):
    """TsfPage<Config>

    """

    def __init__(self):
        """
        :param TotalCount: TsfPageConfig\n        :type TotalCount: int\n        :param Content: 配置项列表\n        :type Content: list of Config\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageConfigRelease(AbstractModel):
    """TSF配置项发布信息分页对象

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 配置项发布信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of ConfigRelease\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageConfigReleaseLog(AbstractModel):
    """TSF配置项发布日志分页对象

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 配置项发布日志数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of ConfigReleaseLog\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageContainerEvent(AbstractModel):
    """分页的 ContainerEvent

    """

    def __init__(self):
        """
        :param TotalCount: 返回个数\n        :type TotalCount: int\n        :param Content: events 数组\n        :type Content: list of ContainerEvent\n        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ContainerEvent()
                obj._deserialize(item)
                self.Content.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageFileConfig(AbstractModel):
    """文件配置项列表

    """

    def __init__(self):
        """
        :param TotalCount: 总数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 文件配置数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of FileConfig\n        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = FileConfig()
                obj._deserialize(item)
                self.Content.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageGatewayDeployGroup(AbstractModel):
    """GatewayDeployGroup 翻页对象

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数\n        :type TotalCount: int\n        :param Content: 记录实体列表\n        :type Content: list of GatewayDeployGroup\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageGatewayPlugin(AbstractModel):
    """GatewayPlugin 翻页对象

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 记录实体列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of GatewayPlugin\n        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = GatewayPlugin()
                obj._deserialize(item)
                self.Content.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageInstance(AbstractModel):
    """TSF机器实例分页对象

    """

    def __init__(self):
        """
        :param TotalCount: 机器实例总数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 机器实例列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of Instance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageMicroservice(AbstractModel):
    """微服务列表信息

    """

    def __init__(self):
        """
        :param TotalCount: 微服务总数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 微服务列表信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of Microservice\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageMsInstance(AbstractModel):
    """微服务实例的分页内容

    """

    def __init__(self):
        """
        :param TotalCount: 微服务实例总数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 微服务实例列表内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of MsInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageNamespace(AbstractModel):
    """Tsf命名空间分页对象

    """

    def __init__(self):
        """
        :param TotalCount: 命名空间总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 命名空间列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of Namespace\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageSimpleApplication(AbstractModel):
    """TSF分页简单应用对象

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 简单应用列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of SimpleApplication\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageSimpleGroup(AbstractModel):
    """TSF简单部署组分页列表

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 简单部署组列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of SimpleGroup\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageStdoutLogV2(AbstractModel):
    """标准输出日志列表

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 标准输出日志列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of StdoutLogV2\n        :param ScrollId: 游标ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScrollId: str\n        :param Status: 查询状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        """
        self.TotalCount = None
        self.Content = None
        self.ScrollId = None
        self.Status = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = StdoutLogV2()
                obj._deserialize(item)
                self.Content.append(obj)
        self.ScrollId = params.get("ScrollId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageUnitNamespace(AbstractModel):
    """单元化命名空间翻页对象

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数\n        :type TotalCount: int\n        :param Content: 记录实体列表\n        :type Content: list of UnitNamespace\n        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = UnitNamespace()
                obj._deserialize(item)
                self.Content.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageUnitRule(AbstractModel):
    """单元化规则翻页对象

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数\n        :type TotalCount: int\n        :param Content: 记录实体列表\n        :type Content: list of UnitRule\n        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = UnitRule()
                obj._deserialize(item)
                self.Content.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageVmGroup(AbstractModel):
    """列表中部署组分页信息

    """

    def __init__(self):
        """
        :param TotalCount: 虚拟机部署组总数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Content: 虚拟机部署组列表信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: list of VmGroupSimple\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindApiGroupRequest(AbstractModel):
    """UnbindApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupGatewayList: 分组网关id列表\n        :type GroupGatewayList: list of GatewayGroupIds\n        """
        self.GroupGatewayList = None


    def _deserialize(self, params):
        if params.get("GroupGatewayList") is not None:
            self.GroupGatewayList = []
            for item in params.get("GroupGatewayList"):
                obj = GatewayGroupIds()
                obj._deserialize(item)
                self.GroupGatewayList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindApiGroupResponse(AbstractModel):
    """UnbindApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，成功失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnitNamespace(AbstractModel):
    """微服务网关单元化命名空间

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空间ID\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间Name\n        :type NamespaceName: str\n        :param Id: 单元化命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        """
        self.NamespaceId = None
        self.NamespaceName = None
        self.Id = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnitRule(AbstractModel):
    """微服务网关单元化规则

    """

    def __init__(self):
        """
        :param Name: 规则名称\n        :type Name: str\n        :param Id: 规则ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        :param GatewayInstanceId: 网关实体ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GatewayInstanceId: str\n        :param Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param Status: 使用状态：enabled/disabled
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param UnitRuleItemList: 规则项列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type UnitRuleItemList: list of UnitRuleItem\n        """
        self.Name = None
        self.Id = None
        self.GatewayInstanceId = None
        self.Description = None
        self.Status = None
        self.UnitRuleItemList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.GatewayInstanceId = params.get("GatewayInstanceId")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        if params.get("UnitRuleItemList") is not None:
            self.UnitRuleItemList = []
            for item in params.get("UnitRuleItemList"):
                obj = UnitRuleItem()
                obj._deserialize(item)
                self.UnitRuleItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnitRuleItem(AbstractModel):
    """微服务网关单元化规则项

    """

    def __init__(self):
        """
        :param Relationship: 逻辑关系：AND/OR\n        :type Relationship: str\n        :param DestNamespaceId: 目的地命名空间ID\n        :type DestNamespaceId: str\n        :param DestNamespaceName: 目的地命名空间名称\n        :type DestNamespaceName: str\n        :param Name: 规则项名称\n        :type Name: str\n        :param Id: 规则项ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        :param UnitRuleId: 单元化规则ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type UnitRuleId: str\n        :param Priority: 规则顺序，越小优先级越高：默认为0
注意：此字段可能返回 null，表示取不到有效值。\n        :type Priority: int\n        :param Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param UnitRuleTagList: 规则标签列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type UnitRuleTagList: list of UnitRuleTag\n        """
        self.Relationship = None
        self.DestNamespaceId = None
        self.DestNamespaceName = None
        self.Name = None
        self.Id = None
        self.UnitRuleId = None
        self.Priority = None
        self.Description = None
        self.UnitRuleTagList = None


    def _deserialize(self, params):
        self.Relationship = params.get("Relationship")
        self.DestNamespaceId = params.get("DestNamespaceId")
        self.DestNamespaceName = params.get("DestNamespaceName")
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.UnitRuleId = params.get("UnitRuleId")
        self.Priority = params.get("Priority")
        self.Description = params.get("Description")
        if params.get("UnitRuleTagList") is not None:
            self.UnitRuleTagList = []
            for item in params.get("UnitRuleTagList"):
                obj = UnitRuleTag()
                obj._deserialize(item)
                self.UnitRuleTagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnitRuleTag(AbstractModel):
    """微服务网关单元化规则标签

    """

    def __init__(self):
        """
        :param TagType: 标签类型 : U(用户标签)\n        :type TagType: str\n        :param TagField: 标签名\n        :type TagField: str\n        :param TagOperator: 操作符:IN/NOT_IN/EQUAL/NOT_EQUAL/REGEX\n        :type TagOperator: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        :param UnitRuleItemId: 单元化规则项ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type UnitRuleItemId: str\n        :param Id: 规则ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        """
        self.TagType = None
        self.TagField = None
        self.TagOperator = None
        self.TagValue = None
        self.UnitRuleItemId = None
        self.Id = None


    def _deserialize(self, params):
        self.TagType = params.get("TagType")
        self.TagField = params.get("TagField")
        self.TagOperator = params.get("TagOperator")
        self.TagValue = params.get("TagValue")
        self.UnitRuleItemId = params.get("UnitRuleItemId")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiGroupRequest(AbstractModel):
    """UpdateApiGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: Api 分组ID\n        :type GroupId: str\n        :param GroupName: Api 分组名称\n        :type GroupName: str\n        :param Description: Api 分组描述\n        :type Description: str\n        :param AuthType: 鉴权类型\n        :type AuthType: str\n        :param GroupContext: 分组上下文\n        :type GroupContext: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiGroupResponse(AbstractModel):
    """UpdateApiGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，true: 成功, false: 失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleId: 限流规则ID\n        :type RuleId: str\n        :param UsableStatus: 开启/禁用，enabled/disabled\n        :type UsableStatus: str\n        :param MaxQps: qps值，开启限流规则时，必填\n        :type MaxQps: int\n        """
        self.RuleId = None
        self.UsableStatus = None
        self.MaxQps = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.UsableStatus = params.get("UsableStatus")
        self.MaxQps = params.get("MaxQps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiRateLimitRuleResponse(AbstractModel):
    """UpdateApiRateLimitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApiIds: API ID 列表\n        :type ApiIds: list of str\n        :param UsableStatus: 开启/禁用，enabled/disabled\n        :type UsableStatus: str\n        :param MaxQps: QPS值。开启限流规则时，必填\n        :type MaxQps: int\n        """
        self.ApiIds = None
        self.UsableStatus = None
        self.MaxQps = None


    def _deserialize(self, params):
        self.ApiIds = params.get("ApiIds")
        self.UsableStatus = params.get("UsableStatus")
        self.MaxQps = params.get("MaxQps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiRateLimitRulesResponse(AbstractModel):
    """UpdateApiRateLimitRules返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateApiTimeoutsRequest(AbstractModel):
    """UpdateApiTimeouts请求参数结构体

    """

    def __init__(self):
        """
        :param ApiIds: API ID 列表\n        :type ApiIds: list of str\n        :param UsableStatus: 开启/禁用，enabled/disabled\n        :type UsableStatus: str\n        :param Timeout: 超时时间，单位毫秒，开启API超时时，必填\n        :type Timeout: int\n        """
        self.ApiIds = None
        self.UsableStatus = None
        self.Timeout = None


    def _deserialize(self, params):
        self.ApiIds = params.get("ApiIds")
        self.UsableStatus = params.get("UsableStatus")
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiTimeoutsResponse(AbstractModel):
    """UpdateApiTimeouts返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApiId: API ID\n        :type ApiId: str\n        :param Path: API 路径\n        :type Path: str\n        :param Method: Api 请求方法\n        :type Method: str\n        :param PathMapping: 请求映射\n        :type PathMapping: str\n        :param Host: api所在服务host\n        :type Host: str\n        :param Description: api描述信息\n        :type Description: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGatewayApiResponse(AbstractModel):
    """UpdateGatewayApi返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果，成功失败\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param GroupId: 部署组ID\n        :type GroupId: str\n        :param EnableHealthCheck: 是否能使健康检查\n        :type EnableHealthCheck: bool\n        :param HealthCheckSettings: 健康检查配置\n        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`\n        """
        self.GroupId = None
        self.EnableHealthCheck = None
        self.HealthCheckSettings = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.EnableHealthCheck = params.get("EnableHealthCheck")
        if params.get("HealthCheckSettings") is not None:
            self.HealthCheckSettings = HealthCheckSettings()
            self.HealthCheckSettings._deserialize(params.get("HealthCheckSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateHealthCheckSettingsResponse(AbstractModel):
    """UpdateHealthCheckSettings返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 更新健康检查配置操作是否成功。
true：操作成功。
false：操作失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RepositoryId: 仓库ID\n        :type RepositoryId: str\n        :param RepositoryDesc: 仓库描述\n        :type RepositoryDesc: str\n        """
        self.RepositoryId = None
        self.RepositoryDesc = None


    def _deserialize(self, params):
        self.RepositoryId = params.get("RepositoryId")
        self.RepositoryDesc = params.get("RepositoryDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRepositoryResponse(AbstractModel):
    """UpdateRepository返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 更新仓库是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateUnitRuleRequest(AbstractModel):
    """UpdateUnitRule请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 规则ID\n        :type Id: str\n        :param Name: 规则名称\n        :type Name: str\n        :param Description: 规则描述\n        :type Description: str\n        :param UnitRuleItemList: 规则项列表\n        :type UnitRuleItemList: list of UnitRuleItem\n        """
        self.Id = None
        self.Name = None
        self.Description = None
        self.UnitRuleItemList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("UnitRuleItemList") is not None:
            self.UnitRuleItemList = []
            for item in params.get("UnitRuleItemList"):
                obj = UnitRuleItem()
                obj._deserialize(item)
                self.UnitRuleItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUnitRuleResponse(AbstractModel):
    """UpdateUnitRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ValueFrom(AbstractModel):
    """k8s env 的 ValueFrom

    """

    def __init__(self):
        """
        :param FieldRef: k8s env 的 FieldRef
注意：此字段可能返回 null，表示取不到有效值。\n        :type FieldRef: :class:`tencentcloud.tsf.v20180326.models.FieldRef`\n        :param ResourceFieldRef: k8s env 的 ResourceFieldRef
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceFieldRef: :class:`tencentcloud.tsf.v20180326.models.ResourceFieldRef`\n        """
        self.FieldRef = None
        self.ResourceFieldRef = None


    def _deserialize(self, params):
        if params.get("FieldRef") is not None:
            self.FieldRef = FieldRef()
            self.FieldRef._deserialize(params.get("FieldRef"))
        if params.get("ResourceFieldRef") is not None:
            self.ResourceFieldRef = ResourceFieldRef()
            self.ResourceFieldRef._deserialize(params.get("ResourceFieldRef"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VmGroup(AbstractModel):
    """虚拟机部署组信息

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param GroupStatus: 部署组状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupStatus: str\n        :param PackageId: 程序包ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageId: str\n        :param PackageName: 程序包名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageName: str\n        :param PackageVersion: 程序包版本号
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageVersion: str\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param InstanceCount: 部署组机器数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceCount: int\n        :param RunInstanceCount: 部署组运行中机器数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type RunInstanceCount: int\n        :param StartupParameters: 部署组启动参数信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartupParameters: str\n        :param CreateTime: 部署组创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: 部署组更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param OffInstanceCount: 部署组停止机器数目
注意：此字段可能返回 null，表示取不到有效值。\n        :type OffInstanceCount: int\n        :param GroupDesc: 部署组描述信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupDesc: str\n        :param MicroserviceType: 微服务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroserviceType: str\n        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationType: str\n        :param GroupResourceType: 部署组资源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupResourceType: str\n        :param UpdatedTime: 部署组更新时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdatedTime: int\n        :param DeployDesc: 部署应用描述信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployDesc: str\n        :param UpdateType: 滚动发布的更新方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateType: int\n        :param DeployBetaEnable: 发布是否启用beta批次
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployBetaEnable: bool\n        :param DeployBatch: 滚动发布的批次比例列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployBatch: list of float\n        :param DeployExeMode: 滚动发布的批次执行方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployExeMode: str\n        :param DeployWaitTime: 滚动发布的每个批次的等待时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployWaitTime: int\n        :param EnableHealthCheck: 是否开启了健康检查
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableHealthCheck: bool\n        :param HealthCheckSettings: 健康检查配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`\n        :param PackageType: 程序包类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageType: str\n        :param StartScript: 启动脚本 base64编码
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartScript: str\n        :param StopScript: 停止脚本 base64编码
注意：此字段可能返回 null，表示取不到有效值。\n        :type StopScript: str\n        :param Alias: 部署组备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: str\n        """
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
        self.PackageType = None
        self.StartScript = None
        self.StopScript = None
        self.Alias = None


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
        self.PackageType = params.get("PackageType")
        self.StartScript = params.get("StartScript")
        self.StopScript = params.get("StopScript")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VmGroupSimple(AbstractModel):
    """虚拟机部署组列表简要字段

    """

    def __init__(self):
        """
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupId: str\n        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param ApplicationType: 应用类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationType: str\n        :param GroupDesc: 部署组描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupDesc: str\n        :param UpdateTime: 部署组更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param StartupParameters: 部署组启动参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartupParameters: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param CreateTime: 部署组创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationId: str\n        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationName: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        :param MicroserviceType: 应用微服务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroserviceType: str\n        :param GroupResourceType: 部署组资源类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupResourceType: str\n        :param UpdatedTime: 部署组更新时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdatedTime: int\n        :param DeployDesc: 部署应用描述信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployDesc: str\n        :param Alias: 部署组备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: str\n        """
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
        self.Alias = None


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
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        