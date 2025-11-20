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
from tencentcloud.cdc.v20201214 import models
from typing import Dict


class CdcClient(AbstractClient):
    _apiVersion = '2020-12-14'
    _endpoint = 'cdc.tencentcloudapi.com'
    _service = 'cdc'

    async def CreateDedicatedCluster(
            self,
            request: models.CreateDedicatedClusterRequest,
            opts: Dict = None,
    ) -> models.CreateDedicatedClusterResponse:
        """
        创建专用集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDedicatedCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDedicatedClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDedicatedClusterImageCache(
            self,
            request: models.CreateDedicatedClusterImageCacheRequest,
            opts: Dict = None,
    ) -> models.CreateDedicatedClusterImageCacheResponse:
        """
        创建云上镜像缓存到本地专用集群中
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDedicatedClusterImageCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDedicatedClusterImageCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDedicatedClusterOrder(
            self,
            request: models.CreateDedicatedClusterOrderRequest,
            opts: Dict = None,
    ) -> models.CreateDedicatedClusterOrderResponse:
        """
        创建专用集群订单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDedicatedClusterOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDedicatedClusterOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSite(
            self,
            request: models.CreateSiteRequest,
            opts: Dict = None,
    ) -> models.CreateSiteResponse:
        """
        创建站点
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSiteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDedicatedClusterImageCache(
            self,
            request: models.DeleteDedicatedClusterImageCacheRequest,
            opts: Dict = None,
    ) -> models.DeleteDedicatedClusterImageCacheResponse:
        """
        删除本地专用集群的云上镜像缓存
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDedicatedClusterImageCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDedicatedClusterImageCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDedicatedClusters(
            self,
            request: models.DeleteDedicatedClustersRequest,
            opts: Dict = None,
    ) -> models.DeleteDedicatedClustersResponse:
        """
        删除专用集群
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDedicatedClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDedicatedClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSites(
            self,
            request: models.DeleteSitesRequest,
            opts: Dict = None,
    ) -> models.DeleteSitesResponse:
        """
        删除站点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSitesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterCbsStatistics(
            self,
            request: models.DescribeDedicatedClusterCbsStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterCbsStatisticsResponse:
        """
        查询本地专用集群云硬盘仓库信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterCbsStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterCbsStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterCosCapacity(
            self,
            request: models.DescribeDedicatedClusterCosCapacityRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterCosCapacityResponse:
        """
        查询专用集群内cos的容量信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterCosCapacity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterCosCapacityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterHostStatistics(
            self,
            request: models.DescribeDedicatedClusterHostStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterHostStatisticsResponse:
        """
        查询专用集群内宿主机的统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterHostStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterHostStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterHosts(
            self,
            request: models.DescribeDedicatedClusterHostsRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterHostsResponse:
        """
        查询专用集群宿主机信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterInstanceTypes(
            self,
            request: models.DescribeDedicatedClusterInstanceTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterInstanceTypesResponse:
        """
        查询专用集群支持的实例规格列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterInstanceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterInstanceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterOrders(
            self,
            request: models.DescribeDedicatedClusterOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterOrdersResponse:
        """
        查询专用集群订单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterOverview(
            self,
            request: models.DescribeDedicatedClusterOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterOverviewResponse:
        """
        查询专用集群概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterTypes(
            self,
            request: models.DescribeDedicatedClusterTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterTypesResponse:
        """
        查询专有集群配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusters(
            self,
            request: models.DescribeDedicatedClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClustersResponse:
        """
        查询专用集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedSupportedZones(
            self,
            request: models.DescribeDedicatedSupportedZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedSupportedZonesResponse:
        """
        查询专用集群支持的可用区列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedSupportedZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedSupportedZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSites(
            self,
            request: models.DescribeSitesRequest,
            opts: Dict = None,
    ) -> models.DescribeSitesResponse:
        """
        查询站点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSitesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSitesDetail(
            self,
            request: models.DescribeSitesDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSitesDetailResponse:
        """
        查询站点详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSitesDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSitesDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDedicatedClusterInfo(
            self,
            request: models.ModifyDedicatedClusterInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDedicatedClusterInfoResponse:
        """
        修改本地专用集群信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDedicatedClusterInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDedicatedClusterInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOrderStatus(
            self,
            request: models.ModifyOrderStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyOrderStatusResponse:
        """
        修改大订单、小订单的状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOrderStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOrderStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySiteDeviceInfo(
            self,
            request: models.ModifySiteDeviceInfoRequest,
            opts: Dict = None,
    ) -> models.ModifySiteDeviceInfoResponse:
        """
        修改机房设备信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySiteDeviceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySiteDeviceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySiteInfo(
            self,
            request: models.ModifySiteInfoRequest,
            opts: Dict = None,
    ) -> models.ModifySiteInfoResponse:
        """
        修改机房信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySiteInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySiteInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)