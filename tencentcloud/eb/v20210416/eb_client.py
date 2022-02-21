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
            body = self.call("CheckRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckRuleResponse()
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


    def CheckTransformation(self, request):
        """用于在ETL配置页面, 测试规则和数据.

        :param request: Request instance for CheckTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.CheckTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CheckTransformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckTransformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckTransformationResponse()
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


    def CreateConnection(self, request):
        """创建事件连接器

        :param request: Request instance for CreateConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateConnectionResponse()
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


    def CreateEventBus(self, request):
        """用于创建事件集

        :param request: Request instance for CreateEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateEventBusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEventBus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEventBusResponse()
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


    def CreateRule(self, request):
        """创建事件规则

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRuleResponse()
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


    def CreateTarget(self, request):
        """创建事件目标

        :param request: Request instance for CreateTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateTargetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTarget", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTargetResponse()
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


    def CreateTransformation(self, request):
        """用于创建转换器

        :param request: Request instance for CreateTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateTransformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTransformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTransformationResponse()
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


    def DeleteConnection(self, request):
        """删除事件连接器

        :param request: Request instance for DeleteConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteConnectionResponse()
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


    def DeleteEventBus(self, request):
        """删除事件集

        :param request: Request instance for DeleteEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteEventBusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEventBus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEventBusResponse()
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


    def DeleteRule(self, request):
        """删除事件规则

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRuleResponse()
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


    def DeleteTarget(self, request):
        """删除事件目标

        :param request: Request instance for DeleteTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteTargetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTarget", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTargetResponse()
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


    def DeleteTransformation(self, request):
        """用于删除转换器

        :param request: Request instance for DeleteTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteTransformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTransformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTransformationResponse()
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


    def GetEventBus(self, request):
        """获取事件集详情

        :param request: Request instance for GetEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetEventBusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetEventBus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetEventBusResponse()
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


    def GetRule(self, request):
        """获取事件规则详情

        :param request: Request instance for GetRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRuleResponse()
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


    def GetTransformation(self, request):
        """用于获取转换器详情

        :param request: Request instance for GetTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetTransformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTransformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTransformationResponse()
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


    def ListConnections(self, request):
        """获取事件连接器列表

        :param request: Request instance for ListConnections.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListConnectionsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListConnectionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListConnections", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListConnectionsResponse()
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


    def ListEventBuses(self, request):
        """获取事件集列表

        :param request: Request instance for ListEventBuses.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListEventBusesRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListEventBusesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEventBuses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEventBusesResponse()
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


    def ListRules(self, request):
        """获取事件规则列表

        :param request: Request instance for ListRules.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListRulesRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListRulesResponse()
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


    def ListTargets(self, request):
        """获取事件目标列表

        :param request: Request instance for ListTargets.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListTargetsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTargetsResponse()
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


    def PublishEvent(self, request):
        """（已废弃）用于Event事件投递

        :param request: Request instance for PublishEvent.
        :type request: :class:`tencentcloud.eb.v20210416.models.PublishEventRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.PublishEventResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishEvent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishEventResponse()
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


    def PutEvents(self, request):
        """用于Event事件投递

        :param request: Request instance for PutEvents.
        :type request: :class:`tencentcloud.eb.v20210416.models.PutEventsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.PutEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutEventsResponse()
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


    def UpdateConnection(self, request):
        """更新事件连接器

        :param request: Request instance for UpdateConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateConnectionResponse()
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


    def UpdateEventBus(self, request):
        """更新事件集

        :param request: Request instance for UpdateEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateEventBusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateEventBus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateEventBusResponse()
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


    def UpdateRule(self, request):
        """更新事件规则

        :param request: Request instance for UpdateRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRuleResponse()
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


    def UpdateTarget(self, request):
        """更新事件目标

        :param request: Request instance for UpdateTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateTargetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateTarget", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateTargetResponse()
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


    def UpdateTransformation(self, request):
        """用于更新转换器

        :param request: Request instance for UpdateTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateTransformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateTransformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateTransformationResponse()
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