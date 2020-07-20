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


class AutoDelStrategyInfo(AbstractModel):
    """自动删除策略信息

    """

    def __init__(self):
        """
        :param Username: 用户名
        :type Username: str
        :param RepoName: 仓库名
        :type RepoName: str
        :param Type: 类型
        :type Type: str
        :param Value: 策略值
        :type Value: int
        :param Valid: Valid
        :type Valid: int
        :param CreationTime: 创建时间
        :type CreationTime: str
        """
        self.Username = None
        self.RepoName = None
        self.Type = None
        self.Value = None
        self.Valid = None
        self.CreationTime = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.RepoName = params.get("RepoName")
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        self.Valid = params.get("Valid")
        self.CreationTime = params.get("CreationTime")


class AutoDelStrategyInfoResp(AbstractModel):
    """获取自动删除策略

    """

    def __init__(self):
        """
        :param TotalCount: 总数目
        :type TotalCount: int
        :param StrategyInfo: 自动删除策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyInfo: list of AutoDelStrategyInfo
        """
        self.TotalCount = None
        self.StrategyInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("StrategyInfo") is not None:
            self.StrategyInfo = []
            for item in params.get("StrategyInfo"):
                obj = AutoDelStrategyInfo()
                obj._deserialize(item)
                self.StrategyInfo.append(obj)


class BatchDeleteImagePersonalRequest(AbstractModel):
    """BatchDeleteImagePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Tags: Tag列表
        :type Tags: list of str
        """
        self.RepoName = None
        self.Tags = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Tags = params.get("Tags")


class BatchDeleteImagePersonalResponse(AbstractModel):
    """BatchDeleteImagePersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchDeleteRepositoryPersonalRequest(AbstractModel):
    """BatchDeleteRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoNames: 仓库名称数组
        :type RepoNames: list of str
        """
        self.RepoNames = None


    def _deserialize(self, params):
        self.RepoNames = params.get("RepoNames")


class BatchDeleteRepositoryPersonalResponse(AbstractModel):
    """BatchDeleteRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateApplicationTriggerPersonalRequest(AbstractModel):
    """CreateApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 触发器关联的镜像仓库，library/test格式
        :type RepoName: str
        :param TriggerName: 触发器名称
        :type TriggerName: str
        :param InvokeMethod: 触发方式，"all"全部触发，"taglist"指定tag触发，"regex"正则触发
        :type InvokeMethod: str
        :param ClusterId: 应用所在TKE集群ID
        :type ClusterId: str
        :param Namespace: 应用所在TKE集群命名空间
        :type Namespace: str
        :param WorkloadType: 应用所在TKE集群工作负载类型,支持Deployment、StatefulSet、DaemonSet、CronJob、Job。
        :type WorkloadType: str
        :param WorkloadName: 应用所在TKE集群工作负载名称
        :type WorkloadName: str
        :param ContainerName: 应用所在TKE集群工作负载下容器名称
        :type ContainerName: str
        :param ClusterRegion: 应用所在TKE集群地域
        :type ClusterRegion: int
        :param InvokeExpr: 触发方式对应的表达式
        :type InvokeExpr: str
        """
        self.RepoName = None
        self.TriggerName = None
        self.InvokeMethod = None
        self.ClusterId = None
        self.Namespace = None
        self.WorkloadType = None
        self.WorkloadName = None
        self.ContainerName = None
        self.ClusterRegion = None
        self.InvokeExpr = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TriggerName = params.get("TriggerName")
        self.InvokeMethod = params.get("InvokeMethod")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.WorkloadType = params.get("WorkloadType")
        self.WorkloadName = params.get("WorkloadName")
        self.ContainerName = params.get("ContainerName")
        self.ClusterRegion = params.get("ClusterRegion")
        self.InvokeExpr = params.get("InvokeExpr")


class CreateApplicationTriggerPersonalResponse(AbstractModel):
    """CreateApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateImageLifecyclePersonalRequest(AbstractModel):
    """CreateImageLifecyclePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Type: keep_last_days:保留最近几天的数据;keep_last_nums:保留最近多少个
        :type Type: str
        :param Val: 策略值
        :type Val: int
        """
        self.RepoName = None
        self.Type = None
        self.Val = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Type = params.get("Type")
        self.Val = params.get("Val")


class CreateImageLifecyclePersonalResponse(AbstractModel):
    """CreateImageLifecyclePersonal返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param RegistryName: 企业版实例名称
        :type RegistryName: str
        :param RegistryType: 企业版实例类型
        :type RegistryType: str
        """
        self.RegistryName = None
        self.RegistryType = None


    def _deserialize(self, params):
        self.RegistryName = params.get("RegistryName")
        self.RegistryType = params.get("RegistryType")


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 企业版实例Id
        :type RegistryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateInstanceTokenRequest(AbstractModel):
    """CreateInstanceToken请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param TokenType: 访问凭证类型，longterm 为长期访问凭证，temp 为临时访问凭证，默认是临时访问凭证，有效期1小时
        :type TokenType: str
        :param Desc: 长期访问凭证描述信息
        :type Desc: str
        """
        self.RegistryId = None
        self.TokenType = None
        self.Desc = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.TokenType = params.get("TokenType")
        self.Desc = params.get("Desc")


class CreateInstanceTokenResponse(AbstractModel):
    """CreateInstanceToken返回参数结构体

    """

    def __init__(self):
        """
        :param Username: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Username: str
        :param Token: 访问凭证
        :type Token: str
        :param ExpTime: 访问凭证过期时间戳
        :type ExpTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Username = None
        self.Token = None
        self.ExpTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.Token = params.get("Token")
        self.ExpTime = params.get("ExpTime")
        self.RequestId = params.get("RequestId")


class CreateNamespacePersonalRequest(AbstractModel):
    """CreateNamespacePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间名称
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")


class CreateNamespacePersonalResponse(AbstractModel):
    """CreateNamespacePersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间的名称
        :type NamespaceName: str
        :param IsPublic: 是否公开，true为公开，fale为私有
        :type IsPublic: bool
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.IsPublic = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.IsPublic = params.get("IsPublic")


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRepositoryPersonalRequest(AbstractModel):
    """CreateRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Public: 是否公共,1:公共,0:私有
        :type Public: int
        :param Description: 仓库描述
        :type Description: str
        """
        self.RepoName = None
        self.Public = None
        self.Description = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Public = params.get("Public")
        self.Description = params.get("Description")


class CreateRepositoryPersonalResponse(AbstractModel):
    """CreateRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRepositoryRequest(AbstractModel):
    """CreateRepository请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param RepositoryName: 仓库名称
        :type RepositoryName: str
        :param BriefDescription: 仓库简短描述
        :type BriefDescription: str
        :param Description: 仓库详细描述
        :type Description: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.BriefDescription = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.BriefDescription = params.get("BriefDescription")
        self.Description = params.get("Description")


