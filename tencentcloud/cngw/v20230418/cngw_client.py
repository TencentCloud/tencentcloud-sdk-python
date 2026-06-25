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
from tencentcloud.cngw.v20230418 import models


class CngwClient(AbstractClient):
    _apiVersion = '2023-04-18'
    _endpoint = 'cngw.tencentcloudapi.com'
    _service = 'cngw'


    def AddCloudNativeAPIGatewayConsumerGroupAuth(self, request):
        r"""为资源（模型 API / MCP Server）添加消费者组授权。

        :param request: Request instance for AddCloudNativeAPIGatewayConsumerGroupAuth.
        :type request: :class:`tencentcloud.cngw.v20230418.models.AddCloudNativeAPIGatewayConsumerGroupAuthRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AddCloudNativeAPIGatewayConsumerGroupAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCloudNativeAPIGatewayConsumerGroupAuth", params, headers=headers)
            response = json.loads(body)
            model = models.AddCloudNativeAPIGatewayConsumerGroupAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayConsumer(self, request):
        r"""创建AI网关消费者。

        :param request: Request instance for CreateCloudNativeAPIGatewayConsumer.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayConsumerRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayConsumerGroup(self, request):
        r"""创建AI 网关消费者组

        :param request: Request instance for CreateCloudNativeAPIGatewayConsumerGroup.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayConsumerGroupRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayLLMModelAPI(self, request):
        r"""创建 LLM 模型 API。

        :param request: Request instance for CreateCloudNativeAPIGatewayLLMModelAPI.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayLLMModelAPIRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayLLMModelAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayLLMModelAPI", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayLLMModelAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayLLMModelService(self, request):
        r"""创建 LLM 模型服务。同一网关下 Name 唯一。

        :param request: Request instance for CreateCloudNativeAPIGatewayLLMModelService.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayLLMModelServiceRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayLLMModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayLLMModelService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayLLMModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayMCPServer(self, request):
        r"""创建AI网关MCP Server

        :param request: Request instance for CreateCloudNativeAPIGatewayMCPServer.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayMCPServerRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayMCPServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayMCPServer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayMCPServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayMCPTool(self, request):
        r"""创建AI网关MCP Tool

        :param request: Request instance for CreateCloudNativeAPIGatewayMCPTool.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayMCPToolRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayMCPToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayMCPTool", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayMCPToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewaySecretKey(self, request):
        r"""创建消费者密钥。

        :param request: Request instance for CreateCloudNativeAPIGatewaySecretKey.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayConsumer(self, request):
        r"""删除AI 网关消费者（被绑定到消费者组/密钥时需先解绑）。

        :param request: Request instance for DeleteCloudNativeAPIGatewayConsumer.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayConsumerRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayConsumerGroup(self, request):
        r"""删除AI网关消费者组

        :param request: Request instance for DeleteCloudNativeAPIGatewayConsumerGroup.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayConsumerGroupRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayLLMModelAPI(self, request):
        r"""删除 LLM 模型 API。

        :param request: Request instance for DeleteCloudNativeAPIGatewayLLMModelAPI.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayLLMModelAPIRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayLLMModelAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayLLMModelAPI", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayLLMModelAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayLLMModelService(self, request):
        r"""删除 LLM 模型服务（被模型 API 绑定时需先解绑）。

        :param request: Request instance for DeleteCloudNativeAPIGatewayLLMModelService.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayLLMModelServiceRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayLLMModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayLLMModelService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayLLMModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayMCPServer(self, request):
        r"""删除AI网关MCP服务

        :param request: Request instance for DeleteCloudNativeAPIGatewayMCPServer.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayMCPServerRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayMCPServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayMCPServer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayMCPServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayMCPTool(self, request):
        r"""删除AI网关MCP Tool

        :param request: Request instance for DeleteCloudNativeAPIGatewayMCPTool.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayMCPToolRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayMCPToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayMCPTool", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayMCPToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewaySecretKey(self, request):
        r"""删除消费者密钥（被绑定时需先解绑）。

        :param request: Request instance for DeleteCloudNativeAPIGatewaySecretKey.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayConsumer(self, request):
        r"""查询云原生消费者详情

        :param request: Request instance for DescribeCloudNativeAPIGatewayConsumer.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayConsumerRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayConsumerGroup(self, request):
        r"""查询消费者组详情。

        :param request: Request instance for DescribeCloudNativeAPIGatewayConsumerGroup.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayConsumerGroupRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayLLMModelAPI(self, request):
        r"""查询单个 LLM 模型 API 详情。

        :param request: Request instance for DescribeCloudNativeAPIGatewayLLMModelAPI.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMModelAPIRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMModelAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayLLMModelAPI", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayLLMModelAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayLLMModelAPIs(self, request):
        r"""查询 LLM 模型 API 列表。

        :param request: Request instance for DescribeCloudNativeAPIGatewayLLMModelAPIs.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMModelAPIsRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMModelAPIsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayLLMModelAPIs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayLLMModelAPIsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayLLMModelService(self, request):
        r"""查询单个 LLM 模型服务详情。

        :param request: Request instance for DescribeCloudNativeAPIGatewayLLMModelService.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMModelServiceRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayLLMModelService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayLLMModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayLLMModelServices(self, request):
        r"""查询 LLM 模型服务列表。

        :param request: Request instance for DescribeCloudNativeAPIGatewayLLMModelServices.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMModelServicesRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMModelServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayLLMModelServices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayLLMModelServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayLLMTokenUsageList(self, request):
        r"""查询 AI 网关Token 消耗统计

        :param request: Request instance for DescribeCloudNativeAPIGatewayLLMTokenUsageList.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMTokenUsageListRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMTokenUsageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayLLMTokenUsageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayLLMTokenUsageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayLLMTokenUsageStatistics(self, request):
        r"""查询 AI 网关Token 消耗统计汇总

        :param request: Request instance for DescribeCloudNativeAPIGatewayLLMTokenUsageStatistics.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMTokenUsageStatisticsRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayLLMTokenUsageStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayLLMTokenUsageStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayLLMTokenUsageStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayMCPServer(self, request):
        r"""查询AI 网关MCP服务信息

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPServer.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPServerRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPServer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayMCPServerACL(self, request):
        r"""查看 MCP Server ACL

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPServerACL.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPServerACLRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPServerACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPServerACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPServerACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayMCPServerAuth(self, request):
        r"""查询 MCP Server 的认证配置

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPServerAuth.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPServerAuthRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPServerAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPServerAuth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPServerAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayMCPServerList(self, request):
        r"""AI网关查询MCP服务列表

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPServerList.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPServerListRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPServerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPServerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPServerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayMCPTool(self, request):
        r"""查看AI网关MCP Tool

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPTool.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPTool", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayMCPToolACLList(self, request):
        r"""查询云原生网关 MCP Server 下所有 Tool 的 ACL 状态一览（含 Server ACLType 回显）。

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPToolACLList.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolACLListRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolACLListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPToolACLList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPToolACLListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayMCPToolList(self, request):
        r"""查询 AI 网关MCP Tool 列表

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPToolList.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolListRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPToolList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPToolListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewaySecretKey(self, request):
        r"""查询密钥详情（SecretValue 字段会被掩码）。

        :param request: Request instance for DescribeCloudNativeAPIGatewaySecretKey.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewaySecretKeyValue(self, request):
        r"""查询密钥明文值（KMS 类型密钥不可获取）。

        :param request: Request instance for DescribeCloudNativeAPIGatewaySecretKeyValue.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewaySecretKeyValueRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewaySecretKeyValueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewaySecretKeyValue", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewaySecretKeyValueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayConsumer(self, request):
        r"""修改AI网关消费者

        :param request: Request instance for ModifyCloudNativeAPIGatewayConsumer.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayConsumerRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayConsumerGroup(self, request):
        r"""修改消费者组。

        :param request: Request instance for ModifyCloudNativeAPIGatewayConsumerGroup.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayConsumerGroupRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayLLMModelAPI(self, request):
        r"""修改 LLM 模型 API。

        :param request: Request instance for ModifyCloudNativeAPIGatewayLLMModelAPI.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayLLMModelAPIRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayLLMModelAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayLLMModelAPI", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayLLMModelAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayLLMModelService(self, request):
        r"""修改 LLM 模型服务。

        :param request: Request instance for ModifyCloudNativeAPIGatewayLLMModelService.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayLLMModelServiceRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayLLMModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayLLMModelService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayLLMModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayMCPServer(self, request):
        r"""修改MCP服务配置

        :param request: Request instance for ModifyCloudNativeAPIGatewayMCPServer.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPServerRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayMCPServer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayMCPServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayMCPServerACL(self, request):
        r"""修改 MCP Server ACL

        :param request: Request instance for ModifyCloudNativeAPIGatewayMCPServerACL.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPServerACLRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPServerACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayMCPServerACL", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayMCPServerACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayMCPServerAuth(self, request):
        r"""修改 MCP Server 的认证配置

        :param request: Request instance for ModifyCloudNativeAPIGatewayMCPServerAuth.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPServerAuthRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPServerAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayMCPServerAuth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayMCPServerAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayMCPServerStatus(self, request):
        r"""创建AI 网关MCP Server

        :param request: Request instance for ModifyCloudNativeAPIGatewayMCPServerStatus.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPServerStatusRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPServerStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayMCPServerStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayMCPServerStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayMCPTool(self, request):
        r"""修改AI网关MCP Tool

        :param request: Request instance for ModifyCloudNativeAPIGatewayMCPTool.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPToolRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayMCPTool", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayMCPToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayMCPToolACL(self, request):
        r"""修改 MCP Server Tool ACL

        :param request: Request instance for ModifyCloudNativeAPIGatewayMCPToolACL.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPToolACLRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPToolACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayMCPToolACL", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayMCPToolACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayMCPToolStatus(self, request):
        r"""AI网关修改MCP Tool上下线状态

        :param request: Request instance for ModifyCloudNativeAPIGatewayMCPToolStatus.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPToolStatusRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPToolStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayMCPToolStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayMCPToolStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewaySecretKey(self, request):
        r"""修改AI网关密钥

        :param request: Request instance for ModifyCloudNativeAPIGatewaySecretKey.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveCloudNativeAPIGatewayConsumerGroupAuth(self, request):
        r"""从资源（模型 API / MCP Server）移除消费者组授权。

        :param request: Request instance for RemoveCloudNativeAPIGatewayConsumerGroupAuth.
        :type request: :class:`tencentcloud.cngw.v20230418.models.RemoveCloudNativeAPIGatewayConsumerGroupAuthRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.RemoveCloudNativeAPIGatewayConsumerGroupAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveCloudNativeAPIGatewayConsumerGroupAuth", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveCloudNativeAPIGatewayConsumerGroupAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))