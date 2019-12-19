# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.cdn.v20180606 import models


class CdnClient(AbstractClient):
    _apiVersion = '2018-06-06'
    _endpoint = 'cdn.tencentcloudapi.com'


    def DescribeCdnData(self, request):
        """DescribeCdnData 用于查询 CDN 实时访问监控数据，支持以下指标查询：

        + 流量（单位为 byte）
        + 带宽（单位为 bps）
        + 请求数（单位为 次）
        + 流量命中率（单位为 %，小数点后保留两位）
        + 状态码 2xx 汇总及各 2 开头状态码明细（单位为 个）
        + 状态码 3xx 汇总及各 3 开头状态码明细（单位为 个）
        + 状态码 4xx 汇总及各 4 开头状态码明细（单位为 个）
        + 状态码 5xx 汇总及各 5 开头状态码明细（单位为 个）

        :param request: Request instance for DescribeCdnData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCdnData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCdnDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCdnDomainLogs(self, request):
        """DescribeCdnDomainLogs 用于查询访问日志下载地址，仅支持 30 天以内的境内、境外访问日志下载链接查询。

        :param request: Request instance for DescribeCdnDomainLogs.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDomainLogsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDomainLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCdnDomainLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCdnDomainLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCdnIp(self, request):
        """DescribeCdnIp 用于查询 CDN IP 归属。

        :param request: Request instance for DescribeCdnIp.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnIpRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCdnIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCdnIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIpVisit(self, request):
        """DescribeIpVisit 用于查询 5 分钟活跃用户数，及日活跃用户数明细

        + 5 分钟活跃用户数：根据日志中客户端 IP，5 分钟粒度去重统计
        + 日活跃用户数：根据日志中客户端 IP，按天粒度去重统计

        :param request: Request instance for DescribeIpVisit.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeIpVisitRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeIpVisitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpVisit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpVisitResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMapInfo(self, request):
        """DescribeMapInfo 用于查询省份对应的 ID，运营商对应的 ID 信息。

        :param request: Request instance for DescribeMapInfo.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeMapInfoRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeMapInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMapInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMapInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOriginData(self, request):
        """DescribeOriginData 用于查询 CDN 实时回源监控数据，支持以下指标查询：

        + 回源流量（单位为 byte）
        + 回源带宽（单位为 bps）
        + 回源请求数（单位为 次）
        + 回源失败请求数（单位为 次）
        + 回源失败率（单位为 %，小数点后保留两位）
        + 回源状态码 2xx 汇总及各 2 开头回源状态码明细（单位为 个）
        + 回源状态码 3xx 汇总及各 3 开头回源状态码明细（单位为 个）
        + 回源状态码 4xx 汇总及各 4 开头回源状态码明细（单位为 个）
        + 回源状态码 5xx 汇总及各 5 开头回源状态码明细（单位为 个）

        :param request: Request instance for DescribeOriginData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeOriginDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeOriginDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOriginData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOriginDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePayType(self, request):
        """DescribePayType 用于查询用户的计费类型，计费周期等信息。

        :param request: Request instance for DescribePayType.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePayTypeRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePayTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePayType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePayTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePurgeTasks(self, request):
        """DescribePurgeTasks 用于查询提交的 URL 刷新、目录刷新记录及执行进度，通过 PurgePathCache 与 PurgeUrlsCache 接口提交的任务均可通过此接口进行查询。

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePurgeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurgeTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePushTasks(self, request):
        """DescribePushTasks  用于查询预热任务提交历史记录及执行进度。
        接口灰度中，暂未全量开放，敬请期待。

        :param request: Request instance for DescribePushTasks.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePushTasksRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePushTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePushTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePushTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTrafficPackages(self, request):
        """DescribeTrafficPackages 用于查询境内 CDN 流量包详情。

        :param request: Request instance for DescribeTrafficPackages.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrafficPackages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrafficPackagesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableCaches(self, request):
        """DisableCaches 用于禁用 CDN 上指定 URL 的访问，禁用完成后，全网访问会直接返回 403。（接口尚在内测中，暂未全量开放使用）

        :param request: Request instance for DisableCaches.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DisableCachesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DisableCachesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableCaches", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableCachesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableCaches(self, request):
        """EnableCaches 用于解禁手工封禁的 URL，解禁成功后，全网生效时间约 5~10 分钟。（接口尚在内测中，暂未全量开放使用）

        :param request: Request instance for EnableCaches.
        :type request: :class:`tencentcloud.cdn.v20180606.models.EnableCachesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.EnableCachesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableCaches", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableCachesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDisableRecords(self, request):
        """GetDisableRecords 用户查询资源禁用历史，及 URL 当前状态。（接口尚在内测中，暂未全量开放使用）

        :param request: Request instance for GetDisableRecords.
        :type request: :class:`tencentcloud.cdn.v20180606.models.GetDisableRecordsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.GetDisableRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDisableRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDisableRecordsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListTopData(self, request):
        """ListTopData 通过入参 Metric 和 Filter 组合不同，可以查询以下排序数据：

        + 依据总流量、总请求数对访问 URL 排序，从大至小返回 TOP 1000 URL
        + 依据总流量、总请求数对客户端省份排序，从大至小返回省份列表
        + 依据总流量、总请求数对客户端运营商排序，从大至小返回运营商列表
        + 依据总流量、峰值带宽、总请求数、平均命中率、2XX/3XX/4XX/5XX 状态码对域名排序，从大至小返回域名列表
        + 依据总回源流量、回源峰值带宽、总回源请求数、平均回源失败率、2XX/3XX/4XX/5XX 回源状态码对域名排序，从大至小返回域名列表

        :param request: Request instance for ListTopData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListTopDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListTopDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListTopData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTopDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PurgePathCache(self, request):
        """PurgePathCache 用于批量提交目录刷新，根据域名的加速区域进行对应区域的刷新。
        默认情况下境内、境外加速区域每日目录刷新额度为各 100 条，每次最多可提交 20 条。

        :param request: Request instance for PurgePathCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PurgePathCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PurgePathCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PurgePathCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PurgePathCacheResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PurgeUrlsCache(self, request):
        """PurgeUrlsCache 用于批量提交 URL 进行刷新，根据 URL 中域名的当前加速区域进行对应区域的刷新。
        默认情况下境内、境外加速区域每日 URL 刷新额度各为 10000 条，每次最多可提交 1000 条。

        :param request: Request instance for PurgeUrlsCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PurgeUrlsCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PurgeUrlsCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PurgeUrlsCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PurgeUrlsCacheResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PushUrlsCache(self, request):
        """PushUrlsCache 用于将指定 URL 资源列表加载至 CDN 节点，支持指定加速区域预热。
        默认情况下境内、境外每日预热 URL 限额为各 1000 条，每次最多可提交 20 条。
        接口灰度中，暂未全量开放，敬请期待。

        :param request: Request instance for PushUrlsCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PushUrlsCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PushUrlsCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PushUrlsCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PushUrlsCacheResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)