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
from tencentcloud.csip.v20221121 import models
from typing import Dict


class CsipClient(AbstractClient):
    _apiVersion = '2022-11-21'
    _endpoint = 'csip.tencentcloudapi.com'
    _service = 'csip'

    async def AccessAIAnalysisSMTP(
            self,
            request: models.AccessAIAnalysisSMTPRequest,
            opts: Dict = None,
    ) -> models.AccessAIAnalysisSMTPResponse:
        """
        创建/修改SMTP邮箱接入请求
        """
        
        kwargs = {}
        kwargs["action"] = "AccessAIAnalysisSMTP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AccessAIAnalysisSMTPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddDspmAssetManager(
            self,
            request: models.AddDspmAssetManagerRequest,
            opts: Dict = None,
    ) -> models.AddDspmAssetManagerResponse:
        """
        添加资产管理员
        """
        
        kwargs = {}
        kwargs["action"] = "AddDspmAssetManager"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDspmAssetManagerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
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
        
    async def AddNewBindRoleUser(
            self,
            request: models.AddNewBindRoleUserRequest,
            opts: Dict = None,
    ) -> models.AddNewBindRoleUserResponse:
        """
        csip角色授权绑定接口
        """
        
        kwargs = {}
        kwargs["action"] = "AddNewBindRoleUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNewBindRoleUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddVulWhitelist(
            self,
            request: models.AddVulWhitelistRequest,
            opts: Dict = None,
    ) -> models.AddVulWhitelistResponse:
        """
        添加漏洞白名单
        """
        
        kwargs = {}
        kwargs["action"] = "AddVulWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddVulWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyBaselinePolicy(
            self,
            request: models.BatchModifyBaselinePolicyRequest,
            opts: Dict = None,
    ) -> models.BatchModifyBaselinePolicyResponse:
        """
        批量修改基线策略的“周期扫描配置 / 自动同步新增检测项 / 检测项命中配置 / 自定义检测项”等设置。仅修改请求中传入的字段。
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyBaselinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyBaselinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindClusterOwner(
            self,
            request: models.BindClusterOwnerRequest,
            opts: Dict = None,
    ) -> models.BindClusterOwnerResponse:
        """
        绑定集群负责人
        """
        
        kwargs = {}
        kwargs["action"] = "BindClusterOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindClusterOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelEdrAlertIgnore(
            self,
            request: models.CancelEdrAlertIgnoreRequest,
            opts: Dict = None,
    ) -> models.CancelEdrAlertIgnoreResponse:
        """
        取消已永久忽略的EDR多行为告警，从AI-Link永久忽略白名单移除对应主机+规则记录，并将告警状态恢复为待处理（PENDING）
        """
        
        kwargs = {}
        kwargs["action"] = "CancelEdrAlertIgnore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelEdrAlertIgnoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCWPExposePathPermission(
            self,
            request: models.CheckCWPExposePathPermissionRequest,
            opts: Dict = None,
    ) -> models.CheckCWPExposePathPermissionResponse:
        """
        判断当前用户是否旗舰版(适用于主机)
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCWPExposePathPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCWPExposePathPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIsUltimateVersion(
            self,
            request: models.CheckIsUltimateVersionRequest,
            opts: Dict = None,
    ) -> models.CheckIsUltimateVersionResponse:
        """
        判断当前用户是否旗舰版
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIsUltimateVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIsUltimateVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckRisk(
            self,
            request: models.CheckRiskRequest,
            opts: Dict = None,
    ) -> models.CheckRiskResponse:
        """
        风险验证示例
        """
        
        kwargs = {}
        kwargs["action"] = "CheckRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAISchedule(
            self,
            request: models.CreateAIScheduleRequest,
            opts: Dict = None,
    ) -> models.CreateAIScheduleResponse:
        """
        创建AI 定时任务。

        创建一个新的AI 定时任务，需传入任务名称、执行提示词和触发器配置。创建成功后返回AI 定时任务 ID。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAISchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessKeyCheckTask(
            self,
            request: models.CreateAccessKeyCheckTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAccessKeyCheckTaskResponse:
        """
        检测AK 异步任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessKeyCheckTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessKeyCheckTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessKeySyncTask(
            self,
            request: models.CreateAccessKeySyncTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAccessKeySyncTaskResponse:
        """
        发起AK资产同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessKeySyncTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessKeySyncTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAllAssetsExportJob(
            self,
            request: models.CreateAllAssetsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAllAssetsExportJobResponse:
        """
        创建全部资产导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAllAssetsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAllAssetsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetFilterView(
            self,
            request: models.CreateAssetFilterViewRequest,
            opts: Dict = None,
    ) -> models.CreateAssetFilterViewResponse:
        """
        创建资产搜索视图
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetFilterView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetFilterViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetProcessExportJob(
            self,
            request: models.CreateAssetProcessExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAssetProcessExportJobResponse:
        """
        创建主机进程列表导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetProcessExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetProcessExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetSyncTask(
            self,
            request: models.CreateAssetSyncTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAssetSyncTaskResponse:
        """
        创建资产同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetSyncTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetSyncTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetTag(
            self,
            request: models.CreateAssetTagRequest,
            opts: Dict = None,
    ) -> models.CreateAssetTagResponse:
        """
        创建资产标签
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetViewRisksExportJob(
            self,
            request: models.CreateAssetViewRisksExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAssetViewRisksExportJobResponse:
        """
        创建资产视角下风险列表导出任务示例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetViewRisksExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetViewRisksExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaselineAggregatedItemExportJob(
            self,
            request: models.CreateBaselineAggregatedItemExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateBaselineAggregatedItemExportJobResponse:
        """
        创建基线聚合检测项导出任务。通过 ExportType 选择导出统计结果或风险明细，可按策略、分类等条件限定范围；任务在后台异步执行，完成后可在导出任务列表中下载结果文件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaselineAggregatedItemExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaselineAggregatedItemExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaselineFixRecordExportJob(
            self,
            request: models.CreateBaselineFixRecordExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateBaselineFixRecordExportJobResponse:
        """
        创建基线修复记录导出任务，导出已修复检测项的记录数据（含检测项信息、资产信息、修复时间等）。任务在后台异步执行，完成后可在导出任务列表中下载结果文件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaselineFixRecordExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaselineFixRecordExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaselineMainTaskExportJob(
            self,
            request: models.CreateBaselineMainTaskExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateBaselineMainTaskExportJobResponse:
        """
        创建基线主任务导出任务，导出指定主任务下的检测项与子任务数据。任务在后台异步执行，完成后可在导出任务列表中下载结果文件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaselineMainTaskExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaselineMainTaskExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCFGRiskPDFReportExportJob(
            self,
            request: models.CreateCFGRiskPDFReportExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateCFGRiskPDFReportExportJobResponse:
        """
        创建云资源配置检测PDF报告导出任务示例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCFGRiskPDFReportExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCFGRiskPDFReportExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCFGRisksExportJob(
            self,
            request: models.CreateCFGRisksExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateCFGRisksExportJobResponse:
        """
        创建资产视角下风险列表导出任务示例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCFGRisksExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCFGRisksExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCSIPManualMalwareScan(
            self,
            request: models.CreateCSIPManualMalwareScanRequest,
            opts: Dict = None,
    ) -> models.CreateCSIPManualMalwareScanResponse:
        """
        CSIP 手动扫描创建接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCSIPManualMalwareScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCSIPManualMalwareScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCheckViewRisksExportJob(
            self,
            request: models.CreateCheckViewRisksExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateCheckViewRisksExportJobResponse:
        """
        创建资产视角下风险列表导出任务示例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCheckViewRisksExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCheckViewRisksExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudFunctionExportJob(
            self,
            request: models.CreateCloudFunctionExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateCloudFunctionExportJobResponse:
        """
        创建云函数导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudFunctionExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudFunctionExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterAssetSyncTask(
            self,
            request: models.CreateClusterAssetSyncTaskRequest,
            opts: Dict = None,
    ) -> models.CreateClusterAssetSyncTaskResponse:
        """
        创建集群资产同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterAssetSyncTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterAssetSyncTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterContainerListExportJob(
            self,
            request: models.CreateClusterContainerListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateClusterContainerListExportJobResponse:
        """
        创建集群容器列表导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterContainerListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterContainerListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterListExportJob(
            self,
            request: models.CreateClusterListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateClusterListExportJobResponse:
        """
        创建集群列表导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterNamespaceListExportJob(
            self,
            request: models.CreateClusterNamespaceListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateClusterNamespaceListExportJobResponse:
        """
        创建集群命名空间列表导出任务。导出字段包含命名空间名称、Labels、创建时间。支持Filter过滤。导出通过异步任务实现，返回JobId后前端轮询查询导出任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterNamespaceListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterNamespaceListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterNodeListExportJob(
            self,
            request: models.CreateClusterNodeListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateClusterNodeListExportJobResponse:
        """
        创建集群节点列表导出任务。导出字段包含节点ID、节点名称、公网IP、内网IP、节点类型、核数、客户端状态、运行状态。NodeType和ClientStatus、RunStatus均经过国际化翻译。支持Filter过滤（含ClientStatus内存过滤）。导出通过异步任务实现，返回JobId后前端轮询查询导出任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterNodeListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterNodeListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateComplianceRiskExportJob(
            self,
            request: models.CreateComplianceRiskExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateComplianceRiskExportJobResponse:
        """
        创建合规标准聚合视角下风险列表导出任务示例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateComplianceRiskExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateComplianceRiskExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosAssetSyncTask(
            self,
            request: models.CreateCosAssetSyncTaskRequest,
            opts: Dict = None,
    ) -> models.CreateCosAssetSyncTaskResponse:
        """
        创建资产同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosAssetSyncTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosAssetSyncTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosObjectScanTask(
            self,
            request: models.CreateCosObjectScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateCosObjectScanTaskResponse:
        """
        创建cos病毒扫描、敏感数据识别任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosObjectScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosObjectScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosPolicy(
            self,
            request: models.CreateCosPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateCosPolicyResponse:
        """
        添加cos告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosRiskScanTask(
            self,
            request: models.CreateCosRiskScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateCosRiskScanTaskResponse:
        """
        创建风险监测任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosRiskScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosRiskScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainAndIp(
            self,
            request: models.CreateDomainAndIpRequest,
            opts: Dict = None,
    ) -> models.CreateDomainAndIpResponse:
        """
        创建域名、ip相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainAndIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainAndIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmAccessExportJob(
            self,
            request: models.CreateDspmAccessExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmAccessExportJobResponse:
        """
        创建Dspm访问记录导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmAccessExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmAccessExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmApplyOrder(
            self,
            request: models.CreateDspmApplyOrderRequest,
            opts: Dict = None,
    ) -> models.CreateDspmApplyOrderResponse:
        """
        创建Dspm申请单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmApplyOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmApplyOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmApproveHistoryExportJob(
            self,
            request: models.CreateDspmApproveHistoryExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmApproveHistoryExportJobResponse:
        """
        创建Dspm审批历史导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmApproveHistoryExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmApproveHistoryExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmAssetAccessTopologyExportJob(
            self,
            request: models.CreateDspmAssetAccessTopologyExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmAssetAccessTopologyExportJobResponse:
        """
        创建Dspm资产访问拓扑导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmAssetAccessTopologyExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmAssetAccessTopologyExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmAssetIdentifyInfoExportJob(
            self,
            request: models.CreateDspmAssetIdentifyInfoExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmAssetIdentifyInfoExportJobResponse:
        """
        创建Dspm资产列表导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmAssetIdentifyInfoExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmAssetIdentifyInfoExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmAssetsExportJob(
            self,
            request: models.CreateDspmAssetsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmAssetsExportJobResponse:
        """
        创建Dspm资产列表导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmAssetsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmAssetsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmExportTask(
            self,
            request: models.CreateDspmExportTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDspmExportTaskResponse:
        """
        创建日志导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmExportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmExportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyCategory(
            self,
            request: models.CreateDspmIdentifyCategoryRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyCategoryResponse:
        """
        创建dspm数据识别分类
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyComplianceCategoryRelation(
            self,
            request: models.CreateDspmIdentifyComplianceCategoryRelationRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyComplianceCategoryRelationResponse:
        """
        创建dspm数据识别模板分类关联
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyComplianceCategoryRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyComplianceCategoryRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyComplianceGroup(
            self,
            request: models.CreateDspmIdentifyComplianceGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyComplianceGroupResponse:
        """
        创建dspm数据识别模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyComplianceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyComplianceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyComplianceGroupCopy(
            self,
            request: models.CreateDspmIdentifyComplianceGroupCopyRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyComplianceGroupCopyResponse:
        """
        复制dspm数据识别模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyComplianceGroupCopy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyComplianceGroupCopyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyComplianceRuleRelation(
            self,
            request: models.CreateDspmIdentifyComplianceRuleRelationRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyComplianceRuleRelationResponse:
        """
        创建dspm数据识别模板数据项关联
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyComplianceRuleRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyComplianceRuleRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyInfoListExportJob(
            self,
            request: models.CreateDspmIdentifyInfoListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyInfoListExportJobResponse:
        """
        创建Dspm身份列表导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyInfoListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyInfoListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyLevelGroup(
            self,
            request: models.CreateDspmIdentifyLevelGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyLevelGroupResponse:
        """
        创建dspm数据识别分级组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyLevelGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyLevelGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyRule(
            self,
            request: models.CreateDspmIdentifyRuleRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyRuleResponse:
        """
        创建dspm数据识别数据项
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmPersonalIdentify(
            self,
            request: models.CreateDspmPersonalIdentifyRequest,
            opts: Dict = None,
    ) -> models.CreateDspmPersonalIdentifyResponse:
        """
        创建Dspm个人身份id
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmPersonalIdentify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmPersonalIdentifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmRiskExportJob(
            self,
            request: models.CreateDspmRiskExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmRiskExportJobResponse:
        """
        创建Dspm风险导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmRiskExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmRiskExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmWhitelistStrategy(
            self,
            request: models.CreateDspmWhitelistStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateDspmWhitelistStrategyResponse:
        """
        创建Dspm白名单策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmWhitelistStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmWhitelistStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDynamicAssetsExportJob(
            self,
            request: models.CreateDynamicAssetsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDynamicAssetsExportJobResponse:
        """
        创建公网资产导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDynamicAssetsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDynamicAssetsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEDRManualScan(
            self,
            request: models.CreateEDRManualScanRequest,
            opts: Dict = None,
    ) -> models.CreateEDRManualScanResponse:
        """
        点击开始扫描后触发，支持多账号、多资产类型。同时选主机和容器集群时拆分为两个独立任务（主机+容器）。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEDRManualScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEDRManualScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdrAlertExportJob(
            self,
            request: models.CreateEdrAlertExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateEdrAlertExportJobResponse:
        """
        创建EDR告警导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdrAlertExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdrAlertExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdrLessAlertExportJob(
            self,
            request: models.CreateEdrLessAlertExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateEdrLessAlertExportJobResponse:
        """
        创建EDR告警普通导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdrLessAlertExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdrLessAlertExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExposureAutoTagRule(
            self,
            request: models.CreateExposureAutoTagRuleRequest,
            opts: Dict = None,
    ) -> models.CreateExposureAutoTagRuleResponse:
        """
        云边界自动打标-创建规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExposureAutoTagRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExposureAutoTagRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExposuresExportJob(
            self,
            request: models.CreateExposuresExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateExposuresExportJobResponse:
        """
        暴露资产导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExposuresExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExposuresExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHighBaseLineRisksExportJob(
            self,
            request: models.CreateHighBaseLineRisksExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateHighBaseLineRisksExportJobResponse:
        """
        创建高危基线风险导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHighBaseLineRisksExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHighBaseLineRisksExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHostVulExportJob(
            self,
            request: models.CreateHostVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateHostVulExportJobResponse:
        """
        创建主机列漏洞表导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHostVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIaCAccessToken(
            self,
            request: models.CreateIaCAccessTokenRequest,
            opts: Dict = None,
    ) -> models.CreateIaCAccessTokenResponse:
        """
        创建IaC检测接入Token
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIaCAccessToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIaCAccessTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIaCFileExportJob(
            self,
            request: models.CreateIaCFileExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateIaCFileExportJobResponse:
        """
        创建IaC检测文件导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIaCFileExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIaCFileExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIaCFileReScanTask(
            self,
            request: models.CreateIaCFileReScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateIaCFileReScanTaskResponse:
        """
        创建IaC检测文件重新扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIaCFileReScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIaCFileReScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePodContainerListExportJob(
            self,
            request: models.CreatePodContainerListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreatePodContainerListExportJobResponse:
        """
        创建Pod关联容器列表导出任务。导出字段包含容器ID、容器名称、运行状态、节点ID、节点类型、镜像ID、镜像名称、隔离状态。支持Filter过滤。导出通过异步任务实现，返回JobId后前端轮询查询导出任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePodContainerListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePodContainerListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePodServiceListExportJob(
            self,
            request: models.CreatePodServiceListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreatePodServiceListExportJobResponse:
        """
        创建Pod关联服务列表导出任务。导出字段包含服务名称、类型、Selector、命名空间、创建时间。支持Filter过滤。当传入PodUniqueID时，复用DescribeClusterServiceList的Pod关联匹配逻辑。导出通过异步任务实现，返回JobId后前端轮询查询导出任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePodServiceListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePodServiceListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePublicAssetsExportJob(
            self,
            request: models.CreatePublicAssetsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreatePublicAssetsExportJobResponse:
        """
        创建公网资产导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePublicAssetsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePublicAssetsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRiskCenterScanTask(
            self,
            request: models.CreateRiskCenterScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRiskCenterScanTaskResponse:
        """
        创建风险中心扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRiskCenterScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRiskCenterScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRiskDetailExportJob(
            self,
            request: models.CreateRiskDetailExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateRiskDetailExportJobResponse:
        """
        创建云资源配置检查风险详情导出任务示例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRiskDetailExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRiskDetailExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScanStatisticExportJob(
            self,
            request: models.CreateScanStatisticExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateScanStatisticExportJobResponse:
        """
        暴露面扫描结果导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScanStatisticExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScanStatisticExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScanTask(
            self,
            request: models.CreateScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateScanTaskResponse:
        """
        创建立即检测任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSkillScan(
            self,
            request: models.CreateSkillScanRequest,
            opts: Dict = None,
    ) -> models.CreateSkillScanResponse:
        """
        上传 Skill ZIP 文件，触发异步安全检测。上传成功后应使用返回的 ContentHash + EngineVersion 轮询 DescribeSkillScanResult 接口获取结果。上传接口具备幂等性，同一 Hash 的文件重复上传不会创建重复任务。检测结果保留90天，超期后需重新上传检测。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSkillScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSkillScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulFixRetryTask(
            self,
            request: models.CreateVulFixRetryTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVulFixRetryTaskResponse:
        """
        对修复失败的漏洞修复任务进行重试，仅针对原任务中修复失败的主机重新下发修复指令。仅当任务状态为部分修复失败或全部修复失败时允许重试。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulFixRetryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulFixRetryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulFixTask(
            self,
            request: models.CreateVulFixTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVulFixTaskResponse:
        """
        用户手动提交漏洞修复任务，指定需要修复的漏洞和目标主机，系统创建修复任务并下发执行。支持指定修复超时时间、是否创建快照等选项。通过FixItems数组精确控制每个漏洞/KB补丁修复哪些主机。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulFixTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulFixTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulFixedExportJob(
            self,
            request: models.CreateVulFixedExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulFixedExportJobResponse:
        """
        创建已修复漏洞列表的导出任务。支持与 DescribeVulFixedList 相同的过滤条件，导出通过异步任务实现，返回 JobID 后前端轮询查询导出任务状态。导出字段包含漏洞ID、漏洞名称、漏洞等级、VPR评级、漏洞类型、CVE编号、主机名称、实例ID、关联组件&路径、修复时间。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulFixedExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulFixedExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulReScan(
            self,
            request: models.CreateVulReScanRequest,
            opts: Dict = None,
    ) -> models.CreateVulReScanResponse:
        """
        创建漏洞重新扫描
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulReScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulReScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulRisksExportJob(
            self,
            request: models.CreateVulRisksExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulRisksExportJobResponse:
        """
        创建漏洞风险导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulRisksExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulRisksExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulScanManual(
            self,
            request: models.CreateVulScanManualRequest,
            opts: Dict = None,
    ) -> models.CreateVulScanManualResponse:
        """
        创建漏洞扫描（一键扫描）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulScanManual"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulScanManualResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIAnalysisSMTPAccess(
            self,
            request: models.DeleteAIAnalysisSMTPAccessRequest,
            opts: Dict = None,
    ) -> models.DeleteAIAnalysisSMTPAccessResponse:
        """
        删除AI助手的SMTP邮箱接入信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIAnalysisSMTPAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIAnalysisSMTPAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAISchedule(
            self,
            request: models.DeleteAIScheduleRequest,
            opts: Dict = None,
    ) -> models.DeleteAIScheduleResponse:
        """
        删除AI 定时任务。

        根据指定的AI 定时任务 ID 删除对应的定时任务。删除后不可恢复。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAISchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAssetFilterView(
            self,
            request: models.DeleteAssetFilterViewRequest,
            opts: Dict = None,
    ) -> models.DeleteAssetFilterViewResponse:
        """
        删除用户创建的指定资产搜索视图
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAssetFilterView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAssetFilterViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAssetTag(
            self,
            request: models.DeleteAssetTagRequest,
            opts: Dict = None,
    ) -> models.DeleteAssetTagResponse:
        """
        删除资产标签
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAssetTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAssetTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCSIPMalwareScanTask(
            self,
            request: models.DeleteCSIPMalwareScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteCSIPMalwareScanTaskResponse:
        """
        CSIP 手动扫描任务删除接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCSIPMalwareScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCSIPMalwareScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        删除集群
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCosAkAsset(
            self,
            request: models.DeleteCosAkAssetRequest,
            opts: Dict = None,
    ) -> models.DeleteCosAkAssetResponse:
        """
        删除已删除的cos ak资产
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCosAkAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCosAkAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCosPolicy(
            self,
            request: models.DeleteCosPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteCosPolicyResponse:
        """
        删除策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCosPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCosPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainAndIp(
            self,
            request: models.DeleteDomainAndIpRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainAndIpResponse:
        """
        删除域名和ip请求
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainAndIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainAndIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmApplyOrder(
            self,
            request: models.DeleteDspmApplyOrderRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmApplyOrderResponse:
        """
        删除Dspm申请单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmApplyOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmApplyOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmAssetAccount(
            self,
            request: models.DeleteDspmAssetAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmAssetAccountResponse:
        """
        删除Dspm资产账号
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmAssetAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmAssetAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmBackupLogList(
            self,
            request: models.DeleteDspmBackupLogListRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmBackupLogListResponse:
        """
        删除备份日志
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmBackupLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmBackupLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmExportTask(
            self,
            request: models.DeleteDspmExportTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmExportTaskResponse:
        """
        删除导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmExportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmExportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyCategory(
            self,
            request: models.DeleteDspmIdentifyCategoryRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyCategoryResponse:
        """
        删除dspm数据识别分类
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyComplianceCategoryRelation(
            self,
            request: models.DeleteDspmIdentifyComplianceCategoryRelationRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyComplianceCategoryRelationResponse:
        """
        删除dspm数据识别模板分类关联
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyComplianceCategoryRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyComplianceCategoryRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyComplianceGroup(
            self,
            request: models.DeleteDspmIdentifyComplianceGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyComplianceGroupResponse:
        """
        删除dspm数据识别模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyComplianceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyComplianceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyComplianceRuleRelation(
            self,
            request: models.DeleteDspmIdentifyComplianceRuleRelationRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyComplianceRuleRelationResponse:
        """
        删除dspm数据识别模板数据项关联
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyComplianceRuleRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyComplianceRuleRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyLevelGroup(
            self,
            request: models.DeleteDspmIdentifyLevelGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyLevelGroupResponse:
        """
        删除dspm数据识别分级组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyLevelGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyLevelGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyRule(
            self,
            request: models.DeleteDspmIdentifyRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyRuleResponse:
        """
        删除dspm数据识别数据项
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmPersonalIdentify(
            self,
            request: models.DeleteDspmPersonalIdentifyRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmPersonalIdentifyResponse:
        """
        删除Dspm个人身份id
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmPersonalIdentify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmPersonalIdentifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmRestoreLogList(
            self,
            request: models.DeleteDspmRestoreLogListRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmRestoreLogListResponse:
        """
        删除恢复日志
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmRestoreLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmRestoreLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmWhitelistStrategy(
            self,
            request: models.DeleteDspmWhitelistStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmWhitelistStrategyResponse:
        """
        删除Dspm白名单策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmWhitelistStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmWhitelistStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEDRRules(
            self,
            request: models.DeleteEDRRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteEDRRulesResponse:
        """
        删除EDR策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEDRRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEDRRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEDRScanTask(
            self,
            request: models.DeleteEDRScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteEDRScanTaskResponse:
        """
        删除已终止的扫描任务（物理删除主表及明细表）。只允许删除终态任务，只有创建者可操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEDRScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEDRScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEdrLogCollectPaths(
            self,
            request: models.DeleteEdrLogCollectPathsRequest,
            opts: Dict = None,
    ) -> models.DeleteEdrLogCollectPathsResponse:
        """
        批量删除EDR日志采集路径配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEdrLogCollectPaths"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEdrLogCollectPathsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteExposureAutoTagRule(
            self,
            request: models.DeleteExposureAutoTagRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteExposureAutoTagRuleResponse:
        """
        云边界自动打标-删除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteExposureAutoTagRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteExposureAutoTagRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIaCAccessToken(
            self,
            request: models.DeleteIaCAccessTokenRequest,
            opts: Dict = None,
    ) -> models.DeleteIaCAccessTokenResponse:
        """
        删除IaC检测接入Token
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIaCAccessToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIaCAccessTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIaCFile(
            self,
            request: models.DeleteIaCFileRequest,
            opts: Dict = None,
    ) -> models.DeleteIaCFileResponse:
        """
        删除IaC检测文件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIaCFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIaCFileResponse
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
        
    async def DeleteRiskScanTask(
            self,
            request: models.DeleteRiskScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskScanTaskResponse:
        """
        删除风险中心扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVulWhitelist(
            self,
            request: models.DeleteVulWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteVulWhitelistResponse:
        """
        删除漏洞白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVulWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVulWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAgentAssetList(
            self,
            request: models.DescribeAIAgentAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAgentAssetListResponse:
        """
        获取 AI agent 资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAgentAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAgentAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisFileDownloadURL(
            self,
            request: models.DescribeAIAnalysisFileDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisFileDownloadURLResponse:
        """
        获取 AI 分析文件的临时下载链接。

        传入文件的原始地址，返回带签名的临时下载链接，链接有效期为 2 小时。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisFileDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisFileDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisHistory(
            self,
            request: models.DescribeAIAnalysisHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisHistoryResponse:
        """
        获取云安全AI助手历史分析记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisRecommendQuestions(
            self,
            request: models.DescribeAIAnalysisRecommendQuestionsRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisRecommendQuestionsResponse:
        """
        获取AI问答推荐问题
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisRecommendQuestions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisRecommendQuestionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisRobotInfo(
            self,
            request: models.DescribeAIAnalysisRobotInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisRobotInfoResponse:
        """
        获取云安全AI助手基础信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisRobotInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisRobotInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisSMTP(
            self,
            request: models.DescribeAIAnalysisSMTPRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisSMTPResponse:
        """
        查询AI助手的SMTP邮箱接入信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisSMTP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisSMTPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAILinkSetting(
            self,
            request: models.DescribeAILinkSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeAILinkSettingResponse:
        """
        查询AI-Link智链引擎配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAILinkSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAILinkSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIScheduleList(
            self,
            request: models.DescribeAIScheduleListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIScheduleListResponse:
        """
        查询AI 定时任务列表。

        支持分页查询和状态过滤，返回定时任务列表及总条数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIScheduleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIScheduleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAISchedulePlanList(
            self,
            request: models.DescribeAISchedulePlanListRequest,
            opts: Dict = None,
    ) -> models.DescribeAISchedulePlanListResponse:
        """
        查询AI 定时任务触发计划。

        查询指定AI 定时任务在给定时间窗口内的未来触发计划列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAISchedulePlanList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAISchedulePlanListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIScheduleStats(
            self,
            request: models.DescribeAIScheduleStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeAIScheduleStatsResponse:
        """
        查询AI 定时任务统计信息。

        返回当前用户的定时任务总数和当前运行中的任务数量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIScheduleStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIScheduleStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIScheduleTaskDetail(
            self,
            request: models.DescribeAIScheduleTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAIScheduleTaskDetailResponse:
        """
        查询AI 定时任务执行详情。

        根据任务 ID 查询指定执行任务的详细信息，包括执行状态、结果等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIScheduleTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIScheduleTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIScheduleTaskList(
            self,
            request: models.DescribeAIScheduleTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIScheduleTaskListResponse:
        """
        查询AI 定时任务执行列表。

        查询AI 定时任务的历史执行记录，支持分页和按定时任务 ID 过滤。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIScheduleTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIScheduleTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAKAnalysisDetail(
            self,
            request: models.DescribeAKAnalysisDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAKAnalysisDetailResponse:
        """
        访问密钥告警记录AI分析结果详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAKAnalysisDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAKAnalysisDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbTestUser(
            self,
            request: models.DescribeAbTestUserRequest,
            opts: Dict = None,
    ) -> models.DescribeAbTestUserResponse:
        """
        判断用户是否灰度用户
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbTestUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbTestUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalCallRecord(
            self,
            request: models.DescribeAbnormalCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalCallRecordResponse:
        """
        获取调用记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalCallRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalCallRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyAlarm(
            self,
            request: models.DescribeAccessKeyAlarmRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyAlarmResponse:
        """
        访问密钥告警记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyAlarmDetail(
            self,
            request: models.DescribeAccessKeyAlarmDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyAlarmDetailResponse:
        """
        访问密钥告警记录详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyAlarmDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyAlarmDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyAsset(
            self,
            request: models.DescribeAccessKeyAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyAssetResponse:
        """
        获取用户访问密钥资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyRisk(
            self,
            request: models.DescribeAccessKeyRiskRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyRiskResponse:
        """
        访问密钥风险记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyRiskDetail(
            self,
            request: models.DescribeAccessKeyRiskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyRiskDetailResponse:
        """
        访问密钥风险记录详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyRiskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyRiskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyUserDetail(
            self,
            request: models.DescribeAccessKeyUserDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyUserDetailResponse:
        """
        查询用户的账号详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyUserDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyUserDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyUserList(
            self,
            request: models.DescribeAccessKeyUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyUserListResponse:
        """
        查询用户的账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentConfigSetting(
            self,
            request: models.DescribeAgentConfigSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentConfigSettingResponse:
        """
        查询客户端配置设置（配置组），从DescribeAgentRunMode拆分出的独立接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentConfigSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentConfigSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentRunMode(
            self,
            request: models.DescribeAgentRunModeRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentRunModeResponse:
        """
        获取客户端运行模式和运行配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentRunMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentRunModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentRunPolicy(
            self,
            request: models.DescribeAgentRunPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentRunPolicyResponse:
        """
        查询客户端运行策略（策略组），从DescribeAgentRunMode拆分出的独立接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentRunPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentRunPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlertList(
            self,
            request: models.DescribeAlertListRequest,
            opts: Dict = None,
    ) -> models.DescribeAlertListResponse:
        """
        告警中心全量告警列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDetail(
            self,
            request: models.DescribeAssetDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDetailResponse:
        """
        资产详情信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetFilterViews(
            self,
            request: models.DescribeAssetFilterViewsRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetFilterViewsResponse:
        """
        资产搜索视图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetFilterViews"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetFilterViewsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetInfo(
            self,
            request: models.DescribeAssetInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetInfoResponse:
        """
        资产信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetLastSyncTime(
            self,
            request: models.DescribeAssetLastSyncTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetLastSyncTimeResponse:
        """
        资产最近同步时间
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetLastSyncTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetLastSyncTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetOverview(
            self,
            request: models.DescribeAssetOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetOverviewResponse:
        """
        资产概览统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetProcessList(
            self,
            request: models.DescribeAssetProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetProcessListResponse:
        """
        查询云边界分析-暴露路径下主机节点的进程列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetRiskDetail(
            self,
            request: models.DescribeAssetRiskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetRiskDetailResponse:
        """
        资产风险详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetRiskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetRiskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetRiskList(
            self,
            request: models.DescribeAssetRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetRiskListResponse:
        """
        资产视角下云资源配置风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSyncTaskStatus(
            self,
            request: models.DescribeAssetSyncTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSyncTaskStatusResponse:
        """
        资产同步任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSyncTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSyncTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTagAttributes(
            self,
            request: models.DescribeAssetTagAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTagAttributesResponse:
        """
        获取资产标签属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTagAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTagAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTagTree(
            self,
            request: models.DescribeAssetTagTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTagTreeResponse:
        """
        资产标签树结构数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTagTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTagTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTags(
            self,
            request: models.DescribeAssetTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTagsResponse:
        """
        全部资产
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTree(
            self,
            request: models.DescribeAssetTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTreeResponse:
        """
        资产树结构
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetViewVulRiskList(
            self,
            request: models.DescribeAssetViewVulRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetViewVulRiskListResponse:
        """
        获取资产视角的漏洞风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetViewVulRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetViewVulRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssumeRole(
            self,
            request: models.DescribeAssumeRoleRequest,
            opts: Dict = None,
    ) -> models.DescribeAssumeRoleResponse:
        """
        查询是否绑定角色
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssumeRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssumeRoleResponse
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
        
    async def DescribeBaselineAggregatedItemList(
            self,
            request: models.DescribeBaselineAggregatedItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineAggregatedItemListResponse:
        """
        获取检测项维度的聚合扫描结果列表，用于策略详情页“检测项”Tab 按检测项展示通过/未通过资产数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineAggregatedItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineAggregatedItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineAggregatedPolicyList(
            self,
            request: models.DescribeBaselineAggregatedPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineAggregatedPolicyListResponse:
        """
        获取基线策略维度的聚合扫描结果列表，用于概览页“基线扫描策略”模块按策略展示通过/未通过情况。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineAggregatedPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineAggregatedPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineCategoryItemList(
            self,
            request: models.DescribeBaselineCategoryItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineCategoryItemListResponse:
        """
        获取分类检测项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineCategoryItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineCategoryItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineItemRiskList(
            self,
            request: models.DescribeBaselineItemRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineItemRiskListResponse:
        """
        获取检测项维度的风险记录列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineItemRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineItemRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineMainTaskItemList(
            self,
            request: models.DescribeBaselineMainTaskItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineMainTaskItemListResponse:
        """
        获取系统内置基线分类的检测项列表（父分类 → 子分类 → 内置检测项 ID 列表），用于策略编辑页选择基线检测项。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineMainTaskItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineMainTaskItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineMainTaskList(
            self,
            request: models.DescribeBaselineMainTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineMainTaskListResponse:
        """
        获取扫描主任务列表，用于“任务记录”页展示一键扫描 / 周期扫描 / 分散扫描的历史记录及结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineMainTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineMainTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineOverview(
            self,
            request: models.DescribeBaselineOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineOverviewResponse:
        """
        获取基线概览页的头部数据，含未通过检测项总数、近一年修复数、最近一次扫描时间、当前是否启用周期扫描等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselinePolicyList(
            self,
            request: models.DescribeBaselinePolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselinePolicyListResponse:
        """
        获取基线策略列表，用于“周期计划管理”等列表页展示系统/自定义策略及其配置情况。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselinePolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselinePolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineSyncConf(
            self,
            request: models.DescribeBaselineSyncConfRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineSyncConfResponse:
        """
        获取当前账号（管理员）的基线同步配置。仅集团管理员可调用，普通成员账号请使用 DescribeBaselineUserOtherConf。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineSyncConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineSyncConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineSystemCategoryList(
            self,
            request: models.DescribeBaselineSystemCategoryListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineSystemCategoryListResponse:
        """
        获取系统内置基线分类树（父分类 → 子分类 → 内置检测项 ID 列表），用于策略编辑页选择基线检测项。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineSystemCategoryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineSystemCategoryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineUserOtherConf(
            self,
            request: models.DescribeBaselineUserOtherConfRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineUserOtherConfResponse:
        """
        获取当前账号的用户级基线配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineUserOtherConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineUserOtherConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineUserWeakPasswordConf(
            self,
            request: models.DescribeBaselineUserWeakPasswordConfRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineUserWeakPasswordConfResponse:
        """
        获取当前账号的“用户弱口令”自定义字典（服务端解密后返回明文）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineUserWeakPasswordConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineUserWeakPasswordConfResponse
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
        
    async def DescribeBucketInvokeIpList(
            self,
            request: models.DescribeBucketInvokeIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeBucketInvokeIpListResponse:
        """
        查看存储桶调用源ip列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBucketInvokeIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBucketInvokeIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCFGRiskReportStatistics(
            self,
            request: models.DescribeCFGRiskReportStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeCFGRiskReportStatisticsResponse:
        """
        云资源配置检查报告风险统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCFGRiskReportStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCFGRiskReportStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCFGRiskStatistics(
            self,
            request: models.DescribeCFGRiskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeCFGRiskStatisticsResponse:
        """
        获取扫描结果统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCFGRiskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCFGRiskStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCFWAssetStatistics(
            self,
            request: models.DescribeCFWAssetStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeCFWAssetStatisticsResponse:
        """
        云防资产中心统计数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCFWAssetStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCFWAssetStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCLSLogIndexV3(
            self,
            request: models.DescribeCLSLogIndexV3Request,
            opts: Dict = None,
    ) -> models.DescribeCLSLogIndexV3Response:
        """
        获取日志索引信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSLogIndexV3"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSLogIndexV3Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCLSLogListV3(
            self,
            request: models.DescribeCLSLogListV3Request,
            opts: Dict = None,
    ) -> models.DescribeCLSLogListV3Response:
        """
        日志分析检索接口v3
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSLogListV3"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSLogListV3Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSIPMalwareScanTaskDetail(
            self,
            request: models.DescribeCSIPMalwareScanTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCSIPMalwareScanTaskDetailResponse:
        """
        CSIP 扫描任务主机详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSIPMalwareScanTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSIPMalwareScanTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSIPMalwareScanTaskProgress(
            self,
            request: models.DescribeCSIPMalwareScanTaskProgressRequest,
            opts: Dict = None,
    ) -> models.DescribeCSIPMalwareScanTaskProgressResponse:
        """
        CSIP 手动扫描进度查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSIPMalwareScanTaskProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSIPMalwareScanTaskProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSIPRiskStatistics(
            self,
            request: models.DescribeCSIPRiskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeCSIPRiskStatisticsResponse:
        """
        获取风险中心风险概况示例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSIPRiskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSIPRiskStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCVMAssetInfo(
            self,
            request: models.DescribeCVMAssetInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCVMAssetInfoResponse:
        """
        cvm详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCVMAssetInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCVMAssetInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCVMAssets(
            self,
            request: models.DescribeCVMAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeCVMAssetsResponse:
        """
        获取cvm列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCVMAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCVMAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPExposePath(
            self,
            request: models.DescribeCWPExposePathRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPExposePathResponse:
        """
        查询云边界分析路径节点(主机专用)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPExposePath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPExposePathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPExposures(
            self,
            request: models.DescribeCWPExposuresRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPExposuresResponse:
        """
        云边界分析资产列表(适用于主机资产)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPExposures"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPExposuresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPLicenseBindSchedule(
            self,
            request: models.DescribeCWPLicenseBindScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPLicenseBindScheduleResponse:
        """
        查询授权绑定任务的进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPLicenseBindSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPLicenseBindScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPMachineDetail(
            self,
            request: models.DescribeCWPMachineDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPMachineDetailResponse:
        """
        主机详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPMachineDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPMachineDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPMachineOsList(
            self,
            request: models.DescribeCWPMachineOsListRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPMachineOsListResponse:
        """
        查询可筛选操作系统列表.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPMachineOsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPMachineOsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPMachines(
            self,
            request: models.DescribeCWPMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPMachinesResponse:
        """
        主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPOrderList(
            self,
            request: models.DescribeCWPOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPOrderListResponse:
        """
        查询资源订单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPScanIpInfo(
            self,
            request: models.DescribeCWPScanIpInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPScanIpInfoResponse:
        """
        查询腾讯云扫描IP信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPScanIpInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPScanIpInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPTaskDuration(
            self,
            request: models.DescribeCWPTaskDurationRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPTaskDurationResponse:
        """
        获取任务下发时长
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPTaskDuration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPTaskDurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallRecord(
            self,
            request: models.DescribeCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeCallRecordResponse:
        """
        获取调用记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckViewRisks(
            self,
            request: models.DescribeCheckViewRisksRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckViewRisksResponse:
        """
        检查视角下云资源配置风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckViewRisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckViewRisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClbListenerList(
            self,
            request: models.DescribeClbListenerListRequest,
            opts: Dict = None,
    ) -> models.DescribeClbListenerListResponse:
        """
        查询腾讯云指定CLB实例对应的监听器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClbListenerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClbListenerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClbListenerRules(
            self,
            request: models.DescribeClbListenerRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeClbListenerRulesResponse:
        """
        查询腾讯云指定CLB实例对应的七层转发规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClbListenerRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClbListenerRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClbTargets(
            self,
            request: models.DescribeClbTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeClbTargetsResponse:
        """
        查询CLB后端服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClbTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClbTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudAssets(
            self,
            request: models.DescribeCloudAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudAssetsResponse:
        """
        全部资产
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudFunctionList(
            self,
            request: models.DescribeCloudFunctionListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudFunctionListResponse:
        """
        云函数列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudFunctionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudFunctionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAssetList(
            self,
            request: models.DescribeClusterAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAssetListResponse:
        """
        查询容器集群资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAssetSyncTaskStatus(
            self,
            request: models.DescribeClusterAssetSyncTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAssetSyncTaskStatusResponse:
        """
        查询集群资产同步任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAssetSyncTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAssetSyncTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAssets(
            self,
            request: models.DescribeClusterAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAssetsResponse:
        """
        集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerAppList(
            self,
            request: models.DescribeClusterContainerAppListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerAppListResponse:
        """
        查询容器关联应用列表。通过容器ID获取关联的应用服务信息，支持分页。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerComponentList(
            self,
            request: models.DescribeClusterContainerComponentListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerComponentListResponse:
        """
        查询容器关联组件列表。通过容器ID获取关联的组件信息，支持分页。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerComponentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerComponentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerDetail(
            self,
            request: models.DescribeClusterContainerDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerDetailResponse:
        """
        查询集群容器详情。通过容器ID获取容器基本信息、镜像信息、挂载信息、网络信息以及关联节点信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerList(
            self,
            request: models.DescribeClusterContainerListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerListResponse:
        """
        查询集群容器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerPortList(
            self,
            request: models.DescribeClusterContainerPortListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerPortListResponse:
        """
        查询容器关联端口列表。通过容器ID获取关联的端口信息，支持分页。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerPortList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerPortListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerProcessList(
            self,
            request: models.DescribeClusterContainerProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerProcessListResponse:
        """
        查询容器关联进程列表。通过容器ID获取关联的进程信息，支持按启动时间排序和分页。Filter.By支持StartTime；Filter.Order支持ASC/DESC。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerWebServiceList(
            self,
            request: models.DescribeClusterContainerWebServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerWebServiceListResponse:
        """
        查询容器关联Web服务列表。通过容器ID获取关联的Web服务信息，支持分页。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerWebServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerWebServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDetail(
            self,
            request: models.DescribeClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDetailResponse:
        """
        查询集群详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInstallCommand(
            self,
            request: models.DescribeClusterInstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInstallCommandResponse:
        """
        查询集群安装命令
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterListV2(
            self,
            request: models.DescribeClusterListV2Request,
            opts: Dict = None,
    ) -> models.DescribeClusterListV2Response:
        """
        查询集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterListV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterListV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNamespaceList(
            self,
            request: models.DescribeClusterNamespaceListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNamespaceListResponse:
        """
        查询集群命名空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNamespaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNamespaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNodeList(
            self,
            request: models.DescribeClusterNodeListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNodeListResponse:
        """
        查询集群节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNodeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterPodAssets(
            self,
            request: models.DescribeClusterPodAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterPodAssetsResponse:
        """
        集群pod列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterPodAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterPodAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterPodDetail(
            self,
            request: models.DescribeClusterPodDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterPodDetailResponse:
        """
        查询集群 Pod 详情。容器资产改版 A 类新接口，为 Pod 资产详情页主入口。入参仅 UniqueID；出参覆盖资产信息、所属集群、命名空间、节点、Workload、以及按四个风险等级分组的风险事件数和告警事件数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterPodDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterPodDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterPodList(
            self,
            request: models.DescribeClusterPodListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterPodListResponse:
        """
        查询集群pod列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterPodList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterPodListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterServiceList(
            self,
            request: models.DescribeClusterServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterServiceListResponse:
        """
        查询集群service列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterSummary(
            self,
            request: models.DescribeClusterSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterSummaryResponse:
        """
        查询集群概览数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterSuperNodeInfo(
            self,
            request: models.DescribeClusterSuperNodeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterSuperNodeInfoResponse:
        """
        查询集群超级节点详情，返回基本信息（所属地域/可用区/资产最后更新时间/节点来源/子网/核数）与所属集群信息（集群名称/集群ID/集群状态/Kubernetes版本/Kubelet版本）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterSuperNodeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterSuperNodeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceOverview(
            self,
            request: models.DescribeComplianceOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceOverviewResponse:
        """
        云资源配置检测合规概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceRiskList(
            self,
            request: models.DescribeComplianceRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceRiskListResponse:
        """
        合规标准聚合视角下云资源配置风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceStandardTermTree(
            self,
            request: models.DescribeComplianceStandardTermTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceStandardTermTreeResponse:
        """
        云资源配置检测标准章节条款树
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceStandardTermTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceStandardTermTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceStatistics(
            self,
            request: models.DescribeComplianceStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceStatisticsResponse:
        """
        云资源配置检测规范分类统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigCheckRules(
            self,
            request: models.DescribeConfigCheckRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigCheckRulesResponse:
        """
        云资源配置风险规则列表示例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigCheckRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigCheckRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAccessPermission(
            self,
            request: models.DescribeCosAccessPermissionRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAccessPermissionResponse:
        """
        查看cos桶访问权限信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAccessPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAccessPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAccessPermissions(
            self,
            request: models.DescribeCosAccessPermissionsRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAccessPermissionsResponse:
        """
        查看对象存储访问权限列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAccessPermissions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAccessPermissionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosActionList(
            self,
            request: models.DescribeCosActionListRequest,
            opts: Dict = None,
    ) -> models.DescribeCosActionListResponse:
        """
        查看COS接口列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosActionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosActionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAkAsset(
            self,
            request: models.DescribeCosAkAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAkAssetResponse:
        """
        查看ak资产列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAkAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAkAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAkInvokeIpList(
            self,
            request: models.DescribeCosAkInvokeIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAkInvokeIpListResponse:
        """
        查看存储桶调用源ip列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAkInvokeIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAkInvokeIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAlarmList(
            self,
            request: models.DescribeCosAlarmListRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAlarmListResponse:
        """
        查看告警列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAlarmList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAlarmListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAlarmTrendData(
            self,
            request: models.DescribeCosAlarmTrendDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAlarmTrendDataResponse:
        """
        每日告警新增数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAlarmTrendData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAlarmTrendDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAsset(
            self,
            request: models.DescribeCosAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAssetResponse:
        """
        查看cos资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAssetSyncTask(
            self,
            request: models.DescribeCosAssetSyncTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAssetSyncTaskResponse:
        """
        获取对应appid对应的当前正在扫描的taskid
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAssetSyncTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAssetSyncTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAuditAppIdList(
            self,
            request: models.DescribeCosAuditAppIdListRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAuditAppIdListResponse:
        """
        查看该appid下已购买的appid集合
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAuditAppIdList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAuditAppIdListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAuditDictionaryList(
            self,
            request: models.DescribeCosAuditDictionaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAuditDictionaryListResponse:
        """
        查询cos审计字典信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAuditDictionaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAuditDictionaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosAuditPayInfo(
            self,
            request: models.DescribeCosAuditPayInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCosAuditPayInfoResponse:
        """
        获取审计支付信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosAuditPayInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosAuditPayInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosBucketBillingInfo(
            self,
            request: models.DescribeCosBucketBillingInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCosBucketBillingInfoResponse:
        """
        获取存储桶计费信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosBucketBillingInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosBucketBillingInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosBucketList(
            self,
            request: models.DescribeCosBucketListRequest,
            opts: Dict = None,
    ) -> models.DescribeCosBucketListResponse:
        """
        获取存储桶信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosBucketList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosBucketListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosBucketRisk(
            self,
            request: models.DescribeCosBucketRiskRequest,
            opts: Dict = None,
    ) -> models.DescribeCosBucketRiskResponse:
        """
        查看风险资产视角
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosBucketRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosBucketRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosIdentifyFileList(
            self,
            request: models.DescribeCosIdentifyFileListRequest,
            opts: Dict = None,
    ) -> models.DescribeCosIdentifyFileListResponse:
        """
        查询cos文件数据识别结果列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosIdentifyFileList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosIdentifyFileListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosInvokeUa(
            self,
            request: models.DescribeCosInvokeUaRequest,
            opts: Dict = None,
    ) -> models.DescribeCosInvokeUaResponse:
        """
        查看调用记录关联的文件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosInvokeUa"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosInvokeUaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosIpInvokeLog(
            self,
            request: models.DescribeCosIpInvokeLogRequest,
            opts: Dict = None,
    ) -> models.DescribeCosIpInvokeLogResponse:
        """
        查看cos调用日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosIpInvokeLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosIpInvokeLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosIpInvokeRecordFile(
            self,
            request: models.DescribeCosIpInvokeRecordFileRequest,
            opts: Dict = None,
    ) -> models.DescribeCosIpInvokeRecordFileResponse:
        """
        查看调用记录关联的文件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosIpInvokeRecordFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosIpInvokeRecordFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosObjectScanTask(
            self,
            request: models.DescribeCosObjectScanTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeCosObjectScanTaskResponse:
        """
        查询cos风险文件扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosObjectScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosObjectScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosOverview(
            self,
            request: models.DescribeCosOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeCosOverviewResponse:
        """
        cos概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosPolicy(
            self,
            request: models.DescribeCosPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeCosPolicyResponse:
        """
        获取策略列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosRiskActionList(
            self,
            request: models.DescribeCosRiskActionListRequest,
            opts: Dict = None,
    ) -> models.DescribeCosRiskActionListResponse:
        """
        风险接口列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosRiskActionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosRiskActionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosRiskEvidence(
            self,
            request: models.DescribeCosRiskEvidenceRequest,
            opts: Dict = None,
    ) -> models.DescribeCosRiskEvidenceResponse:
        """
        查看风险证据以及描述
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosRiskEvidence"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosRiskEvidenceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosRiskScanTask(
            self,
            request: models.DescribeCosRiskScanTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeCosRiskScanTaskResponse:
        """
        查看存储桶扫描任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosRiskScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosRiskScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosRoleAccessPermission(
            self,
            request: models.DescribeCosRoleAccessPermissionRequest,
            opts: Dict = None,
    ) -> models.DescribeCosRoleAccessPermissionResponse:
        """
        查看cos桶访问权限信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosRoleAccessPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosRoleAccessPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosRoleAccessPermissions(
            self,
            request: models.DescribeCosRoleAccessPermissionsRequest,
            opts: Dict = None,
    ) -> models.DescribeCosRoleAccessPermissionsResponse:
        """
        获取存储桶角色权限列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosRoleAccessPermissions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosRoleAccessPermissionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosSourceIp(
            self,
            request: models.DescribeCosSourceIpRequest,
            opts: Dict = None,
    ) -> models.DescribeCosSourceIpResponse:
        """
        调用源ip列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosSourceIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosSourceIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCspmShardConfig(
            self,
            request: models.DescribeCspmShardConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeCspmShardConfigResponse:
        """
        获取CSPM自动配额共享配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCspmShardConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCspmShardConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomAssetTagCount(
            self,
            request: models.DescribeCustomAssetTagCountRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomAssetTagCountResponse:
        """
        用户自定义 标签数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomAssetTagCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomAssetTagCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomRiskRuleDetail(
            self,
            request: models.DescribeCustomRiskRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomRiskRuleDetailResponse:
        """
        自定义风险规则配置详情列表示例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomRiskRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomRiskRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomRiskRules(
            self,
            request: models.DescribeCustomRiskRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomRiskRulesResponse:
        """
        自定义风险规则配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomRiskRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomRiskRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDbAssetInfo(
            self,
            request: models.DescribeDbAssetInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDbAssetInfoResponse:
        """
        db资产详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDbAssetInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDbAssetInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDbAssets(
            self,
            request: models.DescribeDbAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDbAssetsResponse:
        """
        数据库资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDbAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDbAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainAssets(
            self,
            request: models.DescribeDomainAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainAssetsResponse:
        """
        域名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAccessRecord(
            self,
            request: models.DescribeDspmAccessRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAccessRecordResponse:
        """
        查询Dspm访问记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAccessRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAccessRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAccessTopologyAccounts(
            self,
            request: models.DescribeDspmAccessTopologyAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAccessTopologyAccountsResponse:
        """
        查询Dspm访问拓扑账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAccessTopologyAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAccessTopologyAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAccessTopologyAssets(
            self,
            request: models.DescribeDspmAccessTopologyAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAccessTopologyAssetsResponse:
        """
        查询Dspm访问拓扑资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAccessTopologyAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAccessTopologyAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAccessTopologyIps(
            self,
            request: models.DescribeDspmAccessTopologyIpsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAccessTopologyIpsResponse:
        """
        查询Dspm访问拓扑ip列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAccessTopologyIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAccessTopologyIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmApplyHistory(
            self,
            request: models.DescribeDspmApplyHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmApplyHistoryResponse:
        """
        查询Dspm申请历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmApplyHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmApplyHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmApplyOrderList(
            self,
            request: models.DescribeDspmApplyOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmApplyOrderListResponse:
        """
        查询Dspm申请单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmApplyOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmApplyOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmApproveHistory(
            self,
            request: models.DescribeDspmApproveHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmApproveHistoryResponse:
        """
        查询Dspm审批历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmApproveHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmApproveHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmApproveOrderList(
            self,
            request: models.DescribeDspmApproveOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmApproveOrderListResponse:
        """
        查询Dspm审批单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmApproveOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmApproveOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetAccessTopology(
            self,
            request: models.DescribeDspmAssetAccessTopologyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetAccessTopologyResponse:
        """
        查询Dspm资产访问拓扑
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetAccessTopology"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetAccessTopologyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetAccountIdentify(
            self,
            request: models.DescribeDspmAssetAccountIdentifyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetAccountIdentifyResponse:
        """
        查询Dspm资产账号身份信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetAccountIdentify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetAccountIdentifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetAccountPresetPrivileges(
            self,
            request: models.DescribeDspmAssetAccountPresetPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetAccountPresetPrivilegesResponse:
        """
        查询Dspm资产账号预设特权信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetAccountPresetPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetAccountPresetPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetAccountRecycledPrivileges(
            self,
            request: models.DescribeDspmAssetAccountRecycledPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetAccountRecycledPrivilegesResponse:
        """
        查询Dspm资产账号回收后特权信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetAccountRecycledPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetAccountRecycledPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetAccounts(
            self,
            request: models.DescribeDspmAssetAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetAccountsResponse:
        """
        查询Dspm资产账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetDatabaseList(
            self,
            request: models.DescribeDspmAssetDatabaseListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetDatabaseListResponse:
        """
        查询资产数据库信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetDatabaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetDatabaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetDatabases(
            self,
            request: models.DescribeDspmAssetDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetDatabasesResponse:
        """
        查询Dspm资产数据库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetFieldList(
            self,
            request: models.DescribeDspmAssetFieldListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetFieldListResponse:
        """
        查询dspm资产字段信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetFieldList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetFieldListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetFieldSamples(
            self,
            request: models.DescribeDspmAssetFieldSamplesRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetFieldSamplesResponse:
        """
        查询dspm资产字段样本值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetFieldSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetFieldSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetIdentifyInfoList(
            self,
            request: models.DescribeDspmAssetIdentifyInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetIdentifyInfoListResponse:
        """
        查询dspm资产数据识别信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetIdentifyInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetIdentifyInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetIds(
            self,
            request: models.DescribeDspmAssetIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetIdsResponse:
        """
        查询Dspm资产id列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetLoginCredential(
            self,
            request: models.DescribeDspmAssetLoginCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetLoginCredentialResponse:
        """
        查询Dspm资产登录凭据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetLoginCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetLoginCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetSecurityAnalyseStatus(
            self,
            request: models.DescribeDspmAssetSecurityAnalyseStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetSecurityAnalyseStatusResponse:
        """
        查询Dspm资产安全分析状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetSecurityAnalyseStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetSecurityAnalyseStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetSupportedPrivileges(
            self,
            request: models.DescribeDspmAssetSupportedPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetSupportedPrivilegesResponse:
        """
        查询Dspm资产支持的权限
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetSupportedPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetSupportedPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetTableList(
            self,
            request: models.DescribeDspmAssetTableListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetTableListResponse:
        """
        查询资产表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetTableList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetTableListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssets(
            self,
            request: models.DescribeDspmAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetsResponse:
        """
        查询Dspm资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmBackupLogList(
            self,
            request: models.DescribeDspmBackupLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmBackupLogListResponse:
        """
        查询备份日志列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmBackupLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmBackupLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmBackupSetting(
            self,
            request: models.DescribeDspmBackupSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmBackupSettingResponse:
        """
        查询日志备份配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmBackupSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmBackupSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmDictionaryList(
            self,
            request: models.DescribeDspmDictionaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmDictionaryListResponse:
        """
        查询dspm字典信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmDictionaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmDictionaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmExportTask(
            self,
            request: models.DescribeDspmExportTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmExportTaskResponse:
        """
        查询导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmExportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmExportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyCategoryList(
            self,
            request: models.DescribeDspmIdentifyCategoryListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyCategoryListResponse:
        """
        查询dspm数据识别分类列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyCategoryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyCategoryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyComplianceCategoryRuleList(
            self,
            request: models.DescribeDspmIdentifyComplianceCategoryRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyComplianceCategoryRuleListResponse:
        """
        查询dspm数据识别模板分类关联数据项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyComplianceCategoryRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyComplianceCategoryRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyComplianceGroupDetail(
            self,
            request: models.DescribeDspmIdentifyComplianceGroupDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyComplianceGroupDetailResponse:
        """
        查询dspm识别模板详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyComplianceGroupDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyComplianceGroupDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyComplianceGroupList(
            self,
            request: models.DescribeDspmIdentifyComplianceGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyComplianceGroupListResponse:
        """
        查询dspm数据识别模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyComplianceGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyComplianceGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyDistributionStatistics(
            self,
            request: models.DescribeDspmIdentifyDistributionStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyDistributionStatisticsResponse:
        """
        查询dspm数据识别分布统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyDistributionStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyDistributionStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyIdList(
            self,
            request: models.DescribeDspmIdentifyIdListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyIdListResponse:
        """
        查询Dspm身份id列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyIdList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyIdListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyInfo(
            self,
            request: models.DescribeDspmIdentifyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyInfoResponse:
        """
        查询Dspm身份信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyInfoList(
            self,
            request: models.DescribeDspmIdentifyInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyInfoListResponse:
        """
        查询Dspm身份信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyLevelGroupList(
            self,
            request: models.DescribeDspmIdentifyLevelGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyLevelGroupListResponse:
        """
        查询dspm数据识别分级组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyLevelGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyLevelGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyRuleDetail(
            self,
            request: models.DescribeDspmIdentifyRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyRuleDetailResponse:
        """
        查询dspm数据识别数据项详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyRuleList(
            self,
            request: models.DescribeDspmIdentifyRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyRuleListResponse:
        """
        查询dspm数据识别数据项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyRuleTestResult(
            self,
            request: models.DescribeDspmIdentifyRuleTestResultRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyRuleTestResultResponse:
        """
        查询dspm数据识别数据项验证结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyRuleTestResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyRuleTestResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmLogList(
            self,
            request: models.DescribeDspmLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmLogListResponse:
        """
        查询日志列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmPayInfo(
            self,
            request: models.DescribeDspmPayInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmPayInfoResponse:
        """
        获取已购Dspm订单信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmPayInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmPayInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmPersonApplyHistory(
            self,
            request: models.DescribeDspmPersonApplyHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmPersonApplyHistoryResponse:
        """
        查询Dspm访客申请记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmPersonApplyHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmPersonApplyHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmPersonalIdentifyList(
            self,
            request: models.DescribeDspmPersonalIdentifyListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmPersonalIdentifyListResponse:
        """
        查询Dspm个人身份信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmPersonalIdentifyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmPersonalIdentifyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmRisk(
            self,
            request: models.DescribeDspmRiskRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmRiskResponse:
        """
        查询Dspm风险记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmRiskDetail(
            self,
            request: models.DescribeDspmRiskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmRiskDetailResponse:
        """
        查询Dspm风险详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmRiskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmRiskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmRiskStrategy(
            self,
            request: models.DescribeDspmRiskStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmRiskStrategyResponse:
        """
        查询Dspm风险策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmRiskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmRiskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmRiskStrategyGroup(
            self,
            request: models.DescribeDspmRiskStrategyGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmRiskStrategyGroupResponse:
        """
        查询Dspm风险分组策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmRiskStrategyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmRiskStrategyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmRiskTendency(
            self,
            request: models.DescribeDspmRiskTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmRiskTendencyResponse:
        """
        查询Dspm风险趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmRiskTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmRiskTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmStatistics(
            self,
            request: models.DescribeDspmStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmStatisticsResponse:
        """
        查询Dspm统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmSupportedAssetType(
            self,
            request: models.DescribeDspmSupportedAssetTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmSupportedAssetTypeResponse:
        """
        查询Dspm支持的资产类型信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmSupportedAssetType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmSupportedAssetTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmSyncAssetsStatus(
            self,
            request: models.DescribeDspmSyncAssetsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmSyncAssetsStatusResponse:
        """
        查询Dspm同步资产状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmSyncAssetsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmSyncAssetsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmSyncUsersStatus(
            self,
            request: models.DescribeDspmSyncUsersStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmSyncUsersStatusResponse:
        """
        查询Dspm同步用户状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmSyncUsersStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmSyncUsersStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmWhitelistStrategy(
            self,
            request: models.DescribeDspmWhitelistStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmWhitelistStrategyResponse:
        """
        查询Dspm白名单策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmWhitelistStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmWhitelistStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDynamicAssets(
            self,
            request: models.DescribeDynamicAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDynamicAssetsResponse:
        """
        指定资产类型列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDynamicAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDynamicAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEDRRuleList(
            self,
            request: models.DescribeEDRRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeEDRRuleListResponse:
        """
        获取EDR策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEDRRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEDRRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEDRScanRecordList(
            self,
            request: models.DescribeEDRScanRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeEDRScanRecordListResponse:
        """
        查询扫描任务列表。Filter.Filters支持Name：Keyword(模糊OperatorType=9)、ScanType(MANUAL/CYCLE)、TaskType(HOST/CONTAINER)、Status(WAIT/SCANNING/FINISHED/FAILED/CANCELED)、AppId(账号)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEDRScanRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEDRScanRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEDRScanTaskDetail(
            self,
            request: models.DescribeEDRScanTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeEDRScanTaskDetailResponse:
        """
        查询扫描任务详情。Filter.Filters支持Name：Status（资产扫描状态，OperatorType=7 IN匹配，取值WAIT/SCANNING/FINISHED/FAILED）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEDRScanTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEDRScanTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertCountForAsset(
            self,
            request: models.DescribeEdrAlertCountForAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertCountForAssetResponse:
        """
        获取EDR告警数量统计，供资产模块调用。根据传入的MemberId和InstanceIDs，查询EDR告警表并返回告警记录条数信息。当InstanceIDs为空时返回汇总统计，非空时按InstanceIDs粒度分别返回统计。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertCountForAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertCountForAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertCountForContainer(
            self,
            request: models.DescribeEdrAlertCountForContainerRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertCountForContainerResponse:
        """
        容器场景告警数量统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertCountForContainer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertCountForContainerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertInfo(
            self,
            request: models.DescribeEdrAlertInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertInfoResponse:
        """
        获取EDR告警详情，包含告警内容JSON、资产富化、情报富化等完整信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertList(
            self,
            request: models.DescribeEdrAlertListRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertListResponse:
        """
        获取EDR告警列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertMultiAttackStages(
            self,
            request: models.DescribeEdrAlertMultiAttackStagesRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertMultiAttackStagesResponse:
        """
        EDR告警多攻击阶段查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertMultiAttackStages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertMultiAttackStagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertSummary(
            self,
            request: models.DescribeEdrAlertSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertSummaryResponse:
        """
        获取EDR告警统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertThreatTags(
            self,
            request: models.DescribeEdrAlertThreatTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertThreatTagsResponse:
        """
        EDR告警标签批量查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertThreatTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertThreatTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrExcludeNetworkSegments(
            self,
            request: models.DescribeEdrExcludeNetworkSegmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrExcludeNetworkSegmentsResponse:
        """
        查询EDR日志采集例外网段配置，添加至例外名单的网段，其TCP日志将不被采集。如果用户未配置过，则返回系统推荐的默认网段
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrExcludeNetworkSegments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrExcludeNetworkSegmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrExportJobDownloadURL(
            self,
            request: models.DescribeEdrExportJobDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrExportJobDownloadURLResponse:
        """
        获取EDR导出下载链接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrExportJobDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrExportJobDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrExportJobList(
            self,
            request: models.DescribeEdrExportJobListRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrExportJobListResponse:
        """
        导出EDR任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrExportJobList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrExportJobListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrLogCollectPaths(
            self,
            request: models.DescribeEdrLogCollectPathsRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrLogCollectPathsResponse:
        """
        查询采集路径配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrLogCollectPaths"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrLogCollectPathsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportJobDownloadURL(
            self,
            request: models.DescribeExportJobDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeExportJobDownloadURLResponse:
        """
        导出任务结果下载URL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportJobDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportJobDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportJobManageList(
            self,
            request: models.DescribeExportJobManageListRequest,
            opts: Dict = None,
    ) -> models.DescribeExportJobManageListResponse:
        """
        导出任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportJobManageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportJobManageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposeAssetCategory(
            self,
            request: models.DescribeExposeAssetCategoryRequest,
            opts: Dict = None,
    ) -> models.DescribeExposeAssetCategoryResponse:
        """
        云边界分析资产分类
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposeAssetCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposeAssetCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposePath(
            self,
            request: models.DescribeExposePathRequest,
            opts: Dict = None,
    ) -> models.DescribeExposePathResponse:
        """
        查询云边界分析路径节点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposePath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposePathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposeRiskStatistics(
            self,
            request: models.DescribeExposeRiskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeExposeRiskStatisticsResponse:
        """
        云边界风险待治理风险
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposeRiskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposeRiskStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposeRisks(
            self,
            request: models.DescribeExposeRisksRequest,
            opts: Dict = None,
    ) -> models.DescribeExposeRisksResponse:
        """
        云边界待处理风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposeRisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposeRisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposeRules(
            self,
            request: models.DescribeExposeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeExposeRulesResponse:
        """
        边界规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposureAutoTagAttribute(
            self,
            request: models.DescribeExposureAutoTagAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeExposureAutoTagAttributeResponse:
        """
        云边界自动打标-规则属性
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposureAutoTagAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposureAutoTagAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposureAutoTagRules(
            self,
            request: models.DescribeExposureAutoTagRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeExposureAutoTagRulesResponse:
        """
        云边界自动打标-规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposureAutoTagRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposureAutoTagRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposureTrend(
            self,
            request: models.DescribeExposureTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeExposureTrendResponse:
        """
        查询互联网暴露周期数量趋势统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposureTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposureTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposures(
            self,
            request: models.DescribeExposuresRequest,
            opts: Dict = None,
    ) -> models.DescribeExposuresResponse:
        """
        云边界分析资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposures"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposuresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayAssets(
            self,
            request: models.DescribeGatewayAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayAssetsResponse:
        """
        获取网关列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHighBaseLineRiskList(
            self,
            request: models.DescribeHighBaseLineRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeHighBaseLineRiskListResponse:
        """
        查询云边界分析-暴露路径下主机节点的高危基线风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHighBaseLineRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHighBaseLineRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostKBRiskList(
            self,
            request: models.DescribeHostKBRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostKBRiskListResponse:
        """
        获取主机kb风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostKBRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostKBRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostVulItemVPRInfo(
            self,
            request: models.DescribeHostVulItemVPRInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeHostVulItemVPRInfoResponse:
        """
        获取主机漏洞VPR信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostVulItemVPRInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostVulItemVPRInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostVulOverview(
            self,
            request: models.DescribeHostVulOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeHostVulOverviewResponse:
        """
        获取主机漏洞概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostVulOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostVulOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostVulRiskList(
            self,
            request: models.DescribeHostVulRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostVulRiskListResponse:
        """
        获取主机漏洞风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostVulRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostVulRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIaCFileList(
            self,
            request: models.DescribeIaCFileListRequest,
            opts: Dict = None,
    ) -> models.DescribeIaCFileListResponse:
        """
        获取IaC检测文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIaCFileList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIaCFileListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIaCFileOverview(
            self,
            request: models.DescribeIaCFileOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeIaCFileOverviewResponse:
        """
        获取IaC检测文件概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIaCFileOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIaCFileOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIaCFileReport(
            self,
            request: models.DescribeIaCFileReportRequest,
            opts: Dict = None,
    ) -> models.DescribeIaCFileReportResponse:
        """
        获取IaC检测文件报告
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIaCFileReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIaCFileReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIaCTokenList(
            self,
            request: models.DescribeIaCTokenListRequest,
            opts: Dict = None,
    ) -> models.DescribeIaCTokenListResponse:
        """
        获取IaC检测接入Token列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIaCTokenList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIaCTokenListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpInvokeRecord(
            self,
            request: models.DescribeIpInvokeRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeIpInvokeRecordResponse:
        """
        对象存储异常检测调用记录信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpInvokeRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpInvokeRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpInvokeRecordDetail(
            self,
            request: models.DescribeIpInvokeRecordDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeIpInvokeRecordDetailResponse:
        """
        ip访问列表详情信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpInvokeRecordDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpInvokeRecordDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKBDetail(
            self,
            request: models.DescribeKBDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeKBDetailResponse:
        """
        根据用户输入的 KB 内部 ID 查询单个 Windows KB 补丁的详情信息，返回 KB 基本信息、发布时间、是否需要重启，以及该 KB 关联的漏洞列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKBDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKBDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKBUpdatableMachineList(
            self,
            request: models.DescribeKBUpdatableMachineListRequest,
            opts: Dict = None,
    ) -> models.DescribeKBUpdatableMachineListResponse:
        """
        查询指定KB补丁可以更新的主机列表。用于Windows系统补丁修复场景，在用户提交KB补丁更新任务前，查询哪些主机缺少该补丁且支持自动更新。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKBUpdatableMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKBUpdatableMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKeySandboxCredential(
            self,
            request: models.DescribeKeySandboxCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeKeySandboxCredentialResponse:
        """
        查询凭证详情，返回凭证元数据和打码后的凭据数据。access类型返回Access数组（Key原文、Value打码），sts类型返回STS对象（System原文、SecretID和SecretKey打码）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKeySandboxCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeySandboxCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKeySandboxCredentialList(
            self,
            request: models.DescribeKeySandboxCredentialListRequest,
            opts: Dict = None,
    ) -> models.DescribeKeySandboxCredentialListResponse:
        """
        查询凭证列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKeySandboxCredentialList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeySandboxCredentialListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLastScanTaskInfo(
            self,
            request: models.DescribeLastScanTaskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLastScanTaskInfoResponse:
        """
        获取最近一次立即检测任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLastScanTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLastScanTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLighthouseFirewallRules(
            self,
            request: models.DescribeLighthouseFirewallRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLighthouseFirewallRulesResponse:
        """
        查询轻量应用服务器防火墙规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLighthouseFirewallRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLighthouseFirewallRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerList(
            self,
            request: models.DescribeListenerListRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerListResponse:
        """
        查询clb监听器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginTypeGlobalConf(
            self,
            request: models.DescribeLoginTypeGlobalConfRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginTypeGlobalConfResponse:
        """
        获取防卸载全局配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginTypeGlobalConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginTypeGlobalConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginTypeHost(
            self,
            request: models.DescribeLoginTypeHostRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginTypeHostResponse:
        """
        获取扫码登录主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginTypeHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginTypeHostResponse
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
        
    async def DescribeMachineLoginType(
            self,
            request: models.DescribeMachineLoginTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineLoginTypeResponse:
        """
        获取主机登录方式
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineLoginType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineLoginTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareTimingScanSetting(
            self,
            request: models.DescribeMalwareTimingScanSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareTimingScanSettingResponse:
        """
        查询文件查杀定时扫描配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareTimingScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareTimingScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMandatoryVulSet(
            self,
            request: models.DescribeMandatoryVulSetRequest,
            opts: Dict = None,
    ) -> models.DescribeMandatoryVulSetResponse:
        """
        展示企业必修漏洞情报
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMandatoryVulSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMandatoryVulSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModifyMachinesLoginTypeTasks(
            self,
            request: models.DescribeModifyMachinesLoginTypeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeModifyMachinesLoginTypeTasksResponse:
        """
        获取批量修改主机登录方式任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModifyMachinesLoginTypeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModifyMachinesLoginTypeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNFSScanConf(
            self,
            request: models.DescribeNFSScanConfRequest,
            opts: Dict = None,
    ) -> models.DescribeNFSScanConfResponse:
        """
        获取NFS扫描全局配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNFSScanConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNFSScanConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNFSScanHost(
            self,
            request: models.DescribeNFSScanHostRequest,
            opts: Dict = None,
    ) -> models.DescribeNFSScanHostResponse:
        """
        获取扫码登录主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNFSScanHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNFSScanHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNICAssets(
            self,
            request: models.DescribeNICAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeNICAssetsResponse:
        """
        获取网卡列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNICAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNICAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatRules(
            self,
            request: models.DescribeNatRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeNatRulesResponse:
        """
        查询腾讯云nat网关实例对应的NAT策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetAttackSetting(
            self,
            request: models.DescribeNetAttackSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeNetAttackSettingResponse:
        """
        查询网络攻击检测开关及资产范围配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetAttackSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetAttackSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotifyAssetConfig(
            self,
            request: models.DescribeNotifyAssetConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeNotifyAssetConfigResponse:
        """
        获取通知资产范围配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotifyAssetConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotifyAssetConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotifySetting(
            self,
            request: models.DescribeNotifySettingRequest,
            opts: Dict = None,
    ) -> models.DescribeNotifySettingResponse:
        """
        获取通知设置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotifySetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotifySettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotifySettingAlert(
            self,
            request: models.DescribeNotifySettingAlertRequest,
            opts: Dict = None,
    ) -> models.DescribeNotifySettingAlertResponse:
        """
        获取告警中心通知高级配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotifySettingAlert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotifySettingAlertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationInfo(
            self,
            request: models.DescribeOrganizationInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationInfoResponse:
        """
        查询集团账号详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationUserInfo(
            self,
            request: models.DescribeOrganizationUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationUserInfoResponse:
        """
        查询集团账号用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOtherCloudAssets(
            self,
            request: models.DescribeOtherCloudAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeOtherCloudAssetsResponse:
        """
        资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOtherCloudAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOtherCloudAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePodContainerList(
            self,
            request: models.DescribePodContainerListRequest,
            opts: Dict = None,
    ) -> models.DescribePodContainerListResponse:
        """
        查询 Pod 关联容器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePodContainerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePodContainerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyHitData(
            self,
            request: models.DescribePolicyHitDataRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyHitDataResponse:
        """
        按日期查看策略命中详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyHitData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyHitDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePortDetectList(
            self,
            request: models.DescribePortDetectListRequest,
            opts: Dict = None,
    ) -> models.DescribePortDetectListResponse:
        """
        端口探测列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePortDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePortDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePortScanTaskCount(
            self,
            request: models.DescribePortScanTaskCountRequest,
            opts: Dict = None,
    ) -> models.DescribePortScanTaskCountResponse:
        """
        查询当前账号下端口扫描任务次数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePortScanTaskCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePortScanTaskCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePreventUninstallGlobalConf(
            self,
            request: models.DescribePreventUninstallGlobalConfRequest,
            opts: Dict = None,
    ) -> models.DescribePreventUninstallGlobalConfResponse:
        """
        获取防卸载全局配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePreventUninstallGlobalConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePreventUninstallGlobalConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePreventUninstallHost(
            self,
            request: models.DescribePreventUninstallHostRequest,
            opts: Dict = None,
    ) -> models.DescribePreventUninstallHostResponse:
        """
        获取防卸载主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePreventUninstallHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePreventUninstallHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessDaemonGlobalConf(
            self,
            request: models.DescribeProcessDaemonGlobalConfRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessDaemonGlobalConfResponse:
        """
        获取进程防护全局配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessDaemonGlobalConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessDaemonGlobalConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessDaemonHost(
            self,
            request: models.DescribeProcessDaemonHostRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessDaemonHostResponse:
        """
        获取进程守护主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessDaemonHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessDaemonHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicIpAssets(
            self,
            request: models.DescribePublicIpAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribePublicIpAssetsResponse:
        """
        ip公网列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicIpAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicIpAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRaspLicenseList(
            self,
            request: models.DescribeRaspLicenseListRequest,
            opts: Dict = None,
    ) -> models.DescribeRaspLicenseListResponse:
        """
        查询应用防护授权列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRaspLicenseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRaspLicenseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRepositoryImageAssets(
            self,
            request: models.DescribeRepositoryImageAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeRepositoryImageAssetsResponse:
        """
        仓库镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRepositoryImageAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRepositoryImageAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellSystemPolicyConfig(
            self,
            request: models.DescribeReverseShellSystemPolicyConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellSystemPolicyConfigResponse:
        """
        查询反弹Shell内网告警与资产范围配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellSystemPolicyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellSystemPolicyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskBucketList(
            self,
            request: models.DescribeRiskBucketListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskBucketListResponse:
        """
        查看风险关联的存储桶信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskBucketList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskBucketListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCallRecord(
            self,
            request: models.DescribeRiskCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCallRecordResponse:
        """
        获取风险调用记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCallRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCallRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterAssetViewCFGRiskList(
            self,
            request: models.DescribeRiskCenterAssetViewCFGRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterAssetViewCFGRiskListResponse:
        """
        获取资产视角的配置风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterAssetViewCFGRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterAssetViewCFGRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterAssetViewPortRiskList(
            self,
            request: models.DescribeRiskCenterAssetViewPortRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterAssetViewPortRiskListResponse:
        """
        获取资产视角的端口风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterAssetViewPortRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterAssetViewPortRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterAssetViewVULRiskList(
            self,
            request: models.DescribeRiskCenterAssetViewVULRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterAssetViewVULRiskListResponse:
        """
        获取资产视角的漏洞风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterAssetViewVULRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterAssetViewVULRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterAssetViewWeakPasswordRiskList(
            self,
            request: models.DescribeRiskCenterAssetViewWeakPasswordRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterAssetViewWeakPasswordRiskListResponse:
        """
        获取资产视角的弱口令风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterAssetViewWeakPasswordRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterAssetViewWeakPasswordRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterCFGViewCFGRiskList(
            self,
            request: models.DescribeRiskCenterCFGViewCFGRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterCFGViewCFGRiskListResponse:
        """
        获取配置视角的配置风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterCFGViewCFGRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterCFGViewCFGRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterPortViewPortRiskList(
            self,
            request: models.DescribeRiskCenterPortViewPortRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterPortViewPortRiskListResponse:
        """
        获取端口视角的端口风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterPortViewPortRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterPortViewPortRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterRiskTrendAnalysis(
            self,
            request: models.DescribeRiskCenterRiskTrendAnalysisRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterRiskTrendAnalysisResponse:
        """
        获取风险趋势分析示例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterRiskTrendAnalysis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterRiskTrendAnalysisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterServerRiskList(
            self,
            request: models.DescribeRiskCenterServerRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterServerRiskListResponse:
        """
        获取风险服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterServerRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterServerRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterVULViewVULRiskList(
            self,
            request: models.DescribeRiskCenterVULViewVULRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterVULViewVULRiskListResponse:
        """
        获取漏洞视角的漏洞风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterVULViewVULRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterVULViewVULRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterWebsiteRiskList(
            self,
            request: models.DescribeRiskCenterWebsiteRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterWebsiteRiskListResponse:
        """
        获取内容风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterWebsiteRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterWebsiteRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDetailList(
            self,
            request: models.DescribeRiskDetailListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDetailListResponse:
        """
        风险详情列表示例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDetailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDetailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskItemList(
            self,
            request: models.DescribeRiskItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskItemListResponse:
        """
        获取风险项视角列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskRuleDetail(
            self,
            request: models.DescribeRiskRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskRuleDetailResponse:
        """
        查询风险规则详情示例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskRules(
            self,
            request: models.DescribeRiskRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskRulesResponse:
        """
        高级配置风险规则列表示例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskScanCronConfig(
            self,
            request: models.DescribeRiskScanCronConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskScanCronConfigResponse:
        """
        获取风险扫描周期计划
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskScanCronConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskScanCronConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskTrendData(
            self,
            request: models.DescribeRiskTrendDataRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskTrendDataResponse:
        """
        查看风险趋势图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskTrendData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskTrendDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanReportList(
            self,
            request: models.DescribeScanReportListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanReportListResponse:
        """
        获取扫描报告列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanReportList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanReportListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanStatistic(
            self,
            request: models.DescribeScanStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeScanStatisticResponse:
        """
        查询云边界分析扫描结果统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskList(
            self,
            request: models.DescribeScanTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskListResponse:
        """
        获取扫描任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskRecordList(
            self,
            request: models.DescribeScanTaskRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskRecordListResponse:
        """
        查询扫描任务记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScfCustomDomainEndpoints(
            self,
            request: models.DescribeScfCustomDomainEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeScfCustomDomainEndpointsResponse:
        """
        查询腾讯云SCF自定义域名端点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScfCustomDomainEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScfCustomDomainEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchBugInfo(
            self,
            request: models.DescribeSearchBugInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchBugInfoResponse:
        """
        立体防护中心查询漏洞信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchBugInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchBugInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupPolicy(
            self,
            request: models.DescribeSecurityGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupPolicyResponse:
        """
        查询指定安全组ID对应安全组规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillScanPayInfo(
            self,
            request: models.DescribeSkillScanPayInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillScanPayInfoResponse:
        """
        查询 Skill 安全检测计费信息，包括订单状态、总配额、已消耗配额、到期时间、支付模式等。无订单时返回零值（仅含 TimeNow 和 BetaEndTime）。试用订单通过 ModifyTrialStatus(Module=9) 领取，正式订单通过计费系统创建。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillScanPayInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillScanPayInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillScanResult(
            self,
            request: models.DescribeSkillScanResultRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillScanResultResponse:
        """
        查询 Skill 安全检测结果。调用 CreateSkillScan 成功后使用返回的 ContentHash + EngineVersion 轮询本接口获取结果。上传成功后建议5分钟后首次轮询，如未检测完成之后每隔1分钟轮询一次。响应通过 Status 字段区分四种状态：检测完成（SUCCESS）、检测中（SCANNING）、无记录（NOT_FOUND）、检测失败（FAILED）。注意：检测结果保留90天，超期后将返回 NOT_FOUND。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillScanResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillScanResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSourceIPAsset(
            self,
            request: models.DescribeSourceIPAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeSourceIPAssetResponse:
        """
        获取用户访问密钥资产列表（源IP视角）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSourceIPAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSourceIPAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubUserInfo(
            self,
            request: models.DescribeSubUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSubUserInfoResponse:
        """
        查询集团的子账号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnetAssets(
            self,
            request: models.DescribeSubnetAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetAssetsResponse:
        """
        获取子网列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnetAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagRuleAssets(
            self,
            request: models.DescribeTagRuleAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagRuleAssetsResponse:
        """
        打标策略生效资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagRuleAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagRuleAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLogList(
            self,
            request: models.DescribeTaskLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLogListResponse:
        """
        获取任务扫描报告列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLogURL(
            self,
            request: models.DescribeTaskLogURLRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLogURLResponse:
        """
        获取报告下载的临时链接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLogURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLogURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskPredictCostQuota(
            self,
            request: models.DescribeTaskPredictCostQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskPredictCostQuotaResponse:
        """
        获取扫描预消耗配额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskPredictCostQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskPredictCostQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopAttackInfo(
            self,
            request: models.DescribeTopAttackInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTopAttackInfoResponse:
        """
        查询TOP攻击信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopAttackInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopAttackInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUebaBehaviorSummary(
            self,
            request: models.DescribeUebaBehaviorSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeUebaBehaviorSummaryResponse:
        """
        查询用户行为分析的行为概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUebaBehaviorSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUebaBehaviorSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUebaRule(
            self,
            request: models.DescribeUebaRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeUebaRuleResponse:
        """
        查询用户行为分析策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUebaRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUebaRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUebaUserSummary(
            self,
            request: models.DescribeUebaUserSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeUebaUserSummaryResponse:
        """
        获取用户行为分析模块的用户概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUebaUserSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUebaUserSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCSPMInfoList(
            self,
            request: models.DescribeUserCSPMInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserCSPMInfoListResponse:
        """
        获取账号CSPM信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCSPMInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserCSPMInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCallRecord(
            self,
            request: models.DescribeUserCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeUserCallRecordResponse:
        """
        获取账号调用记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCallRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserCallRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDspmInfoList(
            self,
            request: models.DescribeUserDspmInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDspmInfoListResponse:
        """
        获取账号dspm信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDspmInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDspmInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserInfo(
            self,
            request: models.DescribeUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserInfoResponse:
        """
        用户CSPM配额信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVULList(
            self,
            request: models.DescribeVULListRequest,
            opts: Dict = None,
    ) -> models.DescribeVULListResponse:
        """
        新安全中心风险中心-漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVULList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVULListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVULRiskAdvanceCFGList(
            self,
            request: models.DescribeVULRiskAdvanceCFGListRequest,
            opts: Dict = None,
    ) -> models.DescribeVULRiskAdvanceCFGListResponse:
        """
        查询漏洞风险高级配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVULRiskAdvanceCFGList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVULRiskAdvanceCFGListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVULRiskDetail(
            self,
            request: models.DescribeVULRiskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVULRiskDetailResponse:
        """
        获取漏洞展开详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVULRiskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVULRiskDetailResponse
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
        
    async def DescribeVpcAssets(
            self,
            request: models.DescribeVpcAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcAssetsResponse:
        """
        获取vpc列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulComponentRelateHost(
            self,
            request: models.DescribeVulComponentRelateHostRequest,
            opts: Dict = None,
    ) -> models.DescribeVulComponentRelateHostResponse:
        """
        获取漏洞组件关联主机
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulComponentRelateHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulComponentRelateHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixTaskDetail(
            self,
            request: models.DescribeVulFixTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixTaskDetailResponse:
        """
        查询指定漏洞修复任务的详情信息，包含每台主机的修复状态、快照状态等明细数据，支持分页和筛选。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixTaskList(
            self,
            request: models.DescribeVulFixTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixTaskListResponse:
        """
        分页查询漏洞修复任务记录列表，支持按修复状态、时间范围等条件筛选，展示每个修复任务的概要信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixableMachineList(
            self,
            request: models.DescribeVulFixableMachineListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixableMachineListResponse:
        """
        查询指定漏洞可以被修复的主机列表。在用户提交修复任务前，需要先查询哪些主机支持自动修复，为用户选择修复目标提供数据支持。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixableMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixableMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixedHostDetail(
            self,
            request: models.DescribeVulFixedHostDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixedHostDetailResponse:
        """
        查询某个已修复漏洞在指定主机上的修复详情，包含漏洞基本信息、修复主机信息以及关联组件&路径的详细列表（组件名称、命中版本、关联路径、修复命令）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixedHostDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixedHostDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixedList(
            self,
            request: models.DescribeVulFixedListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixedListResponse:
        """
        查询已被修复的漏洞列表，展示修复成功的漏洞信息及修复情况统计，帮助用户了解修复成效。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixedList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixedListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulHostRelateComponent(
            self,
            request: models.DescribeVulHostRelateComponentRequest,
            opts: Dict = None,
    ) -> models.DescribeVulHostRelateComponentResponse:
        """
        获取漏洞主机关联组件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulHostRelateComponent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulHostRelateComponentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulIgnoreRuleList(
            self,
            request: models.DescribeVulIgnoreRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulIgnoreRuleListResponse:
        """
        获取漏洞忽略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulIgnoreRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulIgnoreRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulItemList(
            self,
            request: models.DescribeVulItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulItemListResponse:
        """
        获取漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulLabelList(
            self,
            request: models.DescribeVulLabelListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulLabelListResponse:
        """
        获取漏洞标签列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulLabelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulLabelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulRiskList(
            self,
            request: models.DescribeVulRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulRiskListResponse:
        """
        查询云边界分析-暴露路径下主机节点的漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulRiskRelateComponent(
            self,
            request: models.DescribeVulRiskRelateComponentRequest,
            opts: Dict = None,
    ) -> models.DescribeVulRiskRelateComponentResponse:
        """
        获取漏洞关联组件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulRiskRelateComponent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulRiskRelateComponentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulRiskRelateHost(
            self,
            request: models.DescribeVulRiskRelateHostRequest,
            opts: Dict = None,
    ) -> models.DescribeVulRiskRelateHostResponse:
        """
        获取漏洞或KB关联的主机
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulRiskRelateHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulRiskRelateHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanPeriodic(
            self,
            request: models.DescribeVulScanPeriodicRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanPeriodicResponse:
        """
        获取漏洞扫描（周期扫描）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanPeriodic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanPeriodicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanTaskDetail(
            self,
            request: models.DescribeVulScanTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanTaskDetailResponse:
        """
        获取扫描漏洞任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanTaskList(
            self,
            request: models.DescribeVulScanTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanTaskListResponse:
        """
        获取漏洞扫描任务记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulViewVulRiskList(
            self,
            request: models.DescribeVulViewVulRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulViewVulRiskListResponse:
        """
        获取漏洞视角的漏洞风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulViewVulRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulViewVulRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableAISchedule(
            self,
            request: models.DisableAIScheduleRequest,
            opts: Dict = None,
    ) -> models.DisableAIScheduleResponse:
        """
        停用AI 定时任务。

        将指定的AI 定时任务状态设置为已停用，停用后任务将暂停自动执行。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableAISchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableAIScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadDspmExportLog(
            self,
            request: models.DownloadDspmExportLogRequest,
            opts: Dict = None,
    ) -> models.DownloadDspmExportLogResponse:
        """
        下载导出日志
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadDspmExportLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadDspmExportLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableAISchedule(
            self,
            request: models.EnableAIScheduleRequest,
            opts: Dict = None,
    ) -> models.EnableAIScheduleResponse:
        """
        启用AI 定时任务。

        将指定的AI 定时任务状态设置为已启用，启用后任务将按触发器配置自动执行。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableAISchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableAIScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportCSIPMalwareScanTaskDetail(
            self,
            request: models.ExportCSIPMalwareScanTaskDetailRequest,
            opts: Dict = None,
    ) -> models.ExportCSIPMalwareScanTaskDetailResponse:
        """
        导出CSIP扫描任务主机详情为Excel文件，异步生成后通过DescribeExportMachines查询下载地址
        """
        
        kwargs = {}
        kwargs["action"] = "ExportCSIPMalwareScanTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportCSIPMalwareScanTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportClientSettingHostList(
            self,
            request: models.ExportClientSettingHostListRequest,
            opts: Dict = None,
    ) -> models.ExportClientSettingHostListResponse:
        """
        客户端设置主机列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "ExportClientSettingHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportClientSettingHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportEDRRules(
            self,
            request: models.ExportEDRRulesRequest,
            opts: Dict = None,
    ) -> models.ExportEDRRulesResponse:
        """
        导出EDR策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportEDRRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportEDRRulesResponse
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
        
    async def InstallClusterAgent(
            self,
            request: models.InstallClusterAgentRequest,
            opts: Dict = None,
    ) -> models.InstallClusterAgentResponse:
        """
        安装集群容器安全Agent（平行容器方式安装 Agent）。

        capi 层处理流程：
        1. 按 ClusterCaMD5List 查询 DB 集群列表（仅用于解析每个集群归属的 appid，不做存在性/类型校验）
        2. 按 appid 分组透传到接入侧 ClusterInstall RPC

        说明（容器资产改版 2026 H1）：本接口为透传接口，capi 层不对 ClusterCaMD5 做存在性/类型/格式校验；DB 中未命中的 ClusterCaMD5 静默跳过、不报错。
        """
        
        kwargs = {}
        kwargs["action"] = "InstallClusterAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallClusterAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAILinkSetting(
            self,
            request: models.ModifyAILinkSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyAILinkSettingResponse:
        """
        修改AI-Link智链引擎配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAILinkSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAILinkSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAISchedule(
            self,
            request: models.ModifyAIScheduleRequest,
            opts: Dict = None,
    ) -> models.ModifyAIScheduleResponse:
        """
        修改AI 定时任务。

        支持部分更新，仅更新传入的可选字段。触发器列表通过 UpdateTriggers 标志控制是否全量替换。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAISchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAIScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentConfigSetting(
            self,
            request: models.ModifyAgentConfigSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentConfigSettingResponse:
        """
        修改客户端日志采集配置（CSIP专属），支持设置日志采集类型和生效资产范围
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentConfigSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentConfigSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentRunMode(
            self,
            request: models.ModifyAgentRunModeRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentRunModeResponse:
        """
        设置客户端运行模式以及配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentRunMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentRunModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentRunPolicy(
            self,
            request: models.ModifyAgentRunPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentRunPolicyResponse:
        """
        修改客户端运行策略（策略组），支持设置自定义策略及关联机器列表
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentRunPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentRunPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmRiskStatus(
            self,
            request: models.ModifyAlarmRiskStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmRiskStatusResponse:
        """
        修改或者更改处置状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmRiskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmRiskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetCoreAttribute(
            self,
            request: models.ModifyAssetCoreAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetCoreAttributeResponse:
        """
        标记资产是否核心
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetCoreAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetCoreAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetFilterView(
            self,
            request: models.ModifyAssetFilterViewRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetFilterViewResponse:
        """
        更新资产搜索视图
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetFilterView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetFilterViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetTag(
            self,
            request: models.ModifyAssetTagRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetTagResponse:
        """
        编辑资产标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetTags(
            self,
            request: models.ModifyAssetTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetTagsResponse:
        """
        操作资产编辑标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetTagsByAssetInfo(
            self,
            request: models.ModifyAssetTagsByAssetInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetTagsByAssetInfoResponse:
        """
        操作资产编辑标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetTagsByAssetInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetTagsByAssetInfoResponse
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
        
    async def ModifyBaselinePolicy(
            self,
            request: models.ModifyBaselinePolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselinePolicyResponse:
        """
        新建或编辑一条基线策略。Policy.ID 为 0 视为新建，非 0 视为编辑；新建/编辑时 Name 必填，CheckAssetType 与 Type 需符合 CheckAssetType / PolicyType 枚举。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBruteAttackBanStatus(
            self,
            request: models.ModifyBruteAttackBanStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBruteAttackBanStatusResponse:
        """
        设置暴力破解阻断开关状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBruteAttackBanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBruteAttackBanStatusResponse
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
        
    async def ModifyCosAuditBucketMonitorStatus(
            self,
            request: models.ModifyCosAuditBucketMonitorStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCosAuditBucketMonitorStatusResponse:
        """
        修改存储桶监测状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCosAuditBucketMonitorStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCosAuditBucketMonitorStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCosAuditMonitorAccount(
            self,
            request: models.ModifyCosAuditMonitorAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyCosAuditMonitorAccountResponse:
        """
        修改cos审计监测账号
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCosAuditMonitorAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCosAuditMonitorAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCosAuditObjectIdentifyStatus(
            self,
            request: models.ModifyCosAuditObjectIdentifyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCosAuditObjectIdentifyStatusResponse:
        """
        修改对象存储识别开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCosAuditObjectIdentifyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCosAuditObjectIdentifyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCosAuditObjectSampleRate(
            self,
            request: models.ModifyCosAuditObjectSampleRateRequest,
            opts: Dict = None,
    ) -> models.ModifyCosAuditObjectSampleRateResponse:
        """
        设置对象存储扫描采样率
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCosAuditObjectSampleRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCosAuditObjectSampleRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCosMarkInfo(
            self,
            request: models.ModifyCosMarkInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyCosMarkInfoResponse:
        """
        修改对象存储备注
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCosMarkInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCosMarkInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCspmShardConfig(
            self,
            request: models.ModifyCspmShardConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyCspmShardConfigResponse:
        """
        更新CSPM自动配额管理者共享开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCspmShardConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCspmShardConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAccessRecord(
            self,
            request: models.ModifyDspmAccessRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAccessRecordResponse:
        """
        修改Dspm访问管理信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAccessRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAccessRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmApplyingIdentifyComplianceGroup(
            self,
            request: models.ModifyDspmApplyingIdentifyComplianceGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmApplyingIdentifyComplianceGroupResponse:
        """
        修改dspm当前应用的数据识别模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmApplyingIdentifyComplianceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmApplyingIdentifyComplianceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmApproveStatus(
            self,
            request: models.ModifyDspmApproveStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmApproveStatusResponse:
        """
        修改Dspm审批单状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmApproveStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmApproveStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetAccount(
            self,
            request: models.ModifyDspmAssetAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetAccountResponse:
        """
        修改Dspm资产账号信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetAccountPrivileges(
            self,
            request: models.ModifyDspmAssetAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetAccountPrivilegesResponse:
        """
        修改Dspm资产账号权限
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetDataScanTask(
            self,
            request: models.ModifyDspmAssetDataScanTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetDataScanTaskResponse:
        """
        修改Dspm资产数据扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetDataScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetDataScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetDataScanTaskStatus(
            self,
            request: models.ModifyDspmAssetDataScanTaskStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetDataScanTaskStatusResponse:
        """
        修改Dspm资产数据扫描任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetDataScanTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetDataScanTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetLogDeliverySwitch(
            self,
            request: models.ModifyDspmAssetLogDeliverySwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetLogDeliverySwitchResponse:
        """
        修改Dspm资产日志投递开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetLogDeliverySwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetLogDeliverySwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetSecurityAnalysisSwitch(
            self,
            request: models.ModifyDspmAssetSecurityAnalysisSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetSecurityAnalysisSwitchResponse:
        """
        修改Dspm资产日志投递开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetSecurityAnalysisSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetSecurityAnalysisSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmBackupSetting(
            self,
            request: models.ModifyDspmBackupSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmBackupSettingResponse:
        """
        修改日志备份设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmBackupSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmBackupSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyCategory(
            self,
            request: models.ModifyDspmIdentifyCategoryRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyCategoryResponse:
        """
        修改dspm数据识别分类
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyComplianceGroup(
            self,
            request: models.ModifyDspmIdentifyComplianceGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyComplianceGroupResponse:
        """
        修改dspm数据识别模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyComplianceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyComplianceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyComplianceGroupStatus(
            self,
            request: models.ModifyDspmIdentifyComplianceGroupStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyComplianceGroupStatusResponse:
        """
        修改dspm数据识别模板状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyComplianceGroupStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyComplianceGroupStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyComplianceRuleLevelInfo(
            self,
            request: models.ModifyDspmIdentifyComplianceRuleLevelInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyComplianceRuleLevelInfoResponse:
        """
        修改dspm数据识别模板数据项关联级别信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyComplianceRuleLevelInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyComplianceRuleLevelInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyInfo(
            self,
            request: models.ModifyDspmIdentifyInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyInfoResponse:
        """
        修改Dspm身份信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyLevelGroup(
            self,
            request: models.ModifyDspmIdentifyLevelGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyLevelGroupResponse:
        """
        修改dspm数据识别分级组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyLevelGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyLevelGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyLevelItem(
            self,
            request: models.ModifyDspmIdentifyLevelItemRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyLevelItemResponse:
        """
        修改dspm数据识别分级信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyLevelItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyLevelItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyRule(
            self,
            request: models.ModifyDspmIdentifyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyRuleResponse:
        """
        修改dspm数据识别数据项
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyRuleStatus(
            self,
            request: models.ModifyDspmIdentifyRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyRuleStatusResponse:
        """
        修改dspm数据识别数据项状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIpInfo(
            self,
            request: models.ModifyDspmIpInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIpInfoResponse:
        """
        修改DspmIp信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIpInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIpInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmPersonalIdentify(
            self,
            request: models.ModifyDspmPersonalIdentifyRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmPersonalIdentifyResponse:
        """
        修改Dspm个人身份id
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmPersonalIdentify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmPersonalIdentifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmRestoreLogTask(
            self,
            request: models.ModifyDspmRestoreLogTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmRestoreLogTaskResponse:
        """
        恢复备份日志
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmRestoreLogTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmRestoreLogTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmRiskInfo(
            self,
            request: models.ModifyDspmRiskInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmRiskInfoResponse:
        """
        修改Dspm风险信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmRiskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmRiskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmRiskStrategy(
            self,
            request: models.ModifyDspmRiskStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmRiskStrategyResponse:
        """
        修改Dspm风险策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmRiskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmRiskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmWhitelistStrategy(
            self,
            request: models.ModifyDspmWhitelistStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmWhitelistStrategyResponse:
        """
        修改Dspm白名单策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmWhitelistStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmWhitelistStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEDRRule(
            self,
            request: models.ModifyEDRRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyEDRRuleResponse:
        """
        编辑或者创建EDR策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEDRRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEDRRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEDRRuleStatus(
            self,
            request: models.ModifyEDRRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEDRRuleStatusResponse:
        """
        修改EDR策略开关状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEDRRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEDRRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEDRRulesAction(
            self,
            request: models.ModifyEDRRulesActionRequest,
            opts: Dict = None,
    ) -> models.ModifyEDRRulesActionResponse:
        """
        批量修改EDR策略动作
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEDRRulesAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEDRRulesActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdrAlertIsolation(
            self,
            request: models.ModifyEdrAlertIsolationRequest,
            opts: Dict = None,
    ) -> models.ModifyEdrAlertIsolationResponse:
        """
        EDR告警隔离和恢复
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdrAlertIsolation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdrAlertIsolationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdrAlertPermanentIgnore(
            self,
            request: models.ModifyEdrAlertPermanentIgnoreRequest,
            opts: Dict = None,
    ) -> models.ModifyEdrAlertPermanentIgnoreResponse:
        """
        永久忽略EDR多行为告警，将告警对应的主机+规则加入AI-Link永久忽略白名单，后续同类告警将自动丢弃
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdrAlertPermanentIgnore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdrAlertPermanentIgnoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdrAlertStatus(
            self,
            request: models.ModifyEdrAlertStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEdrAlertStatusResponse:
        """
        EDR告警状态处置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdrAlertStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdrAlertStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdrExcludeNetworkSegments(
            self,
            request: models.ModifyEdrExcludeNetworkSegmentsRequest,
            opts: Dict = None,
    ) -> models.ModifyEdrExcludeNetworkSegmentsResponse:
        """
        修改日志采集例外网段配置，支持IP/IP段/CIDR格式，最多可添加100条
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdrExcludeNetworkSegments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdrExcludeNetworkSegmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdrLogCollectPath(
            self,
            request: models.ModifyEdrLogCollectPathRequest,
            opts: Dict = None,
    ) -> models.ModifyEdrLogCollectPathResponse:
        """
        修改应用日志采集路径配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdrLogCollectPath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdrLogCollectPathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExposureAutoTagRule(
            self,
            request: models.ModifyExposureAutoTagRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyExposureAutoTagRuleResponse:
        """
        云边界自动打标-更新规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExposureAutoTagRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExposureAutoTagRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExposureAutoTagRuleStatus(
            self,
            request: models.ModifyExposureAutoTagRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyExposureAutoTagRuleStatusResponse:
        """
        云边界自动打标-启停规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExposureAutoTagRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExposureAutoTagRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExposureTag(
            self,
            request: models.ModifyExposureTagRequest,
            opts: Dict = None,
    ) -> models.ModifyExposureTagResponse:
        """
        更新云边界自定义标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExposureTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExposureTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIaCTokenPeriod(
            self,
            request: models.ModifyIaCTokenPeriodRequest,
            opts: Dict = None,
    ) -> models.ModifyIaCTokenPeriodResponse:
        """
        修改IaC检测接入Token存储周期
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIaCTokenPeriod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIaCTokenPeriodResponse
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
        修改主机资产备注信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachineRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachineRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMachinesLoginType(
            self,
            request: models.ModifyMachinesLoginTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyMachinesLoginTypeResponse:
        """
        批量修改主机登录方式
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachinesLoginType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachinesLoginTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMalwareTimingScanSettings(
            self,
            request: models.ModifyMalwareTimingScanSettingsRequest,
            opts: Dict = None,
    ) -> models.ModifyMalwareTimingScanSettingsResponse:
        """
        修改文件查杀定时扫描配置，包含扫描周期、检测模式、资产范围、引擎选择、隔离配置等
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMalwareTimingScanSettings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMalwareTimingScanSettingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNFSScanConf(
            self,
            request: models.ModifyNFSScanConfRequest,
            opts: Dict = None,
    ) -> models.ModifyNFSScanConfResponse:
        """
        新增或更新NFS扫描全局配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNFSScanConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNFSScanConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNFSScanHost(
            self,
            request: models.ModifyNFSScanHostRequest,
            opts: Dict = None,
    ) -> models.ModifyNFSScanHostResponse:
        """
        关闭进程守护功能
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNFSScanHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNFSScanHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetAttackSetting(
            self,
            request: models.ModifyNetAttackSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyNetAttackSettingResponse:
        """
        修改网络攻击检测开关及资产范围配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetAttackSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetAttackSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotifyAssetConfig(
            self,
            request: models.ModifyNotifyAssetConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyNotifyAssetConfigResponse:
        """
        修改通知资产范围配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotifyAssetConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotifyAssetConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotifySetting(
            self,
            request: models.ModifyNotifySettingRequest,
            opts: Dict = None,
    ) -> models.ModifyNotifySettingResponse:
        """
        修改通知设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotifySetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotifySettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotifySettingAlert(
            self,
            request: models.ModifyNotifySettingAlertRequest,
            opts: Dict = None,
    ) -> models.ModifyNotifySettingAlertResponse:
        """
        修改告警中心通知高级配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotifySettingAlert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotifySettingAlertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOrganizationAccountStatus(
            self,
            request: models.ModifyOrganizationAccountStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyOrganizationAccountStatusResponse:
        """
        修改集团账号状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOrganizationAccountStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOrganizationAccountStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPolicyStatus(
            self,
            request: models.ModifyPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyPolicyStatusResponse:
        """
        修改策略状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProtectionSetting(
            self,
            request: models.ModifyProtectionSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyProtectionSettingResponse:
        """
        重保防护包防护设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProtectionSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProtectionSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRaspLicenseBinds(
            self,
            request: models.ModifyRaspLicenseBindsRequest,
            opts: Dict = None,
    ) -> models.ModifyRaspLicenseBindsResponse:
        """
        重保防护授权包绑定
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRaspLicenseBinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRaspLicenseBindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReverseShellSystemPolicyConfig(
            self,
            request: models.ModifyReverseShellSystemPolicyConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyReverseShellSystemPolicyConfigResponse:
        """
        修改反弹Shell内网告警与资产范围配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReverseShellSystemPolicyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReverseShellSystemPolicyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskCenterRiskStatus(
            self,
            request: models.ModifyRiskCenterRiskStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskCenterRiskStatusResponse:
        """
        修改风险中心风险状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskCenterRiskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskCenterRiskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskCenterScanTask(
            self,
            request: models.ModifyRiskCenterScanTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskCenterScanTaskResponse:
        """
        修改风险中心扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskCenterScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskCenterScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskScanCronConfig(
            self,
            request: models.ModifyRiskScanCronConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskScanCronConfigResponse:
        """
        更新周期扫描计划
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskScanCronConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskScanCronConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyShareUserCSPM(
            self,
            request: models.ModifyShareUserCSPMRequest,
            opts: Dict = None,
    ) -> models.ModifyShareUserCSPMResponse:
        """
        编辑CSPM共享账号
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyShareUserCSPM"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyShareUserCSPMResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUebaRuleSwitch(
            self,
            request: models.ModifyUebaRuleSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyUebaRuleSwitchResponse:
        """
        更新自定义策略的开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUebaRuleSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUebaRuleSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulScanPeriodic(
            self,
            request: models.ModifyVulScanPeriodicRequest,
            opts: Dict = None,
    ) -> models.ModifyVulScanPeriodicResponse:
        """
        修改漏洞扫描（周期扫描）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulScanPeriodic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulScanPeriodicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulWhitelistConfig(
            self,
            request: models.ModifyVulWhitelistConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyVulWhitelistConfigResponse:
        """
        修改漏洞白名单配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulWhitelistConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulWhitelistConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulWhitelistSwitch(
            self,
            request: models.ModifyVulWhitelistSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyVulWhitelistSwitchResponse:
        """
        修改漏洞白名单开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulWhitelistSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulWhitelistSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OperateRisk(
            self,
            request: models.OperateRiskRequest,
            opts: Dict = None,
    ) -> models.OperateRiskResponse:
        """
        风险操作示例
        """
        
        kwargs = {}
        kwargs["action"] = "OperateRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OperateRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OperateRiskRulePolicy(
            self,
            request: models.OperateRiskRulePolicyRequest,
            opts: Dict = None,
    ) -> models.OperateRiskRulePolicyResponse:
        """
        自定义风险规则
        """
        
        kwargs = {}
        kwargs["action"] = "OperateRiskRulePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OperateRiskRulePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetDspmAssetAccountPassword(
            self,
            request: models.ResetDspmAssetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetDspmAssetAccountPasswordResponse:
        """
        重置Dspm资产账号密码
        """
        
        kwargs = {}
        kwargs["action"] = "ResetDspmAssetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetDspmAssetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryDspmExportLog(
            self,
            request: models.RetryDspmExportLogRequest,
            opts: Dict = None,
    ) -> models.RetryDspmExportLogResponse:
        """
        RetryExportLog
        """
        
        kwargs = {}
        kwargs["action"] = "RetryDspmExportLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryDspmExportLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevertDspmAssetAccount(
            self,
            request: models.RevertDspmAssetAccountRequest,
            opts: Dict = None,
    ) -> models.RevertDspmAssetAccountResponse:
        """
        恢复Dspm资产账号
        """
        
        kwargs = {}
        kwargs["action"] = "RevertDspmAssetAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevertDspmAssetAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanBaselineAssetItemList(
            self,
            request: models.ScanBaselineAssetItemListRequest,
            opts: Dict = None,
    ) -> models.ScanBaselineAssetItemListResponse:
        """
        对单个资产的部分检测项发起重新扫描（资产详情页“重新扫描”入口）。
        """
        
        kwargs = {}
        kwargs["action"] = "ScanBaselineAssetItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanBaselineAssetItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanBaselineItemList(
            self,
            request: models.ScanBaselineItemListRequest,
            opts: Dict = None,
    ) -> models.ScanBaselineItemListResponse:
        """
        对指定策略下的一批检测项发起重新扫描（策略详情页“检测项”维度的复扫入口）。
        """
        
        kwargs = {}
        kwargs["action"] = "ScanBaselineItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanBaselineItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanCSIPTaskAgain(
            self,
            request: models.ScanCSIPTaskAgainRequest,
            opts: Dict = None,
    ) -> models.ScanCSIPTaskAgainResponse:
        """
        CSIP 手动扫描任务删除接口
        """
        
        kwargs = {}
        kwargs["action"] = "ScanCSIPTaskAgain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanCSIPTaskAgainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanEDRTaskAgain(
            self,
            request: models.ScanEDRTaskAgainRequest,
            opts: Dict = None,
    ) -> models.ScanEDRTaskAgainResponse:
        """
        基于原任务配置新建扫描任务。AssetId为空时从TaskId获取全部资产信息；AssetId非空时仅含该单资产。
        """
        
        kwargs = {}
        kwargs["action"] = "ScanEDRTaskAgain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanEDRTaskAgainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendDspmAssetLoginSmsCode(
            self,
            request: models.SendDspmAssetLoginSmsCodeRequest,
            opts: Dict = None,
    ) -> models.SendDspmAssetLoginSmsCodeResponse:
        """
        发送Dspm资产访问验证码
        """
        
        kwargs = {}
        kwargs["action"] = "SendDspmAssetLoginSmsCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendDspmAssetLoginSmsCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartOrModifyPreventUninstall(
            self,
            request: models.StartOrModifyPreventUninstallRequest,
            opts: Dict = None,
    ) -> models.StartOrModifyPreventUninstallResponse:
        """
        开启或者修改防卸载功能配置
        """
        
        kwargs = {}
        kwargs["action"] = "StartOrModifyPreventUninstall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartOrModifyPreventUninstallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartOrModifyProcessDaemon(
            self,
            request: models.StartOrModifyProcessDaemonRequest,
            opts: Dict = None,
    ) -> models.StartOrModifyProcessDaemonResponse:
        """
        开启或者修改进程守护功能配置
        """
        
        kwargs = {}
        kwargs["action"] = "StartOrModifyProcessDaemon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartOrModifyProcessDaemonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopBaselineScanTask(
            self,
            request: models.StopBaselineScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopBaselineScanTaskResponse:
        """
        停止指定的基线扫描主任务，仅对处于 INIT / SUBTASK_CREATING / SCANNING 状态的任务生效。
        """
        
        kwargs = {}
        kwargs["action"] = "StopBaselineScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopBaselineScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCSIPManualMalwareScan(
            self,
            request: models.StopCSIPManualMalwareScanRequest,
            opts: Dict = None,
    ) -> models.StopCSIPManualMalwareScanResponse:
        """
        CSIP 手动扫描停止接口
        """
        
        kwargs = {}
        kwargs["action"] = "StopCSIPManualMalwareScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCSIPManualMalwareScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopEDRScanTask(
            self,
            request: models.StopEDRScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopEDRScanTaskResponse:
        """
        停止或取消扫描任务。SCANNING状态调RPC停止，WAIT状态直接改库取消。只有任务创建者可操作。
        """
        
        kwargs = {}
        kwargs["action"] = "StopEDRScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopEDRScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopPreventUninstall(
            self,
            request: models.StopPreventUninstallRequest,
            opts: Dict = None,
    ) -> models.StopPreventUninstallResponse:
        """
        关闭防卸载功能
        """
        
        kwargs = {}
        kwargs["action"] = "StopPreventUninstall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopPreventUninstallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopProcessDaemon(
            self,
            request: models.StopProcessDaemonRequest,
            opts: Dict = None,
    ) -> models.StopProcessDaemonResponse:
        """
        关闭进程守护功能
        """
        
        kwargs = {}
        kwargs["action"] = "StopProcessDaemon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopProcessDaemonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopRiskCenterTask(
            self,
            request: models.StopRiskCenterTaskRequest,
            opts: Dict = None,
    ) -> models.StopRiskCenterTaskResponse:
        """
        停止扫风险中心扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopRiskCenterTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRiskCenterTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopVulScanTask(
            self,
            request: models.StopVulScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopVulScanTaskResponse:
        """
        停止漏洞扫描（任务扫描）
        """
        
        kwargs = {}
        kwargs["action"] = "StopVulScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopVulScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncDspmAssets(
            self,
            request: models.SyncDspmAssetsRequest,
            opts: Dict = None,
    ) -> models.SyncDspmAssetsResponse:
        """
        同步dspm支持的资产
        """
        
        kwargs = {}
        kwargs["action"] = "SyncDspmAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncDspmAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncDspmUsers(
            self,
            request: models.SyncDspmUsersRequest,
            opts: Dict = None,
    ) -> models.SyncDspmUsersResponse:
        """
        同步dspm用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "SyncDspmUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncDspmUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallClusterAgent(
            self,
            request: models.UninstallClusterAgentRequest,
            opts: Dict = None,
    ) -> models.UninstallClusterAgentResponse:
        """
        卸载集群容器安全Agent。
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallClusterAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallClusterAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAccessKeyAlarmStatus(
            self,
            request: models.UpdateAccessKeyAlarmStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateAccessKeyAlarmStatusResponse:
        """
        标记风险或者告警为 已处置/已忽略
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAccessKeyAlarmStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAccessKeyAlarmStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAccessKeyRemark(
            self,
            request: models.UpdateAccessKeyRemarkRequest,
            opts: Dict = None,
    ) -> models.UpdateAccessKeyRemarkResponse:
        """
        编辑访问密钥/源IP备注
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAccessKeyRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAccessKeyRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlertStatusList(
            self,
            request: models.UpdateAlertStatusListRequest,
            opts: Dict = None,
    ) -> models.UpdateAlertStatusListResponse:
        """
        批量告警状态处理接口
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlertStatusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAlertStatusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateClusterOwner(
            self,
            request: models.UpdateClusterOwnerRequest,
            opts: Dict = None,
    ) -> models.UpdateClusterOwnerResponse:
        """
        绑定、更新集群负责人
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateClusterOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateClusterOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyDspmAssetLoginCode(
            self,
            request: models.VerifyDspmAssetLoginCodeRequest,
            opts: Dict = None,
    ) -> models.VerifyDspmAssetLoginCodeResponse:
        """
        验证Dspm资产登录验证码
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyDspmAssetLoginCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyDspmAssetLoginCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)