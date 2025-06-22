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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.trocket.v20230308 import models


class TrocketClient(AbstractClient):
    _apiVersion = '2023-03-08'
    _endpoint = 'trocket.tencentcloudapi.com'
    _service = 'trocket'


    def ChangeMigratingTopicToNextStage(self, request):
        """修改迁移中的Topic状态进入下一步

        :param request: Request instance for ChangeMigratingTopicToNextStage.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ChangeMigratingTopicToNextStageRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ChangeMigratingTopicToNextStageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeMigratingTopicToNextStage", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeMigratingTopicToNextStageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsumerGroup(self, request):
        """创建消费组

        :param request: Request instance for CreateConsumerGroup.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateConsumerGroupRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        """创建 RocketMQ 5.x 集群

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMQTTInsPublicEndpoint(self, request):
        """为MQTT实例创建公网接入点

        :param request: Request instance for CreateMQTTInsPublicEndpoint.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateMQTTInsPublicEndpointRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateMQTTInsPublicEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMQTTInsPublicEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMQTTInsPublicEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMQTTInstance(self, request):
        """购买新的MQTT实例

        :param request: Request instance for CreateMQTTInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateMQTTInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateMQTTInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMQTTInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMQTTInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMQTTTopic(self, request):
        """创建主题

        :param request: Request instance for CreateMQTTTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateMQTTTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateMQTTTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMQTTTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMQTTTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMQTTUser(self, request):
        """添加mqtt角色

        :param request: Request instance for CreateMQTTUser.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateMQTTUserRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateMQTTUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMQTTUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMQTTUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRole(self, request):
        """添加角色

        :param request: Request instance for CreateRole.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateRoleRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopic(self, request):
        """创建主题

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConsumerGroup(self, request):
        """删除消费组

        :param request: Request instance for DeleteConsumerGroup.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteConsumerGroupRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        """删除 RocketMQ 5.x 集群。

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMQTTInsPublicEndpoint(self, request):
        """删除MQTT实例的公网接入点

        :param request: Request instance for DeleteMQTTInsPublicEndpoint.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteMQTTInsPublicEndpointRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteMQTTInsPublicEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMQTTInsPublicEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMQTTInsPublicEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMQTTInstance(self, request):
        """删除MQTT实例

        :param request: Request instance for DeleteMQTTInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteMQTTInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteMQTTInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMQTTInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMQTTInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMQTTTopic(self, request):
        """删除MQTT主题

        :param request: Request instance for DeleteMQTTTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteMQTTTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteMQTTTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMQTTTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMQTTTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMQTTUser(self, request):
        """删除MQTT访问用户

        :param request: Request instance for DeleteMQTTUser.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteMQTTUserRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteMQTTUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMQTTUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMQTTUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRole(self, request):
        """删除角色

        :param request: Request instance for DeleteRole.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteRoleRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRole", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSmoothMigrationTask(self, request):
        """删除平滑迁移任务，只有被取消的任务才可删除

        :param request: Request instance for DeleteSmoothMigrationTask.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteSmoothMigrationTaskRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteSmoothMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSmoothMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSmoothMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopic(self, request):
        """删除主题

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerClient(self, request):
        """查询消费者客户端详情

        :param request: Request instance for DescribeConsumerClient.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerClientRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerClient", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerGroup(self, request):
        """查询消费组详情

        :param request: Request instance for DescribeConsumerGroup.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerGroupRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerGroupList(self, request):
        """获取消费组列表，Filter参数使用说明如下：

        1. ConsumerGroupName，名称模糊查询
        2. ConsumeMessageOrderly，投递顺序性。"true":顺序投递；"false":并发投递

        :param request: Request instance for DescribeConsumerGroupList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerGroupListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerLag(self, request):
        """查询指定消费组堆积数。

        :param request: Request instance for DescribeConsumerLag.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerLagRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeConsumerLagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerLag", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerLagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFusionInstanceList(self, request):
        """查询集群列表，支持 4.x 和 5.x 集群，其中 Filters 参数使用说明如下：
        1. InstanceName, 名称模糊查询
        2. InstanceId，集群ID查询
        3. InstanceType, 集群类型查询，支持多选
        4. Version，集群版本查询

        :param request: Request instance for DescribeFusionInstanceList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeFusionInstanceListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeFusionInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFusionInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFusionInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstance(self, request):
        """查询 RocketMQ 5.x 集群信息。

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceList(self, request):
        """查询集群列表，仅支持 5.x 集群。Filters参数使用说明如下：
        1. InstanceName, 名称模糊查询
        2. InstanceId，集群ID查询
        3. InstanceType, 集群类型查询，支持多选
        3. InstanceStatus，集群状态查询，支持多选

        当使用TagFilters查询时，Filters参数失效。

        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeInstanceListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTClient(self, request):
        """查询 MQTT 客户端详情

        :param request: Request instance for DescribeMQTTClient.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTClientRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTClient", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTInsPublicEndpoints(self, request):
        """查询MQTT实例公网接入点

        :param request: Request instance for DescribeMQTTInsPublicEndpoints.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTInsPublicEndpointsRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTInsPublicEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTInsPublicEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTInsPublicEndpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTInsVPCEndpoints(self, request):
        """查询MQTT实例公网接入点

        :param request: Request instance for DescribeMQTTInsVPCEndpoints.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTInsVPCEndpointsRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTInsVPCEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTInsVPCEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTInsVPCEndpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTInstance(self, request):
        """查询实例信息

        :param request: Request instance for DescribeMQTTInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTInstanceCert(self, request):
        """查询MQTT集群证书列表

        :param request: Request instance for DescribeMQTTInstanceCert.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTInstanceCertRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTInstanceCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTInstanceCert", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTInstanceCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTInstanceList(self, request):
        """获取实例列表，Filters参数使用说明如下：
        1. InstanceName, 名称模糊查询
        2. InstanceId，实例ID查询
        3. InstanceType, 实例类型查询，支持多选
        3. InstanceStatus，实例状态查询，支持多选

        当使用TagFilters查询时，Filters参数失效。

        :param request: Request instance for DescribeMQTTInstanceList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTInstanceListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTMessage(self, request):
        """查询MQTT消息详情

        :param request: Request instance for DescribeMQTTMessage.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTMessageRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTMessage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTMessageList(self, request):
        """查询消息列表，如查询死信，请设置ConsumerGroup参数

        :param request: Request instance for DescribeMQTTMessageList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTMessageListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTMessageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTMessageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTMessageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTProductSKUList(self, request):
        """获取产品售卖规格

        :param request: Request instance for DescribeMQTTProductSKUList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTProductSKUListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTProductSKUListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTProductSKUList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTProductSKUListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTTopic(self, request):
        """查询mqtt主题详情

        :param request: Request instance for DescribeMQTTTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTTopicList(self, request):
        """获取主题列表，Filter参数使用说明如下：

        1. TopicName，主题名称模糊搜索
        2. TopicType，主题类型查询，支持多选，可选值：Normal,Order,Transaction,DelayScheduled

        :param request: Request instance for DescribeMQTTTopicList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTTopicListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTTopicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMQTTUserList(self, request):
        """查询用户列表，Filter参数使用说明如下：

        1. Username，用户名称模糊搜索

        :param request: Request instance for DescribeMQTTUserList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTUserListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMQTTUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMQTTUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMQTTUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessage(self, request):
        """查询消息详情

        :param request: Request instance for DescribeMessage.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageList(self, request):
        """查询消息列表。如果查询死信消息，请设置ConsumerGroup参数。

        :param request: Request instance for DescribeMessageList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageTrace(self, request):
        """根据消息 ID 查询消息轨迹。

        :param request: Request instance for DescribeMessageTrace.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageTraceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMessageTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageTrace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigratingGroupStats(self, request):
        """查看迁移消费组的实时信息

        :param request: Request instance for DescribeMigratingGroupStats.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingGroupStatsRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingGroupStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigratingGroupStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigratingGroupStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigratingTopicList(self, request):
        """查询Topic迁移状态列表

        查询过滤器，支持TopicName、MigrationStatus、Namespace查询

        :param request: Request instance for DescribeMigratingTopicList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingTopicListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigratingTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigratingTopicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigratingTopicStats(self, request):
        """用于查询迁移主题的实时数据

        :param request: Request instance for DescribeMigratingTopicStats.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingTopicStatsRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMigratingTopicStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigratingTopicStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigratingTopicStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationTaskList(self, request):
        """获取数据迁移任务列表，Filter参数使用说明如下：

        TaskId，根据任务ID精确查找
        InstanceId，根据实例ID精确查找
        Type，根据任务类型精确查找

        :param request: Request instance for DescribeMigrationTaskList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeMigrationTaskListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeMigrationTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductSKUs(self, request):
        """查询产品售卖规格，针对 RocketMQ 5.x 集群。

        :param request: Request instance for DescribeProductSKUs.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeProductSKUsRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeProductSKUsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductSKUs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductSKUsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoleList(self, request):
        """查询角色列表，Filter参数使用说明如下：

        1. RoleName，角色名称模糊搜索
        2. AccessKey，AccessKey模糊搜索

        :param request: Request instance for DescribeRoleList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeRoleListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeRoleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSmoothMigrationTaskList(self, request):
        """用于查询平滑迁移任务列表

        查询参数Filters， 支持的字段如下：
        TaskStatus, 支持多选
        ConnectionType，支持多选
        InstanceId，精确搜索
        TaskName，支持模糊搜索

        :param request: Request instance for DescribeSmoothMigrationTaskList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeSmoothMigrationTaskListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeSmoothMigrationTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmoothMigrationTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmoothMigrationTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSourceClusterGroupList(self, request):
        """平滑迁移过程获取源集群group列表接口

        查询过滤器，支持字段
        GroupName，消费组名称模糊搜索
        Imported，是否已导入
        ImportStatus，导入状态
        Namespace，命名空间

        :param request: Request instance for DescribeSourceClusterGroupList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeSourceClusterGroupListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeSourceClusterGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSourceClusterGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSourceClusterGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopic(self, request):
        """查询主题详情，Offset和Limit参数是指订阅该主题的消费组查询分页参数，Filter参数使用说明如下：

        ConsumerGroup，消费组名称过滤

        :param request: Request instance for DescribeTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicList(self, request):
        """获取主题列表，Filter参数使用说明如下：

        1. TopicName，主题名称模糊搜索
        2. TopicType，主题类型查询，支持多选，可选值：Normal,Order,Transaction,DelayScheduled

        :param request: Request instance for DescribeTopicList.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicListRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicListByGroup(self, request):
        """根据消费组获取主题列表，Filter参数使用说明如下：

        TopicName，主题名称过滤

        :param request: Request instance for DescribeTopicListByGroup.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicListByGroupRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicListByGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicListByGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicListByGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DoHealthCheckOnMigratingTopic(self, request):
        """检查迁移中的主题是否处于正常状态，只有处于正常状态的主题，才可以进入下一个迁移阶段

        :param request: Request instance for DoHealthCheckOnMigratingTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DoHealthCheckOnMigratingTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DoHealthCheckOnMigratingTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DoHealthCheckOnMigratingTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DoHealthCheckOnMigratingTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportSourceClusterConsumerGroups(self, request):
        """导入消费者组列表

        :param request: Request instance for ImportSourceClusterConsumerGroups.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ImportSourceClusterConsumerGroupsRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ImportSourceClusterConsumerGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportSourceClusterConsumerGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ImportSourceClusterConsumerGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportSourceClusterTopics(self, request):
        """导入topic列表

        :param request: Request instance for ImportSourceClusterTopics.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ImportSourceClusterTopicsRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ImportSourceClusterTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportSourceClusterTopics", params, headers=headers)
            response = json.loads(body)
            model = models.ImportSourceClusterTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsumerGroup(self, request):
        """修改消费组属性

        :param request: Request instance for ModifyConsumerGroup.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyConsumerGroupRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        """修改 RocketMQ 5.x 集群属性。

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceEndpoint(self, request):
        """修改 RocketMQ 5.x 集群接入点。

        :param request: Request instance for ModifyInstanceEndpoint.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyInstanceEndpointRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyInstanceEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMQTTInsPublicEndpoint(self, request):
        """更新MQTT实例公网接入点

        :param request: Request instance for ModifyMQTTInsPublicEndpoint.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyMQTTInsPublicEndpointRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyMQTTInsPublicEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMQTTInsPublicEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMQTTInsPublicEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMQTTInstance(self, request):
        """修改实例属性

        :param request: Request instance for ModifyMQTTInstance.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyMQTTInstanceRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyMQTTInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMQTTInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMQTTInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMQTTInstanceCertBinding(self, request):
        """更新MQTT集群绑定证书
        参数传空，则为删除证书

        :param request: Request instance for ModifyMQTTInstanceCertBinding.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyMQTTInstanceCertBindingRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyMQTTInstanceCertBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMQTTInstanceCertBinding", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMQTTInstanceCertBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMQTTTopic(self, request):
        """修改主题属性

        :param request: Request instance for ModifyMQTTTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyMQTTTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyMQTTTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMQTTTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMQTTTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMQTTUser(self, request):
        """修改MQTT角色

        :param request: Request instance for ModifyMQTTUser.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyMQTTUserRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyMQTTUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMQTTUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMQTTUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRole(self, request):
        """修改角色

        :param request: Request instance for ModifyRole.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyRoleRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTopic(self, request):
        """修改主题属性

        :param request: Request instance for ModifyTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ModifyTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ModifyTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveMigratingTopic(self, request):
        """从迁移列表中移除主题，仅当主题处于初始状态时有效

        :param request: Request instance for RemoveMigratingTopic.
        :type request: :class:`tencentcloud.trocket.v20230308.models.RemoveMigratingTopicRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.RemoveMigratingTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveMigratingTopic", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveMigratingTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResendDeadLetterMessage(self, request):
        """重新发送死信消息

        :param request: Request instance for ResendDeadLetterMessage.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ResendDeadLetterMessageRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ResendDeadLetterMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResendDeadLetterMessage", params, headers=headers)
            response = json.loads(body)
            model = models.ResendDeadLetterMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetConsumerGroupOffset(self, request):
        """重置消费位点

        :param request: Request instance for ResetConsumerGroupOffset.
        :type request: :class:`tencentcloud.trocket.v20230308.models.ResetConsumerGroupOffsetRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ResetConsumerGroupOffsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetConsumerGroupOffset", params, headers=headers)
            response = json.loads(body)
            model = models.ResetConsumerGroupOffsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackMigratingTopicStage(self, request):
        """回滚正在迁移的主题至前一个阶段

        :param request: Request instance for RollbackMigratingTopicStage.
        :type request: :class:`tencentcloud.trocket.v20230308.models.RollbackMigratingTopicStageRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.RollbackMigratingTopicStageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackMigratingTopicStage", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackMigratingTopicStageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))