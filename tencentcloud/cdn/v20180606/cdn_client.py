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
from tencentcloud.cdn.v20180606 import models


class CdnClient(AbstractClient):
    _apiVersion = '2018-06-06'
    _endpoint = 'cdn.tencentcloudapi.com'
    _service = 'cdn'


    def AddCdnDomain(self, request):
        """AddCdnDomain 用于新增内容分发网络加速域名。

        :param request: Request instance for AddCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.AddCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AddCdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddCdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddCdnDomainResponse()
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


    def CreateClsLogTopic(self, request):
        """CreateClsLogTopic 用于创建日志主题。注意：一个日志集下至多可创建10个日志主题。

        :param request: Request instance for CreateClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClsLogTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClsLogTopicResponse()
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


    def CreateDiagnoseUrl(self, request):
        """CreateDiagnoseUrl 用于添加域名诊断任务URL

        :param request: Request instance for CreateDiagnoseUrl.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateDiagnoseUrlRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateDiagnoseUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDiagnoseUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDiagnoseUrlResponse()
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


    def CreateEdgePackTask(self, request):
        """动态打包任务提交接口

        :param request: Request instance for CreateEdgePackTask.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateEdgePackTaskRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateEdgePackTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEdgePackTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEdgePackTaskResponse()
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


    def CreateScdnDomain(self, request):
        """CreateScdnDomain 用于创建 SCDN 加速域名

        :param request: Request instance for CreateScdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateScdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateScdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScdnDomainResponse()
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


    def CreateScdnFailedLogTask(self, request):
        """CreateScdnFailedLogTask 用于重试创建失败的事件日志任务

        :param request: Request instance for CreateScdnFailedLogTask.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateScdnFailedLogTaskRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateScdnFailedLogTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScdnFailedLogTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScdnFailedLogTaskResponse()
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


    def CreateScdnLogTask(self, request):
        """CreateScdnLogTask 用于创建事件日志任务

        :param request: Request instance for CreateScdnLogTask.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateScdnLogTaskRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateScdnLogTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScdnLogTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScdnLogTaskResponse()
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
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateVerifyRecordRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateVerifyRecordResponse`

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


    def DeleteCdnDomain(self, request):
        """DeleteCdnDomain 用于删除指定加速域名

        :param request: Request instance for DeleteCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DeleteCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DeleteCdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCdnDomainResponse()
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


    def DeleteClsLogTopic(self, request):
        """DeleteClsLogTopic 用于删除日志主题。注意：删除后，所有该日志主题下绑定域名的日志将不再继续投递至该主题，已经投递的日志将会被全部清空。生效时间约为 5~15 分钟。

        :param request: Request instance for DeleteClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DeleteClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DeleteClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteClsLogTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClsLogTopicResponse()
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


    def DeleteScdnDomain(self, request):
        """删除SCDN域名

        :param request: Request instance for DeleteScdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DeleteScdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DeleteScdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScdnDomainResponse()
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


    def DescribeBillingData(self, request):
        """DescribeBillingData 用于查询实际计费数据明细。

        :param request: Request instance for DescribeBillingData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeBillingDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeBillingDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillingData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillingDataResponse()
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


    def DescribeCdnData(self, request):
        """DescribeCdnData 用于查询 CDN 实时访问监控数据，支持以下指标查询：

        + 流量（单位为 byte）
        + 带宽（单位为 bps）
        + 请求数（单位为 次）
        + 命中请求数（单位为 次）
        + 请求命中率（单位为 %）
        + 命中流量（单位为 byte）
        + 流量命中率（单位为 %）
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
        （注意：此接口请求频率限制以 CDN 侧限制为准：200次/10分钟）

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


    def DescribeCdnOriginIp(self, request):
        """本接口（DescribeCdnOriginIp）用于查询 CDN 回源节点的IP信息。（注：此接口即将下线，不再进行维护，请通过DescribeIpStatus 接口进行查询）

        :param request: Request instance for DescribeCdnOriginIp.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnOriginIpRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnOriginIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCdnOriginIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCdnOriginIpResponse()
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


    def DescribeCertDomains(self, request):
        """DescribeCertDomains 用于校验SSL证书并提取证书中包含的域名。

        :param request: Request instance for DescribeCertDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCertDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCertDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertDomainsResponse()
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


    def DescribeDiagnoseReport(self, request):
        """DescribeDiagnoseReport 用于获取指定报告id的内容

        :param request: Request instance for DescribeDiagnoseReport.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeDiagnoseReportRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeDiagnoseReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDiagnoseReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDiagnoseReportResponse()
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


    def DescribeDistrictIspData(self, request):
        """查询指定域名的区域、运营商明细数据
        注意事项：接口尚未全量开放，未在内测名单中的账号不支持调用

        :param request: Request instance for DescribeDistrictIspData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeDistrictIspDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeDistrictIspDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDistrictIspData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDistrictIspDataResponse()
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
        """DescribeDomains 用于查询内容分发网络加速域名（含境内、境外）基本配置信息，包括项目ID、服务状态，业务类型、创建时间、更新时间等信息。

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsResponse`

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
        """DescribeDomainsConfig 用于查询内容分发网络加速域名（含境内、境外）的所有配置信息。

        :param request: Request instance for DescribeDomainsConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsConfigResponse`

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


    def DescribeImageConfig(self, request):
        """DescribeImageConfig 用于获取域名图片优化的当前配置，支持Webp、TPG 和 Guetzli。

        :param request: Request instance for DescribeImageConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeImageConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeImageConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageConfigResponse()
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
        """DescribeIpStatus 用于查询域名所在加速平台的边缘节点、回源节点明细。注意事项：边缘节点（edge）尚未全量开放，未在内测名单中的账号不支持调用

        :param request: Request instance for DescribeIpStatus.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeIpStatusRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeIpStatusResponse`

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


    def DescribePurgeQuota(self, request):
        """DescribePurgeQuota 用于查询账户刷新配额和每日可用量。

        :param request: Request instance for DescribePurgeQuota.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeQuotaRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeQuotaResponse`

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


    def DescribePushQuota(self, request):
        """DescribePushQuota  用于查询预热配额和每日可用量。

        :param request: Request instance for DescribePushQuota.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePushQuotaRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePushQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePushQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePushQuotaResponse()
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


    def DescribeReportData(self, request):
        """DescribeReportData 用于查询域名/项目维度的日/周/月报表数据。

        :param request: Request instance for DescribeReportData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeReportDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeReportDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReportData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReportDataResponse()
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


    def DescribeScdnConfig(self, request):
        """DescribeScdnConfig 用于查询指定 SCDN 加速域名的安全相关配置

        :param request: Request instance for DescribeScdnConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeScdnConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeScdnConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScdnConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScdnConfigResponse()
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


    def DescribeScdnIpStrategy(self, request):
        """查询在SCDN IP安全策略

        :param request: Request instance for DescribeScdnIpStrategy.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeScdnIpStrategyRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeScdnIpStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScdnIpStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScdnIpStrategyResponse()
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


    def DescribeScdnTopData(self, request):
        """获取SCDN的Top数据

        :param request: Request instance for DescribeScdnTopData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeScdnTopDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeScdnTopDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScdnTopData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScdnTopDataResponse()
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
        """DescribeTrafficPackages 用于查询中国境内 CDN 流量包详情。

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


    def DescribeUrlViolations(self, request):
        """DescribeUrlViolations 用于查询被 CDN 系统扫描到的域名违规 URL 列表及当前状态。
        对应内容分发网络控制台【图片鉴黄】页面。

        :param request: Request instance for DescribeUrlViolations.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeUrlViolationsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeUrlViolationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUrlViolations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUrlViolationsResponse()
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
        """DisableCaches 用于禁用 CDN 上指定 URL 的访问，禁用完成后，中国境内访问会直接返回 403。（注：接口尚在内测中，暂未全量开放；封禁URL并非无限期永久封禁）

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


    def DisableClsLogTopic(self, request):
        """DisableClsLogTopic 用于停止日志主题投递。注意：停止后，所有绑定该日志主题域名的日志将不再继续投递至该主题，已经投递的日志将会继续保留。生效时间约为 5~15 分钟。

        :param request: Request instance for DisableClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DisableClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DisableClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableClsLogTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableClsLogTopicResponse()
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


    def DuplicateDomainConfig(self, request):
        """拷贝参考域名的配置至新域名。暂不支持自有证书以及定制化配置

        :param request: Request instance for DuplicateDomainConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DuplicateDomainConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DuplicateDomainConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DuplicateDomainConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DuplicateDomainConfigResponse()
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


    def EnableClsLogTopic(self, request):
        """EnableClsLogTopic 用于启动日志主题投递。注意：启动后，所有绑定该日志主题域名的日志将继续投递至该主题。生效时间约为 5~15 分钟。

        :param request: Request instance for EnableClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.EnableClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.EnableClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableClsLogTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableClsLogTopicResponse()
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
        """GetDisableRecords 用于查询资源禁用历史，及 URL 当前状态。（接口尚在内测中，暂未全量开放使用）

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


    def ListClsLogTopics(self, request):
        """ListClsLogTopics 用于显示日志主题列表。注意：一个日志集下至多含10个日志主题。

        :param request: Request instance for ListClsLogTopics.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListClsLogTopicsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListClsLogTopicsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListClsLogTopics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListClsLogTopicsResponse()
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


    def ListClsTopicDomains(self, request):
        """ListClsTopicDomains 用于获取某日志主题下绑定的域名列表。

        :param request: Request instance for ListClsTopicDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListClsTopicDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListClsTopicDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListClsTopicDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListClsTopicDomainsResponse()
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


    def ListDiagnoseReport(self, request):
        """ListDiagnoseReport 用于获取用户诊断URL访问后各个子任务的简要详情。

        :param request: Request instance for ListDiagnoseReport.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListDiagnoseReportRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListDiagnoseReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListDiagnoseReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListDiagnoseReportResponse()
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


    def ListScdnDomains(self, request):
        """ListScdnDomains 用于查询 SCDN 安全加速域名列表，及域名基本配置信息

        :param request: Request instance for ListScdnDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListScdnDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListScdnDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListScdnDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListScdnDomainsResponse()
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


    def ListScdnLogTasks(self, request):
        """ListScdnLogTasks 用于查询SCDN日志下载任务列表,以及展示下载任务基本信息

        :param request: Request instance for ListScdnLogTasks.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListScdnLogTasksRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListScdnLogTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListScdnLogTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListScdnLogTasksResponse()
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


    def ListTopBotData(self, request):
        """获取Bot攻击的Top信息

        :param request: Request instance for ListTopBotData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListTopBotDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListTopBotDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListTopBotData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTopBotDataResponse()
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


    def ListTopCcData(self, request):
        """获取CC攻击Top数据

        :param request: Request instance for ListTopCcData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListTopCcDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListTopCcDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListTopCcData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTopCcDataResponse()
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


    def ListTopDDoSData(self, request):
        """获取DDoS攻击Top数据

        :param request: Request instance for ListTopDDoSData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListTopDDoSDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListTopDDoSDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListTopDDoSData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTopDDoSDataResponse()
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

        注意：仅支持 90 天内数据查询

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


    def ListTopWafData(self, request):
        """获取Waf攻击Top数据

        :param request: Request instance for ListTopWafData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListTopWafDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListTopWafDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListTopWafData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTopWafDataResponse()
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


    def ManageClsTopicDomains(self, request):
        """ManageClsTopicDomains 用于管理某日志主题下绑定的域名列表。

        :param request: Request instance for ManageClsTopicDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ManageClsTopicDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ManageClsTopicDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManageClsTopicDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManageClsTopicDomainsResponse()
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


    def ModifyPurgeFetchTaskStatus(self, request):
        """ModifyPurgeFetchTaskStatus 用于上报定时刷新预热任务执行状态

        :param request: Request instance for ModifyPurgeFetchTaskStatus.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ModifyPurgeFetchTaskStatusRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ModifyPurgeFetchTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPurgeFetchTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPurgeFetchTaskStatusResponse()
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
        默认情况下境内、境外每日预热 URL 限额为各 1000 条，每次最多可提交 20 条。注意：中国境外区域预热，资源默认加载至中国境外边缘节点，所产生的边缘层流量会计入计费流量。

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


    def SearchClsLog(self, request):
        """SearchClsLog 用于 CLS 日志检索。支持检索今天，24小时（可选近7中的某一天），近7天的日志数据。

        :param request: Request instance for SearchClsLog.
        :type request: :class:`tencentcloud.cdn.v20180606.models.SearchClsLogRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.SearchClsLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchClsLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchClsLogResponse()
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


    def StartCdnDomain(self, request):
        """StartCdnDomain 用于启用已停用域名的加速服务

        :param request: Request instance for StartCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.StartCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StartCdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartCdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartCdnDomainResponse()
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


    def StartScdnDomain(self, request):
        """StartScdnDomain 用于开启域名的安全防护配置

        :param request: Request instance for StartScdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.StartScdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StartScdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartScdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartScdnDomainResponse()
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


    def StopCdnDomain(self, request):
        """StopCdnDomain 用于停止域名的加速服务。
        注意：停止加速服务后，访问至加速节点的请求将会直接返回 404。为避免对您的业务造成影响，请在停止加速服务前将解析切走。

        :param request: Request instance for StopCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.StopCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StopCdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopCdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopCdnDomainResponse()
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


    def StopScdnDomain(self, request):
        """StopScdnDomain 用于关闭域名的安全防护配置

        :param request: Request instance for StopScdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.StopScdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StopScdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopScdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopScdnDomainResponse()
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
        """UpdateDomainConfig 用于修改内容分发网络加速域名配置信息
        注意：如果需要更新复杂类型的配置项，必须传递整个对象的所有属性，未传递的属性将使用默认值，建议通过查询接口获取配置属性后，直接修改后传递给本接口。Https配置由于证书的特殊性，更新时不用传递证书和密钥字段。

        :param request: Request instance for UpdateDomainConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.UpdateDomainConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UpdateDomainConfigResponse`

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


    def UpdateImageConfig(self, request):
        """UpdateImageConfig 用于更新控制台图片优化的相关配置，支持Webp、TPG 和 Guetzli。

        :param request: Request instance for UpdateImageConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.UpdateImageConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UpdateImageConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateImageConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateImageConfigResponse()
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


    def UpdatePayType(self, request):
        """本接口(UpdatePayType)用于修改账号计费类型，暂不支持月结用户或子账号修改。

        :param request: Request instance for UpdatePayType.
        :type request: :class:`tencentcloud.cdn.v20180606.models.UpdatePayTypeRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UpdatePayTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdatePayType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePayTypeResponse()
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


    def UpdateScdnDomain(self, request):
        """UpdateScdnDomain 用于修改 SCDN 加速域名安全相关配置

        :param request: Request instance for UpdateScdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.UpdateScdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UpdateScdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateScdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateScdnDomainResponse()
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


    def VerifyDomainRecord(self, request):
        """验证域名解析值

        :param request: Request instance for VerifyDomainRecord.
        :type request: :class:`tencentcloud.cdn.v20180606.models.VerifyDomainRecordRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.VerifyDomainRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyDomainRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyDomainRecordResponse()
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