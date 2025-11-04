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
from tencentcloud.cdn.v20180606 import models


class CdnClient(AbstractClient):
    _apiVersion = '2018-06-06'
    _endpoint = 'cdn.tencentcloudapi.com'
    _service = 'cdn'


    def AddCLSTopicDomains(self, request):
        r"""AddCLSTopicDomains 用于新增域名到某日志主题下

        :param request: Request instance for AddCLSTopicDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.AddCLSTopicDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AddCLSTopicDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCLSTopicDomains", params, headers=headers)
            response = json.loads(body)
            model = models.AddCLSTopicDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCdnDomain(self, request):
        r"""AddCdnDomain 用于新增内容分发网络加速域名。1分钟内最多可新增100个域名。

        :param request: Request instance for AddCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.AddCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AddCdnDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCdnDomain", params, headers=headers)
            response = json.loads(body)
            model = models.AddCdnDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClsLogTopic(self, request):
        r"""CreateClsLogTopic 用于创建日志主题。注意：一个日志集下至多可创建10个日志主题。

        :param request: Request instance for CreateClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClsLogTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClsLogTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDiagnoseUrl(self, request):
        r"""以上诊断报告, 域名版本管理相关接口功能均废弃,  已确认现网0调用, 申请预下线,(预下线不会影响调用, 只会在接口中添加提示信息, 正式下线仍需人工确认)

        ### <font color=red>**该接口已废弃** </font><br>
        CreateDiagnoseUrl 用于添加域名诊断任务URL。

        :param request: Request instance for CreateDiagnoseUrl.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateDiagnoseUrlRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateDiagnoseUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDiagnoseUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDiagnoseUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgePackTask(self, request):
        r"""动态打包任务提交接口

        :param request: Request instance for CreateEdgePackTask.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateEdgePackTaskRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateEdgePackTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgePackTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgePackTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVerifyRecord(self, request):
        r"""CreateVerifyRecord 用于生成一条子域名解析，提示客户添加到域名解析上，用于泛域名及域名取回校验归属权。
        生成的解析记录可通过 [VerifyDomainRecord](https://cloud.tencent.com/document/product/228/48117) 完成归属权校验。
        注意：生成的解析记录有效期为24小时，超过24小时后，需重新生成。
        具体流程可参考：[使用API接口进行域名归属校验](https://cloud.tencent.com/document/product/228/61702#.E6.96.B9.E6.B3.95.E4.B8.89.EF.BC.9Aapi-.E6.8E.A5.E5.8F.A3.E6.93.8D.E4.BD.9C)

        :param request: Request instance for CreateVerifyRecord.
        :type request: :class:`tencentcloud.cdn.v20180606.models.CreateVerifyRecordRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CreateVerifyRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVerifyRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVerifyRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCdnDomain(self, request):
        r"""DeleteCdnDomain 用于删除指定加速域名

        :param request: Request instance for DeleteCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DeleteCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DeleteCdnDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCdnDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCdnDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClsLogTopic(self, request):
        r"""DeleteClsLogTopic 用于删除日志主题。注意：删除后，所有该日志主题下绑定域名的日志将不再继续投递至该主题，已经投递的日志将会被全部清空。生效时间约为 5~15 分钟。

        :param request: Request instance for DeleteClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DeleteClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DeleteClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClsLogTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClsLogTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingData(self, request):
        r"""DescribeBillingData 用于查询实际计费数据明细。
        注意:
        受计费算法的影响，计费数据接口返回的数据均存在一定延时。小时结算客户预计延时3-5小时。月结算客户预计延迟4-28小时，在凌晨4点（不含4点）之前，仅能查询到前2天数据，4点（含）之后，能查询到前1天数据。若您对数据及时性较强的诉求，建议使用[监控访问数据](https://cloud.tencent.com/document/product/228/30986)。

        :param request: Request instance for DescribeBillingData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeBillingDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeBillingDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdnData(self, request):
        r"""DescribeCdnData 用于查询 CDN 实时访问监控数据，支持以下指标查询：

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
            headers = request.headers
            body = self.call("DescribeCdnData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdnDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdnDomainLogs(self, request):
        r"""DescribeCdnDomainLogs 用于查询访问日志下载地址，仅支持 30 天以内的境内、境外访问日志下载链接查询。

        :param request: Request instance for DescribeCdnDomainLogs.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDomainLogsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDomainLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdnDomainLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdnDomainLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdnIp(self, request):
        r"""DescribeCdnIp 用于查询 CDN IP 归属。
        （注意：此接口请求频率限制以 CDN 侧限制为准：200次/10分钟）

        :param request: Request instance for DescribeCdnIp.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnIpRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdnIp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdnIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdnOriginIp(self, request):
        r"""### <font color=red>**该接口已废弃** </font><br>
        本接口（DescribeCdnOriginIp）用于查询 CDN 回源节点的IP信息。（注：替换接口为DescribeIpStatus）

        :param request: Request instance for DescribeCdnOriginIp.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnOriginIpRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnOriginIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdnOriginIp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdnOriginIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertDomains(self, request):
        r"""DescribeCertDomains 用于校验SSL证书并提取证书中包含的域名。

        :param request: Request instance for DescribeCertDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCertDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCertDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiagnoseReport(self, request):
        r"""以上诊断报告, 域名版本管理相关接口功能均废弃,  已确认现网0调用, 申请预下线,(预下线不会影响调用, 只会在接口中添加提示信息, 正式下线仍需人工确认)

        ### <font color=red>**该接口已废弃** </font><br>
        DescribeDiagnoseReport 用于获取指定报告id的内容。

        :param request: Request instance for DescribeDiagnoseReport.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeDiagnoseReportRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeDiagnoseReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiagnoseReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiagnoseReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDistrictIspData(self, request):
        r"""查询指定域名的区域、运营商明细数据
        注意事项：接口尚未全面开放，未在内测名单中的账号不支持调用

        :param request: Request instance for DescribeDistrictIspData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeDistrictIspDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeDistrictIspDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDistrictIspData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDistrictIspDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomains(self, request):
        r"""DescribeDomains 用于查询内容分发网络加速域名（含境内、境外）基本配置信息，包括项目ID、服务状态，业务类型、创建时间、更新时间等信息。

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsResponse`

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
        r"""DescribeDomainsConfig 用于查询内容分发网络加速域名（含境内、境外）的所有配置信息。

        :param request: Request instance for DescribeDomainsConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeDomainsConfigResponse`

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


    def DescribeEdgePackTaskStatus(self, request):
        r"""DescribeEdgePackTaskStatus 用于查询动态打包任务状态列表

        :param request: Request instance for DescribeEdgePackTaskStatus.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeEdgePackTaskStatusRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeEdgePackTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgePackTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgePackTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHttpsPackages(self, request):
        r"""DescribeHttpsPackages 用于查询 CDN HTTPS请求包详情。

        :param request: Request instance for DescribeHttpsPackages.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeHttpsPackagesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeHttpsPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHttpsPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHttpsPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageConfig(self, request):
        r"""DescribeImageConfig 用于获取域名图片优化的当前配置，支持Webp、TPG、 Guetzli 和 Avif。

        :param request: Request instance for DescribeImageConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeImageConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeImageConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpStatus(self, request):
        r"""DescribeIpStatus 用于查询域名所在加速平台的边缘节点、回源节点明细。注意事项：暂不支持查询边缘节点信息并且数据会存在一定延迟。

        >?  若您的业务已迁移至 CDN 控制台，请参考<a href="https://cloud.tencent.com/document/api/228/41954"> CDN 接口文档</a>，使用  CDN 相关API 进行操作。

        :param request: Request instance for DescribeIpStatus.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeIpStatusRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeIpStatusResponse`

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


    def DescribeIpVisit(self, request):
        r"""DescribeIpVisit 用于查询 5 分钟活跃用户数，及日活跃用户数明细

        + 5 分钟活跃用户数：根据日志中客户端 IP，5 分钟粒度去重统计
        + 日活跃用户数：根据日志中客户端 IP，按天粒度去重统计

        :param request: Request instance for DescribeIpVisit.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeIpVisitRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeIpVisitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpVisit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpVisitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMapInfo(self, request):
        r"""DescribeMapInfo 用于查询省份对应的 ID，运营商对应的 ID 信息。

        :param request: Request instance for DescribeMapInfo.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeMapInfoRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeMapInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMapInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMapInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOriginData(self, request):
        r"""DescribeOriginData 用于查询 CDN 实时回源监控数据，支持以下指标查询：

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
            headers = request.headers
            body = self.call("DescribeOriginData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOriginDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePayType(self, request):
        r"""DescribePayType 用于查询用户的计费类型，计费周期等信息。

        :param request: Request instance for DescribePayType.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePayTypeRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePayTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePayType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePayTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePurgeQuota(self, request):
        r"""DescribePurgeQuota 用于查询账户刷新配额和每日可用量。

        :param request: Request instance for DescribePurgeQuota.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeQuotaRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurgeQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePurgeQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePurgeTasks(self, request):
        r"""DescribePurgeTasks 用于查询提交的 URL 刷新、目录刷新记录及执行进度，通过 PurgePathCache 与 PurgeUrlsCache 接口提交的任务均可通过此接口进行查询。

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePurgeTasksResponse`

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


    def DescribePushQuota(self, request):
        r"""DescribePushQuota  用于查询预热配额和每日可用量。

        :param request: Request instance for DescribePushQuota.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePushQuotaRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePushQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePushQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePushQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePushTasks(self, request):
        r"""DescribePushTasks  用于查询预热任务提交历史记录及执行进度。

        :param request: Request instance for DescribePushTasks.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePushTasksRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePushTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePushTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePushTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReportData(self, request):
        r"""DescribeReportData 用于查询域名/项目维度的日/周/月报表数据。

        :param request: Request instance for DescribeReportData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeReportDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeReportDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReportData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReportDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopData(self, request):
        r"""DescribeTopData 通过入参 Metric 和 Filter 组合不同，可以查询以下排序数据：

        + 依据总流量、总请求数对访问 IP 排序，从大至小返回 TOP 100 IP
        + 依据总流量、总请求数对访问 Refer 排序，从大至小返回 TOP 100 Refer
        + 依据总流量、总请求数对访问 设备 排序，从大至小返回 设备类型
        + 依据总流量、总请求数对访问 操作系统 排序，从大至小返回 操作系统
        + 依据总流量、总请求数对访问 浏览器 排序，从大至小返回 浏览器

        注意：
        + 仅支持 90 天内数据查询，且从2021年09月20日开始有数据

        :param request: Request instance for DescribeTopData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeTopDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrafficPackages(self, request):
        r"""DescribeTrafficPackages 用于查询 CDN 流量包详情。

        :param request: Request instance for DescribeTrafficPackages.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrafficPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrafficPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUrlViolations(self, request):
        r"""DescribeUrlViolations 用于查询被 CDN 系统扫描到的域名违规 URL 列表及当前状态。
        对应内容分发网络控制台【内容合规】页面。

        :param request: Request instance for DescribeUrlViolations.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeUrlViolationsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeUrlViolationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUrlViolations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUrlViolationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableClsLogTopic(self, request):
        r"""DisableClsLogTopic 用于停止日志主题投递。注意：停止后，所有绑定该日志主题域名的日志将不再继续投递至该主题，已经投递的日志将会继续保留。生效时间约为 5~15 分钟。

        :param request: Request instance for DisableClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DisableClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DisableClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableClsLogTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DisableClsLogTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DuplicateDomainConfig(self, request):
        r"""拷贝参考域名的配置至新域名。暂不支持自有证书以及定制化配置

        :param request: Request instance for DuplicateDomainConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.DuplicateDomainConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DuplicateDomainConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DuplicateDomainConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DuplicateDomainConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableClsLogTopic(self, request):
        r"""EnableClsLogTopic 用于启动日志主题投递。注意：启动后，所有绑定该日志主题域名的日志将继续投递至该主题。生效时间约为 5~15 分钟。

        :param request: Request instance for EnableClsLogTopic.
        :type request: :class:`tencentcloud.cdn.v20180606.models.EnableClsLogTopicRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.EnableClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableClsLogTopic", params, headers=headers)
            response = json.loads(body)
            model = models.EnableClsLogTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListClsLogTopics(self, request):
        r"""ListClsLogTopics 用于显示日志主题列表。注意：一个日志集下至多含10个日志主题。

        :param request: Request instance for ListClsLogTopics.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListClsLogTopicsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListClsLogTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListClsLogTopics", params, headers=headers)
            response = json.loads(body)
            model = models.ListClsLogTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListClsTopicDomains(self, request):
        r"""ListClsTopicDomains 用于获取某日志主题下绑定的域名列表。

        :param request: Request instance for ListClsTopicDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListClsTopicDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListClsTopicDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListClsTopicDomains", params, headers=headers)
            response = json.loads(body)
            model = models.ListClsTopicDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDiagnoseReport(self, request):
        r"""以上诊断报告, 域名版本管理相关接口功能均废弃,  已确认现网0调用, 申请预下线,(预下线不会影响调用, 只会在接口中添加提示信息, 正式下线仍需人工确认)

        ### <font color=red>**该接口已废弃** </font><br>
        ListDiagnoseReport 用于获取用户诊断URL访问后各个子任务的简要详情。

        :param request: Request instance for ListDiagnoseReport.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListDiagnoseReportRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListDiagnoseReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDiagnoseReport", params, headers=headers)
            response = json.loads(body)
            model = models.ListDiagnoseReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTopClsLogData(self, request):
        r"""通过CLS日志计算Top信息。支持近7天的日志数据。

        :param request: Request instance for ListTopClsLogData.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListTopClsLogDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListTopClsLogDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTopClsLogData", params, headers=headers)
            response = json.loads(body)
            model = models.ListTopClsLogDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTopData(self, request):
        r"""ListTopData 通过入参 Metric 和 Filter 组合不同，可以查询以下排序数据：

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
            headers = request.headers
            body = self.call("ListTopData", params, headers=headers)
            response = json.loads(body)
            model = models.ListTopDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageClsTopicDomains(self, request):
        r"""ManageClsTopicDomains 用于管理某日志主题下绑定的域名列表。

        :param request: Request instance for ManageClsTopicDomains.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ManageClsTopicDomainsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ManageClsTopicDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageClsTopicDomains", params, headers=headers)
            response = json.loads(body)
            model = models.ManageClsTopicDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainConfig(self, request):
        r"""ModifyDomainConfig 用于修改内容分发网络加速域名配置信息
        注意：
        Route 字段，使用点分隔，最后一段称为叶子节点，非叶子节点配置保持不变；
        Value 字段，使用 json 进行序列化，其中固定 update 作为 key，配置路径值参考 https://cloud.tencent.com/document/product/228/41116 接口各配置项复杂类型，为配置路径对应复杂类型下的节点。
        操作审计相关：接口的入参可能包含密钥等敏感信息，所以此接口的入参不会上报到操作审计。

        :param request: Request instance for ModifyDomainConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ModifyDomainConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ModifyDomainConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPurgeFetchTaskStatus(self, request):
        r"""ModifyPurgeFetchTaskStatus 用于上报定时刷新预热任务执行状态

        :param request: Request instance for ModifyPurgeFetchTaskStatus.
        :type request: :class:`tencentcloud.cdn.v20180606.models.ModifyPurgeFetchTaskStatusRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ModifyPurgeFetchTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPurgeFetchTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPurgeFetchTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PurgePathCache(self, request):
        r"""PurgePathCache 用于批量提交目录刷新，根据域名的加速区域进行对应区域的刷新。
        默认情况下境内、境外加速区域每日目录刷新额度为各 100 条，每次最多可提交 500 条。

        :param request: Request instance for PurgePathCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PurgePathCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PurgePathCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PurgePathCache", params, headers=headers)
            response = json.loads(body)
            model = models.PurgePathCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PurgeUrlsCache(self, request):
        r"""PurgeUrlsCache 用于批量提交 URL 进行刷新，根据 URL 中域名的当前加速区域进行对应区域的刷新。
        默认情况下境内、境外加速区域每日 URL 刷新额度各为 10000 条，每次最多可提交 1000 条。

        :param request: Request instance for PurgeUrlsCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PurgeUrlsCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PurgeUrlsCacheResponse`

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


    def PushUrlsCache(self, request):
        r"""PushUrlsCache 用于将指定 URL 资源列表加载至 CDN 节点，支持指定加速区域预热。
        默认情况下境内、境外每日预热 URL 限额为各 1000 条，每次最多可提交 500 条 URL，每次提交的数量会消耗配额总数。如：1次提交500条URL全球预热，此时境内、境外预热 URL 各剩余 500条。注意：中国境外区域预热，资源默认加载至中国境外边缘节点。

        :param request: Request instance for PushUrlsCache.
        :type request: :class:`tencentcloud.cdn.v20180606.models.PushUrlsCacheRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PushUrlsCacheResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PushUrlsCache", params, headers=headers)
            response = json.loads(body)
            model = models.PushUrlsCacheResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchClsLog(self, request):
        r"""SearchClsLog 用于 CLS 日志检索。支持检索今天，24小时（可选近7中的某一天），近7天的日志数据。

        :param request: Request instance for SearchClsLog.
        :type request: :class:`tencentcloud.cdn.v20180606.models.SearchClsLogRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.SearchClsLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchClsLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchClsLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartCdnDomain(self, request):
        r"""StartCdnDomain 用于启用已停用域名的加速服务

        :param request: Request instance for StartCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.StartCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StartCdnDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartCdnDomain", params, headers=headers)
            response = json.loads(body)
            model = models.StartCdnDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCdnDomain(self, request):
        r"""StopCdnDomain 用于停止域名的加速服务。
        注意：停止加速服务后，访问至加速节点的请求将会直接返回 404。为避免对您的业务造成影响，请在停止加速服务前将解析切走。

        :param request: Request instance for StopCdnDomain.
        :type request: :class:`tencentcloud.cdn.v20180606.models.StopCdnDomainRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StopCdnDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCdnDomain", params, headers=headers)
            response = json.loads(body)
            model = models.StopCdnDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDomainConfig(self, request):
        r"""UpdateDomainConfig 用于修改内容分发网络加速域名配置信息。
        注意：如果需要更新复杂类型的配置项，必须传递整个对象的所有属性，未传递的属性将使用默认值，建议通过查询接口获取配置属性后，直接修改后传递给本接口；如果仅修改单独配置项只传对应配置参数即可。
        操作审计相关：接口的入参可能包含密钥等敏感信息，所以此接口的入参不会上报到操作审计。

        :param request: Request instance for UpdateDomainConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.UpdateDomainConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UpdateDomainConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDomainConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDomainConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateImageConfig(self, request):
        r"""UpdateImageConfig 用于更新控制台图片优化的相关配置，支持Webp、TPG、 Guetzli 和 Avif。

        :param request: Request instance for UpdateImageConfig.
        :type request: :class:`tencentcloud.cdn.v20180606.models.UpdateImageConfigRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UpdateImageConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateImageConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateImageConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdatePayType(self, request):
        r"""本接口(UpdatePayType)用于修改账号计费类型，暂不支持月结用户或子账号修改。

        :param request: Request instance for UpdatePayType.
        :type request: :class:`tencentcloud.cdn.v20180606.models.UpdatePayTypeRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UpdatePayTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePayType", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePayTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyDomainRecord(self, request):
        r"""VerifyDomainRecord 用于验证域名解析值。
        验证域名解析记录值前，您需要通过 [CreateVerifyRecord](https://cloud.tencent.com/document/product/228/48118) 生成校验解析值，验证通过后，24小时有效。
        具体流程可参考：[使用API接口进行域名归属校验](https://cloud.tencent.com/document/product/228/61702#.E6.96.B9.E6.B3.95.E4.B8.89.EF.BC.9Aapi-.E6.8E.A5.E5.8F.A3.E6.93.8D.E4.BD.9C)

        :param request: Request instance for VerifyDomainRecord.
        :type request: :class:`tencentcloud.cdn.v20180606.models.VerifyDomainRecordRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.VerifyDomainRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyDomainRecord", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyDomainRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))