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