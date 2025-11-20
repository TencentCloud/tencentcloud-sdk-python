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
from tencentcloud.tem.v20210701 import models
from typing import Dict


class TemClient(AbstractClient):
    _apiVersion = '2021-07-01'
    _endpoint = 'tem.tencentcloudapi.com'
    _service = 'tem'

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
        
    async def CreateApplicationAutoscaler(
            self,
            request: models.CreateApplicationAutoscalerRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationAutoscalerResponse:
        """
        创建弹性伸缩策略组合
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationAutoscaler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationAutoscalerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationService(
            self,
            request: models.CreateApplicationServiceRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationServiceResponse:
        """
        新增访问方式
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfigData(
            self,
            request: models.CreateConfigDataRequest,
            opts: Dict = None,
    ) -> models.CreateConfigDataResponse:
        """
        创建配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfigData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosToken(
            self,
            request: models.CreateCosTokenRequest,
            opts: Dict = None,
    ) -> models.CreateCosTokenResponse:
        """
        生成Cos临时密钥
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnvironment(
            self,
            request: models.CreateEnvironmentRequest,
            opts: Dict = None,
    ) -> models.CreateEnvironmentResponse:
        """
        创建环境
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLogConfig(
            self,
            request: models.CreateLogConfigRequest,
            opts: Dict = None,
    ) -> models.CreateLogConfigResponse:
        """
        创建日志收集配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResource(
            self,
            request: models.CreateResourceRequest,
            opts: Dict = None,
    ) -> models.CreateResourceResponse:
        """
        绑定云资源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplication(
            self,
            request: models.DeleteApplicationRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationResponse:
        """
        服务删除
          - 停止当前运行服务
          - 删除服务相关资源
          - 删除服务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationAutoscaler(
            self,
            request: models.DeleteApplicationAutoscalerRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationAutoscalerResponse:
        """
        删除应用弹性策略组合
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationAutoscaler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationAutoscalerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationService(
            self,
            request: models.DeleteApplicationServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationServiceResponse:
        """
        删除一条访问方式
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIngress(
            self,
            request: models.DeleteIngressRequest,
            opts: Dict = None,
    ) -> models.DeleteIngressResponse:
        """
        删除 Ingress 规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIngress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIngressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployApplication(
            self,
            request: models.DeployApplicationRequest,
            opts: Dict = None,
    ) -> models.DeployApplicationResponse:
        """
        应用部署
        """
        
        kwargs = {}
        kwargs["action"] = "DeployApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationAutoscalerList(
            self,
            request: models.DescribeApplicationAutoscalerListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationAutoscalerListResponse:
        """
        获取应用弹性策略组合
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationAutoscalerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationAutoscalerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationInfo(
            self,
            request: models.DescribeApplicationInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationInfoResponse:
        """
        服务基本信息查看
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationPods(
            self,
            request: models.DescribeApplicationPodsRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationPodsResponse:
        """
        获取应用实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationPods"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationPodsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationServiceList(
            self,
            request: models.DescribeApplicationServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationServiceListResponse:
        """
        查询应用访问方式列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplications(
            self,
            request: models.DescribeApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationsResponse:
        """
        获取运行服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationsStatus(
            self,
            request: models.DescribeApplicationsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationsStatusResponse:
        """
        单环境下所有应用状态查看
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigData(
            self,
            request: models.DescribeConfigDataRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigDataResponse:
        """
        查询配置详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigDataList(
            self,
            request: models.DescribeConfigDataListRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigDataListResponse:
        """
        查询配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigDataList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigDataListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeployApplicationDetail(
            self,
            request: models.DescribeDeployApplicationDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDeployApplicationDetailResponse:
        """
        获取分批发布详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeployApplicationDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeployApplicationDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironment(
            self,
            request: models.DescribeEnvironmentRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentResponse:
        """
        获取环境基础信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironmentStatus(
            self,
            request: models.DescribeEnvironmentStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentStatusResponse:
        """
        获取环境状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironmentStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        获取环境列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIngress(
            self,
            request: models.DescribeIngressRequest,
            opts: Dict = None,
    ) -> models.DescribeIngressResponse:
        """
        查询 Ingress 规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIngress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIngressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIngresses(
            self,
            request: models.DescribeIngressesRequest,
            opts: Dict = None,
    ) -> models.DescribeIngressesResponse:
        """
        查询 Ingress 规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIngresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIngressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogConfig(
            self,
            request: models.DescribeLogConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeLogConfigResponse:
        """
        查询日志收集配置详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePagedLogConfigList(
            self,
            request: models.DescribePagedLogConfigListRequest,
            opts: Dict = None,
    ) -> models.DescribePagedLogConfigListResponse:
        """
        查询分页的日志收集配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePagedLogConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePagedLogConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRelatedIngresses(
            self,
            request: models.DescribeRelatedIngressesRequest,
            opts: Dict = None,
    ) -> models.DescribeRelatedIngressesResponse:
        """
        查询应用关联的 Ingress 规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRelatedIngresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRelatedIngressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyConfigData(
            self,
            request: models.DestroyConfigDataRequest,
            opts: Dict = None,
    ) -> models.DestroyConfigDataResponse:
        """
        销毁配置
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyConfigData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyConfigDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyEnvironment(
            self,
            request: models.DestroyEnvironmentRequest,
            opts: Dict = None,
    ) -> models.DestroyEnvironmentResponse:
        """
        销毁环境
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyLogConfig(
            self,
            request: models.DestroyLogConfigRequest,
            opts: Dict = None,
    ) -> models.DestroyLogConfigResponse:
        """
        销毁日志收集配置
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableApplicationAutoscaler(
            self,
            request: models.DisableApplicationAutoscalerRequest,
            opts: Dict = None,
    ) -> models.DisableApplicationAutoscalerResponse:
        """
        关闭应用弹性策略组合
        """
        
        kwargs = {}
        kwargs["action"] = "DisableApplicationAutoscaler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableApplicationAutoscalerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableApplicationAutoscaler(
            self,
            request: models.EnableApplicationAutoscalerRequest,
            opts: Dict = None,
    ) -> models.EnableApplicationAutoscalerResponse:
        """
        启用应用弹性策略组合
        """
        
        kwargs = {}
        kwargs["action"] = "EnableApplicationAutoscaler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableApplicationAutoscalerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateApplicationPackageDownloadUrl(
            self,
            request: models.GenerateApplicationPackageDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.GenerateApplicationPackageDownloadUrlResponse:
        """
        生成应用程序包预签名下载链接
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateApplicationPackageDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateApplicationPackageDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationAutoscaler(
            self,
            request: models.ModifyApplicationAutoscalerRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationAutoscalerResponse:
        """
        修改弹性伸缩策略组合
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationAutoscaler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationAutoscalerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationInfo(
            self,
            request: models.ModifyApplicationInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationInfoResponse:
        """
        修改应用基本信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationReplicas(
            self,
            request: models.ModifyApplicationReplicasRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationReplicasResponse:
        """
        修改应用实例数量
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationReplicas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationReplicasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationService(
            self,
            request: models.ModifyApplicationServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationServiceResponse:
        """
        修改服务访问方式列表
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConfigData(
            self,
            request: models.ModifyConfigDataRequest,
            opts: Dict = None,
    ) -> models.ModifyConfigDataResponse:
        """
        编辑配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConfigData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConfigDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnvironment(
            self,
            request: models.ModifyEnvironmentRequest,
            opts: Dict = None,
    ) -> models.ModifyEnvironmentResponse:
        """
        编辑环境
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGatewayIngress(
            self,
            request: models.ModifyGatewayIngressRequest,
            opts: Dict = None,
    ) -> models.ModifyGatewayIngressResponse:
        """
        修改网关的转发配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGatewayIngress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGatewayIngressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIngress(
            self,
            request: models.ModifyIngressRequest,
            opts: Dict = None,
    ) -> models.ModifyIngressResponse:
        """
        此接口没有被使用了

        创建或者更新 Ingress 规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIngress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIngressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogConfig(
            self,
            request: models.ModifyLogConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyLogConfigResponse:
        """
        编辑日志收集配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartApplication(
            self,
            request: models.RestartApplicationRequest,
            opts: Dict = None,
    ) -> models.RestartApplicationResponse:
        """
        服务重启
        """
        
        kwargs = {}
        kwargs["action"] = "RestartApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartApplicationPod(
            self,
            request: models.RestartApplicationPodRequest,
            opts: Dict = None,
    ) -> models.RestartApplicationPodResponse:
        """
        重启应用实例
        """
        
        kwargs = {}
        kwargs["action"] = "RestartApplicationPod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartApplicationPodResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeDeployApplication(
            self,
            request: models.ResumeDeployApplicationRequest,
            opts: Dict = None,
    ) -> models.ResumeDeployApplicationResponse:
        """
        开始下一批次发布
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeDeployApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeDeployApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevertDeployApplication(
            self,
            request: models.RevertDeployApplicationRequest,
            opts: Dict = None,
    ) -> models.RevertDeployApplicationResponse:
        """
        回滚分批发布
        """
        
        kwargs = {}
        kwargs["action"] = "RevertDeployApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevertDeployApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollingUpdateApplicationByVersion(
            self,
            request: models.RollingUpdateApplicationByVersionRequest,
            opts: Dict = None,
    ) -> models.RollingUpdateApplicationByVersionResponse:
        """
        更新应用部署版本
        """
        
        kwargs = {}
        kwargs["action"] = "RollingUpdateApplicationByVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollingUpdateApplicationByVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopApplication(
            self,
            request: models.StopApplicationRequest,
            opts: Dict = None,
    ) -> models.StopApplicationResponse:
        """
        服务停止
        """
        
        kwargs = {}
        kwargs["action"] = "StopApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)