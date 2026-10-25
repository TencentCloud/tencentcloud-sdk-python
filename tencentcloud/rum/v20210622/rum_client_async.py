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
from tencentcloud.rum.v20210622 import models
from typing import Dict


class RumClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'rum.tencentcloudapi.com'
    _service = 'rum'

    async def CreateFieldTransformRule(
            self,
            request: models.CreateFieldTransformRuleRequest,
            opts: Dict = None,
    ) -> models.CreateFieldTransformRuleResponse:
        """
        创建字段配置规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFieldTransformRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFieldTransformRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReleaseFile(
            self,
            request: models.CreateReleaseFileRequest,
            opts: Dict = None,
    ) -> models.CreateReleaseFileResponse:
        """
        创建对应项目的文件记录
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReleaseFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReleaseFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStarProject(
            self,
            request: models.CreateStarProjectRequest,
            opts: Dict = None,
    ) -> models.CreateStarProjectResponse:
        """
        个人用户添加星标项目
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStarProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStarProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTDEMApplication(
            self,
            request: models.CreateTDEMApplicationRequest,
            opts: Dict = None,
    ) -> models.CreateTDEMApplicationResponse:
        """
        在指定业务系统下创建应用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTDEMApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTDEMApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTDEMBusinessSystem(
            self,
            request: models.CreateTDEMBusinessSystemRequest,
            opts: Dict = None,
    ) -> models.CreateTDEMBusinessSystemResponse:
        """
        创建业务系统。InstanceId 由后端生成，格式 rum-<12 位随机字母数字>。重名返回 InvalidParameterValue。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTDEMBusinessSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTDEMBusinessSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTDEMDialTask(
            self,
            request: models.CreateTDEMDialTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTDEMDialTaskResponse:
        """
        创建一条移动拨测任务。同一应用处于 active 的任务最多 50 条。四项启动范围都为空时不限制启动；填写多项时必须同时满足，同一项多个值命中任意一个即可。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTDEMDialTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTDEMDialTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTDEMFieldTransformRule(
            self,
            request: models.CreateTDEMFieldTransformRuleRequest,
            opts: Dict = None,
    ) -> models.CreateTDEMFieldTransformRuleResponse:
        """
        为应用创建字段值替换规则，单应用上限 50 条。替代已废弃的 CreateFieldTransformRule；AppId 为 string。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTDEMFieldTransformRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTDEMFieldTransformRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTDEMFunnel(
            self,
            request: models.CreateTDEMFunnelRequest,
            opts: Dict = None,
    ) -> models.CreateTDEMFunnelResponse:
        """
        创建漏斗
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTDEMFunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTDEMFunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWhitelist(
            self,
            request: models.CreateWhitelistRequest,
            opts: Dict = None,
    ) -> models.CreateWhitelistResponse:
        """
        创建白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFieldTransformRule(
            self,
            request: models.DeleteFieldTransformRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteFieldTransformRuleResponse:
        """
        删除字段配置规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFieldTransformRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFieldTransformRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        删除实例，谨慎操作，不可恢复
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMiniProgramReplayPack(
            self,
            request: models.DeleteMiniProgramReplayPackRequest,
            opts: Dict = None,
    ) -> models.DeleteMiniProgramReplayPackResponse:
        """
        删除回放包元数据，并尽力删除COS上回放包与源码zip。不存在返回ResourceNotFound。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMiniProgramReplayPack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMiniProgramReplayPackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        删除给定的 rum 的项目
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReleaseFile(
            self,
            request: models.DeleteReleaseFileRequest,
            opts: Dict = None,
    ) -> models.DeleteReleaseFileResponse:
        """
        将对应 sourcemap 文件删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReleaseFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReleaseFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStarProject(
            self,
            request: models.DeleteStarProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteStarProjectResponse:
        """
        删除用户名下的星标项目
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStarProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStarProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSymbolArtifact(
            self,
            request: models.DeleteSymbolArtifactRequest,
            opts: Dict = None,
    ) -> models.DeleteSymbolArtifactResponse:
        """
        删除指定的符号制品。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSymbolArtifact"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSymbolArtifactResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTDEMApplication(
            self,
            request: models.DeleteTDEMApplicationRequest,
            opts: Dict = None,
    ) -> models.DeleteTDEMApplicationResponse:
        """
        逻辑删除应用，ProjectKey 即刻失效。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTDEMApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTDEMApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTDEMBusinessSystem(
            self,
            request: models.DeleteTDEMBusinessSystemRequest,
            opts: Dict = None,
    ) -> models.DeleteTDEMBusinessSystemResponse:
        """
        删除业务系统。名下存在未删除应用时返回 ResourceInUse。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTDEMBusinessSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTDEMBusinessSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTDEMDialTask(
            self,
            request: models.DeleteTDEMDialTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteTDEMDialTaskResponse:
        """
        将拨测任务标记为已删除。已删除的任务再次删除视为成功。不物理删除任务行，也不删除历史拨测结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTDEMDialTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTDEMDialTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTDEMFieldTransformRule(
            self,
            request: models.DeleteTDEMFieldTransformRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteTDEMFieldTransformRuleResponse:
        """
        按规则 Id 删除字段值替换规则。替代已废弃的 DeleteFieldTransformRule；AppId 为 string。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTDEMFieldTransformRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTDEMFieldTransformRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTDEMFunnel(
            self,
            request: models.DeleteTDEMFunnelRequest,
            opts: Dict = None,
    ) -> models.DeleteTDEMFunnelResponse:
        """
        删除漏斗
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTDEMFunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTDEMFunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWhitelist(
            self,
            request: models.DeleteWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteWhitelistResponse:
        """
        删除白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppDimensionMetrics(
            self,
            request: models.DescribeAppDimensionMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeAppDimensionMetricsResponse:
        """
        用于查询 app 监控多维分析数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppDimensionMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppDimensionMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppMetricsData(
            self,
            request: models.DescribeAppMetricsDataRequest,
            opts: Dict = None,
    ) -> models.DescribeAppMetricsDataResponse:
        """
        获取 app 监控指标数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppMetricsData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppMetricsDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppSingleCaseDetailList(
            self,
            request: models.DescribeAppSingleCaseDetailListRequest,
            opts: Dict = None,
    ) -> models.DescribeAppSingleCaseDetailListResponse:
        """
        查询 app 监控个例样本详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppSingleCaseDetailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppSingleCaseDetailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppSingleCaseList(
            self,
            request: models.DescribeAppSingleCaseListRequest,
            opts: Dict = None,
    ) -> models.DescribeAppSingleCaseListResponse:
        """
        查询 app 监控个例聚合列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppSingleCaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppSingleCaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationExitReportDetail(
            self,
            request: models.DescribeApplicationExitReportDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationExitReportDetailResponse:
        """
        获取应用退出个例上报详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationExitReportDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationExitReportDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationExitReportList(
            self,
            request: models.DescribeApplicationExitReportListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationExitReportListResponse:
        """
        获取应用退出个例上报列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationExitReportList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationExitReportListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeData(
            self,
            request: models.DescribeDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDataResponse:
        """
        转发monitor查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataBridgeUrlV2(
            self,
            request: models.DescribeDataBridgeUrlV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataBridgeUrlV2Response:
        """
        获取DescribeDataBridgeUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataBridgeUrlV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataBridgeUrlV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataCustomUrl(
            self,
            request: models.DescribeDataCustomUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataCustomUrlResponse:
        """
        获取DescribeDataCustomUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataCustomUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataCustomUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataCustomUrlV2(
            self,
            request: models.DescribeDataCustomUrlV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataCustomUrlV2Response:
        """
        获取DescribeDataCustomUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataCustomUrlV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataCustomUrlV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEventUrl(
            self,
            request: models.DescribeDataEventUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEventUrlResponse:
        """
        获取DescribeDataEventUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEventUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEventUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEventUrlV2(
            self,
            request: models.DescribeDataEventUrlV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataEventUrlV2Response:
        """
        获取DescribeDataEventUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEventUrlV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEventUrlV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFetchProject(
            self,
            request: models.DescribeDataFetchProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeDataFetchProjectResponse:
        """
        获取DescribeDataFetchProject信息。已下线，请使用DescribeDataFetchUrl
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFetchProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFetchProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFetchUrl(
            self,
            request: models.DescribeDataFetchUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataFetchUrlResponse:
        """
        获取DescribeDataFetchUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFetchUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFetchUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFetchUrlInfo(
            self,
            request: models.DescribeDataFetchUrlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataFetchUrlInfoResponse:
        """
        获取DescribeDataFetchUrlInfo信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFetchUrlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFetchUrlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFetchUrlV2(
            self,
            request: models.DescribeDataFetchUrlV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataFetchUrlV2Response:
        """
        获取DescribeDataFetchUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFetchUrlV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFetchUrlV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataLogUrlInfo(
            self,
            request: models.DescribeDataLogUrlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataLogUrlInfoResponse:
        """
        获取loginfo信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataLogUrlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataLogUrlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataLogUrlStatistics(
            self,
            request: models.DescribeDataLogUrlStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataLogUrlStatisticsResponse:
        """
        获取LogUrlStatistics信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataLogUrlStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataLogUrlStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataLogUrlStatisticsV2(
            self,
            request: models.DescribeDataLogUrlStatisticsV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataLogUrlStatisticsV2Response:
        """
        获取LogUrlStatistics信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataLogUrlStatisticsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataLogUrlStatisticsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPerformancePage(
            self,
            request: models.DescribeDataPerformancePageRequest,
            opts: Dict = None,
    ) -> models.DescribeDataPerformancePageResponse:
        """
        获取PerformancePage信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPerformancePage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPerformancePageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPerformancePageV2(
            self,
            request: models.DescribeDataPerformancePageV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataPerformancePageV2Response:
        """
        获取PerformancePage信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPerformancePageV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPerformancePageV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPvUrlInfo(
            self,
            request: models.DescribeDataPvUrlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataPvUrlInfoResponse:
        """
        获取PvUrlInfo信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPvUrlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPvUrlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPvUrlStatistics(
            self,
            request: models.DescribeDataPvUrlStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataPvUrlStatisticsResponse:
        """
        获取DescribeDataPvUrlStatistics信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPvUrlStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPvUrlStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPvUrlStatisticsV2(
            self,
            request: models.DescribeDataPvUrlStatisticsV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataPvUrlStatisticsV2Response:
        """
        获取DescribeDataPvUrlStatistics信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPvUrlStatisticsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPvUrlStatisticsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataReportCount(
            self,
            request: models.DescribeDataReportCountRequest,
            opts: Dict = None,
    ) -> models.DescribeDataReportCountResponse:
        """
        获取项目上报量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataReportCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataReportCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataReportCountV2(
            self,
            request: models.DescribeDataReportCountV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataReportCountV2Response:
        """
        获取项目上报量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataReportCountV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataReportCountV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSetUrlStatistics(
            self,
            request: models.DescribeDataSetUrlStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSetUrlStatisticsResponse:
        """
        获取DescribeDataSetUrlStatistics信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSetUrlStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSetUrlStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSetUrlStatisticsV2(
            self,
            request: models.DescribeDataSetUrlStatisticsV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataSetUrlStatisticsV2Response:
        """
        获取DescribeDataSetUrlStatistics信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSetUrlStatisticsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSetUrlStatisticsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticProject(
            self,
            request: models.DescribeDataStaticProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeDataStaticProjectResponse:
        """
        获取DescribeDataStaticProject信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticProjectV2(
            self,
            request: models.DescribeDataStaticProjectV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataStaticProjectV2Response:
        """
        获取DescribeDataStaticProject信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticProjectV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticProjectV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticResource(
            self,
            request: models.DescribeDataStaticResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDataStaticResourceResponse:
        """
        获取DescribeDataStaticResource信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticResourceV2(
            self,
            request: models.DescribeDataStaticResourceV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataStaticResourceV2Response:
        """
        获取DescribeDataStaticResource信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticResourceV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticResourceV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticUrl(
            self,
            request: models.DescribeDataStaticUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataStaticUrlResponse:
        """
        获取DescribeDataStaticUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticUrlV2(
            self,
            request: models.DescribeDataStaticUrlV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataStaticUrlV2Response:
        """
        获取DescribeDataStaticUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticUrlV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticUrlV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataWebVitalsPage(
            self,
            request: models.DescribeDataWebVitalsPageRequest,
            opts: Dict = None,
    ) -> models.DescribeDataWebVitalsPageResponse:
        """
        获取DescribeDataWebVitalsPage信息，用户核心活动信息
        页面加载性能之Web Vitals。性能关键点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataWebVitalsPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataWebVitalsPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataWebVitalsPageV2(
            self,
            request: models.DescribeDataWebVitalsPageV2Request,
            opts: Dict = None,
    ) -> models.DescribeDataWebVitalsPageV2Response:
        """
        获取DescribeDataWebVitalsPage信息，用户核心活动信息
        页面加载性能之Web Vitals。性能关键点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataWebVitalsPageV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataWebVitalsPageV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeError(
            self,
            request: models.DescribeErrorRequest,
            opts: Dict = None,
    ) -> models.DescribeErrorResponse:
        """
        获取首页错误信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeError"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeErrorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExceptionDetail(
            self,
            request: models.DescribeExceptionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeExceptionDetailResponse:
        """
        获取异常问题详情数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExceptionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExceptionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExceptionReportList(
            self,
            request: models.DescribeExceptionReportListRequest,
            opts: Dict = None,
    ) -> models.DescribeExceptionReportListResponse:
        """
        获取异常个例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExceptionReportList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExceptionReportListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFOOMMallocProblemDetail(
            self,
            request: models.DescribeFOOMMallocProblemDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeFOOMMallocProblemDetailResponse:
        """
        获取FOOM内存分配问题详情数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFOOMMallocProblemDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFOOMMallocProblemDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFOOMMallocProblemList(
            self,
            request: models.DescribeFOOMMallocProblemListRequest,
            opts: Dict = None,
    ) -> models.DescribeFOOMMallocProblemListResponse:
        """
        获取FOOM内存分配问题列表数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFOOMMallocProblemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFOOMMallocProblemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFOOMMallocReportList(
            self,
            request: models.DescribeFOOMMallocReportListRequest,
            opts: Dict = None,
    ) -> models.DescribeFOOMMallocReportListResponse:
        """
        获取FOOM内存分配问题上报列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFOOMMallocReportList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFOOMMallocReportListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFOOMProblemDetail(
            self,
            request: models.DescribeFOOMProblemDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeFOOMProblemDetailResponse:
        """
        获取FOOM问题详情数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFOOMProblemDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFOOMProblemDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFOOMProblemList(
            self,
            request: models.DescribeFOOMProblemListRequest,
            opts: Dict = None,
    ) -> models.DescribeFOOMProblemListResponse:
        """
        获取FOOM问题列表数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFOOMProblemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFOOMProblemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFOOMReportList(
            self,
            request: models.DescribeFOOMReportListRequest,
            opts: Dict = None,
    ) -> models.DescribeFOOMReportListResponse:
        """
        获取FOOM问题上报列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFOOMReportList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFOOMReportListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFieldTransformRules(
            self,
            request: models.DescribeFieldTransformRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeFieldTransformRulesResponse:
        """
        获取字段配置规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFieldTransformRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFieldTransformRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFieldValues(
            self,
            request: models.DescribeFieldValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeFieldValuesResponse:
        """
        获取TDEM字段值列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFieldValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFieldValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileCertificate(
            self,
            request: models.DescribeFileCertificateRequest,
            opts: Dict = None,
    ) -> models.DescribeFileCertificateResponse:
        """
        获取COS存储的临时密钥，具体到ProjectId
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssueAffectedUsers(
            self,
            request: models.DescribeIssueAffectedUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeIssueAffectedUsersResponse:
        """
        按用户维度聚合某问题的受影响用户清单，服务端分页。AppId 与 IssueId 必填；AppVersion / StartTime / EndTime / Keyword 用于收窄范围，同时作用于清单与 Total，因此 Total 为当前条件下去重后的用户数， 条件全空时等于问题详情的影响用户数。OrderKey / OrderBy 只改变行序、不改变结果集合；排序一律由服务端执行， 并保留 uid 作为次级键以保证翻页不重不漏。接口只读。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssueAffectedUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssueAffectedUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssueBreadcrumbs(
            self,
            request: models.DescribeIssueBreadcrumbsRequest,
            opts: Dict = None,
    ) -> models.DescribeIssueBreadcrumbsResponse:
        """
        获取指定 Issue 当前事件或最新事件之前的 Breadcrumbs 面包屑序列
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssueBreadcrumbs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssueBreadcrumbsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssueCrashLogDownloadURL(
            self,
            request: models.DescribeIssueCrashLogDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeIssueCrashLogDownloadURLResponse:
        """
        获取日志下载链接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssueCrashLogDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssueCrashLogDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssueDetail(
            self,
            request: models.DescribeIssueDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeIssueDetailResponse:
        """
        获取指定 Issue 的摘要信息以及默认选中的最新事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssueDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssueDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssueEventDetail(
            self,
            request: models.DescribeIssueEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeIssueEventDetailResponse:
        """
        获取指定 Issue 下单个事件的完整详情，包括栈信息、上下文和符号化状态等字段
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssueEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssueEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssueEvents(
            self,
            request: models.DescribeIssueEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeIssueEventsResponse:
        """
        根据条件获取指定 Issue 的错误事件列表，支持按时间范围、关键字和扩展过滤器查询，返回分页事件数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssueEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssueEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssueTrend(
            self,
            request: models.DescribeIssueTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeIssueTrendResponse:
        """
        获取指定 Issue 在给定时间范围内的趋势分桶统计数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssueTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssueTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssues(
            self,
            request: models.DescribeIssuesRequest,
            opts: Dict = None,
    ) -> models.DescribeIssuesResponse:
        """
        根据筛选条件分页查询 Issue 列表，支持环境、Issue 类型、状态、关键字、扩展过滤器和排序条件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssuesDistribution(
            self,
            request: models.DescribeIssuesDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeIssuesDistributionResponse:
        """
        获取问题分布数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssuesDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssuesDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssuesList(
            self,
            request: models.DescribeIssuesListRequest,
            opts: Dict = None,
    ) -> models.DescribeIssuesListResponse:
        """
        获取问题列表数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssuesList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssuesListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIssuesStatisticsTrend(
            self,
            request: models.DescribeIssuesStatisticsTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeIssuesStatisticsTrendResponse:
        """
        获取问题趋势数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIssuesStatisticsTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIssuesStatisticsTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLagANRProblemAccountDetail(
            self,
            request: models.DescribeLagANRProblemAccountDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeLagANRProblemAccountDetailResponse:
        """
        获取卡顿ANR问题用户详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLagANRProblemAccountDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLagANRProblemAccountDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLagANRProblemFeatureAccounts(
            self,
            request: models.DescribeLagANRProblemFeatureAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeLagANRProblemFeatureAccountsResponse:
        """
        获取卡顿ANR问题用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLagANRProblemFeatureAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLagANRProblemFeatureAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLagANRProblemList(
            self,
            request: models.DescribeLagANRProblemListRequest,
            opts: Dict = None,
    ) -> models.DescribeLagANRProblemListResponse:
        """
        获取卡顿ANR问题列表数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLagANRProblemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLagANRProblemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMiniProgramReplayPack(
            self,
            request: models.DescribeMiniProgramReplayPackRequest,
            opts: Dict = None,
    ) -> models.DescribeMiniProgramReplayPackResponse:
        """
        按AppId+BundleHash取已编译回放包正文。成功含Pack（tmpl/css/js/manifest/hash），不返回WXML/WXSS源码。不存在返回ResourceNotFound。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMiniProgramReplayPack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMiniProgramReplayPackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMiniProgramReplayPacks(
            self,
            request: models.DescribeMiniProgramReplayPacksRequest,
            opts: Dict = None,
    ) -> models.DescribeMiniProgramReplayPacksResponse:
        """
        按AppId列出回放包元数据，不含Pack正文。可按Status过滤。Limit默认20、最大100。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMiniProgramReplayPacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMiniProgramReplayPacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePerformanceMetrics(
            self,
            request: models.DescribePerformanceMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribePerformanceMetricsResponse:
        """
        获取TDEM性能指标数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePerformanceMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePerformanceMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectLimits(
            self,
            request: models.DescribeProjectLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectLimitsResponse:
        """
        获取应用上报抽样信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        获取项目列表（实例创建的团队下的项目列表）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePvList(
            self,
            request: models.DescribePvListRequest,
            opts: Dict = None,
    ) -> models.DescribePvListResponse:
        """
        获取项目下的PV列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseFileSign(
            self,
            request: models.DescribeReleaseFileSignRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseFileSignResponse:
        """
        获取上传文件存储的临时密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseFileSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseFileSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseFiles(
            self,
            request: models.DescribeReleaseFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseFilesResponse:
        """
        获取应用对应sourcemap文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplayData(
            self,
            request: models.DescribeReplayDataRequest,
            opts: Dict = None,
    ) -> models.DescribeReplayDataResponse:
        """
        从对象存储读取录屏帧数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplayData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplayDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplayDetails(
            self,
            request: models.DescribeReplayDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeReplayDetailsResponse:
        """
        获取回放日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplayDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplayDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplayMeta(
            self,
            request: models.DescribeReplayMetaRequest,
            opts: Dict = None,
    ) -> models.DescribeReplayMetaResponse:
        """
        获取回放元数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplayMeta"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplayMetaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumGroupLog(
            self,
            request: models.DescribeRumGroupLogRequest,
            opts: Dict = None,
    ) -> models.DescribeRumGroupLogResponse:
        """
        获取项目下的日志聚合信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumGroupLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumGroupLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumGroupLogV2(
            self,
            request: models.DescribeRumGroupLogV2Request,
            opts: Dict = None,
    ) -> models.DescribeRumGroupLogV2Response:
        """
        根据label 聚合分析日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumGroupLogV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumGroupLogV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogDetailsV2(
            self,
            request: models.DescribeRumLogDetailsV2Request,
            opts: Dict = None,
    ) -> models.DescribeRumLogDetailsV2Response:
        """
        查询日志明细
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogDetailsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogDetailsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogExport(
            self,
            request: models.DescribeRumLogExportRequest,
            opts: Dict = None,
    ) -> models.DescribeRumLogExportResponse:
        """
        获取项目下的日志列表（实例创建的项目下的日志列表）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogExportV2(
            self,
            request: models.DescribeRumLogExportV2Request,
            opts: Dict = None,
    ) -> models.DescribeRumLogExportV2Response:
        """
        创建日志导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogExportV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogExportV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogExports(
            self,
            request: models.DescribeRumLogExportsRequest,
            opts: Dict = None,
    ) -> models.DescribeRumLogExportsResponse:
        """
        获取项目下的日志导出列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogExports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogExportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogExportsV2(
            self,
            request: models.DescribeRumLogExportsV2Request,
            opts: Dict = None,
    ) -> models.DescribeRumLogExportsV2Response:
        """
        获取日志导出列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogExportsV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogExportsV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogList(
            self,
            request: models.DescribeRumLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeRumLogListResponse:
        """
        获取项目下的日志列表（实例创建的项目下的日志列表）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogTotalV2(
            self,
            request: models.DescribeRumLogTotalV2Request,
            opts: Dict = None,
    ) -> models.DescribeRumLogTotalV2Response:
        """
        查询原始日志总量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogTotalV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogTotalV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumStatsLogList(
            self,
            request: models.DescribeRumStatsLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeRumStatsLogListResponse:
        """
        获取项目下的日志列表，分钟级
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumStatsLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumStatsLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumStatsLogListV2(
            self,
            request: models.DescribeRumStatsLogListV2Request,
            opts: Dict = None,
    ) -> models.DescribeRumStatsLogListV2Response:
        """
        查询日志时间分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumStatsLogListV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumStatsLogListV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleRate(
            self,
            request: models.DescribeSampleRateRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleRateResponse:
        """
        获取应用的采样率
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScores(
            self,
            request: models.DescribeScoresRequest,
            opts: Dict = None,
    ) -> models.DescribeScoresResponse:
        """
        获取首页分数列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScores"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScoresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScoresV2(
            self,
            request: models.DescribeScoresV2Request,
            opts: Dict = None,
    ) -> models.DescribeScoresV2Response:
        """
        获取首页分数列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScoresV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScoresV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionList(
            self,
            request: models.DescribeSessionListRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionListResponse:
        """
        查询会话列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStruggleDistribution(
            self,
            request: models.DescribeStruggleDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeStruggleDistributionResponse:
        """
        获取挣扎事件分布数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStruggleDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStruggleDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSymbolArtifactUploadCredential(
            self,
            request: models.DescribeSymbolArtifactUploadCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeSymbolArtifactUploadCredentialResponse:
        """
        获取符号制品上传临时凭证。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSymbolArtifactUploadCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSymbolArtifactUploadCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSymbolArtifacts(
            self,
            request: models.DescribeSymbolArtifactsRequest,
            opts: Dict = None,
    ) -> models.DescribeSymbolArtifactsResponse:
        """
        分页查询指定类型的符号制品。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSymbolArtifacts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSymbolArtifactsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMApplications(
            self,
            request: models.DescribeTDEMApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMApplicationsResponse:
        """
        查询应用列表，默认仅当前用户名下有权限的应用；可按业务系统 InstanceId 筛选。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMBusinessSystems(
            self,
            request: models.DescribeTDEMBusinessSystemsRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMBusinessSystemsResponse:
        """
        查询当前用户名下业务系统列表（超管返回全部）。分页 Offset/Limit，默认 Limit=20 上限 100。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMBusinessSystems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMBusinessSystemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMDialDimensions(
            self,
            request: models.DescribeTDEMDialDimensionsRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMDialDimensionsResponse:
        """
        按一个维度拆分拨测指标。Dimension 取值说明：platform、app_version、device、net_type、operator、region、country、target_ip。target_region 不是合法值。region 对应客户端省份，country 对应国家。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMDialDimensions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMDialDimensionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMDialExecutionDetail(
            self,
            request: models.DescribeTDEMDialExecutionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMDialExecutionDetailResponse:
        """
        返回一个拨测批次的探测结果和路由追踪。Probes 的 Region、Operator 是目标 IP 归属。逐跳归属同时写在 Probes.MTR.Hops 和顶层 MTR.Hops。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMDialExecutionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMDialExecutionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMDialExecutionList(
            self,
            request: models.DescribeTDEMDialExecutionListRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMDialExecutionListResponse:
        """
        按批次返回拨测执行记录，一批次一行。TargetIps 是目标地址，TargetIpGeo 是这些地址的地区和运营商。行上的 Region 和 Operator 仍是客户端地区和运营商。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMDialExecutionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMDialExecutionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMDialOverview(
            self,
            request: models.DescribeTDEMDialOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMDialOverviewResponse:
        """
        按时间窗汇总拨测批次。一次多 IP 探测计为 1 个批次。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMDialOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMDialOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMDialTasks(
            self,
            request: models.DescribeTDEMDialTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMDialTasksResponse:
        """
        查询应用下未删除的拨测任务，包含启动范围。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMDialTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMDialTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMDialTrend(
            self,
            request: models.DescribeTDEMDialTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMDialTrendResponse:
        """
        按小时或天返回拨测趋势。Granularity 不传时按小时。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMDialTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMDialTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMEventDetail(
            self,
            request: models.DescribeTDEMEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMEventDetailResponse:
        """
        按 AppId+EventId 查询事件详情，含主表字段与可选符号化结果。Date 推荐传以命中分区；或用 StartDate+EndDate（<=2 天）。越权与不存在统一 ResourceNotFound。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMEventRank(
            self,
            request: models.DescribeTDEMEventRankRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMEventRankResponse:
        """
        错误指纹或 API/资源 URL（含按访问页、状态、标签）排行。读 tdem_events，不走主分析立方 GroupBy。Kind：error/api/resource/api_page/resource_page/api_status/api_status_top/resource_status/tag。 Kind=exception_dimension返回当前普通维度或标签值的同批完整分类计数；展开不另行取数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMEventRank"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMEventRankResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMEventSearch(
            self,
            request: models.DescribeTDEMEventSearchRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMEventSearchResponse:
        """
        数据探索事件明细分页。会话分类不得调用本接口（Category 禁止 session）。时间单位 Unix 毫秒。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMEventSearch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMEventSearchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMEventSearchSummary(
            self,
            request: models.DescribeTDEMEventSearchSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMEventSearchSummaryResponse:
        """
        同一筛选下的分类计数、访问用户、业务用户、窗口合计与分桶趋势。Category 可含 session。空窗返回 0 与空 Series。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMEventSearchSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMEventSearchSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMFieldTransformRules(
            self,
            request: models.DescribeTDEMFieldTransformRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMFieldTransformRulesResponse:
        """
        查询应用下字段值替换规则列表。替代已废弃的 DescribeFieldTransformRules；AppId 为 string。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMFieldTransformRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMFieldTransformRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMFunnelDetail(
            self,
            request: models.DescribeTDEMFunnelDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMFunnelDetailResponse:
        """
        获取漏斗详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMFunnelDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMFunnelDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMFunnelDimensions(
            self,
            request: models.DescribeTDEMFunnelDimensionsRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMFunnelDimensionsResponse:
        """
        获取漏斗分析报告维度数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMFunnelDimensions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMFunnelDimensionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMFunnelList(
            self,
            request: models.DescribeTDEMFunnelListRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMFunnelListResponse:
        """
        获取漏斗列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMFunnelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMFunnelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMFunnelReport(
            self,
            request: models.DescribeTDEMFunnelReportRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMFunnelReportResponse:
        """
        获取漏斗报告
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMFunnelReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMFunnelReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMFunnelStepSessionList(
            self,
            request: models.DescribeTDEMFunnelStepSessionListRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMFunnelStepSessionListResponse:
        """
        获取漏斗步骤会话
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMFunnelStepSessionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMFunnelStepSessionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMFunnelTrend(
            self,
            request: models.DescribeTDEMFunnelTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMFunnelTrendResponse:
        """
        获取漏斗趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMFunnelTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMFunnelTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMMetricDistribution(
            self,
            request: models.DescribeTDEMMetricDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMMetricDistributionResponse:
        """
        按单维度 GroupBy 查询分析指标分布。读 tdem_metric_agg。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMMetricDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMMetricDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMMetricSummary(
            self,
            request: models.DescribeTDEMMetricSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMMetricSummaryResponse:
        """
        查询指定应用与时间窗内的分析指标区间合计。单查返回 Metrics；传 Queries 时返回 Results。读 tdem_metric_agg。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMMetricSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMMetricSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMMetricTrend(
            self,
            request: models.DescribeTDEMMetricTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMMetricTrendResponse:
        """
        查询分析指标时序。可传 CompareStartTime/CompareEndTime 做对比窗（仅批量）。读 tdem_metric_agg。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMMetricTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMMetricTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMOverviewScores(
            self,
            request: models.DescribeTDEMOverviewScoresRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMOverviewScoresResponse:
        """
        客户端总览列表批量评分。按应用列表一次返回各计分项单项分与加权总分。AppIds 1-200；不归属当前用户的应用不出现在响应中。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMOverviewScores"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMOverviewScoresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMRelatedEvents(
            self,
            request: models.DescribeTDEMRelatedEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMRelatedEventsResponse:
        """
        会话时间线 / 页面子事件 / 错误前轨迹。Mode：timeline / page / breadcrumb。Limit 默认 200，上限 200。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMRelatedEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMRelatedEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMSSEDimensions(
            self,
            request: models.DescribeTDEMSSEDimensionsRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMSSEDimensionsResponse:
        """
        按一个维度返回大模型对话次数和当前指标值，按指标值降序，最多 200 行。region 由 country 与 province 拼接。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMSSEDimensions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMSSEDimensionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMSSEDistribution(
            self,
            request: models.DescribeTDEMSSEDistributionRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMSSEDistributionResponse:
        """
        返回吞吐率、首次消息时延或流畅度的分档分布。档位左闭右开，最后一档有限区间右端闭合，超出右端的样本进入溢出档。错误率与卡死率返回 InvalidParameter。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMSSEDistribution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMSSEDistributionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMSSEPercentile(
            self,
            request: models.DescribeTDEMSSEPercentileRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMSSEPercentileResponse:
        """
        返回吞吐率、首次消息时延或流畅度在整个时间窗及各时间桶上的平均值和 P50、P75、P95、P99。错误率与卡死率返回 InvalidParameter。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMSSEPercentile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMSSEPercentileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMSSESummary(
            self,
            request: models.DescribeTDEMSSESummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMSSESummaryResponse:
        """
        查询指定应用与时间窗内的大模型对话汇总，包含对话次数、token 总数、吞吐率、首次消息时延、错误率、卡死率和流畅度。只读 tdem.tdem_events 中 event_type 为 sse_call 的事件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMSSESummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMSSESummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMSSETrend(
            self,
            request: models.DescribeTDEMSSETrendRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMSSETrendResponse:
        """
        按时间桶返回大模型对话趋势。overall 填充 Points，其他维度按整个窗口的指标值从高到低取 TopN 并填充 Series。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMSSETrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMSSETrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMSampleConfig(
            self,
            request: models.DescribeTDEMSampleConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMSampleConfigResponse:
        """
        读取当前生效的 Web 规则化采样文档。ProjectId 必填且 > 0。无行则返回内置缺省（Event.Enabled=true、Types 空、Replay 关闭且体验率 0），不自动插库。SnapshotId 无快照为 0。query handler 做 PascalCase ↔ 存储 snake_case 映射。非 Web 应用不得走本接口，继续 DescribeSampleRate。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMSampleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMSampleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMSampleRate(
            self,
            request: models.DescribeTDEMSampleRateRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMSampleRateResponse:
        """
        查询单个应用的采集采样率与会话回放采样率。替代已废弃的 DescribeSampleRate；AppId 为 string。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMSampleRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMSampleRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMSessionReplayTimeline(
            self,
            request: models.DescribeTDEMSessionReplayTimelineRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMSessionReplayTimelineResponse:
        """
        获取回放时间线数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMSessionReplayTimeline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMSessionReplayTimelineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMUsageDetail(
            self,
            request: models.DescribeTDEMUsageDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMUsageDetailResponse:
        """
        按业务系统/应用查询用量明细（含行趋势、端类型、删除/停用标记）。Keyword 匹配业务系统名、应用名或应用 ID。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMUsageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMUsageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTDEMUsageSummary(
            self,
            request: models.DescribeTDEMUsageSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeTDEMUsageSummaryResponse:
        """
        查询当前使用者名下（超管为全部）上报总量与趋势。时间 StartTime/EndTime 为 YYYY-MM-DD HH:00:00 小时对齐。不要求请求体带 AppId。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTDEMUsageSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTDEMUsageSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTawAreas(
            self,
            request: models.DescribeTawAreasRequest,
            opts: Dict = None,
    ) -> models.DescribeTawAreasResponse:
        """
        查询片区信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTawAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTawAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTawInstances(
            self,
            request: models.DescribeTawInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeTawInstancesResponse:
        """
        查询实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTawInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTawInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeToken(
            self,
            request: models.DescribeTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenResponse:
        """
        查询令牌
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopIssues(
            self,
            request: models.DescribeTopIssuesRequest,
            opts: Dict = None,
    ) -> models.DescribeTopIssuesResponse:
        """
        查询top问题列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopIssues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopIssuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserJourneySanKey(
            self,
            request: models.DescribeUserJourneySanKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeUserJourneySanKeyResponse:
        """
        获取用户旅程数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserJourneySanKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserJourneySanKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUvList(
            self,
            request: models.DescribeUvListRequest,
            opts: Dict = None,
    ) -> models.DescribeUvListResponse:
        """
        获取项目下的UV列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhitelists(
            self,
            request: models.DescribeWhitelistsRequest,
            opts: Dict = None,
    ) -> models.DescribeWhitelistsResponse:
        """
        获取白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhitelists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhitelistsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFieldTransformRule(
            self,
            request: models.ModifyFieldTransformRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyFieldTransformRuleResponse:
        """
        修改字段配置规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFieldTransformRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFieldTransformRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        修改 RUM 业务系统
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIssueStatus(
            self,
            request: models.ModifyIssueStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyIssueStatusResponse:
        """
        更新 Issue 状态，支持 resolve、ignore、reopen 等状态流转动作
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIssueStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIssueStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMiniProgramReplayPack(
            self,
            request: models.ModifyMiniProgramReplayPackRequest,
            opts: Dict = None,
    ) -> models.ModifyMiniProgramReplayPackResponse:
        """
        更新回放包元数据，仅支持改Release，不重编译。换源码请再调UploadMiniProgramSource。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMiniProgramReplayPack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMiniProgramReplayPackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        修改 RUM 应用信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProjectLimit(
            self,
            request: models.ModifyProjectLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectLimitResponse:
        """
        新增修改限流
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProjectLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySampleRate(
            self,
            request: models.ModifySampleRateRequest,
            opts: Dict = None,
    ) -> models.ModifySampleRateResponse:
        """
        配置tdem采样率
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySampleRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySampleRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTDEMApplication(
            self,
            request: models.ModifyTDEMApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyTDEMApplicationResponse:
        """
        修改应用，仅传需修改字段。AppId 必填。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTDEMApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTDEMApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTDEMBusinessSystem(
            self,
            request: models.ModifyTDEMBusinessSystemRequest,
            opts: Dict = None,
    ) -> models.ModifyTDEMBusinessSystemResponse:
        """
        修改业务系统名称或描述。越权 UnauthorizedOperation；不存在或已删除 ResourceNotFound。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTDEMBusinessSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTDEMBusinessSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTDEMDialTask(
            self,
            request: models.ModifyTDEMDialTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyTDEMDialTaskResponse:
        """
        修改拨测任务。未出现在请求中的字段保持原值。启动范围传空字符串表示清空该项。Type 和 ExecutionTime 创建后不可修改。暂停和恢复通过 Status 完成，不提供单独的状态接口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTDEMDialTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTDEMDialTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTDEMFieldTransformRule(
            self,
            request: models.ModifyTDEMFieldTransformRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyTDEMFieldTransformRuleResponse:
        """
        按规则 Id 修改字段值替换规则。替代已废弃的 ModifyFieldTransformRule；AppId 为 string。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTDEMFieldTransformRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTDEMFieldTransformRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTDEMFunnel(
            self,
            request: models.ModifyTDEMFunnelRequest,
            opts: Dict = None,
    ) -> models.ModifyTDEMFunnelResponse:
        """
        修改漏斗
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTDEMFunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTDEMFunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTDEMSampleConfig(
            self,
            request: models.ModifyTDEMSampleConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyTDEMSampleConfigResponse:
        """
        整页保存 Web 规则化采样文档：校验 → INSERT 快照 → UPSERT 当前行 → 刷新 Redis 下发缓存。不写 tdem_sample_rate。采样率 0–100、最多两位小数；规则 Conditions 不可为空；Types 含非闭集 key 返回 InvalidParameter。校验失败不写库。无 Restore/Import/Export/Diff。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTDEMSampleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTDEMSampleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTDEMSampleRate(
            self,
            request: models.ModifyTDEMSampleRateRequest,
            opts: Dict = None,
    ) -> models.ModifyTDEMSampleRateResponse:
        """
        设置或更新应用采集采样率；ReplaySampleRate 可选。替代已废弃的 ModifySampleRate；AppId 为 string。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTDEMSampleRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTDEMSampleRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PreviewTDEMFunnelReport(
            self,
            request: models.PreviewTDEMFunnelReportRequest,
            opts: Dict = None,
    ) -> models.PreviewTDEMFunnelReportResponse:
        """
        根据步骤配置直接生成漏斗预览报告（不保存漏斗，不需要FunnelId）
        """
        
        kwargs = {}
        kwargs["action"] = "PreviewTDEMFunnelReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PreviewTDEMFunnelReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeInstance(
            self,
            request: models.ResumeInstanceRequest,
            opts: Dict = None,
    ) -> models.ResumeInstanceResponse:
        """
        恢复 RUM 业务系统，恢复后，用户可以正常使用和上报数据
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeProject(
            self,
            request: models.ResumeProjectRequest,
            opts: Dict = None,
    ) -> models.ResumeProjectResponse:
        """
        恢复应用使用与上报数据
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeTDEMApplication(
            self,
            request: models.ResumeTDEMApplicationRequest,
            opts: Dict = None,
    ) -> models.ResumeTDEMApplicationResponse:
        """
        恢复已停止的应用，Status 变为 2。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeTDEMApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeTDEMApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstance(
            self,
            request: models.StopInstanceRequest,
            opts: Dict = None,
    ) -> models.StopInstanceResponse:
        """
        停止实例
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopProject(
            self,
            request: models.StopProjectRequest,
            opts: Dict = None,
    ) -> models.StopProjectResponse:
        """
        停止项目使用与上报数据
        """
        
        kwargs = {}
        kwargs["action"] = "StopProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopTDEMApplication(
            self,
            request: models.StopTDEMApplicationRequest,
            opts: Dict = None,
    ) -> models.StopTDEMApplicationResponse:
        """
        停止应用采集，Status 变为 6。
        """
        
        kwargs = {}
        kwargs["action"] = "StopTDEMApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopTDEMApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadMiniProgramSource(
            self,
            request: models.UploadMiniProgramSourceRequest,
            opts: Dict = None,
    ) -> models.UploadMiniProgramSourceResponse:
        """
        上传微信小程序源码zip并同步编译回放包。控制台传FileBase64；zip需含app.json，跳过node_modules。同AppId+BundleHash且已ready则幂等。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadMiniProgramSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadMiniProgramSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadSymbolArtifact(
            self,
            request: models.UploadSymbolArtifactRequest,
            opts: Dict = None,
    ) -> models.UploadSymbolArtifactResponse:
        """
        登记已上传的符号制品。请先获取上传凭证并将文件上传到 COS。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadSymbolArtifact"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadSymbolArtifactResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)