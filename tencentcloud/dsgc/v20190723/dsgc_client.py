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
from tencentcloud.dsgc.v20190723 import models


class DsgcClient(AbstractClient):
    _apiVersion = '2019-07-23'
    _endpoint = 'dsgc.tencentcloudapi.com'
    _service = 'dsgc'


    def AuthorizeDSPAMetaResources(self, request):
        r"""授权用户云资源

        :param request: Request instance for AuthorizeDSPAMetaResources.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.AuthorizeDSPAMetaResourcesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.AuthorizeDSPAMetaResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuthorizeDSPAMetaResources", params, headers=headers)
            response = json.loads(body)
            model = models.AuthorizeDSPAMetaResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindDSPAResourceCosBuckets(self, request):
        r"""绑定或解绑COS桶

        :param request: Request instance for BindDSPAResourceCosBuckets.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.BindDSPAResourceCosBucketsRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.BindDSPAResourceCosBucketsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindDSPAResourceCosBuckets", params, headers=headers)
            response = json.loads(body)
            model = models.BindDSPAResourceCosBucketsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindDSPAResourceDatabases(self, request):
        r"""绑定或解绑数据库实例DB

        :param request: Request instance for BindDSPAResourceDatabases.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.BindDSPAResourceDatabasesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.BindDSPAResourceDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindDSPAResourceDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.BindDSPAResourceDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyDSPATemplate(self, request):
        r"""复制合规组模板

        :param request: Request instance for CopyDSPATemplate.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CopyDSPATemplateRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CopyDSPATemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyDSPATemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CopyDSPATemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetSortingReportRetryTask(self, request):
        r"""创建资产梳理报表导出重试任务

        :param request: Request instance for CreateAssetSortingReportRetryTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateAssetSortingReportRetryTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateAssetSortingReportRetryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetSortingReportRetryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetSortingReportRetryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetSortingReportTask(self, request):
        r"""创建资产梳理报告任务

        :param request: Request instance for CreateAssetSortingReportTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateAssetSortingReportTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateAssetSortingReportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetSortingReportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetSortingReportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPAAssessmentRiskLevel(self, request):
        r"""风险项页面---创建风险等级

        :param request: Request instance for CreateDSPAAssessmentRiskLevel.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAAssessmentRiskLevelRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAAssessmentRiskLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPAAssessmentRiskLevel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPAAssessmentRiskLevelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPAAssessmentRiskTemplate(self, request):
        r"""风险评估模板---创建风险评估模板

        :param request: Request instance for CreateDSPAAssessmentRiskTemplate.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAAssessmentRiskTemplateRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAAssessmentRiskTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPAAssessmentRiskTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPAAssessmentRiskTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPAAssessmentTask(self, request):
        r"""新建DSPA风险评估任务

        :param request: Request instance for CreateDSPAAssessmentTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAAssessmentTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAAssessmentTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPAAssessmentTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPAAssessmentTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPACOSDiscoveryTask(self, request):
        r"""新增COS分类分级扫描任务，单个用户最多允许创建100个任务。

        :param request: Request instance for CreateDSPACOSDiscoveryTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPACOSDiscoveryTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPACOSDiscoveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPACOSDiscoveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPACOSDiscoveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPACategory(self, request):
        r"""新增分类，单个用户最多允许创建100个数据分类。

        :param request: Request instance for CreateDSPACategory.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPACategoryRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPACategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPACategory", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPACategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPACategoryRelation(self, request):
        r"""创建分类关联关系

        :param request: Request instance for CreateDSPACategoryRelation.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPACategoryRelationRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPACategoryRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPACategoryRelation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPACategoryRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPAComplianceGroup(self, request):
        r"""新增分类分级模板，单个用户最多允许创建100个合规组。

        :param request: Request instance for CreateDSPAComplianceGroup.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAComplianceGroupRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAComplianceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPAComplianceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPAComplianceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPAComplianceRules(self, request):
        r"""创建合规组分类规则关联关系

        :param request: Request instance for CreateDSPAComplianceRules.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAComplianceRulesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAComplianceRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPAComplianceRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPAComplianceRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPACosMetaResources(self, request):
        r"""添加COS元数据

        :param request: Request instance for CreateDSPACosMetaResources.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPACosMetaResourcesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPACosMetaResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPACosMetaResources", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPACosMetaResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPADbMetaResources(self, request):
        r"""添加用户云上数据库类型资源

        :param request: Request instance for CreateDSPADbMetaResources.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPADbMetaResourcesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPADbMetaResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPADbMetaResources", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPADbMetaResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPADiscoveryRule(self, request):
        r"""新增分类分级规则，单个用户最多允许创建200个规则。

        :param request: Request instance for CreateDSPADiscoveryRule.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPADiscoveryRuleRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPADiscoveryRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPADiscoveryRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPADiscoveryRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPADiscoveryTask(self, request):
        r"""新增分类分级任务，单个用户最多允许创建100个任务。

        :param request: Request instance for CreateDSPADiscoveryTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPADiscoveryTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPADiscoveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPADiscoveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPADiscoveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPALevelGroup(self, request):
        r"""新增分级，单个Casb实例最多允许创建100个数据分级

        :param request: Request instance for CreateDSPALevelGroup.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPALevelGroupRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPALevelGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPALevelGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPALevelGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPAMetaResources(self, request):
        r"""添加用户云上资源列表

        :param request: Request instance for CreateDSPAMetaResources.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAMetaResourcesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPAMetaResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPAMetaResources", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPAMetaResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDSPASelfBuildMetaResource(self, request):
        r"""新建用户自建云资源

        :param request: Request instance for CreateDSPASelfBuildMetaResource.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPASelfBuildMetaResourceRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateDSPASelfBuildMetaResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDSPASelfBuildMetaResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDSPASelfBuildMetaResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIdentifyRuleAnotherName(self, request):
        r"""创建规则别名

        :param request: Request instance for CreateIdentifyRuleAnotherName.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.CreateIdentifyRuleAnotherNameRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.CreateIdentifyRuleAnotherNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIdentifyRuleAnotherName", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIdentifyRuleAnotherNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DecribeSuggestRiskLevelMatrix(self, request):
        r"""风险等级的定义页面-创建风险等级的时候生成的一个默认的矩阵

        :param request: Request instance for DecribeSuggestRiskLevelMatrix.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DecribeSuggestRiskLevelMatrixRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DecribeSuggestRiskLevelMatrixResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DecribeSuggestRiskLevelMatrix", params, headers=headers)
            response = json.loads(body)
            model = models.DecribeSuggestRiskLevelMatrixResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCosMetaResource(self, request):
        r"""本接口（DeleteCOSMetaData）用于删除COS元数据信息。

        :param request: Request instance for DeleteCosMetaResource.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DeleteCosMetaResourceRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DeleteCosMetaResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCosMetaResource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCosMetaResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDSPAAssessmentTask(self, request):
        r"""删除DSPA风险评估任务

        :param request: Request instance for DeleteDSPAAssessmentTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPAAssessmentTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPAAssessmentTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDSPAAssessmentTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDSPAAssessmentTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDSPACOSDiscoveryTask(self, request):
        r"""删除COS分类分级任务，该接口只有在任务状态为以下几个状态值时才支持正确删除：
        0 待扫描，
        2 扫描终止，
        3 扫描成功，
        4 扫描失败

        :param request: Request instance for DeleteDSPACOSDiscoveryTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPACOSDiscoveryTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPACOSDiscoveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDSPACOSDiscoveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDSPACOSDiscoveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDSPACOSDiscoveryTaskResult(self, request):
        r"""删除COS分类分级任务结果

        :param request: Request instance for DeleteDSPACOSDiscoveryTaskResult.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPACOSDiscoveryTaskResultRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPACOSDiscoveryTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDSPACOSDiscoveryTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDSPACOSDiscoveryTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDSPADiscoveryTask(self, request):
        r"""删除分类分级识别任务，该接口只有在任务状态为以下几个状态值时才支持正确删除：
        0 待扫描，
        2 扫描终止，
        3 扫描成功，
        4 扫描失败

        :param request: Request instance for DeleteDSPADiscoveryTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPADiscoveryTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPADiscoveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDSPADiscoveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDSPADiscoveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDSPADiscoveryTaskResult(self, request):
        r"""删除分类分级识别任务结果

        :param request: Request instance for DeleteDSPADiscoveryTaskResult.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPADiscoveryTaskResultRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPADiscoveryTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDSPADiscoveryTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDSPADiscoveryTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDSPAMetaResource(self, request):
        r"""删除用户云资源

        :param request: Request instance for DeleteDSPAMetaResource.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPAMetaResourceRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DeleteDSPAMetaResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDSPAMetaResource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDSPAMetaResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDetailDataExportResult(self, request):
        r"""查询敏感数据导出结果URL

        :param request: Request instance for DescribeAssetDetailDataExportResult.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeAssetDetailDataExportResultRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeAssetDetailDataExportResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDetailDataExportResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDetailDataExportResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetOverview(self, request):
        r"""数据资产报告页面-查询数据资产概览接口（包括数据库资产详情和存储资产详情）

        :param request: Request instance for DescribeAssetOverview.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeAssetOverviewRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeAssetOverviewResponse`

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


    def DescribeBindDBList(self, request):
        r"""查询DB绑定的列表

        :param request: Request instance for DescribeBindDBList.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeBindDBListRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeBindDBListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindDBList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBindDBListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCOSAssetSensitiveDistribution(self, request):
        r"""数据资产报告-查询cos的资产分布详情接口

        :param request: Request instance for DescribeCOSAssetSensitiveDistribution.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeCOSAssetSensitiveDistributionRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeCOSAssetSensitiveDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCOSAssetSensitiveDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCOSAssetSensitiveDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentHighRiskTop10Overview(self, request):
        r"""查询高风险资产的top10

        :param request: Request instance for DescribeDSPAAssessmentHighRiskTop10Overview.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentHighRiskTop10OverviewRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentHighRiskTop10OverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentHighRiskTop10Overview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentHighRiskTop10OverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentLatestRiskDetailInfo(self, request):
        r"""查询最新风险项详情数据

        :param request: Request instance for DescribeDSPAAssessmentLatestRiskDetailInfo.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentLatestRiskDetailInfoRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentLatestRiskDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentLatestRiskDetailInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentLatestRiskDetailInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentLatestRiskList(self, request):
        r"""查询最新的风险详情列表数据

        :param request: Request instance for DescribeDSPAAssessmentLatestRiskList.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentLatestRiskListRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentLatestRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentLatestRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentLatestRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentNewDiscoveredRiskOverview(self, request):
        r"""风险概览-查询新发现风险统计数

        :param request: Request instance for DescribeDSPAAssessmentNewDiscoveredRiskOverview.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentNewDiscoveredRiskOverviewRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentNewDiscoveredRiskOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentNewDiscoveredRiskOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentNewDiscoveredRiskOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentPendingRiskOverview(self, request):
        r"""风险概览-查询待处理风险统计数

        :param request: Request instance for DescribeDSPAAssessmentPendingRiskOverview.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentPendingRiskOverviewRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentPendingRiskOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentPendingRiskOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentPendingRiskOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentProcessingRiskOverview(self, request):
        r"""风险概览-查询处理中风险统计数

        :param request: Request instance for DescribeDSPAAssessmentProcessingRiskOverview.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentProcessingRiskOverviewRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentProcessingRiskOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentProcessingRiskOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentProcessingRiskOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskAmountOverview(self, request):
        r"""风险概览页风险数量和受影响资产数概览统计

        :param request: Request instance for DescribeDSPAAssessmentRiskAmountOverview.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskAmountOverviewRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskAmountOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskAmountOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskAmountOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskDatasourceTop5(self, request):
        r"""受影响资产TOP5统计

        :param request: Request instance for DescribeDSPAAssessmentRiskDatasourceTop5.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskDatasourceTop5Request`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskDatasourceTop5Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskDatasourceTop5", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskDatasourceTop5Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskDealedOverview(self, request):
        r"""遗留待处理&昨日完成风险处置概览统计

        :param request: Request instance for DescribeDSPAAssessmentRiskDealedOverview.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskDealedOverviewRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskDealedOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskDealedOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskDealedOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskDealedTrend(self, request):
        r"""风险项处理趋势统计

        :param request: Request instance for DescribeDSPAAssessmentRiskDealedTrend.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskDealedTrendRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskDealedTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskDealedTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskDealedTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskDistributionOverview(self, request):
        r"""查询风险分布数据，包含风险类型分布，风险详情分布，风险资产的分布

        :param request: Request instance for DescribeDSPAAssessmentRiskDistributionOverview.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskDistributionOverviewRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskDistributionOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskDistributionOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskDistributionOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskItemTop5(self, request):
        r"""风险分类TOP5统计

        :param request: Request instance for DescribeDSPAAssessmentRiskItemTop5.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskItemTop5Request`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskItemTop5Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskItemTop5", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskItemTop5Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskLevelDetail(self, request):
        r"""风险项页面----查询风险等级的详情数据

        :param request: Request instance for DescribeDSPAAssessmentRiskLevelDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskLevelDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskLevelDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskLevelDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskLevelDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskLevelList(self, request):
        r"""风险项页面----查询风险等级的列表

        :param request: Request instance for DescribeDSPAAssessmentRiskLevelList.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskLevelListRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskLevelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskLevelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskLevelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskLevelTrend(self, request):
        r"""风险级别趋势统计

        :param request: Request instance for DescribeDSPAAssessmentRiskLevelTrend.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskLevelTrendRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskLevelTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskLevelTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskLevelTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskOverview(self, request):
        r"""风险数量概览统计

        :param request: Request instance for DescribeDSPAAssessmentRiskOverview.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskOverviewRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskProcessHistory(self, request):
        r"""查询风险的处理历史

        :param request: Request instance for DescribeDSPAAssessmentRiskProcessHistory.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskProcessHistoryRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskProcessHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskProcessHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskProcessHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskSideDistributed(self, request):
        r"""风险评估概览页，查询风险面的分布

        :param request: Request instance for DescribeDSPAAssessmentRiskSideDistributed.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskSideDistributedRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskSideDistributedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskSideDistributed", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskSideDistributedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskSideList(self, request):
        r"""风险评估概览页，查询风险面的分布

        :param request: Request instance for DescribeDSPAAssessmentRiskSideList.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskSideListRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskSideListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskSideList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskSideListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskTemplateDetail(self, request):
        r"""风险项页面--查看评估模板详情

        :param request: Request instance for DescribeDSPAAssessmentRiskTemplateDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskTemplateDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskTemplateDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskTemplateDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskTemplateDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRiskTemplateVulnerableList(self, request):
        r"""风险模板页面--查询风险模板中的脆弱项配置

        :param request: Request instance for DescribeDSPAAssessmentRiskTemplateVulnerableList.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskTemplateVulnerableListRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRiskTemplateVulnerableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRiskTemplateVulnerableList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRiskTemplateVulnerableListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentRisks(self, request):
        r"""获取DSPA评估风险项列表

        :param request: Request instance for DescribeDSPAAssessmentRisks.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRisksRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentRisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentRisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentRisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentTasks(self, request):
        r"""获取DSPA评估任务列表

        :param request: Request instance for DescribeDSPAAssessmentTasks.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentTasksRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentTemplateControlItems(self, request):
        r"""获取DSPA评估模板关联的评估控制项列表

        :param request: Request instance for DescribeDSPAAssessmentTemplateControlItems.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentTemplateControlItemsRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentTemplateControlItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentTemplateControlItems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentTemplateControlItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAAssessmentTemplates(self, request):
        r"""获取DSPA评估模板列表

        :param request: Request instance for DescribeDSPAAssessmentTemplates.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentTemplatesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAAssessmentTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAAssessmentTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAAssessmentTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACOSDataAssetBuckets(self, request):
        r"""获取COS敏感数据资产桶列表

        :param request: Request instance for DescribeDSPACOSDataAssetBuckets.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDataAssetBucketsRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDataAssetBucketsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACOSDataAssetBuckets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACOSDataAssetBucketsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACOSDataAssetByComplianceId(self, request):
        r"""获取COS单个模板下的敏感数据资产

        :param request: Request instance for DescribeDSPACOSDataAssetByComplianceId.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDataAssetByComplianceIdRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDataAssetByComplianceIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACOSDataAssetByComplianceId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACOSDataAssetByComplianceIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACOSDataAssetDetail(self, request):
        r"""获取COS分类分级数据资产详情

        :param request: Request instance for DescribeDSPACOSDataAssetDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDataAssetDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDataAssetDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACOSDataAssetDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACOSDataAssetDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACOSDiscoveryTaskDetail(self, request):
        r"""获取COS分类分级任务详情

        :param request: Request instance for DescribeDSPACOSDiscoveryTaskDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDiscoveryTaskDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDiscoveryTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACOSDiscoveryTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACOSDiscoveryTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACOSDiscoveryTaskFiles(self, request):
        r"""获取COS分类分级任务结果详情文件列表

        :param request: Request instance for DescribeDSPACOSDiscoveryTaskFiles.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDiscoveryTaskFilesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDiscoveryTaskFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACOSDiscoveryTaskFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACOSDiscoveryTaskFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACOSDiscoveryTaskResult(self, request):
        r"""获取COS分类分级任务结果，该接口只有在任务状态为以下状态时才支持结果正常查询：
        3 扫描成功，
        4 扫描失败

        :param request: Request instance for DescribeDSPACOSDiscoveryTaskResult.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDiscoveryTaskResultRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDiscoveryTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACOSDiscoveryTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACOSDiscoveryTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACOSDiscoveryTasks(self, request):
        r"""获取COS分类分级任务列表

        :param request: Request instance for DescribeDSPACOSDiscoveryTasks.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDiscoveryTasksRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSDiscoveryTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACOSDiscoveryTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACOSDiscoveryTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACOSTaskResultDetail(self, request):
        r"""获取COS分类分级任务结果详情，该接口只有在任务状态为时才支持结果正确查询：
        3 扫描成功

        :param request: Request instance for DescribeDSPACOSTaskResultDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSTaskResultDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACOSTaskResultDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACOSTaskResultDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACOSTaskResultDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACategories(self, request):
        r"""获取敏感数据分类列表

        :param request: Request instance for DescribeDSPACategories.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACategoriesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACategoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACategories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACategoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACategoryRuleStatistic(self, request):
        r"""获取分类规则统计信息

        :param request: Request instance for DescribeDSPACategoryRuleStatistic.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACategoryRuleStatisticRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACategoryRuleStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACategoryRuleStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACategoryRuleStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACategoryRules(self, request):
        r"""获取合规组分类规则信息

        :param request: Request instance for DescribeDSPACategoryRules.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACategoryRulesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACategoryRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACategoryRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACategoryRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACategoryTree(self, request):
        r"""获取分类树信息

        :param request: Request instance for DescribeDSPACategoryTree.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACategoryTreeRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACategoryTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACategoryTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACategoryTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPACategoryTreeWithRules(self, request):
        r"""获取分类规则树信息

        :param request: Request instance for DescribeDSPACategoryTreeWithRules.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACategoryTreeWithRulesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPACategoryTreeWithRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPACategoryTreeWithRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPACategoryTreeWithRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAComplianceGroupDetail(self, request):
        r"""获取模板详情信息

        :param request: Request instance for DescribeDSPAComplianceGroupDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAComplianceGroupDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAComplianceGroupDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAComplianceGroupDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAComplianceGroupDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAComplianceGroups(self, request):
        r"""获取分类分级模板列表

        :param request: Request instance for DescribeDSPAComplianceGroups.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAComplianceGroupsRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAComplianceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAComplianceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAComplianceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAComplianceUpdateNotification(self, request):
        r"""获取模板更新提示信息

        :param request: Request instance for DescribeDSPAComplianceUpdateNotification.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAComplianceUpdateNotificationRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAComplianceUpdateNotificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAComplianceUpdateNotification", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAComplianceUpdateNotificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPADataSourceDbInfo(self, request):
        r"""获取数据源的数据库信息

        :param request: Request instance for DescribeDSPADataSourceDbInfo.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADataSourceDbInfoRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADataSourceDbInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPADataSourceDbInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPADataSourceDbInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPADiscoveryRules(self, request):
        r"""获取分类分级规则列表

        :param request: Request instance for DescribeDSPADiscoveryRules.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryRulesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPADiscoveryRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPADiscoveryRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPADiscoveryServiceStatus(self, request):
        r"""用于查询该用户是否已开通分类分级服务

        :param request: Request instance for DescribeDSPADiscoveryServiceStatus.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryServiceStatusRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryServiceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPADiscoveryServiceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPADiscoveryServiceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPADiscoveryTaskDetail(self, request):
        r"""获取分类分级任务详情

        :param request: Request instance for DescribeDSPADiscoveryTaskDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryTaskDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPADiscoveryTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPADiscoveryTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPADiscoveryTaskResult(self, request):
        r"""获取分类分级任务结果，该接口只有在任务状态为以下状态时才支持结果正常查询：3 扫描成功，4 扫描失败

        :param request: Request instance for DescribeDSPADiscoveryTaskResult.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryTaskResultRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPADiscoveryTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPADiscoveryTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPADiscoveryTaskResultDetail(self, request):
        r"""获取分类分级任务结果详情，该接口只有在任务状态为时才支持结果正确查询：
        3 扫描成功

        :param request: Request instance for DescribeDSPADiscoveryTaskResultDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryTaskResultDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryTaskResultDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPADiscoveryTaskResultDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPADiscoveryTaskResultDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPADiscoveryTaskTables(self, request):
        r"""获取分级分级扫描的表集合

        :param request: Request instance for DescribeDSPADiscoveryTaskTables.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryTaskTablesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryTaskTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPADiscoveryTaskTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPADiscoveryTaskTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPADiscoveryTasks(self, request):
        r"""获取分类分级任务列表

        :param request: Request instance for DescribeDSPADiscoveryTasks.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryTasksRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPADiscoveryTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPADiscoveryTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPADiscoveryTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAESDataAssetByComplianceId(self, request):
        r"""根据合规组id，去查询ES的概览页统计数据

        :param request: Request instance for DescribeDSPAESDataAssetByComplianceId.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAESDataAssetByComplianceIdRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAESDataAssetByComplianceIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAESDataAssetByComplianceId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAESDataAssetByComplianceIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAESDataAssetDetail(self, request):
        r"""根据合规组id，去查询ES的概览页下的统计列表数据

        :param request: Request instance for DescribeDSPAESDataAssetDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAESDataAssetDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAESDataAssetDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAESDataAssetDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAESDataAssetDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAESDataSample(self, request):
        r"""获取ES扫描结果数据样本

        :param request: Request instance for DescribeDSPAESDataSample.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAESDataSampleRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAESDataSampleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAESDataSample", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAESDataSampleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPAESDiscoveryTaskResultDetail(self, request):
        r"""获取ES的分类分级任务结果详情，该接口只有在任务状态为时才支持结果正确查询：
        3 扫描成功

        :param request: Request instance for DescribeDSPAESDiscoveryTaskResultDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAESDiscoveryTaskResultDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPAESDiscoveryTaskResultDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPAESDiscoveryTaskResultDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPAESDiscoveryTaskResultDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPALevelDetail(self, request):
        r"""获取分级详情

        :param request: Request instance for DescribeDSPALevelDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPALevelDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPALevelDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPALevelDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPALevelDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPALevelGroups(self, request):
        r"""获取分级列表，限制100个 不分页返回

        :param request: Request instance for DescribeDSPALevelGroups.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPALevelGroupsRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPALevelGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPALevelGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPALevelGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPARDBDataAssetByComplianceId(self, request):
        r"""获取单个合规组下的RDB关系数据库分类分级数据资产

        :param request: Request instance for DescribeDSPARDBDataAssetByComplianceId.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPARDBDataAssetByComplianceIdRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPARDBDataAssetByComplianceIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPARDBDataAssetByComplianceId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPARDBDataAssetByComplianceIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPARDBDataAssetDetail(self, request):
        r"""获取RDB关系数据库分类分级资产详情

        :param request: Request instance for DescribeDSPARDBDataAssetDetail.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPARDBDataAssetDetailRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPARDBDataAssetDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPARDBDataAssetDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPARDBDataAssetDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPASupportedMetas(self, request):
        r"""拉取DSPA支持的Meta元数据类型，返回包括：元数据类型，支持的元数据地域信息

        :param request: Request instance for DescribeDSPASupportedMetas.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPASupportedMetasRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPASupportedMetasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPASupportedMetas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPASupportedMetasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDSPATaskResultDataSample(self, request):
        r"""获取扫描结果数据样本

        :param request: Request instance for DescribeDSPATaskResultDataSample.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPATaskResultDataSampleRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeDSPATaskResultDataSampleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDSPATaskResultDataSample", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDSPATaskResultDataSampleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeESAssetSensitiveDistribution(self, request):
        r"""数据资产报告-查询es的敏感资产报告，包含（数据库资产，设敏级别数据库top10，资产详情）

        :param request: Request instance for DescribeESAssetSensitiveDistribution.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeESAssetSensitiveDistributionRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeESAssetSensitiveDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeESAssetSensitiveDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeESAssetSensitiveDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportTaskResult(self, request):
        r"""获取导出任务结果

        :param request: Request instance for DescribeExportTaskResult.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeExportTaskResultRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeExportTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMongoAssetSensitiveDistribution(self, request):
        r"""数据资产报告-查询mongo 的敏感资产报告，包含（数据库资产，设敏级别数据库top10，资产详情）

        :param request: Request instance for DescribeMongoAssetSensitiveDistribution.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeMongoAssetSensitiveDistributionRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeMongoAssetSensitiveDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMongoAssetSensitiveDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMongoAssetSensitiveDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRDBAssetSensitiveDistribution(self, request):
        r"""数据资产报告-查询rbd 的敏感资产报告，包含（数据库资产，设敏级别数据库top10，资产详情）

        :param request: Request instance for DescribeRDBAssetSensitiveDistribution.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeRDBAssetSensitiveDistributionRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeRDBAssetSensitiveDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRDBAssetSensitiveDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRDBAssetSensitiveDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReportTaskDownloadUrl(self, request):
        r"""获取报表下载链接

        :param request: Request instance for DescribeReportTaskDownloadUrl.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeReportTaskDownloadUrlRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeReportTaskDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReportTaskDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReportTaskDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReportTasks(self, request):
        r"""获取资产报表任务列表

        :param request: Request instance for DescribeReportTasks.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeReportTasksRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeReportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSensitiveCOSDataDistribution(self, request):
        r"""数据资产报告-查询cos的敏感数据分布（分级分布 分类分布 敏感规则分布详情列表）

        :param request: Request instance for DescribeSensitiveCOSDataDistribution.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeSensitiveCOSDataDistributionRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeSensitiveCOSDataDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSensitiveCOSDataDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSensitiveCOSDataDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSensitiveRDBDataDistribution(self, request):
        r"""数据资产报告-查询rdb的敏感数据分布-敏感规则字段分布-敏感分布详情

        :param request: Request instance for DescribeSensitiveRDBDataDistribution.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DescribeSensitiveRDBDataDistributionRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DescribeSensitiveRDBDataDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSensitiveRDBDataDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSensitiveRDBDataDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableDSPAMetaResourceAuth(self, request):
        r"""取消用户云资源授权

        :param request: Request instance for DisableDSPAMetaResourceAuth.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.DisableDSPAMetaResourceAuthRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.DisableDSPAMetaResourceAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableDSPAMetaResourceAuth", params, headers=headers)
            response = json.loads(body)
            model = models.DisableDSPAMetaResourceAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableDSPADiscoveryRule(self, request):
        r"""打开或者关闭分类分级规则
        注：此API同时对该规则下的RDB跟COS规则操作。

        :param request: Request instance for EnableDSPADiscoveryRule.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.EnableDSPADiscoveryRuleRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.EnableDSPADiscoveryRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableDSPADiscoveryRule", params, headers=headers)
            response = json.loads(body)
            model = models.EnableDSPADiscoveryRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableTrialVersion(self, request):
        r"""启用版本体验

        :param request: Request instance for EnableTrialVersion.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.EnableTrialVersionRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.EnableTrialVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableTrialVersion", params, headers=headers)
            response = json.loads(body)
            model = models.EnableTrialVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetDetailData(self, request):
        r"""创建敏感数据导出任务

        :param request: Request instance for ExportAssetDetailData.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ExportAssetDetailDataRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ExportAssetDetailDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetDetailData", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetDetailDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetResourceConnectionStatus(self, request):
        r"""获取授权资源的连接状态

        :param request: Request instance for GetResourceConnectionStatus.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.GetResourceConnectionStatusRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.GetResourceConnectionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetResourceConnectionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetResourceConnectionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTrialVersion(self, request):
        r"""获取体验版本信息

        :param request: Request instance for GetTrialVersion.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.GetTrialVersionRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.GetTrialVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTrialVersion", params, headers=headers)
            response = json.loads(body)
            model = models.GetTrialVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetUserQuotaInfo(self, request):
        r"""获取用户购买配额信息

        :param request: Request instance for GetUserQuotaInfo.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.GetUserQuotaInfoRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.GetUserQuotaInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUserQuotaInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetUserQuotaInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDSPAClusters(self, request):
        r"""拉取DSPA集群列表

        :param request: Request instance for ListDSPAClusters.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ListDSPAClustersRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ListDSPAClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDSPAClusters", params, headers=headers)
            response = json.loads(body)
            model = models.ListDSPAClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDSPACosMetaResources(self, request):
        r"""本接口用于获取COS元数据信息，返回COS元数据信息列表。

        :param request: Request instance for ListDSPACosMetaResources.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ListDSPACosMetaResourcesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ListDSPACosMetaResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDSPACosMetaResources", params, headers=headers)
            response = json.loads(body)
            model = models.ListDSPACosMetaResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDSPAMetaResources(self, request):
        r"""拉取用户云资源

        :param request: Request instance for ListDSPAMetaResources.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ListDSPAMetaResourcesRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ListDSPAMetaResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDSPAMetaResources", params, headers=headers)
            response = json.loads(body)
            model = models.ListDSPAMetaResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPAAssessmentRisk(self, request):
        r"""修改DSPA评估风险项，支持修改Status

        :param request: Request instance for ModifyDSPAAssessmentRisk.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAAssessmentRiskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAAssessmentRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPAAssessmentRisk", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPAAssessmentRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPAAssessmentRiskLatest(self, request):
        r"""修改最新评估风险项状态

        :param request: Request instance for ModifyDSPAAssessmentRiskLatest.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAAssessmentRiskLatestRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAAssessmentRiskLatestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPAAssessmentRiskLatest", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPAAssessmentRiskLatestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPAAssessmentRiskLevel(self, request):
        r"""风险项页面----修改风险等级的详情数据

        :param request: Request instance for ModifyDSPAAssessmentRiskLevel.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAAssessmentRiskLevelRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAAssessmentRiskLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPAAssessmentRiskLevel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPAAssessmentRiskLevelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPAAssessmentRiskTemplate(self, request):
        r"""风险模板---修改风险模板

        :param request: Request instance for ModifyDSPAAssessmentRiskTemplate.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAAssessmentRiskTemplateRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAAssessmentRiskTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPAAssessmentRiskTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPAAssessmentRiskTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPACOSDiscoveryTask(self, request):
        r"""修改COS分类分级任务，该接口只有在任务状态为以下状态时才支持正确修改：
        0 待扫描，
        2 扫描终止，
        3 扫描成功，
        4 扫描失败

        :param request: Request instance for ModifyDSPACOSDiscoveryTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPACOSDiscoveryTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPACOSDiscoveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPACOSDiscoveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPACOSDiscoveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPACOSTaskResult(self, request):
        r"""调整COS任务扫描结果

        :param request: Request instance for ModifyDSPACOSTaskResult.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPACOSTaskResultRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPACOSTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPACOSTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPACOSTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPACategory(self, request):
        r"""修改分类，内置分类不支持修改。

        :param request: Request instance for ModifyDSPACategory.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPACategoryRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPACategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPACategory", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPACategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPACategoryRelation(self, request):
        r"""修改分类分级关系

        :param request: Request instance for ModifyDSPACategoryRelation.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPACategoryRelationRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPACategoryRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPACategoryRelation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPACategoryRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPAClusterInfo(self, request):
        r"""修改DSPA集群信息

        :param request: Request instance for ModifyDSPAClusterInfo.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAClusterInfoRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAClusterInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPAClusterInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPAClusterInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPAComplianceGroup(self, request):
        r"""修改分类分级模板，内置模板不支持修改。

        :param request: Request instance for ModifyDSPAComplianceGroup.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAComplianceGroupRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAComplianceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPAComplianceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPAComplianceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPADiscoveryRule(self, request):
        r"""修改分类分级规则，单个用户最多允许创建200个规则。
        注：此API同时适用RDB跟COS类型数据。

        :param request: Request instance for ModifyDSPADiscoveryRule.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPADiscoveryRuleRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPADiscoveryRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPADiscoveryRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPADiscoveryRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPADiscoveryTask(self, request):
        r"""修改分类分级任务，该接口只有在任务状态为以下状态时才支持正确修改：
        0 待扫描，
        2 扫描终止，
        3 扫描成功，
        4 扫描失败

        :param request: Request instance for ModifyDSPADiscoveryTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPADiscoveryTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPADiscoveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPADiscoveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPADiscoveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPAESTaskResult(self, request):
        r"""调整ES任务扫描结果

        :param request: Request instance for ModifyDSPAESTaskResult.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAESTaskResultRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPAESTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPAESTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPAESTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDSPATaskResult(self, request):
        r"""调整任务扫描结果

        :param request: Request instance for ModifyDSPATaskResult.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPATaskResultRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.ModifyDSPATaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDSPATaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDSPATaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryDSPAMetaResourceDbList(self, request):
        r"""查询DSPA实例的db列表

        :param request: Request instance for QueryDSPAMetaResourceDbList.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.QueryDSPAMetaResourceDbListRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.QueryDSPAMetaResourceDbListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDSPAMetaResourceDbList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryDSPAMetaResourceDbListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryResourceDbBindStatus(self, request):
        r"""获取资源绑定DB状态

        :param request: Request instance for QueryResourceDbBindStatus.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.QueryResourceDbBindStatusRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.QueryResourceDbBindStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryResourceDbBindStatus", params, headers=headers)
            response = json.loads(body)
            model = models.QueryResourceDbBindStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartDSPAAssessmentTask(self, request):
        r"""重新启动DSPA风险评估任务

        :param request: Request instance for RestartDSPAAssessmentTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.RestartDSPAAssessmentTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.RestartDSPAAssessmentTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartDSPAAssessmentTask", params, headers=headers)
            response = json.loads(body)
            model = models.RestartDSPAAssessmentTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartDSPADiscoveryTask(self, request):
        r"""立即启动分类分级任务，该接口只有在任务状态为以下状态时才支持正确执行立即扫描：
        0 待扫描，
        2 扫描终止，
        3 扫描成功，
        4 扫描失败

        :param request: Request instance for StartDSPADiscoveryTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.StartDSPADiscoveryTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.StartDSPADiscoveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartDSPADiscoveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.StartDSPADiscoveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopDSPADiscoveryTask(self, request):
        r"""停止分类分级任务，该接口只有在任务状态为以下状态时才支持正确执行停止扫描：
        1 扫描中

        :param request: Request instance for StopDSPADiscoveryTask.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.StopDSPADiscoveryTaskRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.StopDSPADiscoveryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopDSPADiscoveryTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopDSPADiscoveryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDSPASelfBuildResource(self, request):
        r"""更新自建资源基础信息，包括：端口、账户名、密码。
        请注意：
        如果资源自身的VPC、VIP信息发生变化，后台会自动更新。
        如果监听的端口发生变化，请显式输入端口。
        如果账户名密码任意一个发生变化，请务必同时显式输入账户名密码。

        :param request: Request instance for UpdateDSPASelfBuildResource.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.UpdateDSPASelfBuildResourceRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.UpdateDSPASelfBuildResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDSPASelfBuildResource", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDSPASelfBuildResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyDSPACOSRule(self, request):
        r"""验证COS分类分级规则

        :param request: Request instance for VerifyDSPACOSRule.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.VerifyDSPACOSRuleRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.VerifyDSPACOSRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyDSPACOSRule", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyDSPACOSRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyDSPADiscoveryRule(self, request):
        r"""验证分类分级规则

        :param request: Request instance for VerifyDSPADiscoveryRule.
        :type request: :class:`tencentcloud.dsgc.v20190723.models.VerifyDSPADiscoveryRuleRequest`
        :rtype: :class:`tencentcloud.dsgc.v20190723.models.VerifyDSPADiscoveryRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyDSPADiscoveryRule", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyDSPADiscoveryRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))