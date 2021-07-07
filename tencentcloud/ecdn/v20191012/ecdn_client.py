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


    def AddEcdnDomain(self, request):
        """本接口（AddEcdnDomain）用于创建加速域名。

        :param request: Request instance for AddEcdnDomain.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.AddEcdnDomainRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.AddEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEcdnDomainResponse()
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


    def CreateVerifyRecord(self, request):
        """生成一条子域名解析，提示客户添加到域名解析上，用于泛域名及域名取回校验归属权

        :param request: Request instance for CreateVerifyRecord.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.CreateVerifyRecordRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.CreateVerifyRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVerifyRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVerifyRecordResponse()
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


    def DeleteEcdnDomain(self, request):
        """本接口（DeleteEcdnDomain）用于删除指定加速域名。待删除域名必须处于已停用状态。

        :param request: Request instance for DeleteEcdnDomain.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DeleteEcdnDomainRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DeleteEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEcdnDomainResponse()
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


    def DescribeDomains(self, request):
        """本接口（DescribeDomains）用于查询CDN域名基本信息，包括项目id，状态，业务类型，创建时间，更新时间等。

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainsResponse()
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


    def DescribeDomainsConfig(self, request):
        """本接口（DescribeDomainsConfig）用于查询CDN加速域名详细配置信息。

        :param request: Request instance for DescribeDomainsConfig.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsConfigRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeDomainsConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainsConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainsConfigResponse()
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


    def DescribeEcdnDomainLogs(self, request):
        """本接口（DescribeEcdnDomainLogs）用于查询域名的访问日志下载地址。

        :param request: Request instance for DescribeEcdnDomainLogs.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainLogsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEcdnDomainLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEcdnDomainLogsResponse()
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


    def DescribeEcdnDomainStatistics(self, request):
        """本接口（DescribeEcdnDomainStatistics）用于查询指定时间段内的域名访问统计指标

        :param request: Request instance for DescribeEcdnDomainStatistics.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainStatisticsRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeEcdnDomainStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEcdnDomainStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEcdnDomainStatisticsResponse()
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


    def DescribeEcdnStatistics(self, request):
        """DescribeEcdnStatistics用于查询 ECDN 实时访问监控数据，支持以下指标查询：

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
            body = self.call("DescribeEcdnStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEcdnStatisticsResponse()
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


    def DescribeIpStatus(self, request):
        """DescribeIpStatus 用于查询域名所在加速平台的所有节点信息, 如果您的源站有白名单设置,可以通过本接口获取ECDN服务的节点IP进行加白, 本接口为内测接口,请联系腾讯云工程师开白。

        由于产品服务节点常有更新，对于源站开白的使用场景，请定期调用接口获取最新节点信息，若新增服务节点发布7日后您尚未更新加白导致回源失败等问题，ECDN侧不对此承担责任。

        :param request: Request instance for DescribeIpStatus.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribeIpStatusRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribeIpStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpStatusResponse()
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


    def DescribePurgeQuota(self, request):
        """查询刷新接口的用量配额。

        :param request: Request instance for DescribePurgeQuota.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribePurgeQuotaRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribePurgeQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePurgeQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurgeQuotaResponse()
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
        """DescribePurgeTasks 用于查询刷新任务提交历史记录及执行进度。

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.DescribePurgeTasksResponse`

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


    def PurgePathCache(self, request):
        """PurgePathCache 用于批量刷新目录缓存，一次提交将返回一个刷新任务id。

        :param request: Request instance for PurgePathCache.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.PurgePathCacheRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.PurgePathCacheResponse`

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
        """PurgeUrlsCache 用于批量刷新Url，一次提交将返回一个刷新任务id。

        :param request: Request instance for PurgeUrlsCache.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.PurgeUrlsCacheRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.PurgeUrlsCacheResponse`

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


    def StartEcdnDomain(self, request):
        """本接口（StartEcdnDomain）用于启用加速域名，待启用域名必须处于已下线状态。

        :param request: Request instance for StartEcdnDomain.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.StartEcdnDomainRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.StartEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartEcdnDomainResponse()
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


    def StopEcdnDomain(self, request):
        """本接口（StopCdnDomain）用于停止加速域名，待停用加速域名必须处于已上线或部署中状态。

        :param request: Request instance for StopEcdnDomain.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.StopEcdnDomainRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.StopEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopEcdnDomainResponse()
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


    def UpdateDomainConfig(self, request):
        """本接口（UpdateDomainConfig）用于更新ECDN加速域名配置信息。
        注意：如果需要更新复杂类型的配置项，必须传递整个对象的所有属性，未传递的属性将使用默认值。建议通过查询接口获取配置属性后，直接修改后传递给本接口。Https配置由于证书的特殊性，更新时不用传递证书和密钥字段。

        :param request: Request instance for UpdateDomainConfig.
        :type request: :class:`tencentcloud.ecdn.v20191012.models.UpdateDomainConfigRequest`
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.UpdateDomainConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDomainConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDomainConfigResponse()
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