class CreateRepositoryResponse(AbstractModel):
    """CreateRepository返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUserPersonalRequest(AbstractModel):
    """CreateUserPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Password: 用户密码
        :type Password: str
        """
        self.Password = None


    def _deserialize(self, params):
        self.Password = params.get("Password")


class CreateUserPersonalResponse(AbstractModel):
    """CreateUserPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWebhookTriggerRequest(AbstractModel):
    """CreateWebhookTrigger请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例 Id
        :type RegistryId: str
        :param Trigger: 触发器参数
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.RegistryId = None
        self.Trigger = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.Namespace = params.get("Namespace")


class CreateWebhookTriggerResponse(AbstractModel):
    """CreateWebhookTrigger返回参数结构体

    """

    def __init__(self):
        """
        :param Trigger: 新建的触发器
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Trigger = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.RequestId = params.get("RequestId")


class DeleteApplicationTriggerPersonalRequest(AbstractModel):
    """DeleteApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param TriggerName: 触发器名称
        :type TriggerName: str
        """
        self.TriggerName = None


    def _deserialize(self, params):
        self.TriggerName = params.get("TriggerName")


class DeleteApplicationTriggerPersonalResponse(AbstractModel):
    """DeleteApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageLifecycleGlobalPersonalRequest(AbstractModel):
    """DeleteImageLifecycleGlobalPersonal请求参数结构体

    """


class DeleteImageLifecycleGlobalPersonalResponse(AbstractModel):
    """DeleteImageLifecycleGlobalPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageLifecyclePersonalRequest(AbstractModel):
    """DeleteImageLifecyclePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")


class DeleteImageLifecyclePersonalResponse(AbstractModel):
    """DeleteImageLifecyclePersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImagePersonalRequest(AbstractModel):
    """DeleteImagePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Tag: Tag名
        :type Tag: str
        """
        self.RepoName = None
        self.Tag = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Tag = params.get("Tag")


class DeleteImagePersonalResponse(AbstractModel):
    """DeleteImagePersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceTokenRequest(AbstractModel):
    """DeleteInstanceToken请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例 ID
        :type RegistryId: str
        :param TokenId: 访问凭证 ID
        :type TokenId: str
        """
        self.RegistryId = None
        self.TokenId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.TokenId = params.get("TokenId")


class DeleteInstanceTokenResponse(AbstractModel):
    """DeleteInstanceToken返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespacePersonalRequest(AbstractModel):
    """DeleteNamespacePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间名称
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")


class DeleteNamespacePersonalResponse(AbstractModel):
    """DeleteNamespacePersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间的名称
        :type NamespaceName: str
        """
        self.RegistryId = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryPersonalRequest(AbstractModel):
    """DeleteRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")


class DeleteRepositoryPersonalResponse(AbstractModel):
    """DeleteRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryRequest(AbstractModel):
    """DeleteRepository请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param NamespaceName: 命名空间的名称
        :type NamespaceName: str
        :param RepositoryName: 仓库名称的名称
        :type RepositoryName: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")


class DeleteRepositoryResponse(AbstractModel):
    """DeleteRepository返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWebhookTriggerRequest(AbstractModel):
    """DeleteWebhookTrigger请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Id: 触发器 Id
        :type Id: int
        """
        self.RegistryId = None
        self.Namespace = None
        self.Id = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Namespace = params.get("Namespace")
        self.Id = params.get("Id")


class DeleteWebhookTriggerResponse(AbstractModel):
    """DeleteWebhookTrigger返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeApplicationTriggerLogPersonalRequest(AbstractModel):
    """DescribeApplicationTriggerLogPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        :param Order: 升序或降序
        :type Order: str
        :param OrderBy: 按某列排序
        :type OrderBy: str
        """
        self.RepoName = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderBy = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")


class DescribeApplicationTriggerLogPersonalResp(AbstractModel):
    """查询应用更新触发器触发日志返回值

    """

    def __init__(self):
        """
        :param TotalCount: 返回总数
        :type TotalCount: int
        :param LogInfo: 触发日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogInfo: list of TriggerLogResp
        """
        self.TotalCount = None
        self.LogInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LogInfo") is not None:
            self.LogInfo = []
            for item in params.get("LogInfo"):
                obj = TriggerLogResp()
                obj._deserialize(item)
                self.LogInfo.append(obj)


