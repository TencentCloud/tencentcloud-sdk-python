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
from tencentcloud.tsf.v20180326 import models


class TsfClient(AbstractClient):
    _apiVersion = '2018-03-26'
    _endpoint = 'tsf.tencentcloudapi.com'
    _service = 'tsf'


    def AddClusterInstances(self, request):
        """添加云主机节点至TSF集群

        :param request: Request instance for AddClusterInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.AddClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.AddClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AddClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddInstances(self, request):
        """添加云主机节点至TSF集群

        :param request: Request instance for AddInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.AddInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.AddInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AddInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateBusinessLogConfig(self, request):
        """关联日志配置项到应用

        :param request: Request instance for AssociateBusinessLogConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.AssociateBusinessLogConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.AssociateBusinessLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateBusinessLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateBusinessLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateConfigWithGroup(self, request):
        """关联投递配置到部署组

        :param request: Request instance for AssociateConfigWithGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.AssociateConfigWithGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.AssociateConfigWithGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateConfigWithGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateConfigWithGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindApiGroup(self, request):
        """网关与API分组批量绑定

        :param request: Request instance for BindApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.BindApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.BindApiGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindApiGroup", params, headers=headers)
            response = json.loads(body)
            model = models.BindApiGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindPlugin(self, request):
        """插件与网关分组/API批量绑定

        :param request: Request instance for BindPlugin.
        :type request: :class:`tencentcloud.tsf.v20180326.models.BindPluginRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.BindPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.BindPluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeApiUsableStatus(self, request):
        """启用或禁用API

        :param request: Request instance for ChangeApiUsableStatus.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ChangeApiUsableStatusRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ChangeApiUsableStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeApiUsableStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeApiUsableStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ContinueRunFailedTaskBatch(self, request):
        """对执行失败的任务批次执行续跑

        :param request: Request instance for ContinueRunFailedTaskBatch.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ContinueRunFailedTaskBatchRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ContinueRunFailedTaskBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ContinueRunFailedTaskBatch", params, headers=headers)
            response = json.loads(body)
            model = models.ContinueRunFailedTaskBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAllGatewayApiAsync(self, request):
        """一键导入API分组

        :param request: Request instance for CreateAllGatewayApiAsync.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateAllGatewayApiAsyncRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateAllGatewayApiAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAllGatewayApiAsync", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAllGatewayApiAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApiGroup(self, request):
        """创建API分组

        :param request: Request instance for CreateApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateApiGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApiRateLimitRule(self, request):
        """创建API限流规则

        :param request: Request instance for CreateApiRateLimitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateApiRateLimitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateApiRateLimitRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiRateLimitRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiRateLimitRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApiRateLimitRuleWithDetailResp(self, request):
        """创建API限流规则,并返回规则信息

        :param request: Request instance for CreateApiRateLimitRuleWithDetailResp.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateApiRateLimitRuleWithDetailRespRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateApiRateLimitRuleWithDetailRespResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiRateLimitRuleWithDetailResp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiRateLimitRuleWithDetailRespResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplication(self, request):
        """创建应用

        :param request: Request instance for CreateApplication.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateApplicationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplication", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        """创建集群

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateClusterResponse`

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


    def CreateConfig(self, request):
        """创建配置项

        :param request: Request instance for CreateConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConfigTemplate(self, request):
        """创建参数模板

        :param request: Request instance for CreateConfigTemplate.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateConfigTemplateRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateConfigTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConfigTemplateWithDetailResp(self, request):
        """创建参数模板，并返回模板详细信息

        :param request: Request instance for CreateConfigTemplateWithDetailResp.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateConfigTemplateWithDetailRespRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateConfigTemplateWithDetailRespResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigTemplateWithDetailResp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigTemplateWithDetailRespResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConfigWithDetailResp(self, request):
        """创建配置项，返回详细信息

        :param request: Request instance for CreateConfigWithDetailResp.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateConfigWithDetailRespRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateConfigWithDetailRespResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigWithDetailResp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigWithDetailRespResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateContainGroup(self, request):
        """（已废弃，请使用 CreateGroup 和 DeployContainerGroup 创建和部署容器部署组）创建容器部署组

        :param request: Request instance for CreateContainGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateContainGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateContainGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateContainGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateContainGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFileConfig(self, request):
        """创建文件配置项

        :param request: Request instance for CreateFileConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateFileConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateFileConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFileConfigWithDetailResp(self, request):
        """创建文件配置项，返回详细信息

        :param request: Request instance for CreateFileConfigWithDetailResp.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateFileConfigWithDetailRespRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateFileConfigWithDetailRespResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileConfigWithDetailResp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileConfigWithDetailRespResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGatewayApi(self, request):
        """批量导入API至api分组(也支持新建API到分组)

        :param request: Request instance for CreateGatewayApi.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateGatewayApiRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateGatewayApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGatewayApi", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGatewayApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGroup(self, request):
        """创建虚拟机部署组

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLane(self, request):
        """创建泳道

        :param request: Request instance for CreateLane.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateLaneRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateLaneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLane", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLaneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLaneRule(self, request):
        """创建泳道规则

        :param request: Request instance for CreateLaneRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateLaneRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateLaneRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLaneRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLaneRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMicroservice(self, request):
        """新增微服务

        :param request: Request instance for CreateMicroservice.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateMicroserviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMicroservice", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMicroserviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMicroserviceWithDetailResp(self, request):
        """新增微服务返回id

        :param request: Request instance for CreateMicroserviceWithDetailResp.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateMicroserviceWithDetailRespRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateMicroserviceWithDetailRespResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMicroserviceWithDetailResp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMicroserviceWithDetailRespResponse()
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
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateNamespaceResponse`

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


    def CreatePathRewrites(self, request):
        """创建路径重写

        :param request: Request instance for CreatePathRewrites.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreatePathRewritesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreatePathRewritesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePathRewrites", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePathRewritesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePathRewritesWithDetailResp(self, request):
        """创建路径重写，并返回路径重写规则信息

        :param request: Request instance for CreatePathRewritesWithDetailResp.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreatePathRewritesWithDetailRespRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreatePathRewritesWithDetailRespResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePathRewritesWithDetailResp", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePathRewritesWithDetailRespResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePublicConfig(self, request):
        """创建公共配置项

        :param request: Request instance for CreatePublicConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreatePublicConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreatePublicConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePublicConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePublicConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePublicConfigWithDetailResp(self, request):
        """创建公共配置项，并返回配置项详细信息

        :param request: Request instance for CreatePublicConfigWithDetailResp.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreatePublicConfigWithDetailRespRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreatePublicConfigWithDetailRespResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePublicConfigWithDetailResp", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePublicConfigWithDetailRespResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRepository(self, request):
        """创建仓库

        :param request: Request instance for CreateRepository.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateRepositoryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRepository", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTask(self, request):
        """创建任务

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskFlow(self, request):
        """创建工作流

        :param request: Request instance for CreateTaskFlow.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateTaskFlowRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateTaskFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUnitNamespaces(self, request):
        """批量创建单元化命名空间

        :param request: Request instance for CreateUnitNamespaces.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateUnitNamespacesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateUnitNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUnitNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUnitNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUnitRule(self, request):
        """创建单元化规则

        :param request: Request instance for CreateUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateUnitRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUnitRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUnitRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUnitRuleWithDetailResp(self, request):
        """创建单元化规则, 并返回详细信息

        :param request: Request instance for CreateUnitRuleWithDetailResp.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateUnitRuleWithDetailRespRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateUnitRuleWithDetailRespResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUnitRuleWithDetailResp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUnitRuleWithDetailRespResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApiGroup(self, request):
        """删除Api分组

        :param request: Request instance for DeleteApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteApiGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApiGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApiGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApiRateLimitRule(self, request):
        """删除API限流规则

        :param request: Request instance for DeleteApiRateLimitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteApiRateLimitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteApiRateLimitRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApiRateLimitRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApiRateLimitRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplication(self, request):
        """删除应用

        :param request: Request instance for DeleteApplication.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteApplicationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationResponse()
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
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteClusterResponse`

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


    def DeleteConfig(self, request):
        """删除配置项

        :param request: Request instance for DeleteConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConfigTemplate(self, request):
        """删除模板

        :param request: Request instance for DeleteConfigTemplate.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteConfigTemplateRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteConfigTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfigTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteContainerGroup(self, request):
        """删除容器部署组

        :param request: Request instance for DeleteContainerGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteContainerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteContainerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteContainerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFileConfig(self, request):
        """删除文件配置项

        :param request: Request instance for DeleteFileConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteFileConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteFileConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFileConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFileConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGatewayApi(self, request):
        """批量删除API

        :param request: Request instance for DeleteGatewayApi.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteGatewayApiRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteGatewayApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGatewayApi", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGatewayApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGroup(self, request):
        """删除容器部署组

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageTags(self, request):
        """批量删除镜像版本

        :param request: Request instance for DeleteImageTags.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteImageTagsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteImageTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageTags", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLane(self, request):
        """删除泳道

        :param request: Request instance for DeleteLane.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteLaneRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteLaneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLane", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLaneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLaneRule(self, request):
        """删除泳道规则

        :param request: Request instance for DeleteLaneRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteLaneRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteLaneRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLaneRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLaneRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMicroservice(self, request):
        """删除微服务

        :param request: Request instance for DeleteMicroservice.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteMicroserviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMicroservice", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMicroserviceResponse()
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
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteNamespaceResponse`

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


    def DeletePathRewrites(self, request):
        """删除路径重写

        :param request: Request instance for DeletePathRewrites.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeletePathRewritesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeletePathRewritesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePathRewrites", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePathRewritesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePkgs(self, request):
        """从软件仓库批量删除程序包。
        一次最多支持删除1000个包，数量超过1000，返回UpperDeleteLimit错误。

        :param request: Request instance for DeletePkgs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeletePkgsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeletePkgsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePkgs", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePkgsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePublicConfig(self, request):
        """删除公共配置项

        :param request: Request instance for DeletePublicConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeletePublicConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeletePublicConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePublicConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePublicConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRepository(self, request):
        """删除仓库

        :param request: Request instance for DeleteRepository.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteRepositoryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRepository", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServerlessGroup(self, request):
        """删除Serverless部署组

        :param request: Request instance for DeleteServerlessGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteServerlessGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteServerlessGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServerlessGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServerlessGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTask(self, request):
        """删除任务

        :param request: Request instance for DeleteTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUnitNamespaces(self, request):
        """删除单元化命名空间

        :param request: Request instance for DeleteUnitNamespaces.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteUnitNamespacesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteUnitNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUnitNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUnitNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUnitRule(self, request):
        """删除单元化规则

        :param request: Request instance for DeleteUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteUnitRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUnitRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUnitRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployContainerGroup(self, request):
        """部署容器应用-更新

        :param request: Request instance for DeployContainerGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeployContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeployContainerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployContainerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeployContainerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployGroup(self, request):
        """部署虚拟机部署组应用

        :param request: Request instance for DeployGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeployGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeployGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeployGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiDetail(self, request):
        """查询API详情

        :param request: Request instance for DescribeApiDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiGroup(self, request):
        """查询API分组

        :param request: Request instance for DescribeApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiGroups(self, request):
        """查询API 分组信息列表

        :param request: Request instance for DescribeApiGroups.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiRateLimitRules(self, request):
        """查询API限流规则

        :param request: Request instance for DescribeApiRateLimitRules.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiRateLimitRulesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiRateLimitRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiRateLimitRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiRateLimitRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiUseDetail(self, request):
        """查询网关API监控明细数据

        :param request: Request instance for DescribeApiUseDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiUseDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiUseDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiUseDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiUseDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiVersions(self, request):
        """查询API 版本

        :param request: Request instance for DescribeApiVersions.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiVersionsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplication(self, request):
        """获取应用详情

        :param request: Request instance for DescribeApplication.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationAttribute(self, request):
        """获取应用列表其它字段，如实例数量信息等

        :param request: Request instance for DescribeApplicationAttribute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationAttributeRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationBusinessLogConfig(self, request):
        """查询应用关联日志配置项信息

        :param request: Request instance for DescribeApplicationBusinessLogConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationBusinessLogConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationBusinessLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationBusinessLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationBusinessLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplications(self, request):
        """获取应用列表

        :param request: Request instance for DescribeApplications.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationsResponse`

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


    def DescribeBasicResourceUsage(self, request):
        """TSF基本资源信息概览接口

        :param request: Request instance for DescribeBasicResourceUsage.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeBasicResourceUsageRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeBasicResourceUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBasicResourceUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBasicResourceUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBusinessLogConfig(self, request):
        """查询业务日志配置项信息

        :param request: Request instance for DescribeBusinessLogConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeBusinessLogConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeBusinessLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBusinessLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBusinessLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBusinessLogConfigs(self, request):
        """查询日志配置项列表

        :param request: Request instance for DescribeBusinessLogConfigs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeBusinessLogConfigsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeBusinessLogConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBusinessLogConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBusinessLogConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterInstances(self, request):
        """查询集群实例

        :param request: Request instance for DescribeClusterInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterInstancesResponse()
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
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeClustersResponse`

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


    def DescribeConfig(self, request):
        """查询配置

        :param request: Request instance for DescribeConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigReleaseLogs(self, request):
        """查询配置发布历史

        :param request: Request instance for DescribeConfigReleaseLogs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigReleaseLogsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigReleaseLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigReleaseLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigReleaseLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigReleases(self, request):
        """查询配置发布信息

        :param request: Request instance for DescribeConfigReleases.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigReleasesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigReleasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigReleases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigReleasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigSummary(self, request):
        """查询配置汇总列表

        :param request: Request instance for DescribeConfigSummary.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigSummaryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigTemplate(self, request):
        """导入配置

        :param request: Request instance for DescribeConfigTemplate.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigTemplateRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigs(self, request):
        """查询配置项列表

        :param request: Request instance for DescribeConfigs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerEvents(self, request):
        """获取容器事件列表

        :param request: Request instance for DescribeContainerEvents.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerEventsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerGroupAttribute(self, request):
        """获取部署组其他字段-用于前端并发调用

        :param request: Request instance for DescribeContainerGroupAttribute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupAttributeRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerGroupDeployInfo(self, request):
        """获取部署组详情

        :param request: Request instance for DescribeContainerGroupDeployInfo.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupDeployInfoRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupDeployInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerGroupDeployInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerGroupDeployInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerGroupDetail(self, request):
        """容器部署组详情（已废弃，请使用  DescribeContainerGroupDeployInfo）

        :param request: Request instance for DescribeContainerGroupDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerGroupDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerGroupDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerGroups(self, request):
        """容器部署组列表

        :param request: Request instance for DescribeContainerGroups.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCreateGatewayApiStatus(self, request):
        """查询一键导入API分组任务的状态

        :param request: Request instance for DescribeCreateGatewayApiStatus.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeCreateGatewayApiStatusRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeCreateGatewayApiStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCreateGatewayApiStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCreateGatewayApiStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeliveryConfig(self, request):
        """获取单个投递项配置信息

        :param request: Request instance for DescribeDeliveryConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeDeliveryConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeDeliveryConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeliveryConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeliveryConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeliveryConfigByGroupId(self, request):
        """用部署组id获取绑定信息

        :param request: Request instance for DescribeDeliveryConfigByGroupId.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeDeliveryConfigByGroupIdRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeDeliveryConfigByGroupIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeliveryConfigByGroupId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeliveryConfigByGroupIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeliveryConfigs(self, request):
        """获取多个投递项配置

        :param request: Request instance for DescribeDeliveryConfigs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeDeliveryConfigsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeDeliveryConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeliveryConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeliveryConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDownloadInfo(self, request):
        """TSF上传的程序包存放在腾讯云对象存储（COS）中，通过该API可以获取从COS下载程序包需要的信息，包括包所在的桶、存储路径、鉴权信息等，之后使用COS API（或SDK）进行下载。
        COS相关文档请查阅：https://cloud.tencent.com/document/product/436

        :param request: Request instance for DescribeDownloadInfo.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeDownloadInfoRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeDownloadInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDownloadInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDownloadInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnabledUnitRule(self, request):
        """查询生效的单元化规则

        :param request: Request instance for DescribeEnabledUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeEnabledUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeEnabledUnitRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnabledUnitRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnabledUnitRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileConfigReleases(self, request):
        """查询文件配置项发布信息

        :param request: Request instance for DescribeFileConfigReleases.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeFileConfigReleasesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeFileConfigReleasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileConfigReleases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileConfigReleasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileConfigs(self, request):
        """查询文件配置项列表

        :param request: Request instance for DescribeFileConfigs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeFileConfigsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeFileConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlowLastBatchState(self, request):
        """查询工作流最新一个批次的状态信息

        :param request: Request instance for DescribeFlowLastBatchState.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeFlowLastBatchStateRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeFlowLastBatchStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowLastBatchState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowLastBatchStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayAllGroupApis(self, request):
        """查询网关所有分组下Api列表

        :param request: Request instance for DescribeGatewayAllGroupApis.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGatewayAllGroupApisRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGatewayAllGroupApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayAllGroupApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayAllGroupApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayApis(self, request):
        """查询API分组下的Api列表信息

        :param request: Request instance for DescribeGatewayApis.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGatewayApisRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGatewayApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayMonitorOverview(self, request):
        """查询网关监控概览

        :param request: Request instance for DescribeGatewayMonitorOverview.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGatewayMonitorOverviewRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGatewayMonitorOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayMonitorOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayMonitorOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroup(self, request):
        """查询虚拟机部署组详情

        :param request: Request instance for DescribeGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupAttribute(self, request):
        """获取部署组其他属性

        :param request: Request instance for DescribeGroupAttribute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupAttributeRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupBindedGateways(self, request):
        """查询某个API分组已绑定的网关部署组信息列表

        :param request: Request instance for DescribeGroupBindedGateways.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupBindedGatewaysRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupBindedGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupBindedGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupBindedGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupBusinessLogConfigs(self, request):
        """查询分组管理日志配置列表

        :param request: Request instance for DescribeGroupBusinessLogConfigs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupBusinessLogConfigsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupBusinessLogConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupBusinessLogConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupBusinessLogConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupGateways(self, request):
        """查询某个网关绑定的API 分组信息列表

        :param request: Request instance for DescribeGroupGateways.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupGatewaysRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupInstances(self, request):
        """查询虚拟机部署组云主机列表

        :param request: Request instance for DescribeGroupInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupRelease(self, request):
        """查询部署组相关的发布信息

        :param request: Request instance for DescribeGroupRelease.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupReleaseRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupRelease", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupUseDetail(self, request):
        """查询网关分组监控明细数据

        :param request: Request instance for DescribeGroupUseDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupUseDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupUseDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupUseDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupUseDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroups(self, request):
        """获取虚拟机部署组列表

        :param request: Request instance for DescribeGroups.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupsWithPlugin(self, request):
        """查询某个插件下绑定或未绑定的API分组

        :param request: Request instance for DescribeGroupsWithPlugin.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupsWithPluginRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupsWithPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupsWithPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupsWithPluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRepository(self, request):
        """查询镜像仓库列表

        :param request: Request instance for DescribeImageRepository.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeImageRepositoryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeImageRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRepository", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageTags(self, request):
        """镜像版本列表

        :param request: Request instance for DescribeImageTags.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeImageTagsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeImageTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInovcationIndicators(self, request):
        """废弃

        :param request: Request instance for DescribeInovcationIndicators.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeInovcationIndicatorsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeInovcationIndicatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInovcationIndicators", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInovcationIndicatorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """无

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInvocationMetricDataCurve(self, request):
        """查询调用指标数据变化曲线

        :param request: Request instance for DescribeInvocationMetricDataCurve.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeInvocationMetricDataCurveRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeInvocationMetricDataCurveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocationMetricDataCurve", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvocationMetricDataCurveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInvocationMetricDataDimension(self, request):
        """查询维度

        :param request: Request instance for DescribeInvocationMetricDataDimension.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeInvocationMetricDataDimensionRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeInvocationMetricDataDimensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocationMetricDataDimension", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvocationMetricDataDimensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInvocationMetricDataPoint(self, request):
        """查询单值指标维度

        :param request: Request instance for DescribeInvocationMetricDataPoint.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeInvocationMetricDataPointRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeInvocationMetricDataPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocationMetricDataPoint", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvocationMetricDataPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInvocationMetricScatterPlot(self, request):
        """查询调用指标数据散点图

        :param request: Request instance for DescribeInvocationMetricScatterPlot.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeInvocationMetricScatterPlotRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeInvocationMetricScatterPlotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocationMetricScatterPlot", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvocationMetricScatterPlotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJvmMonitor(self, request):
        """查询java实例jvm监控数据,返回数据可选

        :param request: Request instance for DescribeJvmMonitor.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeJvmMonitorRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeJvmMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJvmMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJvmMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLaneRules(self, request):
        """查询泳道规则列表

        :param request: Request instance for DescribeLaneRules.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeLaneRulesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeLaneRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLaneRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLaneRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLanes(self, request):
        """查询泳道列表

        :param request: Request instance for DescribeLanes.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeLanesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeLanesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLanes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLanesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMicroservice(self, request):
        """查询微服务详情

        :param request: Request instance for DescribeMicroservice.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroserviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMicroservice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMicroserviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMicroservices(self, request):
        """获取微服务列表

        :param request: Request instance for DescribeMicroservices.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroservicesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroservicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMicroservices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMicroservicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMsApiList(self, request):
        """查询服务API列表

        :param request: Request instance for DescribeMsApiList.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeMsApiListRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeMsApiListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMsApiList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMsApiListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewInvocation(self, request):
        """服务调用监控统计概览

        :param request: Request instance for DescribeOverviewInvocation.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeOverviewInvocationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeOverviewInvocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewInvocation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewInvocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePathRewrite(self, request):
        """查询路径重写

        :param request: Request instance for DescribePathRewrite.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePathRewriteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePathRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePathRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePathRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePathRewrites(self, request):
        """查询路径重写列表

        :param request: Request instance for DescribePathRewrites.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePathRewritesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePathRewritesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePathRewrites", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePathRewritesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePkgs(self, request):
        """无

        :param request: Request instance for DescribePkgs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePkgsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePkgsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePkgs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePkgsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePluginInstances(self, request):
        """分页查询网关分组/API绑定（或未绑定）的插件列表

        :param request: Request instance for DescribePluginInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePluginInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePluginInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePluginInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePodInstances(self, request):
        """获取部署组实例列表

        :param request: Request instance for DescribePodInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePodInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePodInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePodInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePodInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrograms(self, request):
        """查询数据集列表

        :param request: Request instance for DescribePrograms.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeProgramsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeProgramsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrograms", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProgramsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicConfig(self, request):
        """查询公共配置（单条）

        :param request: Request instance for DescribePublicConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicConfigReleaseLogs(self, request):
        """查询公共配置发布历史

        :param request: Request instance for DescribePublicConfigReleaseLogs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigReleaseLogsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigReleaseLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicConfigReleaseLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicConfigReleaseLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicConfigReleases(self, request):
        """查询公共配置发布信息

        :param request: Request instance for DescribePublicConfigReleases.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigReleasesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigReleasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicConfigReleases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicConfigReleasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicConfigSummary(self, request):
        """查询公共配置汇总列表

        :param request: Request instance for DescribePublicConfigSummary.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigSummaryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicConfigSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicConfigSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicConfigs(self, request):
        """查询公共配置项列表

        :param request: Request instance for DescribePublicConfigs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleasedConfig(self, request):
        """查询group发布的配置

        :param request: Request instance for DescribeReleasedConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeReleasedConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeReleasedConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleasedConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleasedConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRepositories(self, request):
        """查询仓库列表

        :param request: Request instance for DescribeRepositories.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeRepositoriesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeRepositoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRepositories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRepositoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRepository(self, request):
        """查询仓库信息

        :param request: Request instance for DescribeRepository.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeRepositoryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRepository", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceTaskStatus(self, request):
        """资源任务的执行状态描述接口

        :param request: Request instance for DescribeResourceTaskStatus.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeResourceTaskStatusRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeResourceTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSimpleApplications(self, request):
        """查询简单应用列表

        :param request: Request instance for DescribeSimpleApplications.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleApplicationsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSimpleApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSimpleApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSimpleClusters(self, request):
        """查询简单集群列表

        :param request: Request instance for DescribeSimpleClusters.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleClustersRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSimpleClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSimpleClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSimpleGroups(self, request):
        """查询简单部署组列表

        :param request: Request instance for DescribeSimpleGroups.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSimpleGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSimpleGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSimpleNamespaces(self, request):
        """查询简单命名空间列表

        :param request: Request instance for DescribeSimpleNamespaces.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleNamespacesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSimpleNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSimpleNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStatistics(self, request):
        """服务统计页面：接口和服务维度

        :param request: Request instance for DescribeStatistics.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeStatisticsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskDetail(self, request):
        """查询任务详情

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLastStatus(self, request):
        """查询任务最近一次执行状态

        :param request: Request instance for DescribeTaskLastStatus.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskLastStatusRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskLastStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLastStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLastStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskRecords(self, request):
        """翻页查询任务列表

        :param request: Request instance for DescribeTaskRecords.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskRecordsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnitApiUseDetail(self, request):
        """查询网关API监控明细数据（仅单元化网关），非单元化网关使用DescribeApiUseDetail

        :param request: Request instance for DescribeUnitApiUseDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitApiUseDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitApiUseDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnitApiUseDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnitApiUseDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnitNamespaces(self, request):
        """查询单元化命名空间列表

        :param request: Request instance for DescribeUnitNamespaces.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitNamespacesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnitNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnitNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnitRule(self, request):
        """查询单元化规则详情

        :param request: Request instance for DescribeUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnitRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnitRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnitRules(self, request):
        """查询单元化规则列表

        :param request: Request instance for DescribeUnitRules.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitRulesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnitRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnitRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnitRulesV2(self, request):
        """查询单元化规则列表V2

        :param request: Request instance for DescribeUnitRulesV2.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitRulesV2Request`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitRulesV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnitRulesV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnitRulesV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUploadInfo(self, request):
        """TSF会将软件包上传到腾讯云对象存储（COS）。调用此接口获取上传信息，如目标地域，桶，包Id，存储路径，鉴权信息等，之后请使用COS API（或SDK）进行上传。
        COS相关文档请查阅：https://cloud.tencent.com/document/product/436

        :param request: Request instance for DescribeUploadInfo.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUploadInfoRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUploadInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUploadInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUploadInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsableUnitNamespaces(self, request):
        """查询可用于被导入的命名空间列表

        :param request: Request instance for DescribeUsableUnitNamespaces.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUsableUnitNamespacesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUsableUnitNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsableUnitNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsableUnitNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableTask(self, request):
        """停用任务

        :param request: Request instance for DisableTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DisableTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DisableTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableTask", params, headers=headers)
            response = json.loads(body)
            model = models.DisableTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableTaskFlow(self, request):
        """停用工作流

        :param request: Request instance for DisableTaskFlow.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DisableTaskFlowRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DisableTaskFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableTaskFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DisableTaskFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableUnitRoute(self, request):
        """禁用单元化路由

        :param request: Request instance for DisableUnitRoute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DisableUnitRouteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DisableUnitRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableUnitRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DisableUnitRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableUnitRule(self, request):
        """禁用单元化规则

        :param request: Request instance for DisableUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DisableUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DisableUnitRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableUnitRule", params, headers=headers)
            response = json.loads(body)
            model = models.DisableUnitRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateBusinessLogConfig(self, request):
        """取消关联业务日志配置项和应用

        :param request: Request instance for DisassociateBusinessLogConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DisassociateBusinessLogConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DisassociateBusinessLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateBusinessLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateBusinessLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateKafkaConfig(self, request):
        """取消关联投递信息和部署组

        :param request: Request instance for DisassociateKafkaConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DisassociateKafkaConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DisassociateKafkaConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateKafkaConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateKafkaConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DraftApiGroup(self, request):
        """下线Api分组

        :param request: Request instance for DraftApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DraftApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DraftApiGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DraftApiGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DraftApiGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableTask(self, request):
        """启用任务

        :param request: Request instance for EnableTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.EnableTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.EnableTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableTask", params, headers=headers)
            response = json.loads(body)
            model = models.EnableTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableTaskFlow(self, request):
        """启用工作流

        :param request: Request instance for EnableTaskFlow.
        :type request: :class:`tencentcloud.tsf.v20180326.models.EnableTaskFlowRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.EnableTaskFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableTaskFlow", params, headers=headers)
            response = json.loads(body)
            model = models.EnableTaskFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableUnitRoute(self, request):
        """启用单元化路由

        :param request: Request instance for EnableUnitRoute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.EnableUnitRouteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.EnableUnitRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableUnitRoute", params, headers=headers)
            response = json.loads(body)
            model = models.EnableUnitRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableUnitRule(self, request):
        """启用单元化规则

        :param request: Request instance for EnableUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.EnableUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.EnableUnitRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableUnitRule", params, headers=headers)
            response = json.loads(body)
            model = models.EnableUnitRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteTask(self, request):
        """手动执行一次任务

        :param request: Request instance for ExecuteTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ExecuteTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ExecuteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteTask", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteTaskFlow(self, request):
        """执行一次工作流

        :param request: Request instance for ExecuteTaskFlow.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ExecuteTaskFlowRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ExecuteTaskFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteTaskFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteTaskFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExpandGroup(self, request):
        """虚拟机部署组添加实例

        :param request: Request instance for ExpandGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ExpandGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ExpandGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExpandGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ExpandGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplication(self, request):
        """修改应用

        :param request: Request instance for ModifyApplication.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyApplicationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCluster(self, request):
        """修改集群信息

        :param request: Request instance for ModifyCluster.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyClusterRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyClusterResponse`

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


    def ModifyContainerGroup(self, request):
        """修改容器部署组

        :param request: Request instance for ModifyContainerGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyContainerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyContainerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyContainerReplicas(self, request):
        """修改容器部署组实例数

        :param request: Request instance for ModifyContainerReplicas.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerReplicasRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerReplicasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyContainerReplicas", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyContainerReplicasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGroup(self, request):
        """更新部署组信息

        :param request: Request instance for ModifyGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLane(self, request):
        """更新泳道信息

        :param request: Request instance for ModifyLane.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyLaneRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyLaneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLane", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLaneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLaneRule(self, request):
        """更新泳道规则

        :param request: Request instance for ModifyLaneRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyLaneRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyLaneRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLaneRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLaneRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMicroservice(self, request):
        """修改微服务详情

        :param request: Request instance for ModifyMicroservice.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyMicroserviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMicroservice", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMicroserviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNamespace(self, request):
        """修改命名空间

        :param request: Request instance for ModifyNamespace.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyNamespaceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPathRewrite(self, request):
        """修改路径重写

        :param request: Request instance for ModifyPathRewrite.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyPathRewriteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyPathRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPathRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPathRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTask(self, request):
        """修改任务

        :param request: Request instance for ModifyTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUploadInfo(self, request):
        """调用该接口和COS的上传接口后，需要调用此接口更新TSF中保存的程序包状态。
        调用此接口完成后，才标志上传包流程结束。

        :param request: Request instance for ModifyUploadInfo.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyUploadInfoRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyUploadInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUploadInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUploadInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OperateApplicationTcrBinding(self, request):
        """绑定解绑tcr仓库

        :param request: Request instance for OperateApplicationTcrBinding.
        :type request: :class:`tencentcloud.tsf.v20180326.models.OperateApplicationTcrBindingRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.OperateApplicationTcrBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateApplicationTcrBinding", params, headers=headers)
            response = json.loads(body)
            model = models.OperateApplicationTcrBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReassociateBusinessLogConfig(self, request):
        """重关联业务日志配置

        :param request: Request instance for ReassociateBusinessLogConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ReassociateBusinessLogConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ReassociateBusinessLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReassociateBusinessLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ReassociateBusinessLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RedoTask(self, request):
        """重新执行任务

        :param request: Request instance for RedoTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RedoTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RedoTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RedoTask", params, headers=headers)
            response = json.loads(body)
            model = models.RedoTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RedoTaskBatch(self, request):
        """重新执行任务批次

        :param request: Request instance for RedoTaskBatch.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RedoTaskBatchRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RedoTaskBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RedoTaskBatch", params, headers=headers)
            response = json.loads(body)
            model = models.RedoTaskBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RedoTaskExecute(self, request):
        """重新执行在某个节点上执行任务。

        :param request: Request instance for RedoTaskExecute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RedoTaskExecuteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RedoTaskExecuteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RedoTaskExecute", params, headers=headers)
            response = json.loads(body)
            model = models.RedoTaskExecuteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RedoTaskFlowBatch(self, request):
        """重新执行工作流批次

        :param request: Request instance for RedoTaskFlowBatch.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RedoTaskFlowBatchRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RedoTaskFlowBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RedoTaskFlowBatch", params, headers=headers)
            response = json.loads(body)
            model = models.RedoTaskFlowBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseApiGroup(self, request):
        """发布Api分组

        :param request: Request instance for ReleaseApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ReleaseApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ReleaseApiGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseApiGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseApiGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseConfig(self, request):
        """发布配置

        :param request: Request instance for ReleaseConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ReleaseConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ReleaseConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseConfigWithDetailResp(self, request):
        """发布配置,并且返回配置 ID

        :param request: Request instance for ReleaseConfigWithDetailResp.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ReleaseConfigWithDetailRespRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ReleaseConfigWithDetailRespResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseConfigWithDetailResp", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseConfigWithDetailRespResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseFileConfig(self, request):
        """发布文件配置

        :param request: Request instance for ReleaseFileConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ReleaseFileConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ReleaseFileConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseFileConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseFileConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleasePublicConfig(self, request):
        """发布公共配置

        :param request: Request instance for ReleasePublicConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ReleasePublicConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ReleasePublicConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleasePublicConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ReleasePublicConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveInstances(self, request):
        """从 TSF 集群中批量移除云主机节点

        :param request: Request instance for RemoveInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RemoveInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RemoveInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevocationConfig(self, request):
        """撤回已发布的配置

        :param request: Request instance for RevocationConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RevocationConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RevocationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevocationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.RevocationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevocationPublicConfig(self, request):
        """撤回已发布的公共配置

        :param request: Request instance for RevocationPublicConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RevocationPublicConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RevocationPublicConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevocationPublicConfig", params, headers=headers)
            response = json.loads(body)
            model = models.RevocationPublicConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevokeFileConfig(self, request):
        """撤回已发布的文件配置

        :param request: Request instance for RevokeFileConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RevokeFileConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RevokeFileConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokeFileConfig", params, headers=headers)
            response = json.loads(body)
            model = models.RevokeFileConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackConfig(self, request):
        """回滚配置

        :param request: Request instance for RollbackConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RollbackConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RollbackConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackConfig", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchBusinessLog(self, request):
        """业务日志搜索

        :param request: Request instance for SearchBusinessLog.
        :type request: :class:`tencentcloud.tsf.v20180326.models.SearchBusinessLogRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.SearchBusinessLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchBusinessLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchBusinessLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchStdoutLog(self, request):
        """标准输出日志搜索

        :param request: Request instance for SearchStdoutLog.
        :type request: :class:`tencentcloud.tsf.v20180326.models.SearchStdoutLogRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.SearchStdoutLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchStdoutLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchStdoutLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ShrinkGroup(self, request):
        """下线部署组所有机器实例

        :param request: Request instance for ShrinkGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ShrinkGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ShrinkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ShrinkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ShrinkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ShrinkInstances(self, request):
        """虚拟机部署组下线实例

        :param request: Request instance for ShrinkInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ShrinkInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ShrinkInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ShrinkInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ShrinkInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartContainerGroup(self, request):
        """启动容器部署组

        :param request: Request instance for StartContainerGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StartContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StartContainerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartContainerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.StartContainerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartGroup(self, request):
        """启动分组

        :param request: Request instance for StartGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StartGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StartGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartGroup", params, headers=headers)
            response = json.loads(body)
            model = models.StartGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopContainerGroup(self, request):
        """停止容器部署组

        :param request: Request instance for StopContainerGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StopContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StopContainerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopContainerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.StopContainerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopGroup(self, request):
        """停止虚拟机部署组

        :param request: Request instance for StopGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StopGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StopGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopGroup", params, headers=headers)
            response = json.loads(body)
            model = models.StopGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopTaskBatch(self, request):
        """停止执行中的任务批次， 非运行中的任务不可调用。

        :param request: Request instance for StopTaskBatch.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StopTaskBatchRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StopTaskBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopTaskBatch", params, headers=headers)
            response = json.loads(body)
            model = models.StopTaskBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopTaskExecute(self, request):
        """停止正在某个节点上执行的任务

        :param request: Request instance for StopTaskExecute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StopTaskExecuteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StopTaskExecuteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopTaskExecute", params, headers=headers)
            response = json.loads(body)
            model = models.StopTaskExecuteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateTaskFlowBatch(self, request):
        """停止一个工作流批次

        :param request: Request instance for TerminateTaskFlowBatch.
        :type request: :class:`tencentcloud.tsf.v20180326.models.TerminateTaskFlowBatchRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.TerminateTaskFlowBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateTaskFlowBatch", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateTaskFlowBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindApiGroup(self, request):
        """API分组批量与网关解绑

        :param request: Request instance for UnbindApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UnbindApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UnbindApiGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindApiGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindApiGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateApiGroup(self, request):
        """更新Api分组

        :param request: Request instance for UpdateApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateApiGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApiGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApiGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateApiRateLimitRule(self, request):
        """更新API限流规则

        :param request: Request instance for UpdateApiRateLimitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateApiRateLimitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateApiRateLimitRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApiRateLimitRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApiRateLimitRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateApiRateLimitRules(self, request):
        """批量更新API限流规则

        :param request: Request instance for UpdateApiRateLimitRules.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateApiRateLimitRulesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateApiRateLimitRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApiRateLimitRules", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApiRateLimitRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateApiTimeouts(self, request):
        """批量更新API超时

        :param request: Request instance for UpdateApiTimeouts.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateApiTimeoutsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateApiTimeoutsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApiTimeouts", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApiTimeoutsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConfigTemplate(self, request):
        """更新参数模板

        :param request: Request instance for UpdateConfigTemplate.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateConfigTemplateRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateConfigTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConfigTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConfigTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateGatewayApi(self, request):
        """更新API

        :param request: Request instance for UpdateGatewayApi.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateGatewayApiRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateGatewayApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGatewayApi", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGatewayApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateHealthCheckSettings(self, request):
        """更新健康检查配置

        :param request: Request instance for UpdateHealthCheckSettings.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateHealthCheckSettingsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateHealthCheckSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateHealthCheckSettings", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateHealthCheckSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRepository(self, request):
        """更新仓库信息

        :param request: Request instance for UpdateRepository.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateRepositoryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateRepositoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRepository", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRepositoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUnitRule(self, request):
        """更新单元化规则

        :param request: Request instance for UpdateUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateUnitRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUnitRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUnitRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))