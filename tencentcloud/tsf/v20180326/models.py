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
        r"""
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
        :param SecurityGroupIds: 安全组 ID 列表
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param SubTaskConcurrency: 子任务单机并发数限制，默认值为2
        :type SubTaskConcurrency: int
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param GatewayInstanceType: 网关实例的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayInstanceType: str
        :param GatewayInstanceId: 网关实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayInstanceId: str
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param ServiceConfigList: 服务配置信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceConfigList: list of ServiceConfig
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
        r"""
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
        r"""
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


class BindPluginRequest(AbstractModel):
    """BindPlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param PluginInstanceList: 分组/API绑定插件列表
        :type PluginInstanceList: list of GatewayPluginBoundParam
        """
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
        r"""
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


class BusinessLogV2(AbstractModel):
    """业务日志

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Content: 日志内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param Timestamp: 日志时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param InstanceIp: 实例IP
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIp: str
        :param LogId: 日志ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogId: str
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
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
        r"""
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
        r"""
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
        :param Alias: 部署组备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param KubeInjectEnable: KubeInjectEnable值
注意：此字段可能返回 null，表示取不到有效值。
        :type KubeInjectEnable: bool
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
        self.Alias = None
        self.KubeInjectEnable = None


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
        self.KubeInjectEnable = params.get("KubeInjectEnable")
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
        r"""
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
        r"""
        :param FirstTimestamp: 第一次出现的时间，以 ms 为单位的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstTimestamp: int
        :param LastTimestamp: 最后一次出现的时间，以 ms 为单位的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTimestamp: int
        :param Type: 级别
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Kind: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Kind: str
        :param Name: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Reason: 内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param Message: 详细描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Count: 出现次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
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
        


class ContainerGroupDeploy(AbstractModel):
    """获取部署组

    """

    def __init__(self):
        r"""
        :param GroupId: 部署组id
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
        :param Server: 镜像server
注意：此字段可能返回 null，表示取不到有效值。
        :type Server: str
        :param Reponame: 镜像名，如/tsf/nginx
注意：此字段可能返回 null，表示取不到有效值。
        :type Reponame: str
        :param TagName: 镜像版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param CpuRequest: 业务容器初始分配的 CPU 核数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuRequest: str
        :param CpuLimit: 业务容器最大分配的 CPU 核数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuLimit: str
        :param MemRequest: 业务容器初始分配的内存 MiB 数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。
        :type MemRequest: str
        :param MemLimit: 业务容器最大分配的内存 MiB 数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。
        :type MemLimit: str
        :param AccessType: 0:公网 1:集群内访问 2：NodePort
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessType: int
        :param ProtocolPorts: 端口映射
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolPorts: list of ProtocolPort
        :param UpdateType: 更新方式：0:快速更新 1:滚动更新
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateType: int
        :param UpdateIvl: 更新间隔,单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateIvl: int
        :param JvmOpts: jvm参数
注意：此字段可能返回 null，表示取不到有效值。
        :type JvmOpts: str
        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param AgentCpuRequest: agent容器初始分配的 CPU 核数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentCpuRequest: str
        :param AgentCpuLimit: agent容器最大分配的 CPU 核数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentCpuLimit: str
        :param AgentMemRequest: agent容器初始分配的内存 MiB 数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentMemRequest: str
        :param AgentMemLimit: agent容器最大分配的内存 MiB 数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentMemLimit: str
        :param IstioCpuRequest: istioproxy容器初始分配的 CPU 核数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。
        :type IstioCpuRequest: str
        :param IstioCpuLimit: istioproxy容器最大分配的 CPU 核数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。
        :type IstioCpuLimit: str
        :param IstioMemRequest: istioproxy容器初始分配的内存 MiB 数，对应 K8S request
注意：此字段可能返回 null，表示取不到有效值。
        :type IstioMemRequest: str
        :param IstioMemLimit: istioproxy容器最大分配的内存 MiB 数，对应 K8S limit
注意：此字段可能返回 null，表示取不到有效值。
        :type IstioMemLimit: str
        :param Envs: 部署组的环境变量数组，这里没有展示 tsf 使用的环境变量，只展示了用户设置的环境变量。
