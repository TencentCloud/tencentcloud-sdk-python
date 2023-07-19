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
from tencentcloud.iecp.v20210914 import models


class IecpClient(AbstractClient):
    _apiVersion = '2021-09-14'
    _endpoint = 'iecp.tencentcloudapi.com'
    _service = 'iecp'


    def ApplyMarketComponent(self, request):
        """从组件市场选中组件并添加到应用模板列表

        :param request: Request instance for ApplyMarketComponent.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ApplyMarketComponentRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ApplyMarketComponentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyMarketComponent", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyMarketComponentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BuildMessageRoute(self, request):
        """建立消息路由

        :param request: Request instance for BuildMessageRoute.
        :type request: :class:`tencentcloud.iecp.v20210914.models.BuildMessageRouteRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.BuildMessageRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BuildMessageRoute", params, headers=headers)
            response = json.loads(body)
            model = models.BuildMessageRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationVisualization(self, request):
        """创建可视化创建应用模板

        :param request: Request instance for CreateApplicationVisualization.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateApplicationVisualizationRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateApplicationVisualizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationVisualization", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationVisualizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConfigMap(self, request):
        """创建ConfigMap

        :param request: Request instance for CreateConfigMap.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateConfigMapRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateConfigMapResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigMap", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigMapResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeNode(self, request):
        """创建边缘节点

        :param request: Request instance for CreateEdgeNode.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeNodeRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeNode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeNodeBatch(self, request):
        """批量预注册节点

        :param request: Request instance for CreateEdgeNodeBatch.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeNodeBatchRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeNodeBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeNodeBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeNodeBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeNodeGroup(self, request):
        """创建边缘单元NodeGroup

        :param request: Request instance for CreateEdgeNodeGroup.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeNodeGroupRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeNodeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeNodeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeNodeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeNodeUnitTemplate(self, request):
        """创建边缘单元NodeUnit模板

        :param request: Request instance for CreateEdgeNodeUnitTemplate.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeNodeUnitTemplateRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeNodeUnitTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeNodeUnitTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeNodeUnitTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeUnitApplicationVisualization(self, request):
        """可视化创建应用

        :param request: Request instance for CreateEdgeUnitApplicationVisualization.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeUnitApplicationVisualizationRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeUnitApplicationVisualizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeUnitApplicationVisualization", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeUnitApplicationVisualizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeUnitApplicationYaml(self, request):
        """yaml方式创建应用

        :param request: Request instance for CreateEdgeUnitApplicationYaml.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeUnitApplicationYamlRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeUnitApplicationYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeUnitApplicationYaml", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeUnitApplicationYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeUnitCloud(self, request):
        """创建边缘单元

        :param request: Request instance for CreateEdgeUnitCloud.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeUnitCloudRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeUnitCloudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeUnitCloud", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeUnitCloudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeUnitDevices(self, request):
        """批量绑定设备到单元

        :param request: Request instance for CreateEdgeUnitDevices.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeUnitDevicesRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateEdgeUnitDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeUnitDevices", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeUnitDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIotDevice(self, request):
        """创建子设备

        :param request: Request instance for CreateIotDevice.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateIotDeviceRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateIotDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIotDevice", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIotDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMessageRoute(self, request):
        """创建消息路由

        :param request: Request instance for CreateMessageRoute.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateMessageRouteRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateMessageRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMessageRoute", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMessageRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNamespace(self, request):
        """创建命名空间

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecret(self, request):
        """创建Secret

        :param request: Request instance for CreateSecret.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateSecretRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecret", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUpdateNodeUnit(self, request):
        """创建或更新边缘单元NodeUnit

        :param request: Request instance for CreateUpdateNodeUnit.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateUpdateNodeUnitRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateUpdateNodeUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUpdateNodeUnit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUpdateNodeUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserToken(self, request):
        """创建token

        :param request: Request instance for CreateUserToken.
        :type request: :class:`tencentcloud.iecp.v20210914.models.CreateUserTokenRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.CreateUserTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplications(self, request):
        """删除应用模板

        :param request: Request instance for DeleteApplications.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteApplicationsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConfigMap(self, request):
        """删除ConfigMap

        :param request: Request instance for DeleteConfigMap.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteConfigMapRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteConfigMapResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfigMap", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigMapResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeNodeGroup(self, request):
        """删除边缘单元NodeGroup

        :param request: Request instance for DeleteEdgeNodeGroup.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeNodeGroupRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeNodeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeNodeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeNodeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeNodeUnitTemplates(self, request):
        """删除边缘单元NodeUnit模板

        :param request: Request instance for DeleteEdgeNodeUnitTemplates.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeNodeUnitTemplatesRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeNodeUnitTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeNodeUnitTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeNodeUnitTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeNodes(self, request):
        """批量删除边缘节点

        :param request: Request instance for DeleteEdgeNodes.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeNodesRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeUnitApplications(self, request):
        """删除应用列表

        :param request: Request instance for DeleteEdgeUnitApplications.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeUnitApplicationsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeUnitApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeUnitApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeUnitApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeUnitCloud(self, request):
        """删除边缘单元

        :param request: Request instance for DeleteEdgeUnitCloud.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeUnitCloudRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeUnitCloudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeUnitCloud", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeUnitCloudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeUnitDeployGridItem(self, request):
        """重新部署边缘单元指定Grid下应用

        :param request: Request instance for DeleteEdgeUnitDeployGridItem.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeUnitDeployGridItemRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeUnitDeployGridItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeUnitDeployGridItem", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeUnitDeployGridItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeUnitDevices(self, request):
        """批量解绑单元设备

        :param request: Request instance for DeleteEdgeUnitDevices.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeUnitDevicesRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeUnitDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeUnitDevices", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeUnitDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeUnitPod(self, request):
        """删除指定pod

        :param request: Request instance for DeleteEdgeUnitPod.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeUnitPodRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteEdgeUnitPodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeUnitPod", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeUnitPodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIotDevice(self, request):
        """删除设备

        :param request: Request instance for DeleteIotDevice.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteIotDeviceRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteIotDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIotDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIotDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIotDeviceBatch(self, request):
        """批量删除设备

        :param request: Request instance for DeleteIotDeviceBatch.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteIotDeviceBatchRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteIotDeviceBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIotDeviceBatch", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIotDeviceBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMessageRoute(self, request):
        """删除消息路由

        :param request: Request instance for DeleteMessageRoute.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteMessageRouteRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteMessageRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMessageRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMessageRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNamespace(self, request):
        """删除命名空间

        :param request: Request instance for DeleteNamespace.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNodeUnit(self, request):
        """删除边缘单元NodeUnit

        :param request: Request instance for DeleteNodeUnit.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteNodeUnitRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteNodeUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNodeUnit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNodeUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecret(self, request):
        """删除Secret

        :param request: Request instance for DeleteSecret.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DeleteSecretRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DeleteSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecret", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationVisualization(self, request):
        """获取应用模板可视化配置信息

        :param request: Request instance for DescribeApplicationVisualization.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeApplicationVisualizationRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeApplicationVisualizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationVisualization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationVisualizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationYaml(self, request):
        """查询应用模板Yaml

        :param request: Request instance for DescribeApplicationYaml.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeApplicationYamlRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeApplicationYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationYaml", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationYamlError(self, request):
        """检查应用模板的Yaml配置

        :param request: Request instance for DescribeApplicationYamlError.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeApplicationYamlErrorRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeApplicationYamlErrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationYamlError", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationYamlErrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplications(self, request):
        """获取应用模板列表

        :param request: Request instance for DescribeApplications.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeApplicationsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigMap(self, request):
        """获取ConfigMap详情

        :param request: Request instance for DescribeConfigMap.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeConfigMapRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeConfigMapResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigMap", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigMapResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigMapYamlError(self, request):
        """校验ConfigMap的Yaml语法

        :param request: Request instance for DescribeConfigMapYamlError.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeConfigMapYamlErrorRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeConfigMapYamlErrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigMapYamlError", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigMapYamlErrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigMaps(self, request):
        """获取ConfigMap列表

        :param request: Request instance for DescribeConfigMaps.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeConfigMapsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeConfigMapsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigMaps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigMapsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDracoEdgeNodeInstaller(self, request):
        """自动获取Draco设备的安装包

        :param request: Request instance for DescribeDracoEdgeNodeInstaller.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeDracoEdgeNodeInstallerRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeDracoEdgeNodeInstallerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDracoEdgeNodeInstaller", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDracoEdgeNodeInstallerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeAgentNodeInstaller(self, request):
        """获取节点安装信息

        :param request: Request instance for DescribeEdgeAgentNodeInstaller.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeAgentNodeInstallerRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeAgentNodeInstallerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeAgentNodeInstaller", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeAgentNodeInstallerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeDefaultVpc(self, request):
        """获取边缘集群默认VPC信息

        :param request: Request instance for DescribeEdgeDefaultVpc.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeDefaultVpcRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeDefaultVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeDefaultVpc", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeDefaultVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeNode(self, request):
        """获取边缘节点信息

        :param request: Request instance for DescribeEdgeNode.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeNodeRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeNode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeNodePodContainers(self, request):
        """查询节点Pod内的容器列表

        :param request: Request instance for DescribeEdgeNodePodContainers.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeNodePodContainersRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeNodePodContainersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeNodePodContainers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeNodePodContainersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeNodePods(self, request):
        """查询节点Pod列表

        :param request: Request instance for DescribeEdgeNodePods.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeNodePodsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeNodePodsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeNodePods", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeNodePodsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeNodeRemarkList(self, request):
        """获取节点备注信息列表

        :param request: Request instance for DescribeEdgeNodeRemarkList.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeNodeRemarkListRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeNodeRemarkListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeNodeRemarkList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeNodeRemarkListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeNodes(self, request):
        """查询边缘节点列表

        :param request: Request instance for DescribeEdgeNodes.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeNodesRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeOperationLogs(self, request):
        """查询边缘操作日志

        :param request: Request instance for DescribeEdgeOperationLogs.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeOperationLogsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeOperationLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeOperationLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeOperationLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgePod(self, request):
        """查询边缘单元Pod

        :param request: Request instance for DescribeEdgePod.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgePodRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgePodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgePod", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgePodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeSnNodes(self, request):
        """查询预注册节点列表

        :param request: Request instance for DescribeEdgeSnNodes.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeSnNodesRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeSnNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeSnNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeSnNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitApplicationEvents(self, request):
        """获取应用事件列表

        :param request: Request instance for DescribeEdgeUnitApplicationEvents.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationEventsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitApplicationEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitApplicationEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitApplicationLogs(self, request):
        """获取应用日志

        :param request: Request instance for DescribeEdgeUnitApplicationLogs.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationLogsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitApplicationLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitApplicationLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitApplicationPodContainers(self, request):
        """获取应用容器状态

        :param request: Request instance for DescribeEdgeUnitApplicationPodContainers.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationPodContainersRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationPodContainersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitApplicationPodContainers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitApplicationPodContainersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitApplicationPods(self, request):
        """获取应用下Pod状态

        :param request: Request instance for DescribeEdgeUnitApplicationPods.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationPodsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationPodsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitApplicationPods", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitApplicationPodsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitApplicationVisualization(self, request):
        """获取单元可视化配置信息

        :param request: Request instance for DescribeEdgeUnitApplicationVisualization.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationVisualizationRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationVisualizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitApplicationVisualization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitApplicationVisualizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitApplicationYaml(self, request):
        """获取应用的Yaml配置

        :param request: Request instance for DescribeEdgeUnitApplicationYaml.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationYamlRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitApplicationYaml", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitApplicationYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitApplicationYamlError(self, request):
        """检查单元应用的Yaml配置

        :param request: Request instance for DescribeEdgeUnitApplicationYamlError.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationYamlErrorRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationYamlErrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitApplicationYamlError", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitApplicationYamlErrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitApplications(self, request):
        """获取单元下应用列表

        :param request: Request instance for DescribeEdgeUnitApplications.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitCloud(self, request):
        """查询边缘集群详情

        :param request: Request instance for DescribeEdgeUnitCloud.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitCloudRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitCloudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitCloud", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitCloudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitDeployGrid(self, request):
        """查询边缘单元Grid列表

        :param request: Request instance for DescribeEdgeUnitDeployGrid.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitDeployGridRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitDeployGridResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitDeployGrid", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitDeployGridResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitDeployGridItem(self, request):
        """查询边缘单元指定Grid下的部署应用列表

        :param request: Request instance for DescribeEdgeUnitDeployGridItem.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitDeployGridItemRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitDeployGridItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitDeployGridItem", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitDeployGridItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitDeployGridItemYaml(self, request):
        """查询指定Grid下应用的Yaml

        :param request: Request instance for DescribeEdgeUnitDeployGridItemYaml.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitDeployGridItemYamlRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitDeployGridItemYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitDeployGridItemYaml", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitDeployGridItemYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitExtra(self, request):
        """查询边缘单元额外信息

        :param request: Request instance for DescribeEdgeUnitExtra.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitExtraRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitExtraResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitExtra", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitExtraResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitGridEvents(self, request):
        """查询边缘单元Grid事件列表

        :param request: Request instance for DescribeEdgeUnitGridEvents.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitGridEventsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitGridEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitGridEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitGridEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitGridPods(self, request):
        """查询边缘单元Grid的Pod列表

        :param request: Request instance for DescribeEdgeUnitGridPods.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitGridPodsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitGridPodsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitGridPods", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitGridPodsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitMonitorStatus(self, request):
        """查询边缘集群监控状态

        :param request: Request instance for DescribeEdgeUnitMonitorStatus.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitMonitorStatusRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitMonitorStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitMonitorStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitMonitorStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitNodeGroup(self, request):
        """查询边缘集群NodeGroup

        :param request: Request instance for DescribeEdgeUnitNodeGroup.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitNodeGroupRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitNodeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitNodeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitNodeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitNodeUnitTemplates(self, request):
        """查询边缘单元EdgeUnit模板列表

        :param request: Request instance for DescribeEdgeUnitNodeUnitTemplates.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitNodeUnitTemplatesRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitNodeUnitTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitNodeUnitTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitNodeUnitTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeUnitsCloud(self, request):
        """查询边缘单元列表

        :param request: Request instance for DescribeEdgeUnitsCloud.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitsCloudRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeEdgeUnitsCloudResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeUnitsCloud", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeUnitsCloudResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIotDevice(self, request):
        """获取设备信息

        :param request: Request instance for DescribeIotDevice.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeIotDeviceRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeIotDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIotDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIotDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIotDevices(self, request):
        """获取设备列表信息

        :param request: Request instance for DescribeIotDevices.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeIotDevicesRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeIotDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIotDevices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIotDevicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMessageRouteList(self, request):
        """获取消息路由列表

        :param request: Request instance for DescribeMessageRouteList.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeMessageRouteListRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeMessageRouteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageRouteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMessageRouteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMonitorMetrics(self, request):
        """查询边缘单元监控数据

        :param request: Request instance for DescribeMonitorMetrics.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeMonitorMetricsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeMonitorMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonitorMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonitorMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNamespace(self, request):
        """获取命名空间

        :param request: Request instance for DescribeNamespace.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeNamespaceRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNamespaceResources(self, request):
        """获取命名空间下的资源信息

        :param request: Request instance for DescribeNamespaceResources.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeNamespaceResourcesRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeNamespaceResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNamespaceResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNamespaceResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNamespaces(self, request):
        """获取命名空间列表信息

        :param request: Request instance for DescribeNamespaces.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeNamespacesRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeUnit(self, request):
        """查询边缘单元NodeUnit列表

        :param request: Request instance for DescribeNodeUnit.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeNodeUnitRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeNodeUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeUnit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeUnitTemplateOnNodeGroup(self, request):
        """查询指定NodeGroup下NodeUnit模板列表

        :param request: Request instance for DescribeNodeUnitTemplateOnNodeGroup.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeNodeUnitTemplateOnNodeGroupRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeNodeUnitTemplateOnNodeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeUnitTemplateOnNodeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeUnitTemplateOnNodeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecret(self, request):
        """获取Secret详情

        :param request: Request instance for DescribeSecret.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeSecretRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecret", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecretYamlError(self, request):
        """校验Secret的Yaml语法

        :param request: Request instance for DescribeSecretYamlError.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeSecretYamlErrorRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeSecretYamlErrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecretYamlError", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecretYamlErrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecrets(self, request):
        """获取Secrets列表

        :param request: Request instance for DescribeSecrets.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeSecretsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeSecretsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecrets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecretsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeYeheResourceLimit(self, request):
        """查询用户的资源限制

        :param request: Request instance for DescribeYeheResourceLimit.
        :type request: :class:`tencentcloud.iecp.v20210914.models.DescribeYeheResourceLimitRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.DescribeYeheResourceLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeYeheResourceLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeYeheResourceLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMarketComponent(self, request):
        """获取组件市场的组件信息

        :param request: Request instance for GetMarketComponent.
        :type request: :class:`tencentcloud.iecp.v20210914.models.GetMarketComponentRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.GetMarketComponentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMarketComponent", params, headers=headers)
            response = json.loads(body)
            model = models.GetMarketComponentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMarketComponentList(self, request):
        """获取组件市场组件列表

        :param request: Request instance for GetMarketComponentList.
        :type request: :class:`tencentcloud.iecp.v20210914.models.GetMarketComponentListRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.GetMarketComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMarketComponentList", params, headers=headers)
            response = json.loads(body)
            model = models.GetMarketComponentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationBasicInfo(self, request):
        """修改应用模板基本信息

        :param request: Request instance for ModifyApplicationBasicInfo.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyApplicationBasicInfoRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyApplicationBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationVisualization(self, request):
        """修改应用模板配置

        :param request: Request instance for ModifyApplicationVisualization.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyApplicationVisualizationRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyApplicationVisualizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationVisualization", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationVisualizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConfigMap(self, request):
        """修改ConfigMap

        :param request: Request instance for ModifyConfigMap.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyConfigMapRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyConfigMapResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConfigMap", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConfigMapResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeDracoNode(self, request):
        """编辑draco设备信息

        :param request: Request instance for ModifyEdgeDracoNode.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeDracoNodeRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeDracoNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeDracoNode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeDracoNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeNodeLabels(self, request):
        """编辑边缘节点标签

        :param request: Request instance for ModifyEdgeNodeLabels.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeNodeLabelsRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeNodeLabelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeNodeLabels", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeNodeLabelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeUnit(self, request):
        """修改边缘集群

        :param request: Request instance for ModifyEdgeUnit.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeUnit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeUnitApplicationBasicInfo(self, request):
        """修改单元应用基本信息

        :param request: Request instance for ModifyEdgeUnitApplicationBasicInfo.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitApplicationBasicInfoRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitApplicationBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeUnitApplicationBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeUnitApplicationBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeUnitApplicationVisualization(self, request):
        """可视化修改应用配置

        :param request: Request instance for ModifyEdgeUnitApplicationVisualization.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitApplicationVisualizationRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitApplicationVisualizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeUnitApplicationVisualization", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeUnitApplicationVisualizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeUnitApplicationYaml(self, request):
        """Yaml方式修改应用配置

        :param request: Request instance for ModifyEdgeUnitApplicationYaml.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitApplicationYamlRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitApplicationYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeUnitApplicationYaml", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeUnitApplicationYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeUnitCloudApi(self, request):
        """更新边缘单元信息

        :param request: Request instance for ModifyEdgeUnitCloudApi.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitCloudApiRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitCloudApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeUnitCloudApi", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeUnitCloudApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeUnitDeployGridItem(self, request):
        """修改边缘单元Grid部署应用副本数

        :param request: Request instance for ModifyEdgeUnitDeployGridItem.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitDeployGridItemRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyEdgeUnitDeployGridItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeUnitDeployGridItem", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeUnitDeployGridItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIotDevice(self, request):
        """修改设备信息

        :param request: Request instance for ModifyIotDevice.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyIotDeviceRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyIotDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIotDevice", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIotDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNodeUnitTemplate(self, request):
        """修改边缘单元NodeUnit模板

        :param request: Request instance for ModifyNodeUnitTemplate.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifyNodeUnitTemplateRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifyNodeUnitTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNodeUnitTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNodeUnitTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecret(self, request):
        """修改Secret

        :param request: Request instance for ModifySecret.
        :type request: :class:`tencentcloud.iecp.v20210914.models.ModifySecretRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.ModifySecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecret", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RedeployEdgeUnitApplication(self, request):
        """单元应用重部署

        :param request: Request instance for RedeployEdgeUnitApplication.
        :type request: :class:`tencentcloud.iecp.v20210914.models.RedeployEdgeUnitApplicationRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.RedeployEdgeUnitApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RedeployEdgeUnitApplication", params, headers=headers)
            response = json.loads(body)
            model = models.RedeployEdgeUnitApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetRouteOnOff(self, request):
        """开关消息路由

        :param request: Request instance for SetRouteOnOff.
        :type request: :class:`tencentcloud.iecp.v20210914.models.SetRouteOnOffRequest`
        :rtype: :class:`tencentcloud.iecp.v20210914.models.SetRouteOnOffResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetRouteOnOff", params, headers=headers)
            response = json.loads(body)
            model = models.SetRouteOnOffResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))