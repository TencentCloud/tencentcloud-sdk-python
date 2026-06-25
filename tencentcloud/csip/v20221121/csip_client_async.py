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