注意：此字段可能返回 null，表示取不到有效值。
        :type Envs: list of Env
        :param HealthCheckSettings: 健康检查配置信息，若不指定该参数，则默认不设置健康检查。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`
        :param DeployAgent: 是否部署Agent容器
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployAgent: bool
        :param Alias: 部署组备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param DisableService: 是否创建 k8s service
注意：此字段可能返回 null，表示取不到有效值。
        :type DisableService: bool
        :param HeadlessService: service 是否为 headless 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadlessService: bool
        :param TcrRepoInfo: TcrRepoInfo值
注意：此字段可能返回 null，表示取不到有效值。
        :type TcrRepoInfo: :class:`tencentcloud.tsf.v20180326.models.TcrRepoInfo`
        :param VolumeInfos: 数据卷信息，list
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeInfos: list of VolumeInfo
        :param VolumeMountInfos: 数据卷挂载信息，list
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeMountInfos: list of VolumeMountInfo
        :param KubeInjectEnable: KubeInjectEnable值
注意：此字段可能返回 null，表示取不到有效值。
        :type KubeInjectEnable: bool
        """
        self.GroupId = None
        self.GroupName = None
        self.InstanceNum = None
        self.CurrentNum = None
        self.Server = None
        self.Reponame = None
        self.TagName = None
        self.CpuRequest = None
        self.CpuLimit = None
        self.MemRequest = None
        self.MemLimit = None
        self.AccessType = None
        self.ProtocolPorts = None
        self.UpdateType = None
        self.UpdateIvl = None
        self.JvmOpts = None
        self.SubnetId = None
        self.AgentCpuRequest = None
        self.AgentCpuLimit = None
        self.AgentMemRequest = None
        self.AgentMemLimit = None
        self.IstioCpuRequest = None
        self.IstioCpuLimit = None
        self.IstioMemRequest = None
        self.IstioMemLimit = None
        self.Envs = None
        self.HealthCheckSettings = None
        self.DeployAgent = None
        self.Alias = None
        self.DisableService = None
        self.HeadlessService = None
        self.TcrRepoInfo = None
        self.VolumeInfos = None
        self.VolumeMountInfos = None
        self.KubeInjectEnable = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.InstanceNum = params.get("InstanceNum")
        self.CurrentNum = params.get("CurrentNum")
        self.Server = params.get("Server")
        self.Reponame = params.get("Reponame")
        self.TagName = params.get("TagName")
        self.CpuRequest = params.get("CpuRequest")
        self.CpuLimit = params.get("CpuLimit")
        self.MemRequest = params.get("MemRequest")
        self.MemLimit = params.get("MemLimit")
        self.AccessType = params.get("AccessType")
        if params.get("ProtocolPorts") is not None:
            self.ProtocolPorts = []
            for item in params.get("ProtocolPorts"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPorts.append(obj)
        self.UpdateType = params.get("UpdateType")
        self.UpdateIvl = params.get("UpdateIvl")
        self.JvmOpts = params.get("JvmOpts")
        self.SubnetId = params.get("SubnetId")
        self.AgentCpuRequest = params.get("AgentCpuRequest")
        self.AgentCpuLimit = params.get("AgentCpuLimit")
        self.AgentMemRequest = params.get("AgentMemRequest")
        self.AgentMemLimit = params.get("AgentMemLimit")
        self.IstioCpuRequest = params.get("IstioCpuRequest")
        self.IstioCpuLimit = params.get("IstioCpuLimit")
        self.IstioMemRequest = params.get("IstioMemRequest")
        self.IstioMemLimit = params.get("IstioMemLimit")
        if params.get("Envs") is not None:
            self.Envs = []
            for item in params.get("Envs"):
                obj = Env()
                obj._deserialize(item)
                self.Envs.append(obj)
        if params.get("HealthCheckSettings") is not None:
            self.HealthCheckSettings = HealthCheckSettings()
            self.HealthCheckSettings._deserialize(params.get("HealthCheckSettings"))
        self.DeployAgent = params.get("DeployAgent")
        self.Alias = params.get("Alias")
        self.DisableService = params.get("DisableService")
        self.HeadlessService = params.get("HeadlessService")
        if params.get("TcrRepoInfo") is not None:
            self.TcrRepoInfo = TcrRepoInfo()
            self.TcrRepoInfo._deserialize(params.get("TcrRepoInfo"))
        if params.get("VolumeInfos") is not None:
            self.VolumeInfos = []
            for item in params.get("VolumeInfos"):
                obj = VolumeInfo()
                obj._deserialize(item)
                self.VolumeInfos.append(obj)
        if params.get("VolumeMountInfos") is not None:
            self.VolumeMountInfos = []
            for item in params.get("VolumeMountInfos"):
                obj = VolumeMountInfo()
                obj._deserialize(item)
                self.VolumeMountInfos.append(obj)
        self.KubeInjectEnable = params.get("KubeInjectEnable")
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
        r"""
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
        :param HealthCheckSettings: 部署组健康检查设置
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckSettings: :class:`tencentcloud.tsf.v20180326.models.HealthCheckSettings`
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
        r"""
        :param BatchId: 批次ID。
        :type BatchId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param GatewayInstanceId: 网关实体ID
        :type GatewayInstanceId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param ServiceConfigList: 服务配置信息列表
        :type ServiceConfigList: list of ServiceConfig
        :param IgnoreCreateImageRepository: 忽略创建镜像仓库
        :type IgnoreCreateImageRepository: bool
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
        """
        self.ApplicationName = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ApplicationDesc = None
        self.ApplicationLogConfig = None
        self.ApplicationResourceType = None
        self.ApplicationRuntimeType = None
        self.ProgramId = None
        self.ServiceConfigList = None
        self.IgnoreCreateImageRepository = None
        self.ProgramIdList = None


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
        self.IgnoreCreateImageRepository = params.get("IgnoreCreateImageRepository")
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
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
        r"""
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
        :param KuberneteApiServer: api地址
        :type KuberneteApiServer: str
        :param KuberneteNativeType: K : kubeconfig, S : service account
        :type KuberneteNativeType: str
        :param KuberneteNativeSecret: native secret
        :type KuberneteNativeSecret: str
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
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
        self.KuberneteApiServer = None
        self.KuberneteNativeType = None
        self.KuberneteNativeSecret = None
        self.ProgramIdList = None


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
        self.KuberneteApiServer = params.get("KuberneteApiServer")
        self.KuberneteNativeType = params.get("KuberneteNativeType")
        self.KuberneteNativeSecret = params.get("KuberneteNativeSecret")
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
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
        r"""
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
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
        """
        self.ConfigName = None
        self.ConfigVersion = None
        self.ConfigValue = None
        self.ApplicationId = None
        self.ConfigVersionDesc = None
        self.ConfigType = None
        self.EncodeWithBase64 = None
        self.ProgramIdList = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ConfigValue = params.get("ConfigValue")
        self.ApplicationId = params.get("ApplicationId")
        self.ConfigVersionDesc = params.get("ConfigVersionDesc")
        self.ConfigType = params.get("ConfigType")
        self.EncodeWithBase64 = params.get("EncodeWithBase64")
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
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
        r"""
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
        r"""
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


class CreateFileConfigRequest(AbstractModel):
    """CreateFileConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConfigName: 配置项名称
        :type ConfigName: str
        :param ConfigVersion: 配置项版本
        :type ConfigVersion: str
        :param ConfigFileName: 配置项文件名
        :type ConfigFileName: str
        :param ConfigFileValue: 配置项文件内容（原始内容编码需要 utf-8 格式，如果 ConfigFileCode 为 gbk，后台会进行转换）
        :type ConfigFileValue: str
        :param ApplicationId: 配置项关联应用ID
        :type ApplicationId: str
        :param ConfigFilePath: 发布路径
        :type ConfigFilePath: str
        :param ConfigVersionDesc: 配置项版本描述
        :type ConfigVersionDesc: str
        :param ConfigFileCode: 配置项文件编码，utf-8 或 gbk。注：如果选择 gbk，需要新版本 tsf-consul-template （公有云虚拟机需要使用 1.32 tsf-agent，容器需要从文档中获取最新的 tsf-consul-template-docker.tar.gz）的支持
        :type ConfigFileCode: str
        :param ConfigPostCmd: 后置命令
        :type ConfigPostCmd: str
        :param EncodeWithBase64: Base64编码的配置项
        :type EncodeWithBase64: bool
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
        """
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
        self.ProgramIdList = None


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
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
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


class CreateGatewayApiRequest(AbstractModel):
    """CreateGatewayApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: API 分组ID
        :type GroupId: str
        :param ApiList: Api信息
        :type ApiList: list of ApiInfo
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
        """
        self.GroupId = None
        self.ApiList = None
        self.ProgramIdList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        if params.get("ApiList") is not None:
            self.ApiList = []
            for item in params.get("ApiList"):
                obj = ApiInfo()
                obj._deserialize(item)
                self.ApiList.append(obj)
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
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
        r"""
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
        :param Alias: 部署组备注
        :type Alias: str
        """
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
        r"""
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
        r"""
        :param LaneName: 泳道名称
        :type LaneName: str
        :param Remark: 泳道备注
        :type Remark: str
        :param LaneGroupList: 泳道部署组信息
        :type LaneGroupList: list of LaneGroup
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
        """
        self.LaneName = None
        self.Remark = None
        self.LaneGroupList = None
        self.ProgramIdList = None


    def _deserialize(self, params):
        self.LaneName = params.get("LaneName")
        self.Remark = params.get("Remark")
        if params.get("LaneGroupList") is not None:
            self.LaneGroupList = []
            for item in params.get("LaneGroupList"):
                obj = LaneGroup()
                obj._deserialize(item)
                self.LaneGroupList.append(obj)
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
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
        r"""
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
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
        """
        self.RuleName = None
        self.Remark = None
        self.RuleTagList = None
        self.RuleTagRelationship = None
        self.LaneId = None
        self.ProgramIdList = None


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
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
        """
        self.NamespaceName = None
        self.ClusterId = None
        self.NamespaceDesc = None
        self.NamespaceResourceType = None
        self.NamespaceType = None
        self.NamespaceId = None
        self.IsHaEnable = None
        self.ProgramId = None
        self.ProgramIdList = None


    def _deserialize(self, params):
        self.NamespaceName = params.get("NamespaceName")
        self.ClusterId = params.get("ClusterId")
        self.NamespaceDesc = params.get("NamespaceDesc")
        self.NamespaceResourceType = params.get("NamespaceResourceType")
        self.NamespaceType = params.get("NamespaceType")
        self.NamespaceId = params.get("NamespaceId")
        self.IsHaEnable = params.get("IsHaEnable")
        self.ProgramId = params.get("ProgramId")
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
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
        r"""
        :param PathRewrites: 路径重写列表
        :type PathRewrites: :class:`tencentcloud.tsf.v20180326.models.PathRewriteCreateObject`
        """
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
        r"""
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
        r"""
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
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
        """
        self.ConfigName = None
        self.ConfigVersion = None
        self.ConfigValue = None
        self.ConfigVersionDesc = None
        self.ConfigType = None
        self.EncodeWithBase64 = None
        self.ProgramIdList = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ConfigValue = params.get("ConfigValue")
        self.ConfigVersionDesc = params.get("ConfigVersionDesc")
        self.ConfigType = params.get("ConfigType")
        self.EncodeWithBase64 = params.get("EncodeWithBase64")
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
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
        r"""
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
        r"""
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


class CreateTaskFlowRequest(AbstractModel):
    """CreateTaskFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowName: 工作流名称
        :type FlowName: str
        :param TriggerRule: 触发方式
        :type TriggerRule: :class:`tencentcloud.tsf.v20180326.models.TaskRule`
        :param FlowEdges: 工作流任务节点列表
        :type FlowEdges: list of TaskFlowEdge
        :param TimeOut: 工作流执行超时时间
        :type TimeOut: int
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
        """
        self.FlowName = None
        self.TriggerRule = None
        self.FlowEdges = None
        self.TimeOut = None
        self.ProgramIdList = None


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
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
        :param Result: 工作流 ID
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


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskName: 任务名称，任务长度64字符
        :type TaskName: str
        :param TaskContent: 任务内容，长度限制65536个字节
        :type TaskContent: str
        :param ExecuteType: 执行类型，unicast/broadcast
        :type ExecuteType: str
        :param TaskType: 任务类型,java
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
        :param SuccessRatio: 判断任务成功率的阈值，如100
        :type SuccessRatio: str
        :param AdvanceSettings: 高级设置
        :type AdvanceSettings: :class:`tencentcloud.tsf.v20180326.models.AdvanceSettings`
        :param TaskArgument: 任务参数，长度限制10000个字符
        :type TaskArgument: str
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
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
        self.ProgramIdList = None


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
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
        :param Result: 任务ID
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


class CreateUnitRuleRequest(AbstractModel):
    """CreateUnitRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayInstanceId: 网关实体ID
        :type GatewayInstanceId: str
        :param Name: 规则名称
        :type Name: str
        :param Description: 规则描述
        :type Description: str
        :param UnitRuleItemList: 规则项列表
        :type UnitRuleItemList: list of UnitRuleItem
        """
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
        r"""
        :param Result: 是否成功
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


class CurvePoint(AbstractModel):
    """构成监控数据图的曲线坐标点

    """

    def __init__(self):
        r"""
        :param Label: 当前坐标 X轴的值 当前是日期格式:"yyyy-MM-dd HH:mm:ss"
        :type Label: str
        :param Value: 当前坐标 Y轴的值
        :type Value: str
        :param Timestamp: 该坐标点时间戳
        :type Timestamp: str
        """
        self.Label = None
        self.Value = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Value = params.get("Value")
        self.Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiGroupRequest(AbstractModel):
    """DeleteApiGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: API 分组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        """
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
        r"""
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
        r"""
        :param ConfigId: 配置项ID
        :type ConfigId: str
        """
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
        r"""
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
        r"""
        :param GroupId: 部署组ID，分组唯一标识
        :type GroupId: str
        """
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
        r"""
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
        r"""
        :param GroupId: 部署组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
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
        r"""
        :param ImageTags: 镜像版本数组
        :type ImageTags: list of DeleteImageTag
        :param RepoType: 企业: tcr ；个人: personal或者不填
        :type RepoType: str
        """
        self.ImageTags = None
        self.RepoType = None


    def _deserialize(self, params):
        if params.get("ImageTags") is not None:
            self.ImageTags = []
            for item in params.get("ImageTags"):
                obj = DeleteImageTag()
                obj._deserialize(item)
                self.ImageTags.append(obj)
        self.RepoType = params.get("RepoType")
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
        r"""
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
        r"""
        :param LaneId: 泳道Idl
        :type LaneId: str
        """
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
        r"""
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


class DeleteLaneRuleRequest(AbstractModel):
    """DeleteLaneRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 泳道规则Id
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaneRuleResponse(AbstractModel):
    """DeleteLaneRule返回参数结构体

    """

    def __init__(self):
        r"""
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


class DeleteMicroserviceRequest(AbstractModel):
    """DeleteMicroservice请求参数结构体

    """

    def __init__(self):
        r"""
        :param MicroserviceId: 微服务ID
        :type MicroserviceId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param PathRewriteIds: 路径重写规则IDs
        :type PathRewriteIds: list of str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param ConfigId: 配置项ID
        :type ConfigId: str
        """
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
        r"""
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
        r"""
        :param RepositoryId: 仓库ID
        :type RepositoryId: str
        """
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
        r"""
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
        r"""
        :param GroupId: groupId，分组唯一标识
        :type GroupId: str
        """
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
        r"""
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
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        """
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
        r"""
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


class DeleteUnitNamespacesRequest(AbstractModel):
    """DeleteUnitNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayInstanceId: 网关实体ID
        :type GatewayInstanceId: str
        :param UnitNamespaceList: 单元化命名空间ID数组
        :type UnitNamespaceList: list of str
        """
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
        r"""
        :param Result: 是否成功
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


class DeleteUnitRuleRequest(AbstractModel):
    """DeleteUnitRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 规则ID
        :type Id: str
        """
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
        r"""
        :param Result: 是否成功
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


class DeployContainerGroupRequest(AbstractModel):
    """DeployContainerGroup请求参数结构体

    """

    def __init__(self):
        r"""
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
        :param CpuRequest: 业务容器分配的 CPU 核数，对应 K8S 的 request，默认0.25
        :type CpuRequest: str
        :param MemRequest: 业务容器分配的内存 MiB 数，对应 K8S 的 request，默认640 MiB
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
        :param IncrementalDeployment: 是否进行增量部署，默认为false，全量更新
        :type IncrementalDeployment: bool
        :param RepoType: tcr或者不填
        :type RepoType: str
        :param VolumeInfos: 数据卷信息-废弃，请用VolumeInfoList参数
        :type VolumeInfos: :class:`tencentcloud.tsf.v20180326.models.VolumeInfo`
        :param VolumeMountInfos: 数据卷挂载点信息-废弃，请用VolumeMountInfoList参数
        :type VolumeMountInfos: :class:`tencentcloud.tsf.v20180326.models.VolumeMountInfo`
        :param VolumeInfoList: 数据卷信息，list
        :type VolumeInfoList: list of VolumeInfo
        :param VolumeMountInfoList: 数据卷挂载点信息，list
        :type VolumeMountInfoList: list of VolumeMountInfo
        :param VolumeClean: 是否清除数据卷信息，默认false
        :type VolumeClean: bool
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
        self.IncrementalDeployment = None
        self.RepoType = None
        self.VolumeInfos = None
        self.VolumeMountInfos = None
        self.VolumeInfoList = None
        self.VolumeMountInfoList = None
        self.VolumeClean = None


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
        self.IncrementalDeployment = params.get("IncrementalDeployment")
        self.RepoType = params.get("RepoType")
        if params.get("VolumeInfos") is not None:
            self.VolumeInfos = VolumeInfo()
            self.VolumeInfos._deserialize(params.get("VolumeInfos"))
        if params.get("VolumeMountInfos") is not None:
            self.VolumeMountInfos = VolumeMountInfo()
            self.VolumeMountInfos._deserialize(params.get("VolumeMountInfos"))
        if params.get("VolumeInfoList") is not None:
            self.VolumeInfoList = []
            for item in params.get("VolumeInfoList"):
                obj = VolumeInfo()
                obj._deserialize(item)
                self.VolumeInfoList.append(obj)
        if params.get("VolumeMountInfoList") is not None:
            self.VolumeMountInfoList = []
            for item in params.get("VolumeMountInfoList"):
                obj = VolumeMountInfo()
                obj._deserialize(item)
                self.VolumeMountInfoList.append(obj)
        self.VolumeClean = params.get("VolumeClean")
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
        r"""
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
        r"""
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
        :param StartScript: 启动脚本 base64编码
        :type StartScript: str
        :param StopScript: 停止脚本 base64编码
        :type StopScript: str
        :param IncrementalDeployment: 是否进行增量部署，默认为false，全量更新
        :type IncrementalDeployment: bool
        :param JdkName: JDK名称: konaJDK或openJDK
        :type JdkName: str
        :param JdkVersion: JDK版本: 8或11 (openJDK只支持8)
        :type JdkVersion: str
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
        self.StartScript = None
        self.StopScript = None
        self.IncrementalDeployment = None
        self.JdkName = None
        self.JdkVersion = None


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
        self.IncrementalDeployment = params.get("IncrementalDeployment")
        self.JdkName = params.get("JdkName")
        self.JdkVersion = params.get("JdkVersion")
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
        r"""
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


class DescribeApiDetailRequest(AbstractModel):
    """DescribeApiDetail请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
        :param GroupId: API 分组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
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
        :param GatewayInstanceId: 网关实体ID
        :type GatewayInstanceId: str
        """
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
        r"""
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
        r"""
        :param ApiId: Api ID
        :type ApiId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        """
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
        r"""
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
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        """
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
        r"""
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
        r"""
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
        :param ApplicationIdList: IdList
        :type ApplicationIdList: list of str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param ConfigId: 配置项ID
        :type ConfigId: str
        """
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
        r"""
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
        r"""
        :param ApplicationId: 应用ID，不传入时查询全量
        :type ApplicationId: str
        :param SearchWord: 查询关键字，模糊查询：应用名称，配置项名称，不传入时查询全量
        :type SearchWord: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 每页条数，默认为20
        :type Limit: int
        :param OrderBy: 按时间排序：creation_time；按名称排序：config_name
        :type OrderBy: str
        :param OrderType: 升序传 0，降序传 1
        :type OrderType: int
        :param ConfigTagList: 无
        :type ConfigTagList: list of str
        :param DisableProgramAuthCheck: 无
        :type DisableProgramAuthCheck: bool
        :param ConfigIdList: 无
        :type ConfigIdList: list of str
        """
        self.ApplicationId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderType = None
        self.ConfigTagList = None
        self.DisableProgramAuthCheck = None
        self.ConfigIdList = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.ConfigTagList = params.get("ConfigTagList")
        self.DisableProgramAuthCheck = params.get("DisableProgramAuthCheck")
        self.ConfigIdList = params.get("ConfigIdList")
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
        r"""
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
        r"""
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
        r"""
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


class DescribeContainerEventsRequest(AbstractModel):
    """DescribeContainerEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceType: event 的资源类型, group 或者 instance
        :type ResourceType: str
        :param ResourceId: event 的资源 id
        :type ResourceId: str
        :param Offset: 偏移量，取值从0开始
        :type Offset: int
        :param Limit: 分页个数，默认为20， 取值应为1~50
        :type Limit: int
        :param GroupId: 当类型是 instance 时需要
        :type GroupId: str
        """
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
        r"""
        :param Result: events 分页列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageContainerEvent`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageContainerEvent()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeContainerGroupDeployInfoRequest(AbstractModel):
    """DescribeContainerGroupDeployInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 实例所属 groupId
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContainerGroupDeployInfoResponse(AbstractModel):
    """DescribeContainerGroupDeployInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 获取部署组
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ContainerGroupDeploy`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ContainerGroupDeploy()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeContainerGroupDetailRequest(AbstractModel):
    """DescribeContainerGroupDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 分组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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


class DescribeEnabledUnitRuleRequest(AbstractModel):
    """DescribeEnabledUnitRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayInstanceId: 网关实体ID
        :type GatewayInstanceId: str
        """
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
        r"""
        :param Result: 单元化规则对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.UnitRule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ConfigId: 配置项ID
        :type ConfigId: str
        :param ConfigIdList: 配置项ID列表
        :type ConfigIdList: list of str
        :param ConfigName: 配置项名称
        :type ConfigName: str
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每页条数
        :type Limit: int
        :param ConfigVersion: 配置项版本
        :type ConfigVersion: str
        """
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
        r"""
        :param Result: 文件配置项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageFileConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param FlowId: 工作流 ID
        :type FlowId: str
        """
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
        r"""
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
        r"""
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
        r"""
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


class DescribeGatewayApisRequest(AbstractModel):
    """DescribeGatewayApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 分组ID
        :type GroupId: str
        :param Offset: 翻页偏移量
        :type Offset: int
        :param Limit: 每页的记录数
        :type Limit: int
        :param SearchWord: 搜索关键字，支持 API path
        :type SearchWord: str
        :param GatewayDeployGroupId: 部署组ID
        :type GatewayDeployGroupId: str
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None
        self.GatewayDeployGroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        self.GatewayDeployGroupId = params.get("GatewayDeployGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayApisResponse(AbstractModel):
    """DescribeGatewayApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 翻页结构
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageApiDetailInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageApiDetailInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGatewayMonitorOverviewRequest(AbstractModel):
    """DescribeGatewayMonitorOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param GatewayDeployGroupId: 网关部署组ID
        :type GatewayDeployGroupId: str
        """
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
        r"""
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


class DescribeGroupAttributeRequest(AbstractModel):
    """DescribeGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 部署组ID字段
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupAttributeResponse(AbstractModel):
    """DescribeGroupAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 虚拟机部署组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.VmGroupOther`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = VmGroupOther()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupBindedGatewaysRequest(AbstractModel):
    """DescribeGroupBindedGateways请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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


class DescribeGroupReleaseRequest(AbstractModel):
    """DescribeGroupRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 部署组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupReleaseResponse(AbstractModel):
    """DescribeGroupRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 部署组发布的相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.GroupRelease`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupRelease()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 部署组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param GroupIdList: 无
        :type GroupIdList: list of str
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
        self.GroupIdList = None


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
        self.GroupIdList = params.get("GroupIdList")
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
        r"""
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


