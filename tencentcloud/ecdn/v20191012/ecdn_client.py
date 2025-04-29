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
from tencentcloud.ecdn.v20191012 import models


class EcdnClient(AbstractClient):
    _apiVersion = '2019-10-12'
    _endpoint = 'ecdn.tencentcloudapi.com'
    _service = 'ecdn'


    def DescribeDomains(self, request):
        """ECDN平台下线，接口开始预下线处理

        本接口（DescribeDomains）用于查询CDN域名基本信息，包括项目id，状态，业务类型，创建时间，更新时间等。

        >?  若您的业务已迁移至 CDN 控制台，请参考<a href="https://cloud.tencent.com/document/api/228/41118"> CDN 接口文档</a>，使用  CDN 相关API 进行操作。

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainsConfig(self, request):
        """ECDN平台下线，接口开始预下线处理

        本接口（DescribeDomainsConfig）用于查询CDN加速域名详细配置信息。

        >?  若您的业务已迁移至 CDN 控制台，请参考<a href="https://cloud.tencent.com/document/api/228/41117"> CDN 接口文档</a>，使用  CDN 相关API 进行操作。

        :param request: Request instance for DescribeDomainsConfig.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsConfigRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainsConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainsConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEcdnDomainLogs(self, request):
        """ECDN平台下线，接口开始预下线处理

        本接口（DescribeEcdnDomainLogs）用于查询域名的访问日志下载地址。

        :param request: Request instance for DescribeEcdnDomainLogs.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainLogsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEcdnDomainLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEcdnDomainLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEcdnDomainStatistics(self, request):
        """ECDN平台下线，接口开始预下线处理

        本接口（DescribeEcdnDomainStatistics）用于查询指定时间段内的域名访问统计指标。

        >?  若您的业务已迁移至 CDN 控制台，请参考<a href="https://cloud.tencent.com/document/api/228/30986"> CDN 接口文档</a>，使用  CDN 相关API 进行操作。

        :param request: Request instance for DescribeEcdnDomainStatistics.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainStatisticsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEcdnDomainStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEcdnDomainStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEcdnStatistics(self, request):
        """ECDN平台下线，接口开始预下线处理

        DescribeEcdnStatistics用于查询 ECDN 实时访问监控数据，支持以下指标查询：

        + 流量（单位为 byte）
        + 带宽（单位为 bps）
        + 请求数（单位为 次）
        + 状态码 2xx 汇总及各 2 开头状态码明细（单位为 个）
        + 状态码 3xx 汇总及各 3 开头状态码明细（单位为 个）
        + 状态码 4xx 汇总及各 4 开头状态码明细（单位为 个）
        + 状态码 5xx 汇总及各 5 开头状态码明细（单位为 个）

        :param request: Request instance for DescribeEcdnStatistics.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnStatisticsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEcdnStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEcdnStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpStatus(self, request):
        """ECDN平台下线，接口开始预下线处理

        DescribeIpStatus 用于查询域名所在加速平台的所有节点信息, 如果您的源站有白名单设置,可以通过本接口获取ECDN服务的节点IP进行加白, 本接口为内测接口,请联系腾讯云工程师开白。

        由于产品服务节点常有更新，对于源站开白的使用场景，请定期调用接口获取最新节点信息，若新增服务节点发布7日后您尚未更新加白导致回源失败等问题，ECDN侧不对此承担责任。

        :param request: Request instance for DescribeIpStatus.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeIpStatusRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeIpStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePurgeTasks(self, request):
        """ECDN即将下线，如需要动态加速请使用EdgeOne

        DescribePurgeTasks 用于查询刷新任务提交历史记录及执行进度。

        >?  若您的业务已迁移至 CDN 控制台，请参考<a href="https://cloud.tencent.com/document/api/228/37873"> CDN 接口文档</a>，使用  CDN 相关API 进行操作。

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurgeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePurgeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PurgeUrlsCache(self, request):
        """ECDN即将下线，如需要动态加速请使用EdgeOne

        PurgeUrlsCache 用于批量刷新Url，一次提交将返回一个刷新任务id。

        >?  若您的业务已迁移至 CDN 控制台，请参考<a href="https://cloud.tencent.com/document/api/228/37870"> CDN 接口文档</a>，使用  CDN 相关API 进行操作。

        :param request: Request instance for PurgeUrlsCache.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.PurgeUrlsCacheRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.PurgeUrlsCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PurgeUrlsCache", params, headers=headers)
            response = json.loads(body)
            model = models.PurgeUrlsCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))