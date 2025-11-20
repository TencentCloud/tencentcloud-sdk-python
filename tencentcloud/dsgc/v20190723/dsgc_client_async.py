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
from tencentcloud.dsgc.v20190723 import models
from typing import Dict


class DsgcClient(AbstractClient):
    _apiVersion = '2019-07-23'
    _endpoint = 'dsgc.tencentcloudapi.com'
    _service = 'dsgc'

    async def AuthorizeDSPAMetaResources(
            self,
            request: models.AuthorizeDSPAMetaResourcesRequest,
            opts: Dict = None,
    ) -> models.AuthorizeDSPAMetaResourcesResponse:
        """
        授权用户云资源
        """
        
        kwargs = {}
        kwargs["action"] = "AuthorizeDSPAMetaResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AuthorizeDSPAMetaResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindDSPAResourceCosBuckets(
            self,
            request: models.BindDSPAResourceCosBucketsRequest,
            opts: Dict = None,
    ) -> models.BindDSPAResourceCosBucketsResponse:
        """
        绑定或解绑COS桶
        """
        
        kwargs = {}
        kwargs["action"] = "BindDSPAResourceCosBuckets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindDSPAResourceCosBucketsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindDSPAResourceDatabases(
            self,
            request: models.BindDSPAResourceDatabasesRequest,
            opts: Dict = None,
    ) -> models.BindDSPAResourceDatabasesResponse:
        """
        绑定或解绑数据库实例DB
        """
        
        kwargs = {}
        kwargs["action"] = "BindDSPAResourceDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindDSPAResourceDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyDSPATemplate(
            self,
            request: models.CopyDSPATemplateRequest,
            opts: Dict = None,
    ) -> models.CopyDSPATemplateResponse:
        """
        复制合规组模板
        """
        
        kwargs = {}
        kwargs["action"] = "CopyDSPATemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyDSPATemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetSortingReportRetryTask(
            self,
            request: models.CreateAssetSortingReportRetryTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAssetSortingReportRetryTaskResponse:
        """
        创建资产梳理报表导出重试任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetSortingReportRetryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetSortingReportRetryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetSortingReportTask(
            self,
            request: models.CreateAssetSortingReportTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAssetSortingReportTaskResponse:
        """
        创建资产梳理报告任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetSortingReportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetSortingReportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPAAssessmentRiskLevel(
            self,
            request: models.CreateDSPAAssessmentRiskLevelRequest,
            opts: Dict = None,
    ) -> models.CreateDSPAAssessmentRiskLevelResponse:
        """
        风险项页面---创建风险等级
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPAAssessmentRiskLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPAAssessmentRiskLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPAAssessmentRiskTemplate(
            self,
            request: models.CreateDSPAAssessmentRiskTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateDSPAAssessmentRiskTemplateResponse:
        """
        风险评估模板---创建风险评估模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPAAssessmentRiskTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPAAssessmentRiskTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPAAssessmentTask(
            self,
            request: models.CreateDSPAAssessmentTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDSPAAssessmentTaskResponse:
        """
        新建DSPA风险评估任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPAAssessmentTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPAAssessmentTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPACOSDiscoveryTask(
            self,
            request: models.CreateDSPACOSDiscoveryTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDSPACOSDiscoveryTaskResponse:
        """
        新增COS分类分级扫描任务，单个用户最多允许创建100个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPACOSDiscoveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPACOSDiscoveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPACategory(
            self,
            request: models.CreateDSPACategoryRequest,
            opts: Dict = None,
    ) -> models.CreateDSPACategoryResponse:
        """
        新增分类，单个用户最多允许创建100个数据分类。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPACategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPACategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPACategoryRelation(
            self,
            request: models.CreateDSPACategoryRelationRequest,
            opts: Dict = None,
    ) -> models.CreateDSPACategoryRelationResponse:
        """
        创建分类关联关系
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPACategoryRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPACategoryRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPAComplianceGroup(
            self,
            request: models.CreateDSPAComplianceGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDSPAComplianceGroupResponse:
        """
        新增分类分级模板，单个用户最多允许创建100个合规组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPAComplianceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPAComplianceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPAComplianceRules(
            self,
            request: models.CreateDSPAComplianceRulesRequest,
            opts: Dict = None,
    ) -> models.CreateDSPAComplianceRulesResponse:
        """
        创建合规组分类规则关联关系
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPAComplianceRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPAComplianceRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPACosMetaResources(
            self,
            request: models.CreateDSPACosMetaResourcesRequest,
            opts: Dict = None,
    ) -> models.CreateDSPACosMetaResourcesResponse:
        """
        添加COS元数据
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPACosMetaResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPACosMetaResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPADbMetaResources(
            self,
            request: models.CreateDSPADbMetaResourcesRequest,
            opts: Dict = None,
    ) -> models.CreateDSPADbMetaResourcesResponse:
        """
        添加用户云上数据库类型资源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPADbMetaResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPADbMetaResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPADiscoveryRule(
            self,
            request: models.CreateDSPADiscoveryRuleRequest,
            opts: Dict = None,
    ) -> models.CreateDSPADiscoveryRuleResponse:
        """
        新增分类分级规则，单个用户最多允许创建200个规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPADiscoveryRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPADiscoveryRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPADiscoveryTask(
            self,
            request: models.CreateDSPADiscoveryTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDSPADiscoveryTaskResponse:
        """
        新增分类分级任务，单个用户最多允许创建100个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPADiscoveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPADiscoveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPALevelGroup(
            self,
            request: models.CreateDSPALevelGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDSPALevelGroupResponse:
        """
        新增分级，单个Casb实例最多允许创建100个数据分级
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPALevelGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPALevelGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPAMetaResources(
            self,
            request: models.CreateDSPAMetaResourcesRequest,
            opts: Dict = None,
    ) -> models.CreateDSPAMetaResourcesResponse:
        """
        添加用户云上资源列表
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPAMetaResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPAMetaResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDSPASelfBuildMetaResource(
            self,
            request: models.CreateDSPASelfBuildMetaResourceRequest,
            opts: Dict = None,
    ) -> models.CreateDSPASelfBuildMetaResourceResponse:
        """
        新建用户自建云资源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDSPASelfBuildMetaResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDSPASelfBuildMetaResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIdentifyRuleAnotherName(
            self,
            request: models.CreateIdentifyRuleAnotherNameRequest,
            opts: Dict = None,
    ) -> models.CreateIdentifyRuleAnotherNameResponse:
        """
        创建规则别名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIdentifyRuleAnotherName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIdentifyRuleAnotherNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DecribeSuggestRiskLevelMatrix(
            self,
            request: models.DecribeSuggestRiskLevelMatrixRequest,
            opts: Dict = None,
    ) -> models.DecribeSuggestRiskLevelMatrixResponse:
        """
        风险等级的定义页面-创建风险等级的时候生成的一个默认的矩阵
        """
        
        kwargs = {}
        kwargs["action"] = "DecribeSuggestRiskLevelMatrix"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DecribeSuggestRiskLevelMatrixResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCosMetaResource(
            self,
            request: models.DeleteCosMetaResourceRequest,
            opts: Dict = None,
    ) -> models.DeleteCosMetaResourceResponse:
        """
        本接口（DeleteCOSMetaData）用于删除COS元数据信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCosMetaResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCosMetaResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDSPAAssessmentTask(
            self,
            request: models.DeleteDSPAAssessmentTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteDSPAAssessmentTaskResponse:
        """
        删除DSPA风险评估任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDSPAAssessmentTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDSPAAssessmentTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDSPACOSDiscoveryTask(
            self,
            request: models.DeleteDSPACOSDiscoveryTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteDSPACOSDiscoveryTaskResponse:
        """
        删除COS分类分级任务，该接口只有在任务状态为以下几个状态值时才支持正确删除：
        0 待扫描，
        2 扫描终止，
        3 扫描成功，
        4 扫描失败
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDSPACOSDiscoveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDSPACOSDiscoveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDSPACOSDiscoveryTaskResult(
            self,
            request: models.DeleteDSPACOSDiscoveryTaskResultRequest,
            opts: Dict = None,
    ) -> models.DeleteDSPACOSDiscoveryTaskResultResponse:
        """
        删除COS分类分级任务结果
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDSPACOSDiscoveryTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDSPACOSDiscoveryTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDSPADiscoveryTask(
            self,
            request: models.DeleteDSPADiscoveryTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteDSPADiscoveryTaskResponse:
        """
        删除分类分级识别任务，该接口只有在任务状态为以下几个状态值时才支持正确删除：
        0 待扫描，
        2 扫描终止，
        3 扫描成功，
        4 扫描失败
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDSPADiscoveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDSPADiscoveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDSPADiscoveryTaskResult(
            self,
            request: models.DeleteDSPADiscoveryTaskResultRequest,
            opts: Dict = None,
    ) -> models.DeleteDSPADiscoveryTaskResultResponse:
        """
        删除分类分级识别任务结果
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDSPADiscoveryTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDSPADiscoveryTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDSPAMetaResource(
            self,
            request: models.DeleteDSPAMetaResourceRequest,
            opts: Dict = None,
    ) -> models.DeleteDSPAMetaResourceResponse:
        """
        删除用户云资源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDSPAMetaResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDSPAMetaResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDetailDataExportResult(
            self,
            request: models.DescribeAssetDetailDataExportResultRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDetailDataExportResultResponse:
        """
        查询敏感数据导出结果URL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDetailDataExportResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDetailDataExportResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetOverview(
            self,
            request: models.DescribeAssetOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetOverviewResponse:
        """
        数据资产报告页面-查询数据资产概览接口（包括数据库资产详情和存储资产详情）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindDBList(
            self,
            request: models.DescribeBindDBListRequest,
            opts: Dict = None,
    ) -> models.DescribeBindDBListResponse:
        """
        查询DB绑定的列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindDBList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindDBListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCOSAssetSensitiveDistribution(
            self,
            request: models.DescribeCOSAssetSensitiveDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeCOSAssetSensitiveDistributionResponse:
        """
        数据资产报告-查询cos的资产分布详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCOSAssetSensitiveDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCOSAssetSensitiveDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentHighRiskTop10Overview(
            self,
            request: models.DescribeDSPAAssessmentHighRiskTop10OverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentHighRiskTop10OverviewResponse:
        """
        查询高风险资产的top10
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentHighRiskTop10Overview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentHighRiskTop10OverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentLatestRiskDetailInfo(
            self,
            request: models.DescribeDSPAAssessmentLatestRiskDetailInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentLatestRiskDetailInfoResponse:
        """
        查询最新风险项详情数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentLatestRiskDetailInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentLatestRiskDetailInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentLatestRiskList(
            self,
            request: models.DescribeDSPAAssessmentLatestRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentLatestRiskListResponse:
        """
        查询最新的风险详情列表数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentLatestRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentLatestRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentNewDiscoveredRiskOverview(
            self,
            request: models.DescribeDSPAAssessmentNewDiscoveredRiskOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentNewDiscoveredRiskOverviewResponse:
        """
        风险概览-查询新发现风险统计数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentNewDiscoveredRiskOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentNewDiscoveredRiskOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentPendingRiskOverview(
            self,
            request: models.DescribeDSPAAssessmentPendingRiskOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentPendingRiskOverviewResponse:
        """
        风险概览-查询待处理风险统计数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentPendingRiskOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentPendingRiskOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentProcessingRiskOverview(
            self,
            request: models.DescribeDSPAAssessmentProcessingRiskOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentProcessingRiskOverviewResponse:
        """
        风险概览-查询处理中风险统计数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentProcessingRiskOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentProcessingRiskOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskAmountOverview(
            self,
            request: models.DescribeDSPAAssessmentRiskAmountOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskAmountOverviewResponse:
        """
        风险概览页风险数量和受影响资产数概览统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskAmountOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskAmountOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskDatasourceTop5(
            self,
            request: models.DescribeDSPAAssessmentRiskDatasourceTop5Request,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskDatasourceTop5Response:
        """
        受影响资产TOP5统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskDatasourceTop5"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskDatasourceTop5Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskDealedOverview(
            self,
            request: models.DescribeDSPAAssessmentRiskDealedOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskDealedOverviewResponse:
        """
        遗留待处理&昨日完成风险处置概览统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskDealedOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskDealedOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskDealedTrend(
            self,
            request: models.DescribeDSPAAssessmentRiskDealedTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskDealedTrendResponse:
        """
        风险项处理趋势统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskDealedTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskDealedTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskDistributionOverview(
            self,
            request: models.DescribeDSPAAssessmentRiskDistributionOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskDistributionOverviewResponse:
        """
        查询风险分布数据，包含风险类型分布，风险详情分布，风险资产的分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskDistributionOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskDistributionOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskItemTop5(
            self,
            request: models.DescribeDSPAAssessmentRiskItemTop5Request,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskItemTop5Response:
        """
        风险分类TOP5统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskItemTop5"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskItemTop5Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskLevelDetail(
            self,
            request: models.DescribeDSPAAssessmentRiskLevelDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskLevelDetailResponse:
        """
        风险项页面----查询风险等级的详情数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskLevelDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskLevelDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskLevelList(
            self,
            request: models.DescribeDSPAAssessmentRiskLevelListRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskLevelListResponse:
        """
        风险项页面----查询风险等级的列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskLevelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskLevelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskLevelTrend(
            self,
            request: models.DescribeDSPAAssessmentRiskLevelTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskLevelTrendResponse:
        """
        风险级别趋势统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskLevelTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskLevelTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskOverview(
            self,
            request: models.DescribeDSPAAssessmentRiskOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskOverviewResponse:
        """
        风险数量概览统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskProcessHistory(
            self,
            request: models.DescribeDSPAAssessmentRiskProcessHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskProcessHistoryResponse:
        """
        查询风险的处理历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskProcessHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskProcessHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskSideDistributed(
            self,
            request: models.DescribeDSPAAssessmentRiskSideDistributedRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskSideDistributedResponse:
        """
        风险评估概览页，查询风险面的分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskSideDistributed"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskSideDistributedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskSideList(
            self,
            request: models.DescribeDSPAAssessmentRiskSideListRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskSideListResponse:
        """
        风险评估概览页，查询风险面的分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskSideList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskSideListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskTemplateDetail(
            self,
            request: models.DescribeDSPAAssessmentRiskTemplateDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskTemplateDetailResponse:
        """
        风险项页面--查看评估模板详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskTemplateDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskTemplateDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRiskTemplateVulnerableList(
            self,
            request: models.DescribeDSPAAssessmentRiskTemplateVulnerableListRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRiskTemplateVulnerableListResponse:
        """
        风险模板页面--查询风险模板中的脆弱项配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRiskTemplateVulnerableList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRiskTemplateVulnerableListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentRisks(
            self,
            request: models.DescribeDSPAAssessmentRisksRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentRisksResponse:
        """
        获取DSPA评估风险项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentRisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentRisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentTasks(
            self,
            request: models.DescribeDSPAAssessmentTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentTasksResponse:
        """
        获取DSPA评估任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentTemplateControlItems(
            self,
            request: models.DescribeDSPAAssessmentTemplateControlItemsRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentTemplateControlItemsResponse:
        """
        获取DSPA评估模板关联的评估控制项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentTemplateControlItems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentTemplateControlItemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAAssessmentTemplates(
            self,
            request: models.DescribeDSPAAssessmentTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAAssessmentTemplatesResponse:
        """
        获取DSPA评估模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAAssessmentTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAAssessmentTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACOSDataAssetBuckets(
            self,
            request: models.DescribeDSPACOSDataAssetBucketsRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACOSDataAssetBucketsResponse:
        """
        获取COS敏感数据资产桶列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACOSDataAssetBuckets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACOSDataAssetBucketsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACOSDataAssetByComplianceId(
            self,
            request: models.DescribeDSPACOSDataAssetByComplianceIdRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACOSDataAssetByComplianceIdResponse:
        """
        获取COS单个模板下的敏感数据资产
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACOSDataAssetByComplianceId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACOSDataAssetByComplianceIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACOSDataAssetDetail(
            self,
            request: models.DescribeDSPACOSDataAssetDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACOSDataAssetDetailResponse:
        """
        获取COS分类分级数据资产详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACOSDataAssetDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACOSDataAssetDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACOSDiscoveryTaskDetail(
            self,
            request: models.DescribeDSPACOSDiscoveryTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACOSDiscoveryTaskDetailResponse:
        """
        获取COS分类分级任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACOSDiscoveryTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACOSDiscoveryTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACOSDiscoveryTaskFiles(
            self,
            request: models.DescribeDSPACOSDiscoveryTaskFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACOSDiscoveryTaskFilesResponse:
        """
        获取COS分类分级任务结果详情文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACOSDiscoveryTaskFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACOSDiscoveryTaskFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACOSDiscoveryTaskResult(
            self,
            request: models.DescribeDSPACOSDiscoveryTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACOSDiscoveryTaskResultResponse:
        """
        获取COS分类分级任务结果，该接口只有在任务状态为以下状态时才支持结果正常查询：
        3 扫描成功，
        4 扫描失败
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACOSDiscoveryTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACOSDiscoveryTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACOSDiscoveryTasks(
            self,
            request: models.DescribeDSPACOSDiscoveryTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACOSDiscoveryTasksResponse:
        """
        获取COS分类分级任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACOSDiscoveryTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACOSDiscoveryTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACOSTaskResultDetail(
            self,
            request: models.DescribeDSPACOSTaskResultDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACOSTaskResultDetailResponse:
        """
        获取COS分类分级任务结果详情，该接口只有在任务状态为时才支持结果正确查询：
        3 扫描成功
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACOSTaskResultDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACOSTaskResultDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACategories(
            self,
            request: models.DescribeDSPACategoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACategoriesResponse:
        """
        获取敏感数据分类列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACategories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACategoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACategoryRuleStatistic(
            self,
            request: models.DescribeDSPACategoryRuleStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACategoryRuleStatisticResponse:
        """
        获取分类规则统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACategoryRuleStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACategoryRuleStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACategoryRules(
            self,
            request: models.DescribeDSPACategoryRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACategoryRulesResponse:
        """
        获取合规组分类规则信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACategoryRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACategoryRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACategoryTree(
            self,
            request: models.DescribeDSPACategoryTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACategoryTreeResponse:
        """
        获取分类树信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACategoryTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACategoryTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPACategoryTreeWithRules(
            self,
            request: models.DescribeDSPACategoryTreeWithRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPACategoryTreeWithRulesResponse:
        """
        获取分类规则树信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPACategoryTreeWithRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPACategoryTreeWithRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAComplianceGroupDetail(
            self,
            request: models.DescribeDSPAComplianceGroupDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAComplianceGroupDetailResponse:
        """
        获取模板详情信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAComplianceGroupDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAComplianceGroupDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAComplianceGroups(
            self,
            request: models.DescribeDSPAComplianceGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAComplianceGroupsResponse:
        """
        获取分类分级模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAComplianceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAComplianceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAComplianceUpdateNotification(
            self,
            request: models.DescribeDSPAComplianceUpdateNotificationRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAComplianceUpdateNotificationResponse:
        """
        获取模板更新提示信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAComplianceUpdateNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAComplianceUpdateNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPADataSourceDbInfo(
            self,
            request: models.DescribeDSPADataSourceDbInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPADataSourceDbInfoResponse:
        """
        获取数据源的数据库信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPADataSourceDbInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPADataSourceDbInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPADiscoveryRules(
            self,
            request: models.DescribeDSPADiscoveryRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPADiscoveryRulesResponse:
        """
        获取分类分级规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPADiscoveryRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPADiscoveryRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPADiscoveryServiceStatus(
            self,
            request: models.DescribeDSPADiscoveryServiceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPADiscoveryServiceStatusResponse:
        """
        用于查询该用户是否已开通分类分级服务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPADiscoveryServiceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPADiscoveryServiceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPADiscoveryTaskDetail(
            self,
            request: models.DescribeDSPADiscoveryTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPADiscoveryTaskDetailResponse:
        """
        获取分类分级任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPADiscoveryTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPADiscoveryTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPADiscoveryTaskResult(
            self,
            request: models.DescribeDSPADiscoveryTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPADiscoveryTaskResultResponse:
        """
        获取分类分级任务结果，该接口只有在任务状态为以下状态时才支持结果正常查询：3 扫描成功，4 扫描失败
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPADiscoveryTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPADiscoveryTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPADiscoveryTaskResultDetail(
            self,
            request: models.DescribeDSPADiscoveryTaskResultDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPADiscoveryTaskResultDetailResponse:
        """
        获取分类分级任务结果详情，该接口只有在任务状态为时才支持结果正确查询：
        3 扫描成功
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPADiscoveryTaskResultDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPADiscoveryTaskResultDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPADiscoveryTaskTables(
            self,
            request: models.DescribeDSPADiscoveryTaskTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPADiscoveryTaskTablesResponse:
        """
        获取分级分级扫描的表集合
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPADiscoveryTaskTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPADiscoveryTaskTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPADiscoveryTasks(
            self,
            request: models.DescribeDSPADiscoveryTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPADiscoveryTasksResponse:
        """
        获取分类分级任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPADiscoveryTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPADiscoveryTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAESDataAssetByComplianceId(
            self,
            request: models.DescribeDSPAESDataAssetByComplianceIdRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAESDataAssetByComplianceIdResponse:
        """
        根据合规组id，去查询ES的概览页统计数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAESDataAssetByComplianceId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAESDataAssetByComplianceIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAESDataAssetDetail(
            self,
            request: models.DescribeDSPAESDataAssetDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAESDataAssetDetailResponse:
        """
        根据合规组id，去查询ES的概览页下的统计列表数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAESDataAssetDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAESDataAssetDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAESDataSample(
            self,
            request: models.DescribeDSPAESDataSampleRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAESDataSampleResponse:
        """
        获取ES扫描结果数据样本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAESDataSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAESDataSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPAESDiscoveryTaskResultDetail(
            self,
            request: models.DescribeDSPAESDiscoveryTaskResultDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPAESDiscoveryTaskResultDetailResponse:
        """
        获取ES的分类分级任务结果详情，该接口只有在任务状态为时才支持结果正确查询：
        3 扫描成功
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPAESDiscoveryTaskResultDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPAESDiscoveryTaskResultDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPALevelDetail(
            self,
            request: models.DescribeDSPALevelDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPALevelDetailResponse:
        """
        获取分级详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPALevelDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPALevelDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPALevelGroups(
            self,
            request: models.DescribeDSPALevelGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPALevelGroupsResponse:
        """
        获取分级列表，限制100个 不分页返回
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPALevelGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPALevelGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPARDBDataAssetByComplianceId(
            self,
            request: models.DescribeDSPARDBDataAssetByComplianceIdRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPARDBDataAssetByComplianceIdResponse:
        """
        获取单个合规组下的RDB关系数据库分类分级数据资产
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPARDBDataAssetByComplianceId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPARDBDataAssetByComplianceIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPARDBDataAssetDetail(
            self,
            request: models.DescribeDSPARDBDataAssetDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPARDBDataAssetDetailResponse:
        """
        获取RDB关系数据库分类分级资产详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPARDBDataAssetDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPARDBDataAssetDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPASupportedMetas(
            self,
            request: models.DescribeDSPASupportedMetasRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPASupportedMetasResponse:
        """
        拉取DSPA支持的Meta元数据类型，返回包括：元数据类型，支持的元数据地域信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPASupportedMetas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPASupportedMetasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDSPATaskResultDataSample(
            self,
            request: models.DescribeDSPATaskResultDataSampleRequest,
            opts: Dict = None,
    ) -> models.DescribeDSPATaskResultDataSampleResponse:
        """
        获取扫描结果数据样本
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDSPATaskResultDataSample"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDSPATaskResultDataSampleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeESAssetSensitiveDistribution(
            self,
            request: models.DescribeESAssetSensitiveDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeESAssetSensitiveDistributionResponse:
        """
        数据资产报告-查询es的敏感资产报告，包含（数据库资产，设敏级别数据库top10，资产详情）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeESAssetSensitiveDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeESAssetSensitiveDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportTaskResult(
            self,
            request: models.DescribeExportTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeExportTaskResultResponse:
        """
        获取导出任务结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMongoAssetSensitiveDistribution(
            self,
            request: models.DescribeMongoAssetSensitiveDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeMongoAssetSensitiveDistributionResponse:
        """
        数据资产报告-查询mongo 的敏感资产报告，包含（数据库资产，设敏级别数据库top10，资产详情）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMongoAssetSensitiveDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMongoAssetSensitiveDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRDBAssetSensitiveDistribution(
            self,
            request: models.DescribeRDBAssetSensitiveDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeRDBAssetSensitiveDistributionResponse:
        """
        数据资产报告-查询rbd 的敏感资产报告，包含（数据库资产，设敏级别数据库top10，资产详情）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRDBAssetSensitiveDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRDBAssetSensitiveDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReportTaskDownloadUrl(
            self,
            request: models.DescribeReportTaskDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeReportTaskDownloadUrlResponse:
        """
        获取报表下载链接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReportTaskDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReportTaskDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReportTasks(
            self,
            request: models.DescribeReportTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeReportTasksResponse:
        """
        获取资产报表任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSensitiveCOSDataDistribution(
            self,
            request: models.DescribeSensitiveCOSDataDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeSensitiveCOSDataDistributionResponse:
        """
        数据资产报告-查询cos的敏感数据分布（分级分布 分类分布 敏感规则分布详情列表）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSensitiveCOSDataDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSensitiveCOSDataDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSensitiveRDBDataDistribution(
            self,
            request: models.DescribeSensitiveRDBDataDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeSensitiveRDBDataDistributionResponse:
        """
        数据资产报告-查询rdb的敏感数据分布-敏感规则字段分布-敏感分布详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSensitiveRDBDataDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSensitiveRDBDataDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableDSPAMetaResourceAuth(
            self,
            request: models.DisableDSPAMetaResourceAuthRequest,
            opts: Dict = None,
    ) -> models.DisableDSPAMetaResourceAuthResponse:
        """
        取消用户云资源授权
        """
        
        kwargs = {}
        kwargs["action"] = "DisableDSPAMetaResourceAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableDSPAMetaResourceAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableDSPADiscoveryRule(
            self,
            request: models.EnableDSPADiscoveryRuleRequest,
            opts: Dict = None,
    ) -> models.EnableDSPADiscoveryRuleResponse:
        """
        打开或者关闭分类分级规则
        注：此API同时对该规则下的RDB跟COS规则操作。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableDSPADiscoveryRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableDSPADiscoveryRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableTrialVersion(
            self,
            request: models.EnableTrialVersionRequest,
            opts: Dict = None,
    ) -> models.EnableTrialVersionResponse:
        """
        启用版本体验
        """
        
        kwargs = {}
        kwargs["action"] = "EnableTrialVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableTrialVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAssetDetailData(
            self,
            request: models.ExportAssetDetailDataRequest,
            opts: Dict = None,
    ) -> models.ExportAssetDetailDataResponse:
        """
        创建敏感数据导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAssetDetailData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAssetDetailDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetResourceConnectionStatus(
            self,
            request: models.GetResourceConnectionStatusRequest,
            opts: Dict = None,
    ) -> models.GetResourceConnectionStatusResponse:
        """
        获取授权资源的连接状态
        """
        
        kwargs = {}
        kwargs["action"] = "GetResourceConnectionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetResourceConnectionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTrialVersion(
            self,
            request: models.GetTrialVersionRequest,
            opts: Dict = None,
    ) -> models.GetTrialVersionResponse:
        """
        获取体验版本信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetTrialVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTrialVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUserQuotaInfo(
            self,
            request: models.GetUserQuotaInfoRequest,
            opts: Dict = None,
    ) -> models.GetUserQuotaInfoResponse:
        """
        获取用户购买配额信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetUserQuotaInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUserQuotaInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDSPAClusters(
            self,
            request: models.ListDSPAClustersRequest,
            opts: Dict = None,
    ) -> models.ListDSPAClustersResponse:
        """
        拉取DSPA集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListDSPAClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDSPAClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDSPACosMetaResources(
            self,
            request: models.ListDSPACosMetaResourcesRequest,
            opts: Dict = None,
    ) -> models.ListDSPACosMetaResourcesResponse:
        """
        本接口用于获取COS元数据信息，返回COS元数据信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListDSPACosMetaResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDSPACosMetaResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDSPAMetaResources(
            self,
            request: models.ListDSPAMetaResourcesRequest,
            opts: Dict = None,
    ) -> models.ListDSPAMetaResourcesResponse:
        """
        拉取用户云资源
        """
        
        kwargs = {}
        kwargs["action"] = "ListDSPAMetaResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDSPAMetaResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPAAssessmentRisk(
            self,
            request: models.ModifyDSPAAssessmentRiskRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPAAssessmentRiskResponse:
        """
        修改DSPA评估风险项，支持修改Status
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPAAssessmentRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPAAssessmentRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPAAssessmentRiskLatest(
            self,
            request: models.ModifyDSPAAssessmentRiskLatestRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPAAssessmentRiskLatestResponse:
        """
        修改最新评估风险项状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPAAssessmentRiskLatest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPAAssessmentRiskLatestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPAAssessmentRiskLevel(
            self,
            request: models.ModifyDSPAAssessmentRiskLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPAAssessmentRiskLevelResponse:
        """
        风险项页面----修改风险等级的详情数据
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPAAssessmentRiskLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPAAssessmentRiskLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPAAssessmentRiskTemplate(
            self,
            request: models.ModifyDSPAAssessmentRiskTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPAAssessmentRiskTemplateResponse:
        """
        风险模板---修改风险模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPAAssessmentRiskTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPAAssessmentRiskTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPACOSDiscoveryTask(
            self,
            request: models.ModifyDSPACOSDiscoveryTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPACOSDiscoveryTaskResponse:
        """
        修改COS分类分级任务，该接口只有在任务状态为以下状态时才支持正确修改：
        0 待扫描，
        2 扫描终止，
        3 扫描成功，
        4 扫描失败
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPACOSDiscoveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPACOSDiscoveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPACOSTaskResult(
            self,
            request: models.ModifyDSPACOSTaskResultRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPACOSTaskResultResponse:
        """
        调整COS任务扫描结果
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPACOSTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPACOSTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPACategory(
            self,
            request: models.ModifyDSPACategoryRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPACategoryResponse:
        """
        修改分类，内置分类不支持修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPACategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPACategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPACategoryRelation(
            self,
            request: models.ModifyDSPACategoryRelationRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPACategoryRelationResponse:
        """
        修改分类分级关系
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPACategoryRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPACategoryRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPAClusterInfo(
            self,
            request: models.ModifyDSPAClusterInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPAClusterInfoResponse:
        """
        修改DSPA集群信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPAClusterInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPAClusterInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPAComplianceGroup(
            self,
            request: models.ModifyDSPAComplianceGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPAComplianceGroupResponse:
        """
        修改分类分级模板，内置模板不支持修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPAComplianceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPAComplianceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPADiscoveryRule(
            self,
            request: models.ModifyDSPADiscoveryRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPADiscoveryRuleResponse:
        """
        修改分类分级规则，单个用户最多允许创建200个规则。
        注：此API同时适用RDB跟COS类型数据。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPADiscoveryRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPADiscoveryRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPADiscoveryTask(
            self,
            request: models.ModifyDSPADiscoveryTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPADiscoveryTaskResponse:
        """
        修改分类分级任务，该接口只有在任务状态为以下状态时才支持正确修改：
        0 待扫描，
        2 扫描终止，
        3 扫描成功，
        4 扫描失败
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPADiscoveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPADiscoveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPAESTaskResult(
            self,
            request: models.ModifyDSPAESTaskResultRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPAESTaskResultResponse:
        """
        调整ES任务扫描结果
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPAESTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPAESTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDSPATaskResult(
            self,
            request: models.ModifyDSPATaskResultRequest,
            opts: Dict = None,
    ) -> models.ModifyDSPATaskResultResponse:
        """
        调整任务扫描结果
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDSPATaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDSPATaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryDSPAMetaResourceDbList(
            self,
            request: models.QueryDSPAMetaResourceDbListRequest,
            opts: Dict = None,
    ) -> models.QueryDSPAMetaResourceDbListResponse:
        """
        查询DSPA实例的db列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryDSPAMetaResourceDbList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryDSPAMetaResourceDbListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryResourceDbBindStatus(
            self,
            request: models.QueryResourceDbBindStatusRequest,
            opts: Dict = None,
    ) -> models.QueryResourceDbBindStatusResponse:
        """
        获取资源绑定DB状态
        """
        
        kwargs = {}
        kwargs["action"] = "QueryResourceDbBindStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryResourceDbBindStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartDSPAAssessmentTask(
            self,
            request: models.RestartDSPAAssessmentTaskRequest,
            opts: Dict = None,
    ) -> models.RestartDSPAAssessmentTaskResponse:
        """
        重新启动DSPA风险评估任务
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDSPAAssessmentTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDSPAAssessmentTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartDSPADiscoveryTask(
            self,
            request: models.StartDSPADiscoveryTaskRequest,
            opts: Dict = None,
    ) -> models.StartDSPADiscoveryTaskResponse:
        """
        立即启动分类分级任务，该接口只有在任务状态为以下状态时才支持正确执行立即扫描：
        0 待扫描，
        2 扫描终止，
        3 扫描成功，
        4 扫描失败
        """
        
        kwargs = {}
        kwargs["action"] = "StartDSPADiscoveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartDSPADiscoveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopDSPADiscoveryTask(
            self,
            request: models.StopDSPADiscoveryTaskRequest,
            opts: Dict = None,
    ) -> models.StopDSPADiscoveryTaskResponse:
        """
        停止分类分级任务，该接口只有在任务状态为以下状态时才支持正确执行停止扫描：
        1 扫描中
        """
        
        kwargs = {}
        kwargs["action"] = "StopDSPADiscoveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopDSPADiscoveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDSPASelfBuildResource(
            self,
            request: models.UpdateDSPASelfBuildResourceRequest,
            opts: Dict = None,
    ) -> models.UpdateDSPASelfBuildResourceResponse:
        """
        更新自建资源基础信息，包括：端口、账户名、密码。
        请注意：
        如果资源自身的VPC、VIP信息发生变化，后台会自动更新。
        如果监听的端口发生变化，请显式输入端口。
        如果账户名密码任意一个发生变化，请务必同时显式输入账户名密码。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDSPASelfBuildResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDSPASelfBuildResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyDSPACOSRule(
            self,
            request: models.VerifyDSPACOSRuleRequest,
            opts: Dict = None,
    ) -> models.VerifyDSPACOSRuleResponse:
        """
        验证COS分类分级规则
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyDSPACOSRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyDSPACOSRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyDSPADiscoveryRule(
            self,
            request: models.VerifyDSPADiscoveryRuleRequest,
            opts: Dict = None,
    ) -> models.VerifyDSPADiscoveryRuleResponse:
        """
        验证分类分级规则
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyDSPADiscoveryRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyDSPADiscoveryRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)