class DescribeGroupsWithPluginRequest(AbstractModel):
    """DescribeGroupsWithPlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param PluginId: 插件ID
        :type PluginId: str
        :param Bound: 绑定/未绑定: true / false
        :type Bound: bool
        :param Offset: 翻页偏移量
        :type Offset: int
        :param Limit: 每页记录数量
        :type Limit: int
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        :param GatewayInstanceId: 网关实体ID
        :type GatewayInstanceId: str
        """
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
        r"""
        :param Result: API分组信息列表
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


class DescribeImageRepositoryRequest(AbstractModel):
    """DescribeImageRepository请求参数结构体

    """

    def __init__(self):
        r"""
        :param SearchWord: 仓库名，搜索关键字,不带命名空间的
        :type SearchWord: str
        :param Offset: 偏移量，取值从0开始
        :type Offset: int
        :param Limit: 分页个数，默认为20， 取值应为1~100
        :type Limit: int
        :param RepoType: 企业: tcr ；个人: personal或者不填
        :type RepoType: str
        :param ApplicationId: 应用id
        :type ApplicationId: str
        :param TcrRepoInfo: TcrRepoInfo值
        :type TcrRepoInfo: :class:`tencentcloud.tsf.v20180326.models.TcrRepoInfo`
        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.RepoType = None
        self.ApplicationId = None
        self.TcrRepoInfo = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.RepoType = params.get("RepoType")
        self.ApplicationId = params.get("ApplicationId")
        if params.get("TcrRepoInfo") is not None:
            self.TcrRepoInfo = TcrRepoInfo()
            self.TcrRepoInfo._deserialize(params.get("TcrRepoInfo"))
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
        r"""
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
        r"""
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
        :param RepoType: 企业: tcr ；个人: personal或者不填
        :type RepoType: str
        :param TcrRepoInfo: TcrRepoInfo值
        :type TcrRepoInfo: :class:`tencentcloud.tsf.v20180326.models.TcrRepoInfo`
        """
        self.ApplicationId = None
        self.Offset = None
        self.Limit = None
        self.QueryImageIdFlag = None
        self.SearchWord = None
        self.RepoType = None
        self.TcrRepoInfo = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.QueryImageIdFlag = params.get("QueryImageIdFlag")
        self.SearchWord = params.get("SearchWord")
        self.RepoType = params.get("RepoType")
        if params.get("TcrRepoInfo") is not None:
            self.TcrRepoInfo = TcrRepoInfo()
            self.TcrRepoInfo._deserialize(params.get("TcrRepoInfo"))
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
        r"""
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


