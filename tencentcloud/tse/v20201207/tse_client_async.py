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
from tencentcloud.tse.v20201207 import models
from typing import Dict


class TseClient(AbstractClient):
    _apiVersion = '2020-12-07'
    _endpoint = 'tse.tencentcloudapi.com'
    _service = 'tse'

    async def BindAutoScalerResourceStrategyToGroups(
            self,
            request: models.BindAutoScalerResourceStrategyToGroupsRequest,
            opts: Dict = None,
    ) -> models.BindAutoScalerResourceStrategyToGroupsResponse:
        """
        弹性伸缩策略批量绑定网关分组
        """
        
        kwargs = {}
        kwargs["action"] = "BindAutoScalerResourceStrategyToGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindAutoScalerResourceStrategyToGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseWafProtection(
            self,
            request: models.CloseWafProtectionRequest,
            opts: Dict = None,
    ) -> models.CloseWafProtectionResponse:
        """
        关闭 WAF 防护
        """
        
        kwargs = {}
        kwargs["action"] = "CloseWafProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseWafProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoScalerResourceStrategy(
            self,
            request: models.CreateAutoScalerResourceStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateAutoScalerResourceStrategyResponse:
        """
        创建弹性伸缩策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoScalerResourceStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoScalerResourceStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGateway(
            self,
            request: models.CreateCloudNativeAPIGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayResponse:
        """
        创建云原生API网关实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayCanaryRule(
            self,
            request: models.CreateCloudNativeAPIGatewayCanaryRuleRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayCanaryRuleResponse:
        """
        创建云原生网关的灰度规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayCanaryRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayCanaryRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayCertificate(
            self,
            request: models.CreateCloudNativeAPIGatewayCertificateRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayCertificateResponse:
        """
        创建云原生网关证书
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayPublicNetwork(
            self,
            request: models.CreateCloudNativeAPIGatewayPublicNetworkRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayPublicNetworkResponse:
        """
        创建公网网络配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayPublicNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayPublicNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayRoute(
            self,
            request: models.CreateCloudNativeAPIGatewayRouteRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayRouteResponse:
        """
        创建云原生网关路由
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayRouteRateLimit(
            self,
            request: models.CreateCloudNativeAPIGatewayRouteRateLimitRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayRouteRateLimitResponse:
        """
        创建云原生网关限流插件(路由)
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayRouteRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayRouteRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayService(
            self,
            request: models.CreateCloudNativeAPIGatewayServiceRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayServiceResponse:
        """
        创建云原生网关服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayServiceRateLimit(
            self,
            request: models.CreateCloudNativeAPIGatewayServiceRateLimitRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayServiceRateLimitResponse:
        """
        创建云原生网关限流插件(服务)
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayServiceRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayServiceRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfigFile(
            self,
            request: models.CreateConfigFileRequest,
            opts: Dict = None,
    ) -> models.CreateConfigFileResponse:
        """
        创建配置文件
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfigFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfigFileGroup(
            self,
            request: models.CreateConfigFileGroupRequest,
            opts: Dict = None,
    ) -> models.CreateConfigFileGroupResponse:
        """
        创建服务治理中心配置文件组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfigFileGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigFileGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEngine(
            self,
            request: models.CreateEngineRequest,
            opts: Dict = None,
    ) -> models.CreateEngineResponse:
        """
        创建引擎实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGovernanceAlias(
            self,
            request: models.CreateGovernanceAliasRequest,
            opts: Dict = None,
    ) -> models.CreateGovernanceAliasResponse:
        """
        创建治理中心服务别名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGovernanceAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGovernanceAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGovernanceInstances(
            self,
            request: models.CreateGovernanceInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateGovernanceInstancesResponse:
        """
        创建服务实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGovernanceInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGovernanceInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGovernanceNamespaces(
            self,
            request: models.CreateGovernanceNamespacesRequest,
            opts: Dict = None,
    ) -> models.CreateGovernanceNamespacesResponse:
        """
        创建治理中心命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGovernanceNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGovernanceNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGovernanceServices(
            self,
            request: models.CreateGovernanceServicesRequest,
            opts: Dict = None,
    ) -> models.CreateGovernanceServicesResponse:
        """
        创建治理中心服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGovernanceServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGovernanceServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNativeGatewayServerGroup(
            self,
            request: models.CreateNativeGatewayServerGroupRequest,
            opts: Dict = None,
    ) -> models.CreateNativeGatewayServerGroupResponse:
        """
        创建云原生网关引擎分组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNativeGatewayServerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNativeGatewayServerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNativeGatewayServiceSource(
            self,
            request: models.CreateNativeGatewayServiceSourceRequest,
            opts: Dict = None,
    ) -> models.CreateNativeGatewayServiceSourceResponse:
        """
        创建网关服务来源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNativeGatewayServiceSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNativeGatewayServiceSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrModifyCloudNativeAPIGatewayIPRestriction(
            self,
            request: models.CreateOrModifyCloudNativeAPIGatewayIPRestrictionRequest,
            opts: Dict = None,
    ) -> models.CreateOrModifyCloudNativeAPIGatewayIPRestrictionResponse:
        """
        创建或编辑云原生网关访问控制
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrModifyCloudNativeAPIGatewayIPRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrModifyCloudNativeAPIGatewayIPRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrUpdateConfigFileAndRelease(
            self,
            request: models.CreateOrUpdateConfigFileAndReleaseRequest,
            opts: Dict = None,
    ) -> models.CreateOrUpdateConfigFileAndReleaseResponse:
        """
        创建或更新配置文件并发布配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrUpdateConfigFileAndRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrUpdateConfigFileAndReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWafDomains(
            self,
            request: models.CreateWafDomainsRequest,
            opts: Dict = None,
    ) -> models.CreateWafDomainsResponse:
        """
        新建 WAF 防护域名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWafDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWafDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoScalerResourceStrategy(
            self,
            request: models.DeleteAutoScalerResourceStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoScalerResourceStrategyResponse:
        """
        删除弹性伸缩策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoScalerResourceStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoScalerResourceStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGateway(
            self,
            request: models.DeleteCloudNativeAPIGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayResponse:
        """
        删除云原生API网关实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayCanaryRule(
            self,
            request: models.DeleteCloudNativeAPIGatewayCanaryRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayCanaryRuleResponse:
        """
        删除云原生网关的灰度规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayCanaryRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayCanaryRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayCertificate(
            self,
            request: models.DeleteCloudNativeAPIGatewayCertificateRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayCertificateResponse:
        """
        删除云原生网关证书
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayIPRestriction(
            self,
            request: models.DeleteCloudNativeAPIGatewayIPRestrictionRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayIPRestrictionResponse:
        """
        删除云原生网关访问控制
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayIPRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayIPRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayPublicNetwork(
            self,
            request: models.DeleteCloudNativeAPIGatewayPublicNetworkRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayPublicNetworkResponse:
        """
        删除公网网络配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayPublicNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayPublicNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayRoute(
            self,
            request: models.DeleteCloudNativeAPIGatewayRouteRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayRouteResponse:
        """
        删除云原生网关路由
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayRouteRateLimit(
            self,
            request: models.DeleteCloudNativeAPIGatewayRouteRateLimitRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayRouteRateLimitResponse:
        """
        删除云原生网关的限流插件(路由)
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayRouteRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayRouteRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayService(
            self,
            request: models.DeleteCloudNativeAPIGatewayServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayServiceResponse:
        """
        删除云原生网关服务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayServiceRateLimit(
            self,
            request: models.DeleteCloudNativeAPIGatewayServiceRateLimitRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayServiceRateLimitResponse:
        """
        删除云原生网关的限流插件(服务)
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayServiceRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayServiceRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfigFileGroup(
            self,
            request: models.DeleteConfigFileGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigFileGroupResponse:
        """
        删除配置文件分组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfigFileGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigFileGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfigFileReleases(
            self,
            request: models.DeleteConfigFileReleasesRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigFileReleasesResponse:
        """
        删除配置发布
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfigFileReleases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigFileReleasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfigFiles(
            self,
            request: models.DeleteConfigFilesRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigFilesResponse:
        """
        删除配置文件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfigFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEngine(
            self,
            request: models.DeleteEngineRequest,
            opts: Dict = None,
    ) -> models.DeleteEngineResponse:
        """
        删除引擎实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGovernanceAliases(
            self,
            request: models.DeleteGovernanceAliasesRequest,
            opts: Dict = None,
    ) -> models.DeleteGovernanceAliasesResponse:
        """
        删除治理中心服务别名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGovernanceAliases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGovernanceAliasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGovernanceInstances(
            self,
            request: models.DeleteGovernanceInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteGovernanceInstancesResponse:
        """
        删除服务实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGovernanceInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGovernanceInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGovernanceInstancesByHost(
            self,
            request: models.DeleteGovernanceInstancesByHostRequest,
            opts: Dict = None,
    ) -> models.DeleteGovernanceInstancesByHostResponse:
        """
        删除治理中心服务实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGovernanceInstancesByHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGovernanceInstancesByHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGovernanceNamespaces(
            self,
            request: models.DeleteGovernanceNamespacesRequest,
            opts: Dict = None,
    ) -> models.DeleteGovernanceNamespacesResponse:
        """
        删除治理中心命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGovernanceNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGovernanceNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGovernanceServices(
            self,
            request: models.DeleteGovernanceServicesRequest,
            opts: Dict = None,
    ) -> models.DeleteGovernanceServicesResponse:
        """
        删除治理中心服务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGovernanceServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGovernanceServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNativeGatewayServerGroup(
            self,
            request: models.DeleteNativeGatewayServerGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteNativeGatewayServerGroupResponse:
        """
        删除网关实例分组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNativeGatewayServerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNativeGatewayServerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNativeGatewayServiceSource(
            self,
            request: models.DeleteNativeGatewayServiceSourceRequest,
            opts: Dict = None,
    ) -> models.DeleteNativeGatewayServiceSourceResponse:
        """
        删除网关服务来源实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNativeGatewayServiceSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNativeGatewayServiceSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWafDomains(
            self,
            request: models.DeleteWafDomainsRequest,
            opts: Dict = None,
    ) -> models.DeleteWafDomainsResponse:
        """
        删除 WAF 防护域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWafDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWafDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllConfigFileTemplates(
            self,
            request: models.DescribeAllConfigFileTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAllConfigFileTemplatesResponse:
        """
        获取全量配置文件模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllConfigFileTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllConfigFileTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalerResourceStrategies(
            self,
            request: models.DescribeAutoScalerResourceStrategiesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalerResourceStrategiesResponse:
        """
        查看弹性伸缩策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalerResourceStrategies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalerResourceStrategiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalerResourceStrategyBindingGroups(
            self,
            request: models.DescribeAutoScalerResourceStrategyBindingGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalerResourceStrategyBindingGroupsResponse:
        """
        查看弹性伸缩策略绑定的网关分组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalerResourceStrategyBindingGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalerResourceStrategyBindingGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGateway(
            self,
            request: models.DescribeCloudNativeAPIGatewayRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayResponse:
        """
        获取云原生API网关实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayCanaryRules(
            self,
            request: models.DescribeCloudNativeAPIGatewayCanaryRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayCanaryRulesResponse:
        """
        查询云原生网关灰度规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayCanaryRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayCanaryRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayCertificateDetails(
            self,
            request: models.DescribeCloudNativeAPIGatewayCertificateDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayCertificateDetailsResponse:
        """
        查询云原生网关单个证书详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayCertificateDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayCertificateDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayCertificates(
            self,
            request: models.DescribeCloudNativeAPIGatewayCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayCertificatesResponse:
        """
        查询云原生网关证书列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayConfig(
            self,
            request: models.DescribeCloudNativeAPIGatewayConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayConfigResponse:
        """
        获取云原生API网关实例网络配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayIPRestriction(
            self,
            request: models.DescribeCloudNativeAPIGatewayIPRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayIPRestrictionResponse:
        """
        查询云原生网关访问控制
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayIPRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayIPRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayInfoByIp(
            self,
            request: models.DescribeCloudNativeAPIGatewayInfoByIpRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayInfoByIpResponse:
        """
        根据公网IP查询云原生网关实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayInfoByIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayInfoByIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayNodes(
            self,
            request: models.DescribeCloudNativeAPIGatewayNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayNodesResponse:
        """
        获取云原生网关节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayPorts(
            self,
            request: models.DescribeCloudNativeAPIGatewayPortsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayPortsResponse:
        """
        获取云原生API网关实例端口信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayPorts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayPortsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayRouteRateLimit(
            self,
            request: models.DescribeCloudNativeAPIGatewayRouteRateLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayRouteRateLimitResponse:
        """
        查询云原生网关的限流插件(路由)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayRouteRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayRouteRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayRoutes(
            self,
            request: models.DescribeCloudNativeAPIGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayRoutesResponse:
        """
        查询云原生网关路由列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayServiceRateLimit(
            self,
            request: models.DescribeCloudNativeAPIGatewayServiceRateLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayServiceRateLimitResponse:
        """
        查询云原生网关的限流插件(服务)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayServiceRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayServiceRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayServices(
            self,
            request: models.DescribeCloudNativeAPIGatewayServicesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayServicesResponse:
        """
        查询云原生网关服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayServicesLight(
            self,
            request: models.DescribeCloudNativeAPIGatewayServicesLightRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayServicesLightResponse:
        """
        轻量查询云原生网关服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayServicesLight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayServicesLightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayUpstream(
            self,
            request: models.DescribeCloudNativeAPIGatewayUpstreamRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayUpstreamResponse:
        """
        获取云原生网关服务详情下的Upstream列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayUpstream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayUpstreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGateways(
            self,
            request: models.DescribeCloudNativeAPIGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewaysResponse:
        """
        获取云原生API网关实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigFile(
            self,
            request: models.DescribeConfigFileRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigFileResponse:
        """
        根据命名空间、组、名字查找配置文件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigFileGroups(
            self,
            request: models.DescribeConfigFileGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigFileGroupsResponse:
        """
        根据条件分页查询配置文件组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigFileGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigFileGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigFileRelease(
            self,
            request: models.DescribeConfigFileReleaseRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigFileReleaseResponse:
        """
        获取配置文件发布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigFileRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigFileReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigFileReleaseHistories(
            self,
            request: models.DescribeConfigFileReleaseHistoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigFileReleaseHistoriesResponse:
        """
        获取配置文件发布历史列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigFileReleaseHistories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigFileReleaseHistoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigFileReleaseVersions(
            self,
            request: models.DescribeConfigFileReleaseVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigFileReleaseVersionsResponse:
        """
        查询某个配置所有版本信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigFileReleaseVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigFileReleaseVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigFileReleases(
            self,
            request: models.DescribeConfigFileReleasesRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigFileReleasesResponse:
        """
        查询配置版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigFileReleases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigFileReleasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigFiles(
            self,
            request: models.DescribeConfigFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigFilesResponse:
        """
        根据命名空间、组名、名称、标签查询配置文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigFilesByGroup(
            self,
            request: models.DescribeConfigFilesByGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigFilesByGroupResponse:
        """
        根据group查询配置文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigFilesByGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigFilesByGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGovernanceAliases(
            self,
            request: models.DescribeGovernanceAliasesRequest,
            opts: Dict = None,
    ) -> models.DescribeGovernanceAliasesResponse:
        """
        查询治理中心服务别名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGovernanceAliases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGovernanceAliasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGovernanceInstances(
            self,
            request: models.DescribeGovernanceInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeGovernanceInstancesResponse:
        """
        查询服务实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGovernanceInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGovernanceInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGovernanceNamespaces(
            self,
            request: models.DescribeGovernanceNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeGovernanceNamespacesResponse:
        """
        查询服务治理中心命名空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGovernanceNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGovernanceNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGovernanceServiceContractVersions(
            self,
            request: models.DescribeGovernanceServiceContractVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeGovernanceServiceContractVersionsResponse:
        """
        查询服务下契约版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGovernanceServiceContractVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGovernanceServiceContractVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGovernanceServiceContracts(
            self,
            request: models.DescribeGovernanceServiceContractsRequest,
            opts: Dict = None,
    ) -> models.DescribeGovernanceServiceContractsResponse:
        """
        查询服务契约定义列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGovernanceServiceContracts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGovernanceServiceContractsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGovernanceServices(
            self,
            request: models.DescribeGovernanceServicesRequest,
            opts: Dict = None,
    ) -> models.DescribeGovernanceServicesResponse:
        """
        查询治理中心服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGovernanceServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGovernanceServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceTagInfos(
            self,
            request: models.DescribeInstanceTagInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTagInfosResponse:
        """
        查看实例的标签信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceTagInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTagInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNacosReplicas(
            self,
            request: models.DescribeNacosReplicasRequest,
            opts: Dict = None,
    ) -> models.DescribeNacosReplicasResponse:
        """
        查询Nacos类型引擎实例副本信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNacosReplicas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNacosReplicasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNacosServerInterfaces(
            self,
            request: models.DescribeNacosServerInterfacesRequest,
            opts: Dict = None,
    ) -> models.DescribeNacosServerInterfacesResponse:
        """
        查询nacos服务接口列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNacosServerInterfaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNacosServerInterfacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNativeGatewayServerGroups(
            self,
            request: models.DescribeNativeGatewayServerGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeNativeGatewayServerGroupsResponse:
        """
        查询云原生网关分组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNativeGatewayServerGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNativeGatewayServerGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNativeGatewayServiceSources(
            self,
            request: models.DescribeNativeGatewayServiceSourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeNativeGatewayServiceSourcesResponse:
        """
        查询网关服务来源实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNativeGatewayServiceSources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNativeGatewayServiceSourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOneCloudNativeAPIGatewayService(
            self,
            request: models.DescribeOneCloudNativeAPIGatewayServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeOneCloudNativeAPIGatewayServiceResponse:
        """
        获取云原生网关服务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOneCloudNativeAPIGatewayService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOneCloudNativeAPIGatewayServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicAddressConfig(
            self,
            request: models.DescribePublicAddressConfigRequest,
            opts: Dict = None,
    ) -> models.DescribePublicAddressConfigResponse:
        """
        查询公网地址信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicAddressConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicAddressConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicNetwork(
            self,
            request: models.DescribePublicNetworkRequest,
            opts: Dict = None,
    ) -> models.DescribePublicNetworkResponse:
        """
        查询云原生API网关实例公网详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSREInstanceAccessAddress(
            self,
            request: models.DescribeSREInstanceAccessAddressRequest,
            opts: Dict = None,
    ) -> models.DescribeSREInstanceAccessAddressResponse:
        """
        查询引擎实例访问地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSREInstanceAccessAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSREInstanceAccessAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSREInstances(
            self,
            request: models.DescribeSREInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeSREInstancesResponse:
        """
        用于查询引擎实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSREInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSREInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpstreamHealthCheckConfig(
            self,
            request: models.DescribeUpstreamHealthCheckConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUpstreamHealthCheckConfigResponse:
        """
        获取云原生网关服务健康检查配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpstreamHealthCheckConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpstreamHealthCheckConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWafDomains(
            self,
            request: models.DescribeWafDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeWafDomainsResponse:
        """
        获取 WAF 防护域名
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWafDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWafDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWafProtection(
            self,
            request: models.DescribeWafProtectionRequest,
            opts: Dict = None,
    ) -> models.DescribeWafProtectionResponse:
        """
        获取 WAF 防护状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWafProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWafProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZookeeperReplicas(
            self,
            request: models.DescribeZookeeperReplicasRequest,
            opts: Dict = None,
    ) -> models.DescribeZookeeperReplicasResponse:
        """
        查询Zookeeper类型注册引擎实例副本信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZookeeperReplicas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZookeeperReplicasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZookeeperServerInterfaces(
            self,
            request: models.DescribeZookeeperServerInterfacesRequest,
            opts: Dict = None,
    ) -> models.DescribeZookeeperServerInterfacesResponse:
        """
        查询zookeeper服务接口列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZookeeperServerInterfaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZookeeperServerInterfacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoScalerResourceStrategy(
            self,
            request: models.ModifyAutoScalerResourceStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoScalerResourceStrategyResponse:
        """
        更新弹性伸缩策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoScalerResourceStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoScalerResourceStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGateway(
            self,
            request: models.ModifyCloudNativeAPIGatewayRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayResponse:
        """
        修改云原生API网关实例基础信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayCanaryRule(
            self,
            request: models.ModifyCloudNativeAPIGatewayCanaryRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayCanaryRuleResponse:
        """
        修改云原生网关的灰度规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayCanaryRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayCanaryRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayCertificate(
            self,
            request: models.ModifyCloudNativeAPIGatewayCertificateRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayCertificateResponse:
        """
        更新云原生网关证书
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayRoute(
            self,
            request: models.ModifyCloudNativeAPIGatewayRouteRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayRouteResponse:
        """
        修改云原生网关路由
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayRouteRateLimit(
            self,
            request: models.ModifyCloudNativeAPIGatewayRouteRateLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayRouteRateLimitResponse:
        """
        修改云原生网关限流插件(路由)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayRouteRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayRouteRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayService(
            self,
            request: models.ModifyCloudNativeAPIGatewayServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayServiceResponse:
        """
        修改云原生网关服务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayServiceRateLimit(
            self,
            request: models.ModifyCloudNativeAPIGatewayServiceRateLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayServiceRateLimitResponse:
        """
        修改云原生网关限流插件(服务)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayServiceRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayServiceRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConfigFileGroup(
            self,
            request: models.ModifyConfigFileGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyConfigFileGroupResponse:
        """
        批量修改配置文件组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConfigFileGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConfigFileGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConfigFiles(
            self,
            request: models.ModifyConfigFilesRequest,
            opts: Dict = None,
    ) -> models.ModifyConfigFilesResponse:
        """
        修改配置文件
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConfigFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConfigFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsoleNetwork(
            self,
            request: models.ModifyConsoleNetworkRequest,
            opts: Dict = None,
    ) -> models.ModifyConsoleNetworkResponse:
        """
        修改网关实例Konga网络配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsoleNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsoleNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGovernanceAlias(
            self,
            request: models.ModifyGovernanceAliasRequest,
            opts: Dict = None,
    ) -> models.ModifyGovernanceAliasResponse:
        """
        修改治理中心服务别名
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGovernanceAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGovernanceAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGovernanceInstances(
            self,
            request: models.ModifyGovernanceInstancesRequest,
            opts: Dict = None,
    ) -> models.ModifyGovernanceInstancesResponse:
        """
        修改治理中心服务实例
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGovernanceInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGovernanceInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGovernanceNamespaces(
            self,
            request: models.ModifyGovernanceNamespacesRequest,
            opts: Dict = None,
    ) -> models.ModifyGovernanceNamespacesResponse:
        """
        修改治理中心命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGovernanceNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGovernanceNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGovernanceServices(
            self,
            request: models.ModifyGovernanceServicesRequest,
            opts: Dict = None,
    ) -> models.ModifyGovernanceServicesResponse:
        """
        修改治理中心服务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGovernanceServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGovernanceServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNativeGatewayServerGroup(
            self,
            request: models.ModifyNativeGatewayServerGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyNativeGatewayServerGroupResponse:
        """
        修改云原生API网关实例分组基础信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNativeGatewayServerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNativeGatewayServerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNativeGatewayServiceSource(
            self,
            request: models.ModifyNativeGatewayServiceSourceRequest,
            opts: Dict = None,
    ) -> models.ModifyNativeGatewayServiceSourceResponse:
        """
        修改网关服务来源
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNativeGatewayServiceSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNativeGatewayServiceSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkAccessStrategy(
            self,
            request: models.ModifyNetworkAccessStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkAccessStrategyResponse:
        """
        修改云原生API网关实例Kong访问策略，支持白名单或者黑名单。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkAccessStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkAccessStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkBasicInfo(
            self,
            request: models.ModifyNetworkBasicInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkBasicInfoResponse:
        """
        修改云原生API网关实例网络基本信息，例如带宽以及描述、规格升级，只支持修改客户端公网/内网的信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkBasicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkBasicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUpstreamNodeStatus(
            self,
            request: models.ModifyUpstreamNodeStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyUpstreamNodeStatusResponse:
        """
        修改云原生网关上游实例节点健康状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUpstreamNodeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUpstreamNodeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenWafProtection(
            self,
            request: models.OpenWafProtectionRequest,
            opts: Dict = None,
    ) -> models.OpenWafProtectionResponse:
        """
        开启 WAF 防护
        """
        
        kwargs = {}
        kwargs["action"] = "OpenWafProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenWafProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishConfigFiles(
            self,
            request: models.PublishConfigFilesRequest,
            opts: Dict = None,
    ) -> models.PublishConfigFilesResponse:
        """
        发布配置文件
        """
        
        kwargs = {}
        kwargs["action"] = "PublishConfigFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishConfigFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartSREInstance(
            self,
            request: models.RestartSREInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartSREInstanceResponse:
        """
        重启微服务引擎实例
        """
        
        kwargs = {}
        kwargs["action"] = "RestartSREInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartSREInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackConfigFileReleases(
            self,
            request: models.RollbackConfigFileReleasesRequest,
            opts: Dict = None,
    ) -> models.RollbackConfigFileReleasesResponse:
        """
        回滚配置发布
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackConfigFileReleases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackConfigFileReleasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindAutoScalerResourceStrategyFromGroups(
            self,
            request: models.UnbindAutoScalerResourceStrategyFromGroupsRequest,
            opts: Dict = None,
    ) -> models.UnbindAutoScalerResourceStrategyFromGroupsResponse:
        """
        弹性伸缩策略批量解绑网关分组
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindAutoScalerResourceStrategyFromGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindAutoScalerResourceStrategyFromGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCloudNativeAPIGatewayCertificateInfo(
            self,
            request: models.UpdateCloudNativeAPIGatewayCertificateInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateCloudNativeAPIGatewayCertificateInfoResponse:
        """
        修改云原生网关证书信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCloudNativeAPIGatewayCertificateInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCloudNativeAPIGatewayCertificateInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCloudNativeAPIGatewaySpec(
            self,
            request: models.UpdateCloudNativeAPIGatewaySpecRequest,
            opts: Dict = None,
    ) -> models.UpdateCloudNativeAPIGatewaySpecResponse:
        """
        修改云原生API网关实例的节点规格信息，例如节点扩缩容或者升降配
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCloudNativeAPIGatewaySpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCloudNativeAPIGatewaySpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEngineInternetAccess(
            self,
            request: models.UpdateEngineInternetAccessRequest,
            opts: Dict = None,
    ) -> models.UpdateEngineInternetAccessResponse:
        """
        修改引擎公网访问配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEngineInternetAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEngineInternetAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUpstreamHealthCheckConfig(
            self,
            request: models.UpdateUpstreamHealthCheckConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateUpstreamHealthCheckConfigResponse:
        """
        更新云原生网关健康检查配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUpstreamHealthCheckConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUpstreamHealthCheckConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUpstreamTargets(
            self,
            request: models.UpdateUpstreamTargetsRequest,
            opts: Dict = None,
    ) -> models.UpdateUpstreamTargetsResponse:
        """
        更新网关上游实例列表，仅支持IPList服务类型
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUpstreamTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUpstreamTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)