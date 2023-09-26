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
        """购买新实例

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
        """删除实例

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


    def DescribeInstance(self, request):
        """查询实例信息

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
        """获取实例列表，Filters参数使用说明如下：
        1. InstanceName, 名称模糊查询
        2. InstanceId，实例ID查询
        3. InstanceType, 实例类型查询，支持多选
        3. InstanceStatus，实例状态查询，支持多选

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


    def DescribeRoleList(self, request):
        """查询角色列表，Filter参数使用说明如下：

        1. RoleName，角色名称模糊搜索

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


    def DescribeTopicStatsOp(self, request):
        """运营端查询topicStata

        :param request: Request instance for DescribeTopicStatsOp.
        :type request: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicStatsOpRequest`
        :rtype: :class:`tencentcloud.trocket.v20230308.models.DescribeTopicStatsOpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicStatsOp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicStatsOpResponse()
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
        """修改实例属性

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