class DescribeInovcationIndicatorsRequest(AbstractModel):
    """DescribeInovcationIndicators请求参数结构体

    """

    def __init__(self):
        r"""
        :param Dimension: 维度
        :type Dimension: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param ServiceId: 微服务ID
        :type ServiceId: str
        :param CallerServiceName: 调用方服务名
        :type CallerServiceName: str
        :param CalleeServiceName: 被调方服务名
        :type CalleeServiceName: str
        :param CallerInterfaceName: 调用方接口名
        :type CallerInterfaceName: str
        :param CalleeInterfaceName: 被调方接口名
        :type CalleeInterfaceName: str
        :param ApplicationId: 应用ID
        :type ApplicationId: str
        :param GroupId: 部署组ID
        :type GroupId: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.Dimension = None
        self.StartTime = None
        self.EndTime = None
        self.NamespaceId = None
        self.ServiceId = None
        self.CallerServiceName = None
        self.CalleeServiceName = None
        self.CallerInterfaceName = None
        self.CalleeInterfaceName = None
        self.ApplicationId = None
        self.GroupId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Dimension = params.get("Dimension")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.NamespaceId = params.get("NamespaceId")
        self.ServiceId = params.get("ServiceId")
        self.CallerServiceName = params.get("CallerServiceName")
        self.CalleeServiceName = params.get("CalleeServiceName")
        self.CallerInterfaceName = params.get("CallerInterfaceName")
        self.CalleeInterfaceName = params.get("CalleeInterfaceName")
        self.ApplicationId = params.get("ApplicationId")
        self.GroupId = params.get("GroupId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInovcationIndicatorsResponse(AbstractModel):
    """DescribeInovcationIndicators返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 服务调用监控指标
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.InvocationIndicator`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InvocationIndicator()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 分页个数，默认为20，最大100
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        :param Result: 机器列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.InstanceEnrichedInfoPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceEnrichedInfoPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInvocationMetricDataCurveRequest(AbstractModel):
    """DescribeInvocationMetricDataCurve请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Period: 查询时间粒度，单位秒可选值：60、3600、86400
        :type Period: int
        :param MetricDimensions: 查询指标维度
        :type MetricDimensions: list of MetricDimension
        :param Metrics: 查询指标名
        :type Metrics: list of Metric
        :param Kind: 视图视角。可选值：SERVER, CLIENT。默认为SERVER
        :type Kind: str
        :param Type: 类型。组件监控使用，可选值：SQL 或者 NoSQL
        :type Type: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Period = None
        self.MetricDimensions = None
        self.Metrics = None
        self.Kind = None
        self.Type = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Period = params.get("Period")
        if params.get("MetricDimensions") is not None:
            self.MetricDimensions = []
            for item in params.get("MetricDimensions"):
                obj = MetricDimension()
                obj._deserialize(item)
                self.MetricDimensions.append(obj)
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = Metric()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.Kind = params.get("Kind")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationMetricDataCurveResponse(AbstractModel):
    """DescribeInvocationMetricDataCurve返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 指标监控数据曲线集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of MetricDataCurve
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = MetricDataCurve()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInvocationMetricDataDimensionRequest(AbstractModel):
    """DescribeInvocationMetricDataDimension请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Offset: 开始index
        :type Offset: int
        :param Limit: 分页大小
        :type Limit: int
        :param DimensionName: 聚合维度
        :type DimensionName: str
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        :param MetricDimensionValues: 维度
        :type MetricDimensionValues: list of MetricDimensionValue
        """
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.DimensionName = None
        self.SearchWord = None
        self.MetricDimensionValues = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DimensionName = params.get("DimensionName")
        self.SearchWord = params.get("SearchWord")
        if params.get("MetricDimensionValues") is not None:
            self.MetricDimensionValues = []
            for item in params.get("MetricDimensionValues"):
                obj = MetricDimensionValue()
                obj._deserialize(item)
                self.MetricDimensionValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationMetricDataDimensionResponse(AbstractModel):
    """DescribeInvocationMetricDataDimension返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 维度
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageDimension`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageDimension()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInvocationMetricDataPointRequest(AbstractModel):
    """DescribeInvocationMetricDataPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param MetricDimensionValues: 维度
        :type MetricDimensionValues: list of MetricDimensionValue
        :param Metrics: 指标
        :type Metrics: list of Metric
        :param Kind: 调用视角。可选值：SERVER, CLIENT。默认为SERVER
        :type Kind: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricDimensionValues = None
        self.Metrics = None
        self.Kind = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("MetricDimensionValues") is not None:
            self.MetricDimensionValues = []
            for item in params.get("MetricDimensionValues"):
                obj = MetricDimensionValue()
                obj._deserialize(item)
                self.MetricDimensionValues.append(obj)
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = Metric()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationMetricDataPointResponse(AbstractModel):
    """DescribeInvocationMetricDataPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 单值指标列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of MetricDataSingleValue
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = MetricDataSingleValue()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInvocationMetricScatterPlotRequest(AbstractModel):
    """DescribeInvocationMetricScatterPlot请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Period: 查询时间粒度，单位秒。可选值：60、3600、86400。
        :type Period: int
        :param MetricDimensions: 查询指标维度
        :type MetricDimensions: list of MetricDimension
        :param Metrics: 查询指标名
        :type Metrics: list of Metric
        :param Kind: 视图视角。可选值：SERVER, CLIENT。默认为SERVER
        :type Kind: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Period = None
        self.MetricDimensions = None
        self.Metrics = None
        self.Kind = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Period = params.get("Period")
        if params.get("MetricDimensions") is not None:
            self.MetricDimensions = []
            for item in params.get("MetricDimensions"):
                obj = MetricDimension()
                obj._deserialize(item)
                self.MetricDimensions.append(obj)
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = Metric()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationMetricScatterPlotResponse(AbstractModel):
    """DescribeInvocationMetricScatterPlot返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 多值时间抽统计指标
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.InvocationMetricScatterPlot`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InvocationMetricScatterPlot()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeJvmMonitorRequest(AbstractModel):
    """DescribeJvmMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 查询的实例Id
        :type InstanceId: str
        :param ApplicationId: 实例所属应用Id
        :type ApplicationId: str
        :param TimeGranularity: 时间粒度,单位:秒
        :type TimeGranularity: int
        :param From: 查询数据起始时间格式(yyyy-MM-dd HH:mm:ss)
        :type From: str
        :param To: 查询数据结束时间格式(yyyy-MM-dd HH:mm:ss)
        :type To: str
        :param RequiredPictures: 查询的监控图列表,以返回值属性名作为入参
        :type RequiredPictures: list of str
        :param Tag: 扩展字段
        :type Tag: str
        """
        self.InstanceId = None
        self.ApplicationId = None
        self.TimeGranularity = None
        self.From = None
        self.To = None
        self.RequiredPictures = None
        self.Tag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ApplicationId = params.get("ApplicationId")
        self.TimeGranularity = params.get("TimeGranularity")
        self.From = params.get("From")
        self.To = params.get("To")
        self.RequiredPictures = params.get("RequiredPictures")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJvmMonitorResponse(AbstractModel):
    """DescribeJvmMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: Java实例jvm监控数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.JvmMonitorData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JvmMonitorData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeLaneRulesRequest(AbstractModel):
    """DescribeLaneRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 每页展示的条数
        :type Limit: int
        :param Offset: 翻页偏移量
        :type Offset: int
        :param SearchWord: 搜索关键词
        :type SearchWord: str
        :param RuleId: 泳道规则ID（用于精确搜索）
        :type RuleId: str
        :param RuleIdList: 无
        :type RuleIdList: list of str
        """
        self.Limit = None
        self.Offset = None
        self.SearchWord = None
        self.RuleId = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SearchWord = params.get("SearchWord")
        self.RuleId = params.get("RuleId")
        self.RuleIdList = params.get("RuleIdList")
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
        r"""
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
        r"""
        :param Limit: 每页展示的条数
        :type Limit: int
        :param Offset: 翻页偏移量
        :type Offset: int
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        :param LaneIdList: 无
        :type LaneIdList: list of str
        :param DisableProgramAuthCheck: 无
        :type DisableProgramAuthCheck: bool
        """
        self.Limit = None
        self.Offset = None
        self.SearchWord = None
        self.LaneIdList = None
        self.DisableProgramAuthCheck = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SearchWord = params.get("SearchWord")
        self.LaneIdList = params.get("LaneIdList")
        self.DisableProgramAuthCheck = params.get("DisableProgramAuthCheck")
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
        r"""
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
        r"""
        :param MicroserviceId: 微服务ID
        :type MicroserviceId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分页个数
        :type Limit: int
        :param GroupIds: 可选，根据部署组ID进行过滤
        :type GroupIds: list of str
        """
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
        r"""
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
        r"""
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
        :param MicroserviceIdList: IdList
        :type MicroserviceIdList: list of str
        :param MicroserviceNameList: 搜索的服务名列表
        :type MicroserviceNameList: list of str
        """
        self.NamespaceId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.MicroserviceIdList = None
        self.MicroserviceNameList = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.MicroserviceIdList = params.get("MicroserviceIdList")
        self.MicroserviceNameList = params.get("MicroserviceNameList")
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
        r"""
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
        r"""
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
        r"""
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


class DescribeOverviewInvocationRequest(AbstractModel):
    """DescribeOverviewInvocation请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param Type: 监控统计类型，可选值：SumReqAmount、AvgFailureRate、AvgTimeCost，分别对应请求量、请求错误率、平均响应耗时
        :type Type: str
        :param Period: 监控统计数据粒度，可选值：60、3600、86400，分别对应1分钟、1小时、1天
        :type Period: int
        :param StartTime: 查询开始时间，默认为当天的 00:00:00
        :type StartTime: str
        :param EndTime: 查询结束时间，默认为当前时间
        :type EndTime: str
        """
        self.NamespaceId = None
        self.Type = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.Type = params.get("Type")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewInvocationResponse(AbstractModel):
    """DescribeOverviewInvocation返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 监控统计数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of MetricDataPoint
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = MetricDataPoint()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePathRewriteRequest(AbstractModel):
    """DescribePathRewrite请求参数结构体

    """

    def __init__(self):
        r"""
        :param PathRewriteId: 路径重写规则ID
        :type PathRewriteId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param PackageTypeList: 程序包类型数组支持（fatjar jar war tar.gz zip）
        :type PackageTypeList: list of str
        """
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
        r"""
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


class DescribePluginInstancesRequest(AbstractModel):
    """DescribePluginInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScopeValue: 分组或者API的ID
        :type ScopeValue: str
        :param Bound: 绑定: true; 未绑定: false
        :type Bound: bool
        :param Offset: 翻页偏移量
        :type Offset: int
        :param Limit: 每页展示的条数
        :type Limit: int
        :param Type: 插件类型
        :type Type: str
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        """
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
        r"""
        :param Result: 插件信息列表
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageGatewayPlugin`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param GroupId: 实例所属groupId
        :type GroupId: str
        :param Offset: 偏移量，取值从0开始
        :type Offset: int
        :param Limit: 分页个数，默认为20， 取值应为1~50
        :type Limit: int
        :param PodNameList: 过滤字段
        :type PodNameList: list of str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param ConfigId: 需要查询的配置项ID
        :type ConfigId: str
        """
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
        r"""
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
        r"""
        :param SearchWord: 查询关键字，模糊查询：配置项名称，不传入时查询全量
        :type SearchWord: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 每页条数，默认为20
        :type Limit: int
        :param OrderBy: 按时间排序：creation_time；按名称排序：config_name
        :type OrderBy: str
        :param OrderType: 升序传 0，降序传 1
        :type OrderType: int
        :param ConfigTagList: 无
        :type ConfigTagList: list of str
        :param DisableProgramAuthCheck: 无
        :type DisableProgramAuthCheck: bool
        :param ConfigIdList: 无
        :type ConfigIdList: list of str
        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderType = None
        self.ConfigTagList = None
        self.DisableProgramAuthCheck = None
        self.ConfigIdList = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.ConfigTagList = params.get("ConfigTagList")
        self.DisableProgramAuthCheck = params.get("DisableProgramAuthCheck")
        self.ConfigIdList = params.get("ConfigIdList")
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param GroupId: 部署组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param RepositoryId: 仓库ID
        :type RepositoryId: str
        """
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
        r"""
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


class DescribeSimpleApplicationsRequest(AbstractModel):
    """DescribeSimpleApplications请求参数结构体

    """

    def __init__(self):
        r"""
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
        :param DisableProgramAuthCheck: 无
        :type DisableProgramAuthCheck: bool
        """
        self.ApplicationIdList = None
        self.ApplicationType = None
        self.Limit = None
        self.Offset = None
        self.MicroserviceType = None
        self.ApplicationResourceTypeList = None
        self.SearchWord = None
        self.DisableProgramAuthCheck = None


    def _deserialize(self, params):
        self.ApplicationIdList = params.get("ApplicationIdList")
        self.ApplicationType = params.get("ApplicationType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationResourceTypeList = params.get("ApplicationResourceTypeList")
        self.SearchWord = params.get("SearchWord")
        self.DisableProgramAuthCheck = params.get("DisableProgramAuthCheck")
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
        r"""
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
        r"""
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
        :param DisableProgramAuthCheck: 无
        :type DisableProgramAuthCheck: bool
        """
        self.ClusterIdList = None
        self.ClusterType = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None
        self.DisableProgramAuthCheck = None


    def _deserialize(self, params):
        self.ClusterIdList = params.get("ClusterIdList")
        self.ClusterType = params.get("ClusterType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        self.DisableProgramAuthCheck = params.get("DisableProgramAuthCheck")
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param DisableProgramAuthCheck: 无
        :type DisableProgramAuthCheck: bool
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
        self.DisableProgramAuthCheck = None


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
        self.DisableProgramAuthCheck = params.get("DisableProgramAuthCheck")
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
        r"""
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


class DescribeStatisticsRequest(AbstractModel):
    """DescribeStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 类型：Interface、Service、Group、Instance、SQL、NoSQL
        :type Type: str
        :param TimeStep: 步长，单位s：60、3600、86400
        :type TimeStep: int
        :param Offset: 偏移量，取值范围大于等于0，默认值为0
        :type Offset: int
        :param Limit: 单页请求配置数量，取值范围[1, 50]，默认值为10
        :type Limit: int
        :param NamespaceId: 命名空间Id
        :type NamespaceId: str
        :param OrderBy: 排序字段:AvgTimeConsuming[默认]、RequestCount、ErrorRate。实例监控还支持 CpuPercent
        :type OrderBy: str
        :param OrderType: 排序方式：ASC:0、DESC:1
        :type OrderType: int
        :param EndTime: 开始时间：年月日 时分秒2020-05-12 14:43:12
        :type EndTime: str
        :param StartTime: 开始时间：年月日 时分秒2020-05-12 14:43:12
        :type StartTime: str
        :param ServiceName: 服务名称
        :type ServiceName: str
        :param SearchWord: 搜索关键词
        :type SearchWord: str
        :param MetricDimensionValues: 维度
        :type MetricDimensionValues: list of MetricDimensionValue
        :param BucketKey: 聚合关键词
        :type BucketKey: str
        :param DbName: 数据库
        :type DbName: str
        """
        self.Type = None
        self.TimeStep = None
        self.Offset = None
        self.Limit = None
        self.NamespaceId = None
        self.OrderBy = None
        self.OrderType = None
        self.EndTime = None
        self.StartTime = None
        self.ServiceName = None
        self.SearchWord = None
        self.MetricDimensionValues = None
        self.BucketKey = None
        self.DbName = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TimeStep = params.get("TimeStep")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NamespaceId = params.get("NamespaceId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.ServiceName = params.get("ServiceName")
        self.SearchWord = params.get("SearchWord")
        if params.get("MetricDimensionValues") is not None:
            self.MetricDimensionValues = []
            for item in params.get("MetricDimensionValues"):
                obj = MetricDimensionValue()
                obj._deserialize(item)
                self.MetricDimensionValues.append(obj)
        self.BucketKey = params.get("BucketKey")
        self.DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStatisticsResponse(AbstractModel):
    """DescribeStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 查询服务统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ServiceStatisticsResults`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceStatisticsResults()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param TaskLogId: 任务历史ID
        :type TaskLogId: str
        """
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
        r"""
        :param Result: 任务详情
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskRecord`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        """
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
        r"""
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


class DescribeTaskRecordsRequest(AbstractModel):
    """DescribeTaskRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 翻页偏移量。
        :type Offset: int
        :param Limit: 翻页查询单页数量。
        :type Limit: int
        :param SearchWord: 模糊查询关键字，支持任务ID和任务名称。
        :type SearchWord: str
        :param TaskState: 任务启用状态。enabled/disabled
        :type TaskState: str
        :param GroupId: 分组ID。
        :type GroupId: str
        :param TaskType: 任务类型。
        :type TaskType: str
        :param ExecuteType: 任务触发类型，UNICAST、BROADCAST。
        :type ExecuteType: str
        :param Ids: 无
        :type Ids: list of str
        """
        self.Offset = None
        self.Limit = None
        self.SearchWord = None
        self.TaskState = None
        self.GroupId = None
        self.TaskType = None
        self.ExecuteType = None
        self.Ids = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        self.TaskState = params.get("TaskState")
        self.GroupId = params.get("GroupId")
        self.TaskType = params.get("TaskType")
        self.ExecuteType = params.get("ExecuteType")
        self.Ids = params.get("Ids")
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
        r"""
        :param Result: 任务记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskRecordPage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param GatewayDeployGroupId: 网关部署组ID
        :type GatewayDeployGroupId: str
        :param ApiId: 网关分组Api ID
        :type ApiId: str
        :param StartTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss
        :type StartTime: str
        :param EndTime: 查询的日期,格式：yyyy-MM-dd HH:mm:ss
        :type EndTime: str
        :param GatewayInstanceId: 网关实例ID
        :type GatewayInstanceId: str
        :param GroupId: 网关分组ID
        :type GroupId: str
        :param Offset: 翻页查询偏移量
        :type Offset: int
        :param Limit: 翻页查询每页记录数
        :type Limit: int
        :param Period: 监控统计数据粒度
        :type Period: int
        """
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
        r"""
        :param Result: 单元化使用统计对象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.GroupUnitApiUseStatistics`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param GatewayInstanceId: 网关实体ID
        :type GatewayInstanceId: str
        :param SearchWord: 根据命名空间名或ID模糊查询
        :type SearchWord: str
        :param Offset: 翻页查询偏移量
        :type Offset: int
        :param Limit: 翻页查询每页记录数
        :type Limit: int
        """
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
        r"""
        :param Result: 单元化命名空间对象列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageUnitNamespace`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Id: 单元化规则ID
        :type Id: str
        """
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
        r"""
        :param Result: 单元化规则对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.UnitRule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param GatewayInstanceId: 网关实体ID
        :type GatewayInstanceId: str
        :param SearchWord: 根据规则名或备注内容模糊查询
        :type SearchWord: str
        :param Status: 启用状态, disabled: 未发布， enabled: 发布
        :type Status: str
        :param Offset: 翻页查询偏移量
        :type Offset: int
        :param Limit: 翻页查询每页记录数
        :type Limit: int
        """
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
        r"""
        :param Result: 分页列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of TsfPageUnitRule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
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
        r"""
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


class DescribeUsableUnitNamespacesRequest(AbstractModel):
    """DescribeUsableUnitNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param SearchWord: 根据命名空间名或ID模糊查询
        :type SearchWord: str
        :param Offset: 翻页查询偏移量
        :type Offset: int
        :param Limit: 翻页查询每页记录数
        :type Limit: int
        """
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
        r"""
        :param Result: 单元化命名空间对象列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageUnitNamespace`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param FlowId: 工作流 ID
        :type FlowId: str
        """
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
        r"""
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
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        """
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
        r"""
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


class DisableUnitRouteRequest(AbstractModel):
    """DisableUnitRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 网关实体ID
        :type Id: str
        """
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
        r"""
        :param Result: 返回结果，成功失败
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


class DisableUnitRuleRequest(AbstractModel):
    """DisableUnitRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 规则ID
        :type Id: str
        """
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
        r"""
        :param Result: 是否成功
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


class DraftApiGroupRequest(AbstractModel):
    """DraftApiGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: Api 分组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
        :param FlowId: 工作流 ID
        :type FlowId: str
        """
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
        r"""
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
        r"""
        :param TaskId: 启用任务
        :type TaskId: str
        """
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
        r"""
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


class EnableUnitRouteRequest(AbstractModel):
    """EnableUnitRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 网关实体ID
        :type Id: str
        """
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
        r"""
        :param Result: 返回结果，成功失败
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


class EnableUnitRuleRequest(AbstractModel):
    """EnableUnitRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 规则ID
        :type Id: str
        """
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
        r"""
        :param Result: 是否成功
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


class Env(AbstractModel):
    """环境变量

    """

    def __init__(self):
        r"""
        :param Name: 环境变量名称
        :type Name: str
        :param Value: 环境变量值
        :type Value: str
        :param ValueFrom: k8s ValueFrom
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueFrom: :class:`tencentcloud.tsf.v20180326.models.ValueFrom`
        """
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
        r"""
        :param FlowId: 工作流 ID
        :type FlowId: str
        """
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
        r"""
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
        r"""
        :param TaskId: 任务 ID。
        :type TaskId: str
        """
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
        r"""
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
        r"""
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
        r"""
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


class FieldRef(AbstractModel):
    """容器 env 的 FieldRef

    """

    def __init__(self):
        r"""
        :param FieldPath: k8s 的 FieldPath
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldPath: str
        """
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
        r"""
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
        :param ConfigFileName: 配置项文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigFileName: str
        :param ConfigFileValue: 配置项文件内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigFileValue: str
        :param ConfigFileCode: 配置项文件编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigFileCode: str
        :param CreationTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param ApplicationId: 配置项归属应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param DeleteFlag: 删除标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteFlag: bool
        :param ConfigVersionCount: 配置项版本数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigVersionCount: int
        :param LastUpdateTime: 配置项最后更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param ConfigFilePath: 发布路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigFilePath: str
        :param ConfigPostCmd: 后置命令
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigPostCmd: str
        :param ConfigFileValueLength: 配置项文件长度
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigFileValueLength: int
        """
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
        


class FileConfigRelease(AbstractModel):
    """文件配置项发布信息

    """

    def __init__(self):
        r"""
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
        :param ReleaseDesc: 发布描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseDesc: str
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
        """
        self.ConfigReleaseId = None
        self.ConfigId = None
        self.ConfigName = None
        self.ConfigVersion = None
        self.ReleaseDesc = None
        self.ReleaseTime = None
        self.GroupId = None
        self.GroupName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.ClusterId = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.ConfigReleaseId = params.get("ConfigReleaseId")
        self.ConfigId = params.get("ConfigId")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ReleaseDesc = params.get("ReleaseDesc")
        self.ReleaseTime = params.get("ReleaseTime")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """用于请求参数中的条件过滤字段

    """

    def __init__(self):
        r"""
        :param Name: 过滤条件名
        :type Name: str
        :param Values: 过滤条件匹配值，几个条件间是或关系
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
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
        r"""
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
        :param GatewayInstanceType: 网关实例的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayInstanceType: str
        :param GatewayInstanceId: 网关实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayInstanceId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param Id: 网关插件id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param Name: 插件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Type: 插件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Description: 插件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param UpdatedTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        :param Status: 发布状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
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
        r"""
        :param PluginId: 插件id
        :type PluginId: str
        :param ScopeType: 插件绑定到的对象类型:group/api
        :type ScopeType: str
        :param ScopeValue: 插件绑定到的对象主键值，例如分组的ID/API的ID
        :type ScopeValue: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupRelease(AbstractModel):
    """部署组配置发布相关信息

    """

    def __init__(self):
        r"""
        :param PackageId: 程序包ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param PackageName: 程序包名
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param PackageVersion: 程序包版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param RepoName: 镜像名
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoName: str
        :param TagName: 镜像版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param PublicConfigReleaseList: 已发布的全局配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicConfigReleaseList: list of ConfigRelease
        :param ConfigReleaseList: 已发布的应用配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigReleaseList: list of ConfigRelease
        :param FileConfigReleaseList: 已发布的文件配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FileConfigReleaseList: list of FileConfigRelease
        """
        self.PackageId = None
        self.PackageName = None
        self.PackageVersion = None
        self.RepoName = None
        self.TagName = None
        self.PublicConfigReleaseList = None
        self.ConfigReleaseList = None
        self.FileConfigReleaseList = None


    def _deserialize(self, params):
        self.PackageId = params.get("PackageId")
        self.PackageName = params.get("PackageName")
        self.PackageVersion = params.get("PackageVersion")
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")
        if params.get("PublicConfigReleaseList") is not None:
            self.PublicConfigReleaseList = []
            for item in params.get("PublicConfigReleaseList"):
                obj = ConfigRelease()
                obj._deserialize(item)
                self.PublicConfigReleaseList.append(obj)
        if params.get("ConfigReleaseList") is not None:
            self.ConfigReleaseList = []
            for item in params.get("ConfigReleaseList"):
                obj = ConfigRelease()
                obj._deserialize(item)
                self.ConfigReleaseList.append(obj)
        if params.get("FileConfigReleaseList") is not None:
            self.FileConfigReleaseList = []
            for item in params.get("FileConfigReleaseList"):
                obj = FileConfigRelease()
                obj._deserialize(item)
                self.FileConfigReleaseList.append(obj)
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
        r"""
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param SumReqAmount: 该API在该命名空间下的总调用次数
        :type SumReqAmount: str
        :param AvgFailureRate: 该API在该命名空间下的平均错误率
        :type AvgFailureRate: str
        :param AvgTimeCost: 该API在该命名空间下的平均响应时间
        :type AvgTimeCost: str
        :param MetricDataPointMap: 监控数据曲线点位图Map集合
        :type MetricDataPointMap: :class:`tencentcloud.tsf.v20180326.models.MetricDataPointMap`
        :param TopStatusCode: 状态码分布详情
        :type TopStatusCode: list of ApiUseStatisticsEntity
        :param TopTimeCost: 耗时分布详情
        :type TopTimeCost: list of ApiUseStatisticsEntity
        :param Quantile: 分位值对象
        :type Quantile: :class:`tencentcloud.tsf.v20180326.models.QuantileEntity`
        """
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
        r"""
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param Content: 查询网关API监控明细对象集合
        :type Content: list of GroupUnitApiDailyUseStatistics
        """
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
        r"""
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
        r"""
        :param Path: 健康检查路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        :param TcrRepoInfo: TcrRepoInfo值
注意：此字段可能返回 null，表示取不到有效值。
        :type TcrRepoInfo: :class:`tencentcloud.tsf.v20180326.models.TcrRepoInfo`
        :param TcrBindingId: TcrBindingId值
注意：此字段可能返回 null，表示取不到有效值。
        :type TcrBindingId: int
        :param ApplicationId: applicationid值
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: ApplicationName值（废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationName: :class:`tencentcloud.tsf.v20180326.models.ScalableRule`
        :param ApplicationNameReal: ApplicationName值
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationNameReal: str
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
        self.TcrRepoInfo = None
        self.TcrBindingId = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationNameReal = None


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
        if params.get("TcrRepoInfo") is not None:
            self.TcrRepoInfo = TcrRepoInfo()
            self.TcrRepoInfo._deserialize(params.get("TcrRepoInfo"))
        self.TcrBindingId = params.get("TcrBindingId")
        self.ApplicationId = params.get("ApplicationId")
        if params.get("ApplicationName") is not None:
            self.ApplicationName = ScalableRule()
            self.ApplicationName._deserialize(params.get("ApplicationName"))
        self.ApplicationNameReal = params.get("ApplicationNameReal")
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
        r"""
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
        r"""
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
        :param TcrRepoInfo: TcrRepoInfo值
注意：此字段可能返回 null，表示取不到有效值。
        :type TcrRepoInfo: :class:`tencentcloud.tsf.v20180326.models.TcrRepoInfo`
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
        self.TcrRepoInfo = None


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
        if params.get("TcrRepoInfo") is not None:
            self.TcrRepoInfo = TcrRepoInfo()
            self.TcrRepoInfo._deserialize(params.get("TcrRepoInfo"))
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndicatorCoord(AbstractModel):
    """监控指标坐标

    """

    def __init__(self):
        r"""
        :param CoordX: 指标横坐标值
注意：此字段可能返回 null，表示取不到有效值。
        :type CoordX: str
        :param CoordY: 指标纵坐标值
注意：此字段可能返回 null，表示取不到有效值。
        :type CoordY: str
        :param CoordTag: 指标标签，用于标识附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CoordTag: str
        """
        self.CoordX = None
        self.CoordY = None
        self.CoordTag = None


    def _deserialize(self, params):
        self.CoordX = params.get("CoordX")
        self.CoordY = params.get("CoordY")
        self.CoordTag = params.get("CoordTag")
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
        r"""
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
        :param AgentVersion: agent版本
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentVersion: str
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnrichedInfo(AbstractModel):
    """包含虚拟机所在TSF中的位置信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 机器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 机器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param LanIp: 机器内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type LanIp: str
        :param WanIp: 机器外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type WanIp: str
        :param VpcId: 机器所在VPC
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param InstanceStatus: 机器运行状态 Pending Running Stopped Rebooting Starting Stopping Abnormal Unknown
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStatus: str
        :param InstanceAvailableStatus: 机器可用状态（表示机器上的Agent在线）
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAvailableStatus: str
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
        :param GroupId: 机器所在部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 部署组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.LanIp = None
        self.WanIp = None
        self.VpcId = None
        self.InstanceStatus = None
        self.InstanceAvailableStatus = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationType = None
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterType = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.LanIp = params.get("LanIp")
        self.WanIp = params.get("WanIp")
        self.VpcId = params.get("VpcId")
        self.InstanceStatus = params.get("InstanceStatus")
        self.InstanceAvailableStatus = params.get("InstanceAvailableStatus")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterType = params.get("ClusterType")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnrichedInfoPage(AbstractModel):
    """InstanceEnrichedInfo列表结构

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of InstanceEnrichedInfo
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = InstanceEnrichedInfo()
                obj._deserialize(item)
                self.Content.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationIndicator(AbstractModel):
    """服务调用监控指标

    """

    def __init__(self):
        r"""
        :param InvocationQuantity: 总请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationQuantity: int
        :param InvocationSuccessRate: 请求成功率，百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationSuccessRate: float
        :param InvocationAvgDuration: 请求平均耗时，单位毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationAvgDuration: float
        :param InvocationSuccessDistribution: 成功请求数时间分布
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationSuccessDistribution: list of IndicatorCoord
        :param InvocationFailedDistribution: 失败请求数时间分布
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationFailedDistribution: list of IndicatorCoord
        :param InvocationStatusDistribution: 状态码分布
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationStatusDistribution: list of IndicatorCoord
        :param InvocationDurationDistribution: 时延分布
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationDurationDistribution: list of IndicatorCoord
        :param InvocationQuantityDistribution: 并发请求次数时间分布
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationQuantityDistribution: list of IndicatorCoord
        """
        self.InvocationQuantity = None
        self.InvocationSuccessRate = None
        self.InvocationAvgDuration = None
        self.InvocationSuccessDistribution = None
        self.InvocationFailedDistribution = None
        self.InvocationStatusDistribution = None
        self.InvocationDurationDistribution = None
        self.InvocationQuantityDistribution = None


    def _deserialize(self, params):
        self.InvocationQuantity = params.get("InvocationQuantity")
        self.InvocationSuccessRate = params.get("InvocationSuccessRate")
        self.InvocationAvgDuration = params.get("InvocationAvgDuration")
        if params.get("InvocationSuccessDistribution") is not None:
            self.InvocationSuccessDistribution = []
            for item in params.get("InvocationSuccessDistribution"):
                obj = IndicatorCoord()
                obj._deserialize(item)
                self.InvocationSuccessDistribution.append(obj)
        if params.get("InvocationFailedDistribution") is not None:
            self.InvocationFailedDistribution = []
            for item in params.get("InvocationFailedDistribution"):
                obj = IndicatorCoord()
                obj._deserialize(item)
                self.InvocationFailedDistribution.append(obj)
        if params.get("InvocationStatusDistribution") is not None:
            self.InvocationStatusDistribution = []
            for item in params.get("InvocationStatusDistribution"):
                obj = IndicatorCoord()
                obj._deserialize(item)
                self.InvocationStatusDistribution.append(obj)
        if params.get("InvocationDurationDistribution") is not None:
            self.InvocationDurationDistribution = []
            for item in params.get("InvocationDurationDistribution"):
                obj = IndicatorCoord()
                obj._deserialize(item)
                self.InvocationDurationDistribution.append(obj)
        if params.get("InvocationQuantityDistribution") is not None:
            self.InvocationQuantityDistribution = []
            for item in params.get("InvocationQuantityDistribution"):
                obj = IndicatorCoord()
                obj._deserialize(item)
                self.InvocationQuantityDistribution.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationMetricScatterPlot(AbstractModel):
    """监控数据散点图

    """

    def __init__(self):
        r"""
        :param EndTime: 时间轴截止时间，GMT，精确到毫秒
        :type EndTime: int
        :param StartTime: 时间粒度
        :type StartTime: int
        :param Period: 时间轴开始时间，GMT，精确到毫秒
        :type Period: int
        :param DataPoints: 多值数据点集合
注意：此字段可能返回 null，表示取不到有效值。
        :type DataPoints: list of MultiValueDataPoints
        """
        self.EndTime = None
        self.StartTime = None
        self.Period = None
        self.DataPoints = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.Period = params.get("Period")
        if params.get("DataPoints") is not None:
            self.DataPoints = []
            for item in params.get("DataPoints"):
                obj = MultiValueDataPoints()
                obj._deserialize(item)
                self.DataPoints.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JvmMonitorData(AbstractModel):
    """DescribeJvmMonitor查询jvm监控数据接口返回数据封装

    """

    def __init__(self):
        r"""
        :param HeapMemory: 堆内存监控图,三条线
注意：此字段可能返回 null，表示取不到有效值。
        :type HeapMemory: :class:`tencentcloud.tsf.v20180326.models.MemoryPicture`
        :param NonHeapMemory: 非堆内存监控图,三条线
注意：此字段可能返回 null，表示取不到有效值。
        :type NonHeapMemory: :class:`tencentcloud.tsf.v20180326.models.MemoryPicture`
        :param EdenSpace: 伊甸园区监控图,三条线
注意：此字段可能返回 null，表示取不到有效值。
        :type EdenSpace: :class:`tencentcloud.tsf.v20180326.models.MemoryPicture`
        :param SurvivorSpace: 幸存者区监控图,三条线
注意：此字段可能返回 null，表示取不到有效值。
        :type SurvivorSpace: :class:`tencentcloud.tsf.v20180326.models.MemoryPicture`
        :param OldSpace: 老年代监控图,三条线
注意：此字段可能返回 null，表示取不到有效值。
        :type OldSpace: :class:`tencentcloud.tsf.v20180326.models.MemoryPicture`
        :param MetaSpace: 元空间监控图,三条线
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaSpace: :class:`tencentcloud.tsf.v20180326.models.MemoryPicture`
        :param ThreadPicture: 线程监控图,三条线
注意：此字段可能返回 null，表示取不到有效值。
        :type ThreadPicture: :class:`tencentcloud.tsf.v20180326.models.ThreadPicture`
        :param YoungGC: youngGC增量监控图,一条线
注意：此字段可能返回 null，表示取不到有效值。
        :type YoungGC: list of CurvePoint
        :param FullGC: fullGC增量监控图,一条线
注意：此字段可能返回 null，表示取不到有效值。
        :type FullGC: list of CurvePoint
        :param CpuUsage: cpu使用率,一条线
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuUsage: list of CurvePoint
        :param ClassCount: 加载类数,一条线
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassCount: list of CurvePoint
        """
        self.HeapMemory = None
        self.NonHeapMemory = None
        self.EdenSpace = None
        self.SurvivorSpace = None
        self.OldSpace = None
        self.MetaSpace = None
        self.ThreadPicture = None
        self.YoungGC = None
        self.FullGC = None
        self.CpuUsage = None
        self.ClassCount = None


    def _deserialize(self, params):
        if params.get("HeapMemory") is not None:
            self.HeapMemory = MemoryPicture()
            self.HeapMemory._deserialize(params.get("HeapMemory"))
        if params.get("NonHeapMemory") is not None:
            self.NonHeapMemory = MemoryPicture()
            self.NonHeapMemory._deserialize(params.get("NonHeapMemory"))
        if params.get("EdenSpace") is not None:
            self.EdenSpace = MemoryPicture()
            self.EdenSpace._deserialize(params.get("EdenSpace"))
        if params.get("SurvivorSpace") is not None:
            self.SurvivorSpace = MemoryPicture()
            self.SurvivorSpace._deserialize(params.get("SurvivorSpace"))
        if params.get("OldSpace") is not None:
            self.OldSpace = MemoryPicture()
            self.OldSpace._deserialize(params.get("OldSpace"))
        if params.get("MetaSpace") is not None:
            self.MetaSpace = MemoryPicture()
            self.MetaSpace._deserialize(params.get("MetaSpace"))
        if params.get("ThreadPicture") is not None:
            self.ThreadPicture = ThreadPicture()
            self.ThreadPicture._deserialize(params.get("ThreadPicture"))
        if params.get("YoungGC") is not None:
            self.YoungGC = []
            for item in params.get("YoungGC"):
                obj = CurvePoint()
                obj._deserialize(item)
                self.YoungGC.append(obj)
        if params.get("FullGC") is not None:
            self.FullGC = []
            for item in params.get("FullGC"):
                obj = CurvePoint()
                obj._deserialize(item)
                self.FullGC.append(obj)
        if params.get("CpuUsage") is not None:
            self.CpuUsage = []
            for item in params.get("CpuUsage"):
                obj = CurvePoint()
                obj._deserialize(item)
                self.CpuUsage.append(obj)
        if params.get("ClassCount") is not None:
            self.ClassCount = []
            for item in params.get("ClassCount"):
                obj = CurvePoint()
                obj._deserialize(item)
                self.ClassCount.append(obj)
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MemoryPicture(AbstractModel):
    """Jvm监控内存数据封装

    """

    def __init__(self):
        r"""
        :param Max: 内存最大值
        :type Max: list of CurvePoint
        :param Used: 已用内存大小
        :type Used: list of CurvePoint
        :param Committed: 系统分配内存大小
        :type Committed: list of CurvePoint
        """
        self.Max = None
        self.Used = None
        self.Committed = None


    def _deserialize(self, params):
        if params.get("Max") is not None:
            self.Max = []
            for item in params.get("Max"):
                obj = CurvePoint()
                obj._deserialize(item)
                self.Max.append(obj)
        if params.get("Used") is not None:
            self.Used = []
            for item in params.get("Used"):
                obj = CurvePoint()
                obj._deserialize(item)
                self.Used.append(obj)
        if params.get("Committed") is not None:
            self.Committed = []
            for item in params.get("Committed"):
                obj = CurvePoint()
                obj._deserialize(item)
                self.Committed.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Metric(AbstractModel):
    """指标

    """

    def __init__(self):
        r"""
        :param Name: 指标名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Function: 指标计算方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Function: str
        """
        self.Name = None
        self.Function = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Function = params.get("Function")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDataCurve(AbstractModel):
    """指标监控数据曲线

    """

    def __init__(self):
        r"""
        :param MetricName: 指标名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param MetricFunction: 指标计算方式
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricFunction: str
        :param MetricDataPoints: 指标数据点集合
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricDataPoints: list of MetricDataPoint
        """
        self.MetricName = None
        self.MetricFunction = None
        self.MetricDataPoints = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.MetricFunction = params.get("MetricFunction")
        if params.get("MetricDataPoints") is not None:
            self.MetricDataPoints = []
            for item in params.get("MetricDataPoints"):
                obj = MetricDataPoint()
                obj._deserialize(item)
                self.MetricDataPoints.append(obj)
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
        r"""
        :param Key: 数据点键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 数据点值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Tag: 数据点标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        """
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
        r"""
        :param SumReqAmount: 总调用次数监控数据点集合
        :type SumReqAmount: list of MetricDataPoint
        :param AvgFailureRate: 平均错误率监控数据点集合
        :type AvgFailureRate: list of MetricDataPoint
        :param AvgTimeCost: 平均响应时间监控数据点集合
        :type AvgTimeCost: list of MetricDataPoint
        """
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
        


class MetricDataSingleValue(AbstractModel):
    """单值指标

    """

    def __init__(self):
        r"""
        :param MetricName: 指标
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param MetricFunction: 统计方式
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricFunction: str
        :param MetricDataValue: 指标值
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricDataValue: str
        """
        self.MetricName = None
        self.MetricFunction = None
        self.MetricDataValue = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.MetricFunction = params.get("MetricFunction")
        self.MetricDataValue = params.get("MetricDataValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDimension(AbstractModel):
    """指标维度

    """

    def __init__(self):
        r"""
        :param Name: 指标维度名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 指标维度取值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricDimensionValue(AbstractModel):
    """指标维度多值匹配

    """

    def __init__(self):
        r"""
        :param Name: 维度名
        :type Name: str
        :param Value: 维度值
        :type Value: list of str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
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
        r"""
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
        r"""
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
        :param Alias: 部署组备注
        :type Alias: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :type ShardArguments: list of ShardArgument
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
        :param ProgramIdList: 无
        :type ProgramIdList: list of str
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
        self.ProgramIdList = None


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
        self.ProgramIdList = params.get("ProgramIdList")
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
        r"""
        :param Result: 更新是否成功
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


class ModifyUploadInfoRequest(AbstractModel):
    """ModifyUploadInfo请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiValue(AbstractModel):
    """多值数据

    """

    def __init__(self):
        r"""
        :param Values: 数据点
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of float
        """
        self.Values = None


    def _deserialize(self, params):
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiValueDataPoints(AbstractModel):
    """多值数据点集合

    """

    def __init__(self):
        r"""
        :param Points: 多值数据点
        :type Points: list of MultiValue
        :param MetricName: 指标名称
        :type MetricName: str
        :param PointKeys: 多值数据点key列表，每个值表示当前数据点所在区域的下限
        :type PointKeys: list of str
        """
        self.Points = None
        self.MetricName = None
        self.PointKeys = None


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = MultiValue()
                obj._deserialize(item)
                self.Points.append(obj)
        self.MetricName = params.get("MetricName")
        self.PointKeys = params.get("PointKeys")
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
        r"""
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
        :param KubeInjectEnable: KubeInjectEnable值
注意：此字段可能返回 null，表示取不到有效值。
        :type KubeInjectEnable: bool
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
        self.KubeInjectEnable = None


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
        self.KubeInjectEnable = params.get("KubeInjectEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateApplicationTcrBindingRequest(AbstractModel):
    """OperateApplicationTcrBinding请求参数结构体

    """

    def __init__(self):
        r"""
        :param Command: bind 或 unbind
        :type Command: str
        :param ApplicationId: 应用id
        :type ApplicationId: str
        :param TcrRepoInfo: TcrRepoInfo值
        :type TcrRepoInfo: :class:`tencentcloud.tsf.v20180326.models.TcrRepoInfo`
        """
        self.Command = None
        self.ApplicationId = None
        self.TcrRepoInfo = None


    def _deserialize(self, params):
        self.Command = params.get("Command")
        self.ApplicationId = params.get("ApplicationId")
        if params.get("TcrRepoInfo") is not None:
            self.TcrRepoInfo = TcrRepoInfo()
            self.TcrRepoInfo._deserialize(params.get("TcrRepoInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateApplicationTcrBindingResponse(AbstractModel):
    """OperateApplicationTcrBinding返回参数结构体

    """

    def __init__(self):
        r"""
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


class OperationInfo(AbstractModel):
    """提供给前端，控制按钮是否显示

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param TargetPort: 服务端口
        :type TargetPort: int
        :param Protocol: 端口协议
        :type Protocol: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param FlowBatchId: 工作流批次 ID
        :type FlowBatchId: str
        """
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
        r"""
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
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        """
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
        r"""
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
        r"""
        :param GroupId: Api 分组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
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
        r"""
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


class ReleaseFileConfigRequest(AbstractModel):
    """ReleaseFileConfig请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param Result: 发布结果
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


class ReleasePublicConfigRequest(AbstractModel):
    """ReleasePublicConfig请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param Resource: k8s 的 Resource
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: str
        """
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
        r"""
        :param ConfigReleaseId: 配置项发布ID
        :type ConfigReleaseId: str
        """
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
        r"""
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
        r"""
        :param ConfigReleaseId: 配置项发布ID
        :type ConfigReleaseId: str
        """
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
        r"""
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
        r"""
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
        r"""
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


class ScalableRule(AbstractModel):
    """ScalableRule值

    """

    def __init__(self):
        r"""
        :param RuleId: RuleId值
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param Name: Name值
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param ExpandVmCountLimit: ExpandVmCountLimit值
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpandVmCountLimit: int
        :param ShrinkVmCountLimit: ShrinkVmCountLimit值
注意：此字段可能返回 null，表示取不到有效值。
        :type ShrinkVmCountLimit: int
        :param GroupCount: GroupCount值
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupCount: int
        :param Desc: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param Description: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self.RuleId = None
        self.Name = None
        self.ExpandVmCountLimit = None
        self.ShrinkVmCountLimit = None
        self.GroupCount = None
        self.Desc = None
        self.Description = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Name = params.get("Name")
        self.ExpandVmCountLimit = params.get("ExpandVmCountLimit")
        self.ShrinkVmCountLimit = params.get("ShrinkVmCountLimit")
        self.GroupCount = params.get("GroupCount")
        self.Desc = params.get("Desc")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulingStrategy(AbstractModel):
    """tsf 容器集群节点调度策略

    """

    def __init__(self):
        r"""
        :param Type: NONE：不使用调度策略；CROSS_AZ：跨可用区部署
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
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
        r"""
        :param ConfigId: 日志配置项ID
        :type ConfigId: str
        :param InstanceIds: 机器实例ID，不传表示全部实例
        :type InstanceIds: list of str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Offset: 请求偏移量，取值范围大于等于0，默认值为0
        :type Offset: int
        :param Limit: 单页请求配置数量，取值范围[1, 200]，默认值为50
        :type Limit: int
        :param OrderBy: 排序规则，默认值"time"
        :type OrderBy: str
        :param OrderType: 排序方式，取值"asc"或"desc"，默认值"desc"
        :type OrderType: str
        :param SearchWords: 检索关键词
        :type SearchWords: list of str
        :param GroupIds: 部署组ID列表，不传表示全部部署组
        :type GroupIds: list of str
        :param SearchWordType: 检索类型，取值"LUCENE", "REGEXP", "NORMAL"
        :type SearchWordType: str
        :param BatchType: 批量请求类型，取值"page"或"scroll"
        :type BatchType: str
        :param ScrollId: 游标ID
        :type ScrollId: str
        """
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
        r"""
        :param Result: 业务日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageBusinessLogV2`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: 机器实例ID
        :type InstanceId: str
        :param Limit: 单页请求配置数量，取值范围[1, 500]，默认值为100
        :type Limit: int
        :param SearchWords: 检索关键词
        :type SearchWords: list of str
        :param StartTime: 查询起始时间
        :type StartTime: str
        :param GroupId: 部署组ID
        :type GroupId: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Offset: 请求偏移量，取值范围大于等于0，默认值为
0
        :type Offset: int
        :param OrderBy: 排序规则，默认值"time"
        :type OrderBy: str
        :param OrderType: 排序方式，取值"asc"或"desc"，默认
值"desc"
        :type OrderType: str
        :param SearchWordType: 检索类型，取值"LUCENE", "REGEXP",
"NORMAL"
        :type SearchWordType: str
        :param BatchType: 批量请求类型，取值"page"或"scroll"，默认
值"page"
        :type BatchType: str
        :param ScrollId: 游标ID
        :type ScrollId: str
        """
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
        r"""
        :param Result: 标准输出日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageStdoutLogV2`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageStdoutLogV2()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ServiceConfig(AbstractModel):
    """服务配置

    """

    def __init__(self):
        r"""
        :param Name: 服务名
        :type Name: str
        :param Ports: 端口信息列表
        :type Ports: list of Ports
        :param HealthCheck: 健康检查配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`tencentcloud.tsf.v20180326.models.HealthCheckConfig`
        """
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
        r"""
        :param AccessType: 0:公网, 1:集群内访问, 2：NodePort, 3: VPC 内网访问
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessType: int
        :param ProtocolPorts: 容器端口映射
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolPorts: list of ProtocolPort
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param DisableService: 是否创建 k8s service，默认为 false
注意：此字段可能返回 null，表示取不到有效值。
        :type DisableService: bool
        :param HeadlessService: service 是否为 headless 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadlessService: bool
        :param AllowDeleteService: 当为 true 且 DisableService 也为 true 时，会删除之前创建的 service，请小心使用
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowDeleteService: bool
        :param OpenSessionAffinity: 开启SessionAffinity，true为开启，false为不开启，默认为false
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenSessionAffinity: bool
        :param SessionAffinityTimeoutSeconds: SessionAffinity会话时间，默认10800
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAffinityTimeoutSeconds: int
        """
        self.AccessType = None
        self.ProtocolPorts = None
        self.SubnetId = None
        self.DisableService = None
        self.HeadlessService = None
        self.AllowDeleteService = None
        self.OpenSessionAffinity = None
        self.SessionAffinityTimeoutSeconds = None


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
        self.OpenSessionAffinity = params.get("OpenSessionAffinity")
        self.SessionAffinityTimeoutSeconds = params.get("SessionAffinityTimeoutSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceStatisticsResult(AbstractModel):
    """服务统计结果

    """

    def __init__(self):
        r"""
        :param Path: 请求模版路径:type为接口时返回，服务时不返回
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Method: 请求方法:type为接口时返回，服务时不返回
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param MicroserviceId: 微服务Id
        :type MicroserviceId: str
        :param MicroserviceName: 微服务名称
        :type MicroserviceName: str
        :param RequestCount: 请求数
        :type RequestCount: int
        :param ErrorRate: 请求错误率，不带百分号
        :type ErrorRate: float
        :param AvgTimeConsuming: 平均响应耗时ms
        :type AvgTimeConsuming: float
        :param MetricDataCurves: 响应耗时曲线
        :type MetricDataCurves: list of MetricDataCurve
        :param InstanceId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 实例name
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param GroupId: 部署组id
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 部署组name
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param ClusterType: 部署组类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param GroupExist: 部署组是否存在
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupExist: int
        :param InstanceExist: 实例是否存在，仅限cvm
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceExist: int
        :param ApplicationId: 应用id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param MicroserviceType: 微服务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param CpuPercent: cpu使用率
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuPercent: int
        :param HeapUsed: 已用堆大小,单位KB
注意：此字段可能返回 null，表示取不到有效值。
        :type HeapUsed: int
        :param DbName: 数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type DbName: str
        :param Script: Script值
注意：此字段可能返回 null，表示取不到有效值。
        :type Script: str
        :param DbType: 数据库类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DbType: str
        :param Apdex: Apdex值
注意：此字段可能返回 null，表示取不到有效值。
        :type Apdex: float
        :param Qps: Qps值
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: float
        :param InstanceOnlineCount: 实例在线数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceOnlineCount: int
        :param InstanceTotalCount: 实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTotalCount: int
        :param Status: normal/error
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ErrorRateLevel: normal/warn/error
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorRateLevel: str
        :param AvgTimeConsumingLevel: normal/warn/error
注意：此字段可能返回 null，表示取不到有效值。
        :type AvgTimeConsumingLevel: str
        :param ApdexLevel: normal/warn/error
注意：此字段可能返回 null，表示取不到有效值。
        :type ApdexLevel: str
        """
        self.Path = None
        self.Method = None
        self.MicroserviceId = None
        self.MicroserviceName = None
        self.RequestCount = None
        self.ErrorRate = None
        self.AvgTimeConsuming = None
        self.MetricDataCurves = None
        self.InstanceId = None
        self.InstanceName = None
        self.GroupId = None
        self.GroupName = None
        self.ClusterType = None
        self.GroupExist = None
        self.InstanceExist = None
        self.ApplicationId = None
        self.MicroserviceType = None
        self.CpuPercent = None
        self.HeapUsed = None
        self.DbName = None
        self.Script = None
        self.DbType = None
        self.Apdex = None
        self.Qps = None
        self.InstanceOnlineCount = None
        self.InstanceTotalCount = None
        self.Status = None
        self.ErrorRateLevel = None
        self.AvgTimeConsumingLevel = None
        self.ApdexLevel = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.MicroserviceId = params.get("MicroserviceId")
        self.MicroserviceName = params.get("MicroserviceName")
        self.RequestCount = params.get("RequestCount")
        self.ErrorRate = params.get("ErrorRate")
        self.AvgTimeConsuming = params.get("AvgTimeConsuming")
        if params.get("MetricDataCurves") is not None:
            self.MetricDataCurves = []
            for item in params.get("MetricDataCurves"):
                obj = MetricDataCurve()
                obj._deserialize(item)
                self.MetricDataCurves.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ClusterType = params.get("ClusterType")
        self.GroupExist = params.get("GroupExist")
        self.InstanceExist = params.get("InstanceExist")
        self.ApplicationId = params.get("ApplicationId")
        self.MicroserviceType = params.get("MicroserviceType")
        self.CpuPercent = params.get("CpuPercent")
        self.HeapUsed = params.get("HeapUsed")
        self.DbName = params.get("DbName")
        self.Script = params.get("Script")
        self.DbType = params.get("DbType")
        self.Apdex = params.get("Apdex")
        self.Qps = params.get("Qps")
        self.InstanceOnlineCount = params.get("InstanceOnlineCount")
        self.InstanceTotalCount = params.get("InstanceTotalCount")
        self.Status = params.get("Status")
        self.ErrorRateLevel = params.get("ErrorRateLevel")
        self.AvgTimeConsumingLevel = params.get("AvgTimeConsumingLevel")
        self.ApdexLevel = params.get("ApdexLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceStatisticsResults(AbstractModel):
    """服务统计结果集

    """

    def __init__(self):
        r"""
        :param Content: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of ServiceStatisticsResult
        :param TotalCount: 条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self.Content = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ServiceStatisticsResult()
                obj._deserialize(item)
                self.Content.append(obj)
        self.TotalCount = params.get("TotalCount")
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
        r"""
        :param ShardKey: 分片参数 KEY，整形, 范围 [1,1000]
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
        r"""
        :param GroupId: 部署组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param GroupId: 部署组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
        :param GroupId: 部署组ID
        :type GroupId: str
        """
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
        r"""
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


class StdoutLogV2(AbstractModel):
    """标准输出日志

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Content: 日志内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param Timestamp: 日志时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param InstanceIp: 实例IP
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIp: str
        """
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
        r"""
        :param GroupId: 部署组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
        :param GroupId: 部署组ID
        :type GroupId: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
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
        r"""
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
        r"""
        :param TaskName: 任务名称
        :type TaskName: str
        :param TaskType: 任务类型
        :type TaskType: str
        :param ExecuteType: 执行类型
        :type ExecuteType: str
        :param TaskContent: 任务内容，长度限制65535字节
        :type TaskContent: str
        :param GroupId: 分组ID
        :type GroupId: str
        :param TimeOut: 超时时间
        :type TimeOut: int
        :param RetryCount: 重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryCount: int
        :param RetryInterval: 重试间隔
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryInterval: int
        :param TaskRule: 触发规则
        :type TaskRule: :class:`tencentcloud.tsf.v20180326.models.TaskRule`
        :param TaskState: 是否启用任务,ENABLED/DISABLED
        :type TaskState: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param SuccessOperator: 判断任务成功的操作符
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessOperator: str
        :param SuccessRatio: 判断任务成功的阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessRatio: int
        :param ShardCount: 分片数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardCount: int
        :param AdvanceSettings: 高级设置
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceSettings: :class:`tencentcloud.tsf.v20180326.models.AdvanceSettings`
        :param ShardArguments: 分片参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardArguments: list of ShardArgument
        :param BelongFlowIds: 所属工作流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BelongFlowIds: list of str
        :param TaskLogId: 任务历史ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskLogId: str
        :param TriggerType: 触发类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: str
        :param TaskArgument: 任务参数，长度限制10000个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskArgument: str
        """
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
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param Content: 任务记录列表
        :type Content: list of TaskRecord
        """
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcrRepoInfo(AbstractModel):
    """tcr仓库信息

    """

    def __init__(self):
        r"""
        :param Region: 地域（填数字）
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param RegistryId: 实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryId: str
        :param RegistryName: 实例名
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryName: str
        :param Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param RepoName: 仓库名
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoName: str
        """
        self.Region = None
        self.RegistryId = None
        self.RegistryName = None
        self.Namespace = None
        self.RepoName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegistryId = params.get("RegistryId")
        self.RegistryName = params.get("RegistryName")
        self.Namespace = params.get("Namespace")
        self.RepoName = params.get("RepoName")
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
        r"""
        :param FlowBatchId: 工作流批次 ID
        :type FlowBatchId: str
        """
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
        r"""
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


class ThreadPicture(AbstractModel):
    """jvm监控数据线程数据封装

    """

    def __init__(self):
        r"""
        :param ThreadCount: 总线程数
        :type ThreadCount: list of CurvePoint
        :param ThreadActive: 活跃线程数
        :type ThreadActive: list of CurvePoint
        :param DeamonThreadCount: 守护线程数
        :type DeamonThreadCount: list of CurvePoint
        """
        self.ThreadCount = None
        self.ThreadActive = None
        self.DeamonThreadCount = None


    def _deserialize(self, params):
        if params.get("ThreadCount") is not None:
            self.ThreadCount = []
            for item in params.get("ThreadCount"):
                obj = CurvePoint()
                obj._deserialize(item)
                self.ThreadCount.append(obj)
        if params.get("ThreadActive") is not None:
            self.ThreadActive = []
            for item in params.get("ThreadActive"):
                obj = CurvePoint()
                obj._deserialize(item)
                self.ThreadActive.append(obj)
        if params.get("DeamonThreadCount") is not None:
            self.DeamonThreadCount = []
            for item in params.get("DeamonThreadCount"):
                obj = CurvePoint()
                obj._deserialize(item)
                self.DeamonThreadCount.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfApiListResponse(AbstractModel):
    """TsfApiListResponse

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfPageApiDetailInfo(AbstractModel):
    """ApiDetailInfo 翻页对象

    """

    def __init__(self):
        r"""
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param Content: API 信息列表
        :type Content: list of ApiDetailInfo
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ApiDetailInfo()
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
        r"""
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
        r"""
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
        r"""
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 业务日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of BusinessLogV2
        :param ScrollId: 游标ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ScrollId: str
        :param Status: 查询状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param TotalCount: 返回个数
        :type TotalCount: int
        :param Content: events 数组
        :type Content: list of ContainerEvent
        """
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
        


class TsfPageDimension(AbstractModel):
    """维度分页

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param Content: 维度
        :type Content: list of str
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Content = params.get("Content")
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
        r"""
        :param TotalCount: 总数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 文件配置数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of FileConfig
        """
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
        r"""
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
        r"""
        :param TotalCount: 记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 记录实体列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of GatewayPlugin
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 标准输出日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of StdoutLogV2
        :param ScrollId: 游标ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ScrollId: str
        :param Status: 查询状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
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
        r"""
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param Content: 记录实体列表
        :type Content: list of UnitNamespace
        """
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
        r"""
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param Content: 记录实体列表
        :type Content: list of UnitRule
        """
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
        r"""
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
        r"""
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
        r"""
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


class UnitNamespace(AbstractModel):
    """微服务网关单元化命名空间

    """

    def __init__(self):
        r"""
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param NamespaceName: 命名空间Name
        :type NamespaceName: str
        :param Id: 单元化命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        """
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
        r"""
        :param Name: 规则名称
        :type Name: str
        :param Id: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param GatewayInstanceId: 网关实体ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayInstanceId: str
        :param Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Status: 使用状态：enabled/disabled
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param UnitRuleItemList: 规则项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitRuleItemList: list of UnitRuleItem
        """
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
        r"""
        :param Relationship: 逻辑关系：AND/OR
        :type Relationship: str
        :param DestNamespaceId: 目的地命名空间ID
        :type DestNamespaceId: str
        :param DestNamespaceName: 目的地命名空间名称
        :type DestNamespaceName: str
        :param Name: 规则项名称
        :type Name: str
        :param Id: 规则项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param UnitRuleId: 单元化规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitRuleId: str
        :param Priority: 规则顺序，越小优先级越高：默认为0
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param UnitRuleTagList: 规则标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitRuleTagList: list of UnitRuleTag
        """
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
        r"""
        :param TagType: 标签类型 : U(用户标签)
        :type TagType: str
        :param TagField: 标签名
        :type TagField: str
        :param TagOperator: 操作符:IN/NOT_IN/EQUAL/NOT_EQUAL/REGEX
        :type TagOperator: str
        :param TagValue: 标签值
        :type TagValue: str
        :param UnitRuleItemId: 单元化规则项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitRuleItemId: str
        :param Id: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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


class UpdateApiTimeoutsRequest(AbstractModel):
    """UpdateApiTimeouts请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiIds: API ID 列表
        :type ApiIds: list of str
        :param UsableStatus: 开启/禁用，enabled/disabled
        :type UsableStatus: str
        :param Timeout: 超时时间，单位毫秒，开启API超时时，必填
        :type Timeout: int
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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


class UpdateUnitRuleRequest(AbstractModel):
    """UpdateUnitRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 规则ID
        :type Id: str
        :param Name: 规则名称
        :type Name: str
        :param Description: 规则描述
        :type Description: str
        :param UnitRuleItemList: 规则项列表
        :type UnitRuleItemList: list of UnitRuleItem
        """
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
        r"""
        :param Result: 是否成功
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


class ValueFrom(AbstractModel):
    """k8s env 的 ValueFrom

    """

    def __init__(self):
        r"""
        :param FieldRef: k8s env 的 FieldRef
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldRef: :class:`tencentcloud.tsf.v20180326.models.FieldRef`
        :param ResourceFieldRef: k8s env 的 ResourceFieldRef
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceFieldRef: :class:`tencentcloud.tsf.v20180326.models.ResourceFieldRef`
        """
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
        r"""
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
        :param PackageType: 程序包类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param StartScript: 启动脚本 base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type StartScript: str
        :param StopScript: 停止脚本 base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type StopScript: str
        :param Alias: 部署组备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
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
        


class VmGroupOther(AbstractModel):
    """虚拟机部署组其他字段

    """

    def __init__(self):
        r"""
        :param GroupId: 部署组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param PackageId: 程序包ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param PackageName: 程序包名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param PackageVersion: 程序包版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param InstanceCount: 部署组实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param RunInstanceCount: 部署组运行中实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type RunInstanceCount: int
        :param OffInstanceCount: 部署组中停止实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type OffInstanceCount: int
        :param GroupStatus: 部署组状态
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupStatus: str
        :param IsNotEqualServiceConfig: 服务配置信息是否匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNotEqualServiceConfig: bool
        """
        self.GroupId = None
        self.PackageId = None
        self.PackageName = None
        self.PackageVersion = None
        self.InstanceCount = None
        self.RunInstanceCount = None
        self.OffInstanceCount = None
        self.GroupStatus = None
        self.IsNotEqualServiceConfig = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PackageId = params.get("PackageId")
        self.PackageName = params.get("PackageName")
        self.PackageVersion = params.get("PackageVersion")
        self.InstanceCount = params.get("InstanceCount")
        self.RunInstanceCount = params.get("RunInstanceCount")
        self.OffInstanceCount = params.get("OffInstanceCount")
        self.GroupStatus = params.get("GroupStatus")
        self.IsNotEqualServiceConfig = params.get("IsNotEqualServiceConfig")
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
        r"""
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
        :param Alias: 部署组备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
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
        


class VolumeInfo(AbstractModel):
    """容器卷挂载信息

    """

    def __init__(self):
        r"""
        :param VolumeType: 数据卷类型
        :type VolumeType: str
        :param VolumeName: 数据卷名称
        :type VolumeName: str
        :param VolumeConfig: 数据卷配置
        :type VolumeConfig: str
        """
        self.VolumeType = None
        self.VolumeName = None
        self.VolumeConfig = None


    def _deserialize(self, params):
        self.VolumeType = params.get("VolumeType")
        self.VolumeName = params.get("VolumeName")
        self.VolumeConfig = params.get("VolumeConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeMountInfo(AbstractModel):
    """容器卷挂载点信息

    """

    def __init__(self):
        r"""
        :param VolumeMountName: 挂载数据卷名称
        :type VolumeMountName: str
        :param VolumeMountPath: 挂载路径
        :type VolumeMountPath: str
        :param VolumeMountSubPath: 挂载子路径
        :type VolumeMountSubPath: str
        :param ReadOrWrite: 读写，1：读 2：读写
        :type ReadOrWrite: str
        """
        self.VolumeMountName = None
        self.VolumeMountPath = None
        self.VolumeMountSubPath = None
        self.ReadOrWrite = None


    def _deserialize(self, params):
        self.VolumeMountName = params.get("VolumeMountName")
        self.VolumeMountPath = params.get("VolumeMountPath")
        self.VolumeMountSubPath = params.get("VolumeMountSubPath")
        self.ReadOrWrite = params.get("ReadOrWrite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        