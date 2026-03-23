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
from tencentcloud.apis.v20240801 import models


class ApisClient(AbstractClient):
    _apiVersion = '2024-08-01'
    _endpoint = 'apis.tencentcloudapi.com'
    _service = 'apis'


    def CreateAgentApp(self, request):
        r"""创建app

        :param request: Request instance for CreateAgentApp.
        :type request: :class:`tencentcloud.apis.v20240801.models.CreateAgentAppRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.CreateAgentAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgentApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAgentAppMcpServers(self, request):
        r"""创建app的mcp server关联

        :param request: Request instance for CreateAgentAppMcpServers.
        :type request: :class:`tencentcloud.apis.v20240801.models.CreateAgentAppMcpServersRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.CreateAgentAppMcpServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgentAppMcpServers", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentAppMcpServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAgentAppModelServices(self, request):
        r"""创建app的model service关联

        :param request: Request instance for CreateAgentAppModelServices.
        :type request: :class:`tencentcloud.apis.v20240801.models.CreateAgentAppModelServicesRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.CreateAgentAppModelServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgentAppModelServices", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentAppModelServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAgentCredential(self, request):
        r"""创建Credential

        :param request: Request instance for CreateAgentCredential.
        :type request: :class:`tencentcloud.apis.v20240801.models.CreateAgentCredentialRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.CreateAgentCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgentCredential", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMcpServer(self, request):
        r"""创建mcp server

        :param request: Request instance for CreateMcpServer.
        :type request: :class:`tencentcloud.apis.v20240801.models.CreateMcpServerRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.CreateMcpServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMcpServer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMcpServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModel(self, request):
        r"""创建模型

        :param request: Request instance for CreateModel.
        :type request: :class:`tencentcloud.apis.v20240801.models.CreateModelRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.CreateModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModelService(self, request):
        r"""创建模型服务

        :param request: Request instance for CreateModelService.
        :type request: :class:`tencentcloud.apis.v20240801.models.CreateModelServiceRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.CreateModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModelService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAgentApp(self, request):
        r"""删除app

        :param request: Request instance for DeleteAgentApp.
        :type request: :class:`tencentcloud.apis.v20240801.models.DeleteAgentAppRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DeleteAgentAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAgentApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAgentAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAgentAppMcpServers(self, request):
        r"""删除app的mcp server

        :param request: Request instance for DeleteAgentAppMcpServers.
        :type request: :class:`tencentcloud.apis.v20240801.models.DeleteAgentAppMcpServersRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DeleteAgentAppMcpServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAgentAppMcpServers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAgentAppMcpServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAgentAppModelServices(self, request):
        r"""删除app的model service关联

        :param request: Request instance for DeleteAgentAppModelServices.
        :type request: :class:`tencentcloud.apis.v20240801.models.DeleteAgentAppModelServicesRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DeleteAgentAppModelServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAgentAppModelServices", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAgentAppModelServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAgentCredential(self, request):
        r"""删除Credential

        :param request: Request instance for DeleteAgentCredential.
        :type request: :class:`tencentcloud.apis.v20240801.models.DeleteAgentCredentialRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DeleteAgentCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAgentCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAgentCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMcpServer(self, request):
        r"""删除mcp server

        :param request: Request instance for DeleteMcpServer.
        :type request: :class:`tencentcloud.apis.v20240801.models.DeleteMcpServerRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DeleteMcpServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMcpServer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMcpServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModel(self, request):
        r"""删除模型

        :param request: Request instance for DeleteModel.
        :type request: :class:`tencentcloud.apis.v20240801.models.DeleteModelRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DeleteModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModelService(self, request):
        r"""删除模型服务

        :param request: Request instance for DeleteModelService.
        :type request: :class:`tencentcloud.apis.v20240801.models.DeleteModelServiceRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DeleteModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModelService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentApp(self, request):
        r"""查询app详情

        :param request: Request instance for DescribeAgentApp.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentAppMcpServers(self, request):
        r"""查询app mcpServer关联列表

        :param request: Request instance for DescribeAgentAppMcpServers.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppMcpServersRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppMcpServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentAppMcpServers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentAppMcpServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentAppModelServices(self, request):
        r"""查询app modelService关联列表

        :param request: Request instance for DescribeAgentAppModelServices.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppModelServicesRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppModelServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentAppModelServices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentAppModelServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentApps(self, request):
        r"""查询app列表

        :param request: Request instance for DescribeAgentApps.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppsRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentAppsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentApps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentAppsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentCredential(self, request):
        r"""查询Credential详情

        :param request: Request instance for DescribeAgentCredential.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeAgentCredentialRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentCredentials(self, request):
        r"""查询Credential列表

        :param request: Request instance for DescribeAgentCredentials.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeAgentCredentialsRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeAgentCredentialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentCredentials", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentCredentialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMcpServer(self, request):
        r"""查询mcp server详情

        :param request: Request instance for DescribeMcpServer.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeMcpServerRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeMcpServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMcpServer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMcpServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMcpServers(self, request):
        r"""查询mcp server列表

        :param request: Request instance for DescribeMcpServers.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeMcpServersRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeMcpServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMcpServers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMcpServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModel(self, request):
        r"""查询模型详情

        :param request: Request instance for DescribeModel.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeModelRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelService(self, request):
        r"""查询模型服务详情

        :param request: Request instance for DescribeModelService.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeModelServiceRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelServices(self, request):
        r"""查询模型服务列表

        :param request: Request instance for DescribeModelServices.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeModelServicesRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeModelServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelServices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModels(self, request):
        r"""查询模型列表

        :param request: Request instance for DescribeModels.
        :type request: :class:`tencentcloud.apis.v20240801.models.DescribeModelsRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.DescribeModelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentApp(self, request):
        r"""修改app

        :param request: Request instance for ModifyAgentApp.
        :type request: :class:`tencentcloud.apis.v20240801.models.ModifyAgentAppRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.ModifyAgentAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentAppModelServices(self, request):
        r"""编辑app的model service关联

        :param request: Request instance for ModifyAgentAppModelServices.
        :type request: :class:`tencentcloud.apis.v20240801.models.ModifyAgentAppModelServicesRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.ModifyAgentAppModelServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentAppModelServices", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentAppModelServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentCredential(self, request):
        r"""修改Credential

        :param request: Request instance for ModifyAgentCredential.
        :type request: :class:`tencentcloud.apis.v20240801.models.ModifyAgentCredentialRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.ModifyAgentCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentCredential", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMcpServer(self, request):
        r"""修改mcp server

        :param request: Request instance for ModifyMcpServer.
        :type request: :class:`tencentcloud.apis.v20240801.models.ModifyMcpServerRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.ModifyMcpServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMcpServer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMcpServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModel(self, request):
        r"""修改模型

        :param request: Request instance for ModifyModel.
        :type request: :class:`tencentcloud.apis.v20240801.models.ModifyModelRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.ModifyModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModelService(self, request):
        r"""修改模型服务

        :param request: Request instance for ModifyModelService.
        :type request: :class:`tencentcloud.apis.v20240801.models.ModifyModelServiceRequest`
        :rtype: :class:`tencentcloud.apis.v20240801.models.ModifyModelServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModelService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModelServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))