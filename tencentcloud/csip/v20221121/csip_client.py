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
from tencentcloud.csip.v20221121 import models


class CsipClient(AbstractClient):
    _apiVersion = '2022-11-21'
    _endpoint = 'csip.tencentcloudapi.com'
    _service = 'csip'


    def AddNewBindRoleUser(self, request):
        r"""csip角色授权绑定接口

        :param request: Request instance for AddNewBindRoleUser.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddNewBindRoleUserRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddNewBindRoleUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNewBindRoleUser", params, headers=headers)
            response = json.loads(body)
            model = models.AddNewBindRoleUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccessKeyCheckTask(self, request):
        r"""检测AK 异步任务

        :param request: Request instance for CreateAccessKeyCheckTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAccessKeyCheckTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAccessKeyCheckTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccessKeyCheckTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccessKeyCheckTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccessKeySyncTask(self, request):
        r"""发起AK资产同步任务

        :param request: Request instance for CreateAccessKeySyncTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAccessKeySyncTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAccessKeySyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccessKeySyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccessKeySyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainAndIp(self, request):
        r"""创建域名、ip相关信息

        :param request: Request instance for CreateDomainAndIp.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDomainAndIpRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDomainAndIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainAndIp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainAndIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRiskCenterScanTask(self, request):
        r"""创建风险中心扫描任务

        :param request: Request instance for CreateRiskCenterScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateRiskCenterScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateRiskCenterScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRiskCenterScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRiskCenterScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomainAndIp(self, request):
        r"""删除域名和ip请求

        :param request: Request instance for DeleteDomainAndIp.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDomainAndIpRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDomainAndIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainAndIp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainAndIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRiskScanTask(self, request):
        r"""删除风险中心扫描任务

        :param request: Request instance for DeleteRiskScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteRiskScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteRiskScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRiskScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbnormalCallRecord(self, request):
        r"""获取调用记录列表

        :param request: Request instance for DescribeAbnormalCallRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAbnormalCallRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAbnormalCallRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalCallRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbnormalCallRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyAlarm(self, request):
        r"""访问密钥告警记录列表

        :param request: Request instance for DescribeAccessKeyAlarm.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAlarmRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyAlarmDetail(self, request):
        r"""访问密钥告警记录详情

        :param request: Request instance for DescribeAccessKeyAlarmDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAlarmDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAlarmDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyAlarmDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyAlarmDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyAsset(self, request):
        r"""获取用户访问密钥资产列表

        :param request: Request instance for DescribeAccessKeyAsset.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAssetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyRisk(self, request):
        r"""访问密钥风险记录列表

        :param request: Request instance for DescribeAccessKeyRisk.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyRiskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyRisk", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyRiskDetail(self, request):
        r"""访问密钥风险记录详情

        :param request: Request instance for DescribeAccessKeyRiskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyRiskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyRiskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyRiskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyRiskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyUserDetail(self, request):
        r"""查询用户的账号详情

        :param request: Request instance for DescribeAccessKeyUserDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyUserDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyUserDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyUserDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyUserDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyUserList(self, request):
        r"""查询用户的账号列表

        :param request: Request instance for DescribeAccessKeyUserList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyUserListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlertList(self, request):
        r"""告警中心全量告警列表接口

        :param request: Request instance for DescribeAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetProcessList(self, request):
        r"""查询云边界分析-暴露路径下主机节点的进程列表

        :param request: Request instance for DescribeAssetProcessList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetProcessListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetRiskList(self, request):
        r"""资产视角下云资源配置风险列表

        :param request: Request instance for DescribeAssetRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetViewVulRiskList(self, request):
        r"""获取资产视角的漏洞风险列表

        :param request: Request instance for DescribeAssetViewVulRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetViewVulRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetViewVulRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetViewVulRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetViewVulRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCFWAssetStatistics(self, request):
        r"""云防资产中心统计数据

        :param request: Request instance for DescribeCFWAssetStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCFWAssetStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCFWAssetStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCFWAssetStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCFWAssetStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSIPRiskStatistics(self, request):
        r"""获取风险中心风险概况示例

        :param request: Request instance for DescribeCSIPRiskStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPRiskStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPRiskStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSIPRiskStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSIPRiskStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCVMAssetInfo(self, request):
        r"""cvm详情

        :param request: Request instance for DescribeCVMAssetInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCVMAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCVMAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCVMAssets(self, request):
        r"""获取cvm列表

        :param request: Request instance for DescribeCVMAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCVMAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCVMAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCallRecord(self, request):
        r"""获取调用记录列表

        :param request: Request instance for DescribeCallRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCallRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCallRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCallRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCallRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCheckViewRisks(self, request):
        r"""检查视角下云资源配置风险列表示例

        :param request: Request instance for DescribeCheckViewRisks.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCheckViewRisksRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCheckViewRisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCheckViewRisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCheckViewRisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterAssets(self, request):
        r"""集群列表

        :param request: Request instance for DescribeClusterAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterPodAssets(self, request):
        r"""集群pod列表

        :param request: Request instance for DescribeClusterPodAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPodAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPodAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigCheckRules(self, request):
        r"""云资源配置风险规则列表示例

        :param request: Request instance for DescribeConfigCheckRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeConfigCheckRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeConfigCheckRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigCheckRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigCheckRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDbAssetInfo(self, request):
        r"""db资产详情

        :param request: Request instance for DescribeDbAssetInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDbAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDbAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDbAssets(self, request):
        r"""数据库资产列表

        :param request: Request instance for DescribeDbAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDbAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDbAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainAssets(self, request):
        r"""域名列表

        :param request: Request instance for DescribeDomainAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDomainAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDomainAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposeAssetCategory(self, request):
        r"""云边界分析资产分类

        :param request: Request instance for DescribeExposeAssetCategory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposeAssetCategoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposeAssetCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposeAssetCategory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposeAssetCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposePath(self, request):
        r"""查询云边界分析路径节点

        :param request: Request instance for DescribeExposePath.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposePathRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposePath", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposures(self, request):
        r"""云边界分析资产列表

        :param request: Request instance for DescribeExposures.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposuresRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposuresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposures", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposuresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayAssets(self, request):
        r"""获取网关列表

        :param request: Request instance for DescribeGatewayAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeGatewayAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeGatewayAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHighBaseLineRiskList(self, request):
        r"""查询云边界分析-暴露路径下主机节点的高危基线风险列表

        :param request: Request instance for DescribeHighBaseLineRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeHighBaseLineRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeHighBaseLineRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHighBaseLineRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHighBaseLineRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerList(self, request):
        r"""查询clb监听器列表

        :param request: Request instance for DescribeListenerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeListenerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeListenerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNICAssets(self, request):
        r"""获取网卡列表

        :param request: Request instance for DescribeNICAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNICAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNICAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNICAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNICAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationInfo(self, request):
        r"""查询集团账号详情

        :param request: Request instance for DescribeOrganizationInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeOrganizationInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeOrganizationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationUserInfo(self, request):
        r"""查询集团账号用户列表

        :param request: Request instance for DescribeOrganizationUserInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeOrganizationUserInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeOrganizationUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOtherCloudAssets(self, request):
        r"""资产列表

        :param request: Request instance for DescribeOtherCloudAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeOtherCloudAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeOtherCloudAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOtherCloudAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOtherCloudAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicIpAssets(self, request):
        r"""ip公网列表

        :param request: Request instance for DescribePublicIpAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePublicIpAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePublicIpAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicIpAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicIpAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRepositoryImageAssets(self, request):
        r"""仓库镜像列表

        :param request: Request instance for DescribeRepositoryImageAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRepositoryImageAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRepositoryImageAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRepositoryImageAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRepositoryImageAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCallRecord(self, request):
        r"""获取风险调用记录列表

        :param request: Request instance for DescribeRiskCallRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCallRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCallRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCallRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCallRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewCFGRiskList(self, request):
        r"""获取资产视角的配置风险列表

        :param request: Request instance for DescribeRiskCenterAssetViewCFGRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewCFGRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewCFGRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewCFGRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewCFGRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewPortRiskList(self, request):
        r"""获取资产视角的端口风险列表

        :param request: Request instance for DescribeRiskCenterAssetViewPortRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewPortRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewPortRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewPortRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewPortRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewVULRiskList(self, request):
        r"""获取资产视角的漏洞风险列表

        :param request: Request instance for DescribeRiskCenterAssetViewVULRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewVULRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewVULRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewVULRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewVULRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewWeakPasswordRiskList(self, request):
        r"""获取资产视角的弱口令风险列表

        :param request: Request instance for DescribeRiskCenterAssetViewWeakPasswordRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewWeakPasswordRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewWeakPasswordRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewWeakPasswordRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewWeakPasswordRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterCFGViewCFGRiskList(self, request):
        r"""获取配置视角的配置风险列表

        :param request: Request instance for DescribeRiskCenterCFGViewCFGRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterCFGViewCFGRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterCFGViewCFGRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterCFGViewCFGRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterCFGViewCFGRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterPortViewPortRiskList(self, request):
        r"""获取端口视角的端口风险列表

        :param request: Request instance for DescribeRiskCenterPortViewPortRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterPortViewPortRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterPortViewPortRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterPortViewPortRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterPortViewPortRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterServerRiskList(self, request):
        r"""获取风险服务列表

        :param request: Request instance for DescribeRiskCenterServerRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterServerRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterServerRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterServerRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterServerRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterVULViewVULRiskList(self, request):
        r"""获取漏洞视角的漏洞风险列表

        :param request: Request instance for DescribeRiskCenterVULViewVULRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterVULViewVULRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterVULViewVULRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterVULViewVULRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterVULViewVULRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterWebsiteRiskList(self, request):
        r"""获取内容风险列表

        :param request: Request instance for DescribeRiskCenterWebsiteRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterWebsiteRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterWebsiteRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterWebsiteRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterWebsiteRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDetailList(self, request):
        r"""风险详情列表示例

        :param request: Request instance for DescribeRiskDetailList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskDetailListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskDetailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDetailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDetailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskRuleDetail(self, request):
        r"""查询风险规则详情示例

        :param request: Request instance for DescribeRiskRuleDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskRuleDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskRules(self, request):
        r"""高级配置风险规则列表示例

        :param request: Request instance for DescribeRiskRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanReportList(self, request):
        r"""获取扫描报告列表

        :param request: Request instance for DescribeScanReportList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScanReportListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScanReportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanReportList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanReportListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanStatistic(self, request):
        r"""查询云边界分析扫描结果统计信息

        :param request: Request instance for DescribeScanStatistic.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScanStatisticRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScanStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanTaskList(self, request):
        r"""获取扫描任务列表

        :param request: Request instance for DescribeScanTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScanTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchBugInfo(self, request):
        r"""立体防护中心查询漏洞信息

        :param request: Request instance for DescribeSearchBugInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSearchBugInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSearchBugInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchBugInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchBugInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSourceIPAsset(self, request):
        r"""获取用户访问密钥资产列表（源IP视角）

        :param request: Request instance for DescribeSourceIPAsset.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSourceIPAssetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSourceIPAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSourceIPAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSourceIPAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubUserInfo(self, request):
        r"""查询集团的子账号列表

        :param request: Request instance for DescribeSubUserInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSubUserInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSubUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnetAssets(self, request):
        r"""获取子网列表

        :param request: Request instance for DescribeSubnetAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSubnetAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSubnetAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnetAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLogList(self, request):
        r"""获取任务扫描报告列表

        :param request: Request instance for DescribeTaskLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLogURL(self, request):
        r"""获取报告下载的临时链接

        :param request: Request instance for DescribeTaskLogURL.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogURLRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLogURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLogURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopAttackInfo(self, request):
        r"""查询TOP攻击信息

        :param request: Request instance for DescribeTopAttackInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTopAttackInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTopAttackInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopAttackInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopAttackInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUebaRule(self, request):
        r"""查询用户行为分析策略列表

        :param request: Request instance for DescribeUebaRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUebaRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUebaRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUebaRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUebaRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCallRecord(self, request):
        r"""获取账号调用记录列表

        :param request: Request instance for DescribeUserCallRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUserCallRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUserCallRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCallRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserCallRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVULList(self, request):
        r"""新安全中心风险中心-漏洞列表

        :param request: Request instance for DescribeVULList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVULListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVULListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVULList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVULListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVULRiskAdvanceCFGList(self, request):
        r"""查询漏洞风险高级配置

        :param request: Request instance for DescribeVULRiskAdvanceCFGList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVULRiskAdvanceCFGListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVULRiskAdvanceCFGListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVULRiskAdvanceCFGList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVULRiskAdvanceCFGListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVULRiskDetail(self, request):
        r"""获取漏洞展开详情

        :param request: Request instance for DescribeVULRiskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVULRiskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVULRiskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVULRiskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVULRiskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcAssets(self, request):
        r"""获取vpc列表

        :param request: Request instance for DescribeVpcAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVpcAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVpcAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulRiskList(self, request):
        r"""查询云边界分析-暴露路径下主机节点的漏洞列表

        :param request: Request instance for DescribeVulRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulViewVulRiskList(self, request):
        r"""获取漏洞视角的漏洞风险列表

        :param request: Request instance for DescribeVulViewVulRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulViewVulRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulViewVulRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulViewVulRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulViewVulRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOrganizationAccountStatus(self, request):
        r"""修改集团账号状态

        :param request: Request instance for ModifyOrganizationAccountStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyOrganizationAccountStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyOrganizationAccountStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOrganizationAccountStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOrganizationAccountStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskCenterRiskStatus(self, request):
        r"""修改风险中心风险状态

        :param request: Request instance for ModifyRiskCenterRiskStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyRiskCenterRiskStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyRiskCenterRiskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskCenterRiskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskCenterRiskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskCenterScanTask(self, request):
        r"""修改风险中心扫描任务

        :param request: Request instance for ModifyRiskCenterScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyRiskCenterScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyRiskCenterScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskCenterScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskCenterScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUebaRuleSwitch(self, request):
        r"""更新自定义策略的开关

        :param request: Request instance for ModifyUebaRuleSwitch.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyUebaRuleSwitchRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyUebaRuleSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUebaRuleSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUebaRuleSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopRiskCenterTask(self, request):
        r"""停止扫风险中心扫描任务

        :param request: Request instance for StopRiskCenterTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopRiskCenterTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopRiskCenterTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopRiskCenterTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopRiskCenterTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAccessKeyAlarmStatus(self, request):
        r"""标记风险或者告警为 已处置/已忽略

        :param request: Request instance for UpdateAccessKeyAlarmStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.UpdateAccessKeyAlarmStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UpdateAccessKeyAlarmStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAccessKeyAlarmStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAccessKeyAlarmStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAccessKeyRemark(self, request):
        r"""编辑访问密钥/源IP备注

        :param request: Request instance for UpdateAccessKeyRemark.
        :type request: :class:`tencentcloud.csip.v20221121.models.UpdateAccessKeyRemarkRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UpdateAccessKeyRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAccessKeyRemark", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAccessKeyRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAlertStatusList(self, request):
        r"""批量告警状态处理接口

        :param request: Request instance for UpdateAlertStatusList.
        :type request: :class:`tencentcloud.csip.v20221121.models.UpdateAlertStatusListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UpdateAlertStatusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlertStatusList", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAlertStatusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))