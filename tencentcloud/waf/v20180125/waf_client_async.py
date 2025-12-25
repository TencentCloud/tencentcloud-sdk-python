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
from tencentcloud.waf.v20180125 import models
from typing import Dict


class WafClient(AbstractClient):
    _apiVersion = '2018-01-25'
    _endpoint = 'waf.tencentcloudapi.com'
    _service = 'waf'

    async def AddAntiFakeUrl(
            self,
            request: models.AddAntiFakeUrlRequest,
            opts: Dict = None,
    ) -> models.AddAntiFakeUrlResponse:
        """
        添加防篡改url
        """
        
        kwargs = {}
        kwargs["action"] = "AddAntiFakeUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAntiFakeUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAntiInfoLeakRules(
            self,
            request: models.AddAntiInfoLeakRulesRequest,
            opts: Dict = None,
    ) -> models.AddAntiInfoLeakRulesResponse:
        """
        添加信息防泄漏规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddAntiInfoLeakRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAntiInfoLeakRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAreaBanAreas(
            self,
            request: models.AddAreaBanAreasRequest,
            opts: Dict = None,
    ) -> models.AddAreaBanAreasResponse:
        """
        添加地域封禁中的地域信息
        """
        
        kwargs = {}
        kwargs["action"] = "AddAreaBanAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAreaBanAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAttackWhiteRule(
            self,
            request: models.AddAttackWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.AddAttackWhiteRuleResponse:
        """
        供用户控制台调用，增加Tiga规则引擎白名单。
        """
        
        kwargs = {}
        kwargs["action"] = "AddAttackWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAttackWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddBypassAllRule(
            self,
            request: models.AddBypassAllRuleRequest,
            opts: Dict = None,
    ) -> models.AddBypassAllRuleResponse:
        """
        添加一键bypass能力支持,直接添加APPID
        """
        
        kwargs = {}
        kwargs["action"] = "AddBypassAllRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddBypassAllRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCustomRule(
            self,
            request: models.AddCustomRuleRequest,
            opts: Dict = None,
    ) -> models.AddCustomRuleResponse:
        """
        增加访问控制（自定义策略）
        """
        
        kwargs = {}
        kwargs["action"] = "AddCustomRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCustomRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCustomWhiteRule(
            self,
            request: models.AddCustomWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.AddCustomWhiteRuleResponse:
        """
        增加精准白名单规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddCustomWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCustomWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddDomainWhiteRule(
            self,
            request: models.AddDomainWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.AddDomainWhiteRuleResponse:
        """
        增加域名规则白名单
        """
        
        kwargs = {}
        kwargs["action"] = "AddDomainWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDomainWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddSpartaProtection(
            self,
            request: models.AddSpartaProtectionRequest,
            opts: Dict = None,
    ) -> models.AddSpartaProtectionResponse:
        """
        添加SaaS型WAF防护域名
        """
        
        kwargs = {}
        kwargs["action"] = "AddSpartaProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddSpartaProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchOperateUserSignatureRules(
            self,
            request: models.BatchOperateUserSignatureRulesRequest,
            opts: Dict = None,
    ) -> models.BatchOperateUserSignatureRulesResponse:
        """
        批量操作tiga子规则
        """
        
        kwargs = {}
        kwargs["action"] = "BatchOperateUserSignatureRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchOperateUserSignatureRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessExport(
            self,
            request: models.CreateAccessExportRequest,
            opts: Dict = None,
    ) -> models.CreateAccessExportResponse:
        """
        本接口用于创建访问日志导出
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAreaBanRule(
            self,
            request: models.CreateAreaBanRuleRequest,
            opts: Dict = None,
    ) -> models.CreateAreaBanRuleResponse:
        """
        添加（编辑）地域封禁中的地域信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAreaBanRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAreaBanRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBatchIpAccessControl(
            self,
            request: models.CreateBatchIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.CreateBatchIpAccessControlResponse:
        """
        批量IP黑白名单新增接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBatchIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBatchIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeals(
            self,
            request: models.CreateDealsRequest,
            opts: Dict = None,
    ) -> models.CreateDealsResponse:
        """
        计费资源购买、续费下单接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeals"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDealsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExport(
            self,
            request: models.CreateExportRequest,
            opts: Dict = None,
    ) -> models.CreateExportResponse:
        """
        本接口仅创建下载任务，任务返回的下载地址，请用户调用DescribeExports查看任务列表。其中有下载地址CosPath参数。参考文档https://cloud.tencent.com/document/product/614/56449
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHost(
            self,
            request: models.CreateHostRequest,
            opts: Dict = None,
    ) -> models.CreateHostResponse:
        """
        clb-waf中添加防护域名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIpAccessControl(
            self,
            request: models.CreateIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.CreateIpAccessControlResponse:
        """
        Waf IP黑白名单新增接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOwaspWhiteRule(
            self,
            request: models.CreateOwaspWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.CreateOwaspWhiteRuleResponse:
        """
        添加规则引擎白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOwaspWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOwaspWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePostCKafkaFlow(
            self,
            request: models.CreatePostCKafkaFlowRequest,
            opts: Dict = None,
    ) -> models.CreatePostCKafkaFlowResponse:
        """
        创建CKafka投递流任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePostCKafkaFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePostCKafkaFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePostCLSFlow(
            self,
            request: models.CreatePostCLSFlowRequest,
            opts: Dict = None,
    ) -> models.CreatePostCLSFlowResponse:
        """
        创建CLS投递流任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePostCLSFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePostCLSFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRateLimitV2(
            self,
            request: models.CreateRateLimitV2Request,
            opts: Dict = None,
    ) -> models.CreateRateLimitV2Response:
        """
        创建限流规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRateLimitV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRateLimitV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccessExport(
            self,
            request: models.DeleteAccessExportRequest,
            opts: Dict = None,
    ) -> models.DeleteAccessExportResponse:
        """
        本接口用于删除访问日志导出
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccessExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccessExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAntiFakeUrl(
            self,
            request: models.DeleteAntiFakeUrlRequest,
            opts: Dict = None,
    ) -> models.DeleteAntiFakeUrlResponse:
        """
        删除防篡改url
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAntiFakeUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAntiFakeUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAntiInfoLeakRule(
            self,
            request: models.DeleteAntiInfoLeakRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAntiInfoLeakRuleResponse:
        """
        信息防泄漏删除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAntiInfoLeakRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAntiInfoLeakRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAttackDownloadRecord(
            self,
            request: models.DeleteAttackDownloadRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteAttackDownloadRecordResponse:
        """
        删除攻击日志下载任务记录
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAttackDownloadRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAttackDownloadRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAttackWhiteRule(
            self,
            request: models.DeleteAttackWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAttackWhiteRuleResponse:
        """
        供用户控制台调用，删除Tiga规则引擎白名单。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAttackWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAttackWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBatchIpAccessControl(
            self,
            request: models.DeleteBatchIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.DeleteBatchIpAccessControlResponse:
        """
        批量黑白名单删除接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBatchIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBatchIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBotSceneUCBRule(
            self,
            request: models.DeleteBotSceneUCBRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteBotSceneUCBRuleResponse:
        """
        场景化后删除Bot的UCB自定义规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBotSceneUCBRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBotSceneUCBRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCRule(
            self,
            request: models.DeleteCCRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteCCRuleResponse:
        """
        Waf  CC V2 Delete接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomRule(
            self,
            request: models.DeleteCustomRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomRuleResponse:
        """
        删除自定义规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomWhiteRule(
            self,
            request: models.DeleteCustomWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomWhiteRuleResponse:
        """
        删除精准白名单规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainWhiteRules(
            self,
            request: models.DeleteDomainWhiteRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainWhiteRulesResponse:
        """
        删除域名规则白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainWhiteRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainWhiteRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteExport(
            self,
            request: models.DeleteExportRequest,
            opts: Dict = None,
    ) -> models.DeleteExportResponse:
        """
        本接口用于删除日志下载任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHost(
            self,
            request: models.DeleteHostRequest,
            opts: Dict = None,
    ) -> models.DeleteHostResponse:
        """
        删除负载均衡型域名，支持批量操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIpAccessControl(
            self,
            request: models.DeleteIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.DeleteIpAccessControlResponse:
        """
        Waf IP黑白名单Delete接口（建议使用DeleteIpAccessControlV2来替换当前接口）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIpAccessControlV2(
            self,
            request: models.DeleteIpAccessControlV2Request,
            opts: Dict = None,
    ) -> models.DeleteIpAccessControlV2Response:
        """
        Waf IP黑白名单最新版本删除接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIpAccessControlV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIpAccessControlV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOwaspRuleStatus(
            self,
            request: models.DeleteOwaspRuleStatusRequest,
            opts: Dict = None,
    ) -> models.DeleteOwaspRuleStatusResponse:
        """
        解除门神规则的状态锁
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOwaspRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOwaspRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOwaspWhiteRule(
            self,
            request: models.DeleteOwaspWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteOwaspWhiteRuleResponse:
        """
        删除用户规则引擎白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOwaspWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOwaspWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRateLimitsV2(
            self,
            request: models.DeleteRateLimitsV2Request,
            opts: Dict = None,
    ) -> models.DeleteRateLimitsV2Response:
        """
        删除自研版限流规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRateLimitsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRateLimitsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSession(
            self,
            request: models.DeleteSessionRequest,
            opts: Dict = None,
    ) -> models.DeleteSessionResponse:
        """
        删除CC攻击的session设置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSpartaProtection(
            self,
            request: models.DeleteSpartaProtectionRequest,
            opts: Dict = None,
    ) -> models.DeleteSpartaProtectionResponse:
        """
        SaaS型WAF删除防护域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSpartaProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSpartaProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessExports(
            self,
            request: models.DescribeAccessExportsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessExportsResponse:
        """
        本接口用于获取访问日志导出列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessExports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessExportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessFastAnalysis(
            self,
            request: models.DescribeAccessFastAnalysisRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessFastAnalysisResponse:
        """
        本接口用于访问日志的快速分析
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessFastAnalysis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessFastAnalysisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessHistogram(
            self,
            request: models.DescribeAccessHistogramRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessHistogramResponse:
        """
        本接口用于访问日志柱状趋势图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessHistogram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessHistogramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessIndex(
            self,
            request: models.DescribeAccessIndexRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessIndexResponse:
        """
        本接口用于获取访问日志索引配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAntiFakeRules(
            self,
            request: models.DescribeAntiFakeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAntiFakeRulesResponse:
        """
        获取防篡改url
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAntiFakeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAntiFakeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAntiInfoLeakageRules(
            self,
            request: models.DescribeAntiInfoLeakageRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAntiInfoLeakageRulesResponse:
        """
        取得信息防泄漏规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAntiInfoLeakageRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAntiInfoLeakageRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiDetail(
            self,
            request: models.DescribeApiDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeApiDetailResponse:
        """
        获取Api请求详情信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiListVersionTwo(
            self,
            request: models.DescribeApiListVersionTwoRequest,
            opts: Dict = None,
    ) -> models.DescribeApiListVersionTwoResponse:
        """
        api资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiListVersionTwo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiListVersionTwoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAreaBanAreas(
            self,
            request: models.DescribeAreaBanAreasRequest,
            opts: Dict = None,
    ) -> models.DescribeAreaBanAreasResponse:
        """
        获取地域封禁配置包括地域封禁开关，设置封禁的地区信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAreaBanAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAreaBanAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAreaBanRule(
            self,
            request: models.DescribeAreaBanRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeAreaBanRuleResponse:
        """
        获取地域封禁规则配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAreaBanRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAreaBanRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAreaBanSupportAreas(
            self,
            request: models.DescribeAreaBanSupportAreasRequest,
            opts: Dict = None,
    ) -> models.DescribeAreaBanSupportAreasResponse:
        """
        获取WAF地域封禁支持的地域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAreaBanSupportAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAreaBanSupportAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackOverview(
            self,
            request: models.DescribeAttackOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackOverviewResponse:
        """
        攻击总览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackType(
            self,
            request: models.DescribeAttackTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackTypeResponse:
        """
        查询指定域名TOP N攻击类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackWhiteRule(
            self,
            request: models.DescribeAttackWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackWhiteRuleResponse:
        """
        获取用户规则白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoDenyIP(
            self,
            request: models.DescribeAutoDenyIPRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoDenyIPResponse:
        """
        描述WAF自动封禁IP详情,对齐自动封堵状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoDenyIP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoDenyIPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchIpAccessControl(
            self,
            request: models.DescribeBatchIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchIpAccessControlResponse:
        """
        Waf 批量防护IP黑白名单查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBotSceneList(
            self,
            request: models.DescribeBotSceneListRequest,
            opts: Dict = None,
    ) -> models.DescribeBotSceneListResponse:
        """
        获取BOT场景列表与概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBotSceneList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBotSceneListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBotSceneOverview(
            self,
            request: models.DescribeBotSceneOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBotSceneOverviewResponse:
        """
        获取Bot场景全局概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBotSceneOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBotSceneOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBotSceneUCBRule(
            self,
            request: models.DescribeBotSceneUCBRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeBotSceneUCBRuleResponse:
        """
        场景化后Bot获取UCB自定义规则策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBotSceneUCBRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBotSceneUCBRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCAutoStatus(
            self,
            request: models.DescribeCCAutoStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeCCAutoStatusResponse:
        """
        获取SAAS型接入的紧急CC防护状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCAutoStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCAutoStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCRule(
            self,
            request: models.DescribeCCRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeCCRuleResponse:
        """
        Waf  CC V2 Query接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCRuleList(
            self,
            request: models.DescribeCCRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCRuleListResponse:
        """
        根据多条件查询CC规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateVerifyResult(
            self,
            request: models.DescribeCertificateVerifyResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateVerifyResultResponse:
        """
        获取证书的检查结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateVerifyResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateVerifyResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCiphersDetail(
            self,
            request: models.DescribeCiphersDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCiphersDetailResponse:
        """
        Saas型WAF接入查询加密套件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCiphersDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCiphersDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomRuleList(
            self,
            request: models.DescribeCustomRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomRuleListResponse:
        """
        获取防护配置中的访问控制策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomWhiteRule(
            self,
            request: models.DescribeCustomWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomWhiteRuleResponse:
        """
        获取防护配置中的精准白名单策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainCountInfo(
            self,
            request: models.DescribeDomainCountInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainCountInfoResponse:
        """
        获取域名概况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainCountInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainCountInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainDetailsClb(
            self,
            request: models.DescribeDomainDetailsClbRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainDetailsClbResponse:
        """
        获取一个clbwaf域名详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainDetailsClb"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainDetailsClbResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainDetailsSaas(
            self,
            request: models.DescribeDomainDetailsSaasRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainDetailsSaasResponse:
        """
        查询单个saaswaf域名详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainDetailsSaas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainDetailsSaasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainRules(
            self,
            request: models.DescribeDomainRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainRulesResponse:
        """
        拉取域名的防护规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainVerifyResult(
            self,
            request: models.DescribeDomainVerifyResultRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainVerifyResultResponse:
        """
        获取添加域名操作的结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainVerifyResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainVerifyResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainWhiteRules(
            self,
            request: models.DescribeDomainWhiteRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainWhiteRulesResponse:
        """
        获取域名的规则白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainWhiteRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainWhiteRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomains(
            self,
            request: models.DescribeDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainsResponse:
        """
        查询用户所有域名的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExports(
            self,
            request: models.DescribeExportsRequest,
            opts: Dict = None,
    ) -> models.DescribeExportsResponse:
        """
        本接口用于获取日志下载任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFindDomainList(
            self,
            request: models.DescribeFindDomainListRequest,
            opts: Dict = None,
    ) -> models.DescribeFindDomainListResponse:
        """
        获取发现域名列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFindDomainList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFindDomainListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowTrend(
            self,
            request: models.DescribeFlowTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowTrendResponse:
        """
        获取waf流量访问趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHistogram(
            self,
            request: models.DescribeHistogramRequest,
            opts: Dict = None,
    ) -> models.DescribeHistogramResponse:
        """
        查询多种条件的聚类分析
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHistogram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHistogramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHost(
            self,
            request: models.DescribeHostRequest,
            opts: Dict = None,
    ) -> models.DescribeHostResponse:
        """
        clb-waf获取防护域名详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostLimit(
            self,
            request: models.DescribeHostLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeHostLimitResponse:
        """
        添加域名的首先验证是否购买了套餐，是否没有达到购买套餐的限制，域名是否已经添加
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHosts(
            self,
            request: models.DescribeHostsRequest,
            opts: Dict = None,
    ) -> models.DescribeHostsResponse:
        """
        clb-waf中获取防护域名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        查询用户所有实例的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpAccessControl(
            self,
            request: models.DescribeIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.DescribeIpAccessControlResponse:
        """
        Waf ip黑白名单查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpHitItems(
            self,
            request: models.DescribeIpHitItemsRequest,
            opts: Dict = None,
    ) -> models.DescribeIpHitItemsResponse:
        """
        Waf  IP封堵状态查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpHitItems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpHitItemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogHistogram(
            self,
            request: models.DescribeLogHistogramRequest,
            opts: Dict = None,
    ) -> models.DescribeLogHistogramResponse:
        """
        本接口用于构建日志数量直方图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogHistogram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogHistogramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModuleStatus(
            self,
            request: models.DescribeModuleStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeModuleStatusResponse:
        """
        查询各个waf基础安全模块的开关状态，看每个模块是否开启
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeObjects(
            self,
            request: models.DescribeObjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeObjectsResponse:
        """
        查看防护对象列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOwaspRuleTypes(
            self,
            request: models.DescribeOwaspRuleTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeOwaspRuleTypesResponse:
        """
        查询规则引擎的规则类型列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOwaspRuleTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOwaspRuleTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOwaspRules(
            self,
            request: models.DescribeOwaspRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeOwaspRulesResponse:
        """
        查询规则引擎的规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOwaspRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOwaspRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOwaspWhiteRules(
            self,
            request: models.DescribeOwaspWhiteRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeOwaspWhiteRulesResponse:
        """
        获取规则引擎白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOwaspWhiteRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOwaspWhiteRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePeakPoints(
            self,
            request: models.DescribePeakPointsRequest,
            opts: Dict = None,
    ) -> models.DescribePeakPointsResponse:
        """
        查询业务和攻击概要趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePeakPoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePeakPointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePeakValue(
            self,
            request: models.DescribePeakValueRequest,
            opts: Dict = None,
    ) -> models.DescribePeakValueResponse:
        """
        获取业务和攻击概览峰值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePeakValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePeakValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyStatus(
            self,
            request: models.DescribePolicyStatusRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyStatusResponse:
        """
        获取防护状态以及生效的实例id
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePorts(
            self,
            request: models.DescribePortsRequest,
            opts: Dict = None,
    ) -> models.DescribePortsResponse:
        """
        获取Saas型WAF防护端口列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePorts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePortsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePostCKafkaFlows(
            self,
            request: models.DescribePostCKafkaFlowsRequest,
            opts: Dict = None,
    ) -> models.DescribePostCKafkaFlowsResponse:
        """
        获取CKafka投递流任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePostCKafkaFlows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePostCKafkaFlowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePostCLSFlows(
            self,
            request: models.DescribePostCLSFlowsRequest,
            opts: Dict = None,
    ) -> models.DescribePostCLSFlowsResponse:
        """
        获取CLS投递流任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePostCLSFlows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePostCLSFlowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProtectionModes(
            self,
            request: models.DescribeProtectionModesRequest,
            opts: Dict = None,
    ) -> models.DescribeProtectionModesResponse:
        """
        查询Tiga引擎大类规则及其防护模式
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProtectionModes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProtectionModesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRateLimitsV2(
            self,
            request: models.DescribeRateLimitsV2Request,
            opts: Dict = None,
    ) -> models.DescribeRateLimitsV2Response:
        """
        查询限流规则列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRateLimitsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRateLimitsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleLimit(
            self,
            request: models.DescribeRuleLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleLimitResponse:
        """
        获取各个模块具体的规格限制
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanIp(
            self,
            request: models.DescribeScanIpRequest,
            opts: Dict = None,
    ) -> models.DescribeScanIpResponse:
        """
        查询扫描ip
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSession(
            self,
            request: models.DescribeSessionRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionResponse:
        """
        Waf 会话定义查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpartaProtectionInfo(
            self,
            request: models.DescribeSpartaProtectionInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSpartaProtectionInfoResponse:
        """
        waf斯巴达-获取防护域名信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpartaProtectionInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpartaProtectionInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTlsVersion(
            self,
            request: models.DescribeTlsVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeTlsVersionResponse:
        """
        查询SaaS型WAF支持的TLS版本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTlsVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTlsVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopAttackDomain(
            self,
            request: models.DescribeTopAttackDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeTopAttackDomainResponse:
        """
        查询Top5的攻击域名
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopAttackDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopAttackDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopics(
            self,
            request: models.DescribeTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicsResponse:
        """
        本接口用于获取日志主题列表，支持分页
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCdcClbWafRegions(
            self,
            request: models.DescribeUserCdcClbWafRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeUserCdcClbWafRegionsResponse:
        """
        在CDC场景下，负载均衡型WAF的添加、编辑域名配置的时候，需要展示CDC负载均衡型WAF（cdc-clb-waf)支持的地域列表，通过DescribeUserCdcClbWafRegions既可以获得当前对客户已经开放的地域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCdcClbWafRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserCdcClbWafRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserClbWafRegions(
            self,
            request: models.DescribeUserClbWafRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeUserClbWafRegionsResponse:
        """
        在负载均衡型WAF的添加、编辑域名配置的时候，需要展示负载均衡型WAF（clb-waf)支持的地域列表，通过DescribeUserClbWafRegions既可以获得当前对客户已经开放的地域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserClbWafRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserClbWafRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDomainInfo(
            self,
            request: models.DescribeUserDomainInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDomainInfoResponse:
        """
        查询saas和clb的域名信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDomainInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDomainInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserLevel(
            self,
            request: models.DescribeUserLevelRequest,
            opts: Dict = None,
    ) -> models.DescribeUserLevelResponse:
        """
        获取用户防护规则等级
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserSignatureClass(
            self,
            request: models.DescribeUserSignatureClassRequest,
            opts: Dict = None,
    ) -> models.DescribeUserSignatureClassResponse:
        """
        查询Tiga引擎规则类型及状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserSignatureClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserSignatureClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserSignatureRule(
            self,
            request: models.DescribeUserSignatureRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeUserSignatureRuleResponse:
        """
        获取用户特征规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserSignatureRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserSignatureRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserSignatureRuleV2(
            self,
            request: models.DescribeUserSignatureRuleV2Request,
            opts: Dict = None,
    ) -> models.DescribeUserSignatureRuleV2Response:
        """
        获取用户特征规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserSignatureRuleV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserSignatureRuleV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVipInfo(
            self,
            request: models.DescribeVipInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVipInfoResponse:
        """
        根据过滤条件查询VIP信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVipInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVipInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWafAutoDenyRules(
            self,
            request: models.DescribeWafAutoDenyRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeWafAutoDenyRulesResponse:
        """
        返回ip惩罚规则详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWafAutoDenyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWafAutoDenyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWafAutoDenyStatus(
            self,
            request: models.DescribeWafAutoDenyStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeWafAutoDenyStatusResponse:
        """
        废弃接口

        描述WAF自动封禁模块详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWafAutoDenyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWafAutoDenyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWafThreatenIntelligence(
            self,
            request: models.DescribeWafThreatenIntelligenceRequest,
            opts: Dict = None,
    ) -> models.DescribeWafThreatenIntelligenceResponse:
        """
        描述WAF威胁情报封禁模块配置详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWafThreatenIntelligence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWafThreatenIntelligenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebshellStatus(
            self,
            request: models.DescribeWebshellStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeWebshellStatusResponse:
        """
        获取域名的webshell状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebshellStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebshellStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPostCKafkaFlow(
            self,
            request: models.DestroyPostCKafkaFlowRequest,
            opts: Dict = None,
    ) -> models.DestroyPostCKafkaFlowResponse:
        """
        销毁CKafka投递流任务
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPostCKafkaFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPostCKafkaFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPostCLSFlow(
            self,
            request: models.DestroyPostCLSFlowRequest,
            opts: Dict = None,
    ) -> models.DestroyPostCLSFlowResponse:
        """
        销毁CLS投递流任务
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPostCLSFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPostCLSFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableRateLimitsV2(
            self,
            request: models.EnableRateLimitsV2Request,
            opts: Dict = None,
    ) -> models.EnableRateLimitsV2Response:
        """
        批量更改自研版限流规则开关
        """
        
        kwargs = {}
        kwargs["action"] = "EnableRateLimitsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableRateLimitsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FreshAntiFakeUrl(
            self,
            request: models.FreshAntiFakeUrlRequest,
            opts: Dict = None,
    ) -> models.FreshAntiFakeUrlResponse:
        """
        刷新防篡改url
        """
        
        kwargs = {}
        kwargs["action"] = "FreshAntiFakeUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FreshAntiFakeUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateDealsAndPayNew(
            self,
            request: models.GenerateDealsAndPayNewRequest,
            opts: Dict = None,
    ) -> models.GenerateDealsAndPayNewResponse:
        """
        计费资源购买、续费下单接口
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateDealsAndPayNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateDealsAndPayNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAttackDownloadRecords(
            self,
            request: models.GetAttackDownloadRecordsRequest,
            opts: Dict = None,
    ) -> models.GetAttackDownloadRecordsResponse:
        """
        查询下载攻击日志任务记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetAttackDownloadRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAttackDownloadRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAttackHistogram(
            self,
            request: models.GetAttackHistogramRequest,
            opts: Dict = None,
    ) -> models.GetAttackHistogramResponse:
        """
        生成攻击日志的产生时间柱状图
        """
        
        kwargs = {}
        kwargs["action"] = "GetAttackHistogram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAttackHistogramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAttackTotalCount(
            self,
            request: models.GetAttackTotalCountRequest,
            opts: Dict = None,
    ) -> models.GetAttackTotalCountResponse:
        """
        按照条件查询展示攻击总次数
        """
        
        kwargs = {}
        kwargs["action"] = "GetAttackTotalCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAttackTotalCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetInstanceQpsLimit(
            self,
            request: models.GetInstanceQpsLimitRequest,
            opts: Dict = None,
    ) -> models.GetInstanceQpsLimitResponse:
        """
        获取套餐实例的弹性qps上限
        """
        
        kwargs = {}
        kwargs["action"] = "GetInstanceQpsLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetInstanceQpsLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportIpAccessControl(
            self,
            request: models.ImportIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.ImportIpAccessControlResponse:
        """
        导入IP黑白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ImportIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAntiFakeUrl(
            self,
            request: models.ModifyAntiFakeUrlRequest,
            opts: Dict = None,
    ) -> models.ModifyAntiFakeUrlResponse:
        """
        编辑防篡改url
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAntiFakeUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAntiFakeUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAntiFakeUrlStatus(
            self,
            request: models.ModifyAntiFakeUrlStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAntiFakeUrlStatusResponse:
        """
        切换防篡改开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAntiFakeUrlStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAntiFakeUrlStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAntiInfoLeakRuleStatus(
            self,
            request: models.ModifyAntiInfoLeakRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAntiInfoLeakRuleStatusResponse:
        """
        信息防泄漏切换规则开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAntiInfoLeakRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAntiInfoLeakRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAntiInfoLeakRules(
            self,
            request: models.ModifyAntiInfoLeakRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyAntiInfoLeakRulesResponse:
        """
        编辑信息防泄漏规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAntiInfoLeakRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAntiInfoLeakRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiAnalyzeStatus(
            self,
            request: models.ModifyApiAnalyzeStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApiAnalyzeStatusResponse:
        """
        api分析页面开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiAnalyzeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiAnalyzeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiSecEventChange(
            self,
            request: models.ModifyApiSecEventChangeRequest,
            opts: Dict = None,
    ) -> models.ModifyApiSecEventChangeResponse:
        """
        api安全状态变更接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiSecEventChange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiSecEventChangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiSecSensitiveRule(
            self,
            request: models.ModifyApiSecSensitiveRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyApiSecSensitiveRuleResponse:
        """
        修改api安全敏感检测规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiSecSensitiveRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiSecSensitiveRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAreaBanAreas(
            self,
            request: models.ModifyAreaBanAreasRequest,
            opts: Dict = None,
    ) -> models.ModifyAreaBanAreasResponse:
        """
        修改地域封禁中的地域信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAreaBanAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAreaBanAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAreaBanRule(
            self,
            request: models.ModifyAreaBanRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyAreaBanRuleResponse:
        """
        添加（编辑）地域封禁中的地域信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAreaBanRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAreaBanRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAreaBanStatus(
            self,
            request: models.ModifyAreaBanStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAreaBanStatusResponse:
        """
        修改防护域名的地域封禁状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAreaBanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAreaBanStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAttackWhiteRule(
            self,
            request: models.ModifyAttackWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyAttackWhiteRuleResponse:
        """
        供用户控制台调用，修改Tiga规则引擎白名单。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAttackWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAttackWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBatchIpAccessControl(
            self,
            request: models.ModifyBatchIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.ModifyBatchIpAccessControlResponse:
        """
        批量IP黑白名单新增接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBatchIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBatchIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBotIdRule(
            self,
            request: models.ModifyBotIdRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyBotIdRuleResponse:
        """
        修改Bot-ID规则配置1
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBotIdRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBotIdRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBotSceneStatus(
            self,
            request: models.ModifyBotSceneStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBotSceneStatusResponse:
        """
        bot子场景开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBotSceneStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBotSceneStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBotSceneUCBRule(
            self,
            request: models.ModifyBotSceneUCBRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyBotSceneUCBRuleResponse:
        """
        【接口复用】场景化后更新Bot的UCB自定义规则，两个调用位置：1.BOT全局白名单 2.BOT场景配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBotSceneUCBRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBotSceneUCBRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBotStatus(
            self,
            request: models.ModifyBotStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBotStatusResponse:
        """
        Bot_V2 bot总开关更新
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBotStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBotStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomRule(
            self,
            request: models.ModifyCustomRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomRuleResponse:
        """
        编辑自定义规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomRuleStatus(
            self,
            request: models.ModifyCustomRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomRuleStatusResponse:
        """
        开启或禁用访问控制（自定义策略）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomWhiteRule(
            self,
            request: models.ModifyCustomWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomWhiteRuleResponse:
        """
        编辑精准白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomWhiteRuleStatus(
            self,
            request: models.ModifyCustomWhiteRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomWhiteRuleStatusResponse:
        """
        开启或禁用精准白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomWhiteRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomWhiteRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainIpv6Status(
            self,
            request: models.ModifyDomainIpv6StatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainIpv6StatusResponse:
        """
        切换ipv6开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainIpv6Status"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainIpv6StatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainPostAction(
            self,
            request: models.ModifyDomainPostActionRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainPostActionResponse:
        """
        修改域名投递状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainPostAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainPostActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainWhiteRule(
            self,
            request: models.ModifyDomainWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainWhiteRuleResponse:
        """
        修改域名规则白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainsCLSStatus(
            self,
            request: models.ModifyDomainsCLSStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainsCLSStatusResponse:
        """
        修改域名列表的访问日志开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainsCLSStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainsCLSStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGenerateDeals(
            self,
            request: models.ModifyGenerateDealsRequest,
            opts: Dict = None,
    ) -> models.ModifyGenerateDealsResponse:
        """
        提供给clb等使用的waf实例下单接口，目前只支持clb旗舰版实例的下单，该接口会进行入参校验，然后调用是否为收购用户，然后调用计费接口下单。目前只支持预付费下单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGenerateDeals"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGenerateDealsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHost(
            self,
            request: models.ModifyHostRequest,
            opts: Dict = None,
    ) -> models.ModifyHostResponse:
        """
        编辑负载均衡型WAF防护域名配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostFlowMode(
            self,
            request: models.ModifyHostFlowModeRequest,
            opts: Dict = None,
    ) -> models.ModifyHostFlowModeResponse:
        """
        设置负载均衡型WAF防护域名的流量模式，切换镜像模式和清洗模式
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostFlowMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostFlowModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostMode(
            self,
            request: models.ModifyHostModeRequest,
            opts: Dict = None,
    ) -> models.ModifyHostModeResponse:
        """
        clb-waf设置防护域名防护状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostStatus(
            self,
            request: models.ModifyHostStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyHostStatusResponse:
        """
        clb-waf 设置防护域名WAF开关
        支持批量操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceAttackLogPost(
            self,
            request: models.ModifyInstanceAttackLogPostRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceAttackLogPostResponse:
        """
        修改实例攻击日志投递开关，企业版及以上版本可以开通，否则返回错误
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceAttackLogPost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceAttackLogPostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceElasticMode(
            self,
            request: models.ModifyInstanceElasticModeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceElasticModeResponse:
        """
        修改实例的QPS弹性计费开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceElasticMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceElasticModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceName(
            self,
            request: models.ModifyInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNameResponse:
        """
        修改实例的名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceQpsLimit(
            self,
            request: models.ModifyInstanceQpsLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceQpsLimitResponse:
        """
        设置套餐实例的弹性qps上限
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceQpsLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceQpsLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceRenewFlag(
            self,
            request: models.ModifyInstanceRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceRenewFlagResponse:
        """
        修改实例的自动续费开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIpAccessControl(
            self,
            request: models.ModifyIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.ModifyIpAccessControlResponse:
        """
        Waf IP黑白名单编辑接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleStatus(
            self,
            request: models.ModifyModuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleStatusResponse:
        """
        设置某个domain下基础安全模块的开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyObject(
            self,
            request: models.ModifyObjectRequest,
            opts: Dict = None,
    ) -> models.ModifyObjectResponse:
        """
        修改防护对象
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyObjects(
            self,
            request: models.ModifyObjectsRequest,
            opts: Dict = None,
    ) -> models.ModifyObjectsResponse:
        """
        批量修改防护对象
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwaspRuleStatus(
            self,
            request: models.ModifyOwaspRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyOwaspRuleStatusResponse:
        """
        更新规则的开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwaspRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwaspRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwaspRuleTypeAction(
            self,
            request: models.ModifyOwaspRuleTypeActionRequest,
            opts: Dict = None,
    ) -> models.ModifyOwaspRuleTypeActionResponse:
        """
        更新规则类型的防护模式
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwaspRuleTypeAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwaspRuleTypeActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwaspRuleTypeLevel(
            self,
            request: models.ModifyOwaspRuleTypeLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyOwaspRuleTypeLevelResponse:
        """
        更新规则类型的防护等级
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwaspRuleTypeLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwaspRuleTypeLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwaspRuleTypeStatus(
            self,
            request: models.ModifyOwaspRuleTypeStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyOwaspRuleTypeStatusResponse:
        """
        更新规则类型的开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwaspRuleTypeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwaspRuleTypeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwaspWhiteRule(
            self,
            request: models.ModifyOwaspWhiteRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyOwaspWhiteRuleResponse:
        """
        编辑规则引擎白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwaspWhiteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwaspWhiteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProtectionLevel(
            self,
            request: models.ModifyProtectionLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyProtectionLevelResponse:
        """
        更改防护等级
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProtectionLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProtectionLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProtectionStatus(
            self,
            request: models.ModifyProtectionStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyProtectionStatusResponse:
        """
        开启、关闭WAF开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProtectionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProtectionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySpartaProtection(
            self,
            request: models.ModifySpartaProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifySpartaProtectionResponse:
        """
        编辑SaaS型WAF域名配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySpartaProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySpartaProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySpartaProtectionMode(
            self,
            request: models.ModifySpartaProtectionModeRequest,
            opts: Dict = None,
    ) -> models.ModifySpartaProtectionModeResponse:
        """
        设置waf防护状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySpartaProtectionMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySpartaProtectionModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserLevel(
            self,
            request: models.ModifyUserLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyUserLevelResponse:
        """
        修改用户防护规则等级
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserSignatureClass(
            self,
            request: models.ModifyUserSignatureClassRequest,
            opts: Dict = None,
    ) -> models.ModifyUserSignatureClassResponse:
        """
        切换Tiga引擎规则类型的生效开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserSignatureClass"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserSignatureClassResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserSignatureRule(
            self,
            request: models.ModifyUserSignatureRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyUserSignatureRuleResponse:
        """
        修改用户防护规则，开启关闭具体的某条规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserSignatureRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserSignatureRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserSignatureRuleV2(
            self,
            request: models.ModifyUserSignatureRuleV2Request,
            opts: Dict = None,
    ) -> models.ModifyUserSignatureRuleV2Response:
        """
        修改用户防护规则，开启关闭具体的某条规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserSignatureRuleV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserSignatureRuleV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWafAutoDenyRules(
            self,
            request: models.ModifyWafAutoDenyRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyWafAutoDenyRulesResponse:
        """
        修改ip惩罚规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWafAutoDenyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWafAutoDenyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWafThreatenIntelligence(
            self,
            request: models.ModifyWafThreatenIntelligenceRequest,
            opts: Dict = None,
    ) -> models.ModifyWafThreatenIntelligenceResponse:
        """
        配置WAF威胁情报封禁模块详情
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWafThreatenIntelligence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWafThreatenIntelligenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebshellStatus(
            self,
            request: models.ModifyWebshellStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyWebshellStatusResponse:
        """
        设置域名的webshell状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebshellStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebshellStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PostAttackDownloadTask(
            self,
            request: models.PostAttackDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.PostAttackDownloadTaskResponse:
        """
        创建搜索下载攻击日志任务，使用CLS新版本的搜索下载getlog接口
        """
        
        kwargs = {}
        kwargs["action"] = "PostAttackDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PostAttackDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryBypassAllStatus(
            self,
            request: models.QueryBypassAllStatusRequest,
            opts: Dict = None,
    ) -> models.QueryBypassAllStatusResponse:
        """
        查询该用户是否被加入了全局的bypass列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryBypassAllStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryBypassAllStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshAccessCheckResult(
            self,
            request: models.RefreshAccessCheckResultRequest,
            opts: Dict = None,
    ) -> models.RefreshAccessCheckResultResponse:
        """
        刷新接入检查的结果，后台会生成接入检查任务
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshAccessCheckResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshAccessCheckResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveBypassAllRule(
            self,
            request: models.RemoveBypassAllRuleRequest,
            opts: Dict = None,
    ) -> models.RemoveBypassAllRuleResponse:
        """
        删除一键bypass规则
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveBypassAllRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveBypassAllRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchAccessLog(
            self,
            request: models.SearchAccessLogRequest,
            opts: Dict = None,
    ) -> models.SearchAccessLogResponse:
        """
        本接口用于搜索WAF访问日志
        """
        
        kwargs = {}
        kwargs["action"] = "SearchAccessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchAccessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchAttackLog(
            self,
            request: models.SearchAttackLogRequest,
            opts: Dict = None,
    ) -> models.SearchAttackLogResponse:
        """
        新版本CLS接口存在参数变化，query改成了query_string支持lucence语法接口搜索查询。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchAttackLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchAttackLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchLog(
            self,
            request: models.SearchLogRequest,
            opts: Dict = None,
    ) -> models.SearchLogResponse:
        """
        本接口用于检索分析日志，使用该接口时请注意如下事项：
        1. 该接口除受默认接口请求频率限制外，针对单个日志主题，查询并发数不能超过15。
        2. 检索语法建议使用CQL语法规则，请使用SyntaxRule参数，将值设置为1。
        3. API返回数据包最大49MB，建议启用 gzip 压缩（HTTP Request Header Accept-Encoding:gzip）。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDomainRules(
            self,
            request: models.SwitchDomainRulesRequest,
            opts: Dict = None,
    ) -> models.SwitchDomainRulesResponse:
        """
        切换域名的规则开关
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDomainRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDomainRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchElasticMode(
            self,
            request: models.SwitchElasticModeRequest,
            opts: Dict = None,
    ) -> models.SwitchElasticModeResponse:
        """
        切换弹性的开关
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchElasticMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchElasticModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProtectionModes(
            self,
            request: models.UpdateProtectionModesRequest,
            opts: Dict = None,
    ) -> models.UpdateProtectionModesResponse:
        """
        更新Tiga引擎下大类规则的防护模式
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProtectionModes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProtectionModesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRateLimitV2(
            self,
            request: models.UpdateRateLimitV2Request,
            opts: Dict = None,
    ) -> models.UpdateRateLimitV2Response:
        """
        更新自研版限流规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRateLimitV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRateLimitV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpsertCCAutoStatus(
            self,
            request: models.UpsertCCAutoStatusRequest,
            opts: Dict = None,
    ) -> models.UpsertCCAutoStatusResponse:
        """
        编辑SAAS型接入的紧急CC防护状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpsertCCAutoStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpsertCCAutoStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpsertCCRule(
            self,
            request: models.UpsertCCRuleRequest,
            opts: Dict = None,
    ) -> models.UpsertCCRuleResponse:
        """
        Waf  CC V2 Upsert接口
        """
        
        kwargs = {}
        kwargs["action"] = "UpsertCCRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpsertCCRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpsertIpAccessControl(
            self,
            request: models.UpsertIpAccessControlRequest,
            opts: Dict = None,
    ) -> models.UpsertIpAccessControlResponse:
        """
        Waf IP黑白名单Upsert接口（建议使用CreateIpAccessControl、ModifyIpAccessControl来替换当前接口）
        """
        
        kwargs = {}
        kwargs["action"] = "UpsertIpAccessControl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpsertIpAccessControlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpsertSession(
            self,
            request: models.UpsertSessionRequest,
            opts: Dict = None,
    ) -> models.UpsertSessionResponse:
        """
        Waf  会话定义 Upsert接口
        """
        
        kwargs = {}
        kwargs["action"] = "UpsertSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpsertSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)