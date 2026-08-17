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


    def AddDspmAssetManager(self, request):
        r"""添加资产管理员

        :param request: Request instance for AddDspmAssetManager.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddDspmAssetManagerRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddDspmAssetManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDspmAssetManager", params, headers=headers)
            response = json.loads(body)
            model = models.AddDspmAssetManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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


    def AddVulWhitelist(self, request):
        r"""添加漏洞白名单

        :param request: Request instance for AddVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.AddVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelEdrAlertIgnore(self, request):
        r"""取消已永久忽略的EDR多行为告警，从AI-Link永久忽略白名单移除对应主机+规则记录，并将告警状态恢复为待处理（PENDING）

        :param request: Request instance for CancelEdrAlertIgnore.
        :type request: :class:`tencentcloud.csip.v20221121.models.CancelEdrAlertIgnoreRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CancelEdrAlertIgnoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelEdrAlertIgnore", params, headers=headers)
            response = json.loads(body)
            model = models.CancelEdrAlertIgnoreResponse()
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


    def CreateCSIPManualMalwareScan(self, request):
        r"""CSIP 手动扫描创建接口

        :param request: Request instance for CreateCSIPManualMalwareScan.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCSIPManualMalwareScanRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCSIPManualMalwareScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCSIPManualMalwareScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCSIPManualMalwareScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCosAssetSyncTask(self, request):
        r"""创建资产同步任务

        :param request: Request instance for CreateCosAssetSyncTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCosAssetSyncTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCosAssetSyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosAssetSyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCosAssetSyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCosObjectScanTask(self, request):
        r"""创建cos病毒扫描、敏感数据识别任务

        :param request: Request instance for CreateCosObjectScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCosObjectScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCosObjectScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosObjectScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCosObjectScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCosPolicy(self, request):
        r"""添加cos告警策略

        :param request: Request instance for CreateCosPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCosPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCosPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCosPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCosRiskScanTask(self, request):
        r"""创建风险监测任务

        :param request: Request instance for CreateCosRiskScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCosRiskScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCosRiskScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosRiskScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCosRiskScanTaskResponse()
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


    def CreateDspmAccessExportJob(self, request):
        r"""创建Dspm访问记录导出任务

        :param request: Request instance for CreateDspmAccessExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmAccessExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmAccessExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmAccessExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmAccessExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmApplyOrder(self, request):
        r"""创建Dspm申请单

        :param request: Request instance for CreateDspmApplyOrder.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmApplyOrderRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmApplyOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmApplyOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmApplyOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmApproveHistoryExportJob(self, request):
        r"""创建Dspm审批历史导出任务

        :param request: Request instance for CreateDspmApproveHistoryExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmApproveHistoryExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmApproveHistoryExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmApproveHistoryExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmApproveHistoryExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmAssetAccessTopologyExportJob(self, request):
        r"""创建Dspm资产访问拓扑导出任务

        :param request: Request instance for CreateDspmAssetAccessTopologyExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetAccessTopologyExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetAccessTopologyExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmAssetAccessTopologyExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmAssetAccessTopologyExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmAssetIdentifyInfoExportJob(self, request):
        r"""创建Dspm资产列表导出任务

        :param request: Request instance for CreateDspmAssetIdentifyInfoExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetIdentifyInfoExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetIdentifyInfoExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmAssetIdentifyInfoExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmAssetIdentifyInfoExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmAssetsExportJob(self, request):
        r"""创建Dspm资产列表导出任务

        :param request: Request instance for CreateDspmAssetsExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetsExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmAssetsExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmAssetsExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmExportTask(self, request):
        r"""创建日志导出任务

        :param request: Request instance for CreateDspmExportTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmExportTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyCategory(self, request):
        r"""创建dspm数据识别分类

        :param request: Request instance for CreateDspmIdentifyCategory.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyCategoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyCategory", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyComplianceCategoryRelation(self, request):
        r"""创建dspm数据识别模板分类关联

        :param request: Request instance for CreateDspmIdentifyComplianceCategoryRelation.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceCategoryRelationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceCategoryRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyComplianceCategoryRelation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyComplianceCategoryRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyComplianceGroup(self, request):
        r"""创建dspm数据识别模板

        :param request: Request instance for CreateDspmIdentifyComplianceGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyComplianceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyComplianceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyComplianceGroupCopy(self, request):
        r"""复制dspm数据识别模板

        :param request: Request instance for CreateDspmIdentifyComplianceGroupCopy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceGroupCopyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceGroupCopyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyComplianceGroupCopy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyComplianceGroupCopyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyComplianceRuleRelation(self, request):
        r"""创建dspm数据识别模板数据项关联

        :param request: Request instance for CreateDspmIdentifyComplianceRuleRelation.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceRuleRelationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceRuleRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyComplianceRuleRelation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyComplianceRuleRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyInfoListExportJob(self, request):
        r"""创建Dspm身份列表导出任务

        :param request: Request instance for CreateDspmIdentifyInfoListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyInfoListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyInfoListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyInfoListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyInfoListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyLevelGroup(self, request):
        r"""创建dspm数据识别分级组

        :param request: Request instance for CreateDspmIdentifyLevelGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyLevelGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyLevelGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyLevelGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyLevelGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyRule(self, request):
        r"""创建dspm数据识别数据项

        :param request: Request instance for CreateDspmIdentifyRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmPersonalIdentify(self, request):
        r"""创建Dspm个人身份id

        :param request: Request instance for CreateDspmPersonalIdentify.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmPersonalIdentifyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmPersonalIdentifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmPersonalIdentify", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmPersonalIdentifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmRiskExportJob(self, request):
        r"""创建Dspm风险导出任务

        :param request: Request instance for CreateDspmRiskExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmRiskExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmRiskExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmRiskExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmRiskExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmWhitelistStrategy(self, request):
        r"""创建Dspm白名单策略

        :param request: Request instance for CreateDspmWhitelistStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmWhitelistStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmWhitelistStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmWhitelistStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmWhitelistStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEDRManualScan(self, request):
        r"""点击开始扫描后触发，支持多账号、多资产类型。同时选主机和容器集群时拆分为两个独立任务（主机+容器）。

        :param request: Request instance for CreateEDRManualScan.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateEDRManualScanRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateEDRManualScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEDRManualScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEDRManualScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdrAlertExportJob(self, request):
        r"""创建EDR告警导出任务

        :param request: Request instance for CreateEdrAlertExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateEdrAlertExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateEdrAlertExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdrAlertExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdrAlertExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHostVulExportJob(self, request):
        r"""创建主机列漏洞表导出任务

        :param request: Request instance for CreateHostVulExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateHostVulExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateHostVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHostVulExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostVulExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIaCAccessToken(self, request):
        r"""创建IaC检测接入Token

        :param request: Request instance for CreateIaCAccessToken.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateIaCAccessTokenRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateIaCAccessTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIaCAccessToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIaCAccessTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIaCFileExportJob(self, request):
        r"""创建IaC检测文件导出任务

        :param request: Request instance for CreateIaCFileExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateIaCFileExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateIaCFileExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIaCFileExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIaCFileExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIaCFileReScanTask(self, request):
        r"""创建IaC检测文件重新扫描任务

        :param request: Request instance for CreateIaCFileReScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateIaCFileReScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateIaCFileReScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIaCFileReScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIaCFileReScanTaskResponse()
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


    def CreateSkillScan(self, request):
        r"""上传 Skill ZIP 文件，触发异步安全检测。上传成功后应使用返回的 ContentHash + EngineVersion 轮询 DescribeSkillScanResult 接口获取结果。上传接口具备幂等性，同一 Hash 的文件重复上传不会创建重复任务。检测结果保留90天，超期后需重新上传检测。

        :param request: Request instance for CreateSkillScan.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateSkillScanRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateSkillScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSkillScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSkillScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulFixRetryTask(self, request):
        r"""对修复失败的漏洞修复任务进行重试，仅针对原任务中修复失败的主机重新下发修复指令。仅当任务状态为部分修复失败或全部修复失败时允许重试。

        :param request: Request instance for CreateVulFixRetryTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulFixRetryTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulFixRetryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulFixRetryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulFixRetryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulFixTask(self, request):
        r"""用户手动提交漏洞修复任务，指定需要修复的漏洞和目标主机，系统创建修复任务并下发执行。支持指定修复超时时间、是否创建快照等选项。通过FixItems数组精确控制每个漏洞/KB补丁修复哪些主机。

        :param request: Request instance for CreateVulFixTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulFixTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulFixTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulFixTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulFixTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulFixedExportJob(self, request):
        r"""创建已修复漏洞列表的导出任务。支持与 DescribeVulFixedList 相同的过滤条件，导出通过异步任务实现，返回 JobID 后前端轮询查询导出任务状态。导出字段包含漏洞ID、漏洞名称、漏洞等级、VPR评级、漏洞类型、CVE编号、主机名称、实例ID、关联组件&路径、修复时间。

        :param request: Request instance for CreateVulFixedExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulFixedExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulFixedExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulFixedExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulFixedExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulReScan(self, request):
        r"""创建漏洞重新扫描

        :param request: Request instance for CreateVulReScan.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulReScanRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulReScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulReScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulReScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulScanManual(self, request):
        r"""创建漏洞扫描（一键扫描）

        :param request: Request instance for CreateVulScanManual.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulScanManualRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulScanManualResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulScanManual", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulScanManualResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCSIPMalwareScanTask(self, request):
        r"""CSIP 手动扫描任务删除接口

        :param request: Request instance for DeleteCSIPMalwareScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteCSIPMalwareScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteCSIPMalwareScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCSIPMalwareScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCSIPMalwareScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCosAkAsset(self, request):
        r"""删除已删除的cos ak资产

        :param request: Request instance for DeleteCosAkAsset.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteCosAkAssetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteCosAkAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCosAkAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCosAkAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCosPolicy(self, request):
        r"""删除策略

        :param request: Request instance for DeleteCosPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteCosPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteCosPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCosPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCosPolicyResponse()
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


    def DeleteDspmApplyOrder(self, request):
        r"""删除Dspm申请单

        :param request: Request instance for DeleteDspmApplyOrder.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmApplyOrderRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmApplyOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmApplyOrder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmApplyOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmAssetAccount(self, request):
        r"""删除Dspm资产账号

        :param request: Request instance for DeleteDspmAssetAccount.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmAssetAccountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmAssetAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmAssetAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmAssetAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmBackupLogList(self, request):
        r"""删除备份日志

        :param request: Request instance for DeleteDspmBackupLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmBackupLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmBackupLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmBackupLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmBackupLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmExportTask(self, request):
        r"""删除导出任务

        :param request: Request instance for DeleteDspmExportTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmExportTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyCategory(self, request):
        r"""删除dspm数据识别分类

        :param request: Request instance for DeleteDspmIdentifyCategory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyCategoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyCategory", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyComplianceCategoryRelation(self, request):
        r"""删除dspm数据识别模板分类关联

        :param request: Request instance for DeleteDspmIdentifyComplianceCategoryRelation.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceCategoryRelationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceCategoryRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyComplianceCategoryRelation", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyComplianceCategoryRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyComplianceGroup(self, request):
        r"""删除dspm数据识别模板

        :param request: Request instance for DeleteDspmIdentifyComplianceGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyComplianceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyComplianceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyComplianceRuleRelation(self, request):
        r"""删除dspm数据识别模板数据项关联

        :param request: Request instance for DeleteDspmIdentifyComplianceRuleRelation.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceRuleRelationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceRuleRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyComplianceRuleRelation", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyComplianceRuleRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyLevelGroup(self, request):
        r"""删除dspm数据识别分级组

        :param request: Request instance for DeleteDspmIdentifyLevelGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyLevelGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyLevelGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyLevelGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyLevelGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyRule(self, request):
        r"""删除dspm数据识别数据项

        :param request: Request instance for DeleteDspmIdentifyRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmPersonalIdentify(self, request):
        r"""删除Dspm个人身份id

        :param request: Request instance for DeleteDspmPersonalIdentify.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmPersonalIdentifyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmPersonalIdentifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmPersonalIdentify", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmPersonalIdentifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmRestoreLogList(self, request):
        r"""删除恢复日志

        :param request: Request instance for DeleteDspmRestoreLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmRestoreLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmRestoreLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmRestoreLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmRestoreLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmWhitelistStrategy(self, request):
        r"""删除Dspm白名单策略

        :param request: Request instance for DeleteDspmWhitelistStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmWhitelistStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmWhitelistStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmWhitelistStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmWhitelistStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEDRRules(self, request):
        r"""删除EDR策略

        :param request: Request instance for DeleteEDRRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteEDRRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteEDRRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEDRRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEDRRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEDRScanTask(self, request):
        r"""删除已终止的扫描任务（物理删除主表及明细表）。只允许删除终态任务，只有创建者可操作。

        :param request: Request instance for DeleteEDRScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteEDRScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteEDRScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEDRScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEDRScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIaCAccessToken(self, request):
        r"""删除IaC检测接入Token

        :param request: Request instance for DeleteIaCAccessToken.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteIaCAccessTokenRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteIaCAccessTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIaCAccessToken", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIaCAccessTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIaCFile(self, request):
        r"""删除IaC检测文件

        :param request: Request instance for DeleteIaCFile.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteIaCFileRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteIaCFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIaCFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIaCFileResponse()
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


    def DeleteVulWhitelist(self, request):
        r"""删除漏洞白名单

        :param request: Request instance for DeleteVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAgentAssetList(self, request):
        r"""获取 AI agent 资产列表

        :param request: Request instance for DescribeAIAgentAssetList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentAssetListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAgentAssetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAgentAssetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAILinkSetting(self, request):
        r"""查询AI-Link智链引擎配置

        :param request: Request instance for DescribeAILinkSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAILinkSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAILinkSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAILinkSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAILinkSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAKAnalysisDetail(self, request):
        r"""访问密钥告警记录AI分析结果详情

        :param request: Request instance for DescribeAKAnalysisDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAKAnalysisDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAKAnalysisDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAKAnalysisDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAKAnalysisDetailResponse()
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


    def DescribeAssumeRole(self, request):
        r"""查询是否绑定角色

        :param request: Request instance for DescribeAssumeRole.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssumeRoleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssumeRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssumeRole", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssumeRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBucketInvokeIpList(self, request):
        r"""查看存储桶调用源ip列表

        :param request: Request instance for DescribeBucketInvokeIpList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBucketInvokeIpListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBucketInvokeIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBucketInvokeIpList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBucketInvokeIpListResponse()
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


    def DescribeCLSLogIndexV3(self, request):
        r"""获取日志索引信息

        :param request: Request instance for DescribeCLSLogIndexV3.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCLSLogIndexV3Request`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCLSLogIndexV3Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCLSLogIndexV3", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCLSLogIndexV3Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCLSLogListV3(self, request):
        r"""日志分析检索接口v3

        :param request: Request instance for DescribeCLSLogListV3.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCLSLogListV3Request`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCLSLogListV3Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCLSLogListV3", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCLSLogListV3Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSIPMalwareScanTaskDetail(self, request):
        r"""CSIP 扫描任务主机详情接口

        :param request: Request instance for DescribeCSIPMalwareScanTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPMalwareScanTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPMalwareScanTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSIPMalwareScanTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSIPMalwareScanTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSIPMalwareScanTaskProgress(self, request):
        r"""CSIP 手动扫描进度查询接口

        :param request: Request instance for DescribeCSIPMalwareScanTaskProgress.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPMalwareScanTaskProgressRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPMalwareScanTaskProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSIPMalwareScanTaskProgress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSIPMalwareScanTaskProgressResponse()
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


    def DescribeCWPMachineDetail(self, request):
        r"""主机详情

        :param request: Request instance for DescribeCWPMachineDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachineDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachineDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPMachineDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPMachineDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPMachines(self, request):
        r"""主机列表

        :param request: Request instance for DescribeCWPMachines.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachinesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPMachinesResponse()
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
        r"""检查视角下云资源配置风险列表

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


    def DescribeCosAccessPermission(self, request):
        r"""查看cos桶访问权限信息

        :param request: Request instance for DescribeCosAccessPermission.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAccessPermissionRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAccessPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAccessPermission", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAccessPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosAccessPermissions(self, request):
        r"""查看对象存储访问权限列表

        :param request: Request instance for DescribeCosAccessPermissions.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAccessPermissionsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAccessPermissionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAccessPermissions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAccessPermissionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosActionList(self, request):
        r"""查看COS接口列表

        :param request: Request instance for DescribeCosActionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosActionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosActionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosActionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosActionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosAkAsset(self, request):
        r"""查看ak资产列表信息

        :param request: Request instance for DescribeCosAkAsset.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAkAssetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAkAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAkAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAkAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosAkInvokeIpList(self, request):
        r"""查看存储桶调用源ip列表

        :param request: Request instance for DescribeCosAkInvokeIpList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAkInvokeIpListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAkInvokeIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAkInvokeIpList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAkInvokeIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosAlarmList(self, request):
        r"""查看告警列表

        :param request: Request instance for DescribeCosAlarmList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAlarmListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAlarmListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAlarmList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAlarmListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosAlarmTrendData(self, request):
        r"""每日告警新增数据

        :param request: Request instance for DescribeCosAlarmTrendData.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAlarmTrendDataRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAlarmTrendDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAlarmTrendData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAlarmTrendDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosAsset(self, request):
        r"""查看cos资产列表

        :param request: Request instance for DescribeCosAsset.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAssetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosAssetSyncTask(self, request):
        r"""获取对应appid对应的当前正在扫描的taskid

        :param request: Request instance for DescribeCosAssetSyncTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAssetSyncTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAssetSyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAssetSyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAssetSyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosAuditAppIdList(self, request):
        r"""查看该appid下已购买的appid集合

        :param request: Request instance for DescribeCosAuditAppIdList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAuditAppIdListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAuditAppIdListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAuditAppIdList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAuditAppIdListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosAuditDictionaryList(self, request):
        r"""查询cos审计字典信息列表

        :param request: Request instance for DescribeCosAuditDictionaryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAuditDictionaryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAuditDictionaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAuditDictionaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAuditDictionaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosAuditPayInfo(self, request):
        r"""获取审计支付信息

        :param request: Request instance for DescribeCosAuditPayInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosAuditPayInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosAuditPayInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosAuditPayInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosAuditPayInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosBucketBillingInfo(self, request):
        r"""获取存储桶计费信息

        :param request: Request instance for DescribeCosBucketBillingInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosBucketBillingInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosBucketBillingInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosBucketBillingInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosBucketBillingInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosBucketList(self, request):
        r"""获取存储桶信息

        :param request: Request instance for DescribeCosBucketList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosBucketListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosBucketListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosBucketList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosBucketListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosBucketRisk(self, request):
        r"""查看风险资产视角

        :param request: Request instance for DescribeCosBucketRisk.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosBucketRiskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosBucketRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosBucketRisk", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosBucketRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosIdentifyFileList(self, request):
        r"""查询cos文件数据识别结果列表

        :param request: Request instance for DescribeCosIdentifyFileList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosIdentifyFileListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosIdentifyFileListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosIdentifyFileList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosIdentifyFileListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosInvokeUa(self, request):
        r"""查看调用记录关联的文件信息

        :param request: Request instance for DescribeCosInvokeUa.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosInvokeUaRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosInvokeUaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosInvokeUa", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosInvokeUaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosIpInvokeLog(self, request):
        r"""查看cos调用日志

        :param request: Request instance for DescribeCosIpInvokeLog.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosIpInvokeLogRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosIpInvokeLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosIpInvokeLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosIpInvokeLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosIpInvokeRecordFile(self, request):
        r"""查看调用记录关联的文件信息

        :param request: Request instance for DescribeCosIpInvokeRecordFile.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosIpInvokeRecordFileRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosIpInvokeRecordFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosIpInvokeRecordFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosIpInvokeRecordFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosObjectScanTask(self, request):
        r"""查询cos风险文件扫描任务

        :param request: Request instance for DescribeCosObjectScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosObjectScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosObjectScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosObjectScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosObjectScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosOverview(self, request):
        r"""cos概览信息

        :param request: Request instance for DescribeCosOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosPolicy(self, request):
        r"""获取策略列表信息

        :param request: Request instance for DescribeCosPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosRiskActionList(self, request):
        r"""风险接口列表信息

        :param request: Request instance for DescribeCosRiskActionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosRiskActionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosRiskActionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosRiskActionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosRiskActionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosRiskEvidence(self, request):
        r"""查看风险证据以及描述

        :param request: Request instance for DescribeCosRiskEvidence.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosRiskEvidenceRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosRiskEvidenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosRiskEvidence", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosRiskEvidenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosRiskScanTask(self, request):
        r"""查看存储桶扫描任务详情

        :param request: Request instance for DescribeCosRiskScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosRiskScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosRiskScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosRiskScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosRiskScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosRoleAccessPermission(self, request):
        r"""查看cos桶访问权限信息

        :param request: Request instance for DescribeCosRoleAccessPermission.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosRoleAccessPermissionRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosRoleAccessPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosRoleAccessPermission", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosRoleAccessPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosRoleAccessPermissions(self, request):
        r"""获取存储桶角色权限列表

        :param request: Request instance for DescribeCosRoleAccessPermissions.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosRoleAccessPermissionsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosRoleAccessPermissionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosRoleAccessPermissions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosRoleAccessPermissionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosSourceIp(self, request):
        r"""调用源ip列表

        :param request: Request instance for DescribeCosSourceIp.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCosSourceIpRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCosSourceIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosSourceIp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosSourceIpResponse()
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


    def DescribeDspmAccessRecord(self, request):
        r"""查询Dspm访问记录

        :param request: Request instance for DescribeDspmAccessRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAccessRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAccessRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAccessTopologyAccounts(self, request):
        r"""查询Dspm访问拓扑账号列表

        :param request: Request instance for DescribeDspmAccessTopologyAccounts.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyAccountsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAccessTopologyAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAccessTopologyAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAccessTopologyAssets(self, request):
        r"""查询Dspm访问拓扑资产列表

        :param request: Request instance for DescribeDspmAccessTopologyAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAccessTopologyAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAccessTopologyAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAccessTopologyIps(self, request):
        r"""查询Dspm访问拓扑ip列表

        :param request: Request instance for DescribeDspmAccessTopologyIps.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyIpsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAccessTopologyIps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAccessTopologyIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmApplyHistory(self, request):
        r"""查询Dspm申请历史

        :param request: Request instance for DescribeDspmApplyHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApplyHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApplyHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmApplyHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmApplyHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmApplyOrderList(self, request):
        r"""查询Dspm申请单列表

        :param request: Request instance for DescribeDspmApplyOrderList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApplyOrderListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApplyOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmApplyOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmApplyOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmApproveHistory(self, request):
        r"""查询Dspm审批历史

        :param request: Request instance for DescribeDspmApproveHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApproveHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApproveHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmApproveHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmApproveHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmApproveOrderList(self, request):
        r"""查询Dspm审批单列表

        :param request: Request instance for DescribeDspmApproveOrderList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApproveOrderListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApproveOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmApproveOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmApproveOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetAccessTopology(self, request):
        r"""查询Dspm资产访问拓扑

        :param request: Request instance for DescribeDspmAssetAccessTopology.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccessTopologyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccessTopologyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetAccessTopology", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetAccessTopologyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetAccountIdentify(self, request):
        r"""查询Dspm资产账号身份信息

        :param request: Request instance for DescribeDspmAssetAccountIdentify.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountIdentifyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountIdentifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetAccountIdentify", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetAccountIdentifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetAccountPresetPrivileges(self, request):
        r"""查询Dspm资产账号预设特权信息

        :param request: Request instance for DescribeDspmAssetAccountPresetPrivileges.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountPresetPrivilegesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountPresetPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetAccountPresetPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetAccountPresetPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetAccountRecycledPrivileges(self, request):
        r"""查询Dspm资产账号回收后特权信息

        :param request: Request instance for DescribeDspmAssetAccountRecycledPrivileges.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountRecycledPrivilegesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountRecycledPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetAccountRecycledPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetAccountRecycledPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetAccounts(self, request):
        r"""查询Dspm资产账号列表

        :param request: Request instance for DescribeDspmAssetAccounts.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetDatabaseList(self, request):
        r"""查询资产数据库信息

        :param request: Request instance for DescribeDspmAssetDatabaseList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetDatabaseListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetDatabaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetDatabaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetDatabaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetDatabases(self, request):
        r"""查询Dspm资产数据库列表

        :param request: Request instance for DescribeDspmAssetDatabases.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetDatabasesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetFieldList(self, request):
        r"""查询dspm资产字段信息

        :param request: Request instance for DescribeDspmAssetFieldList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetFieldListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetFieldListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetFieldList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetFieldListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetFieldSamples(self, request):
        r"""查询dspm资产字段样本值

        :param request: Request instance for DescribeDspmAssetFieldSamples.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetFieldSamplesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetFieldSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetFieldSamples", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetFieldSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetIdentifyInfoList(self, request):
        r"""查询dspm资产数据识别信息列表

        :param request: Request instance for DescribeDspmAssetIdentifyInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetIdentifyInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetIdentifyInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetIdentifyInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetIdentifyInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetIds(self, request):
        r"""查询Dspm资产id列表

        :param request: Request instance for DescribeDspmAssetIds.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetIdsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetLoginCredential(self, request):
        r"""查询Dspm资产登录凭据

        :param request: Request instance for DescribeDspmAssetLoginCredential.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetLoginCredentialRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetLoginCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetLoginCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetLoginCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetSecurityAnalyseStatus(self, request):
        r"""查询Dspm资产安全分析状态

        :param request: Request instance for DescribeDspmAssetSecurityAnalyseStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetSecurityAnalyseStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetSecurityAnalyseStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetSecurityAnalyseStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetSecurityAnalyseStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetSupportedPrivileges(self, request):
        r"""查询Dspm资产支持的权限

        :param request: Request instance for DescribeDspmAssetSupportedPrivileges.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetSupportedPrivilegesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetSupportedPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetSupportedPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetSupportedPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetTableList(self, request):
        r"""查询资产表信息

        :param request: Request instance for DescribeDspmAssetTableList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetTableListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetTableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetTableList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetTableListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssets(self, request):
        r"""查询Dspm资产列表

        :param request: Request instance for DescribeDspmAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmBackupLogList(self, request):
        r"""查询备份日志列表

        :param request: Request instance for DescribeDspmBackupLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmBackupLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmBackupLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmBackupLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmBackupLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmBackupSetting(self, request):
        r"""查询日志备份配置

        :param request: Request instance for DescribeDspmBackupSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmBackupSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmBackupSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmBackupSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmBackupSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmDictionaryList(self, request):
        r"""查询dspm字典信息列表

        :param request: Request instance for DescribeDspmDictionaryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmDictionaryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmDictionaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmDictionaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmDictionaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmExportTask(self, request):
        r"""查询导出任务

        :param request: Request instance for DescribeDspmExportTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmExportTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyCategoryList(self, request):
        r"""查询dspm数据识别分类列表

        :param request: Request instance for DescribeDspmIdentifyCategoryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyCategoryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyComplianceCategoryRuleList(self, request):
        r"""查询dspm数据识别模板分类关联数据项列表

        :param request: Request instance for DescribeDspmIdentifyComplianceCategoryRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceCategoryRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceCategoryRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyComplianceCategoryRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyComplianceCategoryRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyComplianceGroupDetail(self, request):
        r"""查询dspm识别模板详情

        :param request: Request instance for DescribeDspmIdentifyComplianceGroupDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceGroupDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceGroupDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyComplianceGroupDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyComplianceGroupDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyComplianceGroupList(self, request):
        r"""查询dspm数据识别模板列表

        :param request: Request instance for DescribeDspmIdentifyComplianceGroupList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceGroupListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyComplianceGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyComplianceGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyDistributionStatistics(self, request):
        r"""查询dspm数据识别分布统计

        :param request: Request instance for DescribeDspmIdentifyDistributionStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyDistributionStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyDistributionStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyDistributionStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyDistributionStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyIdList(self, request):
        r"""查询Dspm身份id列表

        :param request: Request instance for DescribeDspmIdentifyIdList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyIdListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyIdListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyIdList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyIdListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyInfo(self, request):
        r"""查询Dspm身份信息

        :param request: Request instance for DescribeDspmIdentifyInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyInfoList(self, request):
        r"""查询Dspm身份信息列表

        :param request: Request instance for DescribeDspmIdentifyInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyLevelGroupList(self, request):
        r"""查询dspm数据识别分级组列表

        :param request: Request instance for DescribeDspmIdentifyLevelGroupList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyLevelGroupListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyLevelGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyLevelGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyLevelGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyRuleDetail(self, request):
        r"""查询dspm数据识别数据项详情

        :param request: Request instance for DescribeDspmIdentifyRuleDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyRuleList(self, request):
        r"""查询dspm数据识别数据项列表

        :param request: Request instance for DescribeDspmIdentifyRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyRuleTestResult(self, request):
        r"""查询dspm数据识别数据项验证结果

        :param request: Request instance for DescribeDspmIdentifyRuleTestResult.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleTestResultRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleTestResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyRuleTestResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyRuleTestResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmLogList(self, request):
        r"""查询日志列表信息

        :param request: Request instance for DescribeDspmLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmPayInfo(self, request):
        r"""获取已购Dspm订单信息

        :param request: Request instance for DescribeDspmPayInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPayInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPayInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmPayInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmPayInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmPersonApplyHistory(self, request):
        r"""查询Dspm访客申请记录

        :param request: Request instance for DescribeDspmPersonApplyHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPersonApplyHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPersonApplyHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmPersonApplyHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmPersonApplyHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmPersonalIdentifyList(self, request):
        r"""查询Dspm个人身份信息列表

        :param request: Request instance for DescribeDspmPersonalIdentifyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPersonalIdentifyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPersonalIdentifyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmPersonalIdentifyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmPersonalIdentifyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmRisk(self, request):
        r"""查询Dspm风险记录

        :param request: Request instance for DescribeDspmRisk.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmRisk", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmRiskDetail(self, request):
        r"""查询Dspm风险详情

        :param request: Request instance for DescribeDspmRiskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmRiskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmRiskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmRiskStrategy(self, request):
        r"""查询Dspm风险策略

        :param request: Request instance for DescribeDspmRiskStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmRiskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmRiskStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmRiskStrategyGroup(self, request):
        r"""查询Dspm风险分组策略

        :param request: Request instance for DescribeDspmRiskStrategyGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskStrategyGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskStrategyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmRiskStrategyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmRiskStrategyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmRiskTendency(self, request):
        r"""查询Dspm风险趋势

        :param request: Request instance for DescribeDspmRiskTendency.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskTendencyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmRiskTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmRiskTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmStatistics(self, request):
        r"""查询Dspm统计信息

        :param request: Request instance for DescribeDspmStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmSupportedAssetType(self, request):
        r"""查询Dspm支持的资产类型信息

        :param request: Request instance for DescribeDspmSupportedAssetType.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSupportedAssetTypeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSupportedAssetTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmSupportedAssetType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmSupportedAssetTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmSyncAssetsStatus(self, request):
        r"""查询Dspm同步资产状态

        :param request: Request instance for DescribeDspmSyncAssetsStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSyncAssetsStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSyncAssetsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmSyncAssetsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmSyncAssetsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmSyncUsersStatus(self, request):
        r"""查询Dspm同步用户状态

        :param request: Request instance for DescribeDspmSyncUsersStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSyncUsersStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSyncUsersStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmSyncUsersStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmSyncUsersStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmWhitelistStrategy(self, request):
        r"""查询Dspm白名单策略

        :param request: Request instance for DescribeDspmWhitelistStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmWhitelistStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmWhitelistStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmWhitelistStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmWhitelistStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEDRRuleList(self, request):
        r"""获取EDR策略列表

        :param request: Request instance for DescribeEDRRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEDRRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEDRRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEDRRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEDRRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEDRScanRecordList(self, request):
        r"""查询扫描任务列表。Filter.Filters支持Name：Keyword(模糊OperatorType=9)、ScanType(MANUAL/CYCLE)、TaskType(HOST/CONTAINER)、Status(WAIT/SCANNING/FINISHED/FAILED/CANCELED)、AppId(账号)。

        :param request: Request instance for DescribeEDRScanRecordList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEDRScanRecordListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEDRScanRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEDRScanRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEDRScanRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEDRScanTaskDetail(self, request):
        r"""查询扫描任务详情。Filter.Filters支持Name：Status（资产扫描状态，OperatorType=7 IN匹配，取值WAIT/SCANNING/FINISHED/FAILED）。

        :param request: Request instance for DescribeEDRScanTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEDRScanTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEDRScanTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEDRScanTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEDRScanTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertCountForAsset(self, request):
        r"""获取EDR告警数量统计，供资产模块调用。根据传入的MemberId和InstanceIDs，查询EDR告警表并返回告警记录条数信息。当InstanceIDs为空时返回汇总统计，非空时按InstanceIDs粒度分别返回统计。

        :param request: Request instance for DescribeEdrAlertCountForAsset.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertCountForAssetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertCountForAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertCountForAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertCountForAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertCountForContainer(self, request):
        r"""容器场景告警数量统计

        :param request: Request instance for DescribeEdrAlertCountForContainer.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertCountForContainerRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertCountForContainerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertCountForContainer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertCountForContainerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertInfo(self, request):
        r"""获取EDR告警详情，包含告警内容JSON、资产富化、情报富化等完整信息

        :param request: Request instance for DescribeEdrAlertInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertList(self, request):
        r"""获取EDR告警列表

        :param request: Request instance for DescribeEdrAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertMultiAttackStages(self, request):
        r"""EDR告警多攻击阶段查询

        :param request: Request instance for DescribeEdrAlertMultiAttackStages.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertMultiAttackStagesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertMultiAttackStagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertMultiAttackStages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertMultiAttackStagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertSummary(self, request):
        r"""获取EDR告警统计

        :param request: Request instance for DescribeEdrAlertSummary.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertSummaryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrExportJobDownloadURL(self, request):
        r"""获取EDR导出下载链接

        :param request: Request instance for DescribeEdrExportJobDownloadURL.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExportJobDownloadURLRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExportJobDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrExportJobDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrExportJobDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrExportJobList(self, request):
        r"""导出EDR任务列表

        :param request: Request instance for DescribeEdrExportJobList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExportJobListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExportJobListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrExportJobList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrExportJobListResponse()
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


    def DescribeHostKBRiskList(self, request):
        r"""获取主机kb风险列表

        :param request: Request instance for DescribeHostKBRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeHostKBRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeHostKBRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostKBRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostKBRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostVulItemVPRInfo(self, request):
        r"""获取主机漏洞VPR信息

        :param request: Request instance for DescribeHostVulItemVPRInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulItemVPRInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulItemVPRInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostVulItemVPRInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostVulItemVPRInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostVulOverview(self, request):
        r"""获取主机漏洞概览

        :param request: Request instance for DescribeHostVulOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostVulOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostVulOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostVulRiskList(self, request):
        r"""获取主机漏洞风险列表

        :param request: Request instance for DescribeHostVulRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostVulRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostVulRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIaCFileList(self, request):
        r"""获取IaC检测文件列表

        :param request: Request instance for DescribeIaCFileList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIaCFileList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIaCFileListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIaCFileOverview(self, request):
        r"""获取IaC检测文件概览

        :param request: Request instance for DescribeIaCFileOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIaCFileOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIaCFileOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIaCFileReport(self, request):
        r"""获取IaC检测文件报告

        :param request: Request instance for DescribeIaCFileReport.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileReportRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIaCFileReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIaCFileReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIaCTokenList(self, request):
        r"""获取IaC检测接入Token列表

        :param request: Request instance for DescribeIaCTokenList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeIaCTokenListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeIaCTokenListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIaCTokenList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIaCTokenListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpInvokeRecord(self, request):
        r"""对象存储异常检测调用记录信息

        :param request: Request instance for DescribeIpInvokeRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeIpInvokeRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeIpInvokeRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpInvokeRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpInvokeRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpInvokeRecordDetail(self, request):
        r"""ip访问列表详情信息

        :param request: Request instance for DescribeIpInvokeRecordDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeIpInvokeRecordDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeIpInvokeRecordDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpInvokeRecordDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpInvokeRecordDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKBDetail(self, request):
        r"""根据用户输入的 KB 内部 ID 查询单个 Windows KB 补丁的详情信息，返回 KB 基本信息、发布时间、是否需要重启，以及该 KB 关联的漏洞列表。

        :param request: Request instance for DescribeKBDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeKBDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeKBDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKBDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKBDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKBUpdatableMachineList(self, request):
        r"""查询指定KB补丁可以更新的主机列表。用于Windows系统补丁修复场景，在用户提交KB补丁更新任务前，查询哪些主机缺少该补丁且支持自动更新。

        :param request: Request instance for DescribeKBUpdatableMachineList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeKBUpdatableMachineListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeKBUpdatableMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKBUpdatableMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKBUpdatableMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKeySandboxCredential(self, request):
        r"""查询凭证详情，返回凭证元数据和打码后的凭据数据。access类型返回Access数组（Key原文、Value打码），sts类型返回STS对象（System原文、SecretID和SecretKey打码）

        :param request: Request instance for DescribeKeySandboxCredential.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeKeySandboxCredentialRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeKeySandboxCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKeySandboxCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeySandboxCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKeySandboxCredentialList(self, request):
        r"""查询凭证列表

        :param request: Request instance for DescribeKeySandboxCredentialList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeKeySandboxCredentialListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeKeySandboxCredentialListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKeySandboxCredentialList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeySandboxCredentialListResponse()
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


    def DescribeNetAttackSetting(self, request):
        r"""查询网络攻击检测开关及资产范围配置

        :param request: Request instance for DescribeNetAttackSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNetAttackSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNetAttackSettingResponse`

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


    def DescribeNotifyAssetConfig(self, request):
        r"""获取通知资产范围配置

        :param request: Request instance for DescribeNotifyAssetConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNotifyAssetConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNotifyAssetConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotifyAssetConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotifyAssetConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotifySetting(self, request):
        r"""获取通知设置

        :param request: Request instance for DescribeNotifySetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotifySetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotifySettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotifySettingAlert(self, request):
        r"""获取告警中心通知高级配置

        :param request: Request instance for DescribeNotifySettingAlert.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingAlertRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingAlertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotifySettingAlert", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotifySettingAlertResponse()
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


    def DescribePolicyHitData(self, request):
        r"""按日期查看策略命中详情

        :param request: Request instance for DescribePolicyHitData.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePolicyHitDataRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePolicyHitDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyHitData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyHitDataResponse()
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


    def DescribeReverseShellSystemPolicyConfig(self, request):
        r"""查询反弹Shell内网告警与资产范围配置

        :param request: Request instance for DescribeReverseShellSystemPolicyConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeReverseShellSystemPolicyConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeReverseShellSystemPolicyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellSystemPolicyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellSystemPolicyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskBucketList(self, request):
        r"""查看风险关联的存储桶信息

        :param request: Request instance for DescribeRiskBucketList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskBucketListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskBucketListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskBucketList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskBucketListResponse()
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


    def DescribeRiskItemList(self, request):
        r"""获取风险项视角列表

        :param request: Request instance for DescribeRiskItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskItemListResponse()
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


    def DescribeRiskTrendData(self, request):
        r"""查看风险趋势图

        :param request: Request instance for DescribeRiskTrendData.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskTrendDataRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskTrendDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskTrendData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskTrendDataResponse()
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


    def DescribeSkillScanPayInfo(self, request):
        r"""查询 Skill 安全检测计费信息，包括订单状态、总配额、已消耗配额、到期时间、支付模式等。无订单时返回零值（仅含 TimeNow 和 BetaEndTime）。试用订单通过 ModifyTrialStatus(Module=9) 领取，正式订单通过计费系统创建。

        :param request: Request instance for DescribeSkillScanPayInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanPayInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanPayInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillScanPayInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillScanPayInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillScanResult(self, request):
        r"""查询 Skill 安全检测结果。调用 CreateSkillScan 成功后使用返回的 ContentHash + EngineVersion 轮询本接口获取结果。上传成功后建议5分钟后首次轮询，如未检测完成之后每隔1分钟轮询一次。响应通过 Status 字段区分四种状态：检测完成（SUCCESS）、检测中（SCANNING）、无记录（NOT_FOUND）、检测失败（FAILED）。注意：检测结果保留90天，超期后将返回 NOT_FOUND。

        :param request: Request instance for DescribeSkillScanResult.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanResultRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillScanResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillScanResultResponse()
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


    def DescribeUserDspmInfoList(self, request):
        r"""获取账号dspm信息列表

        :param request: Request instance for DescribeUserDspmInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUserDspmInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUserDspmInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDspmInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDspmInfoListResponse()
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


    def DescribeVulComponentRelateHost(self, request):
        r"""获取漏洞组件关联主机

        :param request: Request instance for DescribeVulComponentRelateHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulComponentRelateHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulComponentRelateHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulComponentRelateHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulComponentRelateHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixTaskDetail(self, request):
        r"""查询指定漏洞修复任务的详情信息，包含每台主机的修复状态、快照状态等明细数据，支持分页和筛选。

        :param request: Request instance for DescribeVulFixTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixTaskList(self, request):
        r"""分页查询漏洞修复任务记录列表，支持按修复状态、时间范围等条件筛选，展示每个修复任务的概要信息。

        :param request: Request instance for DescribeVulFixTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixableMachineList(self, request):
        r"""查询指定漏洞可以被修复的主机列表。在用户提交修复任务前，需要先查询哪些主机支持自动修复，为用户选择修复目标提供数据支持。

        :param request: Request instance for DescribeVulFixableMachineList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixableMachineListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixableMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixableMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixableMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixedHostDetail(self, request):
        r"""查询某个已修复漏洞在指定主机上的修复详情，包含漏洞基本信息、修复主机信息以及关联组件&路径的详细列表（组件名称、命中版本、关联路径、修复命令）。

        :param request: Request instance for DescribeVulFixedHostDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixedHostDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixedHostDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixedHostDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixedHostDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixedList(self, request):
        r"""查询已被修复的漏洞列表，展示修复成功的漏洞信息及修复情况统计，帮助用户了解修复成效。

        :param request: Request instance for DescribeVulFixedList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixedListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixedListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixedList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixedListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulHostRelateComponent(self, request):
        r"""获取漏洞主机关联组件

        :param request: Request instance for DescribeVulHostRelateComponent.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulHostRelateComponentRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulHostRelateComponentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulHostRelateComponent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulHostRelateComponentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulIgnoreRuleList(self, request):
        r"""获取漏洞忽略列表

        :param request: Request instance for DescribeVulIgnoreRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulIgnoreRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulIgnoreRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulIgnoreRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulIgnoreRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulItemList(self, request):
        r"""获取漏洞列表

        :param request: Request instance for DescribeVulItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulLabelList(self, request):
        r"""获取漏洞标签列表

        :param request: Request instance for DescribeVulLabelList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulLabelListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulLabelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLabelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulLabelListResponse()
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


    def DescribeVulRiskRelateComponent(self, request):
        r"""获取漏洞关联组件

        :param request: Request instance for DescribeVulRiskRelateComponent.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskRelateComponentRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskRelateComponentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulRiskRelateComponent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulRiskRelateComponentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulRiskRelateHost(self, request):
        r"""获取漏洞或KB关联的主机

        :param request: Request instance for DescribeVulRiskRelateHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskRelateHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskRelateHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulRiskRelateHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulRiskRelateHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulScanPeriodic(self, request):
        r"""获取漏洞扫描（周期扫描）

        :param request: Request instance for DescribeVulScanPeriodic.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanPeriodicRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanPeriodicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanPeriodic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanPeriodicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulScanTaskDetail(self, request):
        r"""获取扫描漏洞任务详情

        :param request: Request instance for DescribeVulScanTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulScanTaskList(self, request):
        r"""获取漏洞扫描任务记录

        :param request: Request instance for DescribeVulScanTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanTaskListResponse()
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


    def DownloadDspmExportLog(self, request):
        r"""下载导出日志

        :param request: Request instance for DownloadDspmExportLog.
        :type request: :class:`tencentcloud.csip.v20221121.models.DownloadDspmExportLogRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DownloadDspmExportLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadDspmExportLog", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadDspmExportLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportCSIPMalwareScanTaskDetail(self, request):
        r"""导出CSIP扫描任务主机详情为Excel文件，异步生成后通过DescribeExportMachines查询下载地址

        :param request: Request instance for ExportCSIPMalwareScanTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.ExportCSIPMalwareScanTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ExportCSIPMalwareScanTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportCSIPMalwareScanTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ExportCSIPMalwareScanTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportEDRRules(self, request):
        r"""导出EDR策略列表

        :param request: Request instance for ExportEDRRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.ExportEDRRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ExportEDRRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportEDRRules", params, headers=headers)
            response = json.loads(body)
            model = models.ExportEDRRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAILinkSetting(self, request):
        r"""修改AI-Link智链引擎配置

        :param request: Request instance for ModifyAILinkSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAILinkSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAILinkSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAILinkSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAILinkSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAlarmRiskStatus(self, request):
        r"""修改或者更改处置状态

        :param request: Request instance for ModifyAlarmRiskStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAlarmRiskStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAlarmRiskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmRiskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmRiskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCosAuditBucketMonitorStatus(self, request):
        r"""修改存储桶监测状态

        :param request: Request instance for ModifyCosAuditBucketMonitorStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCosAuditBucketMonitorStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCosAuditBucketMonitorStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCosAuditBucketMonitorStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCosAuditBucketMonitorStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCosAuditMonitorAccount(self, request):
        r"""修改cos审计监测账号

        :param request: Request instance for ModifyCosAuditMonitorAccount.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCosAuditMonitorAccountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCosAuditMonitorAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCosAuditMonitorAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCosAuditMonitorAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCosAuditObjectIdentifyStatus(self, request):
        r"""修改对象存储识别开关

        :param request: Request instance for ModifyCosAuditObjectIdentifyStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCosAuditObjectIdentifyStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCosAuditObjectIdentifyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCosAuditObjectIdentifyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCosAuditObjectIdentifyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCosAuditObjectSampleRate(self, request):
        r"""设置对象存储扫描采样率

        :param request: Request instance for ModifyCosAuditObjectSampleRate.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCosAuditObjectSampleRateRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCosAuditObjectSampleRateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCosAuditObjectSampleRate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCosAuditObjectSampleRateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCosMarkInfo(self, request):
        r"""修改对象存储备注

        :param request: Request instance for ModifyCosMarkInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCosMarkInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCosMarkInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCosMarkInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCosMarkInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAccessRecord(self, request):
        r"""修改Dspm访问管理信息

        :param request: Request instance for ModifyDspmAccessRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAccessRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAccessRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAccessRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAccessRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmApplyingIdentifyComplianceGroup(self, request):
        r"""修改dspm当前应用的数据识别模板

        :param request: Request instance for ModifyDspmApplyingIdentifyComplianceGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmApplyingIdentifyComplianceGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmApplyingIdentifyComplianceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmApplyingIdentifyComplianceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmApplyingIdentifyComplianceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmApproveStatus(self, request):
        r"""修改Dspm审批单状态

        :param request: Request instance for ModifyDspmApproveStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmApproveStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmApproveStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmApproveStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmApproveStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetAccount(self, request):
        r"""修改Dspm资产账号信息

        :param request: Request instance for ModifyDspmAssetAccount.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetAccountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetAccountPrivileges(self, request):
        r"""修改Dspm资产账号权限

        :param request: Request instance for ModifyDspmAssetAccountPrivileges.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetDataScanTask(self, request):
        r"""修改Dspm资产数据扫描任务

        :param request: Request instance for ModifyDspmAssetDataScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetDataScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetDataScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetDataScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetDataScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetDataScanTaskStatus(self, request):
        r"""修改Dspm资产数据扫描任务状态

        :param request: Request instance for ModifyDspmAssetDataScanTaskStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetDataScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetDataScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetDataScanTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetDataScanTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetLogDeliverySwitch(self, request):
        r"""修改Dspm资产日志投递开关

        :param request: Request instance for ModifyDspmAssetLogDeliverySwitch.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetLogDeliverySwitchRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetLogDeliverySwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetLogDeliverySwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetLogDeliverySwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetSecurityAnalysisSwitch(self, request):
        r"""修改Dspm资产日志投递开关

        :param request: Request instance for ModifyDspmAssetSecurityAnalysisSwitch.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetSecurityAnalysisSwitchRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetSecurityAnalysisSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetSecurityAnalysisSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetSecurityAnalysisSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmBackupSetting(self, request):
        r"""修改日志备份设置

        :param request: Request instance for ModifyDspmBackupSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmBackupSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmBackupSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmBackupSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmBackupSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyCategory(self, request):
        r"""修改dspm数据识别分类

        :param request: Request instance for ModifyDspmIdentifyCategory.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyCategoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyCategory", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyComplianceGroup(self, request):
        r"""修改dspm数据识别模板

        :param request: Request instance for ModifyDspmIdentifyComplianceGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyComplianceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyComplianceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyComplianceGroupStatus(self, request):
        r"""修改dspm数据识别模板状态

        :param request: Request instance for ModifyDspmIdentifyComplianceGroupStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceGroupStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceGroupStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyComplianceGroupStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyComplianceGroupStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyComplianceRuleLevelInfo(self, request):
        r"""修改dspm数据识别模板数据项关联级别信息

        :param request: Request instance for ModifyDspmIdentifyComplianceRuleLevelInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceRuleLevelInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceRuleLevelInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyComplianceRuleLevelInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyComplianceRuleLevelInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyInfo(self, request):
        r"""修改Dspm身份信息

        :param request: Request instance for ModifyDspmIdentifyInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyLevelGroup(self, request):
        r"""修改dspm数据识别分级组

        :param request: Request instance for ModifyDspmIdentifyLevelGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyLevelGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyLevelGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyLevelGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyLevelGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyLevelItem(self, request):
        r"""修改dspm数据识别分级信息

        :param request: Request instance for ModifyDspmIdentifyLevelItem.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyLevelItemRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyLevelItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyLevelItem", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyLevelItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyRule(self, request):
        r"""修改dspm数据识别数据项

        :param request: Request instance for ModifyDspmIdentifyRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyRuleStatus(self, request):
        r"""修改dspm数据识别数据项状态

        :param request: Request instance for ModifyDspmIdentifyRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIpInfo(self, request):
        r"""修改DspmIp信息

        :param request: Request instance for ModifyDspmIpInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIpInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIpInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIpInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIpInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmPersonalIdentify(self, request):
        r"""修改Dspm个人身份id

        :param request: Request instance for ModifyDspmPersonalIdentify.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmPersonalIdentifyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmPersonalIdentifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmPersonalIdentify", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmPersonalIdentifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmRestoreLogTask(self, request):
        r"""恢复备份日志

        :param request: Request instance for ModifyDspmRestoreLogTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRestoreLogTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRestoreLogTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmRestoreLogTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmRestoreLogTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmRiskInfo(self, request):
        r"""修改Dspm风险信息

        :param request: Request instance for ModifyDspmRiskInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRiskInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRiskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmRiskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmRiskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmRiskStrategy(self, request):
        r"""修改Dspm风险策略

        :param request: Request instance for ModifyDspmRiskStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRiskStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRiskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmRiskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmRiskStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmWhitelistStrategy(self, request):
        r"""修改Dspm白名单策略

        :param request: Request instance for ModifyDspmWhitelistStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmWhitelistStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmWhitelistStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmWhitelistStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmWhitelistStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEDRRule(self, request):
        r"""编辑或者创建EDR策略

        :param request: Request instance for ModifyEDRRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEDRRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEDRRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEDRRuleStatus(self, request):
        r"""修改EDR策略开关状态

        :param request: Request instance for ModifyEDRRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEDRRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEDRRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEDRRulesAction(self, request):
        r"""批量修改EDR策略动作

        :param request: Request instance for ModifyEDRRulesAction.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRulesActionRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRulesActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEDRRulesAction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEDRRulesActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdrAlertIsolation(self, request):
        r"""EDR告警隔离和恢复

        :param request: Request instance for ModifyEdrAlertIsolation.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertIsolationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertIsolationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdrAlertIsolation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdrAlertIsolationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdrAlertPermanentIgnore(self, request):
        r"""永久忽略EDR多行为告警，将告警对应的主机+规则加入AI-Link永久忽略白名单，后续同类告警将自动丢弃

        :param request: Request instance for ModifyEdrAlertPermanentIgnore.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertPermanentIgnoreRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertPermanentIgnoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdrAlertPermanentIgnore", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdrAlertPermanentIgnoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdrAlertStatus(self, request):
        r"""EDR告警状态处置

        :param request: Request instance for ModifyEdrAlertStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdrAlertStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdrAlertStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIaCTokenPeriod(self, request):
        r"""修改IaC检测接入Token存储周期

        :param request: Request instance for ModifyIaCTokenPeriod.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyIaCTokenPeriodRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyIaCTokenPeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIaCTokenPeriod", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIaCTokenPeriodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMachineRemark(self, request):
        r"""修改主机资产备注信息

        :param request: Request instance for ModifyMachineRemark.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyMachineRemarkRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyMachineRemarkResponse`

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


    def ModifyNetAttackSetting(self, request):
        r"""修改网络攻击检测开关及资产范围配置

        :param request: Request instance for ModifyNetAttackSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNetAttackSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNetAttackSettingResponse`

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


    def ModifyNotifyAssetConfig(self, request):
        r"""修改通知资产范围配置

        :param request: Request instance for ModifyNotifyAssetConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyAssetConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyAssetConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifyAssetConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifyAssetConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotifySetting(self, request):
        r"""修改通知设置

        :param request: Request instance for ModifyNotifySetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifySetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifySettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotifySettingAlert(self, request):
        r"""修改告警中心通知高级配置

        :param request: Request instance for ModifyNotifySettingAlert.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingAlertRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingAlertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifySettingAlert", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifySettingAlertResponse()
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


    def ModifyPolicyStatus(self, request):
        r"""修改策略状态

        :param request: Request instance for ModifyPolicyStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyPolicyStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReverseShellSystemPolicyConfig(self, request):
        r"""修改反弹Shell内网告警与资产范围配置

        :param request: Request instance for ModifyReverseShellSystemPolicyConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyReverseShellSystemPolicyConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyReverseShellSystemPolicyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReverseShellSystemPolicyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReverseShellSystemPolicyConfigResponse()
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


    def ModifyVulScanPeriodic(self, request):
        r"""修改漏洞扫描（周期扫描）

        :param request: Request instance for ModifyVulScanPeriodic.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyVulScanPeriodicRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyVulScanPeriodicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulScanPeriodic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVulScanPeriodicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVulWhitelistConfig(self, request):
        r"""修改漏洞白名单配置

        :param request: Request instance for ModifyVulWhitelistConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyVulWhitelistConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyVulWhitelistConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulWhitelistConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVulWhitelistConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVulWhitelistSwitch(self, request):
        r"""修改漏洞白名单开关

        :param request: Request instance for ModifyVulWhitelistSwitch.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyVulWhitelistSwitchRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyVulWhitelistSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulWhitelistSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVulWhitelistSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetDspmAssetAccountPassword(self, request):
        r"""重置Dspm资产账号密码

        :param request: Request instance for ResetDspmAssetAccountPassword.
        :type request: :class:`tencentcloud.csip.v20221121.models.ResetDspmAssetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ResetDspmAssetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetDspmAssetAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetDspmAssetAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryDspmExportLog(self, request):
        r"""RetryExportLog

        :param request: Request instance for RetryDspmExportLog.
        :type request: :class:`tencentcloud.csip.v20221121.models.RetryDspmExportLogRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.RetryDspmExportLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryDspmExportLog", params, headers=headers)
            response = json.loads(body)
            model = models.RetryDspmExportLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevertDspmAssetAccount(self, request):
        r"""恢复Dspm资产账号

        :param request: Request instance for RevertDspmAssetAccount.
        :type request: :class:`tencentcloud.csip.v20221121.models.RevertDspmAssetAccountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.RevertDspmAssetAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevertDspmAssetAccount", params, headers=headers)
            response = json.loads(body)
            model = models.RevertDspmAssetAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanCSIPTaskAgain(self, request):
        r"""CSIP 手动扫描任务删除接口

        :param request: Request instance for ScanCSIPTaskAgain.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanCSIPTaskAgainRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanCSIPTaskAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanCSIPTaskAgain", params, headers=headers)
            response = json.loads(body)
            model = models.ScanCSIPTaskAgainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanEDRTaskAgain(self, request):
        r"""基于原任务配置新建扫描任务。AssetId为空时从TaskId获取全部资产信息；AssetId非空时仅含该单资产。

        :param request: Request instance for ScanEDRTaskAgain.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanEDRTaskAgainRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanEDRTaskAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanEDRTaskAgain", params, headers=headers)
            response = json.loads(body)
            model = models.ScanEDRTaskAgainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendDspmAssetLoginSmsCode(self, request):
        r"""发送Dspm资产访问验证码

        :param request: Request instance for SendDspmAssetLoginSmsCode.
        :type request: :class:`tencentcloud.csip.v20221121.models.SendDspmAssetLoginSmsCodeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.SendDspmAssetLoginSmsCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendDspmAssetLoginSmsCode", params, headers=headers)
            response = json.loads(body)
            model = models.SendDspmAssetLoginSmsCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCSIPManualMalwareScan(self, request):
        r"""CSIP 手动扫描停止接口

        :param request: Request instance for StopCSIPManualMalwareScan.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopCSIPManualMalwareScanRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopCSIPManualMalwareScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCSIPManualMalwareScan", params, headers=headers)
            response = json.loads(body)
            model = models.StopCSIPManualMalwareScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopEDRScanTask(self, request):
        r"""停止或取消扫描任务。SCANNING状态调RPC停止，WAIT状态直接改库取消。只有任务创建者可操作。

        :param request: Request instance for StopEDRScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopEDRScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopEDRScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopEDRScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopEDRScanTaskResponse()
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


    def StopVulScanTask(self, request):
        r"""停止漏洞扫描（任务扫描）

        :param request: Request instance for StopVulScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopVulScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopVulScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopVulScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopVulScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncDspmAssets(self, request):
        r"""同步dspm支持的资产

        :param request: Request instance for SyncDspmAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.SyncDspmAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.SyncDspmAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncDspmAssets", params, headers=headers)
            response = json.loads(body)
            model = models.SyncDspmAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncDspmUsers(self, request):
        r"""同步dspm用户列表

        :param request: Request instance for SyncDspmUsers.
        :type request: :class:`tencentcloud.csip.v20221121.models.SyncDspmUsersRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.SyncDspmUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncDspmUsers", params, headers=headers)
            response = json.loads(body)
            model = models.SyncDspmUsersResponse()
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


    def VerifyDspmAssetLoginCode(self, request):
        r"""验证Dspm资产登录验证码

        :param request: Request instance for VerifyDspmAssetLoginCode.
        :type request: :class:`tencentcloud.csip.v20221121.models.VerifyDspmAssetLoginCodeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.VerifyDspmAssetLoginCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyDspmAssetLoginCode", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyDspmAssetLoginCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))