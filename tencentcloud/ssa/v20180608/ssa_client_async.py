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
from tencentcloud.ssa.v20180608 import models
from typing import Dict


class SsaClient(AbstractClient):
    _apiVersion = '2018-06-08'
    _endpoint = 'ssa.tencentcloudapi.com'
    _service = 'ssa'

    async def DescribeAlarmStat(
            self,
            request: models.DescribeAlarmStatRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmStatResponse:
        """
        安全大屏-用户威胁告警信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDetail(
            self,
            request: models.DescribeAssetDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDetailResponse:
        """
        资产安全页资产详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDetailList(
            self,
            request: models.DescribeAssetDetailListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDetailListResponse:
        """
        资产条件查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDetailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDetailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetList(
            self,
            request: models.DescribeAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetListResponse:
        """
        资产安全资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckConfigAssetList(
            self,
            request: models.DescribeCheckConfigAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckConfigAssetListResponse:
        """
        云安全配置管理资产组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckConfigAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckConfigAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckConfigDetail(
            self,
            request: models.DescribeCheckConfigDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckConfigDetailResponse:
        """
        云安全配置检查项详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckConfigDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckConfigDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceAssetList(
            self,
            request: models.DescribeComplianceAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceAssetListResponse:
        """
        合规管理-资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceDetail(
            self,
            request: models.DescribeComplianceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceDetailResponse:
        """
        合规管理检查项详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceList(
            self,
            request: models.DescribeComplianceListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceListResponse:
        """
        合规管理总览页检查项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigList(
            self,
            request: models.DescribeConfigListRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigListResponse:
        """
        云配置检查项总览页检查项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainList(
            self,
            request: models.DescribeDomainListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainListResponse:
        """
        域名列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventDetail(
            self,
            request: models.DescribeEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeEventDetailResponse:
        """
        获取安全事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLeakDetectionList(
            self,
            request: models.DescribeLeakDetectionListRequest,
            opts: Dict = None,
    ) -> models.DescribeLeakDetectionListResponse:
        """
        获取泄露列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLeakDetectionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLeakDetectionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMappingResults(
            self,
            request: models.DescribeMappingResultsRequest,
            opts: Dict = None,
    ) -> models.DescribeMappingResultsResponse:
        """
        获取测绘列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMappingResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMappingResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSocAlertDetails(
            self,
            request: models.DescribeSocAlertDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeSocAlertDetailsResponse:
        """
        返回告警详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSocAlertDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSocAlertDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSocAlertList(
            self,
            request: models.DescribeSocAlertListRequest,
            opts: Dict = None,
    ) -> models.DescribeSocAlertListResponse:
        """
        拉取告警列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSocAlertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSocAlertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSocCheckItemList(
            self,
            request: models.DescribeSocCheckItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeSocCheckItemListResponse:
        """
        云安全配置检查项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSocCheckItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSocCheckItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSocCheckResultList(
            self,
            request: models.DescribeSocCheckResultListRequest,
            opts: Dict = None,
    ) -> models.DescribeSocCheckResultListResponse:
        """
        云安全配置检查项结果列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSocCheckResultList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSocCheckResultListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSocCspmCompliance(
            self,
            request: models.DescribeSocCspmComplianceRequest,
            opts: Dict = None,
    ) -> models.DescribeSocCspmComplianceResponse:
        """
        合规详情项
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSocCspmCompliance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSocCspmComplianceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDetail(
            self,
            request: models.DescribeVulDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDetailResponse:
        """
        漏洞列表页，获取漏洞详情信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulList(
            self,
            request: models.DescribeVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulListResponse:
        """
        漏洞管理页，获取漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SaDivulgeScanRuleMutate(
            self,
            request: models.SaDivulgeScanRuleMutateRequest,
            opts: Dict = None,
    ) -> models.SaDivulgeScanRuleMutateResponse:
        """
        SaDivulgeScanRuleMutate
        """
        
        kwargs = {}
        kwargs["action"] = "SaDivulgeScanRuleMutate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SaDivulgeScanRuleMutateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SaEventPub(
            self,
            request: models.SaEventPubRequest,
            opts: Dict = None,
    ) -> models.SaEventPubResponse:
        """
        安全事件通用字段
        """
        
        kwargs = {}
        kwargs["action"] = "SaEventPub"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SaEventPubResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)