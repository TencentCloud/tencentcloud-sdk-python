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
from tencentcloud.cdn.v20180606 import models
from typing import Dict


class CdnClient(AbstractClient):
    _apiVersion = '2018-06-06'
    _endpoint = 'cdn.tencentcloudapi.com'
    _service = 'cdn'

    async def AddCLSTopicDomains(
            self,
            request: models.AddCLSTopicDomainsRequest,
            opts: Dict = None,
    ) -> models.AddCLSTopicDomainsResponse:
        """
        AddCLSTopicDomains 用于新增域名到某日志主题下
        """
        
        kwargs = {}
        kwargs["action"] = "AddCLSTopicDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCLSTopicDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCdnDomain(
            self,
            request: models.AddCdnDomainRequest,
            opts: Dict = None,
    ) -> models.AddCdnDomainResponse:
        """
        AddCdnDomain 用于新增内容分发网络加速域名。1分钟内最多可新增100个域名。
        """
        
        kwargs = {}
        kwargs["action"] = "AddCdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClsLogTopic(
            self,
            request: models.CreateClsLogTopicRequest,
            opts: Dict = None,
    ) -> models.CreateClsLogTopicResponse:
        """
        CreateClsLogTopic 用于创建日志主题。注意：一个日志集下至多可创建10个日志主题。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClsLogTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClsLogTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDiagnoseUrl(
            self,
            request: models.CreateDiagnoseUrlRequest,
            opts: Dict = None,
    ) -> models.CreateDiagnoseUrlResponse:
        """
        以上诊断报告, 域名版本管理相关接口功能均废弃,  已确认现网0调用, 申请预下线,(预下线不会影响调用, 只会在接口中添加提示信息, 正式下线仍需人工确认)

        ### <font color=red>**该接口已废弃** </font><br>
        CreateDiagnoseUrl 用于添加域名诊断任务URL。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDiagnoseUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDiagnoseUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdgePackTask(
            self,
            request: models.CreateEdgePackTaskRequest,
            opts: Dict = None,
    ) -> models.CreateEdgePackTaskResponse:
        """
        动态打包任务提交接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdgePackTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdgePackTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVerifyRecord(
            self,
            request: models.CreateVerifyRecordRequest,
            opts: Dict = None,
    ) -> models.CreateVerifyRecordResponse:
        """
        CreateVerifyRecord 用于生成一条子域名解析，提示客户添加到域名解析上，用于泛域名及域名取回校验归属权。
        生成的解析记录可通过 [VerifyDomainRecord](https://cloud.tencent.com/document/product/228/48117) 完成归属权校验。
        注意：生成的解析记录有效期为24小时，超过24小时后，需重新生成。
        具体流程可参考：[使用API接口进行域名归属校验](https://cloud.tencent.com/document/product/228/61702#.E6.96.B9.E6.B3.95.E4.B8.89.EF.BC.9Aapi-.E6.8E.A5.E5.8F.A3.E6.93.8D.E4.BD.9C)
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVerifyRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVerifyRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCdnDomain(
            self,
            request: models.DeleteCdnDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteCdnDomainResponse:
        """
        DeleteCdnDomain 用于删除指定加速域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClsLogTopic(
            self,
            request: models.DeleteClsLogTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteClsLogTopicResponse:
        """
        DeleteClsLogTopic 用于删除日志主题。注意：删除后，所有该日志主题下绑定域名的日志将不再继续投递至该主题，已经投递的日志将会被全部清空。生效时间约为 5~15 分钟。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClsLogTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClsLogTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingData(
            self,
            request: models.DescribeBillingDataRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingDataResponse:
        """
        DescribeBillingData 用于查询实际计费数据明细。
        注意:
        受计费算法的影响，计费数据接口返回的数据均存在一定延时。小时结算客户预计延时3-5小时。月结算客户预计延迟4-28小时，在凌晨4点（不含4点）之前，仅能查询到前2天数据，4点（含）之后，能查询到前1天数据。若您对数据及时性较强的诉求，建议使用[监控访问数据](https://cloud.tencent.com/document/product/228/30986)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnData(
            self,
            request: models.DescribeCdnDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnDataResponse:
        """
        DescribeCdnData 用于查询 CDN 实时访问监控数据，支持以下指标查询：

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
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdnData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdnDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnDomainLogs(
            self,
            request: models.DescribeCdnDomainLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnDomainLogsResponse:
        """
        DescribeCdnDomainLogs 用于查询访问日志下载地址，仅支持 30 天以内的境内、境外访问日志下载链接查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdnDomainLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdnDomainLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnIp(
            self,
            request: models.DescribeCdnIpRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnIpResponse:
        """
        DescribeCdnIp 用于查询 CDN IP 归属。
        （注意：此接口请求频率限制以 CDN 侧限制为准：200次/10分钟）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdnIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdnIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnOriginIp(
            self,
            request: models.DescribeCdnOriginIpRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnOriginIpResponse:
        """
        ### <font color=red>**该接口已废弃** </font><br>
        本接口（DescribeCdnOriginIp）用于查询 CDN 回源节点的IP信息。（注：替换接口为DescribeIpStatus）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdnOriginIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdnOriginIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertDomains(
            self,
            request: models.DescribeCertDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeCertDomainsResponse:
        """
        DescribeCertDomains 用于校验SSL证书并提取证书中包含的域名。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiagnoseReport(
            self,
            request: models.DescribeDiagnoseReportRequest,
            opts: Dict = None,
    ) -> models.DescribeDiagnoseReportResponse:
        """
        以上诊断报告, 域名版本管理相关接口功能均废弃,  已确认现网0调用, 申请预下线,(预下线不会影响调用, 只会在接口中添加提示信息, 正式下线仍需人工确认)

        ### <font color=red>**该接口已废弃** </font><br>
        DescribeDiagnoseReport 用于获取指定报告id的内容。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiagnoseReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiagnoseReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDistrictIspData(
            self,
            request: models.DescribeDistrictIspDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDistrictIspDataResponse:
        """
        查询指定域名的区域、运营商明细数据
        注意事项：接口尚未全面开放，未在内测名单中的账号不支持调用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDistrictIspData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDistrictIspDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomains(
            self,
            request: models.DescribeDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainsResponse:
        """
        DescribeDomains 用于查询内容分发网络加速域名（含境内、境外）基本配置信息，包括项目ID、服务状态，业务类型、创建时间、更新时间等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainsConfig(
            self,
            request: models.DescribeDomainsConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainsConfigResponse:
        """
        DescribeDomainsConfig 用于查询内容分发网络加速域名（含境内、境外）的所有配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainsConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainsConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgePackTaskStatus(
            self,
            request: models.DescribeEdgePackTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgePackTaskStatusResponse:
        """
        DescribeEdgePackTaskStatus 用于查询动态打包任务状态列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgePackTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgePackTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHttpsPackages(
            self,
            request: models.DescribeHttpsPackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeHttpsPackagesResponse:
        """
        DescribeHttpsPackages 用于查询 CDN HTTPS请求包详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHttpsPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHttpsPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageConfig(
            self,
            request: models.DescribeImageConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeImageConfigResponse:
        """
        DescribeImageConfig 用于获取域名图片优化的当前配置，支持Webp、TPG、 Guetzli 和 Avif。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpStatus(
            self,
            request: models.DescribeIpStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeIpStatusResponse:
        """
        DescribeIpStatus 用于查询域名所在加速平台的边缘节点、回源节点明细。注意事项：暂不支持查询边缘节点信息并且数据会存在一定延迟。

        >?  若您的业务已迁移至 CDN 控制台，请参考<a href="https://cloud.tencent.com/document/api/228/41954"> CDN 接口文档</a>，使用  CDN 相关API 进行操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpVisit(
            self,
            request: models.DescribeIpVisitRequest,
            opts: Dict = None,
    ) -> models.DescribeIpVisitResponse:
        """
        DescribeIpVisit 用于查询 5 分钟活跃用户数，及日活跃用户数明细

        + 5 分钟活跃用户数：根据日志中客户端 IP，5 分钟粒度去重统计
        + 日活跃用户数：根据日志中客户端 IP，按天粒度去重统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpVisit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpVisitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMapInfo(
            self,
            request: models.DescribeMapInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeMapInfoResponse:
        """
        DescribeMapInfo 用于查询省份对应的 ID，运营商对应的 ID 信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMapInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMapInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginData(
            self,
            request: models.DescribeOriginDataRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginDataResponse:
        """
        DescribeOriginData 用于查询 CDN 实时回源监控数据，支持以下指标查询：

        + 回源流量（单位为 byte）
        + 回源带宽（单位为 bps）
        + 回源请求数（单位为 次）
        + 回源失败请求数（单位为 次）
        + 回源失败率（单位为 %，小数点后保留两位）
        + 回源状态码 2xx 汇总及各 2 开头回源状态码明细（单位为 个）
        + 回源状态码 3xx 汇总及各 3 开头回源状态码明细（单位为 个）
        + 回源状态码 4xx 汇总及各 4 开头回源状态码明细（单位为 个）
        + 回源状态码 5xx 汇总及各 5 开头回源状态码明细（单位为 个）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePayType(
            self,
            request: models.DescribePayTypeRequest,
            opts: Dict = None,
    ) -> models.DescribePayTypeResponse:
        """
        DescribePayType 用于查询用户的计费类型，计费周期等信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePayType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePayTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurgeQuota(
            self,
            request: models.DescribePurgeQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribePurgeQuotaResponse:
        """
        DescribePurgeQuota 用于查询账户刷新配额和每日可用量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurgeQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurgeQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurgeTasks(
            self,
            request: models.DescribePurgeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePurgeTasksResponse:
        """
        DescribePurgeTasks 用于查询提交的 URL 刷新、目录刷新记录及执行进度，通过 PurgePathCache 与 PurgeUrlsCache 接口提交的任务均可通过此接口进行查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurgeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurgeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePushQuota(
            self,
            request: models.DescribePushQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribePushQuotaResponse:
        """
        DescribePushQuota  用于查询预热配额和每日可用量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePushQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePushQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePushTasks(
            self,
            request: models.DescribePushTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePushTasksResponse:
        """
        DescribePushTasks  用于查询预热任务提交历史记录及执行进度。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePushTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePushTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReportData(
            self,
            request: models.DescribeReportDataRequest,
            opts: Dict = None,
    ) -> models.DescribeReportDataResponse:
        """
        DescribeReportData 用于查询域名/项目维度的日/周/月报表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReportData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReportDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopData(
            self,
            request: models.DescribeTopDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTopDataResponse:
        """
        DescribeTopData 通过入参 Metric 和 Filter 组合不同，可以查询以下排序数据：

        + 依据总流量、总请求数对访问 IP 排序，从大至小返回 TOP 100 IP
        + 依据总流量、总请求数对访问 Refer 排序，从大至小返回 TOP 100 Refer
        + 依据总流量、总请求数对访问 设备 排序，从大至小返回 设备类型
        + 依据总流量、总请求数对访问 操作系统 排序，从大至小返回 操作系统
        + 依据总流量、总请求数对访问 浏览器 排序，从大至小返回 浏览器

        注意：
        + 仅支持 90 天内数据查询，且从2021年09月20日开始有数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficPackages(
            self,
            request: models.DescribeTrafficPackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficPackagesResponse:
        """
        DescribeTrafficPackages 用于查询 CDN 流量包详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUrlViolations(
            self,
            request: models.DescribeUrlViolationsRequest,
            opts: Dict = None,
    ) -> models.DescribeUrlViolationsResponse:
        """
        DescribeUrlViolations 用于查询被 CDN 系统扫描到的域名违规 URL 列表及当前状态。
        对应内容分发网络控制台【内容合规】页面。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUrlViolations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUrlViolationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableClsLogTopic(
            self,
            request: models.DisableClsLogTopicRequest,
            opts: Dict = None,
    ) -> models.DisableClsLogTopicResponse:
        """
        DisableClsLogTopic 用于停止日志主题投递。注意：停止后，所有绑定该日志主题域名的日志将不再继续投递至该主题，已经投递的日志将会继续保留。生效时间约为 5~15 分钟。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableClsLogTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableClsLogTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DuplicateDomainConfig(
            self,
            request: models.DuplicateDomainConfigRequest,
            opts: Dict = None,
    ) -> models.DuplicateDomainConfigResponse:
        """
        拷贝参考域名的配置至新域名。暂不支持自有证书以及定制化配置
        """
        
        kwargs = {}
        kwargs["action"] = "DuplicateDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DuplicateDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableClsLogTopic(
            self,
            request: models.EnableClsLogTopicRequest,
            opts: Dict = None,
    ) -> models.EnableClsLogTopicResponse:
        """
        EnableClsLogTopic 用于启动日志主题投递。注意：启动后，所有绑定该日志主题域名的日志将继续投递至该主题。生效时间约为 5~15 分钟。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableClsLogTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableClsLogTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListClsLogTopics(
            self,
            request: models.ListClsLogTopicsRequest,
            opts: Dict = None,
    ) -> models.ListClsLogTopicsResponse:
        """
        ListClsLogTopics 用于显示日志主题列表。注意：一个日志集下至多含10个日志主题。
        """
        
        kwargs = {}
        kwargs["action"] = "ListClsLogTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListClsLogTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListClsTopicDomains(
            self,
            request: models.ListClsTopicDomainsRequest,
            opts: Dict = None,
    ) -> models.ListClsTopicDomainsResponse:
        """
        ListClsTopicDomains 用于获取某日志主题下绑定的域名列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListClsTopicDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListClsTopicDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDiagnoseReport(
            self,
            request: models.ListDiagnoseReportRequest,
            opts: Dict = None,
    ) -> models.ListDiagnoseReportResponse:
        """
        以上诊断报告, 域名版本管理相关接口功能均废弃,  已确认现网0调用, 申请预下线,(预下线不会影响调用, 只会在接口中添加提示信息, 正式下线仍需人工确认)

        ### <font color=red>**该接口已废弃** </font><br>
        ListDiagnoseReport 用于获取用户诊断URL访问后各个子任务的简要详情。
        """
        
        kwargs = {}
        kwargs["action"] = "ListDiagnoseReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDiagnoseReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTopClsLogData(
            self,
            request: models.ListTopClsLogDataRequest,
            opts: Dict = None,
    ) -> models.ListTopClsLogDataResponse:
        """
        通过CLS日志计算Top信息。支持近7天的日志数据。
        """
        
        kwargs = {}
        kwargs["action"] = "ListTopClsLogData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTopClsLogDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTopData(
            self,
            request: models.ListTopDataRequest,
            opts: Dict = None,
    ) -> models.ListTopDataResponse:
        """
        ListTopData 通过入参 Metric 和 Filter 组合不同，可以查询以下排序数据：

        + 依据总流量、总请求数对访问 URL 排序，从大至小返回 TOP 1000 URL
        + 依据总流量、总请求数对客户端省份排序，从大至小返回省份列表
        + 依据总流量、总请求数对客户端运营商排序，从大至小返回运营商列表
        + 依据总流量、峰值带宽、总请求数、平均命中率、2XX/3XX/4XX/5XX 状态码对域名排序，从大至小返回域名列表
        + 依据总回源流量、回源峰值带宽、总回源请求数、平均回源失败率、2XX/3XX/4XX/5XX 回源状态码对域名排序，从大至小返回域名列表

        注意：仅支持 90 天内数据查询
        """
        
        kwargs = {}
        kwargs["action"] = "ListTopData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTopDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageClsTopicDomains(
            self,
            request: models.ManageClsTopicDomainsRequest,
            opts: Dict = None,
    ) -> models.ManageClsTopicDomainsResponse:
        """
        ManageClsTopicDomains 用于管理某日志主题下绑定的域名列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ManageClsTopicDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageClsTopicDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainConfig(
            self,
            request: models.ModifyDomainConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainConfigResponse:
        """
        ModifyDomainConfig 用于修改内容分发网络加速域名配置信息
        注意：
        Route 字段，使用点分隔，最后一段称为叶子节点，非叶子节点配置保持不变；
        Value 字段，使用 json 进行序列化，其中固定 update 作为 key，配置路径值参考 https://cloud.tencent.com/document/product/228/41116 接口各配置项复杂类型，为配置路径对应复杂类型下的节点。
        操作审计相关：接口的入参可能包含密钥等敏感信息，所以此接口的入参不会上报到操作审计。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPurgeFetchTaskStatus(
            self,
            request: models.ModifyPurgeFetchTaskStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyPurgeFetchTaskStatusResponse:
        """
        ModifyPurgeFetchTaskStatus 用于上报定时刷新预热任务执行状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPurgeFetchTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPurgeFetchTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PurgePathCache(
            self,
            request: models.PurgePathCacheRequest,
            opts: Dict = None,
    ) -> models.PurgePathCacheResponse:
        """
        PurgePathCache 用于批量提交目录刷新，根据域名的加速区域进行对应区域的刷新。
        默认情况下境内、境外加速区域每日目录刷新额度为各 100 条，每次最多可提交 500 条。
        """
        
        kwargs = {}
        kwargs["action"] = "PurgePathCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PurgePathCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PurgeUrlsCache(
            self,
            request: models.PurgeUrlsCacheRequest,
            opts: Dict = None,
    ) -> models.PurgeUrlsCacheResponse:
        """
        PurgeUrlsCache 用于批量提交 URL 进行刷新，根据 URL 中域名的当前加速区域进行对应区域的刷新。
        默认情况下境内、境外加速区域每日 URL 刷新额度各为 10000 条，每次最多可提交 1000 条。
        """
        
        kwargs = {}
        kwargs["action"] = "PurgeUrlsCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PurgeUrlsCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PushUrlsCache(
            self,
            request: models.PushUrlsCacheRequest,
            opts: Dict = None,
    ) -> models.PushUrlsCacheResponse:
        """
        PushUrlsCache 用于将指定 URL 资源列表加载至 CDN 节点，支持指定加速区域预热。
        默认情况下境内、境外每日预热 URL 限额为各 1000 条，每次最多可提交 500 条 URL，每次提交的数量会消耗配额总数。如：1次提交500条URL全球预热，此时境内、境外预热 URL 各剩余 500条。注意：中国境外区域预热，资源默认加载至中国境外边缘节点。
        """
        
        kwargs = {}
        kwargs["action"] = "PushUrlsCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PushUrlsCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchClsLog(
            self,
            request: models.SearchClsLogRequest,
            opts: Dict = None,
    ) -> models.SearchClsLogResponse:
        """
        SearchClsLog 用于 CLS 日志检索。支持检索今天，24小时（可选近7中的某一天），近7天的日志数据。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchClsLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchClsLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCdnDomain(
            self,
            request: models.StartCdnDomainRequest,
            opts: Dict = None,
    ) -> models.StartCdnDomainResponse:
        """
        StartCdnDomain 用于启用已停用域名的加速服务
        """
        
        kwargs = {}
        kwargs["action"] = "StartCdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartCdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCdnDomain(
            self,
            request: models.StopCdnDomainRequest,
            opts: Dict = None,
    ) -> models.StopCdnDomainResponse:
        """
        StopCdnDomain 用于停止域名的加速服务。
        注意：停止加速服务后，访问至加速节点的请求将会直接返回 404。为避免对您的业务造成影响，请在停止加速服务前将解析切走。
        """
        
        kwargs = {}
        kwargs["action"] = "StopCdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDomainConfig(
            self,
            request: models.UpdateDomainConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateDomainConfigResponse:
        """
        UpdateDomainConfig 用于修改内容分发网络加速域名配置信息。
        注意：如果需要更新复杂类型的配置项，必须传递整个对象的所有属性，未传递的属性将使用默认值，建议通过查询接口获取配置属性后，直接修改后传递给本接口；如果仅修改单独配置项只传对应配置参数即可。
        操作审计相关：接口的入参可能包含密钥等敏感信息，所以此接口的入参不会上报到操作审计。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateImageConfig(
            self,
            request: models.UpdateImageConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateImageConfigResponse:
        """
        UpdateImageConfig 用于更新控制台图片优化的相关配置，支持Webp、TPG、 Guetzli 和 Avif。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateImageConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateImageConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePayType(
            self,
            request: models.UpdatePayTypeRequest,
            opts: Dict = None,
    ) -> models.UpdatePayTypeResponse:
        """
        本接口(UpdatePayType)用于修改账号计费类型，暂不支持月结用户或子账号修改。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePayType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePayTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyDomainRecord(
            self,
            request: models.VerifyDomainRecordRequest,
            opts: Dict = None,
    ) -> models.VerifyDomainRecordResponse:
        """
        VerifyDomainRecord 用于验证域名解析值。
        验证域名解析记录值前，您需要通过 [CreateVerifyRecord](https://cloud.tencent.com/document/product/228/48118) 生成校验解析值，验证通过后，24小时有效。
        具体流程可参考：[使用API接口进行域名归属校验](https://cloud.tencent.com/document/product/228/61702#.E6.96.B9.E6.B3.95.E4.B8.89.EF.BC.9Aapi-.E6.8E.A5.E5.8F.A3.E6.93.8D.E4.BD.9C)
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyDomainRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyDomainRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)