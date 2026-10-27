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


    def AddCloudNativeAPIGatewayConsumerInGroup(self, request):
        r"""将消费者添加到消费者组。

        :param request: Request instance for AddCloudNativeAPIGatewayConsumerInGroup.
        :type request: :class:`tencentcloud.cngw.v20230418.models.AddCloudNativeAPIGatewayConsumerInGroupRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.AddCloudNativeAPIGatewayConsumerInGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCloudNativeAPIGatewayConsumerInGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddCloudNativeAPIGatewayConsumerInGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindCloudNativeAPIGatewaySecretKey(self, request):
        r"""添加密钥与资源的引用关系接口
        【消费者批量自动分配 API Key｜修改：内部并发/配额逻辑，字段不变】ResourceType=Consumer 时与批量预留共用实例写锁，单消费者绑定配额使用当前锁定读。仍按原 SecretKeyId、ResourceIds 绑定；消费者目标最多一个，单密钥不能同时绑定多个消费者，成功仍返回 Result=true。此入口不新增 OperationDenied.BatchKeyPending；该错误属于下述四个变更入口的保护逻辑。 完整接口清单与逐项说明：https://iwiki.woa.com/p/4042678235（第 2、2.4 节）。

        :param request: Request instance for BindCloudNativeAPIGatewaySecretKey.
        :type request: :class:`tencentcloud.cngw.v20230418.models.BindCloudNativeAPIGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.BindCloudNativeAPIGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindCloudNativeAPIGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.BindCloudNativeAPIGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCloudNativeAPIGatewayMCPRouteMatch(self, request):
        r"""上传插件前置操作，获取COS相关信息

        :param request: Request instance for CheckCloudNativeAPIGatewayMCPRouteMatch.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CheckCloudNativeAPIGatewayMCPRouteMatchRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CheckCloudNativeAPIGatewayMCPRouteMatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCloudNativeAPIGatewayMCPRouteMatch", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCloudNativeAPIGatewayMCPRouteMatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCloudNativeAPIGatewayMCPToolVersionExist(self, request):
        r"""修改云原生智能网关MCP Tool

        :param request: Request instance for CheckCloudNativeAPIGatewayMCPToolVersionExist.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CheckCloudNativeAPIGatewayMCPToolVersionExistRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CheckCloudNativeAPIGatewayMCPToolVersionExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCloudNativeAPIGatewayMCPToolVersionExist", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCloudNativeAPIGatewayMCPToolVersionExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompareCloudNativeAPIGatewayMCPToolVersion(self, request):
        r"""修改云原生智能网关MCP Tool

        :param request: Request instance for CompareCloudNativeAPIGatewayMCPToolVersion.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CompareCloudNativeAPIGatewayMCPToolVersionRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CompareCloudNativeAPIGatewayMCPToolVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompareCloudNativeAPIGatewayMCPToolVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CompareCloudNativeAPIGatewayMCPToolVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayAIServiceSource(self, request):
        r"""创建云原生网关AI服务来源

        :param request: Request instance for CreateCloudNativeAPIGatewayAIServiceSource.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayAIServiceSourceRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayAIServiceSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayAIServiceSource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayAIServiceSourceResponse()
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


    def CreateCloudNativeAPIGatewayMCPRoute(self, request):
        r"""上传插件前置操作，获取COS相关信息

        :param request: Request instance for CreateCloudNativeAPIGatewayMCPRoute.
        :type request: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayMCPRouteRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.CreateCloudNativeAPIGatewayMCPRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayMCPRoute", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayMCPRouteResponse()
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
        【消费者批量自动分配 API Key｜修改：内部并发/配额逻辑，字段不变】消费者密钥单条创建在事务中使用与批量预留相同的实例写锁，配额检查使用当前锁定读，避免单条与批量并发绕过配额。仍是单条创建；原 GenerateType、请求字段、既有配额错误语义及 Result.Success/ID 不变，不增加 ConsumerIds/ClientToken。 完整接口清单与逐项说明：https://iwiki.woa.com/p/4042678235（第 2、2.4 节）。

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


    def DeleteCloudNativeAPIGatewayAIServiceSource(self, request):
        r"""删除云原生网关AI服务来源

        :param request: Request instance for DeleteCloudNativeAPIGatewayAIServiceSource.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayAIServiceSourceRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayAIServiceSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayAIServiceSource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayAIServiceSourceResponse()
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

        同步组仅在 soft_deleted 状态且全部依赖已清理后允许手动硬删除；ConsumerGroupId 使用组织 UUID。存在配额规则时须先删除规则，单纯停用不能解除依赖。硬删除时重新校验，依赖变化可能导致删除失败。

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


    def DeleteCloudNativeAPIGatewayMCPRoute(self, request):
        r"""上传插件前置操作，获取COS相关信息

        :param request: Request instance for DeleteCloudNativeAPIGatewayMCPRoute.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayMCPRouteRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayMCPRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayMCPRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayMCPRouteResponse()
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


    def DeleteCloudNativeAPIGatewayMCPToolVersion(self, request):
        r"""修改云原生智能网关MCP Tool

        :param request: Request instance for DeleteCloudNativeAPIGatewayMCPToolVersion.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayMCPToolVersionRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DeleteCloudNativeAPIGatewayMCPToolVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayMCPToolVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayMCPToolVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewaySecretKey(self, request):
        r"""删除消费者密钥（被绑定时需先解绑）。
        【消费者批量自动分配 API Key｜修改：新增未完成批次保护，字段不变】目标密钥属于批次且对应项处于 Pending/Running/Reconciling 时，删除返回 OperationDenied.BatchKeyPending。完成后仍执行原绑定/依赖删除检查；原 GatewayId/SecretKeyId 不变，成功不新增业务 Result。删除已生成密钥不改写批次历史成功，后续批次明文读取返回逐项 ResourceNotFound.SecretKey。 完整接口清单与逐项说明：https://iwiki.woa.com/p/4042678235（第 2、2.4 节）。

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


    def DescribeCNGWServicesWithRoutes(self, request):
        r"""查询云原生网关服务和路由列表

        :param request: Request instance for DescribeCNGWServicesWithRoutes.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCNGWServicesWithRoutesRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCNGWServicesWithRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCNGWServicesWithRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCNGWServicesWithRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayAIQuota(self, request):
        r"""查询AI网关配额

        支持 ConsumerGroup 配额，返回 ConsumerGroupPath、ConsumerGroupActive 及实际用量；失效组的规则仍可查询。

        :param request: Request instance for DescribeCloudNativeAPIGatewayAIQuota.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayAIQuotaRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayAIQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayAIQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayAIQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayAIQuotaList(self, request):
        r"""查询AI配额配置列表

        支持按 ConsumerGroup 查询组自身配额，默认仍只查询 Consumer；返回组路径、有效状态及实际用量。上下级关联配额请使用 DescribeAIGWConsumerGroupAIQuotaList。

        :param request: Request instance for DescribeCloudNativeAPIGatewayAIQuotaList.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayAIQuotaListRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayAIQuotaListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayAIQuotaList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayAIQuotaListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayAIServiceSourceList(self, request):
        r"""查询云原生网关AI服务来源

        :param request: Request instance for DescribeCloudNativeAPIGatewayAIServiceSourceList.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayAIServiceSourceListRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayAIServiceSourceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayAIServiceSourceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayAIServiceSourceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayConsumer(self, request):
        r"""查询云原生消费者详情

        组织架构扩展：保留原消费者详情与完整字段，ConsumerGroups 补齐对应组织成员关系；同步成员保持目录归属隔离。

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

        组织架构扩展：ConsumerGroupId 同时支持原 cg-* 和组织部门 UUID；保留状态、数量、时间和描述逻辑。原普通组状态为 Enable/Disable，目录部门状态为 active/disabled/soft_deleted。

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
        r"""查询指定网关实例下的所有 LLM 模型 API 列表。支持按名称关键词模糊搜索、按过滤器筛选，以及分页查询。用于绑定场景时，可通过 ConsumerGroupId 和 UseToBind 参数筛选可绑定的模型 API。

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
        r"""查询 AI 网关 Token 用量列表。网关版本不低于 3.9.8 且 Dimension=ConsumerGroup 时，未指定节点筛选则列出 Kong CP 当前目录的全部真实节点，包含同步、自定义、禁用及保留中的软删节点，排除合成展示节点。按当前名称、节点 UUID 升序，先分页节点再查询历史指标；无调用节点仍返回，Token 与请求数补零。节点指标包含历史下属，同一请求可计入多个组行，不能逐行相加作为网关总量。 网关版本不低于 3.9.8 时，所有支持维度的消费者组筛选统一为 ConsumerGroupId / ConsumerGroupName，均按历史归属查询；旧 OrganizationNodeId / OrganizationNodeName 筛选不再接受。

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
        r"""查询 AI 网关 Token 用量汇总。网关版本不低于 3.9.8 且 Dimension=ConsumerGroup 时，按历史归属对日志并集去重统计；无节点筛选则查询全部成功归属且祖先集合非空的日志，不依赖当前组织目录候选。返回一份汇总，TopConsumers 为空数组。 网关版本不低于 3.9.8 时，所有支持维度的消费者组筛选统一为 ConsumerGroupId / ConsumerGroupName，均按历史归属查询；旧 OrganizationNodeId / OrganizationNodeName 筛选不再接受。

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


    def DescribeCloudNativeAPIGatewayMCPRouteList(self, request):
        r"""上传插件前置操作，获取COS相关信息

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPRouteList.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPRouteListRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPRouteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPRouteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPRouteListResponse()
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


    def DescribeCloudNativeAPIGatewayMCPToolImportTask(self, request):
        r"""查询批量导入MCP Tools的任务进度

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPToolImportTask.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolImportTaskRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolImportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPToolImportTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPToolImportTaskResponse()
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


    def DescribeCloudNativeAPIGatewayMCPToolVersion(self, request):
        r"""修改云原生智能网关MCP Tool

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPToolVersion.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolVersionRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPToolVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPToolVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayMCPToolVersionList(self, request):
        r"""修改云原生智能网关MCP Tool

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPToolVersionList.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolVersionListRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPToolVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPToolVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayMCPToolsFromFile(self, request):
        r"""从OpenAPI文件中解析出可导入的MCP tools

        :param request: Request instance for DescribeCloudNativeAPIGatewayMCPToolsFromFile.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolsFromFileRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewayMCPToolsFromFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayMCPToolsFromFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayMCPToolsFromFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewaySecretKey(self, request):
        r"""查询密钥详情（SecretValue 字段会被掩码）。
        普通版批量新建密钥的生成来源扩展：新页面按需 IncludeCreationInfo=true，省略/false 保持原响应字段。原 GenerateType 不新增 Batch；批量记录仍为 System。协议：https://iwiki.woa.com/p/4042678235。
        【消费者批量自动分配 API Key｜修改：可选参数及可选出参】增加可选 IncludeCreationInfo（默认 false）。仅 true 且 ResourceType=Consumer 时在原 Result 增加 CredentialGenerateType、CreationSource、BatchId 三个非必返字段；省略/false 保持旧响应。原字段、SecretValue 脱敏和单条详情结构不变。 完整接口清单与逐项说明：https://iwiki.woa.com/p/4042678235（第 2、2.4 节）。

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


    def DescribeCloudNativeAPIGatewaySecretKeyList(self, request):
        r"""查询密钥列表。
        普通版批量新建密钥的生成来源扩展：新页面按需 IncludeCreationInfo=true，省略/false 保持原响应字段。原 GenerateType 不新增 Batch；批量记录仍为 System。协议：https://iwiki.woa.com/p/4042678235。
        【消费者批量自动分配 API Key｜修改：可选参数、可选出参及筛选】增加可选 IncludeCreationInfo（默认 false）。仅 true 且 ResourceType=Consumer 时在原 Result.SecretKeys[] 增加 CredentialGenerateType、CreationSource、BatchId 三个非必返字段；Result.TotalCount/SecretKeys 结构不变。Filters 新增 CredentialGenerateType、CreationSource，先过滤后计数分页，与是否返回来源字段独立；保留原 GenerateType 枚举和原分页上限。 完整接口清单与逐项说明：https://iwiki.woa.com/p/4042678235（第 2、2.4 节）。

        :param request: Request instance for DescribeCloudNativeAPIGatewaySecretKeyList.
        :type request: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewaySecretKeyListRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.DescribeCloudNativeAPIGatewaySecretKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewaySecretKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewaySecretKeyListResponse()
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


    def ModifyCloudNativeAPIGatewayAIServiceSource(self, request):
        r"""修改云原生网关AI服务来源

        :param request: Request instance for ModifyCloudNativeAPIGatewayAIServiceSource.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayAIServiceSourceRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayAIServiceSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayAIServiceSource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayAIServiceSourceResponse()
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
        r"""更新指定网关实例内的 LLM 模型服务，可调整该服务向上游请求压缩响应的协商方式。

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


    def ModifyCloudNativeAPIGatewayMCPRoute(self, request):
        r"""上传插件前置操作，获取COS相关信息

        :param request: Request instance for ModifyCloudNativeAPIGatewayMCPRoute.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPRouteRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayMCPRoute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayMCPRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayMCPRouteStatus(self, request):
        r"""上传插件前置操作，获取COS相关信息

        :param request: Request instance for ModifyCloudNativeAPIGatewayMCPRouteStatus.
        :type request: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPRouteStatusRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.ModifyCloudNativeAPIGatewayMCPRouteStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayMCPRouteStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayMCPRouteStatusResponse()
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
        【消费者批量自动分配 API Key｜修改：新增未完成批次保护，字段不变】目标密钥属于批次且对应项处于 Pending/Running/Reconciling 时，编辑返回 OperationDenied.BatchKeyPending，提示等待批次完成。其他情况继续原编辑校验和行为；原 GatewayId/SecretKeyId/Name/Description 不变，成功不新增业务 Result。 完整接口清单与逐项说明：https://iwiki.woa.com/p/4042678235（第 2、2.4 节）。

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


    def RemoveCloudNativeAPIGatewayConsumerInGroup(self, request):
        r"""将消费者从消费者组移除。

        :param request: Request instance for RemoveCloudNativeAPIGatewayConsumerInGroup.
        :type request: :class:`tencentcloud.cngw.v20230418.models.RemoveCloudNativeAPIGatewayConsumerInGroupRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.RemoveCloudNativeAPIGatewayConsumerInGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveCloudNativeAPIGatewayConsumerInGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveCloudNativeAPIGatewayConsumerInGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackCloudNativeAPIGatewayMCPToolVersion(self, request):
        r"""修改云原生智能网关MCP Tool

        :param request: Request instance for RollbackCloudNativeAPIGatewayMCPToolVersion.
        :type request: :class:`tencentcloud.cngw.v20230418.models.RollbackCloudNativeAPIGatewayMCPToolVersionRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.RollbackCloudNativeAPIGatewayMCPToolVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackCloudNativeAPIGatewayMCPToolVersion", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackCloudNativeAPIGatewayMCPToolVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindCloudNativeAPIGatewaySecretKey(self, request):
        r"""解绑密钥
        【消费者批量自动分配 API Key｜修改：新增未完成批次保护，字段不变】目标密钥属于批次且对应项处于 Pending/Running/Reconciling 时，解绑返回 OperationDenied.BatchKeyPending。完成后继续原解绑；原 GatewayId/SecretKeyId/ResourceType/ResourceIds 不变，成功不新增业务 Result。解绑不改写批次历史成功，后续批次明文读取返回逐项 OperationDenied.BindingChanged。 完整接口清单与逐项说明：https://iwiki.woa.com/p/4042678235（第 2、2.4 节）。

        :param request: Request instance for UnbindCloudNativeAPIGatewaySecretKey.
        :type request: :class:`tencentcloud.cngw.v20230418.models.UnbindCloudNativeAPIGatewaySecretKeyRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.UnbindCloudNativeAPIGatewaySecretKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindCloudNativeAPIGatewaySecretKey", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindCloudNativeAPIGatewaySecretKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCloudNativeAPIGatewayMCPTools(self, request):
        r"""批量导入从OpenAPI文件中解析的MCP Tools

        :param request: Request instance for UpdateCloudNativeAPIGatewayMCPTools.
        :type request: :class:`tencentcloud.cngw.v20230418.models.UpdateCloudNativeAPIGatewayMCPToolsRequest`
        :rtype: :class:`tencentcloud.cngw.v20230418.models.UpdateCloudNativeAPIGatewayMCPToolsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCloudNativeAPIGatewayMCPTools", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCloudNativeAPIGatewayMCPToolsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))