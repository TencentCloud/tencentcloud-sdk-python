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


    def AccessAIAnalysisSMTP(self, request):
        r"""创建/修改SMTP邮箱接入请求

        :param request: Request instance for AccessAIAnalysisSMTP.
        :type request: :class:`tencentcloud.csip.v20221121.models.AccessAIAnalysisSMTPRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AccessAIAnalysisSMTPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AccessAIAnalysisSMTP", params, headers=headers)
            response = json.loads(body)
            model = models.AccessAIAnalysisSMTPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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


    def AddImageRegistry(self, request):
        r"""添加镜像仓库信息

        :param request: Request instance for AddImageRegistry.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddImageRegistryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddImageRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddImageRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.AddImageRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddLoginWhiteLists(self, request):
        r"""批量添加异地登录白名单

        :param request: Request instance for AddLoginWhiteLists.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddLoginWhiteListsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddLoginWhiteListsResponse`

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


    def BatchModifyBaselinePolicy(self, request):
        r"""批量修改基线策略的“周期扫描配置 / 自动同步新增检测项 / 检测项命中配置 / 自定义检测项”等设置。仅修改请求中传入的字段。

        :param request: Request instance for BatchModifyBaselinePolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.BatchModifyBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BatchModifyBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyImageRegistryTimedScanTaskConfig(self, request):
        r"""批量修改镜像仓库定时扫描任务配置

        :param request: Request instance for BatchModifyImageRegistryTimedScanTaskConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageRegistryTimedScanTaskConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageRegistryTimedScanTaskConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyImageRegistryTimedScanTaskConfig", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyImageRegistryTimedScanTaskConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyImageSensitiveWhitelist(self, request):
        r"""批量修改容器镜像敏感信息白名单

        :param request: Request instance for BatchModifyImageSensitiveWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageSensitiveWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageSensitiveWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyImageSensitiveWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyImageSensitiveWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyImageVirusWhitelist(self, request):
        r"""批量修改镜像木马白名单

        :param request: Request instance for BatchModifyImageVirusWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageVirusWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageVirusWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyImageVirusWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyImageVirusWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyImageVulWhitelist(self, request):
        r"""批量修改容器镜像漏洞白名单

        :param request: Request instance for BatchModifyImageVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyImageVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyImageVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindClusterOwner(self, request):
        r"""绑定集群负责人

        :param request: Request instance for BindClusterOwner.
        :type request: :class:`tencentcloud.csip.v20221121.models.BindClusterOwnerRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BindClusterOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindClusterOwner", params, headers=headers)
            response = json.loads(body)
            model = models.BindClusterOwnerResponse()
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


    def CheckCWPExposePathPermission(self, request):
        r"""判断当前用户是否旗舰版(适用于主机)

        :param request: Request instance for CheckCWPExposePathPermission.
        :type request: :class:`tencentcloud.csip.v20221121.models.CheckCWPExposePathPermissionRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CheckCWPExposePathPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCWPExposePathPermission", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCWPExposePathPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckImageRegistryInstanceNameDuplicate(self, request):
        r"""检查镜像仓库实例名是否重复

        :param request: Request instance for CheckImageRegistryInstanceNameDuplicate.
        :type request: :class:`tencentcloud.csip.v20221121.models.CheckImageRegistryInstanceNameDuplicateRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CheckImageRegistryInstanceNameDuplicateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckImageRegistryInstanceNameDuplicate", params, headers=headers)
            response = json.loads(body)
            model = models.CheckImageRegistryInstanceNameDuplicateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIsUltimateVersion(self, request):
        r"""判断当前用户是否旗舰版

        :param request: Request instance for CheckIsUltimateVersion.
        :type request: :class:`tencentcloud.csip.v20221121.models.CheckIsUltimateVersionRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CheckIsUltimateVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIsUltimateVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIsUltimateVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckRisk(self, request):
        r"""风险验证示例

        :param request: Request instance for CheckRisk.
        :type request: :class:`tencentcloud.csip.v20221121.models.CheckRiskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CheckRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckRisk", params, headers=headers)
            response = json.loads(body)
            model = models.CheckRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyBaselinePolicy(self, request):
        r"""复制自定义基线策略

        :param request: Request instance for CopyBaselinePolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CopyBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CopyBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CopyBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAISchedule(self, request):
        r"""创建AI 定时任务。

        创建一个新的AI 定时任务，需传入任务名称、执行提示词和触发器配置。创建成功后返回AI 定时任务 ID。

        :param request: Request instance for CreateAISchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAIScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAIScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAISchedule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIScheduleResponse()
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


    def CreateAllAssetsExportJob(self, request):
        r"""创建全部资产导出任务

        :param request: Request instance for CreateAllAssetsExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAllAssetsExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAllAssetsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAllAssetsExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAllAssetsExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetComponentListExportJob(self, request):
        r"""创建镜像资产中组件列表导出任务

        :param request: Request instance for CreateAssetComponentListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetComponentListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetComponentListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetComponentListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetComponentListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetComponentRelatedImageListExportJob(self, request):
        r"""创建镜像仓库组件关联镜像列表导出任务

        :param request: Request instance for CreateAssetComponentRelatedImageListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetComponentRelatedImageListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetComponentRelatedImageListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetComponentRelatedImageListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetComponentRelatedImageListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetFilterView(self, request):
        r"""创建资产搜索视图

        :param request: Request instance for CreateAssetFilterView.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetFilterViewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetFilterViewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetFilterView", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetFilterViewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetProcessExportJob(self, request):
        r"""创建主机进程列表导出任务

        :param request: Request instance for CreateAssetProcessExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetProcessExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetProcessExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetProcessExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetProcessExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetSyncTask(self, request):
        r"""创建资产同步任务

        :param request: Request instance for CreateAssetSyncTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetSyncTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetSyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetSyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetSyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetTag(self, request):
        r"""创建资产标签

        :param request: Request instance for CreateAssetTag.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetTagRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetTag", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetViewRisksExportJob(self, request):
        r"""创建资产视角下风险列表导出任务示例

        :param request: Request instance for CreateAssetViewRisksExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetViewRisksExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetViewRisksExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetViewRisksExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetViewRisksExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaselineAggregatedItemExportJob(self, request):
        r"""创建基线聚合检测项导出任务。通过 ExportType 选择导出统计结果或风险明细，可按策略、分类等条件限定范围；任务在后台异步执行，完成后可在导出任务列表中下载结果文件。

        :param request: Request instance for CreateBaselineAggregatedItemExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateBaselineAggregatedItemExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateBaselineAggregatedItemExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaselineAggregatedItemExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineAggregatedItemExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaselineFixRecordExportJob(self, request):
        r"""创建基线修复记录导出任务，导出已修复检测项的记录数据（含检测项信息、资产信息、修复时间等）。任务在后台异步执行，完成后可在导出任务列表中下载结果文件。

        :param request: Request instance for CreateBaselineFixRecordExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateBaselineFixRecordExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateBaselineFixRecordExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaselineFixRecordExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineFixRecordExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaselineMainTaskExportJob(self, request):
        r"""创建基线主任务导出任务，导出指定主任务下的检测项与子任务数据。任务在后台异步执行，完成后可在导出任务列表中下载结果文件。

        :param request: Request instance for CreateBaselineMainTaskExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateBaselineMainTaskExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateBaselineMainTaskExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaselineMainTaskExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineMainTaskExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCFGRiskPDFReportExportJob(self, request):
        r"""创建云资源配置检测PDF报告导出任务示例

        :param request: Request instance for CreateCFGRiskPDFReportExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCFGRiskPDFReportExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCFGRiskPDFReportExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCFGRiskPDFReportExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCFGRiskPDFReportExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCFGRisksExportJob(self, request):
        r"""创建资产视角下风险列表导出任务示例

        :param request: Request instance for CreateCFGRisksExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCFGRisksExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCFGRisksExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCFGRisksExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCFGRisksExportJobResponse()
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


    def CreateCheckViewRisksExportJob(self, request):
        r"""创建资产视角下风险列表导出任务示例

        :param request: Request instance for CreateCheckViewRisksExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCheckViewRisksExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCheckViewRisksExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCheckViewRisksExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCheckViewRisksExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudFunctionExportJob(self, request):
        r"""创建云函数导出任务

        :param request: Request instance for CreateCloudFunctionExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCloudFunctionExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCloudFunctionExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudFunctionExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudFunctionExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterAssetSyncTask(self, request):
        r"""创建集群资产同步任务

        :param request: Request instance for CreateClusterAssetSyncTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateClusterAssetSyncTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateClusterAssetSyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterAssetSyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterAssetSyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterContainerListExportJob(self, request):
        r"""创建集群容器列表导出任务

        :param request: Request instance for CreateClusterContainerListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateClusterContainerListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateClusterContainerListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterContainerListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterContainerListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterListExportJob(self, request):
        r"""创建集群列表导出任务

        :param request: Request instance for CreateClusterListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateClusterListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateClusterListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterNamespaceListExportJob(self, request):
        r"""创建集群命名空间列表导出任务。导出字段包含命名空间名称、Labels、创建时间。支持Filter过滤。导出通过异步任务实现，返回JobId后前端轮询查询导出任务状态。

        :param request: Request instance for CreateClusterNamespaceListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateClusterNamespaceListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateClusterNamespaceListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterNamespaceListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterNamespaceListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterNodeListExportJob(self, request):
        r"""创建集群节点列表导出任务。导出字段包含节点ID、节点名称、公网IP、内网IP、节点类型、核数、客户端状态、运行状态。NodeType和ClientStatus、RunStatus均经过国际化翻译。支持Filter过滤（含ClientStatus内存过滤）。导出通过异步任务实现，返回JobId后前端轮询查询导出任务状态。

        :param request: Request instance for CreateClusterNodeListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateClusterNodeListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateClusterNodeListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterNodeListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterNodeListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateComplianceRiskExportJob(self, request):
        r"""创建合规标准聚合视角下风险列表导出任务示例

        :param request: Request instance for CreateComplianceRiskExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateComplianceRiskExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateComplianceRiskExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateComplianceRiskExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateComplianceRiskExportJobResponse()
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


    def CreateDspmAuditFilterStrategy(self, request):
        r"""创建Dspm审计过滤策略

        :param request: Request instance for CreateDspmAuditFilterStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmAuditFilterStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmAuditFilterStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmAuditFilterStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmAuditFilterStrategyResponse()
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


    def CreateDspmResource(self, request):
        r"""创建Dspm实例

        :param request: Request instance for CreateDspmResource.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmResourceRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmResourceResponse()
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


    def CreateDspmRiskStrategy(self, request):
        r"""创建Dspm自定义风险策略

        :param request: Request instance for CreateDspmRiskStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmRiskStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmRiskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmRiskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmRiskStrategyResponse()
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


    def CreateDynamicAssetsExportJob(self, request):
        r"""创建公网资产导出任务

        :param request: Request instance for CreateDynamicAssetsExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDynamicAssetsExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDynamicAssetsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDynamicAssetsExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDynamicAssetsExportJobResponse()
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


    def CreateEdrLessAlertExportJob(self, request):
        r"""创建EDR告警普通导出任务

        :param request: Request instance for CreateEdrLessAlertExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateEdrLessAlertExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateEdrLessAlertExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdrLessAlertExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdrLessAlertExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExposureAutoTagRule(self, request):
        r"""云边界自动打标-创建规则

        :param request: Request instance for CreateExposureAutoTagRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateExposureAutoTagRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateExposureAutoTagRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExposureAutoTagRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExposureAutoTagRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExposuresExportJob(self, request):
        r"""暴露资产导出任务

        :param request: Request instance for CreateExposuresExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateExposuresExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateExposuresExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExposuresExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExposuresExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHighBaseLineRisksExportJob(self, request):
        r"""创建高危基线风险导出任务

        :param request: Request instance for CreateHighBaseLineRisksExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateHighBaseLineRisksExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateHighBaseLineRisksExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHighBaseLineRisksExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHighBaseLineRisksExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHostImageListExportJob(self, request):
        r"""创建本地镜像列表导出任务。导出字段包含镜像ID、镜像名、镜像版本、关联容器数、关联主机数、创建时间、所属账号昵称，以及扫描状态/漏洞/木马/敏感信息等风险字段。支持Filter过滤。导出通过异步任务实现，返回JobId后前端轮询查询导出任务状态。单账号模式下自动排除NickName字段。

        :param request: Request instance for CreateHostImageListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateHostImageListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateHostImageListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHostImageListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostImageListExportJobResponse()
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


    def CreateImageAssetListExportJob(self, request):
        r"""创建镜像资产列表导出任务

        :param request: Request instance for CreateImageAssetListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageAssetListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageAssetListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageAssetListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageAssetListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageAssociatedContainerListExportJob(self, request):
        r"""创建镜像关联容器资产导出任务

        :param request: Request instance for CreateImageAssociatedContainerListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageAssociatedContainerListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageAssociatedContainerListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageAssociatedContainerListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageAssociatedContainerListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageAssociatedHostListExportJob(self, request):
        r"""创建镜像关联主机资产列表导出任务

        :param request: Request instance for CreateImageAssociatedHostListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageAssociatedHostListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageAssociatedHostListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageAssociatedHostListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageAssociatedHostListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageComponentListExportJob(self, request):
        r"""创建镜像组件列表导出任务

        :param request: Request instance for CreateImageComponentListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageComponentListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageComponentListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageComponentListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageComponentListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageLayerVulListExportJob(self, request):
        r"""创建镜像层漏洞列表导出任务

        :param request: Request instance for CreateImageLayerVulListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageLayerVulListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageLayerVulListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageLayerVulListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageLayerVulListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageRegistryConnectivityTask(self, request):
        r"""创建镜像仓库联通性检查任务

        :param request: Request instance for CreateImageRegistryConnectivityTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryConnectivityTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryConnectivityTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageRegistryConnectivityTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageRegistryConnectivityTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageRegistryListExportJob(self, request):
        r"""创建镜像仓库列表导出任务

        :param request: Request instance for CreateImageRegistryListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageRegistryListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageRegistryListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageRegistryScanTask(self, request):
        r"""创建镜像扫描任务

        :param request: Request instance for CreateImageRegistryScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageRegistryScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageRegistryScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageRegistryTimedScanTaskConfig(self, request):
        r"""创建镜像仓库镜像扫描任务配置

        :param request: Request instance for CreateImageRegistryTimedScanTaskConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryTimedScanTaskConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryTimedScanTaskConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageRegistryTimedScanTaskConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageRegistryTimedScanTaskConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageSensitiveInfoListExportJob(self, request):
        r"""创建镜像敏感信息列表导出任务

        :param request: Request instance for CreateImageSensitiveInfoListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageSensitiveInfoListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageSensitiveInfoListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageSensitiveInfoListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageSensitiveInfoListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageSensitiveWhitelist(self, request):
        r"""创建容器镜像敏感信息白名单

        :param request: Request instance for CreateImageSensitiveWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageSensitiveWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageSensitiveWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageSensitiveWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageSensitiveWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageVirusListExportJob(self, request):
        r"""创建镜像木马病毒列表导出任务

        :param request: Request instance for CreateImageVirusListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageVirusListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageVirusListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageVirusListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageVirusListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageVirusWhitelist(self, request):
        r"""创建镜像木马白名单

        :param request: Request instance for CreateImageVirusWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageVirusWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageVirusWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageVirusWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageVirusWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageVulListExportJob(self, request):
        r"""创建镜像漏洞列表导出任务

        :param request: Request instance for CreateImageVulListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageVulListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageVulListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageVulListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageVulListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageVulSummaryListExportJob(self, request):
        r"""创建镜像漏洞概览列表导出任务

        :param request: Request instance for CreateImageVulSummaryListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageVulSummaryListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageVulSummaryListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageVulSummaryListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageVulSummaryListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageVulWhitelist(self, request):
        r"""创建容器镜像漏洞白名单

        :param request: Request instance for CreateImageVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePodContainerListExportJob(self, request):
        r"""创建Pod关联容器列表导出任务。导出字段包含容器ID、容器名称、运行状态、节点ID、节点类型、镜像ID、镜像名称、隔离状态。支持Filter过滤。导出通过异步任务实现，返回JobId后前端轮询查询导出任务状态。

        :param request: Request instance for CreatePodContainerListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreatePodContainerListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreatePodContainerListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePodContainerListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePodContainerListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePodServiceListExportJob(self, request):
        r"""创建Pod关联服务列表导出任务。导出字段包含服务名称、类型、Selector、命名空间、创建时间。支持Filter过滤。当传入PodUniqueID时，复用DescribeClusterServiceList的Pod关联匹配逻辑。导出通过异步任务实现，返回JobId后前端轮询查询导出任务状态。

        :param request: Request instance for CreatePodServiceListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreatePodServiceListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreatePodServiceListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePodServiceListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePodServiceListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePublicAssetsExportJob(self, request):
        r"""创建公网资产导出任务

        :param request: Request instance for CreatePublicAssetsExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreatePublicAssetsExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreatePublicAssetsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePublicAssetsExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePublicAssetsExportJobResponse()
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


    def CreateRiskDetailExportJob(self, request):
        r"""创建云资源配置检查风险详情导出任务示例

        :param request: Request instance for CreateRiskDetailExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateRiskDetailExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateRiskDetailExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRiskDetailExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRiskDetailExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSandboxACLRule(self, request):
        r"""创建一条 ACL 用户访问控制规则。可选择引用若干条系统规则，亦可自定义规则，两者至少提供其一

        :param request: Request instance for CreateSandboxACLRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateSandboxACLRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateSandboxACLRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSandboxACLRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSandboxACLRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSandboxDLPRule(self, request):
        r"""创建一条 DLP 用户规则。可引用若干系统规则（SystemRuleIDList），亦可自定义规则（UserRuleContent，名称 + 正则），两者至少提供其一；UserRuleInfo 为新增可选的结构化入参，与 UserRuleContent 同时传入时以 UserRuleInfo 为准

        :param request: Request instance for CreateSandboxDLPRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateSandboxDLPRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateSandboxDLPRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSandboxDLPRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSandboxDLPRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSandboxFileRule(self, request):
        r"""创建命令沙箱文件访问规则

        :param request: Request instance for CreateSandboxFileRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateSandboxFileRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateSandboxFileRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSandboxFileRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSandboxFileRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSandboxLLMAuditRule(self, request):
        r"""创建一条 LLM 审计用户规则。必须引用至少一条系统规则，不支持用户自定义规则内容

        :param request: Request instance for CreateSandboxLLMAuditRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateSandboxLLMAuditRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateSandboxLLMAuditRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSandboxLLMAuditRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSandboxLLMAuditRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScanStatisticExportJob(self, request):
        r"""暴露面扫描结果导出任务

        :param request: Request instance for CreateScanStatisticExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateScanStatisticExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateScanStatisticExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScanStatisticExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScanStatisticExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScanTask(self, request):
        r"""创建立即检测任务

        :param request: Request instance for CreateScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScanTaskResponse()
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


    def CreateVulRisksExportJob(self, request):
        r"""创建漏洞风险导出任务

        :param request: Request instance for CreateVulRisksExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulRisksExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulRisksExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulRisksExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulRisksExportJobResponse()
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


    def DeleteAIAnalysisSMTPAccess(self, request):
        r"""删除AI助手的SMTP邮箱接入信息

        :param request: Request instance for DeleteAIAnalysisSMTPAccess.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteAIAnalysisSMTPAccessRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteAIAnalysisSMTPAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIAnalysisSMTPAccess", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIAnalysisSMTPAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAISchedule(self, request):
        r"""删除AI 定时任务。

        根据指定的AI 定时任务 ID 删除对应的定时任务。删除后不可恢复。

        :param request: Request instance for DeleteAISchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteAIScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteAIScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAISchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAssetFilterView(self, request):
        r"""删除用户创建的指定资产搜索视图

        :param request: Request instance for DeleteAssetFilterView.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteAssetFilterViewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteAssetFilterViewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAssetFilterView", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAssetFilterViewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAssetTag(self, request):
        r"""删除资产标签

        :param request: Request instance for DeleteAssetTag.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteAssetTagRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteAssetTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAssetTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAssetTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineSelfDefinedPolicyList(self, request):
        r"""批量删除自定义基线策略。仅支持删除 PolicyType=SELF 的策略；删除后历史风险记录保留，但不再产生新结果。

        :param request: Request instance for DeleteBaselineSelfDefinedPolicyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteBaselineSelfDefinedPolicyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteBaselineSelfDefinedPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineSelfDefinedPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineSelfDefinedPolicyListResponse()
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


    def DeleteCluster(self, request):
        r"""删除集群

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterResponse()
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


    def DeleteDspmAuditFilterStrategy(self, request):
        r"""删除Dspm审计过滤策略

        :param request: Request instance for DeleteDspmAuditFilterStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmAuditFilterStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmAuditFilterStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmAuditFilterStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmAuditFilterStrategyResponse()
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


    def DeleteDspmCkafkaConfig(self, request):
        r"""取消日志投递配置

        :param request: Request instance for DeleteDspmCkafkaConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmCkafkaConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmCkafkaConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmCkafkaConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmCkafkaConfigResponse()
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


    def DeleteDspmRiskStrategy(self, request):
        r"""删除Dspm自定义风险策略。仅支持删除自定义策略（rule_source=custom）；内置策略不可删除，请通过 ModifyDspmRiskStrategy 的 IsEnabled 禁用。

        :param request: Request instance for DeleteDspmRiskStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmRiskStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmRiskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmRiskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmRiskStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmShareUserData(self, request):
        r"""删除dspmg共享账号数据

        :param request: Request instance for DeleteDspmShareUserData.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmShareUserDataRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmShareUserDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmShareUserData", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmShareUserDataResponse()
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


    def DeleteEdrLogCollectPaths(self, request):
        r"""批量删除EDR日志采集路径配置

        :param request: Request instance for DeleteEdrLogCollectPaths.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteEdrLogCollectPathsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteEdrLogCollectPathsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdrLogCollectPaths", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdrLogCollectPathsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteExposureAutoTagRule(self, request):
        r"""云边界自动打标-删除规则

        :param request: Request instance for DeleteExposureAutoTagRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteExposureAutoTagRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteExposureAutoTagRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExposureAutoTagRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteExposureAutoTagRuleResponse()
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


    def DeleteImageRegistry(self, request):
        r"""删除镜像仓库信息

        :param request: Request instance for DeleteImageRegistry.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageRegistryScanTask(self, request):
        r"""删除镜像仓库扫描任务

        :param request: Request instance for DeleteImageRegistryScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageRegistryScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageRegistryScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageRegistryTimedScanTaskConfig(self, request):
        r"""删除镜像仓库定时扫描任务配置

        :param request: Request instance for DeleteImageRegistryTimedScanTaskConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryTimedScanTaskConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryTimedScanTaskConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageRegistryTimedScanTaskConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageRegistryTimedScanTaskConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageSensitiveWhitelist(self, request):
        r"""删除容器镜像敏感信息白名单

        :param request: Request instance for DeleteImageSensitiveWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageSensitiveWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageSensitiveWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageSensitiveWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageSensitiveWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageVirusWhitelist(self, request):
        r"""删除镜像木马白名单

        :param request: Request instance for DeleteImageVirusWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageVirusWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageVirusWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageVirusWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageVirusWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageVulWhitelist(self, request):
        r"""删除容器镜像漏洞白名单

        :param request: Request instance for DeleteImageVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageVulWhitelistResponse()
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
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteLoginWhiteListResponse`

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


    def DeleteMachineClearHistory(self, request):
        r"""删除机器清理记录

        :param request: Request instance for DeleteMachineClearHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteMachineClearHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteMachineClearHistoryResponse`

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


    def DeleteSandboxACLRule(self, request):
        r"""批量删除 ACL 用户规则。删除后规则不再返回到列表查询，并不再对流量生效。任一 ID 不存在或属于其他租户时整体返回错误

        :param request: Request instance for DeleteSandboxACLRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxACLRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxACLRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSandboxACLRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSandboxACLRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSandboxDLPRule(self, request):
        r"""批量删除 DLP 用户规则。任一 ID 不存在或属于其他租户时整体返回错误

        :param request: Request instance for DeleteSandboxDLPRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxDLPRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxDLPRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSandboxDLPRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSandboxDLPRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSandboxFileRule(self, request):
        r"""创建命令沙箱文件访问规则

        :param request: Request instance for DeleteSandboxFileRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxFileRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxFileRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSandboxFileRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSandboxFileRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSandboxLLMAuditRule(self, request):
        r"""批量删除 LLM 审计用户规则。任一 ID 不存在或属于其他租户时整体返回错误

        :param request: Request instance for DeleteSandboxLLMAuditRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxLLMAuditRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxLLMAuditRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSandboxLLMAuditRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSandboxLLMAuditRuleResponse()
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


    def DeleteWebhookPolicies(self, request):
        r"""批量删除通知策略。

        :param request: Request instance for DeleteWebhookPolicies.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteWebhookPoliciesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteWebhookPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebhookPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebhookPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebhookReceivers(self, request):
        r"""批量删除接收机器人。删除前会自动从所有引用了这些机器人的策略中移除引用关系。

        :param request: Request instance for DeleteWebhookReceivers.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteWebhookReceiversRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteWebhookReceiversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebhookReceivers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebhookReceiversResponse()
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


    def DescribeAIAgentCredentialList(self, request):
        r"""获取 AIAgent 资产凭据扫描列表

        :param request: Request instance for DescribeAIAgentCredentialList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentCredentialListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentCredentialListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAgentCredentialList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAgentCredentialListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAgentCredentialLocationList(self, request):
        r"""按凭据组行 ID 分页查询单个凭据的泄露位置列表。用于配合 DescribeAIAgentCredentialList 接口拆分后的展开场景，避免单接口在数据倾斜场景下一次拉取几十万行 location 导致性能问题。

        :param request: Request instance for DescribeAIAgentCredentialLocationList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentCredentialLocationListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentCredentialLocationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAgentCredentialLocationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAgentCredentialLocationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAgentSkillList(self, request):
        r"""获取 AI Agent skill 列表

        :param request: Request instance for DescribeAIAgentSkillList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentSkillListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentSkillListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAgentSkillList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAgentSkillListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisFileDownloadURL(self, request):
        r"""获取 AI 分析文件的临时下载链接。

        传入文件的原始地址，返回带签名的临时下载链接，链接有效期为 2 小时。

        :param request: Request instance for DescribeAIAnalysisFileDownloadURL.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisFileDownloadURLRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisFileDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisFileDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisFileDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisHistory(self, request):
        r"""获取云安全AI助手历史分析记录

        :param request: Request instance for DescribeAIAnalysisHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisRecommendQuestions(self, request):
        r"""获取AI问答推荐问题

        :param request: Request instance for DescribeAIAnalysisRecommendQuestions.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisRecommendQuestionsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisRecommendQuestionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisRecommendQuestions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisRecommendQuestionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisRobotInfo(self, request):
        r"""获取云安全AI助手基础信息

        :param request: Request instance for DescribeAIAnalysisRobotInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisRobotInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisRobotInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisRobotInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisRobotInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisSMTP(self, request):
        r"""查询AI助手的SMTP邮箱接入信息

        :param request: Request instance for DescribeAIAnalysisSMTP.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisSMTPRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisSMTPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisSMTP", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisSMTPResponse()
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


    def DescribeAIScheduleList(self, request):
        r"""查询AI 定时任务列表。

        支持分页查询和状态过滤，返回定时任务列表及总条数。

        :param request: Request instance for DescribeAIScheduleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIScheduleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIScheduleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAISchedulePlanList(self, request):
        r"""查询AI 定时任务触发计划。

        查询指定AI 定时任务在给定时间窗口内的未来触发计划列表。

        :param request: Request instance for DescribeAISchedulePlanList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAISchedulePlanListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAISchedulePlanListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAISchedulePlanList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAISchedulePlanListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIScheduleStats(self, request):
        r"""查询AI 定时任务统计信息。

        返回当前用户的定时任务总数和当前运行中的任务数量。

        :param request: Request instance for DescribeAIScheduleStats.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleStatsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIScheduleStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIScheduleStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIScheduleTaskDetail(self, request):
        r"""查询AI 定时任务执行详情。

        根据任务 ID 查询指定执行任务的详细信息，包括执行状态、结果等。

        :param request: Request instance for DescribeAIScheduleTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIScheduleTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIScheduleTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIScheduleTaskList(self, request):
        r"""查询AI 定时任务执行列表。

        查询AI 定时任务的历史执行记录，支持分页和按定时任务 ID 过滤。

        :param request: Request instance for DescribeAIScheduleTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIScheduleTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIScheduleTaskListResponse()
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


    def DescribeAbTestUser(self, request):
        r"""判断用户是否灰度用户

        :param request: Request instance for DescribeAbTestUser.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAbTestUserRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAbTestUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbTestUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbTestUserResponse()
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


    def DescribeAccessKeyWhiteList(self, request):
        r"""访问密钥告警记录列表

        :param request: Request instance for DescribeAccessKeyWhiteList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyWhiteListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentConfigSetting(self, request):
        r"""查询客户端配置设置（配置组），从DescribeAgentRunMode拆分出的独立接口

        :param request: Request instance for DescribeAgentConfigSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAgentConfigSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAgentConfigSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentConfigSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentConfigSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentRunMode(self, request):
        r"""获取客户端运行模式和运行配置信息

        :param request: Request instance for DescribeAgentRunMode.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAgentRunModeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAgentRunModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentRunMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentRunModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentRunPolicy(self, request):
        r"""查询客户端运行策略（策略组），从DescribeAgentRunMode拆分出的独立接口

        :param request: Request instance for DescribeAgentRunPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAgentRunPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAgentRunPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentRunPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentRunPolicyResponse()
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


    def DescribeAssetComponentList(self, request):
        r"""查询资产中组件列表

        :param request: Request instance for DescribeAssetComponentList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetComponentListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetComponentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetComponentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetComponentRelatedImageList(self, request):
        r"""查询镜像仓库组件关联的镜像列表

        :param request: Request instance for DescribeAssetComponentRelatedImageList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetComponentRelatedImageListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetComponentRelatedImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetComponentRelatedImageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetComponentRelatedImageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDetail(self, request):
        r"""资产详情信息

        :param request: Request instance for DescribeAssetDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetFilterViews(self, request):
        r"""资产搜索视图

        :param request: Request instance for DescribeAssetFilterViews.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetFilterViewsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetFilterViewsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetFilterViews", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetFilterViewsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetInfo(self, request):
        r"""资产信息

        :param request: Request instance for DescribeAssetInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetInfoResponse`

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


    def DescribeAssetLastSyncTime(self, request):
        r"""资产最近同步时间

        :param request: Request instance for DescribeAssetLastSyncTime.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetLastSyncTimeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetLastSyncTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetLastSyncTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetLastSyncTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetOverview(self, request):
        r"""资产概览统计

        :param request: Request instance for DescribeAssetOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetOverviewResponse()
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


    def DescribeAssetRiskDetail(self, request):
        r"""资产风险详情

        :param request: Request instance for DescribeAssetRiskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetRiskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetRiskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetRiskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetRiskDetailResponse()
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


    def DescribeAssetSyncTaskStatus(self, request):
        r"""资产同步任务状态

        :param request: Request instance for DescribeAssetSyncTaskStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetSyncTaskStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetSyncTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSyncTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetSyncTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTagAttributes(self, request):
        r"""获取资产标签属性

        :param request: Request instance for DescribeAssetTagAttributes.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagAttributesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTagAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTagAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTagTree(self, request):
        r"""资产标签树结构数据

        :param request: Request instance for DescribeAssetTagTree.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagTreeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTagTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTagTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTags(self, request):
        r"""全部资产

        :param request: Request instance for DescribeAssetTags.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTree(self, request):
        r"""资产树结构

        :param request: Request instance for DescribeAssetTree.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTreeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTreeResponse()
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


    def DescribeBackendScanEngineRegionList(self, request):
        r"""查询后台扫描引擎地域列表

        :param request: Request instance for DescribeBackendScanEngineRegionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBackendScanEngineRegionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBackendScanEngineRegionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackendScanEngineRegionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackendScanEngineRegionListResponse()
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
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBanModeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBanModeResponse`

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


    def DescribeBanStatus(self, request):
        r"""获取阻断按钮状态

        :param request: Request instance for DescribeBanStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBanStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBanStatusResponse`

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


    def DescribeBaselineAggregatedItemList(self, request):
        r"""获取检测项维度的聚合扫描结果列表，用于策略详情页“检测项”Tab 按检测项展示通过/未通过资产数。

        :param request: Request instance for DescribeBaselineAggregatedItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineAggregatedItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineAggregatedItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineAggregatedItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineAggregatedItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineAggregatedPolicyList(self, request):
        r"""获取基线策略维度的聚合扫描结果列表，用于概览页“基线扫描策略”模块按策略展示通过/未通过情况。

        :param request: Request instance for DescribeBaselineAggregatedPolicyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineAggregatedPolicyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineAggregatedPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineAggregatedPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineAggregatedPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineCalculatingStatisticsPolicyIDList(self, request):
        r"""查询当前处于“统计计算中”状态的策略 ID 列表，用于前端轮询判断扫描结果统计是否就绪。

        :param request: Request instance for DescribeBaselineCalculatingStatisticsPolicyIDList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineCalculatingStatisticsPolicyIDListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineCalculatingStatisticsPolicyIDListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineCalculatingStatisticsPolicyIDList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineCalculatingStatisticsPolicyIDListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineCategoryItemList(self, request):
        r"""获取分类检测项列表

        :param request: Request instance for DescribeBaselineCategoryItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineCategoryItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineCategoryItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineCategoryItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineCategoryItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineFixRecordList(self, request):
        r"""获取基线风险修复历史记录列表，用于“修复记录”页展示已修复的检测项与对应资产。

        :param request: Request instance for DescribeBaselineFixRecordList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineFixRecordListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineFixRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineFixRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineFixRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemRiskList(self, request):
        r"""获取检测项维度的风险记录列表。

        :param request: Request instance for DescribeBaselineItemRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineItemRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineItemRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineMainTaskItemList(self, request):
        r"""获取系统内置基线分类的检测项列表（父分类 → 子分类 → 内置检测项 ID 列表），用于策略编辑页选择基线检测项。

        :param request: Request instance for DescribeBaselineMainTaskItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineMainTaskItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineMainTaskItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineMainTaskItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineMainTaskItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineMainTaskList(self, request):
        r"""获取扫描主任务列表，用于“任务记录”页展示一键扫描 / 周期扫描 / 分散扫描的历史记录及结果。

        :param request: Request instance for DescribeBaselineMainTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineMainTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineMainTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineMainTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineMainTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineOverview(self, request):
        r"""获取基线概览页的头部数据，含未通过检测项总数、近一年修复数、最近一次扫描时间、当前是否启用周期扫描等。

        :param request: Request instance for DescribeBaselineOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselinePolicyCategoryList(self, request):
        r"""获取系统内置基线分类树（父分类 → 子分类 → 内置检测项 ID 列表），用于策略详情展示。

        :param request: Request instance for DescribeBaselinePolicyCategoryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyCategoryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselinePolicyCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinePolicyCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselinePolicyItemList(self, request):
        r"""获取策略配置的检测项列表

        :param request: Request instance for DescribeBaselinePolicyItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselinePolicyItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinePolicyItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselinePolicyList(self, request):
        r"""获取基线策略列表，用于“周期计划管理”等列表页展示系统/自定义策略及其配置情况。

        :param request: Request instance for DescribeBaselinePolicyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyListResponse`

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


    def DescribeBaselinePolicyNameExistAppidList(self, request):
        r"""获取基线策略名字存在的用户列表

        :param request: Request instance for DescribeBaselinePolicyNameExistAppidList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyNameExistAppidListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyNameExistAppidListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselinePolicyNameExistAppidList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinePolicyNameExistAppidListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineSubTaskList(self, request):
        r"""获取扫描子任务列表，用于任务详情页“资产维度”展示每台主机/每个集群的扫描状态与失败原因。

        :param request: Request instance for DescribeBaselineSubTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSubTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSubTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineSubTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineSubTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineSyncConf(self, request):
        r"""获取当前账号（管理员）的基线同步配置。仅集团管理员可调用，普通成员账号请使用 DescribeBaselineUserOtherConf。

        :param request: Request instance for DescribeBaselineSyncConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSyncConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSyncConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineSyncConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineSyncConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineSystemCategoryList(self, request):
        r"""获取系统内置基线分类树（父分类 → 子分类 → 内置检测项 ID 列表），用于策略编辑页选择基线检测项。

        :param request: Request instance for DescribeBaselineSystemCategoryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSystemCategoryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSystemCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineSystemCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineSystemCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineUserOtherConf(self, request):
        r"""获取当前账号的用户级基线配置。

        :param request: Request instance for DescribeBaselineUserOtherConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineUserOtherConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineUserOtherConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineUserOtherConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineUserOtherConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineUserWeakPasswordConf(self, request):
        r"""获取当前账号的“用户弱口令”自定义字典（服务端解密后返回明文）。

        :param request: Request instance for DescribeBaselineUserWeakPasswordConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineUserWeakPasswordConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineUserWeakPasswordConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineUserWeakPasswordConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineUserWeakPasswordConfResponse()
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
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBruteAttackRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBruteAttackRulesResponse`

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


    def DescribeCFGRiskReportStatistics(self, request):
        r"""云资源配置检查报告风险统计

        :param request: Request instance for DescribeCFGRiskReportStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCFGRiskReportStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCFGRiskReportStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCFGRiskReportStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCFGRiskReportStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCFGRiskStatistics(self, request):
        r"""获取扫描结果统计信息

        :param request: Request instance for DescribeCFGRiskStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCFGRiskStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCFGRiskStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCFGRiskStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCFGRiskStatisticsResponse()
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


    def DescribeCSCPayInfo(self, request):
        r"""查询当前账号的合并版计费信息，包括订单状态、付费模式以及配额等详细信息。

        :param request: Request instance for DescribeCSCPayInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSCPayInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSCPayInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSCPayInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSCPayInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSIPLicenseBindSchedule(self, request):
        r"""查询ModifyCSIPLicenseBinds返回的异步绑定任务进度。

        :param request: Request instance for DescribeCSIPLicenseBindSchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPLicenseBindScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPLicenseBindScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSIPLicenseBindSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSIPLicenseBindScheduleResponse()
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


    def DescribeCSPMPayInfo(self, request):
        r"""获取已购CSPM订单信息

        :param request: Request instance for DescribeCSPMPayInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSPMPayInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSPMPayInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSPMPayInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSPMPayInfoResponse()
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


    def DescribeCWPExposePath(self, request):
        r"""查询云边界分析路径节点(主机专用)

        :param request: Request instance for DescribeCWPExposePath.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPExposePathRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPExposePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPExposePath", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPExposePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPExposures(self, request):
        r"""云边界分析资产列表(适用于主机资产)

        :param request: Request instance for DescribeCWPExposures.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPExposuresRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPExposuresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPExposures", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPExposuresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPLicenseBindSchedule(self, request):
        r"""查询授权绑定任务的进度

        :param request: Request instance for DescribeCWPLicenseBindSchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPLicenseBindScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPLicenseBindScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPLicenseBindSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPLicenseBindScheduleResponse()
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


    def DescribeCWPMachineOsList(self, request):
        r"""查询可筛选操作系统列表.

        :param request: Request instance for DescribeCWPMachineOsList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachineOsListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachineOsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPMachineOsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPMachineOsListResponse()
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


    def DescribeCWPOrderList(self, request):
        r"""查询资源订单列表

        :param request: Request instance for DescribeCWPOrderList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPOrderListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPScanIpInfo(self, request):
        r"""查询腾讯云扫描IP信息

        :param request: Request instance for DescribeCWPScanIpInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPScanIpInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPScanIpInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPScanIpInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPScanIpInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPTaskDuration(self, request):
        r"""获取任务下发时长

        :param request: Request instance for DescribeCWPTaskDuration.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPTaskDurationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPTaskDurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPTaskDuration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPTaskDurationResponse()
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


    def DescribeCheckConnectivityHostList(self, request):
        r"""查询联通性检测主机列表

        :param request: Request instance for DescribeCheckConnectivityHostList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCheckConnectivityHostListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCheckConnectivityHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCheckConnectivityHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCheckConnectivityHostListResponse()
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


    def DescribeClbListenerList(self, request):
        r"""查询腾讯云指定CLB实例对应的监听器列表

        :param request: Request instance for DescribeClbListenerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClbListenerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClbListenerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClbListenerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClbListenerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClbListenerRules(self, request):
        r"""查询腾讯云指定CLB实例对应的七层转发规则列表

        :param request: Request instance for DescribeClbListenerRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClbListenerRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClbListenerRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClbListenerRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClbListenerRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClbTargets(self, request):
        r"""查询CLB后端服务列表

        :param request: Request instance for DescribeClbTargets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClbTargetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClbTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClbTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClbTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudAssets(self, request):
        r"""全部资产

        :param request: Request instance for DescribeCloudAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCloudAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCloudAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudFunctionList(self, request):
        r"""云函数列表

        :param request: Request instance for DescribeCloudFunctionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCloudFunctionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCloudFunctionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudFunctionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudFunctionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterAssetList(self, request):
        r"""查询容器集群资产列表

        :param request: Request instance for DescribeClusterAssetList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAssetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterAssetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterAssetSyncTaskStatus(self, request):
        r"""查询集群资产同步任务状态

        :param request: Request instance for DescribeClusterAssetSyncTaskStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetSyncTaskStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetSyncTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAssetSyncTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterAssetSyncTaskStatusResponse()
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


    def DescribeClusterContainerAppList(self, request):
        r"""查询容器关联应用列表。通过容器ID获取关联的应用服务信息，支持分页。

        :param request: Request instance for DescribeClusterContainerAppList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerAppListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerAppList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerComponentList(self, request):
        r"""查询容器关联组件列表。通过容器ID获取关联的组件信息，支持分页。

        :param request: Request instance for DescribeClusterContainerComponentList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerComponentListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerComponentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerComponentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerDetail(self, request):
        r"""查询集群容器详情。通过容器ID获取容器基本信息、镜像信息、挂载信息、网络信息以及关联节点信息。

        :param request: Request instance for DescribeClusterContainerDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerList(self, request):
        r"""查询集群容器列表

        :param request: Request instance for DescribeClusterContainerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerPortList(self, request):
        r"""查询容器关联端口列表。通过容器ID获取关联的端口信息，支持分页。

        :param request: Request instance for DescribeClusterContainerPortList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerPortListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerPortListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerPortList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerPortListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerProcessList(self, request):
        r"""查询容器关联进程列表。通过容器ID获取关联的进程信息，支持按启动时间排序和分页。Filter.By支持StartTime；Filter.Order支持ASC/DESC。

        :param request: Request instance for DescribeClusterContainerProcessList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerProcessListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerWebServiceList(self, request):
        r"""查询容器关联Web服务列表。通过容器ID获取关联的Web服务信息，支持分页。

        :param request: Request instance for DescribeClusterContainerWebServiceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerWebServiceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerWebServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerWebServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerWebServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterDetail(self, request):
        r"""查询集群详情

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterInstallCommand(self, request):
        r"""查询集群安装命令

        :param request: Request instance for DescribeClusterInstallCommand.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterInstallCommandRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterInstallCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstallCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterInstallCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterListV2(self, request):
        r"""查询集群列表

        :param request: Request instance for DescribeClusterListV2.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterListV2Request`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterListV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterListV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterListV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNamespaceList(self, request):
        r"""查询集群命名空间列表

        :param request: Request instance for DescribeClusterNamespaceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterNamespaceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNamespaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNamespaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNodeList(self, request):
        r"""查询集群节点列表

        :param request: Request instance for DescribeClusterNodeList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterNodeListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterNodeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNodeListResponse()
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


    def DescribeClusterPodDetail(self, request):
        r"""查询集群 Pod 详情。容器资产改版 A 类新接口，为 Pod 资产详情页主入口。入参仅 UniqueID；出参覆盖资产信息、所属集群、命名空间、节点、Workload、以及按四个风险等级分组的风险事件数和告警事件数。

        :param request: Request instance for DescribeClusterPodDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPodDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPodDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterPodList(self, request):
        r"""查询集群pod列表

        :param request: Request instance for DescribeClusterPodList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPodList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPodListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterServiceList(self, request):
        r"""查询集群service列表

        :param request: Request instance for DescribeClusterServiceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterServiceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterSummary(self, request):
        r"""查询集群概览数据

        :param request: Request instance for DescribeClusterSummary.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterSummaryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterSuperNodeInfo(self, request):
        r"""查询集群超级节点详情，返回基本信息（所属地域/可用区/资产最后更新时间/节点来源/子网/核数）与所属集群信息（集群名称/集群ID/集群状态/Kubernetes版本/Kubelet版本）。

        :param request: Request instance for DescribeClusterSuperNodeInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterSuperNodeInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterSuperNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterSuperNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterSuperNodeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceOverview(self, request):
        r"""云资源配置检测合规概览

        :param request: Request instance for DescribeComplianceOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceRiskList(self, request):
        r"""合规标准聚合视角下云资源配置风险列表

        :param request: Request instance for DescribeComplianceRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceStandardTermTree(self, request):
        r"""云资源配置检测标准章节条款树

        :param request: Request instance for DescribeComplianceStandardTermTree.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceStandardTermTreeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceStandardTermTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceStandardTermTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceStandardTermTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceStatistics(self, request):
        r"""云资源配置检测规范分类统计

        :param request: Request instance for DescribeComplianceStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceStatisticsResponse()
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


    def DescribeCspmShardConfig(self, request):
        r"""获取CSPM自动配额共享配置

        :param request: Request instance for DescribeCspmShardConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCspmShardConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCspmShardConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCspmShardConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCspmShardConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomAssetTagCount(self, request):
        r"""用户自定义 标签数量

        :param request: Request instance for DescribeCustomAssetTagCount.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCustomAssetTagCountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCustomAssetTagCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomAssetTagCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomAssetTagCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomRiskRuleDetail(self, request):
        r"""自定义风险规则配置详情列表示例

        :param request: Request instance for DescribeCustomRiskRuleDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCustomRiskRuleDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCustomRiskRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomRiskRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomRiskRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomRiskRules(self, request):
        r"""自定义风险规则配置列表

        :param request: Request instance for DescribeCustomRiskRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCustomRiskRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCustomRiskRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomRiskRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomRiskRulesResponse()
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


    def DescribeDefaultSecurityScoreRule(self, request):
        r"""获取内置默认安全评分规则，用于重置自定义规则

        :param request: Request instance for DescribeDefaultSecurityScoreRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDefaultSecurityScoreRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDefaultSecurityScoreRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultSecurityScoreRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultSecurityScoreRuleResponse()
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


    def DescribeDspmAuditFilterStrategy(self, request):
        r"""查询dspm审计过滤策略

        :param request: Request instance for DescribeDspmAuditFilterStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAuditFilterStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAuditFilterStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAuditFilterStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAuditFilterStrategyResponse()
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


    def DescribeDspmCkafkaRouteList(self, request):
        r"""查询Ckafka实例的路由信息

        :param request: Request instance for DescribeDspmCkafkaRouteList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmCkafkaRouteListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmCkafkaRouteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmCkafkaRouteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmCkafkaRouteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmCkafkaTopicList(self, request):
        r"""查询实例的主题列表

        :param request: Request instance for DescribeDspmCkafkaTopicList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmCkafkaTopicListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmCkafkaTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmCkafkaTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmCkafkaTopicListResponse()
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


    def DescribeDspmLogDeliveryType(self, request):
        r"""查询日志投递的日志类型

        :param request: Request instance for DescribeDspmLogDeliveryType.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogDeliveryTypeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogDeliveryTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmLogDeliveryType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmLogDeliveryTypeResponse()
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


    def DescribeDspmLogTypeConfigList(self, request):
        r"""查询租户日志投递配置

        :param request: Request instance for DescribeDspmLogTypeConfigList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogTypeConfigListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogTypeConfigListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmLogTypeConfigList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmLogTypeConfigListResponse()
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


    def DescribeDspmResource(self, request):
        r"""查询Dspm实例

        :param request: Request instance for DescribeDspmResource.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmResourceRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmResourceResponse()
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


    def DescribeDspmSessionList(self, request):
        r"""查询审计会话列表信息

        :param request: Request instance for DescribeDspmSessionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSessionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmSessionListResponse()
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


    def DescribeDspmUserCkafkaInstanceList(self, request):
        r"""查询租户ckafka实例列表

        :param request: Request instance for DescribeDspmUserCkafkaInstanceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmUserCkafkaInstanceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmUserCkafkaInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmUserCkafkaInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmUserCkafkaInstanceListResponse()
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


    def DescribeDynamicAssets(self, request):
        r"""指定资产类型列表

        :param request: Request instance for DescribeDynamicAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDynamicAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDynamicAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDynamicAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDynamicAssetsResponse()
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


    def DescribeEdrAlertThreatTags(self, request):
        r"""EDR告警标签批量查询

        :param request: Request instance for DescribeEdrAlertThreatTags.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertThreatTagsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertThreatTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertThreatTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertThreatTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrExcludeNetworkSegments(self, request):
        r"""查询EDR日志采集例外网段配置，添加至例外名单的网段，其TCP日志将不被采集。如果用户未配置过，则返回系统推荐的默认网段

        :param request: Request instance for DescribeEdrExcludeNetworkSegments.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExcludeNetworkSegmentsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExcludeNetworkSegmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrExcludeNetworkSegments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrExcludeNetworkSegmentsResponse()
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


    def DescribeEdrLogCollectPaths(self, request):
        r"""查询采集路径配置

        :param request: Request instance for DescribeEdrLogCollectPaths.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrLogCollectPathsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrLogCollectPathsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrLogCollectPaths", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrLogCollectPathsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportJobDownloadURL(self, request):
        r"""导出任务结果下载URL

        :param request: Request instance for DescribeExportJobDownloadURL.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExportJobDownloadURLRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExportJobDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportJobDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportJobDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportJobManageList(self, request):
        r"""导出任务列表

        :param request: Request instance for DescribeExportJobManageList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExportJobManageListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExportJobManageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportJobManageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportJobManageListResponse()
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


    def DescribeExposeRiskStatistics(self, request):
        r"""云边界风险待治理风险

        :param request: Request instance for DescribeExposeRiskStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRiskStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRiskStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposeRiskStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposeRiskStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposeRisks(self, request):
        r"""云边界待处理风险列表

        :param request: Request instance for DescribeExposeRisks.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRisksRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposeRisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposeRisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposeRules(self, request):
        r"""边界规则列表

        :param request: Request instance for DescribeExposeRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposureAutoTagAttribute(self, request):
        r"""云边界自动打标-规则属性

        :param request: Request instance for DescribeExposureAutoTagAttribute.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposureAutoTagAttributeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposureAutoTagAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposureAutoTagAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposureAutoTagAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposureAutoTagRules(self, request):
        r"""云边界自动打标-规则列表

        :param request: Request instance for DescribeExposureAutoTagRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposureAutoTagRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposureAutoTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposureAutoTagRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposureAutoTagRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposureTrend(self, request):
        r"""查询互联网暴露周期数量趋势统计信息

        :param request: Request instance for DescribeExposureTrend.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposureTrendRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposureTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposureTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposureTrendResponse()
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


    def DescribeImageAssetDetail(self, request):
        r"""查询镜像资产详情

        :param request: Request instance for DescribeImageAssetDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssetDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssetDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAssetDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAssetDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAssetList(self, request):
        r"""查询镜像资产列表

        :param request: Request instance for DescribeImageAssetList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssetListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAssetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAssetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAssociatedAssetCount(self, request):
        r"""查询镜像关联资产数

        :param request: Request instance for DescribeImageAssociatedAssetCount.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedAssetCountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedAssetCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAssociatedAssetCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAssociatedAssetCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAssociatedContainerList(self, request):
        r"""查询镜像关联容器资产

        :param request: Request instance for DescribeImageAssociatedContainerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedContainerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedContainerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAssociatedContainerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAssociatedContainerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAssociatedHostList(self, request):
        r"""查询镜像关联主机资产列表

        :param request: Request instance for DescribeImageAssociatedHostList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedHostListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAssociatedHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAssociatedHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageComponentList(self, request):
        r"""查询镜像组件列表

        :param request: Request instance for DescribeImageComponentList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageComponentListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageComponentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageComponentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageExportJobList(self, request):
        r"""查询镜像仓库导出任务列表

        :param request: Request instance for DescribeImageExportJobList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageExportJobListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageExportJobListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageExportJobList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageExportJobListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageLayerList(self, request):
        r"""查询镜像层信息列表

        :param request: Request instance for DescribeImageLayerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageLayerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageLayerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageLayerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageLayerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageLayerVulList(self, request):
        r"""查询镜像层漏洞列表

        :param request: Request instance for DescribeImageLayerVulList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageLayerVulListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageLayerVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageLayerVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageLayerVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryAssetOverview(self, request):
        r"""查询镜像仓库资产总览

        :param request: Request instance for DescribeImageRegistryAssetOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryAssetOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryAssetOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryAssetOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryAssetOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryConnectivityTaskResult(self, request):
        r"""查询镜像仓库联通性检查任务结果

        :param request: Request instance for DescribeImageRegistryConnectivityTaskResult.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryConnectivityTaskResultRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryConnectivityTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryConnectivityTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryConnectivityTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryList(self, request):
        r"""查询镜像仓库列表

        :param request: Request instance for DescribeImageRegistryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryNamespaceList(self, request):
        r"""查询镜像仓库命名空间列表

        :param request: Request instance for DescribeImageRegistryNamespaceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryNamespaceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryNamespaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryNamespaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryScanSubTaskList(self, request):
        r"""查询镜像仓库扫描子任务信息

        :param request: Request instance for DescribeImageRegistryScanSubTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryScanSubTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryScanSubTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryScanSubTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryScanSubTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryScanTaskList(self, request):
        r"""查询镜像仓库镜像扫描任务列表

        :param request: Request instance for DescribeImageRegistryScanTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryScanTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryScanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryScanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryScanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryTimedScanTaskConfig(self, request):
        r"""查看镜像仓库定时扫描任务配置

        :param request: Request instance for DescribeImageRegistryTimedScanTaskConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryTimedScanTaskConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryTimedScanTaskConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryTimedScanTaskConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryTimedScanTaskConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryTimedScanTaskPreview(self, request):
        r"""查询镜像仓库定时扫描任务预览

        :param request: Request instance for DescribeImageRegistryTimedScanTaskPreview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryTimedScanTaskPreviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryTimedScanTaskPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryTimedScanTaskPreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryTimedScanTaskPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageSensitiveInfoList(self, request):
        r"""查询镜像敏感信息列表

        :param request: Request instance for DescribeImageSensitiveInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageSensitiveInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageSensitiveInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageSensitiveInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageSensitiveInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageSensitiveWhitelist(self, request):
        r"""查询容器镜像敏感信息白名单

        :param request: Request instance for DescribeImageSensitiveWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageSensitiveWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageSensitiveWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageSensitiveWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageSensitiveWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVirusList(self, request):
        r"""查询镜像木马病毒列表

        :param request: Request instance for DescribeImageVirusList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVirusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVirusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVirusWhitelist(self, request):
        r"""查询镜像木马白名单

        :param request: Request instance for DescribeImageVirusWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVirusWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVirusWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVirusWhitelistDetail(self, request):
        r"""查询镜像木马白名单详情

        :param request: Request instance for DescribeImageVirusWhitelistDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusWhitelistDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusWhitelistDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVirusWhitelistDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVirusWhitelistDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVulList(self, request):
        r"""查询镜像漏洞列表

        :param request: Request instance for DescribeImageVulList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVulSummaryList(self, request):
        r"""查询镜像漏洞概览列表

        :param request: Request instance for DescribeImageVulSummaryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulSummaryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVulSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVulSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVulWhitelist(self, request):
        r"""查询容器镜像漏洞白名单

        :param request: Request instance for DescribeImageVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVulWhitelistResponse()
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


    def DescribeLastScanTaskInfo(self, request):
        r"""获取最近一次立即检测任务信息

        :param request: Request instance for DescribeLastScanTaskInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLastScanTaskInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLastScanTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLastScanTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLastScanTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseStatus(self, request):
        r"""查询当前账号下所有有效授权的汇总状态，按计费项分组返回总数、已用、剩余及到期时间，同时返回自动加购开关状态和合并剩余解绑次数。输出顺序固定为：旗舰版 → 专业版 → RASP → 其他。

        :param request: Request instance for DescribeLicenseStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLicenseStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLicenseStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLighthouseFirewallRules(self, request):
        r"""查询轻量应用服务器防火墙规则

        :param request: Request instance for DescribeLighthouseFirewallRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLighthouseFirewallRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLighthouseFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLighthouseFirewallRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLighthouseFirewallRulesResponse()
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


    def DescribeLoginTypeGlobalConf(self, request):
        r"""获取防卸载全局配置

        :param request: Request instance for DescribeLoginTypeGlobalConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLoginTypeGlobalConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLoginTypeGlobalConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginTypeGlobalConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginTypeGlobalConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginTypeHost(self, request):
        r"""获取扫码登录主机列表

        :param request: Request instance for DescribeLoginTypeHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLoginTypeHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLoginTypeHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginTypeHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginTypeHostResponse()
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
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLoginWhiteCombinedListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLoginWhiteCombinedListResponse`

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
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLoginWhiteHostListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLoginWhiteHostListResponse`

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


    def DescribeMachineClearHistory(self, request):
        r"""查询机器清理历史记录

        :param request: Request instance for DescribeMachineClearHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMachineClearHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMachineClearHistoryResponse`

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


    def DescribeMachineGeneral(self, request):
        r"""查询主机概览信息

        :param request: Request instance for DescribeMachineGeneral.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMachineGeneralRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMachineGeneralResponse`

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


    def DescribeMachineLoginType(self, request):
        r"""获取主机登录方式

        :param request: Request instance for DescribeMachineLoginType.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMachineLoginTypeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMachineLoginTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineLoginType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineLoginTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareTimingScanSetting(self, request):
        r"""查询文件查杀定时扫描配置

        :param request: Request instance for DescribeMalwareTimingScanSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMalwareTimingScanSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMalwareTimingScanSettingResponse`

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


    def DescribeMandatoryVulSet(self, request):
        r"""展示企业必修漏洞情报

        :param request: Request instance for DescribeMandatoryVulSet.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMandatoryVulSetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMandatoryVulSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMandatoryVulSet", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMandatoryVulSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModifyMachinesLoginTypeTasks(self, request):
        r"""获取批量修改主机登录方式任务列表

        :param request: Request instance for DescribeModifyMachinesLoginTypeTasks.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeModifyMachinesLoginTypeTasksRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeModifyMachinesLoginTypeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModifyMachinesLoginTypeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModifyMachinesLoginTypeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiCloudAssetCount(self, request):
        r"""获取多云（腾讯云、阿里云、AWS、华为云、Azure 等）接入的资产总数及各云厂商资产数量明细

        :param request: Request instance for DescribeMultiCloudAssetCount.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMultiCloudAssetCountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMultiCloudAssetCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiCloudAssetCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiCloudAssetCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNFSScanConf(self, request):
        r"""获取NFS扫描全局配置

        :param request: Request instance for DescribeNFSScanConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNFSScanConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNFSScanConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNFSScanConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNFSScanConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNFSScanHost(self, request):
        r"""获取扫码登录主机列表

        :param request: Request instance for DescribeNFSScanHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNFSScanHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNFSScanHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNFSScanHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNFSScanHostResponse()
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


    def DescribeNatRules(self, request):
        r"""查询腾讯云nat网关实例对应的NAT策略

        :param request: Request instance for DescribeNatRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNatRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNatRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatRulesResponse()
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


    def DescribeNotifyAgentOfflineDuration(self, request):
        r"""查询客户端离线时长

        :param request: Request instance for DescribeNotifyAgentOfflineDuration.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNotifyAgentOfflineDurationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNotifyAgentOfflineDurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotifyAgentOfflineDuration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotifyAgentOfflineDurationResponse()
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


    def DescribeNotifySettingAk(self, request):
        r"""获取通知设置（云API风险治理）

        :param request: Request instance for DescribeNotifySettingAk.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingAkRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingAkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotifySettingAk", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotifySettingAkResponse()
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


    def DescribePodContainerList(self, request):
        r"""查询 Pod 关联容器列表

        :param request: Request instance for DescribePodContainerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePodContainerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePodContainerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePodContainerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePodContainerListResponse()
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


    def DescribePortDetectList(self, request):
        r"""端口探测列表

        :param request: Request instance for DescribePortDetectList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePortDetectListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePortDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePortDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePortDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePortScanTaskCount(self, request):
        r"""查询当前账号下端口扫描任务次数

        :param request: Request instance for DescribePortScanTaskCount.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePortScanTaskCountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePortScanTaskCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePortScanTaskCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePortScanTaskCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePreventUninstallGlobalConf(self, request):
        r"""获取防卸载全局配置

        :param request: Request instance for DescribePreventUninstallGlobalConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePreventUninstallGlobalConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePreventUninstallGlobalConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePreventUninstallGlobalConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePreventUninstallGlobalConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePreventUninstallHost(self, request):
        r"""获取防卸载主机列表

        :param request: Request instance for DescribePreventUninstallHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePreventUninstallHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePreventUninstallHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePreventUninstallHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePreventUninstallHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcessDaemonGlobalConf(self, request):
        r"""获取进程防护全局配置

        :param request: Request instance for DescribeProcessDaemonGlobalConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeProcessDaemonGlobalConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeProcessDaemonGlobalConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessDaemonGlobalConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessDaemonGlobalConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcessDaemonHost(self, request):
        r"""获取进程守护主机列表

        :param request: Request instance for DescribeProcessDaemonHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeProcessDaemonHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeProcessDaemonHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessDaemonHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessDaemonHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicCloudAssets(self, request):
        r"""公网资产

        :param request: Request instance for DescribePublicCloudAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePublicCloudAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePublicCloudAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicCloudAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicCloudAssetsResponse()
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


    def DescribeRaspLicenseList(self, request):
        r"""查询应用防护授权列表

        :param request: Request instance for DescribeRaspLicenseList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRaspLicenseListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRaspLicenseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRaspLicenseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRaspLicenseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistryOverview(self, request):
        r"""查询仓库总览

        :param request: Request instance for DescribeRegistryOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRegistryOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRegistryOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistryOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistryOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistryRegionList(self, request):
        r"""查询镜像仓库地域列表

        :param request: Request instance for DescribeRegistryRegionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRegistryRegionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRegistryRegionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistryRegionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistryRegionListResponse()
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


    def DescribeRiskCenterRiskTrendAnalysis(self, request):
        r"""获取风险趋势分析示例

        :param request: Request instance for DescribeRiskCenterRiskTrendAnalysis.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterRiskTrendAnalysisRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterRiskTrendAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterRiskTrendAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterRiskTrendAnalysisResponse()
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


    def DescribeRiskScanCronConfig(self, request):
        r"""获取风险扫描周期计划

        :param request: Request instance for DescribeRiskScanCronConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskScanCronConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskScanCronConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskScanCronConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskScanCronConfigResponse()
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


    def DescribeSCFAliasList(self, request):
        r"""查询指定 SCF 函数下的别名列表。

        :param request: Request instance for DescribeSCFAliasList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSCFAliasListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSCFAliasListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSCFAliasList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSCFAliasListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSCFFunctionList(self, request):
        r"""查询指定命名空间下的 SCF 函数列表，仅返回 Event 触发器类型的函数。

        :param request: Request instance for DescribeSCFFunctionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSCFFunctionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSCFFunctionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSCFFunctionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSCFFunctionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSCFFunctionVersionList(self, request):
        r"""查询指定 SCF 函数下的版本列表。

        :param request: Request instance for DescribeSCFFunctionVersionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSCFFunctionVersionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSCFFunctionVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSCFFunctionVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSCFFunctionVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSCFNamespaceList(self, request):
        r"""查询当前用户在指定地域下的 SCF（云函数）命名空间列表。

        :param request: Request instance for DescribeSCFNamespaceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSCFNamespaceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSCFNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSCFNamespaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSCFNamespaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxACLAlertList(self, request):
        r"""分页查询 ACL 访问控制告警日志列表。支持按 Filter.Name=ID 精确过滤单条告警用于详情页场景

        :param request: Request instance for DescribeSandboxACLAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxACLAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxACLAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxACLRuleList(self, request):
        r"""查询当前租户的 ACL 用户访问控制规则列表。传入 Filter.Name=RuleID 可精确查询单条规则（用于详情页面场景）

        :param request: Request instance for DescribeSandboxACLRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxACLRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxACLRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxACLSystemRuleList(self, request):
        r"""查询流量沙箱访问控制（ACL）系统规则列表，系统规则由 CSIP 平台内置，可被用户规则引用

        :param request: Request instance for DescribeSandboxACLSystemRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLSystemRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLSystemRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxACLSystemRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxACLSystemRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxDLPAlertList(self, request):
        r"""分页查询 DLP 数据泄露告警日志列表。支持按 Filter.Name=ID 精确过滤单条告警用于详情页场景

        :param request: Request instance for DescribeSandboxDLPAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxDLPAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxDLPAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxDLPRuleList(self, request):
        r"""查询当前租户的 DLP 用户规则列表。传入 Filter.Name=RuleID 可精确查询单条规则（用于详情页面场景）

        :param request: Request instance for DescribeSandboxDLPRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxDLPRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxDLPRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxDLPSystemRuleList(self, request):
        r"""查询流量沙箱数据泄露防护（DLP）系统规则列表，系统规则由 CSIP 平台内置，可被用户规则引用

        :param request: Request instance for DescribeSandboxDLPSystemRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPSystemRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPSystemRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxDLPSystemRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxDLPSystemRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxFileRuleList(self, request):
        r"""获取命令沙箱文件规则列表

        :param request: Request instance for DescribeSandboxFileRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxFileRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxFileRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxFileRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxFileRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxLLMAuditAlertList(self, request):
        r"""分页查询 LLM 审计告警日志列表。支持按 Filter.Name=ID 精确过滤单条告警用于详情页场景

        :param request: Request instance for DescribeSandboxLLMAuditAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxLLMAuditAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxLLMAuditAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxLLMAuditRuleList(self, request):
        r"""查询当前租户的 LLM 审计用户规则列表。LLM 审计规则不支持用户自定义内容，只能引用系统规则组合。传入 Filter.Name=RuleID 可精确查询单条规则（用于详情页面场景）

        :param request: Request instance for DescribeSandboxLLMAuditRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxLLMAuditRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxLLMAuditRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxLLMAuditSystemRuleList(self, request):
        r"""查询 LLM 审计系统规则列表，系统规则由 CSIP 平台内置（来源于 LLM 审计系统规则库），按 LLM 推理防护 / ToolCall 防护拆分为两个扁平规则数组返回，可被用户规则引用

        :param request: Request instance for DescribeSandboxLLMAuditSystemRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditSystemRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditSystemRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxLLMAuditSystemRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxLLMAuditSystemRuleListResponse()
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


    def DescribeScanTaskRecordList(self, request):
        r"""查询扫描任务记录列表

        :param request: Request instance for DescribeScanTaskRecordList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScanTaskRecordListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScanTaskRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScfCustomDomainEndpoints(self, request):
        r"""查询腾讯云SCF自定义域名端点列表

        :param request: Request instance for DescribeScfCustomDomainEndpoints.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScfCustomDomainEndpointsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScfCustomDomainEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScfCustomDomainEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScfCustomDomainEndpointsResponse()
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


    def DescribeSecurityGroupPolicy(self, request):
        r"""查询指定安全组ID对应安全组规则

        :param request: Request instance for DescribeSecurityGroupPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityGroupPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityRiskTrend(self, request):
        r"""获取安全风险趋势，返回按维度分组的每日风险数量

        :param request: Request instance for DescribeSecurityRiskTrend.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityRiskTrendRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityRiskTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityRiskTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityRiskTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityScoreOverview(self, request):
        r"""获取安全评分概览，实时计算各维度和子项扣分情况

        :param request: Request instance for DescribeSecurityScoreOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityScoreOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityScoreOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityScoreOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityScoreOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityScoreRule(self, request):
        r"""获取当前账号的安全评分规则，无自定义则返回内置默认规则

        :param request: Request instance for DescribeSecurityScoreRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityScoreRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityScoreRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityScoreRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityScoreRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillScanAlertDetail(self, request):
        r"""查询 Skill 安全检测告警详情，包含本地告警信息和引擎实时检测数据

        :param request: Request instance for DescribeSkillScanAlertDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanAlertDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanAlertDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillScanAlertDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillScanAlertDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillScanAlertList(self, request):
        r"""查询 Skill 安全检测告警列表，支持分页、过滤和排序

        :param request: Request instance for DescribeSkillScanAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillScanAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillScanAlertListResponse()
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


    def DescribeSourceIPDetail(self, request):
        r"""获取用户访问密钥资产列表（源IP视角）

        :param request: Request instance for DescribeSourceIPDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSourceIPDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSourceIPDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSourceIPDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSourceIPDetailResponse()
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


    def DescribeTCRInstanceList(self, request):
        r"""获取TCR实例列表

        :param request: Request instance for DescribeTCRInstanceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTCRInstanceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTCRInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTCRInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTCRInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagRuleAssets(self, request):
        r"""打标策略生效资产列表

        :param request: Request instance for DescribeTagRuleAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTagRuleAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTagRuleAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagRuleAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagRuleAssetsResponse()
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


    def DescribeTaskPredictCostQuota(self, request):
        r"""获取扫描预消耗配额

        :param request: Request instance for DescribeTaskPredictCostQuota.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTaskPredictCostQuotaRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTaskPredictCostQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskPredictCostQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskPredictCostQuotaResponse()
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


    def DescribeUebaBehaviorSummary(self, request):
        r"""查询用户行为分析的行为概览

        :param request: Request instance for DescribeUebaBehaviorSummary.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUebaBehaviorSummaryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUebaBehaviorSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUebaBehaviorSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUebaBehaviorSummaryResponse()
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


    def DescribeUebaUserSummary(self, request):
        r"""获取用户行为分析模块的用户概览

        :param request: Request instance for DescribeUebaUserSummary.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUebaUserSummaryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUebaUserSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUebaUserSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUebaUserSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserAKInfoList(self, request):
        r"""获取账号AK信息

        :param request: Request instance for DescribeUserAKInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUserAKInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUserAKInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserAKInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserAKInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCSPMInfoList(self, request):
        r"""获取账号CSPM信息

        :param request: Request instance for DescribeUserCSPMInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUserCSPMInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUserCSPMInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCSPMInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserCSPMInfoListResponse()
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


    def DescribeUserInfo(self, request):
        r"""用户CSPM配额信息

        :param request: Request instance for DescribeUserInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUserInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserInfoResponse()
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


    def DescribeVdbAndPocInfo(self, request):
        r"""获取病毒库及POC的更新信息

        :param request: Request instance for DescribeVdbAndPocInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVdbAndPocInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVdbAndPocInfoResponse`

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


    def DescribeVoucherEligibility(self, request):
        r"""检查当前用户是否有资格领取指定活动的代金券。

        :param request: Request instance for DescribeVoucherEligibility.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVoucherEligibilityRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVoucherEligibilityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVoucherEligibility", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVoucherEligibilityResponse()
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


    def DescribeWebhookPolicyList(self, request):
        r"""分页查询当前租户下的通知策略列表，对应「通知中心 - 机器人通知 - 通知策略配置」Tab 的表格。返回的字段为「行展示」所需的精简信息。完整配置在编辑场景下使用 DescribeWebhookPolicy。每租户最多 100 个通知策略

        :param request: Request instance for DescribeWebhookPolicyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeWebhookPolicyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeWebhookPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebhookPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebhookPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebhookReceiverList(self, request):
        r"""分页查询当前租户下的接收机器人列表，对应「通知中心 - 机器人通知 - 接收机器人管理」Tab 的表格。每租户最多 50 个机器人

        :param request: Request instance for DescribeWebhookReceiverList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeWebhookReceiverListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeWebhookReceiverListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebhookReceiverList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebhookReceiverListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableAISchedule(self, request):
        r"""停用AI 定时任务。

        将指定的AI 定时任务状态设置为已停用，停用后任务将暂停自动执行。

        :param request: Request instance for DisableAISchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DisableAIScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DisableAIScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableAISchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DisableAIScheduleResponse()
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


    def EnableAISchedule(self, request):
        r"""启用AI 定时任务。

        将指定的AI 定时任务状态设置为已启用，启用后任务将按触发器配置自动执行。

        :param request: Request instance for EnableAISchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.EnableAIScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.EnableAIScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableAISchedule", params, headers=headers)
            response = json.loads(body)
            model = models.EnableAIScheduleResponse()
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


    def ExportClientSettingHostList(self, request):
        r"""客户端设置主机列表导出

        :param request: Request instance for ExportClientSettingHostList.
        :type request: :class:`tencentcloud.csip.v20221121.models.ExportClientSettingHostListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ExportClientSettingHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportClientSettingHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportClientSettingHostListResponse()
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


    def ExportTasks(self, request):
        r"""用于异步导出数据量大的日志文件

        :param request: Request instance for ExportTasks.
        :type request: :class:`tencentcloud.csip.v20221121.models.ExportTasksRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ExportTasksResponse`

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


    def InstallClusterAgent(self, request):
        r"""安装集群容器安全Agent（平行容器方式安装 Agent）。

        capi 层处理流程：
        1. 按 ClusterCaMD5List 查询 DB 集群列表（仅用于解析每个集群归属的 appid，不做存在性/类型校验）
        2. 按 appid 分组透传到接入侧 ClusterInstall RPC

        说明（容器资产改版 2026 H1）：本接口为透传接口，capi 层不对 ClusterCaMD5 做存在性/类型/格式校验；DB 中未命中的 ClusterCaMD5 静默跳过、不报错。

        :param request: Request instance for InstallClusterAgent.
        :type request: :class:`tencentcloud.csip.v20221121.models.InstallClusterAgentRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.InstallClusterAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallClusterAgent", params, headers=headers)
            response = json.loads(body)
            model = models.InstallClusterAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstallKeySandboxSkill(self, request):
        r"""在指定的机器实例上安装密钥沙箱SKILL。支持批量操作，一次可传入多个实例ID。安装后，目标机器上的AI Agent即可通过密钥沙箱代理访问凭据，无需接触明文密钥。已安装的实例重复调用不会报错（幂等），直接视为成功。

        :param request: Request instance for InstallKeySandboxSkill.
        :type request: :class:`tencentcloud.csip.v20221121.models.InstallKeySandboxSkillRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.InstallKeySandboxSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallKeySandboxSkill", params, headers=headers)
            response = json.loads(body)
            model = models.InstallKeySandboxSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstallSandboxPlugin(self, request):
        r"""触发将流量沙箱插件安装到指定范围内的 AI Agent 资产。通过 BelongAssetType 区分主机/容器维度，通过 EffectScope 指定安装目标（INCLUDE=仅安装到指定资产，EXCLUDE=全部资产减去指定资产）。接口仅触发下发动作，不等待完成

        :param request: Request instance for InstallSandboxPlugin.
        :type request: :class:`tencentcloud.csip.v20221121.models.InstallSandboxPluginRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.InstallSandboxPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallSandboxPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.InstallSandboxPluginResponse()
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


    def ModifyAISchedule(self, request):
        r"""修改AI 定时任务。

        支持部分更新，仅更新传入的可选字段。触发器列表通过 UpdateTriggers 标志控制是否全量替换。

        :param request: Request instance for ModifyAISchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAIScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAIScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAISchedule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAIScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentConfigSetting(self, request):
        r"""修改客户端日志采集配置（CSIP专属），支持设置日志采集类型和生效资产范围

        :param request: Request instance for ModifyAgentConfigSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAgentConfigSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAgentConfigSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentConfigSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentConfigSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentRunMode(self, request):
        r"""设置客户端运行模式以及配置

        :param request: Request instance for ModifyAgentRunMode.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAgentRunModeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAgentRunModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentRunMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentRunModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentRunPolicy(self, request):
        r"""修改客户端运行策略（策略组），支持设置自定义策略及关联机器列表

        :param request: Request instance for ModifyAgentRunPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAgentRunPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAgentRunPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentRunPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentRunPolicyResponse()
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


    def ModifyAssetCoreAttribute(self, request):
        r"""标记资产是否核心

        :param request: Request instance for ModifyAssetCoreAttribute.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAssetCoreAttributeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAssetCoreAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetCoreAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetCoreAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetFilterView(self, request):
        r"""更新资产搜索视图

        :param request: Request instance for ModifyAssetFilterView.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAssetFilterViewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAssetFilterViewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetFilterView", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetFilterViewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetTag(self, request):
        r"""编辑资产标签

        :param request: Request instance for ModifyAssetTag.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetTag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetTags(self, request):
        r"""操作资产编辑标签

        :param request: Request instance for ModifyAssetTags.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetTagsByAssetInfo(self, request):
        r"""操作资产编辑标签

        :param request: Request instance for ModifyAssetTagsByAssetInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagsByAssetInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagsByAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetTagsByAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetTagsByAssetInfoResponse()
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
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBanModeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBanModeResponse`

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


    def ModifyBaselinePolicy(self, request):
        r"""新建或编辑一条基线策略。Policy.ID 为 0 视为新建，非 0 视为编辑；新建/编辑时 Name 必填，CheckAssetType 与 Type 需符合 CheckAssetType / PolicyType 枚举。

        :param request: Request instance for ModifyBaselinePolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBaselinePolicyResponse`

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


    def ModifyBaselinePolicyEnable(self, request):
        r"""批量启用或停用基线策略。停用后的策略将不再参与扫描与统计。

        :param request: Request instance for ModifyBaselinePolicyEnable.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBaselinePolicyEnableRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBaselinePolicyEnableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselinePolicyEnable", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselinePolicyEnableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineSyncConf(self, request):
        r"""更新当前账号（管理员）的基线同步配置。AutoSync=true 时 TargetAppidList 不可为空，且元素不可为 0。

        :param request: Request instance for ModifyBaselineSyncConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineSyncConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineSyncConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineSyncConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineSyncConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineUserOtherConf(self, request):
        r"""更新当前账号的用户级基线配置（允许同步、离线清风险、Agent 扫描超时等）。

        :param request: Request instance for ModifyBaselineUserOtherConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineUserOtherConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineUserOtherConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineUserOtherConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineUserOtherConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineUserWeakPasswordConf(self, request):
        r"""更新当前账号的“用户弱口令”自定义字典。字典原文经服务端加密后存储；传空字符串视为清空。

        :param request: Request instance for ModifyBaselineUserWeakPasswordConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineUserWeakPasswordConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineUserWeakPasswordConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineUserWeakPasswordConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineUserWeakPasswordConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBruteAttackBanStatus(self, request):
        r"""设置暴力破解阻断开关状态

        :param request: Request instance for ModifyBruteAttackBanStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBruteAttackBanStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBruteAttackBanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBruteAttackBanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBruteAttackBanStatusResponse()
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
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBruteAttackRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBruteAttackRulesResponse`

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


    def ModifyCSIPLicenseBinds(self, request):
        r"""绑定主机授权或RASP授权到指定订单。异步执行，返回TaskId供查询进度。通过LicenseType指定授权版本（旗舰版/专业版/RASP）。

        :param request: Request instance for ModifyCSIPLicenseBinds.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPLicenseBindsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPLicenseBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCSIPLicenseBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCSIPLicenseBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCSIPLicenseUnBinds(self, request):
        r"""手动解绑主机授权。同步执行，直接返回结果。仅解绑主机授权（category=0，含专业版/旗舰版）。单订单模式下appid即可定位订单，无需传ResourceId。RASP解绑请用ModifyCSIPRaspLicenseUnBinds。

        :param request: Request instance for ModifyCSIPLicenseUnBinds.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPLicenseUnBindsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPLicenseUnBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCSIPLicenseUnBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCSIPLicenseUnBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCSIPRaspLicenseBinds(self, request):
        r"""绑定 RASP / 旗舰版授权到指定订单。异步执行，返回TaskId供查询进度。LicenseType=rasp 绑 RASP，LicenseType=enterprise_hp 绑旗舰版主机授权；AssetType 区分主机/容器节点/EKS。

        :param request: Request instance for ModifyCSIPRaspLicenseBinds.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPRaspLicenseBindsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPRaspLicenseBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCSIPRaspLicenseBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCSIPRaspLicenseBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCSIPRaspLicenseUnBinds(self, request):
        r"""手动解绑RASP授权。同步执行，直接返回结果。仅解绑RASP授权（category=1），无解绑次数限制。单订单模式下appid即可定位订单，无需传ResourceId。

        :param request: Request instance for ModifyCSIPRaspLicenseUnBinds.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPRaspLicenseUnBindsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPRaspLicenseUnBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCSIPRaspLicenseUnBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCSIPRaspLicenseUnBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterDefendStatus(self, request):
        r"""修改集群防护状态

        :param request: Request instance for ModifyClusterDefendStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyClusterDefendStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyClusterDefendStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterDefendStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterDefendStatusResponse()
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


    def ModifyCspmShardConfig(self, request):
        r"""更新CSPM自动配额管理者共享开关

        :param request: Request instance for ModifyCspmShardConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCspmShardConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCspmShardConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCspmShardConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCspmShardConfigResponse()
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


    def ModifyDspmAuditFilterStrategy(self, request):
        r"""修改Dspm审计过滤策略

        :param request: Request instance for ModifyDspmAuditFilterStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAuditFilterStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAuditFilterStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAuditFilterStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAuditFilterStrategyResponse()
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


    def ModifyDspmCkafkaSave(self, request):
        r"""租户Ckafka配置保存

        :param request: Request instance for ModifyDspmCkafkaSave.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaSaveRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaSaveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmCkafkaSave", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmCkafkaSaveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmCkafkaStart(self, request):
        r"""日志投递开启

        :param request: Request instance for ModifyDspmCkafkaStart.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaStartRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaStartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmCkafkaStart", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmCkafkaStartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmCkafkaStop(self, request):
        r"""日志类型投递关闭

        :param request: Request instance for ModifyDspmCkafkaStop.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaStopRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaStopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmCkafkaStop", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmCkafkaStopResponse()
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


    def ModifyDspmLogDeliveryType(self, request):
        r"""修改日志投递配置信息

        :param request: Request instance for ModifyDspmLogDeliveryType.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmLogDeliveryTypeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmLogDeliveryTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmLogDeliveryType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmLogDeliveryTypeResponse()
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


    def ModifyEdrExcludeNetworkSegments(self, request):
        r"""修改日志采集例外网段配置，支持IP/IP段/CIDR格式，最多可添加100条

        :param request: Request instance for ModifyEdrExcludeNetworkSegments.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEdrExcludeNetworkSegmentsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEdrExcludeNetworkSegmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdrExcludeNetworkSegments", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdrExcludeNetworkSegmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdrLogCollectPath(self, request):
        r"""修改应用日志采集路径配置

        :param request: Request instance for ModifyEdrLogCollectPath.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEdrLogCollectPathRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEdrLogCollectPathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdrLogCollectPath", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdrLogCollectPathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExposureAutoTagRule(self, request):
        r"""云边界自动打标-更新规则

        :param request: Request instance for ModifyExposureAutoTagRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyExposureAutoTagRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyExposureAutoTagRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExposureAutoTagRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExposureAutoTagRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExposureAutoTagRuleStatus(self, request):
        r"""云边界自动打标-启停规则

        :param request: Request instance for ModifyExposureAutoTagRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyExposureAutoTagRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyExposureAutoTagRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExposureAutoTagRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExposureAutoTagRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExposureTag(self, request):
        r"""更新云边界自定义标签

        :param request: Request instance for ModifyExposureTag.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyExposureTagRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyExposureTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExposureTag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExposureTagResponse()
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


    def ModifyImageRegistry(self, request):
        r"""修改镜像仓库信息

        :param request: Request instance for ModifyImageRegistry.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyImageRegistryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyImageRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageRegistryTimedScanTaskConfig(self, request):
        r"""修改镜像仓库定时扫描任务配置

        :param request: Request instance for ModifyImageRegistryTimedScanTaskConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyImageRegistryTimedScanTaskConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyImageRegistryTimedScanTaskConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageRegistryTimedScanTaskConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageRegistryTimedScanTaskConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageSensitiveWhitelist(self, request):
        r"""修改容器镜像敏感信息白名单

        :param request: Request instance for ModifyImageSensitiveWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyImageSensitiveWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyImageSensitiveWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageSensitiveWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageSensitiveWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageVirusWhitelist(self, request):
        r"""查询资产数据库信息

        :param request: Request instance for ModifyImageVirusWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyImageVirusWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyImageVirusWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageVirusWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageVirusWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageVulWhitelist(self, request):
        r"""修改容器镜像漏洞白名单

        :param request: Request instance for ModifyImageVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyImageVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyImageVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageVulWhitelistResponse()
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
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyLoginWhiteRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyLoginWhiteRecordResponse`

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
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyMachineAutoClearConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyMachineAutoClearConfigResponse`

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


    def ModifyMachinesLoginType(self, request):
        r"""批量修改主机登录方式

        :param request: Request instance for ModifyMachinesLoginType.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyMachinesLoginTypeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyMachinesLoginTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMachinesLoginType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMachinesLoginTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMalwareTimingScanSettings(self, request):
        r"""修改文件查杀定时扫描配置，包含扫描周期、检测模式、资产范围、引擎选择、隔离配置等

        :param request: Request instance for ModifyMalwareTimingScanSettings.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyMalwareTimingScanSettingsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyMalwareTimingScanSettingsResponse`

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


    def ModifyNFSScanConf(self, request):
        r"""新增或更新NFS扫描全局配置

        :param request: Request instance for ModifyNFSScanConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNFSScanConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNFSScanConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNFSScanConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNFSScanConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNFSScanHost(self, request):
        r"""关闭进程守护功能

        :param request: Request instance for ModifyNFSScanHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNFSScanHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNFSScanHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNFSScanHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNFSScanHostResponse()
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


    def ModifyNotifyAgentOfflineDuration(self, request):
        r"""修改客户端离线时长

        :param request: Request instance for ModifyNotifyAgentOfflineDuration.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyAgentOfflineDurationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyAgentOfflineDurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifyAgentOfflineDuration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifyAgentOfflineDurationResponse()
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


    def ModifyNotifyMember(self, request):
        r"""修改通知成员账号

        :param request: Request instance for ModifyNotifyMember.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyMemberRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifyMember", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifyMemberResponse()
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


    def ModifyNotifySettingAk(self, request):
        r"""修改通知设置（云API风险治理）

        :param request: Request instance for ModifyNotifySettingAk.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingAkRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingAkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifySettingAk", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifySettingAkResponse()
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


    def ModifyPayConfig(self, request):
        r"""修改自动扩容配置（多模块可扩展，本期仅主机安全模块）。

        「自动扩容」为面向用户的对外概念，等价于底层自动加购(auto_repurchase)：当账号有新增资产时，自动加购所需授权。

        补充说明：
        1. 本期仅实现主机安全模块 HostConfig；后续可扩展容器安全、AI-Agent 安全等命名模块字段，各模块配置字段可异构；
        2. 部分更新语义：模块对象为空表示该模块不修改，模块内字段为空表示该字段不修改；
        3. HostConfig.Switch 联动映射 auto_repurchase_switch；auto_bind_switch（自动绑定）恒开，不由本接口改动；
        4. 自动续费(renew_flag) 不由本接口改动；额度/用量请调用 DescribeLicenseStatus；
        5. 顶部「自动扩容」总开关状态由前端按各模块开关聚合，后端不存储、不返回全局开关。

        :param request: Request instance for ModifyPayConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyPayConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyPayConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPayConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPayConfigResponse()
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


    def ModifyProtectionSetting(self, request):
        r"""重保防护包防护设置

        :param request: Request instance for ModifyProtectionSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyProtectionSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyProtectionSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProtectionSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProtectionSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRaspLicenseBinds(self, request):
        r"""重保防护授权包绑定

        :param request: Request instance for ModifyRaspLicenseBinds.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyRaspLicenseBindsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyRaspLicenseBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRaspLicenseBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRaspLicenseBindsResponse()
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


    def ModifyRiskScanCronConfig(self, request):
        r"""更新周期扫描计划

        :param request: Request instance for ModifyRiskScanCronConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyRiskScanCronConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyRiskScanCronConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskScanCronConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskScanCronConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxACLRule(self, request):
        r"""修改已有的 ACL 用户规则。未传字段保持原值，支持部分字段更新

        :param request: Request instance for ModifySandboxACLRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxACLRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxACLRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxACLRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxACLRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxACLRuleStatus(self, request):
        r"""批量切换 ACL 用户规则的启禁用状态。任一规则不存在、属于其他租户或已删除时整体返回错误

        :param request: Request instance for ModifySandboxACLRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxACLRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxACLRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxACLRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxACLRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxAlertStatus(self, request):
        r"""批量更新流量沙箱告警（覆盖 ACL / DLP / LLM 审计三类）。通过 AlertType + BelongAssetType 定位告警来源。Status 支持 HANDLED / IGNORE 修改状态，以及 DELETE 删除。任一告警 ID 不存在或属于其他租户时整体返回错误。注：加白（PASS）不经本接口，由 Create/Modify***Rule 通过 AlertID 回写触发

        :param request: Request instance for ModifySandboxAlertStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxAlertStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxAlertStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxAlertStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxAlertStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxDLPRule(self, request):
        r"""修改已存在的 DLP 用户规则。未传字段保持原值，支持部分字段更新；不支持修改 BelongAssetType

        :param request: Request instance for ModifySandboxDLPRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxDLPRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxDLPRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxDLPRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxDLPRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxDLPRuleStatus(self, request):
        r"""批量切换 DLP 用户规则的启禁用状态。任一规则不存在、属于其他租户或已删除时整体返回错误

        :param request: Request instance for ModifySandboxDLPRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxDLPRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxDLPRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxDLPRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxDLPRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxFileRule(self, request):
        r"""修改命令沙箱文件访问规则

        :param request: Request instance for ModifySandboxFileRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxFileRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxFileRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxFileRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxFileRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxFileRuleStatus(self, request):
        r"""批量启用或禁用命令沙箱文件访问规则

        :param request: Request instance for ModifySandboxFileRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxFileRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxFileRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxFileRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxFileRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxLLMAuditRule(self, request):
        r"""修改已有的 LLM 审计用户规则。未传字段保持原值，支持部分字段更新

        :param request: Request instance for ModifySandboxLLMAuditRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxLLMAuditRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxLLMAuditRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxLLMAuditRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxLLMAuditRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxLLMAuditRuleStatus(self, request):
        r"""批量切换 LLM 审计用户规则的启禁用状态。任一规则不存在、属于其他租户或已删除时整体返回错误

        :param request: Request instance for ModifySandboxLLMAuditRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxLLMAuditRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxLLMAuditRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxLLMAuditRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxLLMAuditRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityScoreRule(self, request):
        r"""修改安全评分规则，必须传入完整规则集

        :param request: Request instance for ModifySecurityScoreRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySecurityScoreRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySecurityScoreRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityScoreRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityScoreRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyShareUserAK(self, request):
        r"""编辑ak监测账号

        :param request: Request instance for ModifyShareUserAK.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserAKRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserAKResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyShareUserAK", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyShareUserAKResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyShareUserCSPM(self, request):
        r"""编辑CSPM共享账号

        :param request: Request instance for ModifyShareUserCSPM.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserCSPMRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserCSPMResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyShareUserCSPM", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyShareUserCSPMResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyShareUserDspm(self, request):
        r"""编辑dspm监测账号

        :param request: Request instance for ModifyShareUserDspm.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserDspmRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserDspmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyShareUserDspm", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyShareUserDspmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySkillScanAlertStatus(self, request):
        r"""批量修改 Skill 安全检测告警的处理状态

        :param request: Request instance for ModifySkillScanAlertStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySkillScanAlertStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySkillScanAlertStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySkillScanAlertStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySkillScanAlertStatusResponse()
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


    def ModifyWebhookPolicy(self, request):
        r"""新增或修改一条通知策略。ID > 0 表示修改；ID = 0 或不传表示新增。MemberAppIds 配置为空时，策略仅作用于当前主账号事件；非空时同时作用于自身账号 + 所列成员账号。

        :param request: Request instance for ModifyWebhookPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebhookPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebhookPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebhookPolicyStatus(self, request):
        r"""切换通知策略的启用状态。

        :param request: Request instance for ModifyWebhookPolicyStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookPolicyStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebhookPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebhookPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebhookReceiver(self, request):
        r"""新增或修改一个接收机器人。ID > 0 表示修改已有记录；ID = 0 或不传表示新增。机器人类型由 Type 字段决定，Type=WEBHOOK 时 WebhookAddr 必填，Type=SCF 时 SCFRegion/Namespace/FunctionName/FunctionVersion/Alias/MaxWaitSeconds 全部必填。修改时不允许变更 Type

        :param request: Request instance for ModifyWebhookReceiver.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookReceiverRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebhookReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebhookReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OperateRisk(self, request):
        r"""风险操作示例

        :param request: Request instance for OperateRisk.
        :type request: :class:`tencentcloud.csip.v20221121.models.OperateRiskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.OperateRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateRisk", params, headers=headers)
            response = json.loads(body)
            model = models.OperateRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OperateRiskRulePolicy(self, request):
        r"""自定义风险规则

        :param request: Request instance for OperateRiskRulePolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.OperateRiskRulePolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.OperateRiskRulePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateRiskRulePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.OperateRiskRulePolicyResponse()
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


    def ScanBaselineAssetItemList(self, request):
        r"""对单个资产的部分检测项发起重新扫描（资产详情页“重新扫描”入口）。

        :param request: Request instance for ScanBaselineAssetItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanBaselineAssetItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanBaselineAssetItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanBaselineAssetItemList", params, headers=headers)
            response = json.loads(body)
            model = models.ScanBaselineAssetItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanBaselineItemList(self, request):
        r"""对指定策略下的一批检测项发起重新扫描（策略详情页“检测项”维度的复扫入口）。

        :param request: Request instance for ScanBaselineItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanBaselineItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanBaselineItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanBaselineItemList", params, headers=headers)
            response = json.loads(body)
            model = models.ScanBaselineItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanBaselinePolicyList(self, request):
        r"""对一批基线策略发起整体重新扫描（策略列表页“一键扫描”入口），按策略命中的资产范围全量重扫。

        :param request: Request instance for ScanBaselinePolicyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanBaselinePolicyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanBaselinePolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanBaselinePolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.ScanBaselinePolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanBaselineRiskList(self, request):
        r"""对一批风险记录发起重新扫描，常用于“风险列表”页批量勾选风险后的复扫场景。

        :param request: Request instance for ScanBaselineRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanBaselineRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanBaselineRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanBaselineRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.ScanBaselineRiskListResponse()
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


    def SendDspmCkafkaTest(self, request):
        r"""租户Ckafka联通性测试

        :param request: Request instance for SendDspmCkafkaTest.
        :type request: :class:`tencentcloud.csip.v20221121.models.SendDspmCkafkaTestRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.SendDspmCkafkaTestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendDspmCkafkaTest", params, headers=headers)
            response = json.loads(body)
            model = models.SendDspmCkafkaTestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartOrModifyPreventUninstall(self, request):
        r"""开启或者修改防卸载功能配置

        :param request: Request instance for StartOrModifyPreventUninstall.
        :type request: :class:`tencentcloud.csip.v20221121.models.StartOrModifyPreventUninstallRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StartOrModifyPreventUninstallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartOrModifyPreventUninstall", params, headers=headers)
            response = json.loads(body)
            model = models.StartOrModifyPreventUninstallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartOrModifyProcessDaemon(self, request):
        r"""开启或者修改进程守护功能配置

        :param request: Request instance for StartOrModifyProcessDaemon.
        :type request: :class:`tencentcloud.csip.v20221121.models.StartOrModifyProcessDaemonRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StartOrModifyProcessDaemonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartOrModifyProcessDaemon", params, headers=headers)
            response = json.loads(body)
            model = models.StartOrModifyProcessDaemonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopBaselineScanTask(self, request):
        r"""停止指定的基线扫描主任务，仅对处于 INIT / SUBTASK_CREATING / SCANNING 状态的任务生效。

        :param request: Request instance for StopBaselineScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopBaselineScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopBaselineScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopBaselineScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopBaselineScanTaskResponse()
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


    def StopImageRegistryScanTask(self, request):
        r"""停止镜像仓库镜像扫描任务

        :param request: Request instance for StopImageRegistryScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopImageRegistryScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopImageRegistryScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopImageRegistryScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopImageRegistryScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopPreventUninstall(self, request):
        r"""关闭防卸载功能

        :param request: Request instance for StopPreventUninstall.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopPreventUninstallRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopPreventUninstallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopPreventUninstall", params, headers=headers)
            response = json.loads(body)
            model = models.StopPreventUninstallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopProcessDaemon(self, request):
        r"""关闭进程守护功能

        :param request: Request instance for StopProcessDaemon.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopProcessDaemonRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopProcessDaemonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopProcessDaemon", params, headers=headers)
            response = json.loads(body)
            model = models.StopProcessDaemonResponse()
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


    def SyncImageRegistry(self, request):
        r"""镜像仓库同步

        :param request: Request instance for SyncImageRegistry.
        :type request: :class:`tencentcloud.csip.v20221121.models.SyncImageRegistryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.SyncImageRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncImageRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.SyncImageRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TestWebhookReceiver(self, request):
        r"""向指定的接收机器人发送一条测试消息，验证可达性与配置正确性。对应表格行内的「测试」按钮。

        :param request: Request instance for TestWebhookReceiver.
        :type request: :class:`tencentcloud.csip.v20221121.models.TestWebhookReceiverRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.TestWebhookReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TestWebhookReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.TestWebhookReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UninstallClusterAgent(self, request):
        r"""卸载集群容器安全Agent。

        :param request: Request instance for UninstallClusterAgent.
        :type request: :class:`tencentcloud.csip.v20221121.models.UninstallClusterAgentRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UninstallClusterAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallClusterAgent", params, headers=headers)
            response = json.loads(body)
            model = models.UninstallClusterAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UninstallKeySandboxSkill(self, request):
        r"""从指定的机器实例上卸载密钥沙箱SKILL。支持批量操作，一次可传入多个实例ID。卸载后，目标机器上的AI Agent将无法再通过密钥沙箱代理访问凭据。未安装的实例重复调用不会报错（幂等），直接视为成功。

        :param request: Request instance for UninstallKeySandboxSkill.
        :type request: :class:`tencentcloud.csip.v20221121.models.UninstallKeySandboxSkillRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UninstallKeySandboxSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallKeySandboxSkill", params, headers=headers)
            response = json.loads(body)
            model = models.UninstallKeySandboxSkillResponse()
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


    def UpdateClusterOwner(self, request):
        r"""绑定、更新集群负责人

        :param request: Request instance for UpdateClusterOwner.
        :type request: :class:`tencentcloud.csip.v20221121.models.UpdateClusterOwnerRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UpdateClusterOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateClusterOwner", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateClusterOwnerResponse()
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