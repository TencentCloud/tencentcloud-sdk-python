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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.tsf.v20180326 import models
from typing import Dict


class TsfClient(AbstractClient):
    _apiVersion = '2018-03-26'
    _endpoint = 'tsf.tencentcloudapi.com'
    _service = 'tsf'

    async def AddClusterInstances(
            self,
            request: models.AddClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.AddClusterInstancesResponse:
        """
        添加云主机节点至TSF集群
        """
        
        kwargs = {}
        kwargs["action"] = "AddClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddInstances(
            self,
            request: models.AddInstancesRequest,
            opts: Dict = None,
    ) -> models.AddInstancesResponse:
        """
        添加云主机节点至TSF集群
        """
        
        kwargs = {}
        kwargs["action"] = "AddInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateBusinessLogConfig(
            self,
            request: models.AssociateBusinessLogConfigRequest,
            opts: Dict = None,
    ) -> models.AssociateBusinessLogConfigResponse:
        """
        关联日志配置项到应用
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateBusinessLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateBusinessLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateConfigWithGroup(
            self,
            request: models.AssociateConfigWithGroupRequest,
            opts: Dict = None,
    ) -> models.AssociateConfigWithGroupResponse:
        """
        关联投递配置到部署组
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateConfigWithGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateConfigWithGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindApiGroup(
            self,
            request: models.BindApiGroupRequest,
            opts: Dict = None,
    ) -> models.BindApiGroupResponse:
        """
        网关与API分组批量绑定
        """
        
        kwargs = {}
        kwargs["action"] = "BindApiGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindApiGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindPlugin(
            self,
            request: models.BindPluginRequest,
            opts: Dict = None,
    ) -> models.BindPluginResponse:
        """
        插件与网关分组/API批量绑定
        """
        
        kwargs = {}
        kwargs["action"] = "BindPlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindPluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeApiUsableStatus(
            self,
            request: models.ChangeApiUsableStatusRequest,
            opts: Dict = None,
    ) -> models.ChangeApiUsableStatusResponse:
        """
        启用或禁用API
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeApiUsableStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeApiUsableStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ContinueRunFailedTaskBatch(
            self,
            request: models.ContinueRunFailedTaskBatchRequest,
            opts: Dict = None,
    ) -> models.ContinueRunFailedTaskBatchResponse:
        """
        对执行失败的任务批次执行续跑
        """
        
        kwargs = {}
        kwargs["action"] = "ContinueRunFailedTaskBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ContinueRunFailedTaskBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAllGatewayApiAsync(
            self,
            request: models.CreateAllGatewayApiAsyncRequest,
            opts: Dict = None,
    ) -> models.CreateAllGatewayApiAsyncResponse:
        """
        一键导入API分组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAllGatewayApiAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAllGatewayApiAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApiGroup(
            self,
            request: models.CreateApiGroupRequest,
            opts: Dict = None,
    ) -> models.CreateApiGroupResponse:
        """
        创建API分组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApiRateLimitRule(
            self,
            request: models.CreateApiRateLimitRuleRequest,
            opts: Dict = None,
    ) -> models.CreateApiRateLimitRuleResponse:
        """
        创建API限流规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiRateLimitRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiRateLimitRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApiRateLimitRuleWithDetailResp(
            self,
            request: models.CreateApiRateLimitRuleWithDetailRespRequest,
            opts: Dict = None,
    ) -> models.CreateApiRateLimitRuleWithDetailRespResponse:
        """
        创建API限流规则,并返回规则信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiRateLimitRuleWithDetailResp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiRateLimitRuleWithDetailRespResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplication(
            self,
            request: models.CreateApplicationRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationResponse:
        """
        创建应用
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        创建集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfig(
            self,
            request: models.CreateConfigRequest,
            opts: Dict = None,
    ) -> models.CreateConfigResponse:
        """
        创建配置项
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfigTemplate(
            self,
            request: models.CreateConfigTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateConfigTemplateResponse:
        """
        创建参数模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfigTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfigTemplateWithDetailResp(
            self,
            request: models.CreateConfigTemplateWithDetailRespRequest,
            opts: Dict = None,
    ) -> models.CreateConfigTemplateWithDetailRespResponse:
        """
        创建参数模板，并返回模板详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfigTemplateWithDetailResp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigTemplateWithDetailRespResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfigWithDetailResp(
            self,
            request: models.CreateConfigWithDetailRespRequest,
            opts: Dict = None,
    ) -> models.CreateConfigWithDetailRespResponse:
        """
        创建配置项，返回详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfigWithDetailResp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigWithDetailRespResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateContainGroup(
            self,
            request: models.CreateContainGroupRequest,
            opts: Dict = None,
    ) -> models.CreateContainGroupResponse:
        """
        （已废弃，请使用 CreateGroup 和 DeployContainerGroup 创建和部署容器部署组）创建容器部署组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateContainGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateContainGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileConfig(
            self,
            request: models.CreateFileConfigRequest,
            opts: Dict = None,
    ) -> models.CreateFileConfigResponse:
        """
        创建文件配置项
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileConfigWithDetailResp(
            self,
            request: models.CreateFileConfigWithDetailRespRequest,
            opts: Dict = None,
    ) -> models.CreateFileConfigWithDetailRespResponse:
        """
        创建文件配置项，返回详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileConfigWithDetailResp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileConfigWithDetailRespResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGatewayApi(
            self,
            request: models.CreateGatewayApiRequest,
            opts: Dict = None,
    ) -> models.CreateGatewayApiResponse:
        """
        批量导入API至api分组(也支持新建API到分组)
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGatewayApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGatewayApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroup(
            self,
            request: models.CreateGroupRequest,
            opts: Dict = None,
    ) -> models.CreateGroupResponse:
        """
        创建虚拟机部署组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLane(
            self,
            request: models.CreateLaneRequest,
            opts: Dict = None,
    ) -> models.CreateLaneResponse:
        """
        创建泳道配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLane"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLaneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLaneRule(
            self,
            request: models.CreateLaneRuleRequest,
            opts: Dict = None,
    ) -> models.CreateLaneRuleResponse:
        """
        创建灰度发布规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLaneRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLaneRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMicroservice(
            self,
            request: models.CreateMicroserviceRequest,
            opts: Dict = None,
    ) -> models.CreateMicroserviceResponse:
        """
        新增微服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMicroservice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMicroserviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMicroserviceWithDetailResp(
            self,
            request: models.CreateMicroserviceWithDetailRespRequest,
            opts: Dict = None,
    ) -> models.CreateMicroserviceWithDetailRespResponse:
        """
        新增微服务返回ID
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMicroserviceWithDetailResp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMicroserviceWithDetailRespResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNamespace(
            self,
            request: models.CreateNamespaceRequest,
            opts: Dict = None,
    ) -> models.CreateNamespaceResponse:
        """
        创建命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePathRewrites(
            self,
            request: models.CreatePathRewritesRequest,
            opts: Dict = None,
    ) -> models.CreatePathRewritesResponse:
        """
        创建路径重写
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePathRewrites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePathRewritesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePathRewritesWithDetailResp(
            self,
            request: models.CreatePathRewritesWithDetailRespRequest,
            opts: Dict = None,
    ) -> models.CreatePathRewritesWithDetailRespResponse:
        """
        创建路径重写，并返回路径重写规则信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePathRewritesWithDetailResp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePathRewritesWithDetailRespResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProgram(
            self,
            request: models.CreateProgramRequest,
            opts: Dict = None,
    ) -> models.CreateProgramResponse:
        """
        创建数据集
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProgram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProgramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePublicConfig(
            self,
            request: models.CreatePublicConfigRequest,
            opts: Dict = None,
    ) -> models.CreatePublicConfigResponse:
        """
        创建公共配置项
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePublicConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePublicConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePublicConfigWithDetailResp(
            self,
            request: models.CreatePublicConfigWithDetailRespRequest,
            opts: Dict = None,
    ) -> models.CreatePublicConfigWithDetailRespResponse:
        """
        创建公共配置项，并返回配置项详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePublicConfigWithDetailResp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePublicConfigWithDetailRespResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRepository(
            self,
            request: models.CreateRepositoryRequest,
            opts: Dict = None,
    ) -> models.CreateRepositoryResponse:
        """
        创建仓库
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTask(
            self,
            request: models.CreateTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTaskResponse:
        """
        创建任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskFlow(
            self,
            request: models.CreateTaskFlowRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFlowResponse:
        """
        创建工作流
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUnitNamespaces(
            self,
            request: models.CreateUnitNamespacesRequest,
            opts: Dict = None,
    ) -> models.CreateUnitNamespacesResponse:
        """
        批量创建单元化命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUnitNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUnitNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUnitRule(
            self,
            request: models.CreateUnitRuleRequest,
            opts: Dict = None,
    ) -> models.CreateUnitRuleResponse:
        """
        创建单元化规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUnitRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUnitRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUnitRuleWithDetailResp(
            self,
            request: models.CreateUnitRuleWithDetailRespRequest,
            opts: Dict = None,
    ) -> models.CreateUnitRuleWithDetailRespResponse:
        """
        创建单元化规则, 并返回详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUnitRuleWithDetailResp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUnitRuleWithDetailRespResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApiGroup(
            self,
            request: models.DeleteApiGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteApiGroupResponse:
        """
        删除Api分组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApiGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApiGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApiRateLimitRule(
            self,
            request: models.DeleteApiRateLimitRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteApiRateLimitRuleResponse:
        """
        删除API限流规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApiRateLimitRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApiRateLimitRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplication(
            self,
            request: models.DeleteApplicationRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationResponse:
        """
        删除应用
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        删除集群
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfig(
            self,
            request: models.DeleteConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigResponse:
        """
        删除配置项
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfigTemplate(
            self,
            request: models.DeleteConfigTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigTemplateResponse:
        """
        删除模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfigTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteContainerGroup(
            self,
            request: models.DeleteContainerGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteContainerGroupResponse:
        """
        删除容器部署组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteContainerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteContainerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFileConfig(
            self,
            request: models.DeleteFileConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteFileConfigResponse:
        """
        删除文件配置项
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFileConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFileConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGatewayApi(
            self,
            request: models.DeleteGatewayApiRequest,
            opts: Dict = None,
    ) -> models.DeleteGatewayApiResponse:
        """
        批量删除API
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGatewayApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGatewayApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        删除容器部署组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageTags(
            self,
            request: models.DeleteImageTagsRequest,
            opts: Dict = None,
    ) -> models.DeleteImageTagsResponse:
        """
        批量删除镜像版本
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLane(
            self,
            request: models.DeleteLaneRequest,
            opts: Dict = None,
    ) -> models.DeleteLaneResponse:
        """
        删除泳道配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLane"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLaneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLaneRule(
            self,
            request: models.DeleteLaneRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteLaneRuleResponse:
        """
        删除灰度发布规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLaneRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLaneRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMicroservice(
            self,
            request: models.DeleteMicroserviceRequest,
            opts: Dict = None,
    ) -> models.DeleteMicroserviceResponse:
        """
        删除微服务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMicroservice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMicroserviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNamespace(
            self,
            request: models.DeleteNamespaceRequest,
            opts: Dict = None,
    ) -> models.DeleteNamespaceResponse:
        """
        删除命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePathRewrites(
            self,
            request: models.DeletePathRewritesRequest,
            opts: Dict = None,
    ) -> models.DeletePathRewritesResponse:
        """
        删除路径重写
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePathRewrites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePathRewritesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePkgs(
            self,
            request: models.DeletePkgsRequest,
            opts: Dict = None,
    ) -> models.DeletePkgsResponse:
        """
        从软件仓库批量删除程序包。
        一次最多支持删除1000个包，数量超过1000，返回UpperDeleteLimit错误。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePkgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePkgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePublicConfig(
            self,
            request: models.DeletePublicConfigRequest,
            opts: Dict = None,
    ) -> models.DeletePublicConfigResponse:
        """
        删除公共配置项
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePublicConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePublicConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRepository(
            self,
            request: models.DeleteRepositoryRequest,
            opts: Dict = None,
    ) -> models.DeleteRepositoryResponse:
        """
        删除仓库
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServerlessGroup(
            self,
            request: models.DeleteServerlessGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteServerlessGroupResponse:
        """
        serverless 能力已下线。下线对应接口。

        删除Serverless部署组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServerlessGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServerlessGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTask(
            self,
            request: models.DeleteTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskResponse:
        """
        删除任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUnitNamespaces(
            self,
            request: models.DeleteUnitNamespacesRequest,
            opts: Dict = None,
    ) -> models.DeleteUnitNamespacesResponse:
        """
        删除单元化命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUnitNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUnitNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUnitRule(
            self,
            request: models.DeleteUnitRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteUnitRuleResponse:
        """
        删除单元化规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUnitRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUnitRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployContainerApplication(
            self,
            request: models.DeployContainerApplicationRequest,
            opts: Dict = None,
    ) -> models.DeployContainerApplicationResponse:
        """
        部署容器应用-更新
        """
        
        kwargs = {}
        kwargs["action"] = "DeployContainerApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployContainerApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployContainerGroup(
            self,
            request: models.DeployContainerGroupRequest,
            opts: Dict = None,
    ) -> models.DeployContainerGroupResponse:
        """
        部署容器应用-更新
        """
        
        kwargs = {}
        kwargs["action"] = "DeployContainerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployContainerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployGroup(
            self,
            request: models.DeployGroupRequest,
            opts: Dict = None,
    ) -> models.DeployGroupResponse:
        """
        部署虚拟机部署组应用
        """
        
        kwargs = {}
        kwargs["action"] = "DeployGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiDetail(
            self,
            request: models.DescribeApiDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeApiDetailResponse:
        """
        查询API详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiGroup(
            self,
            request: models.DescribeApiGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeApiGroupResponse:
        """
        查询API分组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiGroups(
            self,
            request: models.DescribeApiGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeApiGroupsResponse:
        """
        查询API 分组信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiRateLimitRules(
            self,
            request: models.DescribeApiRateLimitRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeApiRateLimitRulesResponse:
        """
        查询API限流规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiRateLimitRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiRateLimitRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiUseDetail(
            self,
            request: models.DescribeApiUseDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeApiUseDetailResponse:
        """
        查询网关API监控明细数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiUseDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiUseDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiVersions(
            self,
            request: models.DescribeApiVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeApiVersionsResponse:
        """
        查询API版本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplication(
            self,
            request: models.DescribeApplicationRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationResponse:
        """
        获取应用详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationAttribute(
            self,
            request: models.DescribeApplicationAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationAttributeResponse:
        """
        获取应用列表其它字段，如实例数量信息等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplications(
            self,
            request: models.DescribeApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationsResponse:
        """
        获取应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBasicResourceUsage(
            self,
            request: models.DescribeBasicResourceUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeBasicResourceUsageResponse:
        """
        TSF基本资源信息概览接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBasicResourceUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBasicResourceUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBusinessLogConfig(
            self,
            request: models.DescribeBusinessLogConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeBusinessLogConfigResponse:
        """
        查询业务日志配置项信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBusinessLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBusinessLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBusinessLogConfigs(
            self,
            request: models.DescribeBusinessLogConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeBusinessLogConfigsResponse:
        """
        查询日志配置项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBusinessLogConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBusinessLogConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInstances(
            self,
            request: models.DescribeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInstancesResponse:
        """
        查询集群实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        获取集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfig(
            self,
            request: models.DescribeConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigResponse:
        """
        查询配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigReleaseLogs(
            self,
            request: models.DescribeConfigReleaseLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigReleaseLogsResponse:
        """
        查询配置发布历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigReleaseLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigReleaseLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigReleases(
            self,
            request: models.DescribeConfigReleasesRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigReleasesResponse:
        """
        查询配置发布信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigReleases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigReleasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigSummary(
            self,
            request: models.DescribeConfigSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigSummaryResponse:
        """
        查询配置汇总列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigTemplate(
            self,
            request: models.DescribeConfigTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigTemplateResponse:
        """
        导入配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigs(
            self,
            request: models.DescribeConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigsResponse:
        """
        查询配置项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContainerEvents(
            self,
            request: models.DescribeContainerEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeContainerEventsResponse:
        """
        获取容器事件列表
        参数限制

        - 当类型是 instance 时，GroupId是必填项
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContainerEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContainerEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContainerGroupAttribute(
            self,
            request: models.DescribeContainerGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeContainerGroupAttributeResponse:
        """
        获取部署组其他字段-用于前端并发调用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContainerGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContainerGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContainerGroupDeployInfo(
            self,
            request: models.DescribeContainerGroupDeployInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeContainerGroupDeployInfoResponse:
        """
        获取部署组详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContainerGroupDeployInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContainerGroupDeployInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContainerGroupDetail(
            self,
            request: models.DescribeContainerGroupDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeContainerGroupDetailResponse:
        """
        容器部署组详情（已废弃，请使用  [DescribeContainerGroupDeployInfo](https://cloud.tencent.com/document/product/649/67221)）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContainerGroupDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContainerGroupDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContainerGroups(
            self,
            request: models.DescribeContainerGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeContainerGroupsResponse:
        """
        容器部署组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContainerGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContainerGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCreateGatewayApiStatus(
            self,
            request: models.DescribeCreateGatewayApiStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeCreateGatewayApiStatusResponse:
        """
        查询一键导入API分组任务的状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCreateGatewayApiStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCreateGatewayApiStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeliveryConfig(
            self,
            request: models.DescribeDeliveryConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDeliveryConfigResponse:
        """
        获取单个投递项配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeliveryConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeliveryConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeliveryConfigByGroupId(
            self,
            request: models.DescribeDeliveryConfigByGroupIdRequest,
            opts: Dict = None,
    ) -> models.DescribeDeliveryConfigByGroupIdResponse:
        """
        用部署组id获取绑定信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeliveryConfigByGroupId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeliveryConfigByGroupIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeliveryConfigs(
            self,
            request: models.DescribeDeliveryConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeDeliveryConfigsResponse:
        """
        获取多个投递项配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeliveryConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeliveryConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDownloadInfo(
            self,
            request: models.DescribeDownloadInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDownloadInfoResponse:
        """
        TSF上传的程序包存放在腾讯云对象存储（COS）中，通过该API可以获取从COS下载程序包需要的信息，包括包所在的桶、存储路径、鉴权信息等，之后使用COS API（或SDK）进行下载。
        请查阅[COS相关文档](https://cloud.tencent.com/document/product/436)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDownloadInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDownloadInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnabledUnitRule(
            self,
            request: models.DescribeEnabledUnitRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeEnabledUnitRuleResponse:
        """
        查询生效的单元化规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnabledUnitRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnabledUnitRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileConfigReleases(
            self,
            request: models.DescribeFileConfigReleasesRequest,
            opts: Dict = None,
    ) -> models.DescribeFileConfigReleasesResponse:
        """
        查询文件配置项发布信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileConfigReleases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileConfigReleasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileConfigs(
            self,
            request: models.DescribeFileConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileConfigsResponse:
        """
        查询文件配置项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowLastBatchState(
            self,
            request: models.DescribeFlowLastBatchStateRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowLastBatchStateResponse:
        """
        查询工作流最新一个批次的状态信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowLastBatchState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowLastBatchStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayAllGroupApis(
            self,
            request: models.DescribeGatewayAllGroupApisRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayAllGroupApisResponse:
        """
        查询网关所有分组下Api列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayAllGroupApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayAllGroupApisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayApis(
            self,
            request: models.DescribeGatewayApisRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayApisResponse:
        """
        查询API分组下的Api列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayApisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayMonitorOverview(
            self,
            request: models.DescribeGatewayMonitorOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayMonitorOverviewResponse:
        """
        查询网关监控概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayMonitorOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayMonitorOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroup(
            self,
            request: models.DescribeGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupResponse:
        """
        查询虚拟机部署组详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupAttribute(
            self,
            request: models.DescribeGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupAttributeResponse:
        """
        获取部署组其他属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupBindedGateways(
            self,
            request: models.DescribeGroupBindedGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupBindedGatewaysResponse:
        """
        查询某个API分组已绑定的网关部署组信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupBindedGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupBindedGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupBusinessLogConfigs(
            self,
            request: models.DescribeGroupBusinessLogConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupBusinessLogConfigsResponse:
        """
        查询分组管理日志配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupBusinessLogConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupBusinessLogConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupGateways(
            self,
            request: models.DescribeGroupGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupGatewaysResponse:
        """
        查询某个网关绑定的API 分组信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupInstances(
            self,
            request: models.DescribeGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupInstancesResponse:
        """
        查询虚拟机部署组云主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupRelease(
            self,
            request: models.DescribeGroupReleaseRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupReleaseResponse:
        """
        查询部署组相关的发布信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupUseDetail(
            self,
            request: models.DescribeGroupUseDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupUseDetailResponse:
        """
        查询网关分组监控明细数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupUseDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupUseDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroups(
            self,
            request: models.DescribeGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupsResponse:
        """
        获取虚拟机部署组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupsWithPlugin(
            self,
            request: models.DescribeGroupsWithPluginRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupsWithPluginResponse:
        """
        查询某个插件下绑定或未绑定的API分组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupsWithPlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupsWithPluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRepository(
            self,
            request: models.DescribeImageRepositoryRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRepositoryResponse:
        """
        查询镜像仓库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageTags(
            self,
            request: models.DescribeImageTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeImageTagsResponse:
        """
        镜像版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        无
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvocationMetricDataCurve(
            self,
            request: models.DescribeInvocationMetricDataCurveRequest,
            opts: Dict = None,
    ) -> models.DescribeInvocationMetricDataCurveResponse:
        """
        查询调用指标数据变化曲线
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvocationMetricDataCurve"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvocationMetricDataCurveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvocationMetricDataDimension(
            self,
            request: models.DescribeInvocationMetricDataDimensionRequest,
            opts: Dict = None,
    ) -> models.DescribeInvocationMetricDataDimensionResponse:
        """
        查询维度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvocationMetricDataDimension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvocationMetricDataDimensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvocationMetricDataPoint(
            self,
            request: models.DescribeInvocationMetricDataPointRequest,
            opts: Dict = None,
    ) -> models.DescribeInvocationMetricDataPointResponse:
        """
        查询单值指标维度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvocationMetricDataPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvocationMetricDataPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInvocationMetricScatterPlot(
            self,
            request: models.DescribeInvocationMetricScatterPlotRequest,
            opts: Dict = None,
    ) -> models.DescribeInvocationMetricScatterPlotResponse:
        """
        查询调用指标数据散点图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInvocationMetricScatterPlot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInvocationMetricScatterPlotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJvmMonitor(
            self,
            request: models.DescribeJvmMonitorRequest,
            opts: Dict = None,
    ) -> models.DescribeJvmMonitorResponse:
        """
        查询java实例jvm监控数据,返回数据可选
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJvmMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJvmMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLaneRules(
            self,
            request: models.DescribeLaneRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLaneRulesResponse:
        """
        查询灰度发布规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLaneRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLaneRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLanes(
            self,
            request: models.DescribeLanesRequest,
            opts: Dict = None,
    ) -> models.DescribeLanesResponse:
        """
        查询泳道配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLanes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLanesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenses(
            self,
            request: models.DescribeLicensesRequest,
            opts: Dict = None,
    ) -> models.DescribeLicensesResponse:
        """
        查询许可列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicensesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogCapacity(
            self,
            request: models.DescribeLogCapacityRequest,
            opts: Dict = None,
    ) -> models.DescribeLogCapacityResponse:
        """
        获取用户日志使用量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogCapacity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogCapacityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMicroservice(
            self,
            request: models.DescribeMicroserviceRequest,
            opts: Dict = None,
    ) -> models.DescribeMicroserviceResponse:
        """
        查询微服务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMicroservice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMicroserviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMicroservices(
            self,
            request: models.DescribeMicroservicesRequest,
            opts: Dict = None,
    ) -> models.DescribeMicroservicesResponse:
        """
        获取微服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMicroservices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMicroservicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMicroservicesByGroupIds(
            self,
            request: models.DescribeMicroservicesByGroupIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeMicroservicesByGroupIdsResponse:
        """
        通过部署组ID获取微服务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMicroservicesByGroupIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMicroservicesByGroupIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMsApiList(
            self,
            request: models.DescribeMsApiListRequest,
            opts: Dict = None,
    ) -> models.DescribeMsApiListResponse:
        """
        查询服务API列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMsApiList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMsApiListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewInvocation(
            self,
            request: models.DescribeOverviewInvocationRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewInvocationResponse:
        """
        服务调用监控统计概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewInvocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewInvocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePathRewrite(
            self,
            request: models.DescribePathRewriteRequest,
            opts: Dict = None,
    ) -> models.DescribePathRewriteResponse:
        """
        查询路径重写
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePathRewrite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePathRewriteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePathRewrites(
            self,
            request: models.DescribePathRewritesRequest,
            opts: Dict = None,
    ) -> models.DescribePathRewritesResponse:
        """
        查询路径重写列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePathRewrites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePathRewritesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePkgs(
            self,
            request: models.DescribePkgsRequest,
            opts: Dict = None,
    ) -> models.DescribePkgsResponse:
        """
        无
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePkgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePkgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePluginInstances(
            self,
            request: models.DescribePluginInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribePluginInstancesResponse:
        """
        分页查询网关分组/API绑定（或未绑定）的插件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePluginInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePodInstances(
            self,
            request: models.DescribePodInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribePodInstancesResponse:
        """
        获取部署组实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePodInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePodInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrograms(
            self,
            request: models.DescribeProgramsRequest,
            opts: Dict = None,
    ) -> models.DescribeProgramsResponse:
        """
        查询数据集列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrograms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProgramsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicConfig(
            self,
            request: models.DescribePublicConfigRequest,
            opts: Dict = None,
    ) -> models.DescribePublicConfigResponse:
        """
        查询公共配置（单条）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicConfigReleaseLogs(
            self,
            request: models.DescribePublicConfigReleaseLogsRequest,
            opts: Dict = None,
    ) -> models.DescribePublicConfigReleaseLogsResponse:
        """
        查询公共配置发布历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicConfigReleaseLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicConfigReleaseLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicConfigReleases(
            self,
            request: models.DescribePublicConfigReleasesRequest,
            opts: Dict = None,
    ) -> models.DescribePublicConfigReleasesResponse:
        """
        查询公共配置发布信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicConfigReleases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicConfigReleasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicConfigSummary(
            self,
            request: models.DescribePublicConfigSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribePublicConfigSummaryResponse:
        """
        查询公共配置汇总列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicConfigSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicConfigSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicConfigs(
            self,
            request: models.DescribePublicConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribePublicConfigsResponse:
        """
        查询公共配置项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleasedConfig(
            self,
            request: models.DescribeReleasedConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeReleasedConfigResponse:
        """
        查询部署组发布的配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleasedConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleasedConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRepositories(
            self,
            request: models.DescribeRepositoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeRepositoriesResponse:
        """
        查询仓库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRepositories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRepositoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRepository(
            self,
            request: models.DescribeRepositoryRequest,
            opts: Dict = None,
    ) -> models.DescribeRepositoryResponse:
        """
        查询仓库信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceConfig(
            self,
            request: models.DescribeResourceConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceConfigResponse:
        """
        无
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTaskStatus(
            self,
            request: models.DescribeResourceTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTaskStatusResponse:
        """
        资源任务的执行状态描述接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSimpleApplications(
            self,
            request: models.DescribeSimpleApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeSimpleApplicationsResponse:
        """
        查询简单应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSimpleApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSimpleApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSimpleClusters(
            self,
            request: models.DescribeSimpleClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeSimpleClustersResponse:
        """
        查询简单集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSimpleClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSimpleClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSimpleGroups(
            self,
            request: models.DescribeSimpleGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeSimpleGroupsResponse:
        """
        查询简单部署组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSimpleGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSimpleGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSimpleNamespaces(
            self,
            request: models.DescribeSimpleNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeSimpleNamespacesResponse:
        """
        查询简单命名空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSimpleNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSimpleNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStatistics(
            self,
            request: models.DescribeStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeStatisticsResponse:
        """
        服务统计页面：接口和服务维度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskDetail(
            self,
            request: models.DescribeTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskDetailResponse:
        """
        查询任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLastStatus(
            self,
            request: models.DescribeTaskLastStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLastStatusResponse:
        """
        查询任务最近一次执行状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLastStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLastStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskRecords(
            self,
            request: models.DescribeTaskRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskRecordsResponse:
        """
        翻页查询任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnitApiUseDetail(
            self,
            request: models.DescribeUnitApiUseDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeUnitApiUseDetailResponse:
        """
        查询网关API监控明细数据（仅单元化网关），非单元化网关使用DescribeApiUseDetail
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnitApiUseDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnitApiUseDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnitNamespaces(
            self,
            request: models.DescribeUnitNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeUnitNamespacesResponse:
        """
        查询单元化命名空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnitNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnitNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnitRule(
            self,
            request: models.DescribeUnitRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeUnitRuleResponse:
        """
        查询单元化规则详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnitRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnitRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnitRules(
            self,
            request: models.DescribeUnitRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeUnitRulesResponse:
        """
        查询单元化规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnitRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnitRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnitRulesV2(
            self,
            request: models.DescribeUnitRulesV2Request,
            opts: Dict = None,
    ) -> models.DescribeUnitRulesV2Response:
        """
        查询单元化规则列表V2
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnitRulesV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnitRulesV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUploadInfo(
            self,
            request: models.DescribeUploadInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUploadInfoResponse:
        """
        TSF会将软件包上传到腾讯云对象存储（COS）。调用此接口获取上传信息，如目标地域，桶，包Id，存储路径，鉴权信息等，之后请使用COS API（或SDK）进行上传。
        请查阅[COS相关文档](https://cloud.tencent.com/document/product/436)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUploadInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUploadInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsableUnitNamespaces(
            self,
            request: models.DescribeUsableUnitNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeUsableUnitNamespacesResponse:
        """
        查询可用于被导入的命名空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsableUnitNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsableUnitNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableLaneRule(
            self,
            request: models.DisableLaneRuleRequest,
            opts: Dict = None,
    ) -> models.DisableLaneRuleResponse:
        """
        禁用灰度发布规则
        """
        
        kwargs = {}
        kwargs["action"] = "DisableLaneRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableLaneRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableTask(
            self,
            request: models.DisableTaskRequest,
            opts: Dict = None,
    ) -> models.DisableTaskResponse:
        """
        停用任务
        """
        
        kwargs = {}
        kwargs["action"] = "DisableTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableTaskFlow(
            self,
            request: models.DisableTaskFlowRequest,
            opts: Dict = None,
    ) -> models.DisableTaskFlowResponse:
        """
        停用工作流
        """
        
        kwargs = {}
        kwargs["action"] = "DisableTaskFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableTaskFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableUnitRoute(
            self,
            request: models.DisableUnitRouteRequest,
            opts: Dict = None,
    ) -> models.DisableUnitRouteResponse:
        """
        禁用单元化路由
        """
        
        kwargs = {}
        kwargs["action"] = "DisableUnitRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableUnitRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableUnitRule(
            self,
            request: models.DisableUnitRuleRequest,
            opts: Dict = None,
    ) -> models.DisableUnitRuleResponse:
        """
        禁用单元化规则
        """
        
        kwargs = {}
        kwargs["action"] = "DisableUnitRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableUnitRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateBusinessLogConfig(
            self,
            request: models.DisassociateBusinessLogConfigRequest,
            opts: Dict = None,
    ) -> models.DisassociateBusinessLogConfigResponse:
        """
        取消关联业务日志配置项和应用
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateBusinessLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateBusinessLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateKafkaConfig(
            self,
            request: models.DisassociateKafkaConfigRequest,
            opts: Dict = None,
    ) -> models.DisassociateKafkaConfigResponse:
        """
        取消关联投递信息和部署组
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateKafkaConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateKafkaConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DraftApiGroup(
            self,
            request: models.DraftApiGroupRequest,
            opts: Dict = None,
    ) -> models.DraftApiGroupResponse:
        """
        下线Api分组
        """
        
        kwargs = {}
        kwargs["action"] = "DraftApiGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DraftApiGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableLaneRule(
            self,
            request: models.EnableLaneRuleRequest,
            opts: Dict = None,
    ) -> models.EnableLaneRuleResponse:
        """
        启用灰度发布规则
        """
        
        kwargs = {}
        kwargs["action"] = "EnableLaneRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableLaneRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableTask(
            self,
            request: models.EnableTaskRequest,
            opts: Dict = None,
    ) -> models.EnableTaskResponse:
        """
        启用任务
        """
        
        kwargs = {}
        kwargs["action"] = "EnableTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableTaskFlow(
            self,
            request: models.EnableTaskFlowRequest,
            opts: Dict = None,
    ) -> models.EnableTaskFlowResponse:
        """
        启用工作流
        """
        
        kwargs = {}
        kwargs["action"] = "EnableTaskFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableTaskFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableUnitRoute(
            self,
            request: models.EnableUnitRouteRequest,
            opts: Dict = None,
    ) -> models.EnableUnitRouteResponse:
        """
        启用单元化路由
        """
        
        kwargs = {}
        kwargs["action"] = "EnableUnitRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableUnitRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableUnitRule(
            self,
            request: models.EnableUnitRuleRequest,
            opts: Dict = None,
    ) -> models.EnableUnitRuleResponse:
        """
        启用单元化规则
        """
        
        kwargs = {}
        kwargs["action"] = "EnableUnitRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableUnitRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteTask(
            self,
            request: models.ExecuteTaskRequest,
            opts: Dict = None,
    ) -> models.ExecuteTaskResponse:
        """
        手动执行一次任务
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteTaskFlow(
            self,
            request: models.ExecuteTaskFlowRequest,
            opts: Dict = None,
    ) -> models.ExecuteTaskFlowResponse:
        """
        执行一次工作流
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteTaskFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteTaskFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExpandGroup(
            self,
            request: models.ExpandGroupRequest,
            opts: Dict = None,
    ) -> models.ExpandGroupResponse:
        """
        虚拟机部署组添加实例
        """
        
        kwargs = {}
        kwargs["action"] = "ExpandGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExpandGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplication(
            self,
            request: models.ModifyApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationResponse:
        """
        修改应用
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCluster(
            self,
            request: models.ModifyClusterRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterResponse:
        """
        修改集群信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyContainerGroup(
            self,
            request: models.ModifyContainerGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyContainerGroupResponse:
        """
        修改容器部署组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContainerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContainerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyContainerReplicas(
            self,
            request: models.ModifyContainerReplicasRequest,
            opts: Dict = None,
    ) -> models.ModifyContainerReplicasResponse:
        """
        修改容器部署组实例数
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContainerReplicas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContainerReplicasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGroup(
            self,
            request: models.ModifyGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyGroupResponse:
        """
        更新部署组信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGroupLane(
            self,
            request: models.ModifyGroupLaneRequest,
            opts: Dict = None,
    ) -> models.ModifyGroupLaneResponse:
        """
        更新部署组泳道信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGroupLane"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGroupLaneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLane(
            self,
            request: models.ModifyLaneRequest,
            opts: Dict = None,
    ) -> models.ModifyLaneResponse:
        """
        更新泳道配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLane"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLaneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLaneRule(
            self,
            request: models.ModifyLaneRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyLaneRuleResponse:
        """
        更新灰度发布规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLaneRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLaneRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMicroservice(
            self,
            request: models.ModifyMicroserviceRequest,
            opts: Dict = None,
    ) -> models.ModifyMicroserviceResponse:
        """
        修改微服务详情
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMicroservice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMicroserviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNamespace(
            self,
            request: models.ModifyNamespaceRequest,
            opts: Dict = None,
    ) -> models.ModifyNamespaceResponse:
        """
        修改命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPathRewrite(
            self,
            request: models.ModifyPathRewriteRequest,
            opts: Dict = None,
    ) -> models.ModifyPathRewriteResponse:
        """
        修改路径重写
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPathRewrite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPathRewriteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProgram(
            self,
            request: models.ModifyProgramRequest,
            opts: Dict = None,
    ) -> models.ModifyProgramResponse:
        """
        更新数据集
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProgram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProgramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTask(
            self,
            request: models.ModifyTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskResponse:
        """
        修改任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUploadInfo(
            self,
            request: models.ModifyUploadInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyUploadInfoResponse:
        """
        调用该接口和COS的上传接口后，需要调用此接口更新TSF中保存的程序包状态。
        调用此接口完成后，才标志上传包流程结束。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUploadInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUploadInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OperateApplicationTcrBinding(
            self,
            request: models.OperateApplicationTcrBindingRequest,
            opts: Dict = None,
    ) -> models.OperateApplicationTcrBindingResponse:
        """
        绑定解绑tcr仓库
        """
        
        kwargs = {}
        kwargs["action"] = "OperateApplicationTcrBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OperateApplicationTcrBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReassociateBusinessLogConfig(
            self,
            request: models.ReassociateBusinessLogConfigRequest,
            opts: Dict = None,
    ) -> models.ReassociateBusinessLogConfigResponse:
        """
        后端服务已经删除这个接口,  API 接口下线处理

        重关联业务日志配置
        """
        
        kwargs = {}
        kwargs["action"] = "ReassociateBusinessLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReassociateBusinessLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RedoTask(
            self,
            request: models.RedoTaskRequest,
            opts: Dict = None,
    ) -> models.RedoTaskResponse:
        """
        重新执行任务
        """
        
        kwargs = {}
        kwargs["action"] = "RedoTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RedoTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RedoTaskBatch(
            self,
            request: models.RedoTaskBatchRequest,
            opts: Dict = None,
    ) -> models.RedoTaskBatchResponse:
        """
        重新执行任务批次
        """
        
        kwargs = {}
        kwargs["action"] = "RedoTaskBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RedoTaskBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RedoTaskExecute(
            self,
            request: models.RedoTaskExecuteRequest,
            opts: Dict = None,
    ) -> models.RedoTaskExecuteResponse:
        """
        重新执行在某个节点上执行任务。
        """
        
        kwargs = {}
        kwargs["action"] = "RedoTaskExecute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RedoTaskExecuteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RedoTaskFlowBatch(
            self,
            request: models.RedoTaskFlowBatchRequest,
            opts: Dict = None,
    ) -> models.RedoTaskFlowBatchResponse:
        """
        重新执行工作流批次
        """
        
        kwargs = {}
        kwargs["action"] = "RedoTaskFlowBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RedoTaskFlowBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseApiGroup(
            self,
            request: models.ReleaseApiGroupRequest,
            opts: Dict = None,
    ) -> models.ReleaseApiGroupResponse:
        """
        发布Api分组
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseApiGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseApiGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseConfig(
            self,
            request: models.ReleaseConfigRequest,
            opts: Dict = None,
    ) -> models.ReleaseConfigResponse:
        """
        发布配置
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseConfigWithDetailResp(
            self,
            request: models.ReleaseConfigWithDetailRespRequest,
            opts: Dict = None,
    ) -> models.ReleaseConfigWithDetailRespResponse:
        """
        发布配置，并且返回配置ID。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseConfigWithDetailResp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseConfigWithDetailRespResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseFileConfig(
            self,
            request: models.ReleaseFileConfigRequest,
            opts: Dict = None,
    ) -> models.ReleaseFileConfigResponse:
        """
        发布文件配置
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseFileConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseFileConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleasePublicConfig(
            self,
            request: models.ReleasePublicConfigRequest,
            opts: Dict = None,
    ) -> models.ReleasePublicConfigResponse:
        """
        发布公共配置
        """
        
        kwargs = {}
        kwargs["action"] = "ReleasePublicConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleasePublicConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveInstances(
            self,
            request: models.RemoveInstancesRequest,
            opts: Dict = None,
    ) -> models.RemoveInstancesResponse:
        """
        从 TSF 集群中批量移除云主机节点
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevocationConfig(
            self,
            request: models.RevocationConfigRequest,
            opts: Dict = None,
    ) -> models.RevocationConfigResponse:
        """
        撤回已发布的配置
        """
        
        kwargs = {}
        kwargs["action"] = "RevocationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevocationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevocationPublicConfig(
            self,
            request: models.RevocationPublicConfigRequest,
            opts: Dict = None,
    ) -> models.RevocationPublicConfigResponse:
        """
        撤回已发布的公共配置
        """
        
        kwargs = {}
        kwargs["action"] = "RevocationPublicConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevocationPublicConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokeFileConfig(
            self,
            request: models.RevokeFileConfigRequest,
            opts: Dict = None,
    ) -> models.RevokeFileConfigResponse:
        """
        撤回已发布的文件配置
        """
        
        kwargs = {}
        kwargs["action"] = "RevokeFileConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokeFileConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackConfig(
            self,
            request: models.RollbackConfigRequest,
            opts: Dict = None,
    ) -> models.RollbackConfigResponse:
        """
        回滚配置
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchBusinessLog(
            self,
            request: models.SearchBusinessLogRequest,
            opts: Dict = None,
    ) -> models.SearchBusinessLogResponse:
        """
        业务日志搜索
        """
        
        kwargs = {}
        kwargs["action"] = "SearchBusinessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchBusinessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchStdoutLog(
            self,
            request: models.SearchStdoutLogRequest,
            opts: Dict = None,
    ) -> models.SearchStdoutLogResponse:
        """
        标准输出日志搜索
        """
        
        kwargs = {}
        kwargs["action"] = "SearchStdoutLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchStdoutLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ShrinkGroup(
            self,
            request: models.ShrinkGroupRequest,
            opts: Dict = None,
    ) -> models.ShrinkGroupResponse:
        """
        下线部署组所有机器实例
        """
        
        kwargs = {}
        kwargs["action"] = "ShrinkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ShrinkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ShrinkInstances(
            self,
            request: models.ShrinkInstancesRequest,
            opts: Dict = None,
    ) -> models.ShrinkInstancesResponse:
        """
        虚拟机部署组下线实例
        """
        
        kwargs = {}
        kwargs["action"] = "ShrinkInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ShrinkInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartContainerGroup(
            self,
            request: models.StartContainerGroupRequest,
            opts: Dict = None,
    ) -> models.StartContainerGroupResponse:
        """
        启动容器部署组
        """
        
        kwargs = {}
        kwargs["action"] = "StartContainerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartContainerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartGroup(
            self,
            request: models.StartGroupRequest,
            opts: Dict = None,
    ) -> models.StartGroupResponse:
        """
        启动分组
        """
        
        kwargs = {}
        kwargs["action"] = "StartGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopContainerGroup(
            self,
            request: models.StopContainerGroupRequest,
            opts: Dict = None,
    ) -> models.StopContainerGroupResponse:
        """
        停止容器部署组
        """
        
        kwargs = {}
        kwargs["action"] = "StopContainerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopContainerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopGroup(
            self,
            request: models.StopGroupRequest,
            opts: Dict = None,
    ) -> models.StopGroupResponse:
        """
        停止虚拟机部署组
        """
        
        kwargs = {}
        kwargs["action"] = "StopGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopTaskBatch(
            self,
            request: models.StopTaskBatchRequest,
            opts: Dict = None,
    ) -> models.StopTaskBatchResponse:
        """
        停止执行中的任务批次， 非运行中的任务不可调用。
        """
        
        kwargs = {}
        kwargs["action"] = "StopTaskBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopTaskBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopTaskExecute(
            self,
            request: models.StopTaskExecuteRequest,
            opts: Dict = None,
    ) -> models.StopTaskExecuteResponse:
        """
        停止正在某个节点上执行的任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopTaskExecute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopTaskExecuteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateTaskFlowBatch(
            self,
            request: models.TerminateTaskFlowBatchRequest,
            opts: Dict = None,
    ) -> models.TerminateTaskFlowBatchResponse:
        """
        停止一个工作流批次
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateTaskFlowBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateTaskFlowBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindApiGroup(
            self,
            request: models.UnbindApiGroupRequest,
            opts: Dict = None,
    ) -> models.UnbindApiGroupResponse:
        """
        API分组批量与网关解绑
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindApiGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindApiGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateApiGroup(
            self,
            request: models.UpdateApiGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateApiGroupResponse:
        """
        更新Api分组
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateApiGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateApiGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateApiRateLimitRule(
            self,
            request: models.UpdateApiRateLimitRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateApiRateLimitRuleResponse:
        """
        更新API限流规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateApiRateLimitRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateApiRateLimitRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateApiRateLimitRules(
            self,
            request: models.UpdateApiRateLimitRulesRequest,
            opts: Dict = None,
    ) -> models.UpdateApiRateLimitRulesResponse:
        """
        批量更新API限流规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateApiRateLimitRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateApiRateLimitRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateApiTimeouts(
            self,
            request: models.UpdateApiTimeoutsRequest,
            opts: Dict = None,
    ) -> models.UpdateApiTimeoutsResponse:
        """
        批量更新API超时
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateApiTimeouts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateApiTimeoutsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConfigTemplate(
            self,
            request: models.UpdateConfigTemplateRequest,
            opts: Dict = None,
    ) -> models.UpdateConfigTemplateResponse:
        """
        更新参数模板
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConfigTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConfigTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGatewayApi(
            self,
            request: models.UpdateGatewayApiRequest,
            opts: Dict = None,
    ) -> models.UpdateGatewayApiResponse:
        """
        更新API
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGatewayApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGatewayApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateHealthCheckSettings(
            self,
            request: models.UpdateHealthCheckSettingsRequest,
            opts: Dict = None,
    ) -> models.UpdateHealthCheckSettingsResponse:
        """
        更新健康检查配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateHealthCheckSettings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateHealthCheckSettingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRepository(
            self,
            request: models.UpdateRepositoryRequest,
            opts: Dict = None,
    ) -> models.UpdateRepositoryResponse:
        """
        更新仓库信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUnitRule(
            self,
            request: models.UpdateUnitRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateUnitRuleResponse:
        """
        更新单元化规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUnitRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUnitRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)