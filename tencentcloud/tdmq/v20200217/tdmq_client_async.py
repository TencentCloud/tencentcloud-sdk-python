# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.tdmq.v20200217 import models
from typing import Dict


class TdmqClient(AbstractClient):
    _apiVersion = '2020-02-17'
    _endpoint = 'tdmq.tencentcloudapi.com'
    _service = 'tdmq'

    async def AcknowledgeMessage(
            self,
            request: models.AcknowledgeMessageRequest,
            opts: Dict = None,
    ) -> models.AcknowledgeMessageResponse:
        """
        根据提供的 MessageID 确认指定 topic 中的消息
        """
        
        kwargs = {}
        kwargs["action"] = "AcknowledgeMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcknowledgeMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearCmqQueue(
            self,
            request: models.ClearCmqQueueRequest,
            opts: Dict = None,
    ) -> models.ClearCmqQueueResponse:
        """
        清空cmq消息队列中的消息
        """
        
        kwargs = {}
        kwargs["action"] = "ClearCmqQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearCmqQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearCmqSubscriptionFilterTags(
            self,
            request: models.ClearCmqSubscriptionFilterTagsRequest,
            opts: Dict = None,
    ) -> models.ClearCmqSubscriptionFilterTagsResponse:
        """
        清空订阅者消息标签
        """
        
        kwargs = {}
        kwargs["action"] = "ClearCmqSubscriptionFilterTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearCmqSubscriptionFilterTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        创建用户的集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCmqQueue(
            self,
            request: models.CreateCmqQueueRequest,
            opts: Dict = None,
    ) -> models.CreateCmqQueueResponse:
        """
        创建cmq队列接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCmqQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCmqQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCmqSubscribe(
            self,
            request: models.CreateCmqSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreateCmqSubscribeResponse:
        """
        创建cmq订阅接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCmqSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCmqSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCmqTopic(
            self,
            request: models.CreateCmqTopicRequest,
            opts: Dict = None,
    ) -> models.CreateCmqTopicResponse:
        """
        创建cmq主题
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCmqTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCmqTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnvironment(
            self,
            request: models.CreateEnvironmentRequest,
            opts: Dict = None,
    ) -> models.CreateEnvironmentResponse:
        """
        用于在用户账户下创建消息队列 Tdmq 命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnvironmentRole(
            self,
            request: models.CreateEnvironmentRoleRequest,
            opts: Dict = None,
    ) -> models.CreateEnvironmentRoleResponse:
        """
        创建环境角色授权
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvironmentRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvironmentRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProCluster(
            self,
            request: models.CreateProClusterRequest,
            opts: Dict = None,
    ) -> models.CreateProClusterResponse:
        """
        创建专业集群——预付费，仅通过api调用
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQBinding(
            self,
            request: models.CreateRabbitMQBindingRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQBindingResponse:
        """
        创建RabbitMQ路由关系
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQUser(
            self,
            request: models.CreateRabbitMQUserRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQUserResponse:
        """
        创建RabbitMQ的用户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQVipInstance(
            self,
            request: models.CreateRabbitMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQVipInstanceResponse:
        """
        创建 RabbitMQ 托管版实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQVirtualHost(
            self,
            request: models.CreateRabbitMQVirtualHostRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQVirtualHostResponse:
        """
        创建RabbitMQ的vhost
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQCluster(
            self,
            request: models.CreateRocketMQClusterRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQClusterResponse:
        """
        创建 RocketMQ 集群。
        当前 API 适用集群：4.x 虚拟集群。创建 4.x 专享或通用集群的接口文档见 [CreateRocketMQVipInstance](https://cloud.tencent.com/document/api/1179/95721)，创建 5.x 集群接口文档见 [CreateInstance](https://cloud.tencent.com/document/api/1493/97868)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQEnvironmentRole(
            self,
            request: models.CreateRocketMQEnvironmentRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQEnvironmentRoleResponse:
        """
        创建角色授权。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的创建角色接口文档见 [CreateRole](https://cloud.tencent.com/document/api/1493/98864)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQEnvironmentRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQEnvironmentRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQGroup(
            self,
            request: models.CreateRocketMQGroupRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQGroupResponse:
        """
        创建 RocketMQ 消费组。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。创建 5.x 集群消费组的接口文档见 [CreateConsumerGroup](https://cloud.tencent.com/document/api/1493/97943)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQNamespace(
            self,
            request: models.CreateRocketMQNamespaceRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQNamespaceResponse:
        """
        创建 RocketMQ 命名空间。
        当前 API 适用集群：4.x 虚拟集群和 4.x 专享集群，其他集群类型均不支持该功能。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQRole(
            self,
            request: models.CreateRocketMQRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQRoleResponse:
        """
        创建角色。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的创建角色接口文档见 [CreateRole](https://cloud.tencent.com/document/api/1493/98864)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQTopic(
            self,
            request: models.CreateRocketMQTopicRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQTopicResponse:
        """
        批量创建 RocketMQ 主题。
        当前云 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的创建 Topic 接口文档见 [CreateTopic](https://cloud.tencent.com/document/api/1493/97947)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQTopicV2(
            self,
            request: models.CreateRocketMQTopicV2Request,
            opts: Dict = None,
    ) -> models.CreateRocketMQTopicV2Response:
        """
        创建 RocketMQ 主题。
        当前云 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的创建 Topic 接口文档见 [CreateTopic](https://cloud.tencent.com/document/api/1493/97947)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQTopicV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQTopicV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQVipInstance(
            self,
            request: models.CreateRocketMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQVipInstanceResponse:
        """
        创建 RocketMQ 4.x 集群。
        当前 API 适用集群：4.x 专享集群 和 4.x 通用集群。创建 5.x 集群的接口文档见 [CreateInstance](https://cloud.tencent.com/document/api/1493/97868)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRole(
            self,
            request: models.CreateRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRoleResponse:
        """
        创建角色
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubscription(
            self,
            request: models.CreateSubscriptionRequest,
            opts: Dict = None,
    ) -> models.CreateSubscriptionResponse:
        """
        创建一个主题的订阅关系
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopic(
            self,
            request: models.CreateTopicRequest,
            opts: Dict = None,
    ) -> models.CreateTopicResponse:
        """
        新增指定分区、类型的消息主题
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        删除集群
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCmqQueue(
            self,
            request: models.DeleteCmqQueueRequest,
            opts: Dict = None,
    ) -> models.DeleteCmqQueueResponse:
        """
        删除cmq队列
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCmqQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCmqQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCmqSubscribe(
            self,
            request: models.DeleteCmqSubscribeRequest,
            opts: Dict = None,
    ) -> models.DeleteCmqSubscribeResponse:
        """
        删除cmq订阅
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCmqSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCmqSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCmqTopic(
            self,
            request: models.DeleteCmqTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteCmqTopicResponse:
        """
        删除cmq主题
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCmqTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCmqTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnvironmentRoles(
            self,
            request: models.DeleteEnvironmentRolesRequest,
            opts: Dict = None,
    ) -> models.DeleteEnvironmentRolesResponse:
        """
        删除环境角色授权。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnvironmentRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnvironmentRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnvironments(
            self,
            request: models.DeleteEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DeleteEnvironmentsResponse:
        """
        批量删除租户下的命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProCluster(
            self,
            request: models.DeleteProClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteProClusterResponse:
        """
        删除专业集群——预付费，仅通过API 调用
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQBinding(
            self,
            request: models.DeleteRabbitMQBindingRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQBindingResponse:
        """
        解绑RabbitMQ路由关系
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQPermission(
            self,
            request: models.DeleteRabbitMQPermissionRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQPermissionResponse:
        """
        删除RabbitMQ的权限
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQUser(
            self,
            request: models.DeleteRabbitMQUserRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQUserResponse:
        """
        删除RabbitMQ的用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQVipInstance(
            self,
            request: models.DeleteRabbitMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQVipInstanceResponse:
        """
        删除 RabbitMQ 托管版实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQVirtualHost(
            self,
            request: models.DeleteRabbitMQVirtualHostRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQVirtualHostResponse:
        """
        删除RabbitMQ的vhost
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQCluster(
            self,
            request: models.DeleteRocketMQClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQClusterResponse:
        """
        删除 RocketMQ 集群。
        当前 API 适用集群：4.x 虚拟集群。删除 4.x 专享或通用集群的接口文档见 [DeleteRocketMQVipInstance](https://cloud.tencent.com/document/api/1179/95802)，删除 5.x 集群的接口文档见 [DeleteInstance](https://cloud.tencent.com/document/product/1493/97867)。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQEnvironmentRoles(
            self,
            request: models.DeleteRocketMQEnvironmentRolesRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQEnvironmentRolesResponse:
        """
        批量删除角色授权。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的删除角色接口文档见 [DeleteRole](https://cloud.tencent.com/document/api/1493/98863)。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQEnvironmentRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQEnvironmentRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQGroup(
            self,
            request: models.DeleteRocketMQGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQGroupResponse:
        """
        删除 RocketMQ 消费组。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。删除 5.x 集群消费组的接口文档见 [DeleteConsumerGroup](https://cloud.tencent.com/document/api/1493/97942)。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQNamespace(
            self,
            request: models.DeleteRocketMQNamespaceRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQNamespaceResponse:
        """
        删除 RocketMQ 命名空间。
        当前 API 适用集群：4.x 虚拟集群和 4.x 专享集群，其他集群类型均不支持该功能。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQRoles(
            self,
            request: models.DeleteRocketMQRolesRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQRolesResponse:
        """
        批量删除角色。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的删除角色接口文档见 [DeleteRole](https://cloud.tencent.com/document/api/1493/98863)。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQTopic(
            self,
            request: models.DeleteRocketMQTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQTopicResponse:
        """
        删除 RocketMQ 主题。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。删除 5.x 集群主题的接口文档见 [DeleteTopic](https://cloud.tencent.com/document/api/1493/97946)。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQVipInstance(
            self,
            request: models.DeleteRocketMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQVipInstanceResponse:
        """
        删除 RocketMQ 专享或通用集群。
        当前 API 适用集群：4.x 专享集群 和 4.x 通用集群。删除 5.x 集群的接口文档见 [DeleteInstance](https://cloud.tencent.com/document/api/1493/97867)。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoles(
            self,
            request: models.DeleteRolesRequest,
            opts: Dict = None,
    ) -> models.DeleteRolesResponse:
        """
        删除角色，支持批量。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSubscriptions(
            self,
            request: models.DeleteSubscriptionsRequest,
            opts: Dict = None,
    ) -> models.DeleteSubscriptionsResponse:
        """
        删除订阅关系
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSubscriptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSubscriptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopics(
            self,
            request: models.DeleteTopicsRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicsResponse:
        """
        批量删除topics
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAMQPClusters(
            self,
            request: models.DescribeAMQPClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeAMQPClustersResponse:
        """
        历史原因，该接口位于tdmq-manager，目前rabbitmq产品没有使用该接口，当前使用的是DescribeRabbitMQVipInstances。不过从调用链上看，线网还有请求流程，所以走预下线流程。

        获取amqp集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAMQPClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAMQPClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllTenants(
            self,
            request: models.DescribeAllTenantsRequest,
            opts: Dict = None,
    ) -> models.DescribeAllTenantsResponse:
        """
        获取某个租户的虚拟集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllTenants"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllTenantsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindClusters(
            self,
            request: models.DescribeBindClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeBindClustersResponse:
        """
        获取用户绑定的专享集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindVpcs(
            self,
            request: models.DescribeBindVpcsRequest,
            opts: Dict = None,
    ) -> models.DescribeBindVpcsResponse:
        """
        获取租户VPC绑定关系
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindVpcs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindVpcsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDetail(
            self,
            request: models.DescribeClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDetailResponse:
        """
        获取集群的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        获取集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmqQueueDetail(
            self,
            request: models.DescribeCmqQueueDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqQueueDetailResponse:
        """
        查询cmq队列详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqQueueDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqQueueDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmqQueues(
            self,
            request: models.DescribeCmqQueuesRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqQueuesResponse:
        """
        查询cmq全量队列
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqQueues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqQueuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmqSubscriptionDetail(
            self,
            request: models.DescribeCmqSubscriptionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqSubscriptionDetailResponse:
        """
        查询cmq订阅详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqSubscriptionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqSubscriptionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmqTopicDetail(
            self,
            request: models.DescribeCmqTopicDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqTopicDetailResponse:
        """
        查询cmq主题详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqTopicDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqTopicDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmqTopics(
            self,
            request: models.DescribeCmqTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqTopicsResponse:
        """
        枚举cmq全量主题
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironmentAttributes(
            self,
            request: models.DescribeEnvironmentAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentAttributesResponse:
        """
        获取指定命名空间的属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironmentAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironmentRoles(
            self,
            request: models.DescribeEnvironmentRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentRolesResponse:
        """
        获取命名空间角色列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironmentRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        获取租户下命名空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMqMsgTrace(
            self,
            request: models.DescribeMqMsgTraceRequest,
            opts: Dict = None,
    ) -> models.DescribeMqMsgTraceResponse:
        """
        查询消息轨迹
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMqMsgTrace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMqMsgTraceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMsg(
            self,
            request: models.DescribeMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeMsgResponse:
        """
        消息详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMsgTrace(
            self,
            request: models.DescribeMsgTraceRequest,
            opts: Dict = None,
    ) -> models.DescribeMsgTraceResponse:
        """
        查询单条消息的消息轨迹
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMsgTrace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMsgTraceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNamespaceBundlesOpt(
            self,
            request: models.DescribeNamespaceBundlesOptRequest,
            opts: Dict = None,
    ) -> models.DescribeNamespaceBundlesOptResponse:
        """
        运营端获取命名空间bundle列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNamespaceBundlesOpt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNamespaceBundlesOptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodeHealthOpt(
            self,
            request: models.DescribeNodeHealthOptRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeHealthOptResponse:
        """
        运营端获节点健康状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodeHealthOpt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeHealthOptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublisherSummary(
            self,
            request: models.DescribePublisherSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribePublisherSummaryResponse:
        """
        获取消息生产概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublisherSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublisherSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublishers(
            self,
            request: models.DescribePublishersRequest,
            opts: Dict = None,
    ) -> models.DescribePublishersResponse:
        """
        获取生产者信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublishers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublishersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePulsarProInstanceDetail(
            self,
            request: models.DescribePulsarProInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePulsarProInstanceDetailResponse:
        """
        获取Pulsar专业版集群实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePulsarProInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePulsarProInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePulsarProInstances(
            self,
            request: models.DescribePulsarProInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribePulsarProInstancesResponse:
        """
        查询用户已购的Pulsar专业版实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePulsarProInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePulsarProInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQBindings(
            self,
            request: models.DescribeRabbitMQBindingsRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQBindingsResponse:
        """
        查询RabbitMQ路由关系列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQExchanges(
            self,
            request: models.DescribeRabbitMQExchangesRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQExchangesResponse:
        """
        查询RabbitMQ exchange 列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQExchanges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQExchangesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQNodeList(
            self,
            request: models.DescribeRabbitMQNodeListRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQNodeListResponse:
        """
        查询 RabbitMQ 托管版节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQNodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQNodeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQPermission(
            self,
            request: models.DescribeRabbitMQPermissionRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQPermissionResponse:
        """
        查询RabbitMQ权限列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQQueueDetail(
            self,
            request: models.DescribeRabbitMQQueueDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQQueueDetailResponse:
        """
        查询RabbitMQ队列详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQQueueDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQQueueDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQQueues(
            self,
            request: models.DescribeRabbitMQQueuesRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQQueuesResponse:
        """
        查询RabbitMQ队列列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQQueues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQQueuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQUser(
            self,
            request: models.DescribeRabbitMQUserRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQUserResponse:
        """
        查询RabbitMQ用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQVipInstance(
            self,
            request: models.DescribeRabbitMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQVipInstanceResponse:
        """
        获取单个 RabbitMQ 托管版实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQVipInstances(
            self,
            request: models.DescribeRabbitMQVipInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQVipInstancesResponse:
        """
        查询用户已购的 RabbitMQ 托管版实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQVipInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQVipInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQVirtualHost(
            self,
            request: models.DescribeRabbitMQVirtualHostRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQVirtualHostResponse:
        """
        查询RabbitMQ vhost列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQCluster(
            self,
            request: models.DescribeRocketMQClusterRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQClusterResponse:
        """
        查询 RocketMQ 虚拟集群信息。
        当前 API 适用集群：4.x 虚拟集群。查询 4.x 专享或通用集群信息的接口文档见 [DescribeRocketMQVipInstanceDetail](https://cloud.tencent.com/document/api/1179/86725)，查询 5.x 集群信息的接口文档见 [DescribeInstance](https://cloud.tencent.com/document/api/1493/97866)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQClusters(
            self,
            request: models.DescribeRocketMQClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQClustersResponse:
        """
        查询 RocketMQ 虚拟集群列表。
        当前 API 适用集群：4.x 虚拟集群。查询 5.x 集群列表接口文档见 [DescribeInstanceList](https://cloud.tencent.com/document/api/1493/96028)，或者使用 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口适用所有集群类型。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQConsumeStats(
            self,
            request: models.DescribeRocketMQConsumeStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQConsumeStatsResponse:
        """
        查询 RocketMQ 消费详情列表。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。查询 5.x 集群消费详情的接口文档见 [DescribeConsumerGroup](https://cloud.tencent.com/document/api/1493/97941)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQConsumeStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQConsumeStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQConsumerConnectionDetail(
            self,
            request: models.DescribeRocketMQConsumerConnectionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQConsumerConnectionDetailResponse:
        """
        查询 RocketMQ 消费者客户端详情。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的查询消费者客户端详情接口文档见 [DescribeConsumerClient](https://cloud.tencent.com/document/api/1493/115240)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQConsumerConnectionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQConsumerConnectionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQConsumerConnections(
            self,
            request: models.DescribeRocketMQConsumerConnectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQConsumerConnectionsResponse:
        """
        查询 RocketMQ 消费组下的客户端连接列表。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群查询消费组下的客户端连接列表接口文档见 [DescribeConsumerClientList](https://cloud.tencent.com/document/api/1493/120140)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQConsumerConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQConsumerConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQEnvironmentRoles(
            self,
            request: models.DescribeRocketMQEnvironmentRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQEnvironmentRolesResponse:
        """
        查询角色授权列表。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的查询角色列表接口文档见 [DescribeRoleList](https://cloud.tencent.com/document/api/1493/98862)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQEnvironmentRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQEnvironmentRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQGroups(
            self,
            request: models.DescribeRocketMQGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQGroupsResponse:
        """
        查询 RocketMQ 消费组列表。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。查询 5.x 集群的消费组列表接口文档见 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQMigratingTopicList(
            self,
            request: models.DescribeRocketMQMigratingTopicListRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQMigratingTopicListResponse:
        """
        查询Topic迁移状态列表，源集群和目标集群客户端数量信息需要配合DescribeRocketMQSmoothMigrationTaskTopicInsNum接口查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQMigratingTopicList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQMigratingTopicListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQMsg(
            self,
            request: models.DescribeRocketMQMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQMsgResponse:
        """
        查询 RocketMQ 消息详情。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的查询消息详情接口文档见 [DescribeMessage](https://cloud.tencent.com/document/api/1493/114594)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQMsgTrace(
            self,
            request: models.DescribeRocketMQMsgTraceRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQMsgTraceResponse:
        """
        查询消息轨迹。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群查询消息轨迹的接口文档见 [DescribeMessageTrace](https://cloud.tencent.com/document/api/1493/114302)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQMsgTrace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQMsgTraceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQNamespaces(
            self,
            request: models.DescribeRocketMQNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQNamespacesResponse:
        """
        获取 RocketMQ 命名空间列表。
        当前 API 适用集群：4.x 虚拟集群和 4.x 专享集群，其他集群类型均不支持该功能。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQProducers(
            self,
            request: models.DescribeRocketMQProducersRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQProducersResponse:
        """
        查询 RocketMQ 指定主题下的生产者客户端列表。
        当前 API 适用集群：4.x 专享集群 和 4.x 通用集群。查询 5.x 集群主题下的生产者客户端列表接口文档见 [DescribeProducerList](https://cloud.tencent.com/document/api/1493/122548)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQProducers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQProducersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQPublicAccessMonitorData(
            self,
            request: models.DescribeRocketMQPublicAccessMonitorDataRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQPublicAccessMonitorDataResponse:
        """
        查询公网指标监控数据，目前仅支持客户端到 LB 的入带宽和出宽带指标。
        当前 API 适用集群：4.x 专享集群 和 4.x 通用集群。5.x 集群暂不支持该功能。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQPublicAccessMonitorData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQPublicAccessMonitorDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQPublicAccessPoint(
            self,
            request: models.DescribeRocketMQPublicAccessPointRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQPublicAccessPointResponse:
        """
        查询 RocketMQ 集群的公网接入点信息。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。查询 5.x 集群的公网接入点信息接口文档见 [DescribeInstance](https://cloud.tencent.com/document/api/1493/97866)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQPublicAccessPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQPublicAccessPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQRoles(
            self,
            request: models.DescribeRocketMQRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQRolesResponse:
        """
        查询角色列表。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的查询角色列表接口文档见 [DescribeRoleList](https://cloud.tencent.com/document/api/1493/98862)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQSmoothMigrationTask(
            self,
            request: models.DescribeRocketMQSmoothMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQSmoothMigrationTaskResponse:
        """
        用于获取RocketMQ平滑迁移任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQSmoothMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQSmoothMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQSubscriptions(
            self,
            request: models.DescribeRocketMQSubscriptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQSubscriptionsResponse:
        """
        查询 RocketMQ 消费组订阅关系列表。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群查询消费组订阅的主题列表接口文档见 [DescribeTopicListByGroup](https://cloud.tencent.com/document/api/1493/115314)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQSubscriptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQSubscriptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopUsages(
            self,
            request: models.DescribeRocketMQTopUsagesRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopUsagesResponse:
        """
        用于获取RocketMQ指标排序列表，比如集群实例下占用存储空间最多的主题排序。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群暂不支持该功能。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopUsages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopUsagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopic(
            self,
            request: models.DescribeRocketMQTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopicResponse:
        """
        获取RocketMQ主题详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopicMsgs(
            self,
            request: models.DescribeRocketMQTopicMsgsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopicMsgsResponse:
        """
        查询 RocketMQ 消息列表。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的查询消息列表接口文档见 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopicMsgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopicMsgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopicStats(
            self,
            request: models.DescribeRocketMQTopicStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopicStatsResponse:
        """
        查询 RocketMQ 主题生产详情列表。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群暂不支持该功能。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopicStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopicStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopics(
            self,
            request: models.DescribeRocketMQTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopicsResponse:
        """
        查询 RocketMQ 主题列表。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。查询 5.x 集群的主题列表接口文档见 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopicsByGroup(
            self,
            request: models.DescribeRocketMQTopicsByGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopicsByGroupResponse:
        """
        查询 RocketMQ 消费组订阅的主题列表。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群查询消费组订阅的主题列表接口文档见 [DescribeTopicListByGroup](https://cloud.tencent.com/document/api/1493/115314)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopicsByGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopicsByGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQVipInstanceDetail(
            self,
            request: models.DescribeRocketMQVipInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQVipInstanceDetailResponse:
        """
        查询 RocketMQ 集群信息。
        当前 API 适用集群：4.x 专享集群 和 4.x 通用集群。查询 5.x 集群信息的接口文档见 [DescribeInstance](https://cloud.tencent.com/document/api/1493/97866)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQVipInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQVipInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQVipInstances(
            self,
            request: models.DescribeRocketMQVipInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQVipInstancesResponse:
        """
        查询 RocketMQ 4.x 集群列表。
        当前 API 适用集群：4.x 专享集群 和 4.x 通用集群。查询 5.x 集群列表接口文档见 [DescribeInstanceList](https://cloud.tencent.com/document/api/1493/96028)，或者使用 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口适用所有集群类型。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQVipInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQVipInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoles(
            self,
            request: models.DescribeRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeRolesResponse:
        """
        获取角色列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscriptions(
            self,
            request: models.DescribeSubscriptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscriptionsResponse:
        """
        查询指定环境和主题下的订阅者列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscriptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscriptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicMsgs(
            self,
            request: models.DescribeTopicMsgsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicMsgsResponse:
        """
        消息查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicMsgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicMsgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopics(
            self,
            request: models.DescribeTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicsResponse:
        """
        获取环境下主题列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteDisasterRecovery(
            self,
            request: models.ExecuteDisasterRecoveryRequest,
            opts: Dict = None,
    ) -> models.ExecuteDisasterRecoveryResponse:
        """
        执行域名异地访问切换，域名的访问指向将切换至备份集群。
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteDisasterRecovery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteDisasterRecoveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRocketMQMessageDetail(
            self,
            request: models.ExportRocketMQMessageDetailRequest,
            opts: Dict = None,
    ) -> models.ExportRocketMQMessageDetailResponse:
        """
        导出RocketMQ消息详情
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRocketMQMessageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRocketMQMessageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTopicList(
            self,
            request: models.GetTopicListRequest,
            opts: Dict = None,
    ) -> models.GetTopicListResponse:
        """
        获取环境下主题列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetTopicList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTopicListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportRocketMQConsumerGroups(
            self,
            request: models.ImportRocketMQConsumerGroupsRequest,
            opts: Dict = None,
    ) -> models.ImportRocketMQConsumerGroupsResponse:
        """
        输入迁移任务id和要导入的Group，导入后台
        """
        
        kwargs = {}
        kwargs["action"] = "ImportRocketMQConsumerGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportRocketMQConsumerGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportRocketMQTopics(
            self,
            request: models.ImportRocketMQTopicsRequest,
            opts: Dict = None,
    ) -> models.ImportRocketMQTopicsResponse:
        """
        导入topic列表
        """
        
        kwargs = {}
        kwargs["action"] = "ImportRocketMQTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportRocketMQTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCluster(
            self,
            request: models.ModifyClusterRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterResponse:
        """
        更新集群信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCmqQueueAttribute(
            self,
            request: models.ModifyCmqQueueAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCmqQueueAttributeResponse:
        """
        修改cmq队列属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCmqQueueAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCmqQueueAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCmqSubscriptionAttribute(
            self,
            request: models.ModifyCmqSubscriptionAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCmqSubscriptionAttributeResponse:
        """
        修改cmq订阅属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCmqSubscriptionAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCmqSubscriptionAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCmqTopicAttribute(
            self,
            request: models.ModifyCmqTopicAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCmqTopicAttributeResponse:
        """
        修改cmq主题属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCmqTopicAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCmqTopicAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnvironmentAttributes(
            self,
            request: models.ModifyEnvironmentAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyEnvironmentAttributesResponse:
        """
        修改指定命名空间的属性值
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnvironmentAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnvironmentAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnvironmentRole(
            self,
            request: models.ModifyEnvironmentRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyEnvironmentRoleResponse:
        """
        修改环境角色授权。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnvironmentRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnvironmentRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPublicNetworkSecurityPolicy(
            self,
            request: models.ModifyPublicNetworkSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyPublicNetworkSecurityPolicyResponse:
        """
        修改pulsar专业版公网安全策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPublicNetworkSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPublicNetworkSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQPermission(
            self,
            request: models.ModifyRabbitMQPermissionRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQPermissionResponse:
        """
        修改RabbitMQ的权限
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQUser(
            self,
            request: models.ModifyRabbitMQUserRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQUserResponse:
        """
        修改RabbitMQ的用户
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQVipInstance(
            self,
            request: models.ModifyRabbitMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQVipInstanceResponse:
        """
        修改RabbitMQ专享版实例
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQVirtualHost(
            self,
            request: models.ModifyRabbitMQVirtualHostRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQVirtualHostResponse:
        """
        修改RabbitMQ的vhost
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQCluster(
            self,
            request: models.ModifyRocketMQClusterRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQClusterResponse:
        """
        修改 RocketMQ 集群属性。
        当前 API 适用集群：4.x 虚拟集群。修改 4.x 专享或通用集群属性接口文档见 [ModifyRocketMQInstance](https://cloud.tencent.com/document/api/1179/108862)，修改 5.x 集群属性的接口文档见 [ModifyInstance](https://cloud.tencent.com/document/api/1493/97865)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQEnvironmentRole(
            self,
            request: models.ModifyRocketMQEnvironmentRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQEnvironmentRoleResponse:
        """
        修改角色授权。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的修改角色接口文档见 [ModifyRole](https://cloud.tencent.com/document/api/1493/98861)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQEnvironmentRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQEnvironmentRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQGroup(
            self,
            request: models.ModifyRocketMQGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQGroupResponse:
        """
        修改 RocketMQ 消费组属性。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。修改 5.x 集群消费组属性的接口文档见 [ModifyConsumerGroup](https://cloud.tencent.com/document/api/1493/97940)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQInstance(
            self,
            request: models.ModifyRocketMQInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQInstanceResponse:
        """
        修改 RocketMQ 专享或通用集群属性。
        当前 API 适用集群：4.x 专享集群 和 4.x 通用集群。修改 5.x 集群属性的接口文档见 [ModifyInstance](https://cloud.tencent.com/document/api/1493/97865)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQInstanceSpec(
            self,
            request: models.ModifyRocketMQInstanceSpecRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQInstanceSpecResponse:
        """
        修改 RocketMQ 专享集群配置，可以支持实例规格、节点数和存储的升配和实例规格的降配。本 API 发起订单并成功支付后进入实例配置变更的流程，可通过 [DescribeRocketMQVipInstances](https://cloud.tencent.com/document/api/1179/80903) 查询实例是否已变更完成。
        当前 API 适用集群：4.x 专享集群 和 4.x 通用集群。修改 5.x 集群规格的接口文档见 [ModifyInstance](https://cloud.tencent.com/document/api/1493/97865)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQInstanceSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQInstanceSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQNamespace(
            self,
            request: models.ModifyRocketMQNamespaceRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQNamespaceResponse:
        """
        更新 RocketMQ 命名空间。
        当前 API 适用集群：4.x 虚拟集群和 4.x 专享集群，其他集群类型均不支持该功能。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQRole(
            self,
            request: models.ModifyRocketMQRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQRoleResponse:
        """
        修改角色。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的修改角色接口文档见 [ModifyRole](https://cloud.tencent.com/document/api/1493/98861)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQTopic(
            self,
            request: models.ModifyRocketMQTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQTopicResponse:
        """
        修改 RocketMQ 主题属性。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。修改 5.x 集群主题属性的接口文档见 [ModifyTopic](https://cloud.tencent.com/document/api/1493/97944)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRole(
            self,
            request: models.ModifyRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyRoleResponse:
        """
        角色修改
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTopic(
            self,
            request: models.ModifyTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyTopicResponse:
        """
        修改主题备注和分区数
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishCmqMsg(
            self,
            request: models.PublishCmqMsgRequest,
            opts: Dict = None,
    ) -> models.PublishCmqMsgResponse:
        """
        发送cmq主题消息
        """
        
        kwargs = {}
        kwargs["action"] = "PublishCmqMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishCmqMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReceiveMessage(
            self,
            request: models.ReceiveMessageRequest,
            opts: Dict = None,
    ) -> models.ReceiveMessageResponse:
        """
        当前 ReceiveMessage 接口只支持 Partitioned 类型的 Topic。该接口用于接收发送到指定 Partitioned Topic 中的消息，当 Partitioned Topic 中没有消息但还去尝试调用该接口时，会抛出 ReceiveTimeout 的异常。

        如何使用 BatchReceivePolicy：

        BatchReceive 接口提供了如下三个参数：

        ● MaxNumMessages: 即每次使用 BatchReceive 的时候，最多一次Receive接口返回多少条消息。
        ● MaxNumBytes：即每次使用 BatchReceive 的时候，最多一次Receive接口返回多大内容的消息，单位是：bytes。
        ● Timeout：即每次使用 BatchReceive 的时候，最多一次 Receive 接口的超时时间是多久，单位是：MS。

        默认如果上述三个参数都不指定，即关闭 BatchReceive 的特性。如果三个参数中的任意一个参数指定的数值大于 0，即开启 BatchReceive。BatchReceive 的结束条件为到达上述三个参数中任意一个指定的阈值。

        注意：MaxNumMessages 和 MaxNumBytes 每一次接收的最大消息同时受限于 ReceiveQueueSize 的大小，如果 ReceiveQueueSize 的大小设置为 5，MaxNumMessages 设置为10，那么一次 BatchReceive 接收的最多的消息是 5条，而不是10条。



        BatchReceivePolicy 的接口会一次性返回多条消息：

        1. 多条消息的内容之间使用特殊字符 '###' 来进行分割，业务侧接收到消息之后，可以利用不同语言提供的 Split 工具分割不同的消息。
        2. 多条消息的 MessageID 之间使用特殊字符 '###' 来进行分割，业务侧接收到消息之后，可以利用不同语言提供的 Split 工具分割不同的消息。（用于在调用 AcknowledgeMessage 接口中填入所需要的 MessageID 字段信息）
        """
        
        kwargs = {}
        kwargs["action"] = "ReceiveMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReceiveMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetMsgSubOffsetByTimestamp(
            self,
            request: models.ResetMsgSubOffsetByTimestampRequest,
            opts: Dict = None,
    ) -> models.ResetMsgSubOffsetByTimestampResponse:
        """
        根据时间戳进行消息回溯，精确到毫秒
        """
        
        kwargs = {}
        kwargs["action"] = "ResetMsgSubOffsetByTimestamp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetMsgSubOffsetByTimestampResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRocketMQConsumerOffSet(
            self,
            request: models.ResetRocketMQConsumerOffSetRequest,
            opts: Dict = None,
    ) -> models.ResetRocketMQConsumerOffSetResponse:
        """
        重置消费位点。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的重置消费位点接口文档见 [ResetConsumerGroupOffset](https://cloud.tencent.com/document/api/1493/116942)。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRocketMQConsumerOffSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRocketMQConsumerOffSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryRocketMQDlqMessage(
            self,
            request: models.RetryRocketMQDlqMessageRequest,
            opts: Dict = None,
    ) -> models.RetryRocketMQDlqMessageResponse:
        """
        重发 RocketMQ 死信消息。
        当前 API 适用集群：4.x 虚拟集群，4.x 专享集群 和 4.x 通用集群。5.x 集群的重发死信消息接口文档见 [ResendDeadLetterMessage](https://cloud.tencent.com/document/api/1493/114592)。
        """
        
        kwargs = {}
        kwargs["action"] = "RetryRocketMQDlqMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryRocketMQDlqMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RewindCmqQueue(
            self,
            request: models.RewindCmqQueueRequest,
            opts: Dict = None,
    ) -> models.RewindCmqQueueResponse:
        """
        回溯cmq队列
        """
        
        kwargs = {}
        kwargs["action"] = "RewindCmqQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RewindCmqQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendBatchMessages(
            self,
            request: models.SendBatchMessagesRequest,
            opts: Dict = None,
    ) -> models.SendBatchMessagesResponse:
        """
        批量发送消息

        注意：TDMQ 批量发送消息的接口是在 TDMQ-HTTP 的服务侧将消息打包为一个 Batch，然后将该 Batch 在服务内部当作一次 TCP 请求发送出去。所以在使用过程中，用户还是按照单条消息发送的逻辑，每一条消息是一个独立的 HTTP 的请求，在 TDMQ-HTTP 的服务内部，会将多个 HTTP 的请求聚合为一个 Batch 发送到服务端。即，批量发送消息在使用上与发送单条消息是一致的，batch 的聚合是在 TDMQ-HTTP 的服务内部完成的。
        """
        
        kwargs = {}
        kwargs["action"] = "SendBatchMessages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendBatchMessagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendCmqMsg(
            self,
            request: models.SendCmqMsgRequest,
            opts: Dict = None,
    ) -> models.SendCmqMsgResponse:
        """
        发送cmq消息
        """
        
        kwargs = {}
        kwargs["action"] = "SendCmqMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendCmqMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendMessages(
            self,
            request: models.SendMessagesRequest,
            opts: Dict = None,
    ) -> models.SendMessagesResponse:
        """
        发送单条消息
        不支持持久topic
        """
        
        kwargs = {}
        kwargs["action"] = "SendMessages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendMessagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendMsg(
            self,
            request: models.SendMsgRequest,
            opts: Dict = None,
    ) -> models.SendMsgResponse:
        """
        此接口仅用于测试发生消息，不能作为现网正式生产使用
        """
        
        kwargs = {}
        kwargs["action"] = "SendMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendRocketMQMessage(
            self,
            request: models.SendRocketMQMessageRequest,
            opts: Dict = None,
    ) -> models.SendRocketMQMessageResponse:
        """
        发送 RocketMQ 消息，该接口仅用于控制台发送少量测试消息，不保证SLA，且云 API 存在限流，在真实业务场景下，请使用 RocketMQ SDK 发送消息。
        """
        
        kwargs = {}
        kwargs["action"] = "SendRocketMQMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendRocketMQMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetRocketMQPublicAccessPoint(
            self,
            request: models.SetRocketMQPublicAccessPointRequest,
            opts: Dict = None,
    ) -> models.SetRocketMQPublicAccessPointResponse:
        """
        开启或关闭公网访问、设置安全访问策略。
        当前 API 适用集群：4.x 专享集群 和 4.x 通用集群。设置 5.x 集群的公网接入点接口文档见 [ModifyInstanceEndpoint](https://cloud.tencent.com/document/api/1493/115981)。
        """
        
        kwargs = {}
        kwargs["action"] = "SetRocketMQPublicAccessPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetRocketMQPublicAccessPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindCmqDeadLetter(
            self,
            request: models.UnbindCmqDeadLetterRequest,
            opts: Dict = None,
    ) -> models.UnbindCmqDeadLetterResponse:
        """
        解绑cmq死信队列
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindCmqDeadLetter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindCmqDeadLetterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyRocketMQConsume(
            self,
            request: models.VerifyRocketMQConsumeRequest,
            opts: Dict = None,
    ) -> models.VerifyRocketMQConsumeResponse:
        """
        Rocketmq消费验证
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyRocketMQConsume"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyRocketMQConsumeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)