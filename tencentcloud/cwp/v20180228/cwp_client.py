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
from tencentcloud.cwp.v20180228 import models


class CwpClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'cwp.tencentcloudapi.com'
    _service = 'cwp'


    def AddLoginWhiteLists(self, request):
        r"""批量添加异地登录白名单

        :param request: Request instance for AddLoginWhiteLists.
        :type request: :class:`tencentcloud.cwp.v20180228.models.AddLoginWhiteListsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.AddLoginWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLoginWhiteLists", params, headers=headers)
            response = json.loads(body)
            model = models.AddLoginWhiteListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelIgnoreVul(self, request):
        r"""产品变动切换到了\\n切换到 AddVulIgnoreRule / ModifyVulIgnoreRule  CancelVulIgnoreRule\\n相关接口

        取消漏洞忽略

        :param request: Request instance for CancelIgnoreVul.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CancelIgnoreVulRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CancelIgnoreVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelIgnoreVul", params, headers=headers)
            response = json.loads(body)
            model = models.CancelIgnoreVulResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeRuleEventsIgnoreStatus(self, request):
        r"""根据检测项id或事件id批量忽略事件或取消忽略

        :param request: Request instance for ChangeRuleEventsIgnoreStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ChangeRuleEventsIgnoreStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ChangeRuleEventsIgnoreStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeRuleEventsIgnoreStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeRuleEventsIgnoreStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeStrategyEnableStatus(self, request):
        r"""根据策略id修改策略可用状态

        :param request: Request instance for ChangeStrategyEnableStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ChangeStrategyEnableStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ChangeStrategyEnableStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeStrategyEnableStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeStrategyEnableStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckBashPolicyParams(self, request):
        r"""校验高危命令用户规则新增和编辑时的参数。

        :param request: Request instance for CheckBashPolicyParams.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckBashPolicyParamsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckBashPolicyParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBashPolicyParams", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBashPolicyParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckBashRuleParams(self, request):
        r"""校验高危命令用户规则新增和编辑时的参数。

        :param request: Request instance for CheckBashRuleParams.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckBashRuleParamsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckBashRuleParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBashRuleParams", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBashRuleParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckFileTamperRule(self, request):
        r"""检验核心文件监控前端新增和编辑时的规则参数。

        :param request: Request instance for CheckFileTamperRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckFileTamperRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckFileTamperRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFileTamperRule", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFileTamperRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckFirstScanBaseline(self, request):
        r"""查询基线是否第一次检测

        :param request: Request instance for CheckFirstScanBaseline.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckFirstScanBaselineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckFirstScanBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFirstScanBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFirstScanBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckLogKafkaConnectionState(self, request):
        r"""检查日志投递kafka连通性

        :param request: Request instance for CheckLogKafkaConnectionState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckLogKafkaConnectionStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckLogKafkaConnectionStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckLogKafkaConnectionState", params, headers=headers)
            response = json.loads(body)
            model = models.CheckLogKafkaConnectionStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearLocalStorage(self, request):
        r"""清理本地存储数据

        :param request: Request instance for ClearLocalStorage.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ClearLocalStorageRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ClearLocalStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearLocalStorage", params, headers=headers)
            response = json.loads(body)
            model = models.ClearLocalStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBanWhiteList(self, request):
        r"""添加阻断白名单列表

        :param request: Request instance for CreateBanWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateBanWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateBanWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBanWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBanWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaselineStrategy(self, request):
        r"""根据策略信息创建基线策略

        :param request: Request instance for CreateBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaselineStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBuyBindTask(self, request):
        r"""新购授权自动绑定任务

        :param request: Request instance for CreateBuyBindTask.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateBuyBindTaskRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateBuyBindTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBuyBindTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBuyBindTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmergencyVulScan(self, request):
        r"""创建应急漏洞扫描任务

        :param request: Request instance for CreateEmergencyVulScan.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateEmergencyVulScanRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateEmergencyVulScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmergencyVulScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmergencyVulScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIncidentBacktracking(self, request):
        r"""对旗舰版机器单次触发事件调查及告警回溯

        :param request: Request instance for CreateIncidentBacktracking.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateIncidentBacktrackingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateIncidentBacktrackingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIncidentBacktracking", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIncidentBacktrackingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLicenseOrder(self, request):
        r"""CreateLicenseOrder 该接口可以创建专业版/旗舰版订单
        支持预付费后付费创建
        后付费订单直接创建成功
        预付费订单仅下单不支付,需要调用计费支付接口进行支付

        :param request: Request instance for CreateLicenseOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateLicenseOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateLicenseOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLicenseOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLicenseOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLogExport(self, request):
        r"""创建日志下载任务

        :param request: Request instance for CreateLogExport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateLogExportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateLogExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogExport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLogExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMaliciousRequestWhiteList(self, request):
        r"""添加恶意请求白名单

        :param request: Request instance for CreateMaliciousRequestWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateMaliciousRequestWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateMaliciousRequestWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMaliciousRequestWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMaliciousRequestWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMalwareWhiteList(self, request):
        r"""创建木马白名单

        :param request: Request instance for CreateMalwareWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateMalwareWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateMalwareWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMalwareWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMalwareWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetAttackWhiteList(self, request):
        r"""创建网络攻击白名单

        :param request: Request instance for CreateNetAttackWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateNetAttackWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateNetAttackWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetAttackWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetAttackWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProtectServer(self, request):
        r"""添加网站防护服务器

        :param request: Request instance for CreateProtectServer.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateProtectServerRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateProtectServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProtectServer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProtectServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRansomDefenseStrategy(self, request):
        r"""创建或修改防勒索策略

        :param request: Request instance for CreateRansomDefenseStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateRansomDefenseStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateRansomDefenseStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRansomDefenseStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRansomDefenseStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScanMalwareSetting(self, request):
        r"""该接口可以对入侵检测-文件查杀扫描检测

        :param request: Request instance for CreateScanMalwareSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateScanMalwareSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateScanMalwareSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScanMalwareSetting", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScanMalwareSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSearchLog(self, request):
        r"""添加历史搜索记录

        :param request: Request instance for CreateSearchLog.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateSearchLogRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateSearchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSearchLog", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSearchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSearchTemplate(self, request):
        r"""添加检索模板

        :param request: Request instance for CreateSearchTemplate.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateSearchTemplateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateSearchTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSearchTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSearchTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulFix(self, request):
        r"""提交漏洞修护

        :param request: Request instance for CreateVulFix.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateVulFixRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateVulFixResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulFix", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulFixResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWhiteListOrder(self, request):
        r"""该接口可以创建白名单订单

        :param request: Request instance for CreateWhiteListOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateWhiteListOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateWhiteListOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWhiteListOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWhiteListOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAllJavaMemShells(self, request):
        r"""删除全部java内存马事件

        :param request: Request instance for DeleteAllJavaMemShells.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteAllJavaMemShellsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteAllJavaMemShellsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAllJavaMemShells", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAllJavaMemShellsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBanWhiteList(self, request):
        r"""删除阻断白名单列表

        :param request: Request instance for DeleteBanWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBanWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBanWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBanWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBanWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselinePolicy(self, request):
        r"""删除基线策略配置

        :param request: Request instance for DeleteBaselinePolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineRule(self, request):
        r"""删除基线规则

        :param request: Request instance for DeleteBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineRuleIgnore(self, request):
        r"""删除基线忽略规则

        :param request: Request instance for DeleteBaselineRuleIgnore.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineRuleIgnoreRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineRuleIgnoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineRuleIgnore", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineRuleIgnoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineStrategy(self, request):
        r"""根据基线策略id删除策略

        :param request: Request instance for DeleteBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineWeakPassword(self, request):
        r"""删除基线弱口令

        :param request: Request instance for DeleteBaselineWeakPassword.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineWeakPasswordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineWeakPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineWeakPassword", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineWeakPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBashEvents(self, request):
        r"""根据Ids删除高危命令事件

        :param request: Request instance for DeleteBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBashPolicies(self, request):
        r"""删除高危命令策略

        :param request: Request instance for DeleteBashPolicies.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBashPoliciesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBashPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBashPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBashPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBashRules(self, request):
        r"""删除高危命令规则

        :param request: Request instance for DeleteBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBruteAttacks(self, request):
        r"""本接口 (DeleteBruteAttacks) 用于删除暴力破解记录。

        :param request: Request instance for DeleteBruteAttacks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBruteAttacksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLicenseRecord(self, request):
        r"""对授权管理-订单列表内已过期的订单进行删除.(删除后的订单不在统计范畴内)

        :param request: Request instance for DeleteLicenseRecord.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLicenseRecordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLicenseRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLicenseRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLicenseRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLicenseRecordAll(self, request):
        r"""删除授权全部记录

        :param request: Request instance for DeleteLicenseRecordAll.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLicenseRecordAllRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLicenseRecordAllResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLicenseRecordAll", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLicenseRecordAllResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLogExport(self, request):
        r"""删除日志下载任务

        :param request: Request instance for DeleteLogExport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLogExportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLogExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogExport", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoginWhiteList(self, request):
        r"""本接口用于删除异地登录白名单规则。

        :param request: Request instance for DeleteLoginWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachine(self, request):
        r"""本接口（DeleteMachine）用于卸载主机安全客户端。

        :param request: Request instance for DeleteMachine.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachineClearHistory(self, request):
        r"""删除机器清理记录

        :param request: Request instance for DeleteMachineClearHistory.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineClearHistoryRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineClearHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineClearHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineClearHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachineTag(self, request):
        r"""删除服务器关联的标签

        :param request: Request instance for DeleteMachineTag.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineTagRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMaliciousRequestWhiteList(self, request):
        r"""删除恶意请求白名单

        :param request: Request instance for DeleteMaliciousRequestWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMaliciousRequestWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMaliciousRequestWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMaliciousRequests(self, request):
        r"""本接口 (DeleteMaliciousRequests) 用于删除恶意请求记录。

        :param request: Request instance for DeleteMaliciousRequests.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMalwareScanTask(self, request):
        r"""入侵管理-终止扫描任务

        :param request: Request instance for DeleteMalwareScanTask.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwareScanTaskRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwareScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMalwareScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMalwareScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMalwareWhiteList(self, request):
        r"""删除木马白名单

        :param request: Request instance for DeleteMalwareWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwareWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwareWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMalwareWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMalwareWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMalwares(self, request):
        r"""本接口 (DeleteMalwares) 用于删除木马记录。

        :param request: Request instance for DeleteMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetAttackWhiteList(self, request):
        r"""删除网络攻击白名单

        :param request: Request instance for DeleteNetAttackWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteNetAttackWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteNetAttackWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetAttackWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetAttackWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNonlocalLoginPlaces(self, request):
        r"""本接口 (DeleteNonlocalLoginPlaces) 用于删除异地登录记录。

        :param request: Request instance for DeleteNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivilegeEvents(self, request):
        r"""根据Ids删除本地提权

        :param request: Request instance for DeletePrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivilegeRules(self, request):
        r"""删除本地提权规则

        :param request: Request instance for DeletePrivilegeRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivilegeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivilegeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProtectDir(self, request):
        r"""删除防护网站

        :param request: Request instance for DeleteProtectDir.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteProtectDirRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteProtectDirResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProtectDir", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProtectDirResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRaspRules(self, request):
        r"""删除漏洞防御白名单

        :param request: Request instance for DeleteRaspRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteRaspRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteRaspRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRaspRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRaspRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReverseShellEvents(self, request):
        r"""根据Ids删除反弹Shell事件

        :param request: Request instance for DeleteReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReverseShellRules(self, request):
        r"""删除反弹Shell规则

        :param request: Request instance for DeleteReverseShellRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReverseShellRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRiskDnsEvent(self, request):
        r"""删除恶意请求事件

        :param request: Request instance for DeleteRiskDnsEvent.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteRiskDnsEventRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteRiskDnsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskDnsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRiskDnsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRiskDnsPolicy(self, request):
        r"""删除恶意请求策略

        :param request: Request instance for DeleteRiskDnsPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteRiskDnsPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteRiskDnsPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskDnsPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRiskDnsPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScanTask(self, request):
        r"""DeleteScanTask 该接口可以对指定类型的扫描任务进行停止扫描;

        :param request: Request instance for DeleteScanTask.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteScanTaskRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSearchTemplate(self, request):
        r"""删除检索模板

        :param request: Request instance for DeleteSearchTemplate.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteSearchTemplateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteSearchTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSearchTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSearchTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTags(self, request):
        r"""删除标签

        :param request: Request instance for DeleteTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTags", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebHookPolicy(self, request):
        r"""删除告警策略

        :param request: Request instance for DeleteWebHookPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebHookPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebHookPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebHookReceiver(self, request):
        r"""删除告警接收人

        :param request: Request instance for DeleteWebHookReceiver.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookReceiverRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebHookReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebHookReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebHookRule(self, request):
        r"""删除企微机器人规则

        :param request: Request instance for DeleteWebHookRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteWebHookRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebHookRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebHookRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebPageEventLog(self, request):
        r"""网站防篡改-删除事件记录

        :param request: Request instance for DeleteWebPageEventLog.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteWebPageEventLogRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteWebPageEventLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebPageEventLog", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebPageEventLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeABTestConfig(self, request):
        r"""获取用户当前灰度配置

        :param request: Request instance for DescribeABTestConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeABTestConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeABTestConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeABTestConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeABTestConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAESKey(self, request):
        r"""获取配置的aeskey和aesiv

        :param request: Request instance for DescribeAESKey.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAESKeyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAESKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAESKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAESKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountStatistics(self, request):
        r"""本接口 (DescribeAccountStatistics) 用于获取账号统计列表数据。

        :param request: Request instance for DescribeAccountStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAccountStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAccountStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentInstallCommand(self, request):
        r"""获取agent安装命令

        :param request: Request instance for DescribeAgentInstallCommand.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAgentInstallCommandRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAgentInstallCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentInstallCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentInstallCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentInstallationToken(self, request):
        r"""混合云安装agent token获取

        :param request: Request instance for DescribeAgentInstallationToken.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAgentInstallationTokenRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAgentInstallationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentInstallationToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentInstallationTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmIncidentNodes(self, request):
        r"""获取告警点所在事件的所有节点信息

        :param request: Request instance for DescribeAlarmIncidentNodes.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmIncidentNodesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmIncidentNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmIncidentNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmIncidentNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmVertexId(self, request):
        r"""查询告警点id列表

        :param request: Request instance for DescribeAlarmVertexId.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmVertexIdRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmVertexIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmVertexId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmVertexIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetAppCount(self, request):
        r"""获取所有软件应用数量

        :param request: Request instance for DescribeAssetAppCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetAppCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetAppCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetAppList(self, request):
        r"""查询应用列表

        :param request: Request instance for DescribeAssetAppList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetAppList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetAppProcessList(self, request):
        r"""获取软件关联进程列表

        :param request: Request instance for DescribeAssetAppProcessList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppProcessListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetAppProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetAppProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetCoreModuleInfo(self, request):
        r"""获取内核模块详情

        :param request: Request instance for DescribeAssetCoreModuleInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetCoreModuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetCoreModuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetCoreModuleList(self, request):
        r"""查询资产管理内核模块列表

        :param request: Request instance for DescribeAssetCoreModuleList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetCoreModuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetCoreModuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDatabaseCount(self, request):
        r"""获取所有数据库数量

        :param request: Request instance for DescribeAssetDatabaseCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDatabaseCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDatabaseCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDatabaseInfo(self, request):
        r"""获取资产管理数据库详情

        :param request: Request instance for DescribeAssetDatabaseInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDatabaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDatabaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDatabaseList(self, request):
        r"""查询资产管理数据库列表

        :param request: Request instance for DescribeAssetDatabaseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDatabaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDatabaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDiskList(self, request):
        r"""获取主机磁盘分区列表

        :param request: Request instance for DescribeAssetDiskList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDiskListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetEnvList(self, request):
        r"""查询资产管理环境变量列表

        :param request: Request instance for DescribeAssetEnvList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetEnvListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetEnvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetEnvList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetEnvListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetHostTotalCount(self, request):
        r"""获取主机所有资源数量

        :param request: Request instance for DescribeAssetHostTotalCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetHostTotalCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetHostTotalCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetHostTotalCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetHostTotalCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetInfo(self, request):
        r"""获取资产数量： 主机数、账号数、端口数、进程数、软件数、数据库数、Web应用数、Web框架数、Web服务数、Web站点数

        :param request: Request instance for DescribeAssetInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetInitServiceList(self, request):
        r"""查询资产管理启动服务列表

        :param request: Request instance for DescribeAssetInitServiceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInitServiceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInitServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetInitServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetInitServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetJarInfo(self, request):
        r"""获取Jar包详情

        :param request: Request instance for DescribeAssetJarInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetJarInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetJarInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetJarList(self, request):
        r"""查询Jar包列表

        :param request: Request instance for DescribeAssetJarList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetJarList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetJarListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetLoadInfo(self, request):
        r"""获取系统负载、内存使用率、硬盘使用率情况

        :param request: Request instance for DescribeAssetLoadInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetLoadInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetLoadInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetLoadInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetLoadInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetMachineDetail(self, request):
        r"""获取资产管理主机资源详细信息

        :param request: Request instance for DescribeAssetMachineDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetMachineDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetMachineDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetMachineList(self, request):
        r"""获取资产指纹页面的资源监控列表

        :param request: Request instance for DescribeAssetMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetMachineTagTop(self, request):
        r"""获取主机标签Top5

        :param request: Request instance for DescribeAssetMachineTagTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineTagTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineTagTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetMachineTagTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetMachineTagTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetPlanTaskList(self, request):
        r"""查询资产管理计划任务列表

        :param request: Request instance for DescribeAssetPlanTaskList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPlanTaskListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPlanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetPlanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetPlanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetPortCount(self, request):
        r"""获取所有端口数量

        :param request: Request instance for DescribeAssetPortCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPortCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPortCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetPortCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetPortCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetPortInfoList(self, request):
        r"""获取资产管理端口列表

        :param request: Request instance for DescribeAssetPortInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPortInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPortInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetPortInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetPortInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetProcessCount(self, request):
        r"""获取所有进程数量

        :param request: Request instance for DescribeAssetProcessCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetProcessCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetProcessCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetProcessCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetProcessCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetProcessInfoList(self, request):
        r"""获取资产管理进程列表

        :param request: Request instance for DescribeAssetProcessInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetProcessInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetProcessInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetProcessInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetProcessInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetRecentMachineInfo(self, request):
        r"""获取主机最近趋势情况

        :param request: Request instance for DescribeAssetRecentMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetRecentMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetRecentMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetRecentMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetRecentMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetSystemPackageList(self, request):
        r"""获取资产管理系统安装包列表

        :param request: Request instance for DescribeAssetSystemPackageList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetSystemPackageListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetSystemPackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSystemPackageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetSystemPackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTotalCount(self, request):
        r"""获取所有资源数量：主机、账号、端口、进程、软件、数据库、Web应用、Web框架、Web服务、Web站点

        :param request: Request instance for DescribeAssetTotalCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTotalCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTotalCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTotalCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTotalCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTypeTop(self, request):
        r"""获取各种类型资源Top5

        :param request: Request instance for DescribeAssetTypeTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTypeTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTypeTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTypeTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTypeTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTypes(self, request):
        r"""获取资产指纹类型列表

        :param request: Request instance for DescribeAssetTypes.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTypesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetUserCount(self, request):
        r"""获取所有账号数量

        :param request: Request instance for DescribeAssetUserCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetUserCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetUserCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetUserInfo(self, request):
        r"""获取主机账号详情

        :param request: Request instance for DescribeAssetUserInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetUserKeyList(self, request):
        r"""获取主机账号Key列表

        :param request: Request instance for DescribeAssetUserKeyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserKeyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetUserKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetUserKeyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetUserList(self, request):
        r"""获取账号列表

        :param request: Request instance for DescribeAssetUserList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebAppCount(self, request):
        r"""获取所有Web应用数量

        :param request: Request instance for DescribeAssetWebAppCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebAppCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebAppCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebAppList(self, request):
        r"""获取资产管理Web应用列表

        :param request: Request instance for DescribeAssetWebAppList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebAppList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebAppPluginList(self, request):
        r"""获取资产管理Web应用插件列表

        :param request: Request instance for DescribeAssetWebAppPluginList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppPluginListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppPluginListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebAppPluginList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebAppPluginListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebFrameCount(self, request):
        r"""获取所有Web框架数量

        :param request: Request instance for DescribeAssetWebFrameCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebFrameCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebFrameCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebFrameCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebFrameCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebFrameList(self, request):
        r"""获取资产管理Web框架列表

        :param request: Request instance for DescribeAssetWebFrameList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebFrameListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebFrameListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebFrameList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebFrameListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebLocationCount(self, request):
        r"""获取所有Web站点数量

        :param request: Request instance for DescribeAssetWebLocationCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebLocationCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebLocationCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebLocationInfo(self, request):
        r"""获取Web站点详情

        :param request: Request instance for DescribeAssetWebLocationInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebLocationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebLocationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebLocationList(self, request):
        r"""获取Web站点列表

        :param request: Request instance for DescribeAssetWebLocationList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebLocationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebLocationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebLocationPathList(self, request):
        r"""获取Web站点虚拟目录列表

        :param request: Request instance for DescribeAssetWebLocationPathList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationPathListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationPathListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebLocationPathList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebLocationPathListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebServiceCount(self, request):
        r"""获取所有Web服务数量

        :param request: Request instance for DescribeAssetWebServiceCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebServiceCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebServiceCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebServiceInfoList(self, request):
        r"""查询资产管理Web服务列表

        :param request: Request instance for DescribeAssetWebServiceInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebServiceInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebServiceInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebServiceProcessList(self, request):
        r"""获取Web服务关联进程列表

        :param request: Request instance for DescribeAssetWebServiceProcessList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceProcessListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebServiceProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebServiceProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackEventInfo(self, request):
        r"""网络攻击事件详情

        :param request: Request instance for DescribeAttackEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackEvents(self, request):
        r"""按分页形式展示网络攻击检测事件列表

        :param request: Request instance for DescribeAttackEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackStatistics(self, request):
        r"""网络攻击数据统计

        :param request: Request instance for DescribeAttackStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackTop(self, request):
        r"""网络攻击top5数据列表

        :param request: Request instance for DescribeAttackTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackTrends(self, request):
        r"""网络攻击趋势数据

        :param request: Request instance for DescribeAttackTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackTrends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackVulTypeList(self, request):
        r"""获取网络攻击威胁类型列表

        :param request: Request instance for DescribeAttackVulTypeList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackVulTypeListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackVulTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackVulTypeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackVulTypeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableExpertServiceDetail(self, request):
        r"""专家服务-可用订单详情

        :param request: Request instance for DescribeAvailableExpertServiceDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAvailableExpertServiceDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAvailableExpertServiceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableExpertServiceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableExpertServiceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanMode(self, request):
        r"""获取爆破阻断模式

        :param request: Request instance for DescribeBanMode.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanModeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanRegions(self, request):
        r"""获取阻断地域

        :param request: Request instance for DescribeBanRegions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanRegionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanStatus(self, request):
        r"""获取阻断按钮状态

        :param request: Request instance for DescribeBanStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanWhiteList(self, request):
        r"""获取阻断白名单列表

        :param request: Request instance for DescribeBanWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineAnalysisData(self, request):
        r"""根据基线策略id查询基线策略数据概览统计

        :param request: Request instance for DescribeBaselineAnalysisData.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineAnalysisDataRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineAnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineAnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineAnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineBasicInfo(self, request):
        r"""查询基线基础信息列表

        :param request: Request instance for DescribeBaselineBasicInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineBasicInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDefaultStrategyList(self, request):
        r"""查询基线默认策略列表信息

        :param request: Request instance for DescribeBaselineDefaultStrategyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDefaultStrategyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDefaultStrategyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDefaultStrategyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDefaultStrategyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDetail(self, request):
        r"""根据基线id查询基线详情接口

        :param request: Request instance for DescribeBaselineDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDetectList(self, request):
        r"""获取基线检测详情记录

        :param request: Request instance for DescribeBaselineDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDetectOverview(self, request):
        r"""获取基线检测概览

        :param request: Request instance for DescribeBaselineDetectOverview.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetectOverviewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetectOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDetectOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDetectOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDownloadList(self, request):
        r"""获取基线下载列表

        :param request: Request instance for DescribeBaselineDownloadList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDownloadListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDownloadListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDownloadList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDownloadListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineEffectHostList(self, request):
        r"""根据基线id查询基线影响主机列表

        :param request: Request instance for DescribeBaselineEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineFixList(self, request):
        r"""获取基线修复列表

        :param request: Request instance for DescribeBaselineFixList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineFixListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineFixListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineFixList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineFixListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineHostDetectList(self, request):
        r"""获取基线检测主机列表

        :param request: Request instance for DescribeBaselineHostDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineHostDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineHostDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineHostIgnoreList(self, request):
        r"""获取忽略规则主机列表

        :param request: Request instance for DescribeBaselineHostIgnoreList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostIgnoreListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineHostIgnoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineHostIgnoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineHostRiskTop(self, request):
        r"""获取基线服务器风险TOP5

        :param request: Request instance for DescribeBaselineHostRiskTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostRiskTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostRiskTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineHostRiskTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineHostRiskTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineHostTop(self, request):
        r"""接口返回TopN的风险服务器

        :param request: Request instance for DescribeBaselineHostTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineHostTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineHostTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemDetectList(self, request):
        r"""获取基线检测项的列表

        :param request: Request instance for DescribeBaselineItemDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemIgnoreList(self, request):
        r"""获取忽略规则项列表

        :param request: Request instance for DescribeBaselineItemIgnoreList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemIgnoreListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemIgnoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemIgnoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemInfo(self, request):
        r"""获取基线检测项信息

        :param request: Request instance for DescribeBaselineItemInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemList(self, request):
        r"""获取基线项检测结果列表

        :param request: Request instance for DescribeBaselineItemList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemRiskTop(self, request):
        r"""获取基线检测项TOP5

        :param request: Request instance for DescribeBaselineItemRiskTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemRiskTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemRiskTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemRiskTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemRiskTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineList(self, request):
        r"""查询基线列表信息

        :param request: Request instance for DescribeBaselineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselinePolicyList(self, request):
        r"""获取基线策略列表

        :param request: Request instance for DescribeBaselinePolicyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselinePolicyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselinePolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselinePolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinePolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRule(self, request):
        r"""根据基线id查询下属检测项信息

        :param request: Request instance for DescribeBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRuleCategoryList(self, request):
        r"""获取基线分类列表

        :param request: Request instance for DescribeBaselineRuleCategoryList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleCategoryListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRuleCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRuleDetectList(self, request):
        r"""获取基线规则检测列表

        :param request: Request instance for DescribeBaselineRuleDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRuleDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRuleIgnoreList(self, request):
        r"""获取基线忽略规则列表

        :param request: Request instance for DescribeBaselineRuleIgnoreList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleIgnoreListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRuleIgnoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleIgnoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRuleList(self, request):
        r"""获取基线规则列表

        :param request: Request instance for DescribeBaselineRuleList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineScanSchedule(self, request):
        r"""根据任务id查询基线检测进度

        :param request: Request instance for DescribeBaselineScanSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineScanScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineScanScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineScanSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineScanScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineStrategyDetail(self, request):
        r"""根据基线策略id查询策略详情

        :param request: Request instance for DescribeBaselineStrategyDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineStrategyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineStrategyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineStrategyList(self, request):
        r"""查询一个用户下的基线策略信息

        :param request: Request instance for DescribeBaselineStrategyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineStrategyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineStrategyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineTop(self, request):
        r"""根据策略id查询基线检测项TOP

        :param request: Request instance for DescribeBaselineTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineWeakPasswordList(self, request):
        r"""获取基线弱口令列表

        :param request: Request instance for DescribeBaselineWeakPasswordList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineWeakPasswordListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineWeakPasswordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineWeakPasswordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineWeakPasswordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEvents(self, request):
        r"""获取高危命令列表

        :param request: Request instance for DescribeBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEventsInfo(self, request):
        r"""查询高危命令事件详情

        :param request: Request instance for DescribeBashEventsInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEventsInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEventsInfoNew(self, request):
        r"""查询高危命令事件详情(新)

        :param request: Request instance for DescribeBashEventsInfoNew.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsInfoNewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsInfoNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEventsInfoNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsInfoNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEventsNew(self, request):
        r"""获取高危命令列表(新)

        :param request: Request instance for DescribeBashEventsNew.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsNewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEventsNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashPolicies(self, request):
        r"""获取高危命令策略列表

        :param request: Request instance for DescribeBashPolicies.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashPoliciesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashRules(self, request):
        r"""获取高危命令规则列表

        :param request: Request instance for DescribeBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBruteAttackList(self, request):
        r"""获取密码破解列表

        :param request: Request instance for DescribeBruteAttackList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBruteAttackList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBruteAttackListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBruteAttackRules(self, request):
        r"""获取爆破破解规则

        :param request: Request instance for DescribeBruteAttackRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBruteAttackRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBruteAttackRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCanFixVulMachine(self, request):
        r"""漏洞修护-查询可修护主机信息

        :param request: Request instance for DescribeCanFixVulMachine.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeCanFixVulMachineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeCanFixVulMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCanFixVulMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCanFixVulMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCanNotSeparateMachine(self, request):
        r"""获取木马不可隔离的主机

        :param request: Request instance for DescribeCanNotSeparateMachine.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeCanNotSeparateMachineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeCanNotSeparateMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCanNotSeparateMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCanNotSeparateMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientException(self, request):
        r"""获取客户端异常事件

        :param request: Request instance for DescribeClientException.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeClientExceptionRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeClientExceptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientException", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientExceptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefenceEventDetail(self, request):
        r"""获取漏洞防御事件详情

        :param request: Request instance for DescribeDefenceEventDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeDefenceEventDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeDefenceEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefenceEventDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefenceEventDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDirectConnectInstallCommand(self, request):
        r"""获取专线agent安装命令，包含token

        :param request: Request instance for DescribeDirectConnectInstallCommand.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeDirectConnectInstallCommandRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeDirectConnectInstallCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDirectConnectInstallCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDirectConnectInstallCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeESAggregations(self, request):
        r"""获取ES字段聚合结果

        :param request: Request instance for DescribeESAggregations.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeESAggregationsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeESAggregationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeESAggregations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeESAggregationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmergencyResponseList(self, request):
        r"""专家服务-应急响应列表

        :param request: Request instance for DescribeEmergencyResponseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyResponseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyResponseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmergencyResponseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmergencyResponseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmergencyVulList(self, request):
        r"""获取应急漏洞列表

        :param request: Request instance for DescribeEmergencyVulList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyVulListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmergencyVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmergencyVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventByTable(self, request):
        r"""根据事件表名和id查询告警事件详情

        :param request: Request instance for DescribeEventByTable.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeEventByTableRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeEventByTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventByTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventByTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExpertServiceList(self, request):
        r"""专家服务-安全管家列表

        :param request: Request instance for DescribeExpertServiceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExpertServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExpertServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExpertServiceOrderList(self, request):
        r"""专家服务-专家服务订单列表

        :param request: Request instance for DescribeExpertServiceOrderList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceOrderListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExpertServiceOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExpertServiceOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportMachines(self, request):
        r"""本接口 (DescribeExportMachines) 用于导出区域主机列表。

        :param request: Request instance for DescribeExportMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExportMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExportMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFastAnalysis(self, request):
        r"""日志快速分析统计

        :param request: Request instance for DescribeFastAnalysis.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFastAnalysisRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFastAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFastAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFastAnalysisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperEventRuleInfo(self, request):
        r"""查看产生事件时规则详情接口

        :param request: Request instance for DescribeFileTamperEventRuleInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperEventRuleInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperEventRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperEventRuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperEventRuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperEvents(self, request):
        r"""核心文件监控事件列表

        :param request: Request instance for DescribeFileTamperEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperRuleCount(self, request):
        r"""查询主机关联文件监控规则数量

        :param request: Request instance for DescribeFileTamperRuleCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRuleCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRuleCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperRuleCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperRuleCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperRuleInfo(self, request):
        r"""查询某个监控规则的详情

        :param request: Request instance for DescribeFileTamperRuleInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRuleInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperRuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperRuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperRules(self, request):
        r"""核心文件监控规则列表

        :param request: Request instance for DescribeFileTamperRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralStat(self, request):
        r"""获取主机相关统计

        :param request: Request instance for DescribeGeneralStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeGeneralStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeGeneralStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHistoryAccounts(self, request):
        r"""本接口 (DescribeHistoryAccounts) 用于获取账号变更历史列表数据。

        :param request: Request instance for DescribeHistoryAccounts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryAccountsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistoryAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistoryAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHistoryService(self, request):
        r"""查询日志检索服务信息

        :param request: Request instance for DescribeHistoryService.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryServiceRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistoryService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistoryServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostInfo(self, request):
        r"""主机信息与标签信息查询

        :param request: Request instance for DescribeHostInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHostInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHostInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostLoginList(self, request):
        r"""获取异常登录列表

        :param request: Request instance for DescribeHostLoginList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHostLoginListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHostLoginListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostLoginList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostLoginListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHotVulTop(self, request):
        r"""获取全网热点漏洞

        :param request: Request instance for DescribeHotVulTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHotVulTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHotVulTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHotVulTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHotVulTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIgnoreBaselineRule(self, request):
        r"""查询已经忽略的检测项信息

        :param request: Request instance for DescribeIgnoreBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIgnoreBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIgnoreBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIgnoreHostAndItemConfig(self, request):
        r"""获取一键忽略受影响的检测项和主机信息

        :param request: Request instance for DescribeIgnoreHostAndItemConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreHostAndItemConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreHostAndItemConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIgnoreHostAndItemConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIgnoreHostAndItemConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIgnoreRuleEffectHostList(self, request):
        r"""根据检测项id与筛选条件查询忽略检测项影响主机列表信息

        :param request: Request instance for DescribeIgnoreRuleEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreRuleEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreRuleEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIgnoreRuleEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIgnoreRuleEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImportMachineInfo(self, request):
        r"""查询批量导入机器信息

        :param request: Request instance for DescribeImportMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeImportMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeImportMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImportMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImportMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJavaMemShellInfo(self, request):
        r"""查询java内存马事件详细信息

        :param request: Request instance for DescribeJavaMemShellInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJavaMemShellInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJavaMemShellInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJavaMemShellList(self, request):
        r"""查询java内存马事件列表

        :param request: Request instance for DescribeJavaMemShellList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJavaMemShellList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJavaMemShellListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJavaMemShellPluginInfo(self, request):
        r"""查询给定主机java内存马插件信息

        :param request: Request instance for DescribeJavaMemShellPluginInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellPluginInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellPluginInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJavaMemShellPluginInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJavaMemShellPluginInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJavaMemShellPluginList(self, request):
        r"""查询java内存马插件列表

        :param request: Request instance for DescribeJavaMemShellPluginList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellPluginListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellPluginListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJavaMemShellPluginList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJavaMemShellPluginListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicense(self, request):
        r"""查询授权信息

        :param request: Request instance for DescribeLicense.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicense", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseBindList(self, request):
        r"""该接口可以获取设置中心-授权管理,某个授权下已绑定的授权机器列表

        :param request: Request instance for DescribeLicenseBindList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseBindList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseBindListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseBindSchedule(self, request):
        r"""查询授权绑定任务的进度

        :param request: Request instance for DescribeLicenseBindSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseBindSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseBindScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseGeneral(self, request):
        r"""授权管理-授权概览信息

        :param request: Request instance for DescribeLicenseGeneral.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseGeneralRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseGeneralResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseGeneral", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseGeneralResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseList(self, request):
        r"""获取用户所有授权订单信息

        :param request: Request instance for DescribeLicenseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseWhiteConfig(self, request):
        r"""查询授权白名单的可用配置

        :param request: Request instance for DescribeLicenseWhiteConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseWhiteConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseWhiteConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseWhiteConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseWhiteConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogDeliveryKafkaOptions(self, request):
        r"""查询日志投递kafka可选项列表

        :param request: Request instance for DescribeLogDeliveryKafkaOptions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogDeliveryKafkaOptionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogDeliveryKafkaOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogDeliveryKafkaOptions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogDeliveryKafkaOptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogExports(self, request):
        r"""获取日志下载任务列表

        :param request: Request instance for DescribeLogExports.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogExportsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogExportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogExports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogExportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogHistogram(self, request):
        r"""获取日志直方图信息

        :param request: Request instance for DescribeLogHistogram.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogHistogramRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogHistogramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogHistogram", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogHistogramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogIndex(self, request):
        r"""查询索引

        :param request: Request instance for DescribeLogIndex.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogIndexRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogKafkaDeliverInfo(self, request):
        r"""获取kafka投递信息

        :param request: Request instance for DescribeLogKafkaDeliverInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogKafkaDeliverInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogKafkaDeliverInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogKafkaDeliverInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogKafkaDeliverInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogStorageConfig(self, request):
        r"""获取日志存储配置

        :param request: Request instance for DescribeLogStorageConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogStorageConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogStorageConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogStorageRecord(self, request):
        r"""获取日志存储量记录

        :param request: Request instance for DescribeLogStorageRecord.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageRecordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogStorageRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogStorageRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogStorageStatistic(self, request):
        r"""获取日志检索容量使用统计

        :param request: Request instance for DescribeLogStorageStatistic.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageStatisticRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogStorageStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogStorageStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogType(self, request):
        r"""日志分析功能-获取日志类型，使用该接口返回的结果暂时可过滤的日志类型

        :param request: Request instance for DescribeLogType.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogTypeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteCombinedList(self, request):
        r"""获取异地登录白名单合并后列表

        :param request: Request instance for DescribeLoginWhiteCombinedList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteCombinedListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteCombinedListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteCombinedList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteCombinedListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteHostList(self, request):
        r"""查询合并后白名单机器列表

        :param request: Request instance for DescribeLoginWhiteHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteList(self, request):
        r"""获取异地登录白名单列表

        :param request: Request instance for DescribeLoginWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineClearHistory(self, request):
        r"""查询机器清理历史记录

        :param request: Request instance for DescribeMachineClearHistory.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineClearHistoryRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineClearHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineClearHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineClearHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineDefenseCnt(self, request):
        r"""查询主机高级防御事件数统计

        :param request: Request instance for DescribeMachineDefenseCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineDefenseCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineDefenseCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineDefenseCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineDefenseCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineFileTamperRules(self, request):
        r"""查询主机相关核心文件监控规则列表

        :param request: Request instance for DescribeMachineFileTamperRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineFileTamperRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineFileTamperRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineFileTamperRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineFileTamperRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineGeneral(self, request):
        r"""查询主机概览信息

        :param request: Request instance for DescribeMachineGeneral.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineGeneralRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineGeneralResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineGeneral", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineGeneralResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineInfo(self, request):
        r"""本接口（DescribeMachineInfo）用于获取机器详细信息。

        :param request: Request instance for DescribeMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineLicenseDetail(self, request):
        r"""本接口 (DescribeMachineLicenseDetail)查询机器授权信息

        :param request: Request instance for DescribeMachineLicenseDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineLicenseDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineLicenseDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineLicenseDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineLicenseDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineList(self, request):
        r"""用于网页防篡改获取区域主机列表。

        :param request: Request instance for DescribeMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineOsList(self, request):
        r"""查询可筛选操作系统列表.

        :param request: Request instance for DescribeMachineOsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineOsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineOsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineOsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineOsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineRegionList(self, request):
        r"""查询主机地域列表

        :param request: Request instance for DescribeMachineRegionList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineRegionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineRegionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineRegions(self, request):
        r"""获取机器地域列表

        :param request: Request instance for DescribeMachineRegions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineRiskCnt(self, request):
        r"""查询主机入侵检测事件统计

        :param request: Request instance for DescribeMachineRiskCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRiskCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRiskCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineRiskCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineRiskCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineSnapshot(self, request):
        r"""漏洞修护-查询主机创建的快照

        :param request: Request instance for DescribeMachineSnapshot.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineSnapshotRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachines(self, request):
        r"""本接口 (DescribeMachines) 用于获取区域主机列表。

        :param request: Request instance for DescribeMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachinesSimple(self, request):
        r"""本接口 (DescribeMachinesSimple) 用于获取主机列表。

        :param request: Request instance for DescribeMachinesSimple.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesSimpleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesSimpleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachinesSimple", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachinesSimpleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalWareList(self, request):
        r"""入侵检测获取木马列表

        :param request: Request instance for DescribeMalWareList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalWareListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalWareListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalWareList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalWareListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMaliciousRequestWhiteList(self, request):
        r"""查询恶意请求白名单列表

        :param request: Request instance for DescribeMaliciousRequestWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMaliciousRequestWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMaliciousRequestWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaliciousRequestWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaliciousRequestWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareFile(self, request):
        r"""获取木马文件下载地址

        :param request: Request instance for DescribeMalwareFile.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareFileRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareInfo(self, request):
        r"""查看恶意文件详情

        :param request: Request instance for DescribeMalwareInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareRiskOverview(self, request):
        r"""获取文件查杀概览信息

        :param request: Request instance for DescribeMalwareRiskOverview.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareRiskOverviewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareRiskOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareRiskOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareRiskOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareRiskWarning(self, request):
        r"""打开入侵检测-恶意文件检测,弹出风险预警内容

        :param request: Request instance for DescribeMalwareRiskWarning.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareRiskWarningRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareRiskWarningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareRiskWarning", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareRiskWarningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareTimingScanSetting(self, request):
        r"""查询定时扫描配置

        :param request: Request instance for DescribeMalwareTimingScanSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareTimingScanSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareTimingScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareTimingScanSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareTimingScanSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareWhiteList(self, request):
        r"""获取木马白名单列表

        :param request: Request instance for DescribeMalwareWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareWhiteListAffectList(self, request):
        r"""获取木马白名单受影响列表

        :param request: Request instance for DescribeMalwareWhiteListAffectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareWhiteListAffectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareWhiteListAffectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareWhiteListAffectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareWhiteListAffectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMonthInspectionReport(self, request):
        r"""专家服务-安全管家月巡检报告下载

        :param request: Request instance for DescribeMonthInspectionReport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMonthInspectionReportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMonthInspectionReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonthInspectionReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonthInspectionReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetAttackSetting(self, request):
        r"""查询网络攻击设置

        :param request: Request instance for DescribeNetAttackSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeNetAttackSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeNetAttackSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetAttackSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetAttackSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetAttackWhiteList(self, request):
        r"""获取网络攻击白名单列表

        :param request: Request instance for DescribeNetAttackWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeNetAttackWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeNetAttackWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetAttackWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetAttackWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpenPortStatistics(self, request):
        r"""本接口 (DescribeOpenPortStatistics) 用于获取端口统计列表。

        :param request: Request instance for DescribeOpenPortStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeOpenPortStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeOpenPortStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpenPortStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpenPortStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewStatistics(self, request):
        r"""获取概览统计数据。

        :param request: Request instance for DescribeOverviewStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeOverviewStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeOverviewStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivilegeEventInfo(self, request):
        r"""本地提权信息详情

        :param request: Request instance for DescribePrivilegeEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivilegeEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivilegeEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivilegeEvents(self, request):
        r"""获取本地提权事件列表

        :param request: Request instance for DescribePrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivilegeRules(self, request):
        r"""获取本地提权规则列表

        :param request: Request instance for DescribePrivilegeRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivilegeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivilegeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProVersionInfo(self, request):
        r"""用于获取专业版概览信息。

        :param request: Request instance for DescribeProVersionInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProVersionInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProVersionInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProVersionStatus(self, request):
        r"""用于获取单台主机或所有主机是否开通专业版状态。

        :param request: Request instance for DescribeProVersionStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProVersionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProVersionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcessStatistics(self, request):
        r"""本接口 (DescribeProcessStatistics) 用于获取进程统计列表数据。

        :param request: Request instance for DescribeProcessStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProcessStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProcessStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductStatus(self, request):
        r"""产品试用状态查询接口

        :param request: Request instance for DescribeProductStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProductStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProductStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectDirList(self, request):
        r"""网页防篡改防护目录列表

        :param request: Request instance for DescribeProtectDirList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectDirListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectDirListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectDirList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectDirListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectDirRelatedServer(self, request):
        r"""查询防护目录关联服务器列表信息

        :param request: Request instance for DescribeProtectDirRelatedServer.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectDirRelatedServerRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectDirRelatedServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectDirRelatedServer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectDirRelatedServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectNetList(self, request):
        r"""专家服务-旗舰重保列表

        :param request: Request instance for DescribeProtectNetList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectNetListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectNetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectNetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectNetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicProxyInstallCommand(self, request):
        r"""获取公网接入代理安装命令

        :param request: Request instance for DescribePublicProxyInstallCommand.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePublicProxyInstallCommandRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePublicProxyInstallCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicProxyInstallCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicProxyInstallCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseBackupList(self, request):
        r"""查询主机快照备份列表

        :param request: Request instance for DescribeRansomDefenseBackupList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseBackupListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseBackupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseBackupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseBackupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseEventsList(self, request):
        r"""查询防勒索事件列表

        :param request: Request instance for DescribeRansomDefenseEventsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseEventsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseEventsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseEventsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseEventsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseMachineList(self, request):
        r"""查询备份详情列表

        :param request: Request instance for DescribeRansomDefenseMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseMachineStrategyInfo(self, request):
        r"""获取主机绑定策略列表

        :param request: Request instance for DescribeRansomDefenseMachineStrategyInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseMachineStrategyInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseMachineStrategyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseMachineStrategyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseMachineStrategyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseRollBackTaskList(self, request):
        r"""查询回滚任务列表

        :param request: Request instance for DescribeRansomDefenseRollBackTaskList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseRollBackTaskListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseRollBackTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseRollBackTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseRollBackTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseState(self, request):
        r"""获取用户防勒索趋势

        :param request: Request instance for DescribeRansomDefenseState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseStrategyDetail(self, request):
        r"""获取策略详情

        :param request: Request instance for DescribeRansomDefenseStrategyDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseStrategyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseStrategyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseStrategyList(self, request):
        r"""查询防勒索策略列表

        :param request: Request instance for DescribeRansomDefenseStrategyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseStrategyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseStrategyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseStrategyMachines(self, request):
        r"""查询防勒索策略绑定机器列表

        :param request: Request instance for DescribeRansomDefenseStrategyMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseStrategyMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseStrategyMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseStrategyMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRansomDefenseTrend(self, request):
        r"""获取全网勒索态势

        :param request: Request instance for DescribeRansomDefenseTrend.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseTrendRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRansomDefenseTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRansomDefenseTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRansomDefenseTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRaspMaxCpu(self, request):
        r"""查看漏洞防御最大cpu限制

        :param request: Request instance for DescribeRaspMaxCpu.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRaspMaxCpuRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRaspMaxCpuResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRaspMaxCpu", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRaspMaxCpuResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRaspRuleVuls(self, request):
        r"""获取漏洞防御白名单漏洞列表

        :param request: Request instance for DescribeRaspRuleVuls.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRaspRuleVulsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRaspRuleVulsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRaspRuleVuls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRaspRuleVulsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRaspRules(self, request):
        r"""查询漏洞防御白名单

        :param request: Request instance for DescribeRaspRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRaspRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRaspRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRaspRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRaspRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecommendedProtectCpu(self, request):
        r"""查询推荐购买防护核数

        :param request: Request instance for DescribeRecommendedProtectCpu.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRecommendedProtectCpuRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRecommendedProtectCpuResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecommendedProtectCpu", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecommendedProtectCpuResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellEventInfo(self, request):
        r"""反弹shell信息详情

        :param request: Request instance for DescribeReverseShellEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellEvents(self, request):
        r"""获取反弹Shell列表

        :param request: Request instance for DescribeReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellRules(self, request):
        r"""获取反弹Shell规则列表

        :param request: Request instance for DescribeReverseShellRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskBatchStatus(self, request):
        r"""查询入侵检测事件更新状态任务是否完成

        :param request: Request instance for DescribeRiskBatchStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskBatchStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskBatchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskBatchStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskBatchStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsEventInfo(self, request):
        r"""查询恶意请求事件详情

        :param request: Request instance for DescribeRiskDnsEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsEventList(self, request):
        r"""获取恶意请求事件列表

        :param request: Request instance for DescribeRiskDnsEventList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsInfo(self, request):
        r"""查询恶意请求详情

        :param request: Request instance for DescribeRiskDnsInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsList(self, request):
        r"""入侵检测，获取恶意请求列表

        :param request: Request instance for DescribeRiskDnsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsPolicyList(self, request):
        r"""获取恶意请求策略列表

        :param request: Request instance for DescribeRiskDnsPolicyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsPolicyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskProcessEvents(self, request):
        r"""获取异常进程列表

        :param request: Request instance for DescribeRiskProcessEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskProcessEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskProcessEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskProcessEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskProcessEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSafeInfo(self, request):
        r"""查询安全通知信息

        :param request: Request instance for DescribeSafeInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSafeInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSafeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSafeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSafeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanMalwareSchedule(self, request):
        r"""查询木马扫描进度

        :param request: Request instance for DescribeScanMalwareSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanMalwareScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanMalwareScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanMalwareSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanMalwareScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanSchedule(self, request):
        r"""根据taskid查询检测进度

        :param request: Request instance for DescribeScanSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanState(self, request):
        r"""DescribeScanState 该接口能查询对应模块正在进行的扫描任务状态

        :param request: Request instance for DescribeScanState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanTaskDetails(self, request):
        r"""DescribeScanTaskDetails 查询扫描任务详情 , 可以查询扫描进度信息/异常;

        :param request: Request instance for DescribeScanTaskDetails.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskDetailsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanTaskStatus(self, request):
        r"""DescribeScanTaskStatus 查询机器扫描状态列表用于过滤筛选

        :param request: Request instance for DescribeScanTaskStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanVulSetting(self, request):
        r"""查询定期检测的配置

        :param request: Request instance for DescribeScanVulSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanVulSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanVulSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanVulSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanVulSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenAttackHotspot(self, request):
        r"""大屏可视化获取全网攻击热点

        :param request: Request instance for DescribeScreenAttackHotspot.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenAttackHotspotRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenAttackHotspotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenAttackHotspot", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenAttackHotspotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenBroadcasts(self, request):
        r"""大屏可视化安全播报

        :param request: Request instance for DescribeScreenBroadcasts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenBroadcastsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenBroadcastsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenBroadcasts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenBroadcastsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenDefenseTrends(self, request):
        r"""大屏可视化防趋势接口

        :param request: Request instance for DescribeScreenDefenseTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenDefenseTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenDefenseTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenDefenseTrends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenDefenseTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenEmergentMsg(self, request):
        r"""大屏可视化紧急通知

        :param request: Request instance for DescribeScreenEmergentMsg.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenEmergentMsgRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenEmergentMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenEmergentMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenEmergentMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenEventsCnt(self, request):
        r"""大屏可视化获取安全概览相关事件统计数据接口

        :param request: Request instance for DescribeScreenEventsCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenEventsCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenEventsCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenEventsCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenEventsCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenGeneralStat(self, request):
        r"""大屏可视化获取主机相关统计

        :param request: Request instance for DescribeScreenGeneralStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenGeneralStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenGeneralStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenGeneralStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenGeneralStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenHostInvasion(self, request):
        r"""大屏可视化主机入侵详情

        :param request: Request instance for DescribeScreenHostInvasion.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenHostInvasionRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenHostInvasionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenHostInvasion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenHostInvasionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenMachineRegions(self, request):
        r"""大屏可视化主机区域选项列表

        :param request: Request instance for DescribeScreenMachineRegions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenMachineRegionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenMachineRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenMachineRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenMachineRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenMachines(self, request):
        r"""大屏可视化主机区域列表

        :param request: Request instance for DescribeScreenMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenProtectionCnt(self, request):
        r"""大屏可视化主机安全防护引擎介绍

        :param request: Request instance for DescribeScreenProtectionCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenProtectionCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenProtectionCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenProtectionCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenProtectionCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenProtectionStat(self, request):
        r"""大屏获取安全防护状态

        :param request: Request instance for DescribeScreenProtectionStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenProtectionStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenProtectionStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenProtectionStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenProtectionStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScreenRiskAssetsTop(self, request):
        r"""大屏可视化风险资产top5（今日），统计今日风险资产

        :param request: Request instance for DescribeScreenRiskAssetsTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenRiskAssetsTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScreenRiskAssetsTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScreenRiskAssetsTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScreenRiskAssetsTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchLogs(self, request):
        r"""获取历史搜索记录

        :param request: Request instance for DescribeSearchLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchTemplates(self, request):
        r"""获取快速检索列表

        :param request: Request instance for DescribeSearchTemplates.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchTemplatesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityBroadcastInfo(self, request):
        r"""查询安全播报文章信息

        :param request: Request instance for DescribeSecurityBroadcastInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityBroadcastInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityBroadcastInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityBroadcastInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityBroadcastInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityBroadcasts(self, request):
        r"""安全播报列表页

        :param request: Request instance for DescribeSecurityBroadcasts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityBroadcastsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityBroadcastsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityBroadcasts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityBroadcastsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityDynamics(self, request):
        r"""本接口 (DescribeSecurityDynamics) 用于获取安全事件动态消息数据。

        :param request: Request instance for DescribeSecurityDynamics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityDynamicsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityDynamicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityDynamics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityDynamicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityEventStat(self, request):
        r"""获取安全事件统计

        :param request: Request instance for DescribeSecurityEventStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityEventStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityEventStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityEventsCnt(self, request):
        r"""获取安全概览相关事件统计数据接口

        :param request: Request instance for DescribeSecurityEventsCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventsCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventsCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityEventsCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityEventsCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityTrends(self, request):
        r"""本接口 (DescribeSecurityTrends) 用于获取安全事件统计数据。

        :param request: Request instance for DescribeSecurityTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityTrends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServerRelatedDirInfo(self, request):
        r"""查询服务区关联目录详情

        :param request: Request instance for DescribeServerRelatedDirInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeServerRelatedDirInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeServerRelatedDirInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServerRelatedDirInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServerRelatedDirInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServersAndRiskAndFirstInfo(self, request):
        r"""获取待处理风险文件数+影响服务器数+是否试用检测+最近检测时间

        :param request: Request instance for DescribeServersAndRiskAndFirstInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeServersAndRiskAndFirstInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeServersAndRiskAndFirstInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServersAndRiskAndFirstInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServersAndRiskAndFirstInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStrategyExist(self, request):
        r"""根据策略名查询策略是否存在

        :param request: Request instance for DescribeStrategyExist.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeStrategyExistRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeStrategyExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStrategyExist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStrategyExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagMachines(self, request):
        r"""获取指定标签关联的服务器信息

        :param request: Request instance for DescribeTagMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeTagMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeTagMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTags(self, request):
        r"""获取所有主机标签

        :param request: Request instance for DescribeTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrialReport(self, request):
        r"""查询主机安全授权试用报告(仅限控制台申领的)

        :param request: Request instance for DescribeTrialReport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeTrialReportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeTrialReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrialReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrialReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUndoVulCounts(self, request):
        r"""获取漏洞管理模块指定类型的待处理漏洞数、主机数和非专业版主机数量

        :param request: Request instance for DescribeUndoVulCounts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeUndoVulCountsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeUndoVulCountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUndoVulCounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUndoVulCountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsersConfig(self, request):
        r"""用于查询用户自定义配置

        :param request: Request instance for DescribeUsersConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeUsersConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeUsersConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsersConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsersConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsualLoginPlaces(self, request):
        r"""此接口（DescribeUsualLoginPlaces）用于查询常用登录地。

        :param request: Request instance for DescribeUsualLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsualLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsualLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVdbAndPocInfo(self, request):
        r"""获取病毒库及POC的更新信息

        :param request: Request instance for DescribeVdbAndPocInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVdbAndPocInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVdbAndPocInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVdbAndPocInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVdbAndPocInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVersionCompareChart(self, request):
        r"""获取版本对比信息

        :param request: Request instance for DescribeVersionCompareChart.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVersionCompareChartRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVersionCompareChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVersionCompareChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVersionCompareChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVersionStatistics(self, request):
        r"""用于统计专业版和基础版机器数。

        :param request: Request instance for DescribeVersionStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVersionStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVersionStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVersionStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVersionStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVertexDetail(self, request):
        r"""获取指定点属性信息

        :param request: Request instance for DescribeVertexDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVertexDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVertexDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVertexDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVertexDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulCountByDates(self, request):
        r"""漏洞管理模块，获取近日指定类型的漏洞数量和主机数量

        :param request: Request instance for DescribeVulCountByDates.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCountByDatesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCountByDatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulCountByDates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulCountByDatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulCveIdInfo(self, request):
        r"""CveId查询漏洞详情

        :param request: Request instance for DescribeVulCveIdInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCveIdInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCveIdInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulCveIdInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulCveIdInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceEvent(self, request):
        r"""获取漏洞防御事件列表

        :param request: Request instance for DescribeVulDefenceEvent.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceEventRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceList(self, request):
        r"""查询漏洞防御列表

        :param request: Request instance for DescribeVulDefenceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceOverview(self, request):
        r"""获取漏洞防御概览信息，包括事件趋势及插件开启情况

        :param request: Request instance for DescribeVulDefenceOverview.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceOverviewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefencePluginDetail(self, request):
        r"""获取单台主机漏洞防御插件信息

        :param request: Request instance for DescribeVulDefencePluginDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefencePluginDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefencePluginDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefencePluginExceptionCount(self, request):
        r"""获取当前异常插件数

        :param request: Request instance for DescribeVulDefencePluginExceptionCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginExceptionCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginExceptionCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefencePluginExceptionCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefencePluginExceptionCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefencePluginStatus(self, request):
        r"""获取各主机漏洞防御插件状态

        :param request: Request instance for DescribeVulDefencePluginStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefencePluginStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefencePluginStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefencePluginStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulDefenceSetting(self, request):
        r"""获取当前漏洞防御插件设置

        :param request: Request instance for DescribeVulDefenceSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulDefenceSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulDefenceSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulEffectHostList(self, request):
        r"""漏洞影响主机列表

        :param request: Request instance for DescribeVulEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulEffectModules(self, request):
        r"""漏洞影响组件列表

        :param request: Request instance for DescribeVulEffectModules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEffectModulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEffectModulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulEffectModules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulEffectModulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulEmergentMsg(self, request):
        r"""获取漏洞紧急通知

        :param request: Request instance for DescribeVulEmergentMsg.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEmergentMsgRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEmergentMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulEmergentMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulEmergentMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixStatus(self, request):
        r"""漏洞修护-查找主机漏洞修护进度

        :param request: Request instance for DescribeVulFixStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulFixStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulFixStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulHostCountScanTime(self, request):
        r"""获取待处理漏洞数+影响主机数

        :param request: Request instance for DescribeVulHostCountScanTime.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostCountScanTimeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostCountScanTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulHostCountScanTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulHostCountScanTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulHostTop(self, request):
        r"""获取服务器风险top列表

        :param request: Request instance for DescribeVulHostTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulHostTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulHostTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulInfoCvss(self, request):
        r"""漏洞详情，带CVSS版本

        :param request: Request instance for DescribeVulInfoCvss.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulInfoCvssRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulInfoCvssResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulInfoCvss", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulInfoCvssResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulLabels(self, request):
        r"""获取用户漏洞所有标签列表

        :param request: Request instance for DescribeVulLabels.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulLabelsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulLabelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLabels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulLabelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulLevelCount(self, request):
        r"""漏洞数量等级分布统计

        :param request: Request instance for DescribeVulLevelCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulLevelCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulLevelCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLevelCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulLevelCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulList(self, request):
        r"""获取漏洞列表数据

        :param request: Request instance for DescribeVulList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulOverview(self, request):
        r"""获取漏洞概览数据

        :param request: Request instance for DescribeVulOverview.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulOverviewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulStoreList(self, request):
        r"""获取漏洞库列表

        :param request: Request instance for DescribeVulStoreList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulStoreListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulStoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulStoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulStoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulTop(self, request):
        r"""漏洞top统计

        :param request: Request instance for DescribeVulTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulTrend(self, request):
        r"""获取漏洞态势信息

        :param request: Request instance for DescribeVulTrend.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulTrendRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWarningHostConfig(self, request):
        r"""查询告警机器范围配置

        :param request: Request instance for DescribeWarningHostConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWarningHostConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWarningHostConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarningHostConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWarningHostConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWarningList(self, request):
        r"""获取当前用户告警列表

        :param request: Request instance for DescribeWarningList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWarningListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWarningListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarningList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWarningListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebHookPolicy(self, request):
        r"""查询告警策略

        :param request: Request instance for DescribeWebHookPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebHookPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebHookPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebHookReceiver(self, request):
        r"""查询告警接收人列表

        :param request: Request instance for DescribeWebHookReceiver.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookReceiverRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebHookReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebHookReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebHookReceiverUsage(self, request):
        r"""查询指定告警接收人的关联策略使用信息

        :param request: Request instance for DescribeWebHookReceiverUsage.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookReceiverUsageRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookReceiverUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebHookReceiverUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebHookReceiverUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebHookRule(self, request):
        r"""获取企微机器人规则详情

        :param request: Request instance for DescribeWebHookRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebHookRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebHookRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebHookRules(self, request):
        r"""获取企微机器人规则列表

        :param request: Request instance for DescribeWebHookRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebHookRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebHookRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebHookRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebPageEventList(self, request):
        r"""查询篡改事件列表

        :param request: Request instance for DescribeWebPageEventList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageEventListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebPageEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebPageEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebPageGeneralize(self, request):
        r"""查询网站防篡改概览信息

        :param request: Request instance for DescribeWebPageGeneralize.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageGeneralizeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageGeneralizeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebPageGeneralize", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebPageGeneralizeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebPageProtectStat(self, request):
        r"""网站防篡改-查询动态防护信息

        :param request: Request instance for DescribeWebPageProtectStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageProtectStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageProtectStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebPageProtectStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebPageProtectStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebPageServiceInfo(self, request):
        r"""网站防篡改-查询网页防篡改服务器购买信息及服务器信息

        :param request: Request instance for DescribeWebPageServiceInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageServiceInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageServiceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebPageServiceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebPageServiceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyOrder(self, request):
        r"""DestroyOrder  该接口可以对资源销毁.

        :param request: Request instance for DestroyOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DestroyOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DestroyOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyOrder", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditBashRules(self, request):
        r"""新增或修改高危命令规则

        :param request: Request instance for EditBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.EditBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditPrivilegeRules(self, request):
        r"""新增或修改本地提权规则（支持多服务器选择）

        :param request: Request instance for EditPrivilegeRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditPrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditPrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditPrivilegeRules", params, headers=headers)
            response = json.loads(body)
            model = models.EditPrivilegeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditReverseShellRules(self, request):
        r"""编辑反弹Shell规则（支持多服务器选择）

        :param request: Request instance for EditReverseShellRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditReverseShellRules", params, headers=headers)
            response = json.loads(body)
            model = models.EditReverseShellRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditTags(self, request):
        r"""新增或编辑标签

        :param request: Request instance for EditTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditTags", params, headers=headers)
            response = json.loads(body)
            model = models.EditTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetAppList(self, request):
        r"""导出资产管理应用列表

        :param request: Request instance for ExportAssetAppList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetAppListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetAppList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetCoreModuleList(self, request):
        r"""导出资产管理内核模块列表

        :param request: Request instance for ExportAssetCoreModuleList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetCoreModuleListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetCoreModuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetCoreModuleList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetCoreModuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetDatabaseList(self, request):
        r"""导出资产管理数据库列表

        :param request: Request instance for ExportAssetDatabaseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetDatabaseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetDatabaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetDatabaseList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetDatabaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetEnvList(self, request):
        r"""导出资产管理环境变量列表

        :param request: Request instance for ExportAssetEnvList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetEnvListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetEnvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetEnvList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetEnvListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetInitServiceList(self, request):
        r"""导出资产管理启动服务列表

        :param request: Request instance for ExportAssetInitServiceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetInitServiceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetInitServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetInitServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetInitServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetJarList(self, request):
        r"""导出Jar包列表

        :param request: Request instance for ExportAssetJarList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetJarListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetJarListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetJarList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetJarListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetMachineDetail(self, request):
        r"""导出资产管理主机资源详细信息

        :param request: Request instance for ExportAssetMachineDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetMachineDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetMachineDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetMachineDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetMachineDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetMachineList(self, request):
        r"""导出资源监控列表

        :param request: Request instance for ExportAssetMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetPlanTaskList(self, request):
        r"""导出资产管理计划任务列表

        :param request: Request instance for ExportAssetPlanTaskList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetPlanTaskListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetPlanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetPlanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetPlanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetPortInfoList(self, request):
        r"""导出资产管理端口列表

        :param request: Request instance for ExportAssetPortInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetPortInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetPortInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetPortInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetPortInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetProcessInfoList(self, request):
        r"""导出资产管理进程列表

        :param request: Request instance for ExportAssetProcessInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetProcessInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetProcessInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetProcessInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetProcessInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetRecentMachineInfo(self, request):
        r"""导出主机最近趋势情况（最长最近90天）

        :param request: Request instance for ExportAssetRecentMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetRecentMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetRecentMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetRecentMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetRecentMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetSystemPackageList(self, request):
        r"""导出资产管理系统安装包列表

        :param request: Request instance for ExportAssetSystemPackageList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetSystemPackageListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetSystemPackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetSystemPackageList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetSystemPackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetUserList(self, request):
        r"""导出账号列表

        :param request: Request instance for ExportAssetUserList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetUserListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetUserList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetWebAppList(self, request):
        r"""导出资产管理Web应用列表

        :param request: Request instance for ExportAssetWebAppList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebAppListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetWebAppList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetWebAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetWebFrameList(self, request):
        r"""导出资产管理Web框架列表

        :param request: Request instance for ExportAssetWebFrameList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebFrameListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebFrameListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetWebFrameList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetWebFrameListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetWebLocationList(self, request):
        r"""导出Web站点列表

        :param request: Request instance for ExportAssetWebLocationList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebLocationListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebLocationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetWebLocationList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetWebLocationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetWebServiceInfoList(self, request):
        r"""导出资产管理Web服务列表

        :param request: Request instance for ExportAssetWebServiceInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebServiceInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebServiceInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetWebServiceInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetWebServiceInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAttackEvents(self, request):
        r"""导出网络攻击事件

        :param request: Request instance for ExportAttackEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAttackEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAttackEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAttackEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAttackEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineEffectHostList(self, request):
        r"""导出基线影响主机列表

        :param request: Request instance for ExportBaselineEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineFixList(self, request):
        r"""导出修复列表

        :param request: Request instance for ExportBaselineFixList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineFixListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineFixListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineFixList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineFixListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineHostDetectList(self, request):
        r"""导出基线主机检测

        :param request: Request instance for ExportBaselineHostDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineHostDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineHostDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineHostDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineHostDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineItemDetectList(self, request):
        r"""导出基线检测项

        :param request: Request instance for ExportBaselineItemDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineItemDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineItemDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineItemDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineItemDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineItemList(self, request):
        r"""导出检测项结果列表

        :param request: Request instance for ExportBaselineItemList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineItemListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineItemList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineList(self, request):
        r"""导出基线列表

        :param request: Request instance for ExportBaselineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineRuleDetectList(self, request):
        r"""导出基线检测规则

        :param request: Request instance for ExportBaselineRuleDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineRuleDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineRuleDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineRuleDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineRuleDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineWeakPasswordList(self, request):
        r"""导出弱口令配置列表

        :param request: Request instance for ExportBaselineWeakPasswordList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineWeakPasswordListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineWeakPasswordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineWeakPasswordList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineWeakPasswordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBashEvents(self, request):
        r"""导出高危命令事件

        :param request: Request instance for ExportBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBashEventsNew(self, request):
        r"""导出高危命令事件(新)

        :param request: Request instance for ExportBashEventsNew.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsNewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBashEventsNew", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBashEventsNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBashPolicies(self, request):
        r"""导出高危命令策略

        :param request: Request instance for ExportBashPolicies.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBashPoliciesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBashPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBashPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBashPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBruteAttacks(self, request):
        r"""本接口 (ExportBruteAttacks) 用于导出密码破解记录成CSV文件。

        :param request: Request instance for ExportBruteAttacks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBruteAttacksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportFileTamperEvents(self, request):
        r"""导出核心文件事件

        :param request: Request instance for ExportFileTamperEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportFileTamperEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportFileTamperEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportFileTamperEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportFileTamperEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportFileTamperRules(self, request):
        r"""导出核心文件监控规则

        :param request: Request instance for ExportFileTamperRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportFileTamperRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportFileTamperRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportFileTamperRules", params, headers=headers)
            response = json.loads(body)
            model = models.ExportFileTamperRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportIgnoreBaselineRule(self, request):
        r"""导出已忽略基线检测项信息

        :param request: Request instance for ExportIgnoreBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportIgnoreBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.ExportIgnoreBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportIgnoreRuleEffectHostList(self, request):
        r"""根据检测项id导出忽略检测项影响主机列表

        :param request: Request instance for ExportIgnoreRuleEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreRuleEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreRuleEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportIgnoreRuleEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportIgnoreRuleEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportJavaMemShellPlugins(self, request):
        r"""导出java内存马插件信息

        :param request: Request instance for ExportJavaMemShellPlugins.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportJavaMemShellPluginsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportJavaMemShellPluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportJavaMemShellPlugins", params, headers=headers)
            response = json.loads(body)
            model = models.ExportJavaMemShellPluginsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportJavaMemShells(self, request):
        r"""导出java内存马事件列表

        :param request: Request instance for ExportJavaMemShells.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportJavaMemShellsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportJavaMemShellsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportJavaMemShells", params, headers=headers)
            response = json.loads(body)
            model = models.ExportJavaMemShellsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportLicenseDetail(self, request):
        r"""导出授权列表对应的绑定信息

        :param request: Request instance for ExportLicenseDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportLicenseDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportLicenseDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportLicenseDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ExportLicenseDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportMaliciousRequests(self, request):
        r"""本接口 (ExportMaliciousRequests) 用于导出下载恶意请求文件。

        :param request: Request instance for ExportMaliciousRequests.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.ExportMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportMalwares(self, request):
        r"""本接口 (ExportMalwares) 用于导出木马记录CSV文件。

        :param request: Request instance for ExportMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.ExportMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportNonlocalLoginPlaces(self, request):
        r"""本接口 (ExportNonlocalLoginPlaces) 用于导出异地登录事件记录CSV文件。

        :param request: Request instance for ExportNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.ExportNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportPrivilegeEvents(self, request):
        r"""导出本地提权事件

        :param request: Request instance for ExportPrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportPrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportPrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportPrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportPrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportProtectDirList(self, request):
        r"""导出网页防篡改防护目录列表

        :param request: Request instance for ExportProtectDirList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportProtectDirListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportProtectDirListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportProtectDirList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportProtectDirListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRansomDefenseBackupList(self, request):
        r"""导出主机快照备份列表

        :param request: Request instance for ExportRansomDefenseBackupList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseBackupListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseBackupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRansomDefenseBackupList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRansomDefenseBackupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRansomDefenseEventsList(self, request):
        r"""导出防勒索事件列表

        :param request: Request instance for ExportRansomDefenseEventsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseEventsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseEventsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRansomDefenseEventsList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRansomDefenseEventsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRansomDefenseMachineList(self, request):
        r"""导出备份详情列表

        :param request: Request instance for ExportRansomDefenseMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRansomDefenseMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRansomDefenseMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRansomDefenseStrategyList(self, request):
        r"""导出防勒索策略列表

        :param request: Request instance for ExportRansomDefenseStrategyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseStrategyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseStrategyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRansomDefenseStrategyList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRansomDefenseStrategyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRansomDefenseStrategyMachines(self, request):
        r"""导出勒索防御策略绑定机器列表

        :param request: Request instance for ExportRansomDefenseStrategyMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseStrategyMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRansomDefenseStrategyMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRansomDefenseStrategyMachines", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRansomDefenseStrategyMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportReverseShellEvents(self, request):
        r"""导出反弹Shell事件

        :param request: Request instance for ExportReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRiskDnsEventList(self, request):
        r"""导出恶意请求事件列表

        :param request: Request instance for ExportRiskDnsEventList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRiskDnsEventListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRiskDnsEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRiskDnsEventList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRiskDnsEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRiskDnsPolicyList(self, request):
        r"""导出恶意请求策略列表

        :param request: Request instance for ExportRiskDnsPolicyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRiskDnsPolicyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRiskDnsPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRiskDnsPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRiskDnsPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportRiskProcessEvents(self, request):
        r"""导出异常进程事件

        :param request: Request instance for ExportRiskProcessEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportRiskProcessEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportRiskProcessEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRiskProcessEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRiskProcessEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportScanTaskDetails(self, request):
        r"""根据任务id导出指定扫描任务详情

        :param request: Request instance for ExportScanTaskDetails.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportScanTaskDetailsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportScanTaskDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportScanTaskDetails", params, headers=headers)
            response = json.loads(body)
            model = models.ExportScanTaskDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportSecurityTrends(self, request):
        r"""导出风险趋势

        :param request: Request instance for ExportSecurityTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportSecurityTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportSecurityTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportSecurityTrends", params, headers=headers)
            response = json.loads(body)
            model = models.ExportSecurityTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportTasks(self, request):
        r"""用于异步导出数据量大的日志文件

        :param request: Request instance for ExportTasks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportTasksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ExportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDefenceEvent(self, request):
        r"""导出漏洞防御事件

        :param request: Request instance for ExportVulDefenceEvent.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefenceEventRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefenceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDefenceEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDefenceEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDefenceList(self, request):
        r"""导出漏洞防御列表

        :param request: Request instance for ExportVulDefenceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefenceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefenceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDefenceList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDefenceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDefencePluginEvent(self, request):
        r"""导出漏洞防御插件事件

        :param request: Request instance for ExportVulDefencePluginEvent.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefencePluginEventRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDefencePluginEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDefencePluginEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDefencePluginEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDetectionExcel(self, request):
        r"""导出本次漏洞检测Excel

        :param request: Request instance for ExportVulDetectionExcel.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionExcelRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionExcelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDetectionExcel", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDetectionExcelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDetectionReport(self, request):
        r"""导出漏洞检测报告。

        :param request: Request instance for ExportVulDetectionReport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionReportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDetectionReport", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDetectionReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulEffectHostList(self, request):
        r"""导出漏洞影响主机列表

        :param request: Request instance for ExportVulEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulInfo(self, request):
        r"""导出漏洞信息，包括影响主机列表，组件信息

        :param request: Request instance for ExportVulInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulList(self, request):
        r"""漏洞管理-导出漏洞列表

        :param request: Request instance for ExportVulList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportWebPageEventList(self, request):
        r"""导出篡改事件列表

        :param request: Request instance for ExportWebPageEventList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportWebPageEventListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportWebPageEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportWebPageEventList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportWebPageEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FixBaselineDetect(self, request):
        r"""修复基线检测

        :param request: Request instance for FixBaselineDetect.
        :type request: :class:`tencentcloud.cwp.v20180228.models.FixBaselineDetectRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.FixBaselineDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FixBaselineDetect", params, headers=headers)
            response = json.loads(body)
            model = models.FixBaselineDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLocalStorageItem(self, request):
        r"""获取本地存储数据

        :param request: Request instance for GetLocalStorageItem.
        :type request: :class:`tencentcloud.cwp.v20180228.models.GetLocalStorageItemRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.GetLocalStorageItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLocalStorageItem", params, headers=headers)
            response = json.loads(body)
            model = models.GetLocalStorageItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IgnoreImpactedHosts(self, request):
        r"""产品变动切换到了\\n切换到 AddVulIgnoreRule / ModifyVulIgnoreRule  CancelVulIgnoreRule\\n相关接口

        本接口 (IgnoreImpactedHosts) 用于忽略漏洞。

        :param request: Request instance for IgnoreImpactedHosts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.IgnoreImpactedHostsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.IgnoreImpactedHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IgnoreImpactedHosts", params, headers=headers)
            response = json.loads(body)
            model = models.IgnoreImpactedHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KeysLocalStorage(self, request):
        r"""获取本地存储键值列表

        :param request: Request instance for KeysLocalStorage.
        :type request: :class:`tencentcloud.cwp.v20180228.models.KeysLocalStorageRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.KeysLocalStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KeysLocalStorage", params, headers=headers)
            response = json.loads(body)
            model = models.KeysLocalStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoOpenProVersionConfig(self, request):
        r"""用于设置新增主机自动开通专业防护配置。

        :param request: Request instance for ModifyAutoOpenProVersionConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyAutoOpenProVersionConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyAutoOpenProVersionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoOpenProVersionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoOpenProVersionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBanMode(self, request):
        r"""修改爆破阻断模式

        :param request: Request instance for ModifyBanMode.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBanModeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBanModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBanMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBanModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBanStatus(self, request):
        r"""设置阻断开关状态

        :param request: Request instance for ModifyBanStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBanStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBanWhiteList(self, request):
        r"""修改阻断白名单列表

        :param request: Request instance for ModifyBanWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBanWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBanWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBanWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBanWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselinePolicy(self, request):
        r"""更改基线策略设置

        :param request: Request instance for ModifyBaselinePolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselinePolicyState(self, request):
        r"""更改基线策略状态

        :param request: Request instance for ModifyBaselinePolicyState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselinePolicyStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselinePolicyStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselinePolicyState", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselinePolicyStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineRule(self, request):
        r"""更改基线检测规则

        :param request: Request instance for ModifyBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineRuleIgnore(self, request):
        r"""更改基线忽略规则

        :param request: Request instance for ModifyBaselineRuleIgnore.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineRuleIgnoreRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineRuleIgnoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineRuleIgnore", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineRuleIgnoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineWeakPassword(self, request):
        r"""更改或新增弱口令

        :param request: Request instance for ModifyBaselineWeakPassword.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineWeakPasswordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineWeakPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineWeakPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineWeakPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBashPolicy(self, request):
        r"""新增或修改高危命令策略

        :param request: Request instance for ModifyBashPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBashPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBashPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBashPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBashPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBashPolicyStatus(self, request):
        r"""切换高危命令策略状态

        :param request: Request instance for ModifyBashPolicyStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBashPolicyStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBashPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBashPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBashPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBruteAttackRules(self, request):
        r"""修改暴力破解规则

        :param request: Request instance for ModifyBruteAttackRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBruteAttackRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBruteAttackRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBruteAttackRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBruteAttackRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEventAttackStatus(self, request):
        r"""修改网络攻击事件状态

        :param request: Request instance for ModifyEventAttackStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyEventAttackStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyEventAttackStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEventAttackStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEventAttackStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileTamperEvents(self, request):
        r"""核心文件事件更新

        :param request: Request instance for ModifyFileTamperEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileTamperEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileTamperEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileTamperRule(self, request):
        r"""编辑、新增核心文件监控规则

        :param request: Request instance for ModifyFileTamperRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileTamperRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileTamperRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileTamperRuleStatus(self, request):
        r"""核心文件规则状态更新，支持批量删除 关闭

        :param request: Request instance for ModifyFileTamperRuleStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperRuleStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyFileTamperRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileTamperRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileTamperRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyJavaMemShellPluginSwitch(self, request):
        r"""开关java内存马插件

        :param request: Request instance for ModifyJavaMemShellPluginSwitch.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyJavaMemShellPluginSwitchRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyJavaMemShellPluginSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyJavaMemShellPluginSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyJavaMemShellPluginSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyJavaMemShellsStatus(self, request):
        r"""修改java内存马事件状态

        :param request: Request instance for ModifyJavaMemShellsStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyJavaMemShellsStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyJavaMemShellsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyJavaMemShellsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyJavaMemShellsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLicenseBinds(self, request):
        r"""设置中心-授权管理 对某个授权批量绑定机器

        :param request: Request instance for ModifyLicenseBinds.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseBindsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLicenseBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLicenseBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLicenseOrder(self, request):
        r"""编辑《主机安全-按量计费》授权订单

        :param request: Request instance for ModifyLicenseOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLicenseOrder", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLicenseOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLicenseUnBinds(self, request):
        r"""设置中心-授权管理 对某个授权批量解绑机器

        :param request: Request instance for ModifyLicenseUnBinds.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseUnBindsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseUnBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLicenseUnBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLicenseUnBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogKafkaAccess(self, request):
        r"""新增或修改日志投递kafka接入配置

        :param request: Request instance for ModifyLogKafkaAccess.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaAccessRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogKafkaAccess", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogKafkaAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogKafkaDeliverType(self, request):
        r"""修改指定日志类别投递配置、开关

        :param request: Request instance for ModifyLogKafkaDeliverType.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaDeliverTypeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaDeliverTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogKafkaDeliverType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogKafkaDeliverTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogKafkaState(self, request):
        r"""修改日志投递状态信息

        :param request: Request instance for ModifyLogKafkaState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLogKafkaStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogKafkaState", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogKafkaStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogStorageConfig(self, request):
        r"""修改日志存储配置

        :param request: Request instance for ModifyLogStorageConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLogStorageConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLogStorageConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogStorageConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogStorageConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoginWhiteInfo(self, request):
        r"""更新登录审计白名单信息

        :param request: Request instance for ModifyLoginWhiteInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLoginWhiteInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLoginWhiteInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoginWhiteInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoginWhiteInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoginWhiteRecord(self, request):
        r"""更新合并后登录审计白名单信息（服务器列表数目应小于1000）

        :param request: Request instance for ModifyLoginWhiteRecord.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLoginWhiteRecordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLoginWhiteRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoginWhiteRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoginWhiteRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMachineAutoClearConfig(self, request):
        r"""修改机器清理配置

        :param request: Request instance for ModifyMachineAutoClearConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMachineAutoClearConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMachineAutoClearConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMachineAutoClearConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMachineAutoClearConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMachineRemark(self, request):
        r"""修改主机备注信息

        :param request: Request instance for ModifyMachineRemark.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMachineRemarkRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMachineRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMachineRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMachineRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMaliciousRequestWhiteList(self, request):
        r"""更新恶意请求白名单

        :param request: Request instance for ModifyMaliciousRequestWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMaliciousRequestWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMaliciousRequestWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaliciousRequestWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMaliciousRequestWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMalwareTimingScanSettings(self, request):
        r"""定时扫描设置

        :param request: Request instance for ModifyMalwareTimingScanSettings.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareTimingScanSettingsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareTimingScanSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMalwareTimingScanSettings", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMalwareTimingScanSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMalwareWhiteList(self, request):
        r"""编辑木马白名单

        :param request: Request instance for ModifyMalwareWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMalwareWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMalwareWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetAttackSetting(self, request):
        r"""修改网络攻击设置

        :param request: Request instance for ModifyNetAttackSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyNetAttackSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyNetAttackSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetAttackSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetAttackSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetAttackWhiteList(self, request):
        r"""编辑网络攻击白名单

        :param request: Request instance for ModifyNetAttackWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyNetAttackWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyNetAttackWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetAttackWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetAttackWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOrderAttribute(self, request):
        r"""对订单属性编辑

        :param request: Request instance for ModifyOrderAttribute.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyOrderAttributeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyOrderAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOrderAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOrderAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRansomDefenseEventsStatus(self, request):
        r"""修改防勒索事件状态

        :param request: Request instance for ModifyRansomDefenseEventsStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRansomDefenseEventsStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRansomDefenseEventsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRansomDefenseEventsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRansomDefenseEventsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRansomDefenseStrategyStatus(self, request):
        r"""批量修改防勒索策略状态

        :param request: Request instance for ModifyRansomDefenseStrategyStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRansomDefenseStrategyStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRansomDefenseStrategyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRansomDefenseStrategyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRansomDefenseStrategyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRaspMaxCpu(self, request):
        r"""编辑漏洞防御最大cpu配置

        :param request: Request instance for ModifyRaspMaxCpu.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRaspMaxCpuRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRaspMaxCpuResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRaspMaxCpu", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRaspMaxCpuResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRaspRules(self, request):
        r"""添加漏洞防御白名单

        :param request: Request instance for ModifyRaspRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRaspRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRaspRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRaspRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRaspRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReverseShellRulesAggregation(self, request):
        r"""编辑反弹Shell规则（支持多服务器选择）

        :param request: Request instance for ModifyReverseShellRulesAggregation.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyReverseShellRulesAggregationRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyReverseShellRulesAggregationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReverseShellRulesAggregation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReverseShellRulesAggregationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskDnsPolicy(self, request):
        r"""更改恶意请求策略

        :param request: Request instance for ModifyRiskDnsPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskDnsPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskDnsPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskDnsPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskDnsPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskDnsPolicyStatus(self, request):
        r"""更改恶意请求策略状态

        :param request: Request instance for ModifyRiskDnsPolicyStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskDnsPolicyStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskDnsPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskDnsPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskDnsPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskEventsStatus(self, request):
        r"""入侵检测所有事件的状态，包括：文件查杀，异常登录，密码破解，高危命令，反弹shell，本地提取

        :param request: Request instance for ModifyRiskEventsStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskEventsStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyRiskEventsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskEventsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskEventsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUsersConfig(self, request):
        r"""用于创建/修改用户自定义配置

        :param request: Request instance for ModifyUsersConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyUsersConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyUsersConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUsersConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUsersConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVulDefenceEventStatus(self, request):
        r"""修改漏洞防御事件状态（修复漏洞通过其他接口实现）

        :param request: Request instance for ModifyVulDefenceEventStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyVulDefenceEventStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyVulDefenceEventStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulDefenceEventStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVulDefenceEventStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVulDefenceSetting(self, request):
        r"""修改漏洞防御插件设置
        1）新增主机自动加入，scope为1，quuids为空
        2）全量旗舰版不自动加入，scope为0，quuids为当前quuid列表，
        3）给定quuid列表，scope为0，quuids为用户选择quuid

        :param request: Request instance for ModifyVulDefenceSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyVulDefenceSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyVulDefenceSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulDefenceSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVulDefenceSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWarningHostConfig(self, request):
        r"""修改告警机器范围配置

        :param request: Request instance for ModifyWarningHostConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningHostConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningHostConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWarningHostConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWarningHostConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWarningSetting(self, request):
        r"""修改告警设置

        :param request: Request instance for ModifyWarningSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWarningSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWarningSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebHookPolicy(self, request):
        r"""新增或修改告警策略

        :param request: Request instance for ModifyWebHookPolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookPolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebHookPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebHookPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebHookPolicyStatus(self, request):
        r"""修改告警策略开关

        :param request: Request instance for ModifyWebHookPolicyStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookPolicyStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebHookPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebHookPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebHookReceiver(self, request):
        r"""新增或更新告警接收人

        :param request: Request instance for ModifyWebHookReceiver.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookReceiverRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebHookReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebHookReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebHookRule(self, request):
        r"""新增或修改企微机器人规则

        :param request: Request instance for ModifyWebHookRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebHookRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebHookRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebHookRuleStatus(self, request):
        r"""修改企微机器人规则状态

        :param request: Request instance for ModifyWebHookRuleStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookRuleStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebHookRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebHookRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebHookRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebPageProtectDir(self, request):
        r"""创建/修改网站防护目录

        :param request: Request instance for ModifyWebPageProtectDir.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectDirRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectDirResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebPageProtectDir", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebPageProtectDirResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebPageProtectSetting(self, request):
        r"""修改网站防护设置

        :param request: Request instance for ModifyWebPageProtectSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebPageProtectSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebPageProtectSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebPageProtectSwitch(self, request):
        r"""网站防篡改防护设置开关

        :param request: Request instance for ModifyWebPageProtectSwitch.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSwitchRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebPageProtectSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebPageProtectSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RansomDefenseRollback(self, request):
        r"""防勒索快照回滚

        :param request: Request instance for RansomDefenseRollback.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RansomDefenseRollbackRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RansomDefenseRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RansomDefenseRollback", params, headers=headers)
            response = json.loads(body)
            model = models.RansomDefenseRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverMalwares(self, request):
        r"""本接口（RecoverMalwares）用于批量恢复已经被隔离的木马文件。

        :param request: Request instance for RecoverMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RecoverMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RecoverMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveLocalStorageItem(self, request):
        r"""删除本地存储数据

        :param request: Request instance for RemoveLocalStorageItem.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RemoveLocalStorageItemRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RemoveLocalStorageItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveLocalStorageItem", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveLocalStorageItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveMachine(self, request):
        r"""删除主机所有记录，目前只支持非腾讯云主机，且需要主机在离线状态

        :param request: Request instance for RemoveMachine.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RemoveMachineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RemoveMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveMachine", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryCreateSnapshot(self, request):
        r"""快照创建失败时可以重试创建快照并且自动进行漏洞修复

        :param request: Request instance for RetryCreateSnapshot.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RetryCreateSnapshotRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RetryCreateSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryCreateSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.RetryCreateSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryVulFix(self, request):
        r"""修复失败时单独对某一个主机修复漏洞

        :param request: Request instance for RetryVulFix.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RetryVulFixRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RetryVulFixResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryVulFix", params, headers=headers)
            response = json.loads(body)
            model = models.RetryVulFixResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanAsset(self, request):
        r"""资产指纹启动扫描

        :param request: Request instance for ScanAsset.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanAssetRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanAsset", params, headers=headers)
            response = json.loads(body)
            model = models.ScanAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanBaseline(self, request):
        r"""基线检测与基线重新检测接口

        :param request: Request instance for ScanBaseline.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanBaselineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanBaselineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanBaseline", params, headers=headers)
            response = json.loads(body)
            model = models.ScanBaselineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanTaskAgain(self, request):
        r"""ScanTaskAgain  重新开始扫描任务，可以指定机器

        :param request: Request instance for ScanTaskAgain.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanTaskAgainRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanTaskAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanTaskAgain", params, headers=headers)
            response = json.loads(body)
            model = models.ScanTaskAgainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanVul(self, request):
        r"""漏洞一键检测

        :param request: Request instance for ScanVul.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanVul", params, headers=headers)
            response = json.loads(body)
            model = models.ScanVulResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanVulAgain(self, request):
        r"""漏洞管理-重新检测接口

        :param request: Request instance for ScanVulAgain.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulAgainRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanVulAgain", params, headers=headers)
            response = json.loads(body)
            model = models.ScanVulAgainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanVulSetting(self, request):
        r"""定期扫描漏洞设置

        :param request: Request instance for ScanVulSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanVulSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ScanVulSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchLog(self, request):
        r"""查询日志

        :param request: Request instance for SearchLog.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SearchLogRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SearchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SeparateMalwares(self, request):
        r"""本接口（SeparateMalwares）用于隔离木马。

        :param request: Request instance for SeparateMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SeparateMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SeparateMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SeparateMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.SeparateMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetBashEventsStatus(self, request):
        r"""设置高危命令事件状态

        :param request: Request instance for SetBashEventsStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SetBashEventsStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SetBashEventsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetBashEventsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.SetBashEventsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLocalStorageExpire(self, request):
        r"""设置本地存储过期时间

        :param request: Request instance for SetLocalStorageExpire.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SetLocalStorageExpireRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SetLocalStorageExpireResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLocalStorageExpire", params, headers=headers)
            response = json.loads(body)
            model = models.SetLocalStorageExpireResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLocalStorageItem(self, request):
        r"""设置本地存储数据

        :param request: Request instance for SetLocalStorageItem.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SetLocalStorageItemRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SetLocalStorageItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLocalStorageItem", params, headers=headers)
            response = json.loads(body)
            model = models.SetLocalStorageItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartBaselineDetect(self, request):
        r"""检测基线

        :param request: Request instance for StartBaselineDetect.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StartBaselineDetectRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StartBaselineDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartBaselineDetect", params, headers=headers)
            response = json.loads(body)
            model = models.StartBaselineDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAssetScan(self, request):
        r"""停止资产扫描任务

        :param request: Request instance for StopAssetScan.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StopAssetScanRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StopAssetScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAssetScan", params, headers=headers)
            response = json.loads(body)
            model = models.StopAssetScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopBaselineDetect(self, request):
        r"""停止基线检测

        :param request: Request instance for StopBaselineDetect.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StopBaselineDetectRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StopBaselineDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopBaselineDetect", params, headers=headers)
            response = json.loads(body)
            model = models.StopBaselineDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopNoticeBanTips(self, request):
        r"""不再提醒爆破阻断提示弹窗

        :param request: Request instance for StopNoticeBanTips.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StopNoticeBanTipsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StopNoticeBanTipsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopNoticeBanTips", params, headers=headers)
            response = json.loads(body)
            model = models.StopNoticeBanTipsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchBashRules(self, request):
        r"""切换高危命令规则状态

        :param request: Request instance for SwitchBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SwitchBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SwitchBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncAssetScan(self, request):
        r"""同步资产扫描信息

        :param request: Request instance for SyncAssetScan.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SyncAssetScanRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SyncAssetScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncAssetScan", params, headers=headers)
            response = json.loads(body)
            model = models.SyncAssetScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncBaselineDetectSummary(self, request):
        r"""同步基线检测进度概要

        :param request: Request instance for SyncBaselineDetectSummary.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SyncBaselineDetectSummaryRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SyncBaselineDetectSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncBaselineDetectSummary", params, headers=headers)
            response = json.loads(body)
            model = models.SyncBaselineDetectSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncMachines(self, request):
        r"""同步机器信息

        :param request: Request instance for SyncMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SyncMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SyncMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncMachines", params, headers=headers)
            response = json.loads(body)
            model = models.SyncMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TestWebHookRule(self, request):
        r"""测试企微机器人规则

        :param request: Request instance for TestWebHookRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.TestWebHookRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.TestWebHookRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TestWebHookRule", params, headers=headers)
            response = json.loads(body)
            model = models.TestWebHookRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TrustMalwares(self, request):
        r"""本接口(TrustMalwares)将被识别木马文件设为信任。

        :param request: Request instance for TrustMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.TrustMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.TrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TrustMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.TrustMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UntrustMalwares(self, request):
        r"""本接口（UntrustMalwares）用于取消信任木马文件。

        :param request: Request instance for UntrustMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UntrustMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UntrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UntrustMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.UntrustMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBaselineStrategy(self, request):
        r"""根据基线策略id更新策略信息

        :param request: Request instance for UpdateBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UpdateBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UpdateBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBaselineStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBaselineStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateMachineTags(self, request):
        r"""关联机器标签列表

        :param request: Request instance for UpdateMachineTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UpdateMachineTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UpdateMachineTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateMachineTags", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateMachineTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))