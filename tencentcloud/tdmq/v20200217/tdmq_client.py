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
from tencentcloud.tdmq.v20200217 import models


class TdmqClient(AbstractClient):
    _apiVersion = '2020-02-17'
    _endpoint = 'tdmq.tencentcloudapi.com'
    _service = 'tdmq'


    def AcknowledgeMessage(self, request):
        """根据提供的 MessageID 确认指定 topic 中的消息

        :param request: Request instance for AcknowledgeMessage.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.AcknowledgeMessageRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.AcknowledgeMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcknowledgeMessage", params, headers=headers)
            response = json.loads(body)
            model = models.AcknowledgeMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearCmqQueue(self, request):
        """清空cmq消息队列中的消息

        :param request: Request instance for ClearCmqQueue.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ClearCmqQueueRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ClearCmqQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearCmqQueue", params, headers=headers)
            response = json.loads(body)
            model = models.ClearCmqQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearCmqSubscriptionFilterTags(self, request):
        """清空订阅者消息标签

        :param request: Request instance for ClearCmqSubscriptionFilterTags.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ClearCmqSubscriptionFilterTagsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ClearCmqSubscriptionFilterTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearCmqSubscriptionFilterTags", params, headers=headers)
            response = json.loads(body)
            model = models.ClearCmqSubscriptionFilterTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        """创建用户的集群

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCmqQueue(self, request):
        """创建cmq队列接口

        :param request: Request instance for CreateCmqQueue.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqQueueRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCmqQueue", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCmqQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCmqSubscribe(self, request):
        """创建cmq订阅接口

        :param request: Request instance for CreateCmqSubscribe.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqSubscribeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCmqSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCmqSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCmqTopic(self, request):
        """创建cmq主题

        :param request: Request instance for CreateCmqTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCmqTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCmqTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEnvironment(self, request):
        """用于在用户账户下创建消息队列 Tdmq 命名空间

        :param request: Request instance for CreateEnvironment.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateEnvironmentRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEnvironmentRole(self, request):
        """创建环境角色授权

        :param request: Request instance for CreateEnvironmentRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateEnvironmentRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateEnvironmentRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnvironmentRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnvironmentRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProCluster(self, request):
        """创建专业集群——预付费，仅通过api调用

        :param request: Request instance for CreateProCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateProClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateProClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQBinding(self, request):
        """创建RabbitMQ路由关系

        :param request: Request instance for CreateRabbitMQBinding.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQBindingRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQBinding", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQUser(self, request):
        """创建RabbitMQ的用户

        :param request: Request instance for CreateRabbitMQUser.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQUserRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQVipInstance(self, request):
        """创建RabbitMQ专享版实例

        :param request: Request instance for CreateRabbitMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQVirtualHost(self, request):
        """创建RabbitMQ的vhost

        :param request: Request instance for CreateRabbitMQVirtualHost.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQVirtualHostRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRocketMQCluster(self, request):
        """此接口用于创建一个RocketMQ集群

        :param request: Request instance for CreateRocketMQCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRocketMQClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRocketMQEnvironmentRole(self, request):
        """创建环境角色授权

        :param request: Request instance for CreateRocketMQEnvironmentRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQEnvironmentRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQEnvironmentRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQEnvironmentRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRocketMQEnvironmentRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRocketMQGroup(self, request):
        """创建RocketMQ消费组

        :param request: Request instance for CreateRocketMQGroup.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQGroupRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRocketMQGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRocketMQNamespace(self, request):
        """创建RocketMQ命名空间

        :param request: Request instance for CreateRocketMQNamespace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQNamespaceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRocketMQNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRocketMQRole(self, request):
        """创建角色

        :param request: Request instance for CreateRocketMQRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRocketMQRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRocketMQTopic(self, request):
        """创建RocketMQ主题

        :param request: Request instance for CreateRocketMQTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRocketMQTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRocketMQVipInstance(self, request):
        """创建RocketMQ专享实例

        :param request: Request instance for CreateRocketMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRocketMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRole(self, request):
        """创建角色

        :param request: Request instance for CreateRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRoleResponse`

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


    def CreateSubscription(self, request):
        """创建一个主题的订阅关系

        :param request: Request instance for CreateSubscription.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateSubscriptionRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopic(self, request):
        """新增指定分区、类型的消息主题

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateTopicResponse`

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


    def DeleteCluster(self, request):
        """删除集群

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCmqQueue(self, request):
        """删除cmq队列

        :param request: Request instance for DeleteCmqQueue.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqQueueRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCmqQueue", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCmqQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCmqSubscribe(self, request):
        """删除cmq订阅

        :param request: Request instance for DeleteCmqSubscribe.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqSubscribeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCmqSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCmqSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCmqTopic(self, request):
        """删除cmq主题

        :param request: Request instance for DeleteCmqTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCmqTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCmqTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEnvironmentRoles(self, request):
        """删除环境角色授权。

        :param request: Request instance for DeleteEnvironmentRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteEnvironmentRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteEnvironmentRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEnvironmentRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEnvironmentRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEnvironments(self, request):
        """批量删除租户下的命名空间

        :param request: Request instance for DeleteEnvironments.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteEnvironmentsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProCluster(self, request):
        """删除专业集群——预付费，仅通过API 调用

        :param request: Request instance for DeleteProCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteProClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteProClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQBinding(self, request):
        """解绑RabbitMQ路由关系

        :param request: Request instance for DeleteRabbitMQBinding.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQBindingRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQBinding", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQPermission(self, request):
        """删除RabbitMQ的权限

        :param request: Request instance for DeleteRabbitMQPermission.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQPermissionRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQPermission", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQUser(self, request):
        """删除RabbitMQ的用户

        :param request: Request instance for DeleteRabbitMQUser.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQUserRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQVipInstance(self, request):
        """删除RabbitMQ专享版实例

        :param request: Request instance for DeleteRabbitMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQVirtualHost(self, request):
        """删除RabbitMQ的vhost

        :param request: Request instance for DeleteRabbitMQVirtualHost.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQVirtualHostRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRocketMQCluster(self, request):
        """删除RocketMQ集群

        :param request: Request instance for DeleteRocketMQCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRocketMQClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRocketMQEnvironmentRoles(self, request):
        """删除环境角色授权。

        :param request: Request instance for DeleteRocketMQEnvironmentRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQEnvironmentRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQEnvironmentRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQEnvironmentRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRocketMQEnvironmentRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRocketMQGroup(self, request):
        """删除RocketMQ消费组

        :param request: Request instance for DeleteRocketMQGroup.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQGroupRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRocketMQGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRocketMQNamespace(self, request):
        """删除RocketMQ命名空间

        :param request: Request instance for DeleteRocketMQNamespace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQNamespaceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRocketMQNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRocketMQRoles(self, request):
        """删除角色，支持批量。

        :param request: Request instance for DeleteRocketMQRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRocketMQRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRocketMQTopic(self, request):
        """删除RocketMQ主题

        :param request: Request instance for DeleteRocketMQTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRocketMQTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRocketMQVipInstance(self, request):
        """删除RocketMQ专享实例

        :param request: Request instance for DeleteRocketMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRocketMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoles(self, request):
        """删除角色，支持批量。

        :param request: Request instance for DeleteRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSubscriptions(self, request):
        """删除订阅关系

        :param request: Request instance for DeleteSubscriptions.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteSubscriptionsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteSubscriptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSubscriptions", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSubscriptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopics(self, request):
        """批量删除topics

        :param request: Request instance for DeleteTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAMQPClusters(self, request):
        """历史原因，该接口位于tdmq-manager，目前rabbitmq产品没有使用该接口，当前使用的是DescribeRabbitMQVipInstances。不过从调用链上看，线网还有请求流程，所以走预下线流程。

        获取amqp集群列表

        :param request: Request instance for DescribeAMQPClusters.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeAMQPClustersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeAMQPClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAMQPClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAMQPClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllTenants(self, request):
        """获取某个租户的虚拟集群列表

        :param request: Request instance for DescribeAllTenants.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeAllTenantsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeAllTenantsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllTenants", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllTenantsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBindClusters(self, request):
        """获取用户绑定的专享集群列表

        :param request: Request instance for DescribeBindClusters.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeBindClustersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeBindClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBindClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBindVpcs(self, request):
        """获取租户VPC绑定关系

        :param request: Request instance for DescribeBindVpcs.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeBindVpcsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeBindVpcsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindVpcs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBindVpcsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterDetail(self, request):
        """获取集群的详细信息

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusters(self, request):
        """获取集群列表

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCmqQueueDetail(self, request):
        """查询cmq队列详情

        :param request: Request instance for DescribeCmqQueueDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqQueueDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqQueueDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqQueueDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCmqQueueDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCmqQueues(self, request):
        """查询cmq全量队列

        :param request: Request instance for DescribeCmqQueues.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqQueuesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqQueuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqQueues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCmqQueuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCmqSubscriptionDetail(self, request):
        """查询cmq订阅详情

        :param request: Request instance for DescribeCmqSubscriptionDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqSubscriptionDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqSubscriptionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqSubscriptionDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCmqSubscriptionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCmqTopicDetail(self, request):
        """查询cmq主题详情

        :param request: Request instance for DescribeCmqTopicDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqTopicDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqTopicDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqTopicDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCmqTopicDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCmqTopics(self, request):
        """枚举cmq全量主题

        :param request: Request instance for DescribeCmqTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCmqTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironmentAttributes(self, request):
        """获取指定命名空间的属性

        :param request: Request instance for DescribeEnvironmentAttributes.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentAttributesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironmentAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironmentRoles(self, request):
        """获取命名空间角色列表

        :param request: Request instance for DescribeEnvironmentRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironmentRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironments(self, request):
        """获取租户下命名空间列表

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMqMsgTrace(self, request):
        """查询消息轨迹

        :param request: Request instance for DescribeMqMsgTrace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeMqMsgTraceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeMqMsgTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMqMsgTrace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMqMsgTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMsg(self, request):
        """消息详情

        :param request: Request instance for DescribeMsg.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeMsgRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMsgTrace(self, request):
        """查询消息轨迹

        :param request: Request instance for DescribeMsgTrace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeMsgTraceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeMsgTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMsgTrace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMsgTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNamespaceBundlesOpt(self, request):
        """运营端获取命名空间bundle列表

        :param request: Request instance for DescribeNamespaceBundlesOpt.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeNamespaceBundlesOptRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeNamespaceBundlesOptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNamespaceBundlesOpt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNamespaceBundlesOptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeHealthOpt(self, request):
        """运营端获节点健康状态

        :param request: Request instance for DescribeNodeHealthOpt.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeNodeHealthOptRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeNodeHealthOptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeHealthOpt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeHealthOptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublisherSummary(self, request):
        """获取消息生产概览信息

        :param request: Request instance for DescribePublisherSummary.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribePublisherSummaryRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribePublisherSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublisherSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublisherSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublishers(self, request):
        """获取生产者信息列表

        :param request: Request instance for DescribePublishers.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribePublishersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribePublishersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublishers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublishersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePulsarProInstanceDetail(self, request):
        """获取Pulsar专业版集群实例信息

        :param request: Request instance for DescribePulsarProInstanceDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribePulsarProInstanceDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribePulsarProInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePulsarProInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePulsarProInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePulsarProInstances(self, request):
        """查询用户已购的Pulsar专业版实例列表

        :param request: Request instance for DescribePulsarProInstances.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribePulsarProInstancesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribePulsarProInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePulsarProInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePulsarProInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQBindings(self, request):
        """查询RabbitMQ路由关系列表

        :param request: Request instance for DescribeRabbitMQBindings.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQBindingsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQBindings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQExchanges(self, request):
        """查询RabbitMQ exchange 列表

        :param request: Request instance for DescribeRabbitMQExchanges.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQExchangesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQExchangesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQExchanges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQExchangesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQNodeList(self, request):
        """RabbitMQ专享版查询节点列表

        :param request: Request instance for DescribeRabbitMQNodeList.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQNodeListRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQNodeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQNodeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQNodeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQPermission(self, request):
        """查询RabbitMQ权限列表

        :param request: Request instance for DescribeRabbitMQPermission.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQPermissionRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQPermission", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQQueueDetail(self, request):
        """查询RabbitMQ队列详情

        :param request: Request instance for DescribeRabbitMQQueueDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQQueueDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQQueueDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQQueueDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQQueueDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQQueues(self, request):
        """查询RabbitMQ队列列表

        :param request: Request instance for DescribeRabbitMQQueues.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQQueuesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQQueuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQQueues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQQueuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQUser(self, request):
        """查询RabbitMQ用户列表

        :param request: Request instance for DescribeRabbitMQUser.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQUserRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQVipInstance(self, request):
        """获取单个RabbitMQ专享实例信息

        :param request: Request instance for DescribeRabbitMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQVipInstances(self, request):
        """查询用户已购的RabbitMQ专享实例列表

        :param request: Request instance for DescribeRabbitMQVipInstances.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVipInstancesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVipInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQVipInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQVipInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQVirtualHost(self, request):
        """查询RabbitMQ vhost列表

        :param request: Request instance for DescribeRabbitMQVirtualHost.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVirtualHostRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQCluster(self, request):
        """获取单个RocketMQ集群信息

        :param request: Request instance for DescribeRocketMQCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQClusters(self, request):
        """获取RocketMQ集群列表

        :param request: Request instance for DescribeRocketMQClusters.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQClustersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQConsumeStats(self, request):
        """获取消费详情列表

        :param request: Request instance for DescribeRocketMQConsumeStats.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQConsumeStatsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQConsumeStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQConsumeStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQConsumeStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQConsumerConnectionDetail(self, request):
        """获取在线消费端详情

        :param request: Request instance for DescribeRocketMQConsumerConnectionDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQConsumerConnectionDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQConsumerConnectionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQConsumerConnectionDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQConsumerConnectionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQConsumerConnections(self, request):
        """获取指定消费组下当前客户端的连接情况

        :param request: Request instance for DescribeRocketMQConsumerConnections.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQConsumerConnectionsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQConsumerConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQConsumerConnections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQConsumerConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQEnvironmentRoles(self, request):
        """获取命名空间角色列表

        :param request: Request instance for DescribeRocketMQEnvironmentRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQEnvironmentRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQEnvironmentRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQEnvironmentRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQEnvironmentRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQGroups(self, request):
        """获取RocketMQ消费组列表

        :param request: Request instance for DescribeRocketMQGroups.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQGroupsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQMigratingTopicList(self, request):
        """查询Topic迁移状态列表，源集群和目标集群客户端数量信息需要配合DescribeRocketMQSmoothMigrationTaskTopicInsNum接口查询

        :param request: Request instance for DescribeRocketMQMigratingTopicList.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQMigratingTopicListRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQMigratingTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQMigratingTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQMigratingTopicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQMsg(self, request):
        """rocketmq消息详情

        :param request: Request instance for DescribeRocketMQMsg.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQMsgRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQMsgTrace(self, request):
        """查询消息轨迹

        :param request: Request instance for DescribeRocketMQMsgTrace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQMsgTraceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQMsgTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQMsgTrace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQMsgTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQNamespaces(self, request):
        """获取RocketMQ命名空间列表

        :param request: Request instance for DescribeRocketMQNamespaces.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQNamespacesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQPublicAccessMonitorData(self, request):
        """从腾讯云可观测平台拉取公网指标监控数据，目前仅支持客户端到 LB 的入带宽和出宽带指标。

        :param request: Request instance for DescribeRocketMQPublicAccessMonitorData.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQPublicAccessMonitorDataRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQPublicAccessMonitorDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQPublicAccessMonitorData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQPublicAccessMonitorDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQPublicAccessPoint(self, request):
        """接口用于查询RocketMQ实例的公网接入信息

        :param request: Request instance for DescribeRocketMQPublicAccessPoint.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQPublicAccessPointRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQPublicAccessPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQPublicAccessPoint", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQPublicAccessPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQRoles(self, request):
        """获取角色列表

        :param request: Request instance for DescribeRocketMQRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQSmoothMigrationTask(self, request):
        """用于获取RocketMQ平滑迁移任务详情

        :param request: Request instance for DescribeRocketMQSmoothMigrationTask.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQSmoothMigrationTaskRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQSmoothMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQSmoothMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQSmoothMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQSmoothMigrationTaskList(self, request):
        """用于查询RocketMQ平滑迁移任务列表

        :param request: Request instance for DescribeRocketMQSmoothMigrationTaskList.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQSmoothMigrationTaskListRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQSmoothMigrationTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQSmoothMigrationTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQSmoothMigrationTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQSourceClusterGroupList(self, request):
        """平滑迁移过程获取源集群group列表接口

        :param request: Request instance for DescribeRocketMQSourceClusterGroupList.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQSourceClusterGroupListRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQSourceClusterGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQSourceClusterGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQSourceClusterGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQSourceClusterTopicList(self, request):
        """平滑迁移过程获取源集群topic列表接口

        :param request: Request instance for DescribeRocketMQSourceClusterTopicList.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQSourceClusterTopicListRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQSourceClusterTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQSourceClusterTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQSourceClusterTopicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQSubscriptions(self, request):
        """用于获取RocketMQ消费组订阅关系数据

        :param request: Request instance for DescribeRocketMQSubscriptions.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQSubscriptionsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQSubscriptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQSubscriptions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQSubscriptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopUsages(self, request):
        """用于获取RocketMQ指标排序列表，比如集群实例下占用存储空间最多的主题排序。

        :param request: Request instance for DescribeRocketMQTopUsages.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopUsagesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopUsagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopUsages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopUsagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopicMsgs(self, request):
        """rocketmq 消息查询

        :param request: Request instance for DescribeRocketMQTopicMsgs.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicMsgsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicMsgsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopicMsgs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopicMsgsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopicStats(self, request):
        """获取Topic生产详情列表

        :param request: Request instance for DescribeRocketMQTopicStats.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicStatsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopicStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopicStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopics(self, request):
        """获取RocketMQ主题列表

        :param request: Request instance for DescribeRocketMQTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopicsByGroup(self, request):
        """获取指定消费组下订阅的主题列表

        :param request: Request instance for DescribeRocketMQTopicsByGroup.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicsByGroupRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicsByGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopicsByGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopicsByGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQVipInstanceDetail(self, request):
        """获取单个RocketMQ专享集群信息

        :param request: Request instance for DescribeRocketMQVipInstanceDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQVipInstanceDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQVipInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQVipInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQVipInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQVipInstances(self, request):
        """查询用户已购的RocketMQ专享实例列表

        :param request: Request instance for DescribeRocketMQVipInstances.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQVipInstancesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQVipInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQVipInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQVipInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoles(self, request):
        """获取角色列表

        :param request: Request instance for DescribeRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubscriptions(self, request):
        """查询指定环境和主题下的订阅者列表

        :param request: Request instance for DescribeSubscriptions.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeSubscriptionsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeSubscriptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubscriptions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubscriptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicMsgs(self, request):
        """消息查询

        :param request: Request instance for DescribeTopicMsgs.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeTopicMsgsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeTopicMsgsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicMsgs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicMsgsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopics(self, request):
        """获取环境下主题列表

        :param request: Request instance for DescribeTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRocketMQMessageDetail(self, request):
        """导出RocketMQ消息详情

        :param request: Request instance for ExportRocketMQMessageDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ExportRocketMQMessageDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ExportRocketMQMessageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRocketMQMessageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRocketMQMessageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTopicList(self, request):
        """获取环境下主题列表

        :param request: Request instance for GetTopicList.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.GetTopicListRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.GetTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.GetTopicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportRocketMQConsumerGroups(self, request):
        """输入迁移任务id和要导入的Group，导入后台

        :param request: Request instance for ImportRocketMQConsumerGroups.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ImportRocketMQConsumerGroupsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ImportRocketMQConsumerGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportRocketMQConsumerGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ImportRocketMQConsumerGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportRocketMQTopics(self, request):
        """导入topic列表

        :param request: Request instance for ImportRocketMQTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ImportRocketMQTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ImportRocketMQTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportRocketMQTopics", params, headers=headers)
            response = json.loads(body)
            model = models.ImportRocketMQTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAMQPCluster(self, request):
        """历史原因，该接口位于tdmq-manager，目前rabbitmq产品没有使用该接口，当前使用的是ModifyRabbitMQVipInstance。不过从调用链上看，线网还有请求流程，所以走预下线流程。

        更新Amqp集群信息

        :param request: Request instance for ModifyAMQPCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyAMQPClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyAMQPClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAMQPCluster", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAMQPClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCluster(self, request):
        """更新集群信息

        :param request: Request instance for ModifyCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCluster", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCmqQueueAttribute(self, request):
        """修改cmq队列属性

        :param request: Request instance for ModifyCmqQueueAttribute.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqQueueAttributeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqQueueAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCmqQueueAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCmqQueueAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCmqSubscriptionAttribute(self, request):
        """修改cmq订阅属性

        :param request: Request instance for ModifyCmqSubscriptionAttribute.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqSubscriptionAttributeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqSubscriptionAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCmqSubscriptionAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCmqSubscriptionAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCmqTopicAttribute(self, request):
        """修改cmq主题属性

        :param request: Request instance for ModifyCmqTopicAttribute.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqTopicAttributeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqTopicAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCmqTopicAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCmqTopicAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnvironmentAttributes(self, request):
        """修改指定命名空间的属性值

        :param request: Request instance for ModifyEnvironmentAttributes.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyEnvironmentAttributesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyEnvironmentAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnvironmentAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnvironmentAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnvironmentRole(self, request):
        """修改环境角色授权。

        :param request: Request instance for ModifyEnvironmentRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyEnvironmentRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyEnvironmentRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnvironmentRole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnvironmentRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPublicNetworkAccessPoint(self, request):
        """RabbitMQ专享版修改公网管控台，vpc15672开关

        :param request: Request instance for ModifyPublicNetworkAccessPoint.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyPublicNetworkAccessPointRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyPublicNetworkAccessPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublicNetworkAccessPoint", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPublicNetworkAccessPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPublicNetworkSecurityPolicy(self, request):
        """修改pulsar专业版公网安全策略

        :param request: Request instance for ModifyPublicNetworkSecurityPolicy.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyPublicNetworkSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyPublicNetworkSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublicNetworkSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPublicNetworkSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQPermission(self, request):
        """修改RabbitMQ的权限

        :param request: Request instance for ModifyRabbitMQPermission.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQPermissionRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQPermission", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQUser(self, request):
        """修改RabbitMQ的用户

        :param request: Request instance for ModifyRabbitMQUser.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQUserRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQVipInstance(self, request):
        """修改RabbitMQ专享版实例

        :param request: Request instance for ModifyRabbitMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQVirtualHost(self, request):
        """修改RabbitMQ的vhost

        :param request: Request instance for ModifyRabbitMQVirtualHost.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQVirtualHostRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQCluster(self, request):
        """更新RocketMQ集群信息

        :param request: Request instance for ModifyRocketMQCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQCluster", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQEnvironmentRole(self, request):
        """修改环境角色授权。

        :param request: Request instance for ModifyRocketMQEnvironmentRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQEnvironmentRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQEnvironmentRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQEnvironmentRole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQEnvironmentRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQGroup(self, request):
        """更新RocketMQ消费组信息

        :param request: Request instance for ModifyRocketMQGroup.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQGroupRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQInstance(self, request):
        """修改RocketMQ专享实例

        :param request: Request instance for ModifyRocketMQInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQInstanceSpec(self, request):
        """本API用于修改RocketMQ专享实例配置，可以支持实例规格、节点数和存储的升配和实例规格的降配。本API发起订单并成功支付后进入实例配置变更的流程，可通过DescribeRocketMQVipInstances查询实例是否已变更完成。

        :param request: Request instance for ModifyRocketMQInstanceSpec.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQInstanceSpecRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQInstanceSpec", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQInstanceSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQNamespace(self, request):
        """更新RocketMQ命名空间

        :param request: Request instance for ModifyRocketMQNamespace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQNamespaceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQRole(self, request):
        """角色修改

        :param request: Request instance for ModifyRocketMQRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQRole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQTopic(self, request):
        """更新RocketMQ主题信息

        :param request: Request instance for ModifyRocketMQTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRole(self, request):
        """角色修改

        :param request: Request instance for ModifyRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRoleResponse`

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
        """修改主题备注和分区数

        :param request: Request instance for ModifyTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyTopicResponse`

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


    def PublishCmqMsg(self, request):
        """发送cmq主题消息

        :param request: Request instance for PublishCmqMsg.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.PublishCmqMsgRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.PublishCmqMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishCmqMsg", params, headers=headers)
            response = json.loads(body)
            model = models.PublishCmqMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReceiveMessage(self, request):
        """当前 ReceiveMessage 接口只支持 Partitioned 类型的 Topic。该接口用于接收发送到指定 Partitioned Topic 中的消息，当 Partitioned Topic 中没有消息但还去尝试调用该接口时，会抛出 ReceiveTimeout 的异常。

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

        :param request: Request instance for ReceiveMessage.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ReceiveMessageRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ReceiveMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReceiveMessage", params, headers=headers)
            response = json.loads(body)
            model = models.ReceiveMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetMsgSubOffsetByTimestamp(self, request):
        """根据时间戳进行消息回溯，精确到毫秒

        :param request: Request instance for ResetMsgSubOffsetByTimestamp.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ResetMsgSubOffsetByTimestampRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ResetMsgSubOffsetByTimestampResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetMsgSubOffsetByTimestamp", params, headers=headers)
            response = json.loads(body)
            model = models.ResetMsgSubOffsetByTimestampResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetRocketMQConsumerOffSet(self, request):
        """重置指定Group的消费位点到指定时间戳

        :param request: Request instance for ResetRocketMQConsumerOffSet.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ResetRocketMQConsumerOffSetRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ResetRocketMQConsumerOffSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetRocketMQConsumerOffSet", params, headers=headers)
            response = json.loads(body)
            model = models.ResetRocketMQConsumerOffSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryRocketMQDlqMessage(self, request):
        """重发RocketMQ死信消息

        :param request: Request instance for RetryRocketMQDlqMessage.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.RetryRocketMQDlqMessageRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RetryRocketMQDlqMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryRocketMQDlqMessage", params, headers=headers)
            response = json.loads(body)
            model = models.RetryRocketMQDlqMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RewindCmqQueue(self, request):
        """回溯cmq队列

        :param request: Request instance for RewindCmqQueue.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.RewindCmqQueueRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RewindCmqQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RewindCmqQueue", params, headers=headers)
            response = json.loads(body)
            model = models.RewindCmqQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendBatchMessages(self, request):
        """批量发送消息

        注意：TDMQ 批量发送消息的接口是在 TDMQ-HTTP 的服务侧将消息打包为一个 Batch，然后将该 Batch 在服务内部当作一次 TCP 请求发送出去。所以在使用过程中，用户还是按照单条消息发送的逻辑，每一条消息是一个独立的 HTTP 的请求，在 TDMQ-HTTP 的服务内部，会将多个 HTTP 的请求聚合为一个 Batch 发送到服务端。即，批量发送消息在使用上与发送单条消息是一致的，batch 的聚合是在 TDMQ-HTTP 的服务内部完成的。

        :param request: Request instance for SendBatchMessages.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendBatchMessagesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendBatchMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendBatchMessages", params, headers=headers)
            response = json.loads(body)
            model = models.SendBatchMessagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendCmqMsg(self, request):
        """发送cmq消息

        :param request: Request instance for SendCmqMsg.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendCmqMsgRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendCmqMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendCmqMsg", params, headers=headers)
            response = json.loads(body)
            model = models.SendCmqMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendMessages(self, request):
        """发送单条消息
        不支持持久topic

        :param request: Request instance for SendMessages.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendMessagesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendMessages", params, headers=headers)
            response = json.loads(body)
            model = models.SendMessagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendMsg(self, request):
        """此接口仅用于测试发生消息，不能作为现网正式生产使用

        :param request: Request instance for SendMsg.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendMsgRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendMsg", params, headers=headers)
            response = json.loads(body)
            model = models.SendMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendRocketMQMessage(self, request):
        """发送RocketMQ消息

        :param request: Request instance for SendRocketMQMessage.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendRocketMQMessageRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendRocketMQMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendRocketMQMessage", params, headers=headers)
            response = json.loads(body)
            model = models.SendRocketMQMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetRocketMQPublicAccessPoint(self, request):
        """该接口用于开启关闭公网访问、设置安全访问策略

        :param request: Request instance for SetRocketMQPublicAccessPoint.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SetRocketMQPublicAccessPointRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SetRocketMQPublicAccessPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetRocketMQPublicAccessPoint", params, headers=headers)
            response = json.loads(body)
            model = models.SetRocketMQPublicAccessPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindCmqDeadLetter(self, request):
        """解绑cmq死信队列

        :param request: Request instance for UnbindCmqDeadLetter.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.UnbindCmqDeadLetterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.UnbindCmqDeadLetterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindCmqDeadLetter", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindCmqDeadLetterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyRocketMQConsume(self, request):
        """Rocketmq消费验证

        :param request: Request instance for VerifyRocketMQConsume.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.VerifyRocketMQConsumeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.VerifyRocketMQConsumeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyRocketMQConsume", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyRocketMQConsumeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))