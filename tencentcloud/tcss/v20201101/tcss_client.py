# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.tcss.v20201101 import models


class TcssClient(AbstractClient):
    _apiVersion = '2020-11-01'
    _endpoint = 'tcss.tencentcloudapi.com'
    _service = 'tcss'


    def AddAssetImageRegistryRegistryDetail(self, request):
        """新增单个镜像仓库详细信息

        :param request: Request instance for AddAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddAssetImageRegistryRegistryDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddAssetImageRegistryRegistryDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddCompliancePolicyItemToWhitelist(self, request):
        """将指定的检测项添加到白名单中，不显示未通过结果。

        :param request: Request instance for AddCompliancePolicyItemToWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddCompliancePolicyItemToWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddCompliancePolicyItemToWhitelistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddCompliancePolicyItemToWhitelist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddCompliancePolicyItemToWhitelistResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditAbnormalProcessRule(self, request):
        """添加编辑运行时异常进程策略

        :param request: Request instance for AddEditAbnormalProcessRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditAbnormalProcessRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditAbnormalProcessRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddEditAbnormalProcessRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditAbnormalProcessRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditAccessControlRule(self, request):
        """添加编辑运行时访问控制策略

        :param request: Request instance for AddEditAccessControlRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditAccessControlRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditAccessControlRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddEditAccessControlRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditAccessControlRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditReverseShellWhiteList(self, request):
        """添加编辑运行时反弹shell白名单

        :param request: Request instance for AddEditReverseShellWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditReverseShellWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditReverseShellWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddEditReverseShellWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditReverseShellWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditRiskSyscallWhiteList(self, request):
        """添加编辑运行时高危系统调用白名单

        :param request: Request instance for AddEditRiskSyscallWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditRiskSyscallWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditRiskSyscallWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddEditRiskSyscallWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditRiskSyscallWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditWarningRules(self, request):
        """添加编辑告警策略

        :param request: Request instance for AddEditWarningRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditWarningRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditWarningRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddEditWarningRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditWarningRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckRepeatAssetImageRegistry(self, request):
        """检查单个镜像仓库名是否重复

        :param request: Request instance for CheckRepeatAssetImageRegistry.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CheckRepeatAssetImageRegistryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CheckRepeatAssetImageRegistryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckRepeatAssetImageRegistry", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckRepeatAssetImageRegistryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssetImageRegistryScanTask(self, request):
        """镜像仓库创建镜像扫描任务

        :param request: Request instance for CreateAssetImageRegistryScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAssetImageRegistryScanTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssetImageRegistryScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssetImageRegistryScanTaskOneKey(self, request):
        """镜像仓库创建镜像一键扫描任务

        :param request: Request instance for CreateAssetImageRegistryScanTaskOneKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskOneKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskOneKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAssetImageRegistryScanTaskOneKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssetImageRegistryScanTaskOneKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssetImageScanSetting(self, request):
        """添加容器安全镜像扫描设置

        :param request: Request instance for CreateAssetImageScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAssetImageScanSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssetImageScanSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssetImageScanTask(self, request):
        """容器安全创建镜像扫描任务

        :param request: Request instance for CreateAssetImageScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAssetImageScanTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssetImageScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCheckComponent(self, request):
        """安装检查组件，创建防护容器

        :param request: Request instance for CreateCheckComponent.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateCheckComponentRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateCheckComponentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCheckComponent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCheckComponentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateClusterCheckTask(self, request):
        """创建集群检查任务，用户检查用户的集群相关风险项

        :param request: Request instance for CreateClusterCheckTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateClusterCheckTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateClusterCheckTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClusterCheckTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterCheckTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateComplianceTask(self, request):
        """创建合规检查任务，在资产级别触发重新检测时使用。

        :param request: Request instance for CreateComplianceTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateComplianceTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateComplianceTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateComplianceTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateComplianceTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateExportComplianceStatusListJob(self, request):
        """创建一个导出安全合规信息的任务

        :param request: Request instance for CreateExportComplianceStatusListJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateExportComplianceStatusListJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateExportComplianceStatusListJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateExportComplianceStatusListJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateExportComplianceStatusListJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOrModifyPostPayCores(self, request):
        """CreateOrModifyPostPayCores  创建或者编辑弹性计费上限

        :param request: Request instance for CreateOrModifyPostPayCores.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateOrModifyPostPayCoresRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateOrModifyPostPayCoresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateOrModifyPostPayCores", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateOrModifyPostPayCoresResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRefreshTask(self, request):
        """下发刷新任务，会刷新资产信息

        :param request: Request instance for CreateRefreshTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateRefreshTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateRefreshTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRefreshTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRefreshTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVirusScanAgain(self, request):
        """运行时文件查杀重新检测

        :param request: Request instance for CreateVirusScanAgain.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanAgainRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanAgainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVirusScanAgain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVirusScanAgainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVirusScanTask(self, request):
        """运行时文件查杀一键扫描

        :param request: Request instance for CreateVirusScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVirusScanTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVirusScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAbnormalProcessRules(self, request):
        """删除运行异常进程策略

        :param request: Request instance for DeleteAbnormalProcessRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteAbnormalProcessRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteAbnormalProcessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAbnormalProcessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAbnormalProcessRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAccessControlRules(self, request):
        """删除运行访问控制策略

        :param request: Request instance for DeleteAccessControlRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteAccessControlRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteAccessControlRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccessControlRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccessControlRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCompliancePolicyItemFromWhitelist(self, request):
        """从白名单中删除将指定的检测项。

        :param request: Request instance for DeleteCompliancePolicyItemFromWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteCompliancePolicyItemFromWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteCompliancePolicyItemFromWhitelistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCompliancePolicyItemFromWhitelist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCompliancePolicyItemFromWhitelistResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteReverseShellWhiteLists(self, request):
        """删除运行时反弹shell白名单

        :param request: Request instance for DeleteReverseShellWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteReverseShellWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteReverseShellWhiteListsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteReverseShellWhiteLists", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReverseShellWhiteListsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRiskSyscallWhiteLists(self, request):
        """删除运行时高危系统调用白名单

        :param request: Request instance for DeleteRiskSyscallWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteRiskSyscallWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteRiskSyscallWhiteListsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRiskSyscallWhiteLists", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRiskSyscallWhiteListsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessDetail(self, request):
        """查询运行时异常进程事件详细信息

        :param request: Request instance for DescribeAbnormalProcessDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAbnormalProcessDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessEvents(self, request):
        """查询运行时异常进程事件列表信息

        :param request: Request instance for DescribeAbnormalProcessEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAbnormalProcessEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessEventsExport(self, request):
        """查询运行时异常进程事件列表信息导出

        :param request: Request instance for DescribeAbnormalProcessEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAbnormalProcessEventsExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessEventsExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessRuleDetail(self, request):
        """查询运行时异常策略详细信息

        :param request: Request instance for DescribeAbnormalProcessRuleDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRuleDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRuleDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAbnormalProcessRuleDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessRuleDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessRules(self, request):
        """查询运行时异常进程策略列表信息

        :param request: Request instance for DescribeAbnormalProcessRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAbnormalProcessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessRulesExport(self, request):
        """查询运行时异常进程策略列表信息导出

        :param request: Request instance for DescribeAbnormalProcessRulesExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAbnormalProcessRulesExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessRulesExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlDetail(self, request):
        """查询运行时访问控制事件的详细信息

        :param request: Request instance for DescribeAccessControlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessControlDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlEvents(self, request):
        """查询运行时访问控制事件列表

        :param request: Request instance for DescribeAccessControlEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessControlEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlEventsExport(self, request):
        """查询运行时访问控制事件列表导出

        :param request: Request instance for DescribeAccessControlEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessControlEventsExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlEventsExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlRuleDetail(self, request):
        """查询运行时访问控制策略详细信息

        :param request: Request instance for DescribeAccessControlRuleDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRuleDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRuleDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessControlRuleDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlRuleDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlRules(self, request):
        """查询运行访问控制策略列表信息

        :param request: Request instance for DescribeAccessControlRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessControlRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlRulesExport(self, request):
        """查询运行时访问控制策略列表导出

        :param request: Request instance for DescribeAccessControlRulesExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessControlRulesExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlRulesExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAffectedClusterCount(self, request):
        """获取受影响的集群数量，返回数量

        :param request: Request instance for DescribeAffectedClusterCount.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedClusterCountRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedClusterCountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAffectedClusterCount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAffectedClusterCountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAffectedNodeList(self, request):
        """查询节点类型的影响范围，返回节点列表

        :param request: Request instance for DescribeAffectedNodeList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedNodeListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedNodeListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAffectedNodeList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAffectedNodeListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAffectedWorkloadList(self, request):
        """查询workload类型的影响范围，返回workload列表

        :param request: Request instance for DescribeAffectedWorkloadList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedWorkloadListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedWorkloadListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAffectedWorkloadList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAffectedWorkloadListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetAppServiceList(self, request):
        """容器安全查询app服务列表

        :param request: Request instance for DescribeAssetAppServiceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetAppServiceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetAppServiceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetAppServiceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetAppServiceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetComponentList(self, request):
        """容器安全搜索查询容器组件列表

        :param request: Request instance for DescribeAssetComponentList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetComponentListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetComponentListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetComponentList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetComponentListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetContainerDetail(self, request):
        """查询容器详细信息

        :param request: Request instance for DescribeAssetContainerDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetContainerDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetContainerDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetContainerList(self, request):
        """搜索查询容器列表

        :param request: Request instance for DescribeAssetContainerList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetContainerList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetContainerListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetDBServiceList(self, request):
        """容器安全查询db服务列表

        :param request: Request instance for DescribeAssetDBServiceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetDBServiceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetDBServiceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetDBServiceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetDBServiceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetHostDetail(self, request):
        """查询主机详细信息

        :param request: Request instance for DescribeAssetHostDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetHostDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetHostDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetHostList(self, request):
        """容器安全搜索查询主机列表

        :param request: Request instance for DescribeAssetHostList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetHostList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetHostListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageBindRuleInfo(self, request):
        """镜像绑定规则列表信息，包含运行时访问控制和异常进程公用

        :param request: Request instance for DescribeAssetImageBindRuleInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageBindRuleInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageBindRuleInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageBindRuleInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageBindRuleInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageDetail(self, request):
        """查询镜像详细信息

        :param request: Request instance for DescribeAssetImageDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageHostList(self, request):
        """容器安全查询镜像关联主机

        :param request: Request instance for DescribeAssetImageHostList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageHostListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageHostListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageHostList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageHostListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageList(self, request):
        """容器安全搜索查询镜像列表

        :param request: Request instance for DescribeAssetImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageListExport(self, request):
        """容器安全搜索查询镜像列表导出

        :param request: Request instance for DescribeAssetImageListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageListExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryAssetStatus(self, request):
        """查看镜像仓库资产更新进度状态

        :param request: Request instance for DescribeAssetImageRegistryAssetStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryAssetStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryAssetStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryAssetStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryAssetStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryDetail(self, request):
        """镜像仓库镜像仓库列表详情

        :param request: Request instance for DescribeAssetImageRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryList(self, request):
        """镜像仓库镜像仓库列表

        :param request: Request instance for DescribeAssetImageRegistryList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryListExport(self, request):
        """镜像仓库镜像列表导出

        :param request: Request instance for DescribeAssetImageRegistryListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryListExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryRegistryDetail(self, request):
        """查看单个镜像仓库详细信息

        :param request: Request instance for DescribeAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryRegistryDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryRegistryDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryRegistryList(self, request):
        """镜像仓库仓库列表

        :param request: Request instance for DescribeAssetImageRegistryRegistryList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryRegistryList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryRegistryListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryRiskInfoList(self, request):
        """镜像仓库查询镜像高危行为列表

        :param request: Request instance for DescribeAssetImageRegistryRiskInfoList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskInfoListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryRiskInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryRiskInfoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryRiskListExport(self, request):
        """镜像仓库敏感信息列表导出

        :param request: Request instance for DescribeAssetImageRegistryRiskListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskListExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryRiskListExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryRiskListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryScanStatusOneKey(self, request):
        """镜像仓库查询一键镜像扫描状态

        :param request: Request instance for DescribeAssetImageRegistryScanStatusOneKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryScanStatusOneKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryScanStatusOneKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryScanStatusOneKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryScanStatusOneKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistrySummary(self, request):
        """镜像仓库查询镜像统计信息

        :param request: Request instance for DescribeAssetImageRegistrySummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistrySummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistrySummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistrySummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistrySummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryVirusList(self, request):
        """镜像仓库查询木马病毒列表

        :param request: Request instance for DescribeAssetImageRegistryVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryVirusList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryVirusListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryVirusListExport(self, request):
        """镜像仓库木马信息列表导出

        :param request: Request instance for DescribeAssetImageRegistryVirusListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryVirusListExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryVirusListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryVulList(self, request):
        """镜像仓库查询镜像漏洞列表

        :param request: Request instance for DescribeAssetImageRegistryVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryVulList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryVulListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryVulListExport(self, request):
        """镜像仓库漏洞列表导出

        :param request: Request instance for DescribeAssetImageRegistryVulListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRegistryVulListExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryVulListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRiskList(self, request):
        """容器安全查询镜像风险列表

        :param request: Request instance for DescribeAssetImageRiskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRiskList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRiskListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRiskListExport(self, request):
        """容器安全搜索查询镜像风险列表导出

        :param request: Request instance for DescribeAssetImageRiskListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageRiskListExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRiskListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageScanSetting(self, request):
        """获取镜像扫描设置信息

        :param request: Request instance for DescribeAssetImageScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageScanSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageScanSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageScanStatus(self, request):
        """容器安全查询镜像扫描状态

        :param request: Request instance for DescribeAssetImageScanStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageScanStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageScanStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageScanTask(self, request):
        """查询正在一键扫描的镜像扫描taskid

        :param request: Request instance for DescribeAssetImageScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageScanTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageSimpleList(self, request):
        """容器安全搜索查询镜像简略信息列表

        :param request: Request instance for DescribeAssetImageSimpleList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageSimpleListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageSimpleListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageSimpleList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageSimpleListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageVirusList(self, request):
        """容器安全查询镜像病毒列表

        :param request: Request instance for DescribeAssetImageVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageVirusList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageVirusListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageVirusListExport(self, request):
        """容器安全搜索查询镜像木马列表导出

        :param request: Request instance for DescribeAssetImageVirusListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageVirusListExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageVirusListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageVulList(self, request):
        """容器安全查询镜像漏洞列表

        :param request: Request instance for DescribeAssetImageVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageVulList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageVulListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageVulListExport(self, request):
        """容器安全搜索查询镜像漏洞列表导出

        :param request: Request instance for DescribeAssetImageVulListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetImageVulListExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageVulListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetPortList(self, request):
        """容器安全搜索查询端口占用列表

        :param request: Request instance for DescribeAssetPortList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetPortListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetPortListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetPortList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetPortListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetProcessList(self, request):
        """容器安全搜索查询进程列表

        :param request: Request instance for DescribeAssetProcessList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetProcessListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetProcessListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetProcessList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetProcessListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetSummary(self, request):
        """查询账户容器、镜像等统计信息

        :param request: Request instance for DescribeAssetSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetWebServiceList(self, request):
        """容器安全查询web服务列表

        :param request: Request instance for DescribeAssetWebServiceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetWebServiceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetWebServiceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetWebServiceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetWebServiceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCheckItemList(self, request):
        """查询所有检查项接口，返回总数和检查项列表

        :param request: Request instance for DescribeCheckItemList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCheckItemListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCheckItemListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCheckItemList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCheckItemListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterDetail(self, request):
        """查询单个集群的详细信息

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterSummary(self, request):
        """查询用户集群资产总览

        :param request: Request instance for DescribeClusterSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceAssetDetailInfo(self, request):
        """查询某个资产的详情

        :param request: Request instance for DescribeComplianceAssetDetailInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetDetailInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetDetailInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComplianceAssetDetailInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceAssetDetailInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceAssetList(self, request):
        """查询某类资产的列表

        :param request: Request instance for DescribeComplianceAssetList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComplianceAssetList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceAssetListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceAssetPolicyItemList(self, request):
        """查询某资产下的检测项列表

        :param request: Request instance for DescribeComplianceAssetPolicyItemList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetPolicyItemListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetPolicyItemListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComplianceAssetPolicyItemList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceAssetPolicyItemListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCompliancePeriodTaskList(self, request):
        """查询合规检测的定时任务列表

        :param request: Request instance for DescribeCompliancePeriodTaskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePeriodTaskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePeriodTaskListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCompliancePeriodTaskList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCompliancePeriodTaskListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCompliancePolicyItemAffectedAssetList(self, request):
        """按照 检测项 → 资产 的两级层次展开的第二层级：资产层级。

        :param request: Request instance for DescribeCompliancePolicyItemAffectedAssetList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedAssetListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedAssetListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCompliancePolicyItemAffectedAssetList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCompliancePolicyItemAffectedAssetListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCompliancePolicyItemAffectedSummary(self, request):
        """按照 检测项 → 资产 的两级层次展开的第一层级：检测项层级。

        :param request: Request instance for DescribeCompliancePolicyItemAffectedSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCompliancePolicyItemAffectedSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCompliancePolicyItemAffectedSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceScanFailedAssetList(self, request):
        """按照 资产 → 检测项 二层结构展示的信息。这里查询第一层 资产的通过率汇总信息。

        :param request: Request instance for DescribeComplianceScanFailedAssetList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceScanFailedAssetListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceScanFailedAssetListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComplianceScanFailedAssetList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceScanFailedAssetListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceTaskAssetSummary(self, request):
        """查询上次任务的资产通过率汇总信息

        :param request: Request instance for DescribeComplianceTaskAssetSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskAssetSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskAssetSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComplianceTaskAssetSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceTaskAssetSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceTaskPolicyItemSummaryList(self, request):
        """查询最近一次任务发现的检测项的汇总信息列表，按照 检测项 → 资产 的两级层次展开。

        :param request: Request instance for DescribeComplianceTaskPolicyItemSummaryList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskPolicyItemSummaryListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskPolicyItemSummaryListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComplianceTaskPolicyItemSummaryList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceTaskPolicyItemSummaryListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceWhitelistItemList(self, request):
        """查询白名单列表

        :param request: Request instance for DescribeComplianceWhitelistItemList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceWhitelistItemListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceWhitelistItemListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComplianceWhitelistItemList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceWhitelistItemListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeContainerAssetSummary(self, request):
        """查询容器资产概览信息

        :param request: Request instance for DescribeContainerAssetSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerAssetSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerAssetSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerAssetSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerAssetSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeContainerSecEventSummary(self, request):
        """查询容器安全未处理事件信息

        :param request: Request instance for DescribeContainerSecEventSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerSecEventSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerSecEventSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerSecEventSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerSecEventSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeEventDetail(self, request):
        """DescribeEscapeEventDetail  查询容器逃逸事件详情

        :param request: Request instance for DescribeEscapeEventDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEscapeEventDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeEventDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeEventInfo(self, request):
        """DescribeEscapeEventInfo 查询容器逃逸事件列表

        :param request: Request instance for DescribeEscapeEventInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEscapeEventInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeEventInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeEventsExport(self, request):
        """DescribeEscapeEventsExport  查询容器逃逸事件列表导出

        :param request: Request instance for DescribeEscapeEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventsExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEscapeEventsExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeEventsExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeRuleInfo(self, request):
        """DescribeEscapeRuleInfo 查询容器逃逸扫描规则信息

        :param request: Request instance for DescribeEscapeRuleInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeRuleInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeRuleInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEscapeRuleInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeRuleInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeSafeState(self, request):
        """DescribeEscapeSafeState 查询容器逃逸安全状态

        :param request: Request instance for DescribeEscapeSafeState.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeSafeStateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeSafeStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEscapeSafeState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeSafeStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExportJobResult(self, request):
        """查询导出任务的结果

        :param request: Request instance for DescribeExportJobResult.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeExportJobResultRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeExportJobResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeExportJobResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExportJobResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageAuthorizedInfo(self, request):
        """DescribeImageAuthorizedInfo  查询镜像授权信息

        :param request: Request instance for DescribeImageAuthorizedInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAuthorizedInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAuthorizedInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageAuthorizedInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageAuthorizedInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageRegistryTimingScanTask(self, request):
        """镜像仓库查看定时任务

        :param request: Request instance for DescribeImageRegistryTimingScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRegistryTimingScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRegistryTimingScanTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageRegistryTimingScanTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageRegistryTimingScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageRiskSummary(self, request):
        """查询本地镜像风险概览

        :param request: Request instance for DescribeImageRiskSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageRiskSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageRiskSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageRiskTendency(self, request):
        """查询容器安全本地镜像风险趋势

        :param request: Request instance for DescribeImageRiskTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskTendencyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageRiskTendency", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageRiskTendencyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageSimpleList(self, request):
        """DescribeImageSimpleList 查询全部镜像列表

        :param request: Request instance for DescribeImageSimpleList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageSimpleListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageSimpleListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageSimpleList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageSimpleListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePostPayDetail(self, request):
        """DescribePostPayDetail  查询后付费详情

        :param request: Request instance for DescribePostPayDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribePostPayDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribePostPayDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePostPayDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePostPayDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProVersionInfo(self, request):
        """DescribeProVersionInfo  查询专业版需购买信息

        :param request: Request instance for DescribeProVersionInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeProVersionInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeProVersionInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProVersionInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProVersionInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePurchaseStateInfo(self, request):
        """DescribePurchaseStateInfo 查询容器安全服务已购买信息

        :param request: Request instance for DescribePurchaseStateInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribePurchaseStateInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribePurchaseStateInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePurchaseStateInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurchaseStateInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRefreshTask(self, request):
        """查询刷新任务

        :param request: Request instance for DescribeRefreshTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRefreshTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRefreshTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRefreshTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRefreshTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReverseShellDetail(self, request):
        """查询运行时反弹shell事件详细信息

        :param request: Request instance for DescribeReverseShellDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReverseShellDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReverseShellEvents(self, request):
        """查询运行时反弹shell事件列表信息

        :param request: Request instance for DescribeReverseShellEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReverseShellEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReverseShellEventsExport(self, request):
        """查询运行时反弹shell事件列表信息导出

        :param request: Request instance for DescribeReverseShellEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReverseShellEventsExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellEventsExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReverseShellWhiteListDetail(self, request):
        """查询运行时反弹shell白名单详细信息

        :param request: Request instance for DescribeReverseShellWhiteListDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReverseShellWhiteListDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellWhiteListDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReverseShellWhiteLists(self, request):
        """查询运行时运行时反弹shell白名单列表信息

        :param request: Request instance for DescribeReverseShellWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReverseShellWhiteLists", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellWhiteListsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskList(self, request):
        """查询最近一次任务发现的风险项的信息列表，支持根据特殊字段进行过滤

        :param request: Request instance for DescribeRiskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRiskList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallDetail(self, request):
        """查询高危系统调用事件详细信息

        :param request: Request instance for DescribeRiskSyscallDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRiskSyscallDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallEvents(self, request):
        """查询运行时运行时高危系统调用列表信息

        :param request: Request instance for DescribeRiskSyscallEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRiskSyscallEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallEventsExport(self, request):
        """运行时高危系统调用列表导出

        :param request: Request instance for DescribeRiskSyscallEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsExportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRiskSyscallEventsExport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallEventsExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallNames(self, request):
        """查询运行时高危系统调用系统名称列表

        :param request: Request instance for DescribeRiskSyscallNames.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallNamesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallNamesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRiskSyscallNames", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallNamesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallWhiteListDetail(self, request):
        """查询运行时高危系统调用白名单详细信息

        :param request: Request instance for DescribeRiskSyscallWhiteListDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRiskSyscallWhiteListDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallWhiteListDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallWhiteLists(self, request):
        """查询运行时高危系统调用白名单列表信息

        :param request: Request instance for DescribeRiskSyscallWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRiskSyscallWhiteLists", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallWhiteListsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecEventsTendency(self, request):
        """查询容器运行时安全事件趋势

        :param request: Request instance for DescribeSecEventsTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecEventsTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecEventsTendencyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecEventsTendency", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecEventsTendencyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskResultSummary(self, request):
        """查询检查结果总览，返回受影响的节点数量，返回7天的数据，总共7个

        :param request: Request instance for DescribeTaskResultSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeTaskResultSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeTaskResultSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskResultSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResultSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUnfinishRefreshTask(self, request):
        """查询未完成的刷新资产任务信息

        :param request: Request instance for DescribeUnfinishRefreshTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeUnfinishRefreshTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeUnfinishRefreshTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUnfinishRefreshTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUnfinishRefreshTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserCluster(self, request):
        """安全概览和集群安全页进入调用该接口，查询用户集群相关信息。

        :param request: Request instance for DescribeUserCluster.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeUserClusterRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeUserClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserClusterResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeValueAddedSrvInfo(self, request):
        """DescribeValueAddedSrvInfo查询增值服务需购买信息

        :param request: Request instance for DescribeValueAddedSrvInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeValueAddedSrvInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeValueAddedSrvInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeValueAddedSrvInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeValueAddedSrvInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusDetail(self, request):
        """运行时查询木马文件信息

        :param request: Request instance for DescribeVirusDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVirusDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusList(self, request):
        """运行时文件查杀事件列表

        :param request: Request instance for DescribeVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVirusList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusMonitorSetting(self, request):
        """运行时查询文件查杀实时监控设置

        :param request: Request instance for DescribeVirusMonitorSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusMonitorSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusMonitorSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVirusMonitorSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusMonitorSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusScanSetting(self, request):
        """运行时查询文件查杀设置

        :param request: Request instance for DescribeVirusScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVirusScanSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusScanSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusScanTaskStatus(self, request):
        """运行时查询文件查杀任务状态

        :param request: Request instance for DescribeVirusScanTaskStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVirusScanTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusScanTaskStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusScanTimeoutSetting(self, request):
        """运行时文件扫描超时设置查询

        :param request: Request instance for DescribeVirusScanTimeoutSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTimeoutSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTimeoutSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVirusScanTimeoutSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusScanTimeoutSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusSummary(self, request):
        """运行时查询木马概览信息

        :param request: Request instance for DescribeVirusSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVirusSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusTaskList(self, request):
        """运行时查询文件查杀任务列表

        :param request: Request instance for DescribeVirusTaskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusTaskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusTaskListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVirusTaskList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusTaskListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWarningRules(self, request):
        """获取告警策略列表

        :param request: Request instance for DescribeWarningRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeWarningRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeWarningRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWarningRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWarningRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExportVirusList(self, request):
        """运行时文件查杀事件列表导出

        :param request: Request instance for ExportVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ExportVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ExportVirusListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportVirusList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportVirusListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InitializeUserComplianceEnvironment(self, request):
        """为客户初始化合规基线的使用环境，创建必要的数据和选项。

        :param request: Request instance for InitializeUserComplianceEnvironment.
        :type request: :class:`tencentcloud.tcss.v20201101.models.InitializeUserComplianceEnvironmentRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.InitializeUserComplianceEnvironmentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitializeUserComplianceEnvironment", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitializeUserComplianceEnvironmentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAbnormalProcessRuleStatus(self, request):
        """修改运行时异常进程策略的开启关闭状态

        :param request: Request instance for ModifyAbnormalProcessRuleStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessRuleStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessRuleStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAbnormalProcessRuleStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAbnormalProcessRuleStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAbnormalProcessStatus(self, request):
        """修改异常进程事件的状态信息

        :param request: Request instance for ModifyAbnormalProcessStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAbnormalProcessStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAbnormalProcessStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccessControlRuleStatus(self, request):
        """修改运行时访问控制策略的状态，启用或者禁用

        :param request: Request instance for ModifyAccessControlRuleStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlRuleStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlRuleStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccessControlRuleStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessControlRuleStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccessControlStatus(self, request):
        """修改运行时访问控制事件状态信息

        :param request: Request instance for ModifyAccessControlStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccessControlStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessControlStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAsset(self, request):
        """容器安全主机资产刷新

        :param request: Request instance for ModifyAsset.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAsset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAssetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAssetImageRegistryScanStop(self, request):
        """镜像仓库停止镜像扫描任务

        :param request: Request instance for ModifyAssetImageRegistryScanStop.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAssetImageRegistryScanStop", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAssetImageRegistryScanStopResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAssetImageRegistryScanStopOneKey(self, request):
        """镜像仓库停止镜像一键扫描任务

        :param request: Request instance for ModifyAssetImageRegistryScanStopOneKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopOneKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopOneKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAssetImageRegistryScanStopOneKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAssetImageRegistryScanStopOneKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAssetImageScanStop(self, request):
        """容器安全停止镜像扫描

        :param request: Request instance for ModifyAssetImageScanStop.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageScanStopRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageScanStopResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAssetImageScanStop", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAssetImageScanStopResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCompliancePeriodTask(self, request):
        """修改定时任务的设置，包括检测周期、开启/禁用合规基准。

        :param request: Request instance for ModifyCompliancePeriodTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyCompliancePeriodTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyCompliancePeriodTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCompliancePeriodTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCompliancePeriodTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEscapeEventStatus(self, request):
        """ModifyEscapeEventStatus  修改容器逃逸扫描事件状态

        :param request: Request instance for ModifyEscapeEventStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeEventStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeEventStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyEscapeEventStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEscapeEventStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEscapeRule(self, request):
        """ModifyEscapeRule  修改容器逃逸扫描规则信息

        :param request: Request instance for ModifyEscapeRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyEscapeRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEscapeRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyReverseShellStatus(self, request):
        """修改反弹shell事件的状态信息

        :param request: Request instance for ModifyReverseShellStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyReverseShellStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyReverseShellStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyReverseShellStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyReverseShellStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRiskSyscallStatus(self, request):
        """修改高危系统调用事件的状态信息

        :param request: Request instance for ModifyRiskSyscallStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyRiskSyscallStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyRiskSyscallStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRiskSyscallStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRiskSyscallStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVirusFileStatus(self, request):
        """运行时更新木马文件事件状态

        :param request: Request instance for ModifyVirusFileStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusFileStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusFileStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVirusFileStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVirusFileStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVirusMonitorSetting(self, request):
        """运行时更新文件查杀实时监控设置

        :param request: Request instance for ModifyVirusMonitorSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusMonitorSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusMonitorSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVirusMonitorSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVirusMonitorSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVirusScanSetting(self, request):
        """运行时更新文件查杀设置

        :param request: Request instance for ModifyVirusScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVirusScanSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVirusScanSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVirusScanTimeoutSetting(self, request):
        """运行时文件扫描超时设置

        :param request: Request instance for ModifyVirusScanTimeoutSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanTimeoutSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanTimeoutSettingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVirusScanTimeoutSetting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVirusScanTimeoutSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveAssetImageRegistryRegistryDetail(self, request):
        """删除单个镜像仓库详细信息

        :param request: Request instance for RemoveAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.RemoveAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.RemoveAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveAssetImageRegistryRegistryDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveAssetImageRegistryRegistryDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewImageAuthorizeState(self, request):
        """RenewImageAuthorizeState   授权镜像扫描

        :param request: Request instance for RenewImageAuthorizeState.
        :type request: :class:`tencentcloud.tcss.v20201101.models.RenewImageAuthorizeStateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.RenewImageAuthorizeStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewImageAuthorizeState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewImageAuthorizeStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScanComplianceAssets(self, request):
        """重新检测选定的资产

        :param request: Request instance for ScanComplianceAssets.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanComplianceAssets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanComplianceAssetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScanComplianceAssetsByPolicyItem(self, request):
        """用指定的检测项重新检测选定的资产，返回创建的合规检查任务的ID。

        :param request: Request instance for ScanComplianceAssetsByPolicyItem.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsByPolicyItemRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsByPolicyItemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanComplianceAssetsByPolicyItem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanComplianceAssetsByPolicyItemResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScanCompliancePolicyItems(self, request):
        """重新检测选的检测项下的所有资产，返回创建的合规检查任务的ID。

        :param request: Request instance for ScanCompliancePolicyItems.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanCompliancePolicyItemsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanCompliancePolicyItemsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanCompliancePolicyItems", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanCompliancePolicyItemsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScanComplianceScanFailedAssets(self, request):
        """重新检测选定的检测失败的资产下的所有失败的检测项，返回创建的合规检查任务的ID。

        :param request: Request instance for ScanComplianceScanFailedAssets.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceScanFailedAssetsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceScanFailedAssetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanComplianceScanFailedAssets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanComplianceScanFailedAssetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetCheckMode(self, request):
        """设置检测模式和自动检查

        :param request: Request instance for SetCheckMode.
        :type request: :class:`tencentcloud.tcss.v20201101.models.SetCheckModeRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.SetCheckModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetCheckMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetCheckModeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopVirusScanTask(self, request):
        """运行时停止木马查杀任务

        :param request: Request instance for StopVirusScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.StopVirusScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.StopVirusScanTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopVirusScanTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopVirusScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncAssetImageRegistryAsset(self, request):
        """镜像仓库资产刷新

        :param request: Request instance for SyncAssetImageRegistryAsset.
        :type request: :class:`tencentcloud.tcss.v20201101.models.SyncAssetImageRegistryAssetRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.SyncAssetImageRegistryAssetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SyncAssetImageRegistryAsset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncAssetImageRegistryAssetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAssetImageRegistryRegistryDetail(self, request):
        """更新单个镜像仓库详细信息

        :param request: Request instance for UpdateAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAssetImageRegistryRegistryDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAssetImageRegistryRegistryDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateImageRegistryTimingScanTask(self, request):
        """镜像仓库更新定时任务

        :param request: Request instance for UpdateImageRegistryTimingScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateImageRegistryTimingScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateImageRegistryTimingScanTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateImageRegistryTimingScanTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateImageRegistryTimingScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)