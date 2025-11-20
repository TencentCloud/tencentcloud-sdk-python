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
from tencentcloud.apigateway.v20180808 import models
from typing import Dict


class ApigatewayClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'apigateway.tencentcloudapi.com'
    _service = 'apigateway'

    async def AttachPlugin(
            self,
            request: models.AttachPluginRequest,
            opts: Dict = None,
    ) -> models.AttachPluginResponse:
        """
        绑定插件到API上。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachPlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachPluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindApiApp(
            self,
            request: models.BindApiAppRequest,
            opts: Dict = None,
    ) -> models.BindApiAppResponse:
        """
        本接口（BindApiApp）用于绑定应用到API。
        """
        
        kwargs = {}
        kwargs["action"] = "BindApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindEnvironment(
            self,
            request: models.BindEnvironmentRequest,
            opts: Dict = None,
    ) -> models.BindEnvironmentResponse:
        """
        本接口（BindEnvironment）用于绑定使用计划到服务或API。
        用户在发布服务到某个环境中后，如果 API 需要鉴权，还需要绑定使用计划才能进行调用，此接口用户将使用计划绑定到特定环境。
        目前支持绑定使用计划到API，但是同一个服务不能同时存在绑定到服务的使用计划和绑定到API的使用计划，所以对已经绑定过服务级别使用计划的环境，请先使用 服务级别使用计划降级 接口进行降级操作。
        """
        
        kwargs = {}
        kwargs["action"] = "BindEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindIPStrategy(
            self,
            request: models.BindIPStrategyRequest,
            opts: Dict = None,
    ) -> models.BindIPStrategyResponse:
        """
        本接口（BindIPStrategy）用于API绑定IP策略。
        """
        
        kwargs = {}
        kwargs["action"] = "BindIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindSecretIds(
            self,
            request: models.BindSecretIdsRequest,
            opts: Dict = None,
    ) -> models.BindSecretIdsResponse:
        """
        本接口（BindSecretIds）用于为使用计划绑定密钥。
        将密钥绑定到某个使用计划，并将此使用计划绑定到某个服务发布的环境上，调用者方可使用此密钥调用这个服务中的 API，可使用本接口为使用计划绑定密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "BindSecretIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindSecretIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindSubDomain(
            self,
            request: models.BindSubDomainRequest,
            opts: Dict = None,
    ) -> models.BindSubDomainResponse:
        """
        本接口（BindSubDomain）用于绑定自定义域名到服务。
        API 网关中每个服务都会提供一个默认的域名供用户调用，但当用户想使用自己的已有域名时，也可以将自定义域名绑定到此服务，在做好备案、与默认域名的 CNAME 后，可直接调用自定义域名。
        """
        
        kwargs = {}
        kwargs["action"] = "BindSubDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindSubDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BuildAPIDoc(
            self,
            request: models.BuildAPIDocRequest,
            opts: Dict = None,
    ) -> models.BuildAPIDocResponse:
        """
        构建 API 文档
        """
        
        kwargs = {}
        kwargs["action"] = "BuildAPIDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BuildAPIDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAPIDoc(
            self,
            request: models.CreateAPIDocRequest,
            opts: Dict = None,
    ) -> models.CreateAPIDocResponse:
        """
        创建 API 文档
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAPIDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAPIDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApi(
            self,
            request: models.CreateApiRequest,
            opts: Dict = None,
    ) -> models.CreateApiResponse:
        """
        本接口（CreateApi）用于创建 API 接口，创建 API 前，用户需要先创建服务，每个 API 都有自己归属的服务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApiApp(
            self,
            request: models.CreateApiAppRequest,
            opts: Dict = None,
    ) -> models.CreateApiAppResponse:
        """
        本接口（CreateApiApp）用于创建应用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApiKey(
            self,
            request: models.CreateApiKeyRequest,
            opts: Dict = None,
    ) -> models.CreateApiKeyResponse:
        """
        本接口（CreateApiKey）用于创建一对新的 API 密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExclusiveInstances(
            self,
            request: models.CreateExclusiveInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateExclusiveInstancesResponse:
        """
        创建专享实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExclusiveInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExclusiveInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIPStrategy(
            self,
            request: models.CreateIPStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateIPStrategyResponse:
        """
        本接口（CreateIPStrategy）用于创建服务IP策略。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePlugin(
            self,
            request: models.CreatePluginRequest,
            opts: Dict = None,
    ) -> models.CreatePluginResponse:
        """
        创建API网关插件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateService(
            self,
            request: models.CreateServiceRequest,
            opts: Dict = None,
    ) -> models.CreateServiceResponse:
        """
        本接口（CreateService）用于创建服务。
        API 网关使用的最大单元为服务，每个服务中可创建多个 API 接口。每个服务有一个默认域名供客户调用，用户也可绑定自定义域名到此服务中。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUpstream(
            self,
            request: models.CreateUpstreamRequest,
            opts: Dict = None,
    ) -> models.CreateUpstreamResponse:
        """
        用于创建后端通道
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUpstream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUpstreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUsagePlan(
            self,
            request: models.CreateUsagePlanRequest,
            opts: Dict = None,
    ) -> models.CreateUsagePlanResponse:
        """
        本接口（CreateUsagePlan）用于创建使用计划。
        用户在使用 API 网关时，需要创建使用计划并将其绑定到服务的环境中使用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAPIDoc(
            self,
            request: models.DeleteAPIDocRequest,
            opts: Dict = None,
    ) -> models.DeleteAPIDocResponse:
        """
        删除 API 文档
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAPIDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAPIDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApi(
            self,
            request: models.DeleteApiRequest,
            opts: Dict = None,
    ) -> models.DeleteApiResponse:
        """
        本接口（DeleteApi）用于删除已经创建的API。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApiApp(
            self,
            request: models.DeleteApiAppRequest,
            opts: Dict = None,
    ) -> models.DeleteApiAppResponse:
        """
        本接口（DeleteApiApp）用于删除已经创建的应用。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApiKey(
            self,
            request: models.DeleteApiKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteApiKeyResponse:
        """
        本接口（DeleteApiKey）用于删除一对 API 密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIPStrategy(
            self,
            request: models.DeleteIPStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteIPStrategyResponse:
        """
        本接口（DeleteIPStrategy）用于删除服务IP策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePlugin(
            self,
            request: models.DeletePluginRequest,
            opts: Dict = None,
    ) -> models.DeletePluginResponse:
        """
        删除API网关插件
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteService(
            self,
            request: models.DeleteServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceResponse:
        """
        本接口（DeleteService）用于删除 API 网关中某个服务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceSubDomainMapping(
            self,
            request: models.DeleteServiceSubDomainMappingRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceSubDomainMappingResponse:
        """
        本接口（DeleteServiceSubDomainMapping）用于删除服务中某个环境的自定义域名映射。
        当用户使用自定义域名，并使用了自定义映射时，可使用此接口。但需注意，若删除了所有环境的映射时，调用此 API 均会返回失败。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceSubDomainMapping"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceSubDomainMappingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUpstream(
            self,
            request: models.DeleteUpstreamRequest,
            opts: Dict = None,
    ) -> models.DeleteUpstreamResponse:
        """
        删除后端通道，需要注意有API绑定时，不允许删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUpstream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUpstreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsagePlan(
            self,
            request: models.DeleteUsagePlanRequest,
            opts: Dict = None,
    ) -> models.DeleteUsagePlanResponse:
        """
        本接口（DeleteUsagePlan）用于删除使用计划。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DemoteServiceUsagePlan(
            self,
            request: models.DemoteServiceUsagePlanRequest,
            opts: Dict = None,
    ) -> models.DemoteServiceUsagePlanResponse:
        """
        本接口（DemoteServiceUsagePlan）用于将某个服务在某个环境的使用计划，降级到API上。
        如果服务内没有API不允许进行此操作。
        如果当前环境没有发布，不允许进行此操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DemoteServiceUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DemoteServiceUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAPIDocDetail(
            self,
            request: models.DescribeAPIDocDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAPIDocDetailResponse:
        """
        查询 API 文档详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAPIDocDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAPIDocDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAPIDocs(
            self,
            request: models.DescribeAPIDocsRequest,
            opts: Dict = None,
    ) -> models.DescribeAPIDocsResponse:
        """
        查询 API 文档列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAPIDocs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAPIDocsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllPluginApis(
            self,
            request: models.DescribeAllPluginApisRequest,
            opts: Dict = None,
    ) -> models.DescribeAllPluginApisResponse:
        """
        展示插件相关的API列表，包括已绑定的和未绑定的API信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllPluginApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllPluginApisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApi(
            self,
            request: models.DescribeApiRequest,
            opts: Dict = None,
    ) -> models.DescribeApiResponse:
        """
        本接口（DescribeApi）用于查询用户 API 网关的 API 接口的详细信息。​
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiApp(
            self,
            request: models.DescribeApiAppRequest,
            opts: Dict = None,
    ) -> models.DescribeApiAppResponse:
        """
        本接口（DescribeApiApp）用于根据应用ID搜索应用。此接口已下线，如需使用功能请使用DescribeApiAppsStatus接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiAppBindApisStatus(
            self,
            request: models.DescribeApiAppBindApisStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApiAppBindApisStatusResponse:
        """
        本接口（DescribeApiAppBindApisStatus）查询应用绑定的Api列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiAppBindApisStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiAppBindApisStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiAppsStatus(
            self,
            request: models.DescribeApiAppsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApiAppsStatusResponse:
        """
        本接口（DescribeApiAppsStatus）查询应用列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiAppsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiAppsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiBindApiAppsStatus(
            self,
            request: models.DescribeApiBindApiAppsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApiBindApiAppsStatusResponse:
        """
        本接口（DescribeApiBindApiAppsStatus）查询Api绑定的应用列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiBindApiAppsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiBindApiAppsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiEnvironmentStrategy(
            self,
            request: models.DescribeApiEnvironmentStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeApiEnvironmentStrategyResponse:
        """
        本接口（DescribeApiEnvironmentStrategy）用于展示API绑定的限流策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiEnvironmentStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiEnvironmentStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiForApiApp(
            self,
            request: models.DescribeApiForApiAppRequest,
            opts: Dict = None,
    ) -> models.DescribeApiForApiAppResponse:
        """
        本接口（DescribeApiForApiApp）用于应用使用者查询部署于 API 网关的 API 接口的详细信息。​
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiForApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiForApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiKey(
            self,
            request: models.DescribeApiKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeApiKeyResponse:
        """
        本接口（DescribeApiKey）用于查询密钥详情。
        用户在创建密钥后，可用此接口查询一个 API 密钥的详情，该接口会显示密钥 Key。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiKeysStatus(
            self,
            request: models.DescribeApiKeysStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApiKeysStatusResponse:
        """
        本接口（DescribeApiKeysStatus）用于查询密钥列表。
        当用户创建了多个密钥对时，可使用本接口查询一个或多个 API 密钥信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiKeysStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiKeysStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiUsagePlan(
            self,
            request: models.DescribeApiUsagePlanRequest,
            opts: Dict = None,
    ) -> models.DescribeApiUsagePlanResponse:
        """
        本接口（DescribeApiUsagePlan）用于查询服务中 API 使用计划详情。
        服务若需要鉴权限流生效，则需要绑定使用计划到此服务中，本接口用于查询绑定到一个服务及其中 API 的所有使用计划。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApisStatus(
            self,
            request: models.DescribeApisStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApisStatusResponse:
        """
        本接口（DescribeApisStatus）用于查看一个服务下的某个 API 或所有 API 列表及其相关信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApisStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApisStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExclusiveInstanceDetail(
            self,
            request: models.DescribeExclusiveInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeExclusiveInstanceDetailResponse:
        """
        本接口（DescribeExclusiveInstanceDetail）用于查询独享实例详情信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExclusiveInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExclusiveInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExclusiveInstanceRegions(
            self,
            request: models.DescribeExclusiveInstanceRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeExclusiveInstanceRegionsResponse:
        """
        Get the list of supported regions for dedicated instances
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExclusiveInstanceRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExclusiveInstanceRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExclusiveInstances(
            self,
            request: models.DescribeExclusiveInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeExclusiveInstancesResponse:
        """
        本接口（DescribeExclusiveInstances）用于查询独享实例列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExclusiveInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExclusiveInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExclusiveInstancesStatus(
            self,
            request: models.DescribeExclusiveInstancesStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeExclusiveInstancesStatusResponse:
        """
        查询专享实例列表（新）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExclusiveInstancesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExclusiveInstancesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPStrategy(
            self,
            request: models.DescribeIPStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeIPStrategyResponse:
        """
        本接口（DescribeIPStrategy）用于查询IP策略详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPStrategyApisStatus(
            self,
            request: models.DescribeIPStrategyApisStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeIPStrategyApisStatusResponse:
        """
        本接口（DescribeIPStrategyApisStatus）用于查询IP策略可以绑定的API列表。即服务下所有API和该策略已绑定API的差集。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPStrategyApisStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPStrategyApisStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPStrategysStatus(
            self,
            request: models.DescribeIPStrategysStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeIPStrategysStatusResponse:
        """
        本接口（DescribeIPStrategysStatus）用于查询服务IP策略列表，因为接口名拼写错误，已不推荐使用，请优先使用DescribeIPStrategiesStatus接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPStrategysStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPStrategysStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesNetworkConfig(
            self,
            request: models.DescribeInstancesNetworkConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesNetworkConfigResponse:
        """
        获取专享实例网络配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesNetworkConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesNetworkConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogSearch(
            self,
            request: models.DescribeLogSearchRequest,
            opts: Dict = None,
    ) -> models.DescribeLogSearchResponse:
        """
        本接口DescribeLogSearch用于搜索日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogSearch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogSearchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlugin(
            self,
            request: models.DescribePluginRequest,
            opts: Dict = None,
    ) -> models.DescribePluginResponse:
        """
        展示插件详情，支持按照插件ID进行。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePluginApis(
            self,
            request: models.DescribePluginApisRequest,
            opts: Dict = None,
    ) -> models.DescribePluginApisResponse:
        """
        查询指定插件下绑定的API信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePluginApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginApisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlugins(
            self,
            request: models.DescribePluginsRequest,
            opts: Dict = None,
    ) -> models.DescribePluginsResponse:
        """
        展示插件列表和详情，支持分页，支持按照插件类型查询，支持按照插件ID批量查询，支持按照插件名称查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePluginsByApi(
            self,
            request: models.DescribePluginsByApiRequest,
            opts: Dict = None,
    ) -> models.DescribePluginsByApiResponse:
        """
        展示API上已绑定的插件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePluginsByApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePluginsByApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeService(
            self,
            request: models.DescribeServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceResponse:
        """
        本接口（DescribeService）用于查询一个服务的详细信息、包括服务的描述、域名、协议、创建时间、发布情况等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceEnvironmentList(
            self,
            request: models.DescribeServiceEnvironmentListRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceEnvironmentListResponse:
        """
        本接口（DescribeServiceEnvironmentList）用于查询一个服务的环境列表，可查询到此服务下所有环境及其状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceEnvironmentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceEnvironmentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceEnvironmentReleaseHistory(
            self,
            request: models.DescribeServiceEnvironmentReleaseHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceEnvironmentReleaseHistoryResponse:
        """
        本接口（DescribeServiceEnvironmentReleaseHistory）用于查询服务环境的发布历史。
        用户在创建好服务后需要发布到某个环境中才能进行使用，本接口用于查询一个服务某个环境的发布记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceEnvironmentReleaseHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceEnvironmentReleaseHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceEnvironmentStrategy(
            self,
            request: models.DescribeServiceEnvironmentStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceEnvironmentStrategyResponse:
        """
        本接口（DescribeServiceEnvironmentStrategy）用于展示服务限流策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceEnvironmentStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceEnvironmentStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceForApiApp(
            self,
            request: models.DescribeServiceForApiAppRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceForApiAppResponse:
        """
        本接口（DescribeServiceForApiApp）用于应用使用者查询一个服务的详细信息、包括服务的描述、域名、协议等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceForApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceForApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceReleaseVersion(
            self,
            request: models.DescribeServiceReleaseVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceReleaseVersionResponse:
        """
        本接口（DescribeServiceReleaseVersion）查询一个服务下面所有已经发布的版本列表。
        用户在发布服务时，常有多个版本发布，可使用本接口查询已发布的版本。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceReleaseVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceReleaseVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceSubDomainMappings(
            self,
            request: models.DescribeServiceSubDomainMappingsRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceSubDomainMappingsResponse:
        """
        本接口（DescribeServiceSubDomainMappings）用于查询自定义域名的路径映射。
        API 网关可绑定自定义域名到服务，并且可以对自定义域名的路径进行映射，可自定义不同的路径映射到服务中的三个环境，本接口用于查询绑定服务的自定义域名的路径映射列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceSubDomainMappings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceSubDomainMappingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceSubDomains(
            self,
            request: models.DescribeServiceSubDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceSubDomainsResponse:
        """
        本接口（DescribeServiceSubDomains）用于查询自定义域名列表。
        API 网关可绑定自定义域名到服务，用于服务调用。此接口用于查询用户绑定在服务的自定义域名列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceSubDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceSubDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceUsagePlan(
            self,
            request: models.DescribeServiceUsagePlanRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceUsagePlanResponse:
        """
        本接口（DescribeServiceUsagePlan）用于查询服务使用计划详情。
        服务若需要鉴权限流生效，则需要绑定使用计划到此服务中，本接口用于查询绑定到一个服务的所有使用计划。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServicesStatus(
            self,
            request: models.DescribeServicesStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeServicesStatusResponse:
        """
        本接口（DescribeServicesStatus）用于搜索查询某一个服务或多个服务的列表，并返回服务相关的域名、时间等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServicesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServicesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpstreamBindApis(
            self,
            request: models.DescribeUpstreamBindApisRequest,
            opts: Dict = None,
    ) -> models.DescribeUpstreamBindApisResponse:
        """
        查询后端通道所绑定的API列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpstreamBindApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpstreamBindApisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpstreams(
            self,
            request: models.DescribeUpstreamsRequest,
            opts: Dict = None,
    ) -> models.DescribeUpstreamsResponse:
        """
        查询后端通道列表详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpstreams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpstreamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsagePlan(
            self,
            request: models.DescribeUsagePlanRequest,
            opts: Dict = None,
    ) -> models.DescribeUsagePlanResponse:
        """
        本接口（DescribeUsagePlan）用于查询一个使用计划的详细信息，包括名称、QPS、创建时间绑定的环境等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsagePlanEnvironments(
            self,
            request: models.DescribeUsagePlanEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeUsagePlanEnvironmentsResponse:
        """
        本接口（DescribeUsagePlanEnvironments）用于查询使用计划绑定的环境列表。
        用户在绑定了某个使用计划到环境后，可使用本接口查询这个使用计划绑定的所有服务的环境。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsagePlanEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsagePlanEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsagePlanSecretIds(
            self,
            request: models.DescribeUsagePlanSecretIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeUsagePlanSecretIdsResponse:
        """
        本接口（DescribeUsagePlanSecretIds）用于查询使用计划绑定的密钥列表。
        在 API 网关中，一个使用计划可绑定多个密钥对，可使用本接口查询使用计划绑定的密钥列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsagePlanSecretIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsagePlanSecretIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsagePlansStatus(
            self,
            request: models.DescribeUsagePlansStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeUsagePlansStatusResponse:
        """
        本接口（DescribeUsagePlanStatus）用于查询使用计划的列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsagePlansStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsagePlansStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachPlugin(
            self,
            request: models.DetachPluginRequest,
            opts: Dict = None,
    ) -> models.DetachPluginResponse:
        """
        解除插件与API绑定
        """
        
        kwargs = {}
        kwargs["action"] = "DetachPlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachPluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableApiKey(
            self,
            request: models.DisableApiKeyRequest,
            opts: Dict = None,
    ) -> models.DisableApiKeyResponse:
        """
        本接口（DisableApiKey）用于禁用一对 API 密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableApiKey(
            self,
            request: models.EnableApiKeyRequest,
            opts: Dict = None,
    ) -> models.EnableApiKeyResponse:
        """
        本接口（EnableApiKey）用于启动一对被禁用的 API 密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportOpenApi(
            self,
            request: models.ImportOpenApiRequest,
            opts: Dict = None,
    ) -> models.ImportOpenApiResponse:
        """
        本接口（ImportOpenApi）用于将OpenAPI规范定义的API导入到API网关。
        """
        
        kwargs = {}
        kwargs["action"] = "ImportOpenApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportOpenApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAPIDoc(
            self,
            request: models.ModifyAPIDocRequest,
            opts: Dict = None,
    ) -> models.ModifyAPIDocResponse:
        """
        修改 API 文档
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAPIDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAPIDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApi(
            self,
            request: models.ModifyApiRequest,
            opts: Dict = None,
    ) -> models.ModifyApiResponse:
        """
        本接口（ModifyApi）用于修改 API 接口，可调用此接口对已经配置的 API 接口进行编辑修改。修改后的 API 需要重新发布 API 所在的服务到对应环境方能生效。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApi"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiApp(
            self,
            request: models.ModifyApiAppRequest,
            opts: Dict = None,
    ) -> models.ModifyApiAppResponse:
        """
        本接口（ModifyApiApp）用于修改已经创建的应用。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiEnvironmentStrategy(
            self,
            request: models.ModifyApiEnvironmentStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyApiEnvironmentStrategyResponse:
        """
        本接口（ModifyApiEnvironmentStrategy）用于修改API限流策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiEnvironmentStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiEnvironmentStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiIncrement(
            self,
            request: models.ModifyApiIncrementRequest,
            opts: Dict = None,
    ) -> models.ModifyApiIncrementResponse:
        """
        提供增量更新API能力，主要是给程序调用（区别于ModifyApi，该接口是需要传入API的全量参数，对console使用较友好）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiIncrement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiIncrementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExclusiveInstance(
            self,
            request: models.ModifyExclusiveInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyExclusiveInstanceResponse:
        """
        本接口（ModifyExclusiveInstance）用于修改独享实例信息。​
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExclusiveInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExclusiveInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIPStrategy(
            self,
            request: models.ModifyIPStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyIPStrategyResponse:
        """
        本接口（ModifyIPStrategy）用于修改服务IP策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPlugin(
            self,
            request: models.ModifyPluginRequest,
            opts: Dict = None,
    ) -> models.ModifyPluginResponse:
        """
        修改API网关插件。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyService(
            self,
            request: models.ModifyServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceResponse:
        """
        本接口（ModifyService）用于修改服务的相关信息。当服务创建后，服务的名称、描述和服务类型均可被修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceEnvironmentStrategy(
            self,
            request: models.ModifyServiceEnvironmentStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceEnvironmentStrategyResponse:
        """
        本接口（ModifyServiceEnvironmentStrategy）用于修改服务限流策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceEnvironmentStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceEnvironmentStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubDomain(
            self,
            request: models.ModifySubDomainRequest,
            opts: Dict = None,
    ) -> models.ModifySubDomainResponse:
        """
        本接口（ModifySubDomain）用于修改服务的自定义域名设置中的路径映射，可以修改绑定自定义域名之前的路径映射规则。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUpstream(
            self,
            request: models.ModifyUpstreamRequest,
            opts: Dict = None,
    ) -> models.ModifyUpstreamResponse:
        """
        修改后端通道
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUpstream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUpstreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUsagePlan(
            self,
            request: models.ModifyUsagePlanRequest,
            opts: Dict = None,
    ) -> models.ModifyUsagePlanResponse:
        """
        本接口（ModifyUsagePlan）用于修改使用计划的名称，描述及 QPS。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUsagePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUsagePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseService(
            self,
            request: models.ReleaseServiceRequest,
            opts: Dict = None,
    ) -> models.ReleaseServiceResponse:
        """
        本接口（ReleaseService）用于发布服务。
        API 网关的服务创建后，需要发布到某个环境方生效后，使用者才能进行调用，此接口用于发布服务到环境，如 release 环境。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAPIDocPassword(
            self,
            request: models.ResetAPIDocPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAPIDocPasswordResponse:
        """
        重置API文档密码
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAPIDocPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAPIDocPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindEnvironment(
            self,
            request: models.UnBindEnvironmentRequest,
            opts: Dict = None,
    ) -> models.UnBindEnvironmentResponse:
        """
        本接口（UnBindEnvironment）用于将使用计划从特定环境解绑。
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindIPStrategy(
            self,
            request: models.UnBindIPStrategyRequest,
            opts: Dict = None,
    ) -> models.UnBindIPStrategyResponse:
        """
        本接口（UnBindIPStrategy）用于服务解绑IP策略。
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindIPStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindIPStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindSecretIds(
            self,
            request: models.UnBindSecretIdsRequest,
            opts: Dict = None,
    ) -> models.UnBindSecretIdsResponse:
        """
        本接口（UnBindSecretIds）用于为使用计划解绑密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindSecretIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindSecretIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindSubDomain(
            self,
            request: models.UnBindSubDomainRequest,
            opts: Dict = None,
    ) -> models.UnBindSubDomainResponse:
        """
        本接口（UnBindSubDomain）用于解绑自定义域名。
        用户使用 API 网关绑定了自定义域名到服务中后，若想要解绑此自定义域名，可使用此接口。
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindSubDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindSubDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnReleaseService(
            self,
            request: models.UnReleaseServiceRequest,
            opts: Dict = None,
    ) -> models.UnReleaseServiceResponse:
        """
        本接口（UnReleaseService）用于下线服务。
        用户发布服务到某个环境后，此服务中的 API 方可被调用者进行调用，当用户需要将此服务从发布环境中下线时，可调用此 API。下线后的服务不可被调用。
        """
        
        kwargs = {}
        kwargs["action"] = "UnReleaseService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnReleaseServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindApiApp(
            self,
            request: models.UnbindApiAppRequest,
            opts: Dict = None,
    ) -> models.UnbindApiAppResponse:
        """
        本接口（UnbindApiApp）用于解除应用和API绑定。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindApiApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindApiAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateApiAppKey(
            self,
            request: models.UpdateApiAppKeyRequest,
            opts: Dict = None,
    ) -> models.UpdateApiAppKeyResponse:
        """
        本接口（UpdateApiAppKey）用于更新应用密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateApiAppKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateApiAppKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateApiKey(
            self,
            request: models.UpdateApiKeyRequest,
            opts: Dict = None,
    ) -> models.UpdateApiKeyResponse:
        """
        本接口（UpdateApiKey）用于更换用户已创建的一对 API 密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateService(
            self,
            request: models.UpdateServiceRequest,
            opts: Dict = None,
    ) -> models.UpdateServiceResponse:
        """
        本接口（UpdateService）用于从服务已发布的环境中将运行版本切换到特定版本。用户在使用 API 网关创建服务并发布服务到某个环境后，如在开发过程产生多个版本需要切换，此时可调用本接口。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)