class DescribeApplicationTriggerLogPersonalResponse(AbstractModel):
    """DescribeApplicationTriggerLogPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 触发日志返回值
        :type Data: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerLogPersonalResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeApplicationTriggerLogPersonalResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationTriggerPersonalRequest(AbstractModel):
    """DescribeApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param TriggerName: 触发器名称
        :type TriggerName: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        """
        self.RepoName = None
        self.TriggerName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TriggerName = params.get("TriggerName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeApplicationTriggerPersonalResp(AbstractModel):
    """拉取触发器列表返回值

    """

    def __init__(self):
        """
        :param TotalCount: 返回条目总数
        :type TotalCount: int
        :param TriggerInfo: 触发器列表
        :type TriggerInfo: list of TriggerResp
        """
        self.TotalCount = None
        self.TriggerInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TriggerInfo") is not None:
            self.TriggerInfo = []
            for item in params.get("TriggerInfo"):
                obj = TriggerResp()
                obj._deserialize(item)
                self.TriggerInfo.append(obj)


class DescribeApplicationTriggerPersonalResponse(AbstractModel):
    """DescribeApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 触发器列表返回值
        :type Data: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerPersonalResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeApplicationTriggerPersonalResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeFavorRepositoryPersonalRequest(AbstractModel):
    """DescribeFavorRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Limit: 分页Limit
        :type Limit: int
        :param Offset: Offset用于分页
        :type Offset: int
        """
        self.RepoName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeFavorRepositoryPersonalResponse(AbstractModel):
    """DescribeFavorRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 个人收藏仓库列表返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.FavorResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = FavorResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageFilterPersonalRequest(AbstractModel):
    """DescribeImageFilterPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Tag: Tag名
        :type Tag: str
        """
        self.RepoName = None
        self.Tag = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Tag = params.get("Tag")


class DescribeImageFilterPersonalResponse(AbstractModel):
    """DescribeImageFilterPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: payload
        :type Data: :class:`tencentcloud.tcr.v20190924.models.SameImagesResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SameImagesResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageLifecycleGlobalPersonalRequest(AbstractModel):
    """DescribeImageLifecycleGlobalPersonal请求参数结构体

    """


class DescribeImageLifecycleGlobalPersonalResponse(AbstractModel):
    """DescribeImageLifecycleGlobalPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 全局自动删除策略信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.AutoDelStrategyInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AutoDelStrategyInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageLifecyclePersonalRequest(AbstractModel):
    """DescribeImageLifecyclePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")


class DescribeImageLifecyclePersonalResponse(AbstractModel):
    """DescribeImageLifecyclePersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 自动删除策略信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.AutoDelStrategyInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AutoDelStrategyInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageManifestsRequest(AbstractModel):
    """DescribeImageManifests请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param ImageVersion: 镜像版本
        :type ImageVersion: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")


class DescribeImageManifestsResponse(AbstractModel):
    """DescribeImageManifests返回参数结构体

    """

    def __init__(self):
        """
        :param Manifest: 镜像的Manifest信息
        :type Manifest: str
        :param Config: 镜像的配置信息
        :type Config: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Manifest = None
        self.Config = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Manifest = params.get("Manifest")
        self.Config = params.get("Config")
        self.RequestId = params.get("RequestId")


class DescribeImagePersonalRequest(AbstractModel):
    """DescribeImagePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        :param Tag: tag名称，可根据输入搜索
        :type Tag: str
        """
        self.RepoName = None
        self.Offset = None
        self.Limit = None
        self.Tag = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Tag = params.get("Tag")


class DescribeImagePersonalResponse(AbstractModel):
    """DescribeImagePersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 镜像tag信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.TagInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TagInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param ImageVersion: 指定镜像版本(Tag)，不填默认返回仓库内全部容器镜像
        :type ImageVersion: str
        :param Limit: 每页个数，用于分页，默认20
        :type Limit: int
        :param Offset: 页数，默认值为1
        :type Offset: int
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        """
        :param ImageInfoList: 容器镜像信息列表
        :type ImageInfoList: list of TcrImageInfo
        :param TotalCount: 容器镜像总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageInfoList") is not None:
            self.ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = TcrImageInfo()
                obj._deserialize(item)
                self.ImageInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstanceStatusRequest(AbstractModel):
    """DescribeInstanceStatus请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryIds: 实例ID的数组
        :type RegistryIds: list of str
        """
        self.RegistryIds = None


    def _deserialize(self, params):
        self.RegistryIds = params.get("RegistryIds")


class DescribeInstanceStatusResponse(AbstractModel):
    """DescribeInstanceStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RegistryStatusSet: 实例的状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryStatusSet: list of RegistryStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegistryStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegistryStatusSet") is not None:
            self.RegistryStatusSet = []
            for item in params.get("RegistryStatusSet"):
                obj = RegistryStatus()
                obj._deserialize(item)
                self.RegistryStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTokenRequest(AbstractModel):
    """DescribeInstanceToken请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例 ID
        :type RegistryId: str
        :param Limit: 分页单页数量
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        """
        self.RegistryId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeInstanceTokenResponse(AbstractModel):
    """DescribeInstanceToken返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 长期访问凭证总数
        :type TotalCount: int
        :param Tokens: 长期访问凭证列表
        :type Tokens: list of TcrInstanceToken
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tokens = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tokens") is not None:
            self.Tokens = []
            for item in params.get("Tokens"):
                obj = TcrInstanceToken()
                obj._deserialize(item)
                self.Tokens.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Registryids: 实例ID列表(为空时，
表示获取账号下所有实例)
        :type Registryids: list of str
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param AllRegion: 获取所有地域的实例，默认为False
        :type AllRegion: bool
        """
        self.Registryids = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.AllRegion = None


    def _deserialize(self, params):
        self.Registryids = params.get("Registryids")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.AllRegion = params.get("AllRegion")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总实例个数
        :type TotalCount: int
        :param Registries: 实例信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Registries: list of Registry
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Registries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Registries") is not None:
            self.Registries = []
            for item in params.get("Registries"):
                obj = Registry()
                obj._deserialize(item)
                self.Registries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNamespacePersonalRequest(AbstractModel):
    """DescribeNamespacePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间，支持模糊查询
        :type Namespace: str
        :param Limit: 单页数量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.Namespace = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeNamespacePersonalResponse(AbstractModel):
    """DescribeNamespacePersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 用户命名空间返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.NamespaceInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = NamespaceInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param NamespaceName: 指定命名空间，不填写默认查询所有命名空间
        :type NamespaceName: str
        :param Limit: 每页个数
        :type Limit: int
        :param Offset: 页偏移
        :type Offset: int
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces返回参数结构体

    """

    def __init__(self):
        """
        :param NamespaceList: 命名空间列表信息
        :type NamespaceList: list of TcrNamespaceInfo
        :param TotalCount: 总个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NamespaceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NamespaceList") is not None:
            self.NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = TcrNamespaceInfo()
                obj._deserialize(item)
                self.NamespaceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRepositoriesRequest(AbstractModel):
    """DescribeRepositories请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param NamespaceName: 指定命名空间，不填写默认为查询所有命名空间下镜像仓库
        :type NamespaceName: str
        :param RepositoryName: 指定镜像仓库，不填写默认查询指定命名空间下所有镜像仓库
        :type RepositoryName: str
        :param Offset: 页数，用于分页
        :type Offset: int
        :param Limit: 每页个数，用于分页
        :type Limit: int
        :param SortBy: 基于字段排序，支持的值有-creation_time,-name, -update_time
        :type SortBy: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.Offset = None
        self.Limit = None
        self.SortBy = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")


class DescribeRepositoriesResponse(AbstractModel):
    """DescribeRepositories返回参数结构体

    """

    def __init__(self):
        """
        :param RepositoryList: 仓库信息列表
        :type RepositoryList: list of TcrRepositoryInfo
        :param TotalCount: 总个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RepositoryList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RepositoryList") is not None:
            self.RepositoryList = []
            for item in params.get("RepositoryList"):
                obj = TcrRepositoryInfo()
                obj._deserialize(item)
                self.RepositoryList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRepositoryFilterPersonalRequest(AbstractModel):
    """DescribeRepositoryFilterPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 搜索镜像名
        :type RepoName: str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回最大数量，默认 20，最大100
        :type Limit: int
        :param Public: 筛选条件：1表示public，0表示private
        :type Public: int
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.RepoName = None
        self.Offset = None
        self.Limit = None
        self.Public = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Public = params.get("Public")
        self.Namespace = params.get("Namespace")


class DescribeRepositoryFilterPersonalResponse(AbstractModel):
    """DescribeRepositoryFilterPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 仓库信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.SearchUserRepositoryResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SearchUserRepositoryResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRepositoryOwnerPersonalRequest(AbstractModel):
    """DescribeRepositoryOwnerPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回最大数量，默认 20, 最大值 100
        :type Limit: int
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.Offset = None
        self.Limit = None
        self.RepoName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.RepoName = params.get("RepoName")


class DescribeRepositoryOwnerPersonalResponse(AbstractModel):
    """DescribeRepositoryOwnerPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 仓库信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepoInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RepoInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRepositoryPersonalRequest(AbstractModel):
    """DescribeRepositoryPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名字
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")


class DescribeRepositoryPersonalResponse(AbstractModel):
    """DescribeRepositoryPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 仓库信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepositoryInfoResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RepositoryInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeUserQuotaPersonalRequest(AbstractModel):
    """DescribeUserQuotaPersonal请求参数结构体

    """


class DescribeUserQuotaPersonalResponse(AbstractModel):
    """DescribeUserQuotaPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 配额返回信息
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RespLimit`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RespLimit()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeWebhookTriggerLogRequest(AbstractModel):
    """DescribeWebhookTriggerLog请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例 Id
        :type RegistryId: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Id: 触发器 Id
        :type Id: int
        :param Limit: 分页单页数量
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        """
        self.RegistryId = None
        self.Namespace = None
        self.Id = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Namespace = params.get("Namespace")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWebhookTriggerLogResponse(AbstractModel):
    """DescribeWebhookTriggerLog返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param Logs: 日志列表
        :type Logs: list of WebhookTriggerLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Logs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Logs") is not None:
            self.Logs = []
            for item in params.get("Logs"):
                obj = WebhookTriggerLog()
                obj._deserialize(item)
                self.Logs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWebhookTriggerRequest(AbstractModel):
    """DescribeWebhookTrigger请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param Limit: 分页单页数量
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.RegistryId = None
        self.Limit = None
        self.Offset = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Namespace = params.get("Namespace")


class DescribeWebhookTriggerResponse(AbstractModel):
    """DescribeWebhookTrigger返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 触发器总数
        :type TotalCount: int
        :param Triggers: 触发器列表
        :type Triggers: list of WebhookTrigger
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Triggers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Triggers") is not None:
            self.Triggers = []
            for item in params.get("Triggers"):
                obj = WebhookTrigger()
                obj._deserialize(item)
                self.Triggers.append(obj)
        self.RequestId = params.get("RequestId")


class DupImageTagResp(AbstractModel):
    """复制镜像tag返回值

    """

    def __init__(self):
        """
        :param Digest: 镜像Digest值
        :type Digest: str
        """
        self.Digest = None


    def _deserialize(self, params):
        self.Digest = params.get("Digest")


class DuplicateImagePersonalRequest(AbstractModel):
    """DuplicateImagePersonal请求参数结构体

    """

    def __init__(self):
        """
        :param SrcImage: 源镜像名称，不包含domain。例如： tencentyun/foo:v1
        :type SrcImage: str
        :param DestImage: 目的镜像名称，不包含domain。例如： tencentyun/foo:latest
        :type DestImage: str
        """
        self.SrcImage = None
        self.DestImage = None


    def _deserialize(self, params):
        self.SrcImage = params.get("SrcImage")
        self.DestImage = params.get("DestImage")


class DuplicateImagePersonalResponse(AbstractModel):
    """DuplicateImagePersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 复制镜像返回值
        :type Data: :class:`tencentcloud.tcr.v20190924.models.DupImageTagResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DupImageTagResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class FavorResp(AbstractModel):
    """用于获取收藏仓库的响应

    """

    def __init__(self):
        """
        :param TotalCount: 收藏仓库的总数
        :type TotalCount: int
        :param RepoInfo: 仓库信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoInfo: list of Favors
        """
        self.TotalCount = None
        self.RepoInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self.RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = Favors()
                obj._deserialize(item)
                self.RepoInfo.append(obj)


class Favors(AbstractModel):
    """仓库收藏

    """

    def __init__(self):
        """
        :param RepoName: 仓库名字
        :type RepoName: str
        :param RepoType: 仓库类型
        :type RepoType: str
        :param PullCount: Pull总共的次数
注意：此字段可能返回 null，表示取不到有效值。
        :type PullCount: int
        :param FavorCount: 仓库收藏次数
注意：此字段可能返回 null，表示取不到有效值。
        :type FavorCount: int
        :param Public: 仓库是否公开
注意：此字段可能返回 null，表示取不到有效值。
        :type Public: int
        :param IsQcloudOfficial: 是否为官方所有
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQcloudOfficial: bool
        :param TagCount: 仓库Tag的数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TagCount: int
        :param Logo: Logo
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: str
        :param Region: 地域
        :type Region: str
        :param RegionId: 地域的Id
        :type RegionId: int
        """
        self.RepoName = None
        self.RepoType = None
        self.PullCount = None
        self.FavorCount = None
        self.Public = None
        self.IsQcloudOfficial = None
        self.TagCount = None
        self.Logo = None
        self.Region = None
        self.RegionId = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.RepoType = params.get("RepoType")
        self.PullCount = params.get("PullCount")
        self.FavorCount = params.get("FavorCount")
        self.Public = params.get("Public")
        self.IsQcloudOfficial = params.get("IsQcloudOfficial")
        self.TagCount = params.get("TagCount")
        self.Logo = params.get("Logo")
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        """
        :param Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Name: str
        :param Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Header(AbstractModel):
    """Header KV

    """

    def __init__(self):
        """
        :param Key: Header Key
        :type Key: str
        :param Values: Header Values
        :type Values: list of str
        """
        self.Key = None
        self.Values = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Values = params.get("Values")


class Limit(AbstractModel):
    """共享镜像仓库用户配额

    """

    def __init__(self):
        """
        :param Username: 用户名
        :type Username: str
        :param Type: 配额的类型
        :type Type: str
        :param Value: 配置的值
        :type Value: int
        """
        self.Username = None
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.Type = params.get("Type")
        self.Value = params.get("Value")


class ManageImageLifecycleGlobalPersonalRequest(AbstractModel):
    """ManageImageLifecycleGlobalPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Type: global_keep_last_days:全局保留最近几天的数据;global_keep_last_nums:全局保留最近多少个
        :type Type: str
        :param Val: 策略值
        :type Val: int
        """
        self.Type = None
        self.Val = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Val = params.get("Val")


class ManageImageLifecycleGlobalPersonalResponse(AbstractModel):
    """ManageImageLifecycleGlobalPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationTriggerPersonalRequest(AbstractModel):
    """ModifyApplicationTriggerPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 触发器关联的镜像仓库，library/test格式
        :type RepoName: str
        :param TriggerName: 触发器名称
        :type TriggerName: str
        :param InvokeMethod: 触发方式，"all"全部触发，"taglist"指定tag触发，"regex"正则触发
        :type InvokeMethod: str
        :param InvokeExpr: 触发方式对应的表达式
        :type InvokeExpr: str
        :param ClusterId: 应用所在TKE集群ID
        :type ClusterId: str
        :param Namespace: 应用所在TKE集群命名空间
        :type Namespace: str
        :param WorkloadType: 应用所在TKE集群工作负载类型,支持Deployment、StatefulSet、DaemonSet、CronJob、Job。
        :type WorkloadType: str
        :param WorkloadName: 应用所在TKE集群工作负载名称
        :type WorkloadName: str
        :param ContainerName: 应用所在TKE集群工作负载下容器名称
        :type ContainerName: str
        :param ClusterRegion: 应用所在TKE集群地域数字ID，如1（广州）、16（成都）
        :type ClusterRegion: int
        :param NewTriggerName: 新触发器名称
        :type NewTriggerName: str
        """
        self.RepoName = None
        self.TriggerName = None
        self.InvokeMethod = None
        self.InvokeExpr = None
        self.ClusterId = None
        self.Namespace = None
        self.WorkloadType = None
        self.WorkloadName = None
        self.ContainerName = None
        self.ClusterRegion = None
        self.NewTriggerName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TriggerName = params.get("TriggerName")
        self.InvokeMethod = params.get("InvokeMethod")
        self.InvokeExpr = params.get("InvokeExpr")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.WorkloadType = params.get("WorkloadType")
        self.WorkloadName = params.get("WorkloadName")
        self.ContainerName = params.get("ContainerName")
        self.ClusterRegion = params.get("ClusterRegion")
        self.NewTriggerName = params.get("NewTriggerName")


class ModifyApplicationTriggerPersonalResponse(AbstractModel):
    """ModifyApplicationTriggerPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceTokenRequest(AbstractModel):
    """ModifyInstanceToken请求参数结构体

    """

    def __init__(self):
        """
        :param TokenId: 实例长期访问凭证 ID
        :type TokenId: str
        :param Enable: 启用或禁用实例长期访问凭证
        :type Enable: bool
        :param RegistryId: 实例 ID
        :type RegistryId: str
        """
        self.TokenId = None
        self.Enable = None
        self.RegistryId = None


    def _deserialize(self, params):
        self.TokenId = params.get("TokenId")
        self.Enable = params.get("Enable")
        self.RegistryId = params.get("RegistryId")


class ModifyInstanceTokenResponse(AbstractModel):
    """ModifyInstanceToken返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param IsPublic: 访问级别，True为公开，False为私有
        :type IsPublic: bool
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.IsPublic = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.IsPublic = params.get("IsPublic")


class ModifyNamespaceResponse(AbstractModel):
    """ModifyNamespace返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryAccessPersonalRequest(AbstractModel):
    """ModifyRepositoryAccessPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Public: 默认值为0
        :type Public: int
        """
        self.RepoName = None
        self.Public = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Public = params.get("Public")


class ModifyRepositoryAccessPersonalResponse(AbstractModel):
    """ModifyRepositoryAccessPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryInfoPersonalRequest(AbstractModel):
    """ModifyRepositoryInfoPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param Description: 仓库描述
        :type Description: str
        """
        self.RepoName = None
        self.Description = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Description = params.get("Description")


class ModifyRepositoryInfoPersonalResponse(AbstractModel):
    """ModifyRepositoryInfoPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryRequest(AbstractModel):
    """ModifyRepository请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param RepositoryName: 镜像仓库名称
        :type RepositoryName: str
        :param BriefDescription: 仓库简短描述
        :type BriefDescription: str
        :param Description: 仓库详细描述
        :type Description: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.BriefDescription = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.BriefDescription = params.get("BriefDescription")
        self.Description = params.get("Description")


class ModifyRepositoryResponse(AbstractModel):
    """ModifyRepository返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserPasswordPersonalRequest(AbstractModel):
    """ModifyUserPasswordPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Password: 更新后的密码
        :type Password: str
        """
        self.Password = None


    def _deserialize(self, params):
        self.Password = params.get("Password")


class ModifyUserPasswordPersonalResponse(AbstractModel):
    """ModifyUserPasswordPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWebhookTriggerRequest(AbstractModel):
    """ModifyWebhookTrigger请求参数结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例Id
        :type RegistryId: str
        :param Trigger: 触发器参数
        :type Trigger: :class:`tencentcloud.tcr.v20190924.models.WebhookTrigger`
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.RegistryId = None
        self.Trigger = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.Namespace = params.get("Namespace")


class ModifyWebhookTriggerResponse(AbstractModel):
    """ModifyWebhookTrigger返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NamespaceInfo(AbstractModel):
    """命名空间信息

    """

    def __init__(self):
        """
        :param Namespace: 命名空间
        :type Namespace: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param RepoCount: 命名空间下仓库数量
        :type RepoCount: int
        """
        self.Namespace = None
        self.CreationTime = None
        self.RepoCount = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.CreationTime = params.get("CreationTime")
        self.RepoCount = params.get("RepoCount")


class NamespaceInfoResp(AbstractModel):
    """获取命名空间信息返回

    """

    def __init__(self):
        """
        :param NamespaceCount: 命名空间数量
        :type NamespaceCount: int
        :param NamespaceInfo: 命名空间信息
        :type NamespaceInfo: list of NamespaceInfo
        """
        self.NamespaceCount = None
        self.NamespaceInfo = None


    def _deserialize(self, params):
        self.NamespaceCount = params.get("NamespaceCount")
        if params.get("NamespaceInfo") is not None:
            self.NamespaceInfo = []
            for item in params.get("NamespaceInfo"):
                obj = NamespaceInfo()
                obj._deserialize(item)
                self.NamespaceInfo.append(obj)


class NamespaceIsExistsResp(AbstractModel):
    """NamespaceIsExists返回类型

    """

    def __init__(self):
        """
        :param IsExist: 命名空间是否存在
        :type IsExist: bool
        :param IsPreserved: 是否为保留命名空间
        :type IsPreserved: bool
        """
        self.IsExist = None
        self.IsPreserved = None


    def _deserialize(self, params):
        self.IsExist = params.get("IsExist")
        self.IsPreserved = params.get("IsPreserved")


class Registry(AbstractModel):
    """实例信息结构体

    """

    def __init__(self):
        """
        :param RegistryId: 实例ID
        :type RegistryId: str
        :param RegistryName: 实例名称
        :type RegistryName: str
        :param RegistryType: 实例规格
        :type RegistryType: str
        :param Status: 实例状态
        :type Status: str
        :param PublicDomain: 实例的公共访问地址
        :type PublicDomain: str
        :param CreatedAt: 实例创建时间
        :type CreatedAt: str
        :param RegionName: 地域名称
        :type RegionName: str
        :param RegionId: 地域Id
        :type RegionId: int
        :param EnableAnonymous: 是否支持匿名
        :type EnableAnonymous: bool
        :param TokenValidTime: Token有效时间
        :type TokenValidTime: int
        :param InternalEndpoint: 实例内部访问地址
        :type InternalEndpoint: str
        """
        self.RegistryId = None
        self.RegistryName = None
        self.RegistryType = None
        self.Status = None
        self.PublicDomain = None
        self.CreatedAt = None
        self.RegionName = None
        self.RegionId = None
        self.EnableAnonymous = None
        self.TokenValidTime = None
        self.InternalEndpoint = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RegistryName = params.get("RegistryName")
        self.RegistryType = params.get("RegistryType")
        self.Status = params.get("Status")
        self.PublicDomain = params.get("PublicDomain")
        self.CreatedAt = params.get("CreatedAt")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.EnableAnonymous = params.get("EnableAnonymous")
        self.TokenValidTime = params.get("TokenValidTime")
        self.InternalEndpoint = params.get("InternalEndpoint")


class RegistryCondition(AbstractModel):
    """实例创建过程

    """

    def __init__(self):
        """
        :param Type: 实例创建过程类型
        :type Type: str
        :param Status: 实例创建过程状态
        :type Status: str
        :param Reason: 转换到该过程的简明原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self.Type = None
        self.Status = None
        self.Reason = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")


class RegistryStatus(AbstractModel):
    """实例状态

    """

    def __init__(self):
        """
        :param RegistryId: 实例的Id
        :type RegistryId: str
        :param Status: 实例的状态
        :type Status: str
        :param Conditions: 附加状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of RegistryCondition
        """
        self.RegistryId = None
        self.Status = None
        self.Conditions = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Status = params.get("Status")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RegistryCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)


class RepoInfo(AbstractModel):
    """仓库的信息

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        :param RepoType: 仓库类型
        :type RepoType: str
        :param TagCount: Tag数量
        :type TagCount: int
        :param Public: 是否为公开
        :type Public: int
        :param IsUserFavor: 是否为用户收藏
        :type IsUserFavor: bool
        :param IsQcloudOfficial: 是否为腾讯云官方仓库
        :type IsQcloudOfficial: bool
        :param FavorCount: 被收藏的个数
        :type FavorCount: int
        :param PullCount: 拉取的数量
        :type PullCount: int
        :param Description: 描述
        :type Description: str
        :param CreationTime: 仓库创建时间
        :type CreationTime: str
        :param UpdateTime: 仓库更新时间
        :type UpdateTime: str
        """
        self.RepoName = None
        self.RepoType = None
        self.TagCount = None
        self.Public = None
        self.IsUserFavor = None
        self.IsQcloudOfficial = None
        self.FavorCount = None
        self.PullCount = None
        self.Description = None
        self.CreationTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.RepoType = params.get("RepoType")
        self.TagCount = params.get("TagCount")
        self.Public = params.get("Public")
        self.IsUserFavor = params.get("IsUserFavor")
        self.IsQcloudOfficial = params.get("IsQcloudOfficial")
        self.FavorCount = params.get("FavorCount")
        self.PullCount = params.get("PullCount")
        self.Description = params.get("Description")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")


class RepoInfoResp(AbstractModel):
    """仓库信息的返回信息

    """

    def __init__(self):
        """
        :param TotalCount: 仓库总数
        :type TotalCount: int
        :param RepoInfo: 仓库信息列表
        :type RepoInfo: list of RepoInfo
        :param Server: Server信息
        :type Server: str
        """
        self.TotalCount = None
        self.RepoInfo = None
        self.Server = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self.RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = RepoInfo()
                obj._deserialize(item)
                self.RepoInfo.append(obj)
        self.Server = params.get("Server")


class RepoIsExistResp(AbstractModel):
    """仓库是否存在的返回值

    """

    def __init__(self):
        """
        :param IsExist: 仓库是否存在
        :type IsExist: bool
        """
        self.IsExist = None


    def _deserialize(self, params):
        self.IsExist = params.get("IsExist")


class RepositoryInfoResp(AbstractModel):
    """查询共享版仓库信息返回

    """

    def __init__(self):
        """
        :param RepoName: 镜像仓库名字
        :type RepoName: str
        :param RepoType: 镜像仓库类型
        :type RepoType: str
        :param Server: 镜像仓库服务地址
        :type Server: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param Description: 镜像仓库描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Public: 是否为公有镜像
        :type Public: int
        :param PullCount: 下载次数
        :type PullCount: int
        :param FavorCount: 收藏次数
        :type FavorCount: int
        :param IsUserFavor: 是否为用户收藏
        :type IsUserFavor: bool
        :param IsQcloudOfficial: 是否为腾讯云官方镜像
        :type IsQcloudOfficial: bool
        """
        self.RepoName = None
        self.RepoType = None
        self.Server = None
        self.CreationTime = None
        self.Description = None
        self.Public = None
        self.PullCount = None
        self.FavorCount = None
        self.IsUserFavor = None
        self.IsQcloudOfficial = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.RepoType = params.get("RepoType")
        self.Server = params.get("Server")
        self.CreationTime = params.get("CreationTime")
        self.Description = params.get("Description")
        self.Public = params.get("Public")
        self.PullCount = params.get("PullCount")
        self.FavorCount = params.get("FavorCount")
        self.IsUserFavor = params.get("IsUserFavor")
        self.IsQcloudOfficial = params.get("IsQcloudOfficial")


class RespLimit(AbstractModel):
    """用户配额返回值

    """

    def __init__(self):
        """
        :param LimitInfo: 配额信息
        :type LimitInfo: list of Limit
        """
        self.LimitInfo = None


    def _deserialize(self, params):
        if params.get("LimitInfo") is not None:
            self.LimitInfo = []
            for item in params.get("LimitInfo"):
                obj = Limit()
                obj._deserialize(item)
                self.LimitInfo.append(obj)


class SameImagesResp(AbstractModel):
    """指定tag镜像内容相同的tag列表

    """

    def __init__(self):
        """
        :param SameImages: tag列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SameImages: list of str
        """
        self.SameImages = None


    def _deserialize(self, params):
        self.SameImages = params.get("SameImages")


class SearchUserRepositoryResp(AbstractModel):
    """获取满足输入搜索条件的用户镜像仓库

    """

    def __init__(self):
        """
        :param TotalCount: 总个数
        :type TotalCount: int
        :param RepoInfo: 仓库列表
        :type RepoInfo: list of RepoInfo
        :param Server: Server
        :type Server: str
        :param PrivilegeFiltered: PrivilegeFiltered
        :type PrivilegeFiltered: bool
        """
        self.TotalCount = None
        self.RepoInfo = None
        self.Server = None
        self.PrivilegeFiltered = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self.RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = RepoInfo()
                obj._deserialize(item)
                self.RepoInfo.append(obj)
        self.Server = params.get("Server")
        self.PrivilegeFiltered = params.get("PrivilegeFiltered")


class TagInfo(AbstractModel):
    """镜像tag信息

    """

    def __init__(self):
        """
        :param TagName: Tag名称
        :type TagName: str
        :param TagId: 镜像Id
        :type TagId: str
        :param ImageId: docker image 可以看到的id
        :type ImageId: str
        :param Size: 大小
        :type Size: str
        :param CreationTime: 镜像的创建时间
        :type CreationTime: str
        :param DurationDays: 镜像创建至今时间长度
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationDays: str
        :param Author: 镜像的作者
        :type Author: str
        :param Architecture: 次镜像建议运行的系统架构
        :type Architecture: str
        :param DockerVersion: 创建此镜像的docker版本
        :type DockerVersion: str
        :param OS: 此镜像建议运行系统
        :type OS: str
        :param SizeByte: SizeByte
        :type SizeByte: int
        :param Id: Id
        :type Id: int
        :param UpdateTime: 数据更新时间
        :type UpdateTime: str
        :param PushTime: 镜像更新时间
        :type PushTime: str
        """
        self.TagName = None
        self.TagId = None
        self.ImageId = None
        self.Size = None
        self.CreationTime = None
        self.DurationDays = None
        self.Author = None
        self.Architecture = None
        self.DockerVersion = None
        self.OS = None
        self.SizeByte = None
        self.Id = None
        self.UpdateTime = None
        self.PushTime = None


    def _deserialize(self, params):
        self.TagName = params.get("TagName")
        self.TagId = params.get("TagId")
        self.ImageId = params.get("ImageId")
        self.Size = params.get("Size")
        self.CreationTime = params.get("CreationTime")
        self.DurationDays = params.get("DurationDays")
        self.Author = params.get("Author")
        self.Architecture = params.get("Architecture")
        self.DockerVersion = params.get("DockerVersion")
        self.OS = params.get("OS")
        self.SizeByte = params.get("SizeByte")
        self.Id = params.get("Id")
        self.UpdateTime = params.get("UpdateTime")
        self.PushTime = params.get("PushTime")


class TagInfoResp(AbstractModel):
    """Tag列表的返回值

    """

    def __init__(self):
        """
        :param TagCount: Tag的总数
        :type TagCount: int
        :param TagInfo: TagInfo列表
        :type TagInfo: list of TagInfo
        :param Server: Server
        :type Server: str
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.TagCount = None
        self.TagInfo = None
        self.Server = None
        self.RepoName = None


    def _deserialize(self, params):
        self.TagCount = params.get("TagCount")
        if params.get("TagInfo") is not None:
            self.TagInfo = []
            for item in params.get("TagInfo"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagInfo.append(obj)
        self.Server = params.get("Server")
        self.RepoName = params.get("RepoName")


class TcrImageInfo(AbstractModel):
    """镜像信息

    """

    def __init__(self):
        """
        :param Digest: 哈希值
        :type Digest: str
        :param Size: 镜像大小
        :type Size: int
        :param ImageVersion: Tag名称
        :type ImageVersion: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.Digest = None
        self.Size = None
        self.ImageVersion = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Digest = params.get("Digest")
        self.Size = params.get("Size")
        self.ImageVersion = params.get("ImageVersion")
        self.UpdateTime = params.get("UpdateTime")


class TcrInstanceToken(AbstractModel):
    """实例登录令牌

    """

    def __init__(self):
        """
        :param Id: 令牌ID
        :type Id: str
        :param Desc: 令牌描述
        :type Desc: str
        :param RegistryId: 令牌所属实例ID
        :type RegistryId: str
        :param Enabled: 令牌启用状态
        :type Enabled: bool
        :param CreatedAt: 令牌创建时间
        :type CreatedAt: str
        :param ExpiredAt: 令牌过期时间戳
        :type ExpiredAt: int
        """
        self.Id = None
        self.Desc = None
        self.RegistryId = None
        self.Enabled = None
        self.CreatedAt = None
        self.ExpiredAt = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Desc = params.get("Desc")
        self.RegistryId = params.get("RegistryId")
        self.Enabled = params.get("Enabled")
        self.CreatedAt = params.get("CreatedAt")
        self.ExpiredAt = params.get("ExpiredAt")


class TcrNamespaceInfo(AbstractModel):
    """Tcr 命名空间的描述

    """

    def __init__(self):
        """
        :param Name: 命名空间名称
        :type Name: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param Public: 访问级别
        :type Public: bool
        :param NamespaceId: 命名空间的Id
        :type NamespaceId: int
        """
        self.Name = None
        self.CreationTime = None
        self.Public = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CreationTime = params.get("CreationTime")
        self.Public = params.get("Public")
        self.NamespaceId = params.get("NamespaceId")


class TcrRepositoryInfo(AbstractModel):
    """Tcr镜像仓库信息

    """

    def __init__(self):
        """
        :param Name: 仓库名称
        :type Name: str
        :param Namespace: 命名空间名称
        :type Namespace: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param Public: 是否公开
        :type Public: bool
        :param Description: 仓库详细描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param BriefDescription: 简单描述
注意：此字段可能返回 null，表示取不到有效值。
        :type BriefDescription: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.Name = None
        self.Namespace = None
        self.CreationTime = None
        self.Public = None
        self.Description = None
        self.BriefDescription = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.CreationTime = params.get("CreationTime")
        self.Public = params.get("Public")
        self.Description = params.get("Description")
        self.BriefDescription = params.get("BriefDescription")
        self.UpdateTime = params.get("UpdateTime")


class TriggerInvokeCondition(AbstractModel):
    """触发器触发条件

    """

    def __init__(self):
        """
        :param InvokeMethod: 触发方式
        :type InvokeMethod: str
        :param InvokeExpr: 触发表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeExpr: str
        """
        self.InvokeMethod = None
        self.InvokeExpr = None


    def _deserialize(self, params):
        self.InvokeMethod = params.get("InvokeMethod")
        self.InvokeExpr = params.get("InvokeExpr")


class TriggerInvokePara(AbstractModel):
    """触发器触发参数

    """

    def __init__(self):
        """
        :param AppId: AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param ClusterId: TKE集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Namespace: TKE集群命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param ServiceName: TKE集群工作负载名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param ContainerName: TKE集群工作负载中容器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerName: str
        :param ClusterRegion: TKE集群地域数字ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterRegion: int
        """
        self.AppId = None
        self.ClusterId = None
        self.Namespace = None
        self.ServiceName = None
        self.ContainerName = None
        self.ClusterRegion = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.ServiceName = params.get("ServiceName")
        self.ContainerName = params.get("ContainerName")
        self.ClusterRegion = params.get("ClusterRegion")


class TriggerInvokeResult(AbstractModel):
    """触发器触发结果

    """

    def __init__(self):
        """
        :param ReturnCode: 请求TKE返回值
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnCode: int
        :param ReturnMsg: 请求TKE返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnMsg: str
        """
        self.ReturnCode = None
        self.ReturnMsg = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")


class TriggerLogResp(AbstractModel):
    """触发器日志

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RepoName: str
        :param TagName: Tag名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param TriggerName: 触发器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerName: str
        :param InvokeSource: 触发方式
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeSource: str
        :param InvokeAction: 触发动作
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeAction: str
        :param InvokeTime: 触发时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeTime: str
        :param InvokeCondition: 触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeCondition: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeCondition`
        :param InvokePara: 触发参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokePara: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokePara`
        :param InvokeResult: 触发结果
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeResult: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeResult`
        """
        self.RepoName = None
        self.TagName = None
        self.TriggerName = None
        self.InvokeSource = None
        self.InvokeAction = None
        self.InvokeTime = None
        self.InvokeCondition = None
        self.InvokePara = None
        self.InvokeResult = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")
        self.TriggerName = params.get("TriggerName")
        self.InvokeSource = params.get("InvokeSource")
        self.InvokeAction = params.get("InvokeAction")
        self.InvokeTime = params.get("InvokeTime")
        if params.get("InvokeCondition") is not None:
            self.InvokeCondition = TriggerInvokeCondition()
            self.InvokeCondition._deserialize(params.get("InvokeCondition"))
        if params.get("InvokePara") is not None:
            self.InvokePara = TriggerInvokePara()
            self.InvokePara._deserialize(params.get("InvokePara"))
        if params.get("InvokeResult") is not None:
            self.InvokeResult = TriggerInvokeResult()
            self.InvokeResult._deserialize(params.get("InvokeResult"))


class TriggerResp(AbstractModel):
    """触发器返回值

    """

    def __init__(self):
        """
        :param TriggerName: 触发器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerName: str
        :param InvokeSource: 触发来源
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeSource: str
        :param InvokeAction: 触发动作
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeAction: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param InvokeCondition: 触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokeCondition: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokeCondition`
        :param InvokePara: 触发器参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokePara: :class:`tencentcloud.tcr.v20190924.models.TriggerInvokePara`
        """
        self.TriggerName = None
        self.InvokeSource = None
        self.InvokeAction = None
        self.CreateTime = None
        self.UpdateTime = None
        self.InvokeCondition = None
        self.InvokePara = None


    def _deserialize(self, params):
        self.TriggerName = params.get("TriggerName")
        self.InvokeSource = params.get("InvokeSource")
        self.InvokeAction = params.get("InvokeAction")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("InvokeCondition") is not None:
            self.InvokeCondition = TriggerInvokeCondition()
            self.InvokeCondition._deserialize(params.get("InvokeCondition"))
        if params.get("InvokePara") is not None:
            self.InvokePara = TriggerInvokePara()
            self.InvokePara._deserialize(params.get("InvokePara"))


class ValidateNamespaceExistPersonalRequest(AbstractModel):
    """ValidateNamespaceExistPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间名称
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")


class ValidateNamespaceExistPersonalResponse(AbstractModel):
    """ValidateNamespaceExistPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 命名空间是否存在
        :type Data: :class:`tencentcloud.tcr.v20190924.models.NamespaceIsExistsResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = NamespaceIsExistsResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ValidateRepositoryExistPersonalRequest(AbstractModel):
    """ValidateRepositoryExistPersonal请求参数结构体

    """

    def __init__(self):
        """
        :param RepoName: 仓库名称
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")


class ValidateRepositoryExistPersonalResponse(AbstractModel):
    """ValidateRepositoryExistPersonal返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 仓库是否存在
        :type Data: :class:`tencentcloud.tcr.v20190924.models.RepoIsExistResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RepoIsExistResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class WebhookTarget(AbstractModel):
    """触发器目标

    """

    def __init__(self):
        """
        :param Address: 目标地址
        :type Address: str
        :param Headers: 自定义 Headers
        :type Headers: list of Header
        """
        self.Address = None
        self.Headers = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self.Headers.append(obj)


class WebhookTrigger(AbstractModel):
    """Webhook 触发器

    """

    def __init__(self):
        """
        :param Name: 触发器名称
        :type Name: str
        :param Targets: 触发器目标
        :type Targets: list of WebhookTarget
        :param EventTypes: 触发动作
        :type EventTypes: list of str
        :param Condition: 触发规则
        :type Condition: str
        :param Enabled: 启用触发器
        :type Enabled: bool
        :param Id: 触发器Id
        :type Id: int
        :param Description: 触发器描述
        :type Description: str
        :param NamespaceId: 触发器所属命名空间 Id
        :type NamespaceId: int
        """
        self.Name = None
        self.Targets = None
        self.EventTypes = None
        self.Condition = None
        self.Enabled = None
        self.Id = None
        self.Description = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = WebhookTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.EventTypes = params.get("EventTypes")
        self.Condition = params.get("Condition")
        self.Enabled = params.get("Enabled")
        self.Id = params.get("Id")
        self.Description = params.get("Description")
        self.NamespaceId = params.get("NamespaceId")


class WebhookTriggerLog(AbstractModel):
    """触发器日志

    """

    def __init__(self):
        """
        :param Id: 日志 Id
        :type Id: int
        :param TriggerId: 触发器 Id
        :type TriggerId: int
        :param EventType: 事件类型
        :type EventType: str
        :param NotifyType: 通知类型
        :type NotifyType: str
        :param Detail: 详情
        :type Detail: str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Status: 状态
        :type Status: str
        """
        self.Id = None
        self.TriggerId = None
        self.EventType = None
        self.NotifyType = None
        self.Detail = None
        self.CreationTime = None
        self.UpdateTime = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TriggerId = params.get("TriggerId")
        self.EventType = params.get("EventType")
        self.NotifyType = params.get("NotifyType")
        self.Detail = params.get("Detail")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")