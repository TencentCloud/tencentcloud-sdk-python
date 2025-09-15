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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.trabbit.v20230418 import models


class TrabbitClient(AbstractClient):
    _apiVersion = '2023-04-18'
    _endpoint = 'trabbit.tencentcloudapi.com'
    _service = 'trabbit'


    def CreateRabbitMQServerlessBinding(self, request):
        r"""创建RabbitMQ路由关系

        :param request: Request instance for CreateRabbitMQServerlessBinding.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.CreateRabbitMQServerlessBindingRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.CreateRabbitMQServerlessBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQServerlessBinding", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQServerlessBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQServerlessExchange(self, request):
        r"""创建RabbitMQ exchange

        :param request: Request instance for CreateRabbitMQServerlessExchange.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.CreateRabbitMQServerlessExchangeRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.CreateRabbitMQServerlessExchangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQServerlessExchange", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQServerlessExchangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQServerlessQueue(self, request):
        r"""创建RabbitMQ队列

        :param request: Request instance for CreateRabbitMQServerlessQueue.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.CreateRabbitMQServerlessQueueRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.CreateRabbitMQServerlessQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQServerlessQueue", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQServerlessQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQServerlessUser(self, request):
        r"""创建RabbitMQ的用户

        :param request: Request instance for CreateRabbitMQServerlessUser.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.CreateRabbitMQServerlessUserRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.CreateRabbitMQServerlessUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQServerlessUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQServerlessUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQServerlessVirtualHost(self, request):
        r"""创建RabbitMQ的vhost

        :param request: Request instance for CreateRabbitMQServerlessVirtualHost.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.CreateRabbitMQServerlessVirtualHostRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.CreateRabbitMQServerlessVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQServerlessVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQServerlessVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQServerlessBinding(self, request):
        r"""解绑RabbitMQ路由关系

        :param request: Request instance for DeleteRabbitMQServerlessBinding.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessBindingRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQServerlessBinding", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQServerlessBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQServerlessExchange(self, request):
        r"""删除RabbitMQ exchange

        :param request: Request instance for DeleteRabbitMQServerlessExchange.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessExchangeRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessExchangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQServerlessExchange", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQServerlessExchangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQServerlessPermission(self, request):
        r"""删除RabbitMQ的权限

        :param request: Request instance for DeleteRabbitMQServerlessPermission.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessPermissionRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQServerlessPermission", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQServerlessPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQServerlessQueue(self, request):
        r"""删除RabbitMQ队列

        :param request: Request instance for DeleteRabbitMQServerlessQueue.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessQueueRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQServerlessQueue", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQServerlessQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQServerlessUser(self, request):
        r"""删除RabbitMQ的用户

        :param request: Request instance for DeleteRabbitMQServerlessUser.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessUserRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQServerlessUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQServerlessUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQServerlessVirtualHost(self, request):
        r"""删除RabbitMQ的vhost

        :param request: Request instance for DeleteRabbitMQServerlessVirtualHost.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessVirtualHostRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DeleteRabbitMQServerlessVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQServerlessVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQServerlessVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessBindings(self, request):
        r"""获取路由关系列表

        :param request: Request instance for DescribeRabbitMQServerlessBindings.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessBindingsRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessBindings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessConnection(self, request):
        r"""查询RabbitMQ连接列表

        :param request: Request instance for DescribeRabbitMQServerlessConnection.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessConnectionRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessConsumers(self, request):
        r"""查询RabbitMQ队列消费者列表

        :param request: Request instance for DescribeRabbitMQServerlessConsumers.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessConsumersRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessConsumersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessConsumers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessConsumersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessExchangeDetail(self, request):
        r"""查询RabbitMQ exchange 详情

        :param request: Request instance for DescribeRabbitMQServerlessExchangeDetail.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessExchangeDetailRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessExchangeDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessExchangeDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessExchangeDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessExchanges(self, request):
        r"""查询RabbitMQ exchange 列表

        :param request: Request instance for DescribeRabbitMQServerlessExchanges.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessExchangesRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessExchangesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessExchanges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessExchangesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessInstance(self, request):
        r"""获取单个RabbitMQ专享实例信息

        :param request: Request instance for DescribeRabbitMQServerlessInstance.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessInstanceRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessPermission(self, request):
        r"""查询RabbitMQ权限列表

        :param request: Request instance for DescribeRabbitMQServerlessPermission.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessPermissionRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessPermission", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessQueueDetail(self, request):
        r"""查询RabbitMQ队列详情

        :param request: Request instance for DescribeRabbitMQServerlessQueueDetail.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessQueueDetailRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessQueueDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessQueueDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessQueueDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessQueues(self, request):
        r"""查询RabbitMQ队列列表

        :param request: Request instance for DescribeRabbitMQServerlessQueues.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessQueuesRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessQueuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessQueues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessQueuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessUser(self, request):
        r"""查询RabbitMQ用户列表

        :param request: Request instance for DescribeRabbitMQServerlessUser.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessUserRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQServerlessVirtualHost(self, request):
        r"""查询RabbitMQ vhost列表

        :param request: Request instance for DescribeRabbitMQServerlessVirtualHost.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessVirtualHostRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.DescribeRabbitMQServerlessVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQServerlessVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQServerlessVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRabbitMQServerlessInstances(self, request):
        r"""获取实例列表

        :param request: Request instance for ListRabbitMQServerlessInstances.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.ListRabbitMQServerlessInstancesRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.ListRabbitMQServerlessInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRabbitMQServerlessInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListRabbitMQServerlessInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQServerlessExchange(self, request):
        r"""修改RabbitMQ exchange

        :param request: Request instance for ModifyRabbitMQServerlessExchange.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessExchangeRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessExchangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQServerlessExchange", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQServerlessExchangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQServerlessInstance(self, request):
        r"""修改集群信息

        :param request: Request instance for ModifyRabbitMQServerlessInstance.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessInstanceRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQServerlessInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQServerlessInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQServerlessPermission(self, request):
        r"""修改RabbitMQ的权限

        :param request: Request instance for ModifyRabbitMQServerlessPermission.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessPermissionRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQServerlessPermission", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQServerlessPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQServerlessQueue(self, request):
        r"""修改RabbitMQ队列

        :param request: Request instance for ModifyRabbitMQServerlessQueue.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessQueueRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQServerlessQueue", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQServerlessQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQServerlessUser(self, request):
        r"""修改RabbitMQ的用户

        :param request: Request instance for ModifyRabbitMQServerlessUser.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessUserRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQServerlessUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQServerlessUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQServerlessVirtualHost(self, request):
        r"""修改RabbitMQ的vhost

        :param request: Request instance for ModifyRabbitMQServerlessVirtualHost.
        :type request: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessVirtualHostRequest`
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.ModifyRabbitMQServerlessVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQServerlessVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQServerlessVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))