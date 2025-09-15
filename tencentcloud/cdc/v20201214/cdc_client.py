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
from tencentcloud.cdc.v20201214 import models


class CdcClient(AbstractClient):
    _apiVersion = '2020-12-14'
    _endpoint = 'cdc.tencentcloudapi.com'
    _service = 'cdc'


    def CreateDedicatedCluster(self, request):
        r"""创建专用集群

        :param request: Request instance for CreateDedicatedCluster.
        :type request: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDedicatedCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDedicatedClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDedicatedClusterImageCache(self, request):
        r"""创建云上镜像缓存到本地专用集群中

        :param request: Request instance for CreateDedicatedClusterImageCache.
        :type request: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterImageCacheRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterImageCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDedicatedClusterImageCache", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDedicatedClusterImageCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDedicatedClusterOrder(self, request):
        r"""创建专用集群订单

        :param request: Request instance for CreateDedicatedClusterOrder.
        :type request: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterOrderRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDedicatedClusterOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDedicatedClusterOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSite(self, request):
        r"""创建站点

        :param request: Request instance for CreateSite.
        :type request: :class:`tencentcloud.cdc.v20201214.models.CreateSiteRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CreateSiteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSite", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSiteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDedicatedClusterImageCache(self, request):
        r"""删除本地专用集群的云上镜像缓存

        :param request: Request instance for DeleteDedicatedClusterImageCache.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DeleteDedicatedClusterImageCacheRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DeleteDedicatedClusterImageCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDedicatedClusterImageCache", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDedicatedClusterImageCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDedicatedClusters(self, request):
        r"""删除专用集群

        :param request: Request instance for DeleteDedicatedClusters.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DeleteDedicatedClustersRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DeleteDedicatedClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDedicatedClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDedicatedClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSites(self, request):
        r"""删除站点

        :param request: Request instance for DeleteSites.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DeleteSitesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DeleteSitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSites", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSitesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterCbsStatistics(self, request):
        r"""查询本地专用集群云硬盘仓库信息

        :param request: Request instance for DescribeDedicatedClusterCbsStatistics.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterCbsStatisticsRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterCbsStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterCbsStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterCbsStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterCosCapacity(self, request):
        r"""查询专用集群内cos的容量信息

        :param request: Request instance for DescribeDedicatedClusterCosCapacity.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterCosCapacityRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterCosCapacityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterCosCapacity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterCosCapacityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterHostStatistics(self, request):
        r"""查询专用集群内宿主机的统计信息

        :param request: Request instance for DescribeDedicatedClusterHostStatistics.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostStatisticsRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterHostStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterHostStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterHosts(self, request):
        r"""查询专用集群宿主机信息

        :param request: Request instance for DescribeDedicatedClusterHosts.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostsRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterHosts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterInstanceTypes(self, request):
        r"""查询专用集群支持的实例规格列表

        :param request: Request instance for DescribeDedicatedClusterInstanceTypes.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterInstanceTypesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterInstanceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterInstanceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterOrders(self, request):
        r"""查询专用集群订单列表

        :param request: Request instance for DescribeDedicatedClusterOrders.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOrdersRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOrdersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterOrders", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterOrdersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterOverview(self, request):
        r"""查询专用集群概览信息

        :param request: Request instance for DescribeDedicatedClusterOverview.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOverviewRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterTypes(self, request):
        r"""查询专有集群配置列表

        :param request: Request instance for DescribeDedicatedClusterTypes.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterTypesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusters(self, request):
        r"""查询专用集群列表

        :param request: Request instance for DescribeDedicatedClusters.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClustersRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedSupportedZones(self, request):
        r"""查询专用集群支持的可用区列表

        :param request: Request instance for DescribeDedicatedSupportedZones.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedSupportedZonesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedSupportedZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedSupportedZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedSupportedZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSites(self, request):
        r"""查询站点列表

        :param request: Request instance for DescribeSites.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSites", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSitesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSitesDetail(self, request):
        r"""查询站点详情

        :param request: Request instance for DescribeSitesDetail.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesDetailRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSitesDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSitesDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDedicatedClusterInfo(self, request):
        r"""修改本地专用集群信息

        :param request: Request instance for ModifyDedicatedClusterInfo.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifyDedicatedClusterInfoRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifyDedicatedClusterInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDedicatedClusterInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDedicatedClusterInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOrderStatus(self, request):
        r"""修改大订单、小订单的状态

        :param request: Request instance for ModifyOrderStatus.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifyOrderStatusRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifyOrderStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOrderStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOrderStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySiteDeviceInfo(self, request):
        r"""修改机房设备信息

        :param request: Request instance for ModifySiteDeviceInfo.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifySiteDeviceInfoRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifySiteDeviceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySiteDeviceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySiteDeviceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySiteInfo(self, request):
        r"""修改机房信息

        :param request: Request instance for ModifySiteInfo.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifySiteInfoRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifySiteInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySiteInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySiteInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))