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
from tencentcloud.cwp.v20180228 import models
from typing import Dict


class CwpClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'cwp.tencentcloudapi.com'
    _service = 'cwp'

    async def AddLoginWhiteLists(
            self,
            request: models.AddLoginWhiteListsRequest,
            opts: Dict = None,
    ) -> models.AddLoginWhiteListsResponse:
        """
        批量添加异地登录白名单
        """
        
        kwargs = {}
        kwargs["action"] = "AddLoginWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddLoginWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelIgnoreVul(
            self,
            request: models.CancelIgnoreVulRequest,
            opts: Dict = None,
    ) -> models.CancelIgnoreVulResponse:
        """
        产品变动切换到了\\n切换到 AddVulIgnoreRule / ModifyVulIgnoreRule  CancelVulIgnoreRule\\n相关接口

        取消漏洞忽略
        """
        
        kwargs = {}
        kwargs["action"] = "CancelIgnoreVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelIgnoreVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeRuleEventsIgnoreStatus(
            self,
            request: models.ChangeRuleEventsIgnoreStatusRequest,
            opts: Dict = None,
    ) -> models.ChangeRuleEventsIgnoreStatusResponse:
        """
        根据检测项id或事件id批量忽略事件或取消忽略
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeRuleEventsIgnoreStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeRuleEventsIgnoreStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeStrategyEnableStatus(
            self,
            request: models.ChangeStrategyEnableStatusRequest,
            opts: Dict = None,
    ) -> models.ChangeStrategyEnableStatusResponse:
        """
        根据策略id修改策略可用状态
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeStrategyEnableStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeStrategyEnableStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBashPolicyParams(
            self,
            request: models.CheckBashPolicyParamsRequest,
            opts: Dict = None,
    ) -> models.CheckBashPolicyParamsResponse:
        """
        校验高危命令用户规则新增和编辑时的参数。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBashPolicyParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBashPolicyParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckBashRuleParams(
            self,
            request: models.CheckBashRuleParamsRequest,
            opts: Dict = None,
    ) -> models.CheckBashRuleParamsResponse:
        """
        校验高危命令用户规则新增和编辑时的参数。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckBashRuleParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckBashRuleParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckFileTamperRule(
            self,
            request: models.CheckFileTamperRuleRequest,
            opts: Dict = None,
    ) -> models.CheckFileTamperRuleResponse:
        """
        检验核心文件监控前端新增和编辑时的规则参数。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckFileTamperRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckFileTamperRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckFirstScanBaseline(
            self,
            request: models.CheckFirstScanBaselineRequest,
            opts: Dict = None,
    ) -> models.CheckFirstScanBaselineResponse:
        """
        查询基线是否第一次检测
        """
        
        kwargs = {}
        kwargs["action"] = "CheckFirstScanBaseline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckFirstScanBaselineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckLogKafkaConnectionState(
            self,
            request: models.CheckLogKafkaConnectionStateRequest,
            opts: Dict = None,
    ) -> models.CheckLogKafkaConnectionStateResponse:
        """
        检查日志投递kafka连通性
        """
        
        kwargs = {}
        kwargs["action"] = "CheckLogKafkaConnectionState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckLogKafkaConnectionStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearLocalStorage(
            self,
            request: models.ClearLocalStorageRequest,
            opts: Dict = None,
    ) -> models.ClearLocalStorageResponse:
        """
        清理本地存储数据
        """
        
        kwargs = {}
        kwargs["action"] = "ClearLocalStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearLocalStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBanWhiteList(
            self,
            request: models.CreateBanWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateBanWhiteListResponse:
        """
        添加阻断白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBanWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBanWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaselineStrategy(
            self,
            request: models.CreateBaselineStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateBaselineStrategyResponse:
        """
        根据策略信息创建基线策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaselineStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaselineStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBuyBindTask(
            self,
            request: models.CreateBuyBindTaskRequest,
            opts: Dict = None,
    ) -> models.CreateBuyBindTaskResponse:
        """
        新购授权自动绑定任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBuyBindTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBuyBindTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmergencyVulScan(
            self,
            request: models.CreateEmergencyVulScanRequest,
            opts: Dict = None,
    ) -> models.CreateEmergencyVulScanResponse:
        """
        创建应急漏洞扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmergencyVulScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmergencyVulScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIncidentBacktracking(
            self,
            request: models.CreateIncidentBacktrackingRequest,
            opts: Dict = None,
    ) -> models.CreateIncidentBacktrackingResponse:
        """
        对旗舰版机器单次触发事件调查及告警回溯
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIncidentBacktracking"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIncidentBacktrackingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLicenseOrder(
            self,
            request: models.CreateLicenseOrderRequest,
            opts: Dict = None,
    ) -> models.CreateLicenseOrderResponse:
        """
        CreateLicenseOrder 该接口可以创建专业版/旗舰版订单
        支持预付费后付费创建
        后付费订单直接创建成功
        预付费订单仅下单不支付,需要调用计费支付接口进行支付
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLicenseOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLicenseOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLogExport(
            self,
            request: models.CreateLogExportRequest,
            opts: Dict = None,
    ) -> models.CreateLogExportResponse:
        """
        创建日志下载任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMaliciousRequestWhiteList(
            self,
            request: models.CreateMaliciousRequestWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateMaliciousRequestWhiteListResponse:
        """
        添加恶意请求白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMaliciousRequestWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMaliciousRequestWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMalwareWhiteList(
            self,
            request: models.CreateMalwareWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateMalwareWhiteListResponse:
        """
        创建木马白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMalwareWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMalwareWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetAttackWhiteList(
            self,
            request: models.CreateNetAttackWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateNetAttackWhiteListResponse:
        """
        创建网络攻击白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetAttackWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetAttackWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProtectServer(
            self,
            request: models.CreateProtectServerRequest,
            opts: Dict = None,
    ) -> models.CreateProtectServerResponse:
        """
        添加网站防护服务器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProtectServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProtectServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRansomDefenseStrategy(
            self,
            request: models.CreateRansomDefenseStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateRansomDefenseStrategyResponse:
        """
        创建或修改防勒索策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRansomDefenseStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRansomDefenseStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScanMalwareSetting(
            self,
            request: models.CreateScanMalwareSettingRequest,
            opts: Dict = None,
    ) -> models.CreateScanMalwareSettingResponse:
        """
        该接口可以对入侵检测-文件查杀扫描检测
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScanMalwareSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScanMalwareSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSearchLog(
            self,
            request: models.CreateSearchLogRequest,
            opts: Dict = None,
    ) -> models.CreateSearchLogResponse:
        """
        添加历史搜索记录
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSearchTemplate(
            self,
            request: models.CreateSearchTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSearchTemplateResponse:
        """
        添加检索模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSearchTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSearchTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulFix(
            self,
            request: models.CreateVulFixRequest,
            opts: Dict = None,
    ) -> models.CreateVulFixResponse:
        """
        提交漏洞修护
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulFix"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulFixResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWhiteListOrder(
            self,
            request: models.CreateWhiteListOrderRequest,
            opts: Dict = None,
    ) -> models.CreateWhiteListOrderResponse:
        """
        该接口可以创建白名单订单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWhiteListOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWhiteListOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAllJavaMemShells(
            self,
            request: models.DeleteAllJavaMemShellsRequest,
            opts: Dict = None,
    ) -> models.DeleteAllJavaMemShellsResponse:
        """
        删除全部java内存马事件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAllJavaMemShells"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAllJavaMemShellsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBanWhiteList(
            self,
            request: models.DeleteBanWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteBanWhiteListResponse:
        """
        删除阻断白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBanWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBanWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBaselinePolicy(
            self,
            request: models.DeleteBaselinePolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteBaselinePolicyResponse:
        """
        删除基线策略配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBaselinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBaselinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBaselineRule(
            self,
            request: models.DeleteBaselineRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteBaselineRuleResponse:
        """
        删除基线规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBaselineRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBaselineRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBaselineRuleIgnore(
            self,
            request: models.DeleteBaselineRuleIgnoreRequest,
            opts: Dict = None,
    ) -> models.DeleteBaselineRuleIgnoreResponse:
        """
        删除基线忽略规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBaselineRuleIgnore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBaselineRuleIgnoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBaselineStrategy(
            self,
            request: models.DeleteBaselineStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteBaselineStrategyResponse:
        """
        根据基线策略id删除策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBaselineStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBaselineStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBaselineWeakPassword(
            self,
            request: models.DeleteBaselineWeakPasswordRequest,
            opts: Dict = None,
    ) -> models.DeleteBaselineWeakPasswordResponse:
        """
        删除基线弱口令
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBaselineWeakPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBaselineWeakPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBashEvents(
            self,
            request: models.DeleteBashEventsRequest,
            opts: Dict = None,
    ) -> models.DeleteBashEventsResponse:
        """
        根据Ids删除高危命令事件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBashEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBashEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBashPolicies(
            self,
            request: models.DeleteBashPoliciesRequest,
            opts: Dict = None,
    ) -> models.DeleteBashPoliciesResponse:
        """
        删除高危命令策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBashPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBashPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBashRules(
            self,
            request: models.DeleteBashRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteBashRulesResponse:
        """
        删除高危命令规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBruteAttacks(
            self,
            request: models.DeleteBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.DeleteBruteAttacksResponse:
        """
        本接口 (DeleteBruteAttacks) 用于删除暴力破解记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLicenseRecord(
            self,
            request: models.DeleteLicenseRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteLicenseRecordResponse:
        """
        对授权管理-订单列表内已过期的订单进行删除.(删除后的订单不在统计范畴内)
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLicenseRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLicenseRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLicenseRecordAll(
            self,
            request: models.DeleteLicenseRecordAllRequest,
            opts: Dict = None,
    ) -> models.DeleteLicenseRecordAllResponse:
        """
        删除授权全部记录
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLicenseRecordAll"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLicenseRecordAllResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogExport(
            self,
            request: models.DeleteLogExportRequest,
            opts: Dict = None,
    ) -> models.DeleteLogExportResponse:
        """
        删除日志下载任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoginWhiteList(
            self,
            request: models.DeleteLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteLoginWhiteListResponse:
        """
        本接口用于删除异地登录白名单规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachine(
            self,
            request: models.DeleteMachineRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineResponse:
        """
        本接口（DeleteMachine）用于卸载主机安全客户端。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineClearHistory(
            self,
            request: models.DeleteMachineClearHistoryRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineClearHistoryResponse:
        """
        删除机器清理记录
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineClearHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineClearHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineTag(
            self,
            request: models.DeleteMachineTagRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineTagResponse:
        """
        删除服务器关联的标签
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMaliciousRequestWhiteList(
            self,
            request: models.DeleteMaliciousRequestWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteMaliciousRequestWhiteListResponse:
        """
        删除恶意请求白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMaliciousRequestWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMaliciousRequestWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMaliciousRequests(
            self,
            request: models.DeleteMaliciousRequestsRequest,
            opts: Dict = None,
    ) -> models.DeleteMaliciousRequestsResponse:
        """
        本接口 (DeleteMaliciousRequests) 用于删除恶意请求记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMaliciousRequests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMaliciousRequestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMalwareScanTask(
            self,
            request: models.DeleteMalwareScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteMalwareScanTaskResponse:
        """
        入侵管理-终止扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMalwareScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMalwareScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMalwareWhiteList(
            self,
            request: models.DeleteMalwareWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteMalwareWhiteListResponse:
        """
        删除木马白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMalwareWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMalwareWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMalwares(
            self,
            request: models.DeleteMalwaresRequest,
            opts: Dict = None,
    ) -> models.DeleteMalwaresResponse:
        """
        本接口 (DeleteMalwares) 用于删除木马记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetAttackWhiteList(
            self,
            request: models.DeleteNetAttackWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteNetAttackWhiteListResponse:
        """
        删除网络攻击白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetAttackWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetAttackWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNonlocalLoginPlaces(
            self,
            request: models.DeleteNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DeleteNonlocalLoginPlacesResponse:
        """
        本接口 (DeleteNonlocalLoginPlaces) 用于删除异地登录记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivilegeEvents(
            self,
            request: models.DeletePrivilegeEventsRequest,
            opts: Dict = None,
    ) -> models.DeletePrivilegeEventsResponse:
        """
        根据Ids删除本地提权
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivilegeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivilegeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivilegeRules(
            self,
            request: models.DeletePrivilegeRulesRequest,
            opts: Dict = None,
    ) -> models.DeletePrivilegeRulesResponse:
        """
        删除本地提权规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivilegeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivilegeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProtectDir(
            self,
            request: models.DeleteProtectDirRequest,
            opts: Dict = None,
    ) -> models.DeleteProtectDirResponse:
        """
        删除防护网站
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProtectDir"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProtectDirResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRaspRules(
            self,
            request: models.DeleteRaspRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteRaspRulesResponse:
        """
        删除漏洞防御白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRaspRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRaspRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReverseShellEvents(
            self,
            request: models.DeleteReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.DeleteReverseShellEventsResponse:
        """
        根据Ids删除反弹Shell事件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReverseShellRules(
            self,
            request: models.DeleteReverseShellRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteReverseShellRulesResponse:
        """
        删除反弹Shell规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReverseShellRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReverseShellRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRiskDnsEvent(
            self,
            request: models.DeleteRiskDnsEventRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskDnsEventResponse:
        """
        删除恶意请求事件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskDnsEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskDnsEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRiskDnsPolicy(
            self,
            request: models.DeleteRiskDnsPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskDnsPolicyResponse:
        """
        删除恶意请求策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskDnsPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskDnsPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScanTask(
            self,
            request: models.DeleteScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteScanTaskResponse:
        """
        DeleteScanTask 该接口可以对指定类型的扫描任务进行停止扫描;
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSearchTemplate(
            self,
            request: models.DeleteSearchTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSearchTemplateResponse:
        """
        删除检索模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSearchTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSearchTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTags(
            self,
            request: models.DeleteTagsRequest,
            opts: Dict = None,
    ) -> models.DeleteTagsResponse:
        """
        删除标签
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebHookPolicy(
            self,
            request: models.DeleteWebHookPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteWebHookPolicyResponse:
        """
        删除告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebHookPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebHookPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebHookReceiver(
            self,
            request: models.DeleteWebHookReceiverRequest,
            opts: Dict = None,
    ) -> models.DeleteWebHookReceiverResponse:
        """
        删除告警接收人
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebHookReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebHookReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebHookRule(
            self,
            request: models.DeleteWebHookRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteWebHookRuleResponse:
        """
        删除企微机器人规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebHookRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebHookRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebPageEventLog(
            self,
            request: models.DeleteWebPageEventLogRequest,
            opts: Dict = None,
    ) -> models.DeleteWebPageEventLogResponse:
        """
        网站防篡改-删除事件记录
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebPageEventLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebPageEventLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeABTestConfig(
            self,
            request: models.DescribeABTestConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeABTestConfigResponse:
        """
        获取用户当前灰度配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeABTestConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeABTestConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAESKey(
            self,
            request: models.DescribeAESKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeAESKeyResponse:
        """
        获取配置的aeskey和aesiv
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAESKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAESKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountStatistics(
            self,
            request: models.DescribeAccountStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountStatisticsResponse:
        """
        本接口 (DescribeAccountStatistics) 用于获取账号统计列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentInstallCommand(
            self,
            request: models.DescribeAgentInstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentInstallCommandResponse:
        """
        获取agent安装命令
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentInstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentInstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentInstallationToken(
            self,
            request: models.DescribeAgentInstallationTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentInstallationTokenResponse:
        """
        混合云安装agent token获取
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentInstallationToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentInstallationTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmIncidentNodes(
            self,
            request: models.DescribeAlarmIncidentNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmIncidentNodesResponse:
        """
        获取告警点所在事件的所有节点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmIncidentNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmIncidentNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmVertexId(
            self,
            request: models.DescribeAlarmVertexIdRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmVertexIdResponse:
        """
        查询告警点id列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmVertexId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmVertexIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetAppCount(
            self,
            request: models.DescribeAssetAppCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetAppCountResponse:
        """
        获取所有软件应用数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetAppCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetAppCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetAppList(
            self,
            request: models.DescribeAssetAppListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetAppListResponse:
        """
        查询应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetAppProcessList(
            self,
            request: models.DescribeAssetAppProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetAppProcessListResponse:
        """
        获取软件关联进程列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetAppProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetAppProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetCoreModuleInfo(
            self,
            request: models.DescribeAssetCoreModuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetCoreModuleInfoResponse:
        """
        获取内核模块详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetCoreModuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetCoreModuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetCoreModuleList(
            self,
            request: models.DescribeAssetCoreModuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetCoreModuleListResponse:
        """
        查询资产管理内核模块列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetCoreModuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetCoreModuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDatabaseCount(
            self,
            request: models.DescribeAssetDatabaseCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDatabaseCountResponse:
        """
        获取所有数据库数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDatabaseCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDatabaseCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDatabaseInfo(
            self,
            request: models.DescribeAssetDatabaseInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDatabaseInfoResponse:
        """
        获取资产管理数据库详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDatabaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDatabaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDatabaseList(
            self,
            request: models.DescribeAssetDatabaseListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDatabaseListResponse:
        """
        查询资产管理数据库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDatabaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDatabaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDiskList(
            self,
            request: models.DescribeAssetDiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDiskListResponse:
        """
        获取主机磁盘分区列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetEnvList(
            self,
            request: models.DescribeAssetEnvListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetEnvListResponse:
        """
        查询资产管理环境变量列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetEnvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetEnvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetHostTotalCount(
            self,
            request: models.DescribeAssetHostTotalCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetHostTotalCountResponse:
        """
        获取主机所有资源数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetHostTotalCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetHostTotalCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetInfo(
            self,
            request: models.DescribeAssetInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetInfoResponse:
        """
        获取资产数量： 主机数、账号数、端口数、进程数、软件数、数据库数、Web应用数、Web框架数、Web服务数、Web站点数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetInitServiceList(
            self,
            request: models.DescribeAssetInitServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetInitServiceListResponse:
        """
        查询资产管理启动服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetInitServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetInitServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetJarInfo(
            self,
            request: models.DescribeAssetJarInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetJarInfoResponse:
        """
        获取Jar包详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetJarInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetJarInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetJarList(
            self,
            request: models.DescribeAssetJarListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetJarListResponse:
        """
        查询Jar包列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetJarList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetJarListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetLoadInfo(
            self,
            request: models.DescribeAssetLoadInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetLoadInfoResponse:
        """
        获取系统负载、内存使用率、硬盘使用率情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetLoadInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetLoadInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetMachineDetail(
            self,
            request: models.DescribeAssetMachineDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetMachineDetailResponse:
        """
        获取资产管理主机资源详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetMachineDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetMachineDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetMachineList(
            self,
            request: models.DescribeAssetMachineListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetMachineListResponse:
        """
        获取资产指纹页面的资源监控列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetMachineTagTop(
            self,
            request: models.DescribeAssetMachineTagTopRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetMachineTagTopResponse:
        """
        获取主机标签Top5
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetMachineTagTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetMachineTagTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetPlanTaskList(
            self,
            request: models.DescribeAssetPlanTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetPlanTaskListResponse:
        """
        查询资产管理计划任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetPlanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetPlanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetPortCount(
            self,
            request: models.DescribeAssetPortCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetPortCountResponse:
        """
        获取所有端口数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetPortCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetPortCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetPortInfoList(
            self,
            request: models.DescribeAssetPortInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetPortInfoListResponse:
        """
        获取资产管理端口列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetPortInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetPortInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetProcessCount(
            self,
            request: models.DescribeAssetProcessCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetProcessCountResponse:
        """
        获取所有进程数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetProcessCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetProcessCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetProcessInfoList(
            self,
            request: models.DescribeAssetProcessInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetProcessInfoListResponse:
        """
        获取资产管理进程列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetProcessInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetProcessInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetRecentMachineInfo(
            self,
            request: models.DescribeAssetRecentMachineInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetRecentMachineInfoResponse:
        """
        获取主机最近趋势情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetRecentMachineInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetRecentMachineInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSystemPackageList(
            self,
            request: models.DescribeAssetSystemPackageListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSystemPackageListResponse:
        """
        获取资产管理系统安装包列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSystemPackageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSystemPackageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTotalCount(
            self,
            request: models.DescribeAssetTotalCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTotalCountResponse:
        """
        获取所有资源数量：主机、账号、端口、进程、软件、数据库、Web应用、Web框架、Web服务、Web站点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTotalCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTotalCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTypeTop(
            self,
            request: models.DescribeAssetTypeTopRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTypeTopResponse:
        """
        获取各种类型资源Top5
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTypeTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTypeTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTypes(
            self,
            request: models.DescribeAssetTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTypesResponse:
        """
        获取资产指纹类型列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetUserCount(
            self,
            request: models.DescribeAssetUserCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetUserCountResponse:
        """
        获取所有账号数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetUserCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetUserCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetUserInfo(
            self,
            request: models.DescribeAssetUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetUserInfoResponse:
        """
        获取主机账号详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetUserKeyList(
            self,
            request: models.DescribeAssetUserKeyListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetUserKeyListResponse:
        """
        获取主机账号Key列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetUserKeyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetUserKeyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetUserList(
            self,
            request: models.DescribeAssetUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetUserListResponse:
        """
        获取账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebAppCount(
            self,
            request: models.DescribeAssetWebAppCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebAppCountResponse:
        """
        获取所有Web应用数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebAppCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebAppCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebAppList(
            self,
            request: models.DescribeAssetWebAppListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebAppListResponse:
        """
        获取资产管理Web应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebAppPluginList(
            self,
            request: models.DescribeAssetWebAppPluginListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebAppPluginListResponse:
        """
        获取资产管理Web应用插件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebAppPluginList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebAppPluginListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebFrameCount(
            self,
            request: models.DescribeAssetWebFrameCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebFrameCountResponse:
        """
        获取所有Web框架数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebFrameCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebFrameCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebFrameList(
            self,
            request: models.DescribeAssetWebFrameListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebFrameListResponse:
        """
        获取资产管理Web框架列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebFrameList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebFrameListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebLocationCount(
            self,
            request: models.DescribeAssetWebLocationCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebLocationCountResponse:
        """
        获取所有Web站点数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebLocationCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebLocationCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebLocationInfo(
            self,
            request: models.DescribeAssetWebLocationInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebLocationInfoResponse:
        """
        获取Web站点详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebLocationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebLocationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebLocationList(
            self,
            request: models.DescribeAssetWebLocationListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebLocationListResponse:
        """
        获取Web站点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebLocationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebLocationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebLocationPathList(
            self,
            request: models.DescribeAssetWebLocationPathListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebLocationPathListResponse:
        """
        获取Web站点虚拟目录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebLocationPathList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebLocationPathListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebServiceCount(
            self,
            request: models.DescribeAssetWebServiceCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebServiceCountResponse:
        """
        获取所有Web服务数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebServiceCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebServiceCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebServiceInfoList(
            self,
            request: models.DescribeAssetWebServiceInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebServiceInfoListResponse:
        """
        查询资产管理Web服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebServiceInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebServiceInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebServiceProcessList(
            self,
            request: models.DescribeAssetWebServiceProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebServiceProcessListResponse:
        """
        获取Web服务关联进程列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebServiceProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebServiceProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackEventInfo(
            self,
            request: models.DescribeAttackEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackEventInfoResponse:
        """
        网络攻击事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackEvents(
            self,
            request: models.DescribeAttackEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackEventsResponse:
        """
        按分页形式展示网络攻击检测事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackStatistics(
            self,
            request: models.DescribeAttackStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackStatisticsResponse:
        """
        网络攻击数据统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackTop(
            self,
            request: models.DescribeAttackTopRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackTopResponse:
        """
        网络攻击top5数据列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackTrends(
            self,
            request: models.DescribeAttackTrendsRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackTrendsResponse:
        """
        网络攻击趋势数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackTrends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackTrendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttackVulTypeList(
            self,
            request: models.DescribeAttackVulTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeAttackVulTypeListResponse:
        """
        获取网络攻击威胁类型列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttackVulTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttackVulTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableExpertServiceDetail(
            self,
            request: models.DescribeAvailableExpertServiceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableExpertServiceDetailResponse:
        """
        专家服务-可用订单详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableExpertServiceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableExpertServiceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBanMode(
            self,
            request: models.DescribeBanModeRequest,
            opts: Dict = None,
    ) -> models.DescribeBanModeResponse:
        """
        获取爆破阻断模式
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBanMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBanModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBanRegions(
            self,
            request: models.DescribeBanRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeBanRegionsResponse:
        """
        获取阻断地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBanRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBanRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBanStatus(
            self,
            request: models.DescribeBanStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBanStatusResponse:
        """
        获取阻断按钮状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBanStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBanWhiteList(
            self,
            request: models.DescribeBanWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeBanWhiteListResponse:
        """
        获取阻断白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBanWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBanWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineAnalysisData(
            self,
            request: models.DescribeBaselineAnalysisDataRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineAnalysisDataResponse:
        """
        根据基线策略id查询基线策略数据概览统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineAnalysisData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineAnalysisDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineBasicInfo(
            self,
            request: models.DescribeBaselineBasicInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineBasicInfoResponse:
        """
        查询基线基础信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineBasicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineBasicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineDefaultStrategyList(
            self,
            request: models.DescribeBaselineDefaultStrategyListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineDefaultStrategyListResponse:
        """
        查询基线默认策略列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineDefaultStrategyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineDefaultStrategyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineDetail(
            self,
            request: models.DescribeBaselineDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineDetailResponse:
        """
        根据基线id查询基线详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineDetectList(
            self,
            request: models.DescribeBaselineDetectListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineDetectListResponse:
        """
        获取基线检测详情记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineDetectOverview(
            self,
            request: models.DescribeBaselineDetectOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineDetectOverviewResponse:
        """
        获取基线检测概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineDetectOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineDetectOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineDownloadList(
            self,
            request: models.DescribeBaselineDownloadListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineDownloadListResponse:
        """
        获取基线下载列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineDownloadList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineDownloadListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineEffectHostList(
            self,
            request: models.DescribeBaselineEffectHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineEffectHostListResponse:
        """
        根据基线id查询基线影响主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineFixList(
            self,
            request: models.DescribeBaselineFixListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineFixListResponse:
        """
        获取基线修复列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineFixList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineFixListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineHostDetectList(
            self,
            request: models.DescribeBaselineHostDetectListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineHostDetectListResponse:
        """
        获取基线检测主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineHostDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineHostDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineHostIgnoreList(
            self,
            request: models.DescribeBaselineHostIgnoreListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineHostIgnoreListResponse:
        """
        获取忽略规则主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineHostIgnoreList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineHostIgnoreListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineHostRiskTop(
            self,
            request: models.DescribeBaselineHostRiskTopRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineHostRiskTopResponse:
        """
        获取基线服务器风险TOP5
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineHostRiskTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineHostRiskTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineHostTop(
            self,
            request: models.DescribeBaselineHostTopRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineHostTopResponse:
        """
        接口返回TopN的风险服务器
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineHostTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineHostTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineItemDetectList(
            self,
            request: models.DescribeBaselineItemDetectListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineItemDetectListResponse:
        """
        获取基线检测项的列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineItemDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineItemDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineItemIgnoreList(
            self,
            request: models.DescribeBaselineItemIgnoreListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineItemIgnoreListResponse:
        """
        获取忽略规则项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineItemIgnoreList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineItemIgnoreListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineItemInfo(
            self,
            request: models.DescribeBaselineItemInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineItemInfoResponse:
        """
        获取基线检测项信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineItemInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineItemInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineItemList(
            self,
            request: models.DescribeBaselineItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineItemListResponse:
        """
        获取基线项检测结果列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineItemRiskTop(
            self,
            request: models.DescribeBaselineItemRiskTopRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineItemRiskTopResponse:
        """
        获取基线检测项TOP5
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineItemRiskTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineItemRiskTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineList(
            self,
            request: models.DescribeBaselineListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineListResponse:
        """
        查询基线列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselinePolicyList(
            self,
            request: models.DescribeBaselinePolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselinePolicyListResponse:
        """
        获取基线策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselinePolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselinePolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineRule(
            self,
            request: models.DescribeBaselineRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineRuleResponse:
        """
        根据基线id查询下属检测项信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineRuleCategoryList(
            self,
            request: models.DescribeBaselineRuleCategoryListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineRuleCategoryListResponse:
        """
        获取基线分类列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineRuleCategoryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineRuleCategoryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineRuleDetectList(
            self,
            request: models.DescribeBaselineRuleDetectListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineRuleDetectListResponse:
        """
        获取基线规则检测列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineRuleDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineRuleDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineRuleIgnoreList(
            self,
            request: models.DescribeBaselineRuleIgnoreListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineRuleIgnoreListResponse:
        """
        获取基线忽略规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineRuleIgnoreList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineRuleIgnoreListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineRuleList(
            self,
            request: models.DescribeBaselineRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineRuleListResponse:
        """
        获取基线规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineScanSchedule(
            self,
            request: models.DescribeBaselineScanScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineScanScheduleResponse:
        """
        根据任务id查询基线检测进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineScanSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineScanScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineStrategyDetail(
            self,
            request: models.DescribeBaselineStrategyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineStrategyDetailResponse:
        """
        根据基线策略id查询策略详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineStrategyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineStrategyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineStrategyList(
            self,
            request: models.DescribeBaselineStrategyListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineStrategyListResponse:
        """
        查询一个用户下的基线策略信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineStrategyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineStrategyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineTop(
            self,
            request: models.DescribeBaselineTopRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineTopResponse:
        """
        根据策略id查询基线检测项TOP
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineWeakPasswordList(
            self,
            request: models.DescribeBaselineWeakPasswordListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineWeakPasswordListResponse:
        """
        获取基线弱口令列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineWeakPasswordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineWeakPasswordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashEvents(
            self,
            request: models.DescribeBashEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeBashEventsResponse:
        """
        获取高危命令列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashEventsInfo(
            self,
            request: models.DescribeBashEventsInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeBashEventsInfoResponse:
        """
        查询高危命令事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashEventsInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashEventsInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashEventsInfoNew(
            self,
            request: models.DescribeBashEventsInfoNewRequest,
            opts: Dict = None,
    ) -> models.DescribeBashEventsInfoNewResponse:
        """
        查询高危命令事件详情(新)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashEventsInfoNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashEventsInfoNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashEventsNew(
            self,
            request: models.DescribeBashEventsNewRequest,
            opts: Dict = None,
    ) -> models.DescribeBashEventsNewResponse:
        """
        获取高危命令列表(新)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashEventsNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashEventsNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashPolicies(
            self,
            request: models.DescribeBashPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeBashPoliciesResponse:
        """
        获取高危命令策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBashRules(
            self,
            request: models.DescribeBashRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBashRulesResponse:
        """
        获取高危命令规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBruteAttackList(
            self,
            request: models.DescribeBruteAttackListRequest,
            opts: Dict = None,
    ) -> models.DescribeBruteAttackListResponse:
        """
        获取密码破解列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBruteAttackList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBruteAttackListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBruteAttackRules(
            self,
            request: models.DescribeBruteAttackRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBruteAttackRulesResponse:
        """
        获取爆破破解规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBruteAttackRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBruteAttackRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCanFixVulMachine(
            self,
            request: models.DescribeCanFixVulMachineRequest,
            opts: Dict = None,
    ) -> models.DescribeCanFixVulMachineResponse:
        """
        漏洞修护-查询可修护主机信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCanFixVulMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCanFixVulMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCanNotSeparateMachine(
            self,
            request: models.DescribeCanNotSeparateMachineRequest,
            opts: Dict = None,
    ) -> models.DescribeCanNotSeparateMachineResponse:
        """
        获取木马不可隔离的主机
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCanNotSeparateMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCanNotSeparateMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientException(
            self,
            request: models.DescribeClientExceptionRequest,
            opts: Dict = None,
    ) -> models.DescribeClientExceptionResponse:
        """
        获取客户端异常事件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientException"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientExceptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefenceEventDetail(
            self,
            request: models.DescribeDefenceEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDefenceEventDetailResponse:
        """
        获取漏洞防御事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefenceEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefenceEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnectInstallCommand(
            self,
            request: models.DescribeDirectConnectInstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectInstallCommandResponse:
        """
        获取专线agent安装命令，包含token
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnectInstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectInstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeESAggregations(
            self,
            request: models.DescribeESAggregationsRequest,
            opts: Dict = None,
    ) -> models.DescribeESAggregationsResponse:
        """
        获取ES字段聚合结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeESAggregations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeESAggregationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEmergencyResponseList(
            self,
            request: models.DescribeEmergencyResponseListRequest,
            opts: Dict = None,
    ) -> models.DescribeEmergencyResponseListResponse:
        """
        专家服务-应急响应列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEmergencyResponseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEmergencyResponseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEmergencyVulList(
            self,
            request: models.DescribeEmergencyVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeEmergencyVulListResponse:
        """
        获取应急漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEmergencyVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEmergencyVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventByTable(
            self,
            request: models.DescribeEventByTableRequest,
            opts: Dict = None,
    ) -> models.DescribeEventByTableResponse:
        """
        根据事件表名和id查询告警事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventByTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventByTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExpertServiceList(
            self,
            request: models.DescribeExpertServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeExpertServiceListResponse:
        """
        专家服务-安全管家列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExpertServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExpertServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExpertServiceOrderList(
            self,
            request: models.DescribeExpertServiceOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeExpertServiceOrderListResponse:
        """
        专家服务-专家服务订单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExpertServiceOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExpertServiceOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportMachines(
            self,
            request: models.DescribeExportMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeExportMachinesResponse:
        """
        本接口 (DescribeExportMachines) 用于导出区域主机列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFastAnalysis(
            self,
            request: models.DescribeFastAnalysisRequest,
            opts: Dict = None,
    ) -> models.DescribeFastAnalysisResponse:
        """
        日志快速分析统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFastAnalysis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFastAnalysisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTamperEventRuleInfo(
            self,
            request: models.DescribeFileTamperEventRuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTamperEventRuleInfoResponse:
        """
        查看产生事件时规则详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTamperEventRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTamperEventRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTamperEvents(
            self,
            request: models.DescribeFileTamperEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTamperEventsResponse:
        """
        核心文件监控事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTamperEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTamperEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTamperRuleCount(
            self,
            request: models.DescribeFileTamperRuleCountRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTamperRuleCountResponse:
        """
        查询主机关联文件监控规则数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTamperRuleCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTamperRuleCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTamperRuleInfo(
            self,
            request: models.DescribeFileTamperRuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTamperRuleInfoResponse:
        """
        查询某个监控规则的详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTamperRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTamperRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileTamperRules(
            self,
            request: models.DescribeFileTamperRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeFileTamperRulesResponse:
        """
        核心文件监控规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileTamperRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileTamperRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralStat(
            self,
            request: models.DescribeGeneralStatRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralStatResponse:
        """
        获取主机相关统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHistoryAccounts(
            self,
            request: models.DescribeHistoryAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeHistoryAccountsResponse:
        """
        本接口 (DescribeHistoryAccounts) 用于获取账号变更历史列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHistoryAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHistoryAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHistoryService(
            self,
            request: models.DescribeHistoryServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeHistoryServiceResponse:
        """
        查询日志检索服务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHistoryService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHistoryServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostInfo(
            self,
            request: models.DescribeHostInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeHostInfoResponse:
        """
        主机信息与标签信息查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostLoginList(
            self,
            request: models.DescribeHostLoginListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostLoginListResponse:
        """
        获取异常登录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostLoginList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostLoginListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHotVulTop(
            self,
            request: models.DescribeHotVulTopRequest,
            opts: Dict = None,
    ) -> models.DescribeHotVulTopResponse:
        """
        获取全网热点漏洞
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHotVulTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHotVulTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIgnoreBaselineRule(
            self,
            request: models.DescribeIgnoreBaselineRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeIgnoreBaselineRuleResponse:
        """
        查询已经忽略的检测项信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIgnoreBaselineRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIgnoreBaselineRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIgnoreHostAndItemConfig(
            self,
            request: models.DescribeIgnoreHostAndItemConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeIgnoreHostAndItemConfigResponse:
        """
        获取一键忽略受影响的检测项和主机信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIgnoreHostAndItemConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIgnoreHostAndItemConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIgnoreRuleEffectHostList(
            self,
            request: models.DescribeIgnoreRuleEffectHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeIgnoreRuleEffectHostListResponse:
        """
        根据检测项id与筛选条件查询忽略检测项影响主机列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIgnoreRuleEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIgnoreRuleEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImportMachineInfo(
            self,
            request: models.DescribeImportMachineInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeImportMachineInfoResponse:
        """
        查询批量导入机器信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImportMachineInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImportMachineInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJavaMemShellInfo(
            self,
            request: models.DescribeJavaMemShellInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeJavaMemShellInfoResponse:
        """
        查询java内存马事件详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJavaMemShellInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJavaMemShellInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJavaMemShellList(
            self,
            request: models.DescribeJavaMemShellListRequest,
            opts: Dict = None,
    ) -> models.DescribeJavaMemShellListResponse:
        """
        查询java内存马事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJavaMemShellList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJavaMemShellListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJavaMemShellPluginInfo(
            self,
            request: models.DescribeJavaMemShellPluginInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeJavaMemShellPluginInfoResponse:
        """
        查询给定主机java内存马插件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJavaMemShellPluginInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJavaMemShellPluginInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJavaMemShellPluginList(
            self,
            request: models.DescribeJavaMemShellPluginListRequest,
            opts: Dict = None,
    ) -> models.DescribeJavaMemShellPluginListResponse:
        """
        查询java内存马插件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJavaMemShellPluginList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJavaMemShellPluginListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicense(
            self,
            request: models.DescribeLicenseRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseResponse:
        """
        查询授权信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseBindList(
            self,
            request: models.DescribeLicenseBindListRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseBindListResponse:
        """
        该接口可以获取设置中心-授权管理,某个授权下已绑定的授权机器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseBindList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseBindListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseBindSchedule(
            self,
            request: models.DescribeLicenseBindScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseBindScheduleResponse:
        """
        查询授权绑定任务的进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseBindSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseBindScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseGeneral(
            self,
            request: models.DescribeLicenseGeneralRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseGeneralResponse:
        """
        授权管理-授权概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseGeneral"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseGeneralResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseList(
            self,
            request: models.DescribeLicenseListRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseListResponse:
        """
        获取用户所有授权订单信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseWhiteConfig(
            self,
            request: models.DescribeLicenseWhiteConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseWhiteConfigResponse:
        """
        查询授权白名单的可用配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseWhiteConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseWhiteConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogDeliveryKafkaOptions(
            self,
            request: models.DescribeLogDeliveryKafkaOptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogDeliveryKafkaOptionsResponse:
        """
        查询日志投递kafka可选项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogDeliveryKafkaOptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogDeliveryKafkaOptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogExports(
            self,
            request: models.DescribeLogExportsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogExportsResponse:
        """
        获取日志下载任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogExports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogExportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogHistogram(
            self,
            request: models.DescribeLogHistogramRequest,
            opts: Dict = None,
    ) -> models.DescribeLogHistogramResponse:
        """
        获取日志直方图信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogHistogram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogHistogramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogIndex(
            self,
            request: models.DescribeLogIndexRequest,
            opts: Dict = None,
    ) -> models.DescribeLogIndexResponse:
        """
        查询索引
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogKafkaDeliverInfo(
            self,
            request: models.DescribeLogKafkaDeliverInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLogKafkaDeliverInfoResponse:
        """
        获取kafka投递信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogKafkaDeliverInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogKafkaDeliverInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogStorageConfig(
            self,
            request: models.DescribeLogStorageConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeLogStorageConfigResponse:
        """
        获取日志存储配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogStorageConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogStorageConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogStorageRecord(
            self,
            request: models.DescribeLogStorageRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeLogStorageRecordResponse:
        """
        获取日志存储量记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogStorageRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogStorageRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogStorageStatistic(
            self,
            request: models.DescribeLogStorageStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeLogStorageStatisticResponse:
        """
        获取日志检索容量使用统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogStorageStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogStorageStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogType(
            self,
            request: models.DescribeLogTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeLogTypeResponse:
        """
        日志分析功能-获取日志类型，使用该接口返回的结果暂时可过滤的日志类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginWhiteCombinedList(
            self,
            request: models.DescribeLoginWhiteCombinedListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginWhiteCombinedListResponse:
        """
        获取异地登录白名单合并后列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginWhiteCombinedList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginWhiteCombinedListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginWhiteHostList(
            self,
            request: models.DescribeLoginWhiteHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginWhiteHostListResponse:
        """
        查询合并后白名单机器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginWhiteHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginWhiteHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginWhiteList(
            self,
            request: models.DescribeLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginWhiteListResponse:
        """
        获取异地登录白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineClearHistory(
            self,
            request: models.DescribeMachineClearHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineClearHistoryResponse:
        """
        查询机器清理历史记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineClearHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineClearHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineDefenseCnt(
            self,
            request: models.DescribeMachineDefenseCntRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineDefenseCntResponse:
        """
        查询主机高级防御事件数统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineDefenseCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineDefenseCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineFileTamperRules(
            self,
            request: models.DescribeMachineFileTamperRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineFileTamperRulesResponse:
        """
        查询主机相关核心文件监控规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineFileTamperRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineFileTamperRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineGeneral(
            self,
            request: models.DescribeMachineGeneralRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineGeneralResponse:
        """
        查询主机概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineGeneral"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineGeneralResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineInfo(
            self,
            request: models.DescribeMachineInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineInfoResponse:
        """
        本接口（DescribeMachineInfo）用于获取机器详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineLicenseDetail(
            self,
            request: models.DescribeMachineLicenseDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineLicenseDetailResponse:
        """
        本接口 (DescribeMachineLicenseDetail)查询机器授权信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineLicenseDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineLicenseDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineList(
            self,
            request: models.DescribeMachineListRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineListResponse:
        """
        用于网页防篡改获取区域主机列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineOsList(
            self,
            request: models.DescribeMachineOsListRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineOsListResponse:
        """
        查询可筛选操作系统列表.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineOsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineOsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineRegionList(
            self,
            request: models.DescribeMachineRegionListRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineRegionListResponse:
        """
        查询主机地域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineRegionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineRegionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineRegions(
            self,
            request: models.DescribeMachineRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineRegionsResponse:
        """
        获取机器地域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineRiskCnt(
            self,
            request: models.DescribeMachineRiskCntRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineRiskCntResponse:
        """
        查询主机入侵检测事件统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineRiskCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineRiskCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineSnapshot(
            self,
            request: models.DescribeMachineSnapshotRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineSnapshotResponse:
        """
        漏洞修护-查询主机创建的快照
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachines(
            self,
            request: models.DescribeMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeMachinesResponse:
        """
        本接口 (DescribeMachines) 用于获取区域主机列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachinesSimple(
            self,
            request: models.DescribeMachinesSimpleRequest,
            opts: Dict = None,
    ) -> models.DescribeMachinesSimpleResponse:
        """
        本接口 (DescribeMachinesSimple) 用于获取主机列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachinesSimple"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachinesSimpleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalWareList(
            self,
            request: models.DescribeMalWareListRequest,
            opts: Dict = None,
    ) -> models.DescribeMalWareListResponse:
        """
        入侵检测获取木马列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalWareList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalWareListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaliciousRequestWhiteList(
            self,
            request: models.DescribeMaliciousRequestWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeMaliciousRequestWhiteListResponse:
        """
        查询恶意请求白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaliciousRequestWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaliciousRequestWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareFile(
            self,
            request: models.DescribeMalwareFileRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareFileResponse:
        """
        获取木马文件下载地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareInfo(
            self,
            request: models.DescribeMalwareInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareInfoResponse:
        """
        查看恶意文件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareRiskOverview(
            self,
            request: models.DescribeMalwareRiskOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareRiskOverviewResponse:
        """
        获取文件查杀概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareRiskOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareRiskOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareRiskWarning(
            self,
            request: models.DescribeMalwareRiskWarningRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareRiskWarningResponse:
        """
        打开入侵检测-恶意文件检测,弹出风险预警内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareRiskWarning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareRiskWarningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareTimingScanSetting(
            self,
            request: models.DescribeMalwareTimingScanSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareTimingScanSettingResponse:
        """
        查询定时扫描配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareTimingScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareTimingScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareWhiteList(
            self,
            request: models.DescribeMalwareWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareWhiteListResponse:
        """
        获取木马白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareWhiteListAffectList(
            self,
            request: models.DescribeMalwareWhiteListAffectListRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareWhiteListAffectListResponse:
        """
        获取木马白名单受影响列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareWhiteListAffectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareWhiteListAffectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonthInspectionReport(
            self,
            request: models.DescribeMonthInspectionReportRequest,
            opts: Dict = None,
    ) -> models.DescribeMonthInspectionReportResponse:
        """
        专家服务-安全管家月巡检报告下载
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonthInspectionReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonthInspectionReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetAttackSetting(
            self,
            request: models.DescribeNetAttackSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeNetAttackSettingResponse:
        """
        查询网络攻击设置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetAttackSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetAttackSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetAttackWhiteList(
            self,
            request: models.DescribeNetAttackWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetAttackWhiteListResponse:
        """
        获取网络攻击白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetAttackWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetAttackWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpenPortStatistics(
            self,
            request: models.DescribeOpenPortStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeOpenPortStatisticsResponse:
        """
        本接口 (DescribeOpenPortStatistics) 用于获取端口统计列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpenPortStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpenPortStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewStatistics(
            self,
            request: models.DescribeOverviewStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewStatisticsResponse:
        """
        获取概览统计数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivilegeEventInfo(
            self,
            request: models.DescribePrivilegeEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePrivilegeEventInfoResponse:
        """
        本地提权信息详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivilegeEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivilegeEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivilegeEvents(
            self,
            request: models.DescribePrivilegeEventsRequest,
            opts: Dict = None,
    ) -> models.DescribePrivilegeEventsResponse:
        """
        获取本地提权事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivilegeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivilegeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivilegeRules(
            self,
            request: models.DescribePrivilegeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribePrivilegeRulesResponse:
        """
        获取本地提权规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivilegeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivilegeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProVersionInfo(
            self,
            request: models.DescribeProVersionInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProVersionInfoResponse:
        """
        用于获取专业版概览信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProVersionInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProVersionInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProVersionStatus(
            self,
            request: models.DescribeProVersionStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeProVersionStatusResponse:
        """
        用于获取单台主机或所有主机是否开通专业版状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProVersionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProVersionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessStatistics(
            self,
            request: models.DescribeProcessStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessStatisticsResponse:
        """
        本接口 (DescribeProcessStatistics) 用于获取进程统计列表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductStatus(
            self,
            request: models.DescribeProductStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeProductStatusResponse:
        """
        产品试用状态查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProtectDirList(
            self,
            request: models.DescribeProtectDirListRequest,
            opts: Dict = None,
    ) -> models.DescribeProtectDirListResponse:
        """
        网页防篡改防护目录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProtectDirList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProtectDirListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProtectDirRelatedServer(
            self,
            request: models.DescribeProtectDirRelatedServerRequest,
            opts: Dict = None,
    ) -> models.DescribeProtectDirRelatedServerResponse:
        """
        查询防护目录关联服务器列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProtectDirRelatedServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProtectDirRelatedServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProtectNetList(
            self,
            request: models.DescribeProtectNetListRequest,
            opts: Dict = None,
    ) -> models.DescribeProtectNetListResponse:
        """
        专家服务-旗舰重保列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProtectNetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProtectNetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicProxyInstallCommand(
            self,
            request: models.DescribePublicProxyInstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribePublicProxyInstallCommandResponse:
        """
        获取公网接入代理安装命令
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicProxyInstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicProxyInstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseBackupList(
            self,
            request: models.DescribeRansomDefenseBackupListRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseBackupListResponse:
        """
        查询主机快照备份列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseBackupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseBackupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseEventsList(
            self,
            request: models.DescribeRansomDefenseEventsListRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseEventsListResponse:
        """
        查询防勒索事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseEventsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseEventsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseMachineList(
            self,
            request: models.DescribeRansomDefenseMachineListRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseMachineListResponse:
        """
        查询备份详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseMachineStrategyInfo(
            self,
            request: models.DescribeRansomDefenseMachineStrategyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseMachineStrategyInfoResponse:
        """
        获取主机绑定策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseMachineStrategyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseMachineStrategyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseRollBackTaskList(
            self,
            request: models.DescribeRansomDefenseRollBackTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseRollBackTaskListResponse:
        """
        查询回滚任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseRollBackTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseRollBackTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseState(
            self,
            request: models.DescribeRansomDefenseStateRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseStateResponse:
        """
        获取用户防勒索趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseStrategyDetail(
            self,
            request: models.DescribeRansomDefenseStrategyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseStrategyDetailResponse:
        """
        获取策略详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseStrategyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseStrategyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseStrategyList(
            self,
            request: models.DescribeRansomDefenseStrategyListRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseStrategyListResponse:
        """
        查询防勒索策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseStrategyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseStrategyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseStrategyMachines(
            self,
            request: models.DescribeRansomDefenseStrategyMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseStrategyMachinesResponse:
        """
        查询防勒索策略绑定机器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseStrategyMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseStrategyMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRansomDefenseTrend(
            self,
            request: models.DescribeRansomDefenseTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeRansomDefenseTrendResponse:
        """
        获取全网勒索态势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRansomDefenseTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRansomDefenseTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRaspMaxCpu(
            self,
            request: models.DescribeRaspMaxCpuRequest,
            opts: Dict = None,
    ) -> models.DescribeRaspMaxCpuResponse:
        """
        查看漏洞防御最大cpu限制
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRaspMaxCpu"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRaspMaxCpuResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRaspRuleVuls(
            self,
            request: models.DescribeRaspRuleVulsRequest,
            opts: Dict = None,
    ) -> models.DescribeRaspRuleVulsResponse:
        """
        获取漏洞防御白名单漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRaspRuleVuls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRaspRuleVulsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRaspRules(
            self,
            request: models.DescribeRaspRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRaspRulesResponse:
        """
        查询漏洞防御白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRaspRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRaspRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecommendedProtectCpu(
            self,
            request: models.DescribeRecommendedProtectCpuRequest,
            opts: Dict = None,
    ) -> models.DescribeRecommendedProtectCpuResponse:
        """
        查询推荐购买防护核数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecommendedProtectCpu"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecommendedProtectCpuResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellEventInfo(
            self,
            request: models.DescribeReverseShellEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellEventInfoResponse:
        """
        反弹shell信息详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellEvents(
            self,
            request: models.DescribeReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellEventsResponse:
        """
        获取反弹Shell列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellRules(
            self,
            request: models.DescribeReverseShellRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellRulesResponse:
        """
        获取反弹Shell规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskBatchStatus(
            self,
            request: models.DescribeRiskBatchStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskBatchStatusResponse:
        """
        查询入侵检测事件更新状态任务是否完成
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskBatchStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskBatchStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsEventInfo(
            self,
            request: models.DescribeRiskDnsEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsEventInfoResponse:
        """
        查询恶意请求事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsEventList(
            self,
            request: models.DescribeRiskDnsEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsEventListResponse:
        """
        获取恶意请求事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsInfo(
            self,
            request: models.DescribeRiskDnsInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsInfoResponse:
        """
        查询恶意请求详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsList(
            self,
            request: models.DescribeRiskDnsListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsListResponse:
        """
        入侵检测，获取恶意请求列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsPolicyList(
            self,
            request: models.DescribeRiskDnsPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsPolicyListResponse:
        """
        获取恶意请求策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskProcessEvents(
            self,
            request: models.DescribeRiskProcessEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskProcessEventsResponse:
        """
        获取异常进程列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskProcessEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskProcessEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSafeInfo(
            self,
            request: models.DescribeSafeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSafeInfoResponse:
        """
        查询安全通知信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSafeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSafeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanMalwareSchedule(
            self,
            request: models.DescribeScanMalwareScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeScanMalwareScheduleResponse:
        """
        查询木马扫描进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanMalwareSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanMalwareScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanSchedule(
            self,
            request: models.DescribeScanScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeScanScheduleResponse:
        """
        根据taskid查询检测进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanState(
            self,
            request: models.DescribeScanStateRequest,
            opts: Dict = None,
    ) -> models.DescribeScanStateResponse:
        """
        DescribeScanState 该接口能查询对应模块正在进行的扫描任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskDetails(
            self,
            request: models.DescribeScanTaskDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskDetailsResponse:
        """
        DescribeScanTaskDetails 查询扫描任务详情 , 可以查询扫描进度信息/异常;
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskStatus(
            self,
            request: models.DescribeScanTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskStatusResponse:
        """
        DescribeScanTaskStatus 查询机器扫描状态列表用于过滤筛选
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanVulSetting(
            self,
            request: models.DescribeScanVulSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeScanVulSettingResponse:
        """
        查询定期检测的配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanVulSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanVulSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenAttackHotspot(
            self,
            request: models.DescribeScreenAttackHotspotRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenAttackHotspotResponse:
        """
        大屏可视化获取全网攻击热点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenAttackHotspot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenAttackHotspotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenBroadcasts(
            self,
            request: models.DescribeScreenBroadcastsRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenBroadcastsResponse:
        """
        大屏可视化安全播报
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenBroadcasts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenBroadcastsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenDefenseTrends(
            self,
            request: models.DescribeScreenDefenseTrendsRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenDefenseTrendsResponse:
        """
        大屏可视化防趋势接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenDefenseTrends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenDefenseTrendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenEmergentMsg(
            self,
            request: models.DescribeScreenEmergentMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenEmergentMsgResponse:
        """
        大屏可视化紧急通知
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenEmergentMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenEmergentMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenEventsCnt(
            self,
            request: models.DescribeScreenEventsCntRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenEventsCntResponse:
        """
        大屏可视化获取安全概览相关事件统计数据接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenEventsCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenEventsCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenGeneralStat(
            self,
            request: models.DescribeScreenGeneralStatRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenGeneralStatResponse:
        """
        大屏可视化获取主机相关统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenGeneralStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenGeneralStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenHostInvasion(
            self,
            request: models.DescribeScreenHostInvasionRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenHostInvasionResponse:
        """
        大屏可视化主机入侵详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenHostInvasion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenHostInvasionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenMachineRegions(
            self,
            request: models.DescribeScreenMachineRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenMachineRegionsResponse:
        """
        大屏可视化主机区域选项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenMachineRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenMachineRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenMachines(
            self,
            request: models.DescribeScreenMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenMachinesResponse:
        """
        大屏可视化主机区域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenProtectionCnt(
            self,
            request: models.DescribeScreenProtectionCntRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenProtectionCntResponse:
        """
        大屏可视化主机安全防护引擎介绍
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenProtectionCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenProtectionCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenProtectionStat(
            self,
            request: models.DescribeScreenProtectionStatRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenProtectionStatResponse:
        """
        大屏获取安全防护状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenProtectionStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenProtectionStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScreenRiskAssetsTop(
            self,
            request: models.DescribeScreenRiskAssetsTopRequest,
            opts: Dict = None,
    ) -> models.DescribeScreenRiskAssetsTopResponse:
        """
        大屏可视化风险资产top5（今日），统计今日风险资产
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScreenRiskAssetsTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScreenRiskAssetsTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchLogs(
            self,
            request: models.DescribeSearchLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchLogsResponse:
        """
        获取历史搜索记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchTemplates(
            self,
            request: models.DescribeSearchTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchTemplatesResponse:
        """
        获取快速检索列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityBroadcastInfo(
            self,
            request: models.DescribeSecurityBroadcastInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityBroadcastInfoResponse:
        """
        查询安全播报文章信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityBroadcastInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityBroadcastInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityBroadcasts(
            self,
            request: models.DescribeSecurityBroadcastsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityBroadcastsResponse:
        """
        安全播报列表页
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityBroadcasts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityBroadcastsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityDynamics(
            self,
            request: models.DescribeSecurityDynamicsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityDynamicsResponse:
        """
        本接口 (DescribeSecurityDynamics) 用于获取安全事件动态消息数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityDynamics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityDynamicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityEventStat(
            self,
            request: models.DescribeSecurityEventStatRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityEventStatResponse:
        """
        获取安全事件统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityEventStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityEventStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityEventsCnt(
            self,
            request: models.DescribeSecurityEventsCntRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityEventsCntResponse:
        """
        获取安全概览相关事件统计数据接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityEventsCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityEventsCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityTrends(
            self,
            request: models.DescribeSecurityTrendsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityTrendsResponse:
        """
        本接口 (DescribeSecurityTrends) 用于获取安全事件统计数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityTrends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityTrendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerRelatedDirInfo(
            self,
            request: models.DescribeServerRelatedDirInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeServerRelatedDirInfoResponse:
        """
        查询服务区关联目录详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerRelatedDirInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerRelatedDirInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServersAndRiskAndFirstInfo(
            self,
            request: models.DescribeServersAndRiskAndFirstInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeServersAndRiskAndFirstInfoResponse:
        """
        获取待处理风险文件数+影响服务器数+是否试用检测+最近检测时间
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServersAndRiskAndFirstInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServersAndRiskAndFirstInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStrategyExist(
            self,
            request: models.DescribeStrategyExistRequest,
            opts: Dict = None,
    ) -> models.DescribeStrategyExistResponse:
        """
        根据策略名查询策略是否存在
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStrategyExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStrategyExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagMachines(
            self,
            request: models.DescribeTagMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeTagMachinesResponse:
        """
        获取指定标签关联的服务器信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTags(
            self,
            request: models.DescribeTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsResponse:
        """
        获取所有主机标签
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrialReport(
            self,
            request: models.DescribeTrialReportRequest,
            opts: Dict = None,
    ) -> models.DescribeTrialReportResponse:
        """
        查询主机安全授权试用报告(仅限控制台申领的)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrialReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrialReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUndoVulCounts(
            self,
            request: models.DescribeUndoVulCountsRequest,
            opts: Dict = None,
    ) -> models.DescribeUndoVulCountsResponse:
        """
        获取漏洞管理模块指定类型的待处理漏洞数、主机数和非专业版主机数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUndoVulCounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUndoVulCountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsersConfig(
            self,
            request: models.DescribeUsersConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersConfigResponse:
        """
        用于查询用户自定义配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsersConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsualLoginPlaces(
            self,
            request: models.DescribeUsualLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DescribeUsualLoginPlacesResponse:
        """
        此接口（DescribeUsualLoginPlaces）用于查询常用登录地。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsualLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsualLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVdbAndPocInfo(
            self,
            request: models.DescribeVdbAndPocInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVdbAndPocInfoResponse:
        """
        获取病毒库及POC的更新信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVdbAndPocInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVdbAndPocInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVersionCompareChart(
            self,
            request: models.DescribeVersionCompareChartRequest,
            opts: Dict = None,
    ) -> models.DescribeVersionCompareChartResponse:
        """
        获取版本对比信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVersionCompareChart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVersionCompareChartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVersionStatistics(
            self,
            request: models.DescribeVersionStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeVersionStatisticsResponse:
        """
        用于统计专业版和基础版机器数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVersionStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVersionStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVertexDetail(
            self,
            request: models.DescribeVertexDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVertexDetailResponse:
        """
        获取指定点属性信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVertexDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVertexDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulCountByDates(
            self,
            request: models.DescribeVulCountByDatesRequest,
            opts: Dict = None,
    ) -> models.DescribeVulCountByDatesResponse:
        """
        漏洞管理模块，获取近日指定类型的漏洞数量和主机数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulCountByDates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulCountByDatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulCveIdInfo(
            self,
            request: models.DescribeVulCveIdInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVulCveIdInfoResponse:
        """
        CveId查询漏洞详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulCveIdInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulCveIdInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceEvent(
            self,
            request: models.DescribeVulDefenceEventRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceEventResponse:
        """
        获取漏洞防御事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceList(
            self,
            request: models.DescribeVulDefenceListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceListResponse:
        """
        查询漏洞防御列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceOverview(
            self,
            request: models.DescribeVulDefenceOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceOverviewResponse:
        """
        获取漏洞防御概览信息，包括事件趋势及插件开启情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefencePluginDetail(
            self,
            request: models.DescribeVulDefencePluginDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefencePluginDetailResponse:
        """
        获取单台主机漏洞防御插件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefencePluginDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefencePluginDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefencePluginExceptionCount(
            self,
            request: models.DescribeVulDefencePluginExceptionCountRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefencePluginExceptionCountResponse:
        """
        获取当前异常插件数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefencePluginExceptionCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefencePluginExceptionCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefencePluginStatus(
            self,
            request: models.DescribeVulDefencePluginStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefencePluginStatusResponse:
        """
        获取各主机漏洞防御插件状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefencePluginStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefencePluginStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceSetting(
            self,
            request: models.DescribeVulDefenceSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceSettingResponse:
        """
        获取当前漏洞防御插件设置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulEffectHostList(
            self,
            request: models.DescribeVulEffectHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulEffectHostListResponse:
        """
        漏洞影响主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulEffectModules(
            self,
            request: models.DescribeVulEffectModulesRequest,
            opts: Dict = None,
    ) -> models.DescribeVulEffectModulesResponse:
        """
        漏洞影响组件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulEffectModules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulEffectModulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulEmergentMsg(
            self,
            request: models.DescribeVulEmergentMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeVulEmergentMsgResponse:
        """
        获取漏洞紧急通知
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulEmergentMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulEmergentMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixStatus(
            self,
            request: models.DescribeVulFixStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixStatusResponse:
        """
        漏洞修护-查找主机漏洞修护进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulHostCountScanTime(
            self,
            request: models.DescribeVulHostCountScanTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeVulHostCountScanTimeResponse:
        """
        获取待处理漏洞数+影响主机数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulHostCountScanTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulHostCountScanTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulHostTop(
            self,
            request: models.DescribeVulHostTopRequest,
            opts: Dict = None,
    ) -> models.DescribeVulHostTopResponse:
        """
        获取服务器风险top列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulHostTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulHostTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulInfoCvss(
            self,
            request: models.DescribeVulInfoCvssRequest,
            opts: Dict = None,
    ) -> models.DescribeVulInfoCvssResponse:
        """
        漏洞详情，带CVSS版本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulInfoCvss"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulInfoCvssResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulLabels(
            self,
            request: models.DescribeVulLabelsRequest,
            opts: Dict = None,
    ) -> models.DescribeVulLabelsResponse:
        """
        获取用户漏洞所有标签列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulLabels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulLabelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulLevelCount(
            self,
            request: models.DescribeVulLevelCountRequest,
            opts: Dict = None,
    ) -> models.DescribeVulLevelCountResponse:
        """
        漏洞数量等级分布统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulLevelCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulLevelCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulList(
            self,
            request: models.DescribeVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulListResponse:
        """
        获取漏洞列表数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulOverview(
            self,
            request: models.DescribeVulOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeVulOverviewResponse:
        """
        获取漏洞概览数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulStoreList(
            self,
            request: models.DescribeVulStoreListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulStoreListResponse:
        """
        获取漏洞库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulStoreList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulStoreListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulTop(
            self,
            request: models.DescribeVulTopRequest,
            opts: Dict = None,
    ) -> models.DescribeVulTopResponse:
        """
        漏洞top统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulTrend(
            self,
            request: models.DescribeVulTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeVulTrendResponse:
        """
        获取漏洞态势信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWarningHostConfig(
            self,
            request: models.DescribeWarningHostConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeWarningHostConfigResponse:
        """
        查询告警机器范围配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWarningHostConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWarningHostConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWarningList(
            self,
            request: models.DescribeWarningListRequest,
            opts: Dict = None,
    ) -> models.DescribeWarningListResponse:
        """
        获取当前用户告警列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWarningList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWarningListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebHookPolicy(
            self,
            request: models.DescribeWebHookPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeWebHookPolicyResponse:
        """
        查询告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebHookPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebHookPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebHookReceiver(
            self,
            request: models.DescribeWebHookReceiverRequest,
            opts: Dict = None,
    ) -> models.DescribeWebHookReceiverResponse:
        """
        查询告警接收人列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebHookReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebHookReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebHookReceiverUsage(
            self,
            request: models.DescribeWebHookReceiverUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeWebHookReceiverUsageResponse:
        """
        查询指定告警接收人的关联策略使用信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebHookReceiverUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebHookReceiverUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebHookRule(
            self,
            request: models.DescribeWebHookRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeWebHookRuleResponse:
        """
        获取企微机器人规则详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebHookRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebHookRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebHookRules(
            self,
            request: models.DescribeWebHookRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeWebHookRulesResponse:
        """
        获取企微机器人规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebHookRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebHookRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebPageEventList(
            self,
            request: models.DescribeWebPageEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeWebPageEventListResponse:
        """
        查询篡改事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebPageEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebPageEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebPageGeneralize(
            self,
            request: models.DescribeWebPageGeneralizeRequest,
            opts: Dict = None,
    ) -> models.DescribeWebPageGeneralizeResponse:
        """
        查询网站防篡改概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebPageGeneralize"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebPageGeneralizeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebPageProtectStat(
            self,
            request: models.DescribeWebPageProtectStatRequest,
            opts: Dict = None,
    ) -> models.DescribeWebPageProtectStatResponse:
        """
        网站防篡改-查询动态防护信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebPageProtectStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebPageProtectStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebPageServiceInfo(
            self,
            request: models.DescribeWebPageServiceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeWebPageServiceInfoResponse:
        """
        网站防篡改-查询网页防篡改服务器购买信息及服务器信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebPageServiceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebPageServiceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyOrder(
            self,
            request: models.DestroyOrderRequest,
            opts: Dict = None,
    ) -> models.DestroyOrderResponse:
        """
        DestroyOrder  该接口可以对资源销毁.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditBashRules(
            self,
            request: models.EditBashRulesRequest,
            opts: Dict = None,
    ) -> models.EditBashRulesResponse:
        """
        新增或修改高危命令规则
        """
        
        kwargs = {}
        kwargs["action"] = "EditBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditPrivilegeRules(
            self,
            request: models.EditPrivilegeRulesRequest,
            opts: Dict = None,
    ) -> models.EditPrivilegeRulesResponse:
        """
        新增或修改本地提权规则（支持多服务器选择）
        """
        
        kwargs = {}
        kwargs["action"] = "EditPrivilegeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditPrivilegeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditReverseShellRules(
            self,
            request: models.EditReverseShellRulesRequest,
            opts: Dict = None,
    ) -> models.EditReverseShellRulesResponse:
        """
        编辑反弹Shell规则（支持多服务器选择）
        """
        
        kwargs = {}
        kwargs["action"] = "EditReverseShellRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditReverseShellRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditTags(
            self,
            request: models.EditTagsRequest,
            opts: Dict = None,
    ) -> models.EditTagsResponse:
        """
        新增或编辑标签
        """
        
        kwargs = {}
        kwargs["action"] = "EditTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetAppList(
            self,
            request: models.ExportAssetAppListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetAppListResponse:
        """
        导出资产管理应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetCoreModuleList(
            self,
            request: models.ExportAssetCoreModuleListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetCoreModuleListResponse:
        """
        导出资产管理内核模块列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetCoreModuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetCoreModuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetDatabaseList(
            self,
            request: models.ExportAssetDatabaseListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetDatabaseListResponse:
        """
        导出资产管理数据库列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetDatabaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetDatabaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetEnvList(
            self,
            request: models.ExportAssetEnvListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetEnvListResponse:
        """
        导出资产管理环境变量列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetEnvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetEnvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetInitServiceList(
            self,
            request: models.ExportAssetInitServiceListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetInitServiceListResponse:
        """
        导出资产管理启动服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetInitServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetInitServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetJarList(
            self,
            request: models.ExportAssetJarListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetJarListResponse:
        """
        导出Jar包列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetJarList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetJarListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetMachineDetail(
            self,
            request: models.ExportAssetMachineDetailRequest,
            opts: Dict = None,
    ) -> models.ExportAssetMachineDetailResponse:
        """
        导出资产管理主机资源详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetMachineDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetMachineDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetMachineList(
            self,
            request: models.ExportAssetMachineListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetMachineListResponse:
        """
        导出资源监控列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetPlanTaskList(
            self,
            request: models.ExportAssetPlanTaskListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetPlanTaskListResponse:
        """
        导出资产管理计划任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetPlanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetPlanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetPortInfoList(
            self,
            request: models.ExportAssetPortInfoListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetPortInfoListResponse:
        """
        导出资产管理端口列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetPortInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetPortInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetProcessInfoList(
            self,
            request: models.ExportAssetProcessInfoListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetProcessInfoListResponse:
        """
        导出资产管理进程列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetProcessInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetProcessInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetRecentMachineInfo(
            self,
            request: models.ExportAssetRecentMachineInfoRequest,
            opts: Dict = None,
    ) -> models.ExportAssetRecentMachineInfoResponse:
        """
        导出主机最近趋势情况（最长最近90天）
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetRecentMachineInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetRecentMachineInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetSystemPackageList(
            self,
            request: models.ExportAssetSystemPackageListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetSystemPackageListResponse:
        """
        导出资产管理系统安装包列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetSystemPackageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetSystemPackageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetUserList(
            self,
            request: models.ExportAssetUserListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetUserListResponse:
        """
        导出账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetWebAppList(
            self,
            request: models.ExportAssetWebAppListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetWebAppListResponse:
        """
        导出资产管理Web应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetWebAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetWebAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetWebFrameList(
            self,
            request: models.ExportAssetWebFrameListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetWebFrameListResponse:
        """
        导出资产管理Web框架列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetWebFrameList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetWebFrameListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetWebLocationList(
            self,
            request: models.ExportAssetWebLocationListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetWebLocationListResponse:
        """
        导出Web站点列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetWebLocationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetWebLocationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetWebServiceInfoList(
            self,
            request: models.ExportAssetWebServiceInfoListRequest,
            opts: Dict = None,
    ) -> models.ExportAssetWebServiceInfoListResponse:
        """
        导出资产管理Web服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetWebServiceInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetWebServiceInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAttackEvents(
            self,
            request: models.ExportAttackEventsRequest,
            opts: Dict = None,
    ) -> models.ExportAttackEventsResponse:
        """
        导出网络攻击事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAttackEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAttackEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineEffectHostList(
            self,
            request: models.ExportBaselineEffectHostListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineEffectHostListResponse:
        """
        导出基线影响主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineFixList(
            self,
            request: models.ExportBaselineFixListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineFixListResponse:
        """
        导出修复列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineFixList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineFixListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineHostDetectList(
            self,
            request: models.ExportBaselineHostDetectListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineHostDetectListResponse:
        """
        导出基线主机检测
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineHostDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineHostDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineItemDetectList(
            self,
            request: models.ExportBaselineItemDetectListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineItemDetectListResponse:
        """
        导出基线检测项
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineItemDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineItemDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineItemList(
            self,
            request: models.ExportBaselineItemListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineItemListResponse:
        """
        导出检测项结果列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineList(
            self,
            request: models.ExportBaselineListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineListResponse:
        """
        导出基线列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineRuleDetectList(
            self,
            request: models.ExportBaselineRuleDetectListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineRuleDetectListResponse:
        """
        导出基线检测规则
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineRuleDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineRuleDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBaselineWeakPasswordList(
            self,
            request: models.ExportBaselineWeakPasswordListRequest,
            opts: Dict = None,
    ) -> models.ExportBaselineWeakPasswordListResponse:
        """
        导出弱口令配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBaselineWeakPasswordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBaselineWeakPasswordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBashEvents(
            self,
            request: models.ExportBashEventsRequest,
            opts: Dict = None,
    ) -> models.ExportBashEventsResponse:
        """
        导出高危命令事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBashEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBashEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBashEventsNew(
            self,
            request: models.ExportBashEventsNewRequest,
            opts: Dict = None,
    ) -> models.ExportBashEventsNewResponse:
        """
        导出高危命令事件(新)
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBashEventsNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBashEventsNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBashPolicies(
            self,
            request: models.ExportBashPoliciesRequest,
            opts: Dict = None,
    ) -> models.ExportBashPoliciesResponse:
        """
        导出高危命令策略
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBashPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBashPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBruteAttacks(
            self,
            request: models.ExportBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.ExportBruteAttacksResponse:
        """
        本接口 (ExportBruteAttacks) 用于导出密码破解记录成CSV文件。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportFileTamperEvents(
            self,
            request: models.ExportFileTamperEventsRequest,
            opts: Dict = None,
    ) -> models.ExportFileTamperEventsResponse:
        """
        导出核心文件事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportFileTamperEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportFileTamperEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportFileTamperRules(
            self,
            request: models.ExportFileTamperRulesRequest,
            opts: Dict = None,
    ) -> models.ExportFileTamperRulesResponse:
        """
        导出核心文件监控规则
        """
        
        kwargs = {}
        kwargs["action"] = "ExportFileTamperRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportFileTamperRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportIgnoreBaselineRule(
            self,
            request: models.ExportIgnoreBaselineRuleRequest,
            opts: Dict = None,
    ) -> models.ExportIgnoreBaselineRuleResponse:
        """
        导出已忽略基线检测项信息
        """
        
        kwargs = {}
        kwargs["action"] = "ExportIgnoreBaselineRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportIgnoreBaselineRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportIgnoreRuleEffectHostList(
            self,
            request: models.ExportIgnoreRuleEffectHostListRequest,
            opts: Dict = None,
    ) -> models.ExportIgnoreRuleEffectHostListResponse:
        """
        根据检测项id导出忽略检测项影响主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportIgnoreRuleEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportIgnoreRuleEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportJavaMemShellPlugins(
            self,
            request: models.ExportJavaMemShellPluginsRequest,
            opts: Dict = None,
    ) -> models.ExportJavaMemShellPluginsResponse:
        """
        导出java内存马插件信息
        """
        
        kwargs = {}
        kwargs["action"] = "ExportJavaMemShellPlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportJavaMemShellPluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportJavaMemShells(
            self,
            request: models.ExportJavaMemShellsRequest,
            opts: Dict = None,
    ) -> models.ExportJavaMemShellsResponse:
        """
        导出java内存马事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportJavaMemShells"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportJavaMemShellsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportLicenseDetail(
            self,
            request: models.ExportLicenseDetailRequest,
            opts: Dict = None,
    ) -> models.ExportLicenseDetailResponse:
        """
        导出授权列表对应的绑定信息
        """
        
        kwargs = {}
        kwargs["action"] = "ExportLicenseDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportLicenseDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportMaliciousRequests(
            self,
            request: models.ExportMaliciousRequestsRequest,
            opts: Dict = None,
    ) -> models.ExportMaliciousRequestsResponse:
        """
        本接口 (ExportMaliciousRequests) 用于导出下载恶意请求文件。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportMaliciousRequests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportMaliciousRequestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportMalwares(
            self,
            request: models.ExportMalwaresRequest,
            opts: Dict = None,
    ) -> models.ExportMalwaresResponse:
        """
        本接口 (ExportMalwares) 用于导出木马记录CSV文件。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportNonlocalLoginPlaces(
            self,
            request: models.ExportNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.ExportNonlocalLoginPlacesResponse:
        """
        本接口 (ExportNonlocalLoginPlaces) 用于导出异地登录事件记录CSV文件。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportPrivilegeEvents(
            self,
            request: models.ExportPrivilegeEventsRequest,
            opts: Dict = None,
    ) -> models.ExportPrivilegeEventsResponse:
        """
        导出本地提权事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportPrivilegeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportPrivilegeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportProtectDirList(
            self,
            request: models.ExportProtectDirListRequest,
            opts: Dict = None,
    ) -> models.ExportProtectDirListResponse:
        """
        导出网页防篡改防护目录列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportProtectDirList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportProtectDirListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRansomDefenseBackupList(
            self,
            request: models.ExportRansomDefenseBackupListRequest,
            opts: Dict = None,
    ) -> models.ExportRansomDefenseBackupListResponse:
        """
        导出主机快照备份列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRansomDefenseBackupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRansomDefenseBackupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRansomDefenseEventsList(
            self,
            request: models.ExportRansomDefenseEventsListRequest,
            opts: Dict = None,
    ) -> models.ExportRansomDefenseEventsListResponse:
        """
        导出防勒索事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRansomDefenseEventsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRansomDefenseEventsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRansomDefenseMachineList(
            self,
            request: models.ExportRansomDefenseMachineListRequest,
            opts: Dict = None,
    ) -> models.ExportRansomDefenseMachineListResponse:
        """
        导出备份详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRansomDefenseMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRansomDefenseMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRansomDefenseStrategyList(
            self,
            request: models.ExportRansomDefenseStrategyListRequest,
            opts: Dict = None,
    ) -> models.ExportRansomDefenseStrategyListResponse:
        """
        导出防勒索策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRansomDefenseStrategyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRansomDefenseStrategyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRansomDefenseStrategyMachines(
            self,
            request: models.ExportRansomDefenseStrategyMachinesRequest,
            opts: Dict = None,
    ) -> models.ExportRansomDefenseStrategyMachinesResponse:
        """
        导出勒索防御策略绑定机器列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRansomDefenseStrategyMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRansomDefenseStrategyMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportReverseShellEvents(
            self,
            request: models.ExportReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.ExportReverseShellEventsResponse:
        """
        导出反弹Shell事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRiskDnsEventList(
            self,
            request: models.ExportRiskDnsEventListRequest,
            opts: Dict = None,
    ) -> models.ExportRiskDnsEventListResponse:
        """
        导出恶意请求事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRiskDnsEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRiskDnsEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRiskDnsPolicyList(
            self,
            request: models.ExportRiskDnsPolicyListRequest,
            opts: Dict = None,
    ) -> models.ExportRiskDnsPolicyListResponse:
        """
        导出恶意请求策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRiskDnsPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRiskDnsPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRiskProcessEvents(
            self,
            request: models.ExportRiskProcessEventsRequest,
            opts: Dict = None,
    ) -> models.ExportRiskProcessEventsResponse:
        """
        导出异常进程事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRiskProcessEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRiskProcessEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportScanTaskDetails(
            self,
            request: models.ExportScanTaskDetailsRequest,
            opts: Dict = None,
    ) -> models.ExportScanTaskDetailsResponse:
        """
        根据任务id导出指定扫描任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "ExportScanTaskDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportScanTaskDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportSecurityTrends(
            self,
            request: models.ExportSecurityTrendsRequest,
            opts: Dict = None,
    ) -> models.ExportSecurityTrendsResponse:
        """
        导出风险趋势
        """
        
        kwargs = {}
        kwargs["action"] = "ExportSecurityTrends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportSecurityTrendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportTasks(
            self,
            request: models.ExportTasksRequest,
            opts: Dict = None,
    ) -> models.ExportTasksResponse:
        """
        用于异步导出数据量大的日志文件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulDefenceEvent(
            self,
            request: models.ExportVulDefenceEventRequest,
            opts: Dict = None,
    ) -> models.ExportVulDefenceEventResponse:
        """
        导出漏洞防御事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulDefenceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulDefenceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulDefenceList(
            self,
            request: models.ExportVulDefenceListRequest,
            opts: Dict = None,
    ) -> models.ExportVulDefenceListResponse:
        """
        导出漏洞防御列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulDefenceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulDefenceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulDefencePluginEvent(
            self,
            request: models.ExportVulDefencePluginEventRequest,
            opts: Dict = None,
    ) -> models.ExportVulDefencePluginEventResponse:
        """
        导出漏洞防御插件事件
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulDefencePluginEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulDefencePluginEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulDetectionExcel(
            self,
            request: models.ExportVulDetectionExcelRequest,
            opts: Dict = None,
    ) -> models.ExportVulDetectionExcelResponse:
        """
        导出本次漏洞检测Excel
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulDetectionExcel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulDetectionExcelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulDetectionReport(
            self,
            request: models.ExportVulDetectionReportRequest,
            opts: Dict = None,
    ) -> models.ExportVulDetectionReportResponse:
        """
        导出漏洞检测报告。
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulDetectionReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulDetectionReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulEffectHostList(
            self,
            request: models.ExportVulEffectHostListRequest,
            opts: Dict = None,
    ) -> models.ExportVulEffectHostListResponse:
        """
        导出漏洞影响主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulEffectHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulEffectHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulInfo(
            self,
            request: models.ExportVulInfoRequest,
            opts: Dict = None,
    ) -> models.ExportVulInfoResponse:
        """
        导出漏洞信息，包括影响主机列表，组件信息
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVulList(
            self,
            request: models.ExportVulListRequest,
            opts: Dict = None,
    ) -> models.ExportVulListResponse:
        """
        漏洞管理-导出漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportWebPageEventList(
            self,
            request: models.ExportWebPageEventListRequest,
            opts: Dict = None,
    ) -> models.ExportWebPageEventListResponse:
        """
        导出篡改事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportWebPageEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportWebPageEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FixBaselineDetect(
            self,
            request: models.FixBaselineDetectRequest,
            opts: Dict = None,
    ) -> models.FixBaselineDetectResponse:
        """
        修复基线检测
        """
        
        kwargs = {}
        kwargs["action"] = "FixBaselineDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FixBaselineDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLocalStorageItem(
            self,
            request: models.GetLocalStorageItemRequest,
            opts: Dict = None,
    ) -> models.GetLocalStorageItemResponse:
        """
        获取本地存储数据
        """
        
        kwargs = {}
        kwargs["action"] = "GetLocalStorageItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLocalStorageItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IgnoreImpactedHosts(
            self,
            request: models.IgnoreImpactedHostsRequest,
            opts: Dict = None,
    ) -> models.IgnoreImpactedHostsResponse:
        """
        产品变动切换到了\\n切换到 AddVulIgnoreRule / ModifyVulIgnoreRule  CancelVulIgnoreRule\\n相关接口

        本接口 (IgnoreImpactedHosts) 用于忽略漏洞。
        """
        
        kwargs = {}
        kwargs["action"] = "IgnoreImpactedHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IgnoreImpactedHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KeysLocalStorage(
            self,
            request: models.KeysLocalStorageRequest,
            opts: Dict = None,
    ) -> models.KeysLocalStorageResponse:
        """
        获取本地存储键值列表
        """
        
        kwargs = {}
        kwargs["action"] = "KeysLocalStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KeysLocalStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoOpenProVersionConfig(
            self,
            request: models.ModifyAutoOpenProVersionConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoOpenProVersionConfigResponse:
        """
        用于设置新增主机自动开通专业防护配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoOpenProVersionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoOpenProVersionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBanMode(
            self,
            request: models.ModifyBanModeRequest,
            opts: Dict = None,
    ) -> models.ModifyBanModeResponse:
        """
        修改爆破阻断模式
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBanMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBanModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBanStatus(
            self,
            request: models.ModifyBanStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBanStatusResponse:
        """
        设置阻断开关状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBanStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBanWhiteList(
            self,
            request: models.ModifyBanWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyBanWhiteListResponse:
        """
        修改阻断白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBanWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBanWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselinePolicy(
            self,
            request: models.ModifyBaselinePolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselinePolicyResponse:
        """
        更改基线策略设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselinePolicyState(
            self,
            request: models.ModifyBaselinePolicyStateRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselinePolicyStateResponse:
        """
        更改基线策略状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselinePolicyState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselinePolicyStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselineRule(
            self,
            request: models.ModifyBaselineRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselineRuleResponse:
        """
        更改基线检测规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselineRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselineRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselineRuleIgnore(
            self,
            request: models.ModifyBaselineRuleIgnoreRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselineRuleIgnoreResponse:
        """
        更改基线忽略规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselineRuleIgnore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselineRuleIgnoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselineWeakPassword(
            self,
            request: models.ModifyBaselineWeakPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselineWeakPasswordResponse:
        """
        更改或新增弱口令
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselineWeakPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselineWeakPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBashPolicy(
            self,
            request: models.ModifyBashPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyBashPolicyResponse:
        """
        新增或修改高危命令策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBashPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBashPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBashPolicyStatus(
            self,
            request: models.ModifyBashPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBashPolicyStatusResponse:
        """
        切换高危命令策略状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBashPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBashPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBruteAttackRules(
            self,
            request: models.ModifyBruteAttackRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyBruteAttackRulesResponse:
        """
        修改暴力破解规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBruteAttackRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBruteAttackRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEventAttackStatus(
            self,
            request: models.ModifyEventAttackStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEventAttackStatusResponse:
        """
        修改网络攻击事件状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEventAttackStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEventAttackStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileTamperEvents(
            self,
            request: models.ModifyFileTamperEventsRequest,
            opts: Dict = None,
    ) -> models.ModifyFileTamperEventsResponse:
        """
        核心文件事件更新
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileTamperEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileTamperEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileTamperRule(
            self,
            request: models.ModifyFileTamperRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyFileTamperRuleResponse:
        """
        编辑、新增核心文件监控规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileTamperRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileTamperRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileTamperRuleStatus(
            self,
            request: models.ModifyFileTamperRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyFileTamperRuleStatusResponse:
        """
        核心文件规则状态更新，支持批量删除 关闭
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileTamperRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileTamperRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyJavaMemShellPluginSwitch(
            self,
            request: models.ModifyJavaMemShellPluginSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyJavaMemShellPluginSwitchResponse:
        """
        开关java内存马插件
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyJavaMemShellPluginSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyJavaMemShellPluginSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyJavaMemShellsStatus(
            self,
            request: models.ModifyJavaMemShellsStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyJavaMemShellsStatusResponse:
        """
        修改java内存马事件状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyJavaMemShellsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyJavaMemShellsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLicenseBinds(
            self,
            request: models.ModifyLicenseBindsRequest,
            opts: Dict = None,
    ) -> models.ModifyLicenseBindsResponse:
        """
        设置中心-授权管理 对某个授权批量绑定机器
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLicenseBinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLicenseBindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLicenseOrder(
            self,
            request: models.ModifyLicenseOrderRequest,
            opts: Dict = None,
    ) -> models.ModifyLicenseOrderResponse:
        """
        编辑《主机安全-按量计费》授权订单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLicenseOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLicenseOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLicenseUnBinds(
            self,
            request: models.ModifyLicenseUnBindsRequest,
            opts: Dict = None,
    ) -> models.ModifyLicenseUnBindsResponse:
        """
        设置中心-授权管理 对某个授权批量解绑机器
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLicenseUnBinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLicenseUnBindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogKafkaAccess(
            self,
            request: models.ModifyLogKafkaAccessRequest,
            opts: Dict = None,
    ) -> models.ModifyLogKafkaAccessResponse:
        """
        新增或修改日志投递kafka接入配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogKafkaAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogKafkaAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogKafkaDeliverType(
            self,
            request: models.ModifyLogKafkaDeliverTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyLogKafkaDeliverTypeResponse:
        """
        修改指定日志类别投递配置、开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogKafkaDeliverType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogKafkaDeliverTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogKafkaState(
            self,
            request: models.ModifyLogKafkaStateRequest,
            opts: Dict = None,
    ) -> models.ModifyLogKafkaStateResponse:
        """
        修改日志投递状态信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogKafkaState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogKafkaStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogStorageConfig(
            self,
            request: models.ModifyLogStorageConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyLogStorageConfigResponse:
        """
        修改日志存储配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogStorageConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogStorageConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoginWhiteInfo(
            self,
            request: models.ModifyLoginWhiteInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyLoginWhiteInfoResponse:
        """
        更新登录审计白名单信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoginWhiteInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoginWhiteInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoginWhiteRecord(
            self,
            request: models.ModifyLoginWhiteRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyLoginWhiteRecordResponse:
        """
        更新合并后登录审计白名单信息（服务器列表数目应小于1000）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoginWhiteRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoginWhiteRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMachineAutoClearConfig(
            self,
            request: models.ModifyMachineAutoClearConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyMachineAutoClearConfigResponse:
        """
        修改机器清理配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachineAutoClearConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachineAutoClearConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMachineRemark(
            self,
            request: models.ModifyMachineRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyMachineRemarkResponse:
        """
        修改主机备注信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachineRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachineRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaliciousRequestWhiteList(
            self,
            request: models.ModifyMaliciousRequestWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyMaliciousRequestWhiteListResponse:
        """
        更新恶意请求白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaliciousRequestWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaliciousRequestWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMalwareTimingScanSettings(
            self,
            request: models.ModifyMalwareTimingScanSettingsRequest,
            opts: Dict = None,
    ) -> models.ModifyMalwareTimingScanSettingsResponse:
        """
        定时扫描设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMalwareTimingScanSettings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMalwareTimingScanSettingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMalwareWhiteList(
            self,
            request: models.ModifyMalwareWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyMalwareWhiteListResponse:
        """
        编辑木马白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMalwareWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMalwareWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetAttackSetting(
            self,
            request: models.ModifyNetAttackSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyNetAttackSettingResponse:
        """
        修改网络攻击设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetAttackSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetAttackSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetAttackWhiteList(
            self,
            request: models.ModifyNetAttackWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyNetAttackWhiteListResponse:
        """
        编辑网络攻击白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetAttackWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetAttackWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOrderAttribute(
            self,
            request: models.ModifyOrderAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyOrderAttributeResponse:
        """
        对订单属性编辑
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOrderAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOrderAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRansomDefenseEventsStatus(
            self,
            request: models.ModifyRansomDefenseEventsStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRansomDefenseEventsStatusResponse:
        """
        修改防勒索事件状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRansomDefenseEventsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRansomDefenseEventsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRansomDefenseStrategyStatus(
            self,
            request: models.ModifyRansomDefenseStrategyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRansomDefenseStrategyStatusResponse:
        """
        批量修改防勒索策略状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRansomDefenseStrategyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRansomDefenseStrategyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRaspMaxCpu(
            self,
            request: models.ModifyRaspMaxCpuRequest,
            opts: Dict = None,
    ) -> models.ModifyRaspMaxCpuResponse:
        """
        编辑漏洞防御最大cpu配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRaspMaxCpu"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRaspMaxCpuResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRaspRules(
            self,
            request: models.ModifyRaspRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyRaspRulesResponse:
        """
        添加漏洞防御白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRaspRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRaspRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReverseShellRulesAggregation(
            self,
            request: models.ModifyReverseShellRulesAggregationRequest,
            opts: Dict = None,
    ) -> models.ModifyReverseShellRulesAggregationResponse:
        """
        编辑反弹Shell规则（支持多服务器选择）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReverseShellRulesAggregation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReverseShellRulesAggregationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskDnsPolicy(
            self,
            request: models.ModifyRiskDnsPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskDnsPolicyResponse:
        """
        更改恶意请求策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskDnsPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskDnsPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskDnsPolicyStatus(
            self,
            request: models.ModifyRiskDnsPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskDnsPolicyStatusResponse:
        """
        更改恶意请求策略状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskDnsPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskDnsPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskEventsStatus(
            self,
            request: models.ModifyRiskEventsStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskEventsStatusResponse:
        """
        入侵检测所有事件的状态，包括：文件查杀，异常登录，密码破解，高危命令，反弹shell，本地提取
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskEventsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskEventsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUsersConfig(
            self,
            request: models.ModifyUsersConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyUsersConfigResponse:
        """
        用于创建/修改用户自定义配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUsersConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUsersConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulDefenceEventStatus(
            self,
            request: models.ModifyVulDefenceEventStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyVulDefenceEventStatusResponse:
        """
        修改漏洞防御事件状态（修复漏洞通过其他接口实现）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulDefenceEventStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulDefenceEventStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulDefenceSetting(
            self,
            request: models.ModifyVulDefenceSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVulDefenceSettingResponse:
        """
        修改漏洞防御插件设置
        1）新增主机自动加入，scope为1，quuids为空
        2）全量旗舰版不自动加入，scope为0，quuids为当前quuid列表，
        3）给定quuid列表，scope为0，quuids为用户选择quuid
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulDefenceSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulDefenceSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWarningHostConfig(
            self,
            request: models.ModifyWarningHostConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyWarningHostConfigResponse:
        """
        修改告警机器范围配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWarningHostConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWarningHostConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWarningSetting(
            self,
            request: models.ModifyWarningSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyWarningSettingResponse:
        """
        修改告警设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWarningSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWarningSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebHookPolicy(
            self,
            request: models.ModifyWebHookPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyWebHookPolicyResponse:
        """
        新增或修改告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebHookPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebHookPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebHookPolicyStatus(
            self,
            request: models.ModifyWebHookPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyWebHookPolicyStatusResponse:
        """
        修改告警策略开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebHookPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebHookPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebHookReceiver(
            self,
            request: models.ModifyWebHookReceiverRequest,
            opts: Dict = None,
    ) -> models.ModifyWebHookReceiverResponse:
        """
        新增或更新告警接收人
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebHookReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebHookReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebHookRule(
            self,
            request: models.ModifyWebHookRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyWebHookRuleResponse:
        """
        新增或修改企微机器人规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebHookRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebHookRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebHookRuleStatus(
            self,
            request: models.ModifyWebHookRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyWebHookRuleStatusResponse:
        """
        修改企微机器人规则状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebHookRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebHookRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebPageProtectDir(
            self,
            request: models.ModifyWebPageProtectDirRequest,
            opts: Dict = None,
    ) -> models.ModifyWebPageProtectDirResponse:
        """
        创建/修改网站防护目录
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebPageProtectDir"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebPageProtectDirResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebPageProtectSetting(
            self,
            request: models.ModifyWebPageProtectSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyWebPageProtectSettingResponse:
        """
        修改网站防护设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebPageProtectSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebPageProtectSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebPageProtectSwitch(
            self,
            request: models.ModifyWebPageProtectSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyWebPageProtectSwitchResponse:
        """
        网站防篡改防护设置开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebPageProtectSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebPageProtectSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RansomDefenseRollback(
            self,
            request: models.RansomDefenseRollbackRequest,
            opts: Dict = None,
    ) -> models.RansomDefenseRollbackResponse:
        """
        防勒索快照回滚
        """
        
        kwargs = {}
        kwargs["action"] = "RansomDefenseRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RansomDefenseRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverMalwares(
            self,
            request: models.RecoverMalwaresRequest,
            opts: Dict = None,
    ) -> models.RecoverMalwaresResponse:
        """
        本接口（RecoverMalwares）用于批量恢复已经被隔离的木马文件。
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveLocalStorageItem(
            self,
            request: models.RemoveLocalStorageItemRequest,
            opts: Dict = None,
    ) -> models.RemoveLocalStorageItemResponse:
        """
        删除本地存储数据
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveLocalStorageItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveLocalStorageItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveMachine(
            self,
            request: models.RemoveMachineRequest,
            opts: Dict = None,
    ) -> models.RemoveMachineResponse:
        """
        删除主机所有记录，目前只支持非腾讯云主机，且需要主机在离线状态
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryCreateSnapshot(
            self,
            request: models.RetryCreateSnapshotRequest,
            opts: Dict = None,
    ) -> models.RetryCreateSnapshotResponse:
        """
        快照创建失败时可以重试创建快照并且自动进行漏洞修复
        """
        
        kwargs = {}
        kwargs["action"] = "RetryCreateSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryCreateSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryVulFix(
            self,
            request: models.RetryVulFixRequest,
            opts: Dict = None,
    ) -> models.RetryVulFixResponse:
        """
        修复失败时单独对某一个主机修复漏洞
        """
        
        kwargs = {}
        kwargs["action"] = "RetryVulFix"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryVulFixResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanAsset(
            self,
            request: models.ScanAssetRequest,
            opts: Dict = None,
    ) -> models.ScanAssetResponse:
        """
        资产指纹启动扫描
        """
        
        kwargs = {}
        kwargs["action"] = "ScanAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanBaseline(
            self,
            request: models.ScanBaselineRequest,
            opts: Dict = None,
    ) -> models.ScanBaselineResponse:
        """
        基线检测与基线重新检测接口
        """
        
        kwargs = {}
        kwargs["action"] = "ScanBaseline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanBaselineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanTaskAgain(
            self,
            request: models.ScanTaskAgainRequest,
            opts: Dict = None,
    ) -> models.ScanTaskAgainResponse:
        """
        ScanTaskAgain  重新开始扫描任务，可以指定机器
        """
        
        kwargs = {}
        kwargs["action"] = "ScanTaskAgain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanTaskAgainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanVul(
            self,
            request: models.ScanVulRequest,
            opts: Dict = None,
    ) -> models.ScanVulResponse:
        """
        漏洞一键检测
        """
        
        kwargs = {}
        kwargs["action"] = "ScanVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanVulAgain(
            self,
            request: models.ScanVulAgainRequest,
            opts: Dict = None,
    ) -> models.ScanVulAgainResponse:
        """
        漏洞管理-重新检测接口
        """
        
        kwargs = {}
        kwargs["action"] = "ScanVulAgain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanVulAgainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanVulSetting(
            self,
            request: models.ScanVulSettingRequest,
            opts: Dict = None,
    ) -> models.ScanVulSettingResponse:
        """
        定期扫描漏洞设置
        """
        
        kwargs = {}
        kwargs["action"] = "ScanVulSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanVulSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchLog(
            self,
            request: models.SearchLogRequest,
            opts: Dict = None,
    ) -> models.SearchLogResponse:
        """
        查询日志
        """
        
        kwargs = {}
        kwargs["action"] = "SearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SeparateMalwares(
            self,
            request: models.SeparateMalwaresRequest,
            opts: Dict = None,
    ) -> models.SeparateMalwaresResponse:
        """
        本接口（SeparateMalwares）用于隔离木马。
        """
        
        kwargs = {}
        kwargs["action"] = "SeparateMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SeparateMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetBashEventsStatus(
            self,
            request: models.SetBashEventsStatusRequest,
            opts: Dict = None,
    ) -> models.SetBashEventsStatusResponse:
        """
        设置高危命令事件状态
        """
        
        kwargs = {}
        kwargs["action"] = "SetBashEventsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetBashEventsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLocalStorageExpire(
            self,
            request: models.SetLocalStorageExpireRequest,
            opts: Dict = None,
    ) -> models.SetLocalStorageExpireResponse:
        """
        设置本地存储过期时间
        """
        
        kwargs = {}
        kwargs["action"] = "SetLocalStorageExpire"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLocalStorageExpireResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLocalStorageItem(
            self,
            request: models.SetLocalStorageItemRequest,
            opts: Dict = None,
    ) -> models.SetLocalStorageItemResponse:
        """
        设置本地存储数据
        """
        
        kwargs = {}
        kwargs["action"] = "SetLocalStorageItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLocalStorageItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartBaselineDetect(
            self,
            request: models.StartBaselineDetectRequest,
            opts: Dict = None,
    ) -> models.StartBaselineDetectResponse:
        """
        检测基线
        """
        
        kwargs = {}
        kwargs["action"] = "StartBaselineDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartBaselineDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAssetScan(
            self,
            request: models.StopAssetScanRequest,
            opts: Dict = None,
    ) -> models.StopAssetScanResponse:
        """
        停止资产扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopAssetScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAssetScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopBaselineDetect(
            self,
            request: models.StopBaselineDetectRequest,
            opts: Dict = None,
    ) -> models.StopBaselineDetectResponse:
        """
        停止基线检测
        """
        
        kwargs = {}
        kwargs["action"] = "StopBaselineDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopBaselineDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopNoticeBanTips(
            self,
            request: models.StopNoticeBanTipsRequest,
            opts: Dict = None,
    ) -> models.StopNoticeBanTipsResponse:
        """
        不再提醒爆破阻断提示弹窗
        """
        
        kwargs = {}
        kwargs["action"] = "StopNoticeBanTips"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopNoticeBanTipsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchBashRules(
            self,
            request: models.SwitchBashRulesRequest,
            opts: Dict = None,
    ) -> models.SwitchBashRulesResponse:
        """
        切换高危命令规则状态
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchBashRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchBashRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncAssetScan(
            self,
            request: models.SyncAssetScanRequest,
            opts: Dict = None,
    ) -> models.SyncAssetScanResponse:
        """
        同步资产扫描信息
        """
        
        kwargs = {}
        kwargs["action"] = "SyncAssetScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncAssetScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncBaselineDetectSummary(
            self,
            request: models.SyncBaselineDetectSummaryRequest,
            opts: Dict = None,
    ) -> models.SyncBaselineDetectSummaryResponse:
        """
        同步基线检测进度概要
        """
        
        kwargs = {}
        kwargs["action"] = "SyncBaselineDetectSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncBaselineDetectSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncMachines(
            self,
            request: models.SyncMachinesRequest,
            opts: Dict = None,
    ) -> models.SyncMachinesResponse:
        """
        同步机器信息
        """
        
        kwargs = {}
        kwargs["action"] = "SyncMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TestWebHookRule(
            self,
            request: models.TestWebHookRuleRequest,
            opts: Dict = None,
    ) -> models.TestWebHookRuleResponse:
        """
        测试企微机器人规则
        """
        
        kwargs = {}
        kwargs["action"] = "TestWebHookRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TestWebHookRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TrustMalwares(
            self,
            request: models.TrustMalwaresRequest,
            opts: Dict = None,
    ) -> models.TrustMalwaresResponse:
        """
        本接口(TrustMalwares)将被识别木马文件设为信任。
        """
        
        kwargs = {}
        kwargs["action"] = "TrustMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TrustMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UntrustMalwares(
            self,
            request: models.UntrustMalwaresRequest,
            opts: Dict = None,
    ) -> models.UntrustMalwaresResponse:
        """
        本接口（UntrustMalwares）用于取消信任木马文件。
        """
        
        kwargs = {}
        kwargs["action"] = "UntrustMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UntrustMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateBaselineStrategy(
            self,
            request: models.UpdateBaselineStrategyRequest,
            opts: Dict = None,
    ) -> models.UpdateBaselineStrategyResponse:
        """
        根据基线策略id更新策略信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateBaselineStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateBaselineStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateMachineTags(
            self,
            request: models.UpdateMachineTagsRequest,
            opts: Dict = None,
    ) -> models.UpdateMachineTagsResponse:
        """
        关联机器标签列表
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateMachineTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateMachineTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)