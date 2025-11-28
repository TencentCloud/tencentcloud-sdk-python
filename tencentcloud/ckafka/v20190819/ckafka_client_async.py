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
from tencentcloud.ckafka.v20190819 import models
from typing import Dict


class CkafkaClient(AbstractClient):
    _apiVersion = '2019-08-19'
    _endpoint = 'ckafka.tencentcloudapi.com'
    _service = 'ckafka'

    async def AuthorizeToken(
            self,
            request: models.AuthorizeTokenRequest,
            opts: Dict = None,
    ) -> models.AuthorizeTokenResponse:
        """
        给实例授权token
        """
        
        kwargs = {}
        kwargs["action"] = "AuthorizeToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AuthorizeTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateAcl(
            self,
            request: models.BatchCreateAclRequest,
            opts: Dict = None,
    ) -> models.BatchCreateAclResponse:
        """
        批量添加ACL策略
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyGroupOffsets(
            self,
            request: models.BatchModifyGroupOffsetsRequest,
            opts: Dict = None,
    ) -> models.BatchModifyGroupOffsetsResponse:
        """
        批量修改消费组offset
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyGroupOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyGroupOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyTopicAttributes(
            self,
            request: models.BatchModifyTopicAttributesRequest,
            opts: Dict = None,
    ) -> models.BatchModifyTopicAttributesResponse:
        """
        批量设置主题属性
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyTopicAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyTopicAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelAuthorizationToken(
            self,
            request: models.CancelAuthorizationTokenRequest,
            opts: Dict = None,
    ) -> models.CancelAuthorizationTokenResponse:
        """
        取消授权token
        """
        
        kwargs = {}
        kwargs["action"] = "CancelAuthorizationToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelAuthorizationTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCdcCluster(
            self,
            request: models.CheckCdcClusterRequest,
            opts: Dict = None,
    ) -> models.CheckCdcClusterResponse:
        """
        用于查询cdc-ckafka任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCdcCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCdcClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAcl(
            self,
            request: models.CreateAclRequest,
            opts: Dict = None,
    ) -> models.CreateAclResponse:
        """
        添加 ACL 策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAclRule(
            self,
            request: models.CreateAclRuleRequest,
            opts: Dict = None,
    ) -> models.CreateAclRuleResponse:
        """
        添加 ACL 规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCdcCluster(
            self,
            request: models.CreateCdcClusterRequest,
            opts: Dict = None,
    ) -> models.CreateCdcClusterResponse:
        """
        用于cdc的专用ckafka集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCdcCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCdcClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConnectResource(
            self,
            request: models.CreateConnectResourceRequest,
            opts: Dict = None,
    ) -> models.CreateConnectResourceResponse:
        """
        创建Datahub连接源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConnectResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConnectResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsumer(
            self,
            request: models.CreateConsumerRequest,
            opts: Dict = None,
    ) -> models.CreateConsumerResponse:
        """
        创建消费者组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatahubTask(
            self,
            request: models.CreateDatahubTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDatahubTaskResponse:
        """
        创建DIP转储任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatahubTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatahubTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatahubTopic(
            self,
            request: models.CreateDatahubTopicRequest,
            opts: Dict = None,
    ) -> models.CreateDatahubTopicResponse:
        """
        创建DIP主题
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatahubTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatahubTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstancePre(
            self,
            request: models.CreateInstancePreRequest,
            opts: Dict = None,
    ) -> models.CreateInstancePreResponse:
        """
        创建实例(预付费包年包月),  仅支持创建专业版实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstancePre"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstancePreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePartition(
            self,
            request: models.CreatePartitionRequest,
            opts: Dict = None,
    ) -> models.CreatePartitionResponse:
        """
        本接口用于增加主题中的分区
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePartition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePartitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePostPaidInstance(
            self,
            request: models.CreatePostPaidInstanceRequest,
            opts: Dict = None,
    ) -> models.CreatePostPaidInstanceResponse:
        """
        当前接口用来替代 CreateInstancePost 接口。创建按量计费实例。通常用于 SDK 或云 API 控制台调用接口，创建后付费 CKafka 实例。调用接口与在 CKafka 控制台购买按量付费实例效果相同。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePostPaidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePostPaidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheus(
            self,
            request: models.CreatePrometheusRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusResponse:
        """
        添加普罗米修斯监控
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoute(
            self,
            request: models.CreateRouteRequest,
            opts: Dict = None,
    ) -> models.CreateRouteResponse:
        """
        添加实例路由
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateToken(
            self,
            request: models.CreateTokenRequest,
            opts: Dict = None,
    ) -> models.CreateTokenResponse:
        """
        创建最高权限的token
        """
        
        kwargs = {}
        kwargs["action"] = "CreateToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopic(
            self,
            request: models.CreateTopicRequest,
            opts: Dict = None,
    ) -> models.CreateTopicResponse:
        """
        创建ckafka主题
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopicIpWhiteList(
            self,
            request: models.CreateTopicIpWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateTopicIpWhiteListResponse:
        """
        创建主题ip白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopicIpWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicIpWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        添加用户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAcl(
            self,
            request: models.DeleteAclRequest,
            opts: Dict = None,
    ) -> models.DeleteAclResponse:
        """
        删除ACL
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAclRule(
            self,
            request: models.DeleteAclRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAclRuleResponse:
        """
        删除ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConnectResource(
            self,
            request: models.DeleteConnectResourceRequest,
            opts: Dict = None,
    ) -> models.DeleteConnectResourceResponse:
        """
        删除Datahub连接源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConnectResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConnectResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDatahubTask(
            self,
            request: models.DeleteDatahubTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteDatahubTaskResponse:
        """
        删除Dip任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDatahubTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDatahubTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDatahubTopic(
            self,
            request: models.DeleteDatahubTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteDatahubTopicResponse:
        """
        删除DIP主题
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDatahubTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDatahubTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        删除消费组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroupSubscribeTopic(
            self,
            request: models.DeleteGroupSubscribeTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupSubscribeTopicResponse:
        """
        删除消费分组订阅的topic(消费分组必须是Empty 状态)
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroupSubscribeTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupSubscribeTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstancePost(
            self,
            request: models.DeleteInstancePostRequest,
            opts: Dict = None,
    ) -> models.DeleteInstancePostResponse:
        """
        删除后付费实例，通过调用API删除不会对连接器和任务进行关联预检查，直接进行实例销毁。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstancePost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstancePostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstancePre(
            self,
            request: models.DeleteInstancePreRequest,
            opts: Dict = None,
    ) -> models.DeleteInstancePreResponse:
        """
        删除预付费实例，该接口会对实例执行隔离并删除的动作，执行成功后实例会被直接删除销毁。通过调用API删除不会对连接器和任务进行关联预检查，直接进行实例销毁。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstancePre"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstancePreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoute(
            self,
            request: models.DeleteRouteRequest,
            opts: Dict = None,
    ) -> models.DeleteRouteResponse:
        """
        删除路由
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRouteTriggerTime(
            self,
            request: models.DeleteRouteTriggerTimeRequest,
            opts: Dict = None,
    ) -> models.DeleteRouteTriggerTimeResponse:
        """
        修改删除路由延迟触发时间
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRouteTriggerTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRouteTriggerTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopic(
            self,
            request: models.DeleteTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicResponse:
        """
        删除ckafka主题
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopicIpWhiteList(
            self,
            request: models.DeleteTopicIpWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicIpWhiteListResponse:
        """
        删除主题IP白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopicIpWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicIpWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        删除用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeACL(
            self,
            request: models.DescribeACLRequest,
            opts: Dict = None,
    ) -> models.DescribeACLResponse:
        """
        枚举ACL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAclRule(
            self,
            request: models.DescribeAclRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeAclRuleResponse:
        """
        查询ACL规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCkafkaVersion(
            self,
            request: models.DescribeCkafkaVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeCkafkaVersionResponse:
        """
        查询实例版本信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCkafkaVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCkafkaVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCkafkaZone(
            self,
            request: models.DescribeCkafkaZoneRequest,
            opts: Dict = None,
    ) -> models.DescribeCkafkaZoneResponse:
        """
        用于查看ckafka的可用区列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCkafkaZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCkafkaZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConnectResource(
            self,
            request: models.DescribeConnectResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeConnectResourceResponse:
        """
        查询Datahub连接源
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConnectResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConnectResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConnectResources(
            self,
            request: models.DescribeConnectResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeConnectResourcesResponse:
        """
        查询Datahub连接源列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConnectResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConnectResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerGroup(
            self,
            request: models.DescribeConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerGroupResponse:
        """
        查询消费分组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCvmInfo(
            self,
            request: models.DescribeCvmInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCvmInfoResponse:
        """
        本接口用于获取实例对应后端CVM信息，包括cvmId和ip等。用于专业版，标准版返回数据为空
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCvmInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCvmInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatahubGroupOffsets(
            self,
            request: models.DescribeDatahubGroupOffsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatahubGroupOffsetsResponse:
        """
        获取Datahub消费分组offset
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatahubGroupOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatahubGroupOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatahubTask(
            self,
            request: models.DescribeDatahubTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeDatahubTaskResponse:
        """
        查询Datahub任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatahubTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatahubTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatahubTasks(
            self,
            request: models.DescribeDatahubTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeDatahubTasksResponse:
        """
        查询Datahub任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatahubTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatahubTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatahubTopic(
            self,
            request: models.DescribeDatahubTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeDatahubTopicResponse:
        """
        获取DIP主题属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatahubTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatahubTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatahubTopics(
            self,
            request: models.DescribeDatahubTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatahubTopicsResponse:
        """
        查询DIP主题列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatahubTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatahubTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroup(
            self,
            request: models.DescribeGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupResponse:
        """
        枚举消费分组(精简版)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupInfo(
            self,
            request: models.DescribeGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupInfoResponse:
        """
        获取消费分组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupOffsets(
            self,
            request: models.DescribeGroupOffsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupOffsetsResponse:
        """
        获取消费分组offset
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceAttributes(
            self,
            request: models.DescribeInstanceAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceAttributesResponse:
        """
        获取实例属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        本接口（DescribeInstances）用于在用户账户下获取消息队列 CKafka 实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesDetail(
            self,
            request: models.DescribeInstancesDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesDetailResponse:
        """
        用户账户下获取实例列表详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModifyType(
            self,
            request: models.DescribeModifyTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeModifyTypeResponse:
        """
        查询实例变配类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModifyType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModifyTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheus(
            self,
            request: models.DescribePrometheusRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusResponse:
        """
        获取实例Prometheus信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegion(
            self,
            request: models.DescribeRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionResponse:
        """
        枚举地域,只支持广州地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoute(
            self,
            request: models.DescribeRouteRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteResponse:
        """
        查看路由信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupRoutes(
            self,
            request: models.DescribeSecurityGroupRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupRoutesResponse:
        """
        获取安全组路由信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatus(
            self,
            request: models.DescribeTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatusResponse:
        """
        查询任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopic(
            self,
            request: models.DescribeTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicResponse:
        """
        接口请求域名：https://ckafka.tencentcloudapi.com
        本接口（DescribeTopic）用于在用户获取消息队列 CKafka 实例的主题列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicAttributes(
            self,
            request: models.DescribeTopicAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicAttributesResponse:
        """
        获取主题属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicDetail(
            self,
            request: models.DescribeTopicDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicDetailResponse:
        """
        获取主题列表详情（仅控制台调用）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicFlowRanking(
            self,
            request: models.DescribeTopicFlowRankingRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicFlowRankingResponse:
        """
        获取Topic流量排行，消费者流量排行
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicFlowRanking"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicFlowRankingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicProduceConnection(
            self,
            request: models.DescribeTopicProduceConnectionRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicProduceConnectionResponse:
        """
        查询topic 生产端连接信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicProduceConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicProduceConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicSubscribeGroup(
            self,
            request: models.DescribeTopicSubscribeGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicSubscribeGroupResponse:
        """
        查询订阅某主题消息分组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicSubscribeGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicSubscribeGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicSyncReplica(
            self,
            request: models.DescribeTopicSyncReplicaRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicSyncReplicaResponse:
        """
        获取Topic 副本详情信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicSyncReplica"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicSyncReplicaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTypeInstances(
            self,
            request: models.DescribeTypeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeTypeInstancesResponse:
        """
        本接口（DescribeTypeInstances）用于在用户账户下获取指定类型消息队列 CKafka 实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTypeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTypeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUser(
            self,
            request: models.DescribeUserRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResponse:
        """
        查询用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FetchDatahubMessageByOffset(
            self,
            request: models.FetchDatahubMessageByOffsetRequest,
            opts: Dict = None,
    ) -> models.FetchDatahubMessageByOffsetResponse:
        """
        根据指定offset位置的消息
        """
        
        kwargs = {}
        kwargs["action"] = "FetchDatahubMessageByOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FetchDatahubMessageByOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FetchLatestDatahubMessageList(
            self,
            request: models.FetchLatestDatahubMessageListRequest,
            opts: Dict = None,
    ) -> models.FetchLatestDatahubMessageListResponse:
        """
        查询最新消息列表
        """
        
        kwargs = {}
        kwargs["action"] = "FetchLatestDatahubMessageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FetchLatestDatahubMessageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FetchMessageByOffset(
            self,
            request: models.FetchMessageByOffsetRequest,
            opts: Dict = None,
    ) -> models.FetchMessageByOffsetResponse:
        """
        根据指定offset位置的消息
        """
        
        kwargs = {}
        kwargs["action"] = "FetchMessageByOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FetchMessageByOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FetchMessageListByOffset(
            self,
            request: models.FetchMessageListByOffsetRequest,
            opts: Dict = None,
    ) -> models.FetchMessageListByOffsetResponse:
        """
        根据位点查询消息列表
        """
        
        kwargs = {}
        kwargs["action"] = "FetchMessageListByOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FetchMessageListByOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FetchMessageListByTimestamp(
            self,
            request: models.FetchMessageListByTimestampRequest,
            opts: Dict = None,
    ) -> models.FetchMessageListByTimestampResponse:
        """
        根据时间戳查询消息列表
        """
        
        kwargs = {}
        kwargs["action"] = "FetchMessageListByTimestamp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FetchMessageListByTimestampResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquireCkafkaPrice(
            self,
            request: models.InquireCkafkaPriceRequest,
            opts: Dict = None,
    ) -> models.InquireCkafkaPriceResponse:
        """
        Ckafka实例购买/续费询价
        """
        
        kwargs = {}
        kwargs["action"] = "InquireCkafkaPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquireCkafkaPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstanceScalingDown(
            self,
            request: models.InstanceScalingDownRequest,
            opts: Dict = None,
    ) -> models.InstanceScalingDownResponse:
        """
        按量实例缩容
        """
        
        kwargs = {}
        kwargs["action"] = "InstanceScalingDown"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstanceScalingDownResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAclRule(
            self,
            request: models.ModifyAclRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyAclRuleResponse:
        """
        修改ACL策略，目前只支持预设规则的是否应用到新增topic这一项的修改
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConnectResource(
            self,
            request: models.ModifyConnectResourceRequest,
            opts: Dict = None,
    ) -> models.ModifyConnectResourceResponse:
        """
        编辑Datahub连接源
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConnectResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConnectResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatahubTask(
            self,
            request: models.ModifyDatahubTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyDatahubTaskResponse:
        """
        修改Datahub任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatahubTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatahubTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatahubTopic(
            self,
            request: models.ModifyDatahubTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyDatahubTopicResponse:
        """
        修改DIP主题属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatahubTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatahubTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGroupOffsets(
            self,
            request: models.ModifyGroupOffsetsRequest,
            opts: Dict = None,
    ) -> models.ModifyGroupOffsetsResponse:
        """
        设置Groups 消费分组offset
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGroupOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGroupOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceAttributes(
            self,
            request: models.ModifyInstanceAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceAttributesResponse:
        """
        设置实例属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancePre(
            self,
            request: models.ModifyInstancePreRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancePreResponse:
        """
        预付费实例变配接口，调整磁盘，带宽,  分区
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancePre"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancePreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPassword(
            self,
            request: models.ModifyPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyPasswordResponse:
        """
        修改密码
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoutineMaintenanceTask(
            self,
            request: models.ModifyRoutineMaintenanceTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyRoutineMaintenanceTaskResponse:
        """
        设置自动化运维属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoutineMaintenanceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoutineMaintenanceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTopicAttributes(
            self,
            request: models.ModifyTopicAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyTopicAttributesResponse:
        """
        本接口用于修改主题属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopicAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseDatahubTask(
            self,
            request: models.PauseDatahubTaskRequest,
            opts: Dict = None,
    ) -> models.PauseDatahubTaskResponse:
        """
        暂停Dip任务
        """
        
        kwargs = {}
        kwargs["action"] = "PauseDatahubTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseDatahubTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewCkafkaInstance(
            self,
            request: models.RenewCkafkaInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewCkafkaInstanceResponse:
        """
        续费Ckafka实例, 目前只支持国内站包年包月实例续费
        """
        
        kwargs = {}
        kwargs["action"] = "RenewCkafkaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewCkafkaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartDatahubTask(
            self,
            request: models.RestartDatahubTaskRequest,
            opts: Dict = None,
    ) -> models.RestartDatahubTaskResponse:
        """
        Datahub任务异常时，重启Datahub任务
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDatahubTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDatahubTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeDatahubTask(
            self,
            request: models.ResumeDatahubTaskRequest,
            opts: Dict = None,
    ) -> models.ResumeDatahubTaskResponse:
        """
        恢复Dip任务
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeDatahubTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeDatahubTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendMessage(
            self,
            request: models.SendMessageRequest,
            opts: Dict = None,
    ) -> models.SendMessageResponse:
        """
        通过HTTP接入层发送消息
        """
        
        kwargs = {}
        kwargs["action"] = "SendMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeBrokerVersion(
            self,
            request: models.UpgradeBrokerVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeBrokerVersionResponse:
        """
        broker版本升级
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeBrokerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeBrokerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)