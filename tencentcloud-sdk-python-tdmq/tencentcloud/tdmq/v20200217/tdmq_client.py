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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tdmq.v20200217 import models


class TdmqClient(AbstractClient):
    _apiVersion = '2020-02-17'
    _endpoint = 'tdmq.tencentcloudapi.com'


    def CreateEnvironment(self, request):
        """用于在用户账户下创建消息队列 Tdmq环境（命名空间）

        :param request: Request instance for CreateEnvironment.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateEnvironmentRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateEnvironmentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEnvironment", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEnvironmentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSubscription(self, request):
        """创建一个主题的订阅关系

        :param request: Request instance for CreateSubscription.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateSubscriptionRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateSubscriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubscription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubscriptionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTopic(self, request):
        """新增指定分区、类型的消息主题

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTopicResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteEnvironments(self, request):
        """批量删除租户下的环境

        :param request: Request instance for DeleteEnvironments.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteEnvironmentsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEnvironments", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEnvironmentsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSubscriptions(self, request):
        """删除订阅关系

        :param request: Request instance for DeleteSubscriptions.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteSubscriptionsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteSubscriptionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSubscriptions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSubscriptionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTopics(self, request):
        """批量删除topics

        :param request: Request instance for DeleteTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteTopicsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTopics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTopicsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvironmentAttributes(self, request):
        """获取指定环境的属性

        :param request: Request instance for DescribeEnvironmentAttributes.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentAttributesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEnvironmentAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvironmentAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvironments(self, request):
        """获取租户下环境列表

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEnvironments", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvironmentsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProducers(self, request):
        """获取生产者列表，仅显示在线的生产者

        :param request: Request instance for DescribeProducers.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeProducersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeProducersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProducers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProducersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSubscriptions(self, request):
        """查询指定环境和主题下的订阅者列表

        :param request: Request instance for DescribeSubscriptions.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeSubscriptionsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeSubscriptionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubscriptions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubscriptionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTopics(self, request):
        """获取环境下主题列表

        :param request: Request instance for DescribeTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeTopicsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopicsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEnvironmentAttributes(self, request):
        """修改指定环境的属性值

        :param request: Request instance for ModifyEnvironmentAttributes.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyEnvironmentAttributesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyEnvironmentAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyEnvironmentAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEnvironmentAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTopic(self, request):
        """修改主题备注和分区数

        :param request: Request instance for ModifyTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTopicResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetMsgSubOffsetByTimestamp(self, request):
        """根据时间戳进行消息回溯，精确到毫秒

        :param request: Request instance for ResetMsgSubOffsetByTimestamp.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ResetMsgSubOffsetByTimestampRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ResetMsgSubOffsetByTimestampResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetMsgSubOffsetByTimestamp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetMsgSubOffsetByTimestampResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)