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
from tencentcloud.trocket.v20230308 import models
from typing import Dict


class TrocketClient(AbstractClient):
    _apiVersion = '2023-03-08'
    _endpoint = 'trocket.tencentcloudapi.com'
    _service = 'trocket'

    async def ChangeMigratingTopicToNextStage(
            self,
            request: models.ChangeMigratingTopicToNextStageRequest,
            opts: Dict = None,
    ) -> models.ChangeMigratingTopicToNextStageResponse:
        """
        修改迁移中的Topic状态进入下一步
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeMigratingTopicToNextStage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeMigratingTopicToNextStageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsumerGroup(
            self,
            request: models.CreateConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.CreateConsumerGroupResponse:
        """
        创建消费组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        创建 RocketMQ 5.x 集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMQTTInsPublicEndpoint(
            self,
            request: models.CreateMQTTInsPublicEndpointRequest,
            opts: Dict = None,
    ) -> models.CreateMQTTInsPublicEndpointResponse:
        """
        为MQTT实例创建公网接入点
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMQTTInsPublicEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMQTTInsPublicEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMQTTInstance(
            self,
            request: models.CreateMQTTInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateMQTTInstanceResponse:
        """
        购买新的MQTT实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMQTTInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMQTTInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMQTTTopic(
            self,
            request: models.CreateMQTTTopicRequest,
            opts: Dict = None,
    ) -> models.CreateMQTTTopicResponse:
        """
        创建主题
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMQTTTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMQTTTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMQTTUser(
            self,
            request: models.CreateMQTTUserRequest,
            opts: Dict = None,
    ) -> models.CreateMQTTUserResponse:
        """
        添加mqtt角色
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMQTTUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMQTTUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRole(
            self,
            request: models.CreateRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRoleResponse:
        """
        添加角色
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopic(
            self,
            request: models.CreateTopicRequest,
            opts: Dict = None,
    ) -> models.CreateTopicResponse:
        """
        创建主题
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsumerGroup(
            self,
            request: models.DeleteConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteConsumerGroupResponse:
        """
        删除消费组。消费者组删除后，消费者组的所有配置和相关数据都会被清空，且无法找回。删除后，在线的消费者客户端会出现报错，建议您提前下线客户端。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        删除 RocketMQ 5.x 集群，删除前请先删除正在使用的主题、消费组和角色信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMQTTInsPublicEndpoint(
            self,
            request: models.DeleteMQTTInsPublicEndpointRequest,
            opts: Dict = None,
    ) -> models.DeleteMQTTInsPublicEndpointResponse:
        """
        删除MQTT实例的公网接入点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMQTTInsPublicEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMQTTInsPublicEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMQTTInstance(
            self,
            request: models.DeleteMQTTInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteMQTTInstanceResponse:
        """
        删除MQTT实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMQTTInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMQTTInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMQTTTopic(
            self,
            request: models.DeleteMQTTTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteMQTTTopicResponse:
        """
        删除MQTT主题
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMQTTTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMQTTTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMQTTUser(
            self,
            request: models.DeleteMQTTUserRequest,
            opts: Dict = None,
    ) -> models.DeleteMQTTUserResponse:
        """
        删除MQTT访问用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMQTTUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMQTTUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRole(
            self,
            request: models.DeleteRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteRoleResponse:
        """
        删除角色。请确保该角色相关信息不在当前代码中被使用。删除角色后，原先使用该角色进行生产或消费消息的密钥（AccessKey 和 SecretKey）将立即失效。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSmoothMigrationTask(
            self,
            request: models.DeleteSmoothMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteSmoothMigrationTaskResponse:
        """
        删除平滑迁移任务，只有被取消的任务才可删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmoothMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmoothMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopic(
            self,
            request: models.DeleteTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicResponse:
        """
        删除主题。主题删除后，主题的所有配置和相关数据都会被清空，且无法找回。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerClient(
            self,
            request: models.DescribeConsumerClientRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerClientResponse:
        """
        查询消费者客户端详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerClientResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerClientList(
            self,
            request: models.DescribeConsumerClientListRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerClientListResponse:
        """
        查询消费组下的客户端连接列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerClientList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerClientListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerGroup(
            self,
            request: models.DescribeConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerGroupResponse:
        """
        查询消费组详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerGroupList(
            self,
            request: models.DescribeConsumerGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerGroupListResponse:
        """
        获取消费组列表，Filter参数使用说明如下：

        - ConsumerGroupName 消费组名称，支持模糊查询，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        - ConsumeMessageOrderly，投递顺序性，枚举值如下：
            - true 顺序投递
            - false 并发投递

        Filters示例：
        [{ "Name": "ConsumeMessageOrderly", "Values": ["true"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerLag(
            self,
            request: models.DescribeConsumerLagRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerLagResponse:
        """
        查询指定消费组堆积数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerLag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerLagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFusionInstanceList(
            self,
            request: models.DescribeFusionInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeFusionInstanceListResponse:
        """
        查询集群列表，支持 4.x 和 5.x 集群，其中 Filters 参数使用说明如下：

        - InstanceName 集群名称，支持模糊查询，从本接口返回值或控制台获得
        - InstanceId 集群ID，精确查询，从当前接口或控制台获得
        - InstanceType 集群类型，可参考 [InstanceItem](https://cloud.tencent.com/document/api/1493/96031#InstanceItem) 数据结构，支持多选
        - Version 集群版本，枚举值如下：
            - 4 RocketMQ 4.x 集群
            - 5 RocketMQ 5.x 集群

        Filters示例：
         [{ "Name": "InstanceId", "Values": ["rmq-72mo3a9o"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFusionInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFusionInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstance(
            self,
            request: models.DescribeInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceResponse:
        """
        查询 RocketMQ 5.x 集群信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceList(
            self,
            request: models.DescribeInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceListResponse:
        """
        查询集群列表，仅支持 5.x 集群。Filters参数使用说明如下：

        - InstanceName 集群名称，支持模糊搜索
        - InstanceId 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得
        - InstanceType 集群类型，可参考 [InstanceItem](https://cloud.tencent.com/document/api/1493/96031#InstanceItem) 数据结构，支持多选
        - InstanceStatus 集群状态，可参考 [InstanceItem](https://cloud.tencent.com/document/api/1493/96031#InstanceItem) 数据结构，支持多选

        Filters示例：
        [{
            "Name": "InstanceId",
            "Values": ["rmq-72mo3a9o"]
        }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTClient(
            self,
            request: models.DescribeMQTTClientRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTClientResponse:
        """
        查询 MQTT 客户端详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTClientResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTInsPublicEndpoints(
            self,
            request: models.DescribeMQTTInsPublicEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTInsPublicEndpointsResponse:
        """
        查询MQTT实例公网接入点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTInsPublicEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTInsPublicEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTInsVPCEndpoints(
            self,
            request: models.DescribeMQTTInsVPCEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTInsVPCEndpointsResponse:
        """
        查询MQTT实例公网接入点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTInsVPCEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTInsVPCEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTInstance(
            self,
            request: models.DescribeMQTTInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTInstanceResponse:
        """
        查询实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTInstanceCert(
            self,
            request: models.DescribeMQTTInstanceCertRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTInstanceCertResponse:
        """
        查询MQTT集群证书列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTInstanceCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTInstanceCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTInstanceList(
            self,
            request: models.DescribeMQTTInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTInstanceListResponse:
        """
        获取实例列表，Filters参数使用说明如下：
        1. InstanceName, 名称模糊查询
        2. InstanceId，实例ID查询
        3. InstanceType, 实例类型查询，支持多选
        3. InstanceStatus，实例状态查询，支持多选

        当使用TagFilters查询时，Filters参数失效。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTMessage(
            self,
            request: models.DescribeMQTTMessageRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTMessageResponse:
        """
        查询MQTT消息详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTMessageList(
            self,
            request: models.DescribeMQTTMessageListRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTMessageListResponse:
        """
        查询消息列表，如查询死信，请设置ConsumerGroup参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTMessageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTMessageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTProductSKUList(
            self,
            request: models.DescribeMQTTProductSKUListRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTProductSKUListResponse:
        """
        获取产品售卖规格
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTProductSKUList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTProductSKUListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTTopic(
            self,
            request: models.DescribeMQTTTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTTopicResponse:
        """
        查询mqtt主题详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTTopicList(
            self,
            request: models.DescribeMQTTTopicListRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTTopicListResponse:
        """
        获取主题列表，Filter参数使用说明如下：

        1. TopicName，主题名称模糊搜索
        2. TopicType，主题类型查询，支持多选，可选值：Normal,Order,Transaction,DelayScheduled
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTTopicList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTTopicListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMQTTUserList(
            self,
            request: models.DescribeMQTTUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeMQTTUserListResponse:
        """
        查询用户列表，Filter参数使用说明如下：

        1. Username，用户名称模糊搜索
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMQTTUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMQTTUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessage(
            self,
            request: models.DescribeMessageRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageResponse:
        """
        查询消息详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageList(
            self,
            request: models.DescribeMessageListRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageListResponse:
        """
        查询消息列表。如果查询死信消息，请设置ConsumerGroup参数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageTrace(
            self,
            request: models.DescribeMessageTraceRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageTraceResponse:
        """
        根据消息 ID 查询消息轨迹。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageTrace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageTraceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigratingGroupStats(
            self,
            request: models.DescribeMigratingGroupStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeMigratingGroupStatsResponse:
        """
        查看迁移消费组的实时信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigratingGroupStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigratingGroupStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigratingTopicList(
            self,
            request: models.DescribeMigratingTopicListRequest,
            opts: Dict = None,
    ) -> models.DescribeMigratingTopicListResponse:
        """
        查询Topic迁移状态列表。

        Filters字段为查询过滤器，支持以下条件：
        * TopicName 主题名称，支持模糊查询
        * MigrationStatus 迁移状态，可参考[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构
        * Namespace 命名空间，仅4.x集群有效

        Filters示例：
        [{
            "Name": "TopicName",
            "Values": ["topic-a"]
        }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigratingTopicList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigratingTopicListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigratingTopicStats(
            self,
            request: models.DescribeMigratingTopicStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeMigratingTopicStatsResponse:
        """
        用于查询迁移主题的实时数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigratingTopicStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigratingTopicStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationTaskList(
            self,
            request: models.DescribeMigrationTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationTaskListResponse:
        """
        获取数据迁移任务列表，Filter参数使用说明如下：

        TaskId，根据任务ID精确查找
        InstanceId，根据实例ID精确查找
        Type，根据任务类型精确查找
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProducerList(
            self,
            request: models.DescribeProducerListRequest,
            opts: Dict = None,
    ) -> models.DescribeProducerListResponse:
        """
        查询主题关联的生产者列表信息，Filters支持以下筛选条件：
        - ClientIP，客户端IP
        - ClientID，客户端ID
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProducerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProducerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductSKUs(
            self,
            request: models.DescribeProductSKUsRequest,
            opts: Dict = None,
    ) -> models.DescribeProductSKUsResponse:
        """
        查询产品售卖规格，针对 RocketMQ 5.x 集群。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductSKUs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductSKUsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoleList(
            self,
            request: models.DescribeRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeRoleListResponse:
        """
        查询角色列表，Filter参数使用说明如下：

        - RoleName 角色名称，支持模糊搜索，从本接口返回值或控制台获得
        - AccessKey AccessKey，支持模糊搜索，从本接口返回值或控制台获得

        Filters示例：
        [{ "Name": "RoleName", "Values": ["test_role"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmoothMigrationTaskList(
            self,
            request: models.DescribeSmoothMigrationTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeSmoothMigrationTaskListResponse:
        """
        用于查询平滑迁移任务列表。

        查询参数Filters， 支持的字段如下：
        * TaskStatus, 任务状态，支持多选
        * ConnectionType，网络连接类型，支持多选，参考[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)的说明
        * InstanceId，实例ID，精确搜索
        * TaskName，任务名称，支持模糊搜索

        Filters示例：
        [{
            "Name": "InstanceId",
            "Values": ["rmq-1gzecldfg"]
        }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmoothMigrationTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmoothMigrationTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSourceClusterGroupList(
            self,
            request: models.DescribeSourceClusterGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeSourceClusterGroupListResponse:
        """
        平滑迁移过程获取源集群group列表接口。

        Filters字段为查询过滤器，支持以下字段：
        * GroupName，消费组名称，支持模糊搜索
        * Imported，是否已导入
        * ImportStatus，导入状态，参考[SourceClusterGroupConfig](https://cloud.tencent.com/document/api/1493/96031#SourceClusterGroupConfig)的说明
        * Namespace，命名空间，仅4.x集群有效

        Filters示例：
        [{
            "Name": "GroupName",
            "Values": ["group-a"]
        }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSourceClusterGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSourceClusterGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopic(
            self,
            request: models.DescribeTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicResponse:
        """
        查询主题详情，Offset和Limit参数是指订阅该主题的消费组查询分页参数，Filter参数使用说明如下：

        - ConsumerGroup 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。

        Filters示例：
        [{ "Name": "ConsumerGroup", "Values": ["test_group"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicList(
            self,
            request: models.DescribeTopicListRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicListResponse:
        """
        获取主题列表，Filter参数使用说明如下：

        - TopicName 主题名称，支持模糊搜索，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得
        - TopicType 主题类型查询，支持多选，参考 [DescribeTopic](https://cloud.tencent.com/document/api/1493/97945) 接口 TopicType 字段

        Filters示例：
         [{ "Name": "TopicName", "Values": ["test_topic"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicListByGroup(
            self,
            request: models.DescribeTopicListByGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicListByGroupResponse:
        """
        根据消费组获取主题列表，Filter参数使用说明如下：

        - TopicName 主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。

        Filters示例：
        [{ "Name": "TopicName", "Values": ["test_topic"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicListByGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicListByGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DoHealthCheckOnMigratingTopic(
            self,
            request: models.DoHealthCheckOnMigratingTopicRequest,
            opts: Dict = None,
    ) -> models.DoHealthCheckOnMigratingTopicResponse:
        """
        检查迁移中的主题是否处于正常状态，只有处于正常状态的主题，才可以进入下一个迁移阶段
        """
        
        kwargs = {}
        kwargs["action"] = "DoHealthCheckOnMigratingTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DoHealthCheckOnMigratingTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportSourceClusterConsumerGroups(
            self,
            request: models.ImportSourceClusterConsumerGroupsRequest,
            opts: Dict = None,
    ) -> models.ImportSourceClusterConsumerGroupsResponse:
        """
        导入消费者组列表
        """
        
        kwargs = {}
        kwargs["action"] = "ImportSourceClusterConsumerGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportSourceClusterConsumerGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportSourceClusterTopics(
            self,
            request: models.ImportSourceClusterTopicsRequest,
            opts: Dict = None,
    ) -> models.ImportSourceClusterTopicsResponse:
        """
        导入topic列表
        """
        
        kwargs = {}
        kwargs["action"] = "ImportSourceClusterTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportSourceClusterTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsumerGroup(
            self,
            request: models.ModifyConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyConsumerGroupResponse:
        """
        修改消费组属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        修改 RocketMQ 5.x 集群属性，仅支持修改运行中的集群。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceEndpoint(
            self,
            request: models.ModifyInstanceEndpointRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceEndpointResponse:
        """
        修改 RocketMQ 5.x 集群接入点，操作前请先确认接入点已存在。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMQTTInsPublicEndpoint(
            self,
            request: models.ModifyMQTTInsPublicEndpointRequest,
            opts: Dict = None,
    ) -> models.ModifyMQTTInsPublicEndpointResponse:
        """
        更新MQTT实例公网接入点
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMQTTInsPublicEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMQTTInsPublicEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMQTTInstance(
            self,
            request: models.ModifyMQTTInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyMQTTInstanceResponse:
        """
        修改实例属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMQTTInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMQTTInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMQTTInstanceCertBinding(
            self,
            request: models.ModifyMQTTInstanceCertBindingRequest,
            opts: Dict = None,
    ) -> models.ModifyMQTTInstanceCertBindingResponse:
        """
        更新MQTT集群绑定证书
        参数传空，则为删除证书
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMQTTInstanceCertBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMQTTInstanceCertBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMQTTTopic(
            self,
            request: models.ModifyMQTTTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyMQTTTopicResponse:
        """
        修改主题属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMQTTTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMQTTTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMQTTUser(
            self,
            request: models.ModifyMQTTUserRequest,
            opts: Dict = None,
    ) -> models.ModifyMQTTUserResponse:
        """
        修改MQTT角色
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMQTTUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMQTTUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRole(
            self,
            request: models.ModifyRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyRoleResponse:
        """
        修改角色
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
        修改主题属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveMigratingTopic(
            self,
            request: models.RemoveMigratingTopicRequest,
            opts: Dict = None,
    ) -> models.RemoveMigratingTopicResponse:
        """
        从迁移列表中移除主题，仅当主题处于初始状态时有效
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveMigratingTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveMigratingTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResendDeadLetterMessage(
            self,
            request: models.ResendDeadLetterMessageRequest,
            opts: Dict = None,
    ) -> models.ResendDeadLetterMessageResponse:
        """
        重新发送死信消息
        """
        
        kwargs = {}
        kwargs["action"] = "ResendDeadLetterMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResendDeadLetterMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetConsumerGroupOffset(
            self,
            request: models.ResetConsumerGroupOffsetRequest,
            opts: Dict = None,
    ) -> models.ResetConsumerGroupOffsetResponse:
        """
        重置消费位点
        """
        
        kwargs = {}
        kwargs["action"] = "ResetConsumerGroupOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetConsumerGroupOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackMigratingTopicStage(
            self,
            request: models.RollbackMigratingTopicStageRequest,
            opts: Dict = None,
    ) -> models.RollbackMigratingTopicStageResponse:
        """
        回滚正在迁移的主题至前一个阶段
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackMigratingTopicStage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackMigratingTopicStageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)