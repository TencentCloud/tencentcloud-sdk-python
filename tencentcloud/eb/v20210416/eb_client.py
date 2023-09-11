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
from tencentcloud.eb.v20210416 import models


class EbClient(AbstractClient):
    _apiVersion = '2021-04-16'
    _endpoint = 'eb.tencentcloudapi.com'
    _service = 'eb'


    def CheckRule(self, request):
        """检验规则

        :param request: Request instance for CheckRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.CheckRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CheckRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckRule", params, headers=headers)
            response = json.loads(body)
            model = models.CheckRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckTransformation(self, request):
        """用于在ETL配置页面, 测试规则和数据.

        :param request: Request instance for CheckTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.CheckTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CheckTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTransformation", params, headers=headers)
            response = json.loads(body)
            model = models.CheckTransformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConnection(self, request):
        """创建事件连接器

        :param request: Request instance for CreateConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConnection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEventBus(self, request):
        """用于创建事件集

        :param request: Request instance for CreateEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateEventBusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEventBus", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEventBusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        """创建事件规则

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTarget(self, request):
        """创建事件目标

        :param request: Request instance for CreateTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTarget", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTransformation(self, request):
        """用于创建转换器

        :param request: Request instance for CreateTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTransformation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTransformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConnection(self, request):
        """删除事件连接器

        :param request: Request instance for DeleteConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEventBus(self, request):
        """删除事件集

        :param request: Request instance for DeleteEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteEventBusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEventBus", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEventBusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRule(self, request):
        """删除事件规则

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTarget(self, request):
        """删除事件目标

        :param request: Request instance for DeleteTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTarget", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTransformation(self, request):
        """用于删除转换器

        :param request: Request instance for DeleteTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTransformation", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTransformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogTagValue(self, request):
        """查询日志索引维度值

        :param request: Request instance for DescribeLogTagValue.
        :type request: :class:`tencentcloud.eb.v20210416.models.DescribeLogTagValueRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DescribeLogTagValueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogTagValue", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogTagValueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEventBus(self, request):
        """获取事件集详情

        :param request: Request instance for GetEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetEventBusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEventBus", params, headers=headers)
            response = json.loads(body)
            model = models.GetEventBusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPlatformEventTemplate(self, request):
        """获取平台产品事件模板

        :param request: Request instance for GetPlatformEventTemplate.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetPlatformEventTemplateRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetPlatformEventTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPlatformEventTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.GetPlatformEventTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRule(self, request):
        """获取事件规则详情

        :param request: Request instance for GetRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRule", params, headers=headers)
            response = json.loads(body)
            model = models.GetRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTransformation(self, request):
        """用于获取转换器详情

        :param request: Request instance for GetTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTransformation", params, headers=headers)
            response = json.loads(body)
            model = models.GetTransformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConnections(self, request):
        """获取事件连接器列表

        :param request: Request instance for ListConnections.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListConnectionsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConnections", params, headers=headers)
            response = json.loads(body)
            model = models.ListConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEventBuses(self, request):
        """获取事件集列表

        :param request: Request instance for ListEventBuses.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListEventBusesRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListEventBusesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEventBuses", params, headers=headers)
            response = json.loads(body)
            model = models.ListEventBusesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListPlatformEventNames(self, request):
        """获取平台产品事件名称

        :param request: Request instance for ListPlatformEventNames.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListPlatformEventNamesRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListPlatformEventNamesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPlatformEventNames", params, headers=headers)
            response = json.loads(body)
            model = models.ListPlatformEventNamesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListPlatformEventPatterns(self, request):
        """获取平台产品事件匹配规则

        :param request: Request instance for ListPlatformEventPatterns.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListPlatformEventPatternsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListPlatformEventPatternsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPlatformEventPatterns", params, headers=headers)
            response = json.loads(body)
            model = models.ListPlatformEventPatternsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListPlatformProducts(self, request):
        """获取平台产品列表

        :param request: Request instance for ListPlatformProducts.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListPlatformProductsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListPlatformProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPlatformProducts", params, headers=headers)
            response = json.loads(body)
            model = models.ListPlatformProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRules(self, request):
        """获取事件规则列表

        :param request: Request instance for ListRules.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListRulesRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTargets(self, request):
        """获取事件目标列表

        :param request: Request instance for ListTargets.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListTargetsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTargets", params, headers=headers)
            response = json.loads(body)
            model = models.ListTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishEvent(self, request):
        """（已废弃）用于Event事件投递

        :param request: Request instance for PublishEvent.
        :type request: :class:`tencentcloud.eb.v20210416.models.PublishEventRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.PublishEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishEvent", params, headers=headers)
            response = json.loads(body)
            model = models.PublishEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutEvents(self, request):
        """用于Event事件投递

        :param request: Request instance for PutEvents.
        :type request: :class:`tencentcloud.eb.v20210416.models.PutEventsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.PutEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutEvents", params, headers=headers)
            response = json.loads(body)
            model = models.PutEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchLog(self, request):
        """日志检索

        :param request: Request instance for SearchLog.
        :type request: :class:`tencentcloud.eb.v20210416.models.SearchLogRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.SearchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConnection(self, request):
        """更新事件连接器

        :param request: Request instance for UpdateConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConnection", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEventBus(self, request):
        """更新事件集

        :param request: Request instance for UpdateEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateEventBusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEventBus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEventBusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRule(self, request):
        """更新事件规则

        :param request: Request instance for UpdateRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTarget(self, request):
        """更新事件目标

        :param request: Request instance for UpdateTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTarget", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTransformation(self, request):
        """用于更新转换器

        :param request: Request instance for UpdateTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTransformation", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTransformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))