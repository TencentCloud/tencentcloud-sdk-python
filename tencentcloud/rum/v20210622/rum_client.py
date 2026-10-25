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
from tencentcloud.rum.v20210622 import models


class RumClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'rum.tencentcloudapi.com'
    _service = 'rum'


    def CreateFieldTransformRule(self, request):
        r"""创建字段配置规则

        :param request: Request instance for CreateFieldTransformRule.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateFieldTransformRuleRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateFieldTransformRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFieldTransformRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFieldTransformRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReleaseFile(self, request):
        r"""创建对应项目的文件记录

        :param request: Request instance for CreateReleaseFile.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateReleaseFileRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateReleaseFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReleaseFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReleaseFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStarProject(self, request):
        r"""个人用户添加星标项目

        :param request: Request instance for CreateStarProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateStarProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateStarProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStarProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStarProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDEMApplication(self, request):
        r"""在指定业务系统下创建应用。

        :param request: Request instance for CreateTDEMApplication.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateTDEMApplicationRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateTDEMApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDEMApplication", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDEMApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDEMBusinessSystem(self, request):
        r"""创建业务系统。InstanceId 由后端生成，格式 rum-<12 位随机字母数字>。重名返回 InvalidParameterValue。

        :param request: Request instance for CreateTDEMBusinessSystem.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateTDEMBusinessSystemRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateTDEMBusinessSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDEMBusinessSystem", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDEMBusinessSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDEMDialTask(self, request):
        r"""创建一条移动拨测任务。同一应用处于 active 的任务最多 50 条。四项启动范围都为空时不限制启动；填写多项时必须同时满足，同一项多个值命中任意一个即可。

        :param request: Request instance for CreateTDEMDialTask.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateTDEMDialTaskRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateTDEMDialTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDEMDialTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDEMDialTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDEMFieldTransformRule(self, request):
        r"""为应用创建字段值替换规则，单应用上限 50 条。替代已废弃的 CreateFieldTransformRule；AppId 为 string。

        :param request: Request instance for CreateTDEMFieldTransformRule.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateTDEMFieldTransformRuleRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateTDEMFieldTransformRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDEMFieldTransformRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDEMFieldTransformRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDEMFunnel(self, request):
        r"""创建漏斗

        :param request: Request instance for CreateTDEMFunnel.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateTDEMFunnelRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateTDEMFunnelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDEMFunnel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDEMFunnelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWhitelist(self, request):
        r"""创建白名单

        :param request: Request instance for CreateWhitelist.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateWhitelistRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFieldTransformRule(self, request):
        r"""删除字段配置规则

        :param request: Request instance for DeleteFieldTransformRule.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteFieldTransformRuleRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteFieldTransformRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFieldTransformRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFieldTransformRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        r"""删除实例，谨慎操作，不可恢复

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMiniProgramReplayPack(self, request):
        r"""删除回放包元数据，并尽力删除COS上回放包与源码zip。不存在返回ResourceNotFound。

        :param request: Request instance for DeleteMiniProgramReplayPack.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteMiniProgramReplayPackRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteMiniProgramReplayPackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMiniProgramReplayPack", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMiniProgramReplayPackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        r"""删除给定的 rum 的项目

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReleaseFile(self, request):
        r"""将对应 sourcemap 文件删除

        :param request: Request instance for DeleteReleaseFile.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteReleaseFileRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteReleaseFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReleaseFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReleaseFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStarProject(self, request):
        r"""删除用户名下的星标项目

        :param request: Request instance for DeleteStarProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteStarProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteStarProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStarProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStarProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSymbolArtifact(self, request):
        r"""删除指定的符号制品。

        :param request: Request instance for DeleteSymbolArtifact.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteSymbolArtifactRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteSymbolArtifactResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSymbolArtifact", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSymbolArtifactResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTDEMApplication(self, request):
        r"""逻辑删除应用，ProjectKey 即刻失效。

        :param request: Request instance for DeleteTDEMApplication.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteTDEMApplicationRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteTDEMApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTDEMApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTDEMApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTDEMBusinessSystem(self, request):
        r"""删除业务系统。名下存在未删除应用时返回 ResourceInUse。

        :param request: Request instance for DeleteTDEMBusinessSystem.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteTDEMBusinessSystemRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteTDEMBusinessSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTDEMBusinessSystem", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTDEMBusinessSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTDEMDialTask(self, request):
        r"""将拨测任务标记为已删除。已删除的任务再次删除视为成功。不物理删除任务行，也不删除历史拨测结果。

        :param request: Request instance for DeleteTDEMDialTask.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteTDEMDialTaskRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteTDEMDialTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTDEMDialTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTDEMDialTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTDEMFieldTransformRule(self, request):
        r"""按规则 Id 删除字段值替换规则。替代已废弃的 DeleteFieldTransformRule；AppId 为 string。

        :param request: Request instance for DeleteTDEMFieldTransformRule.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteTDEMFieldTransformRuleRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteTDEMFieldTransformRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTDEMFieldTransformRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTDEMFieldTransformRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTDEMFunnel(self, request):
        r"""删除漏斗

        :param request: Request instance for DeleteTDEMFunnel.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteTDEMFunnelRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteTDEMFunnelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTDEMFunnel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTDEMFunnelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWhitelist(self, request):
        r"""删除白名单

        :param request: Request instance for DeleteWhitelist.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteWhitelistRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppDimensionMetrics(self, request):
        r"""用于查询 app 监控多维分析数据

        :param request: Request instance for DescribeAppDimensionMetrics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeAppDimensionMetricsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeAppDimensionMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppDimensionMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppDimensionMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppMetricsData(self, request):
        r"""获取 app 监控指标数据

        :param request: Request instance for DescribeAppMetricsData.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeAppMetricsDataRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeAppMetricsDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppMetricsData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppMetricsDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppSingleCaseDetailList(self, request):
        r"""查询 app 监控个例样本详情列表

        :param request: Request instance for DescribeAppSingleCaseDetailList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeAppSingleCaseDetailListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeAppSingleCaseDetailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppSingleCaseDetailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppSingleCaseDetailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppSingleCaseList(self, request):
        r"""查询 app 监控个例聚合列表

        :param request: Request instance for DescribeAppSingleCaseList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeAppSingleCaseListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeAppSingleCaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppSingleCaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppSingleCaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationExitReportDetail(self, request):
        r"""获取应用退出个例上报详情

        :param request: Request instance for DescribeApplicationExitReportDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeApplicationExitReportDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeApplicationExitReportDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationExitReportDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationExitReportDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationExitReportList(self, request):
        r"""获取应用退出个例上报列表

        :param request: Request instance for DescribeApplicationExitReportList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeApplicationExitReportListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeApplicationExitReportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationExitReportList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationExitReportListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeData(self, request):
        r"""转发monitor查询

        :param request: Request instance for DescribeData.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataBridgeUrlV2(self, request):
        r"""获取DescribeDataBridgeUrl信息

        :param request: Request instance for DescribeDataBridgeUrlV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataBridgeUrlV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataBridgeUrlV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataBridgeUrlV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataBridgeUrlV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataCustomUrl(self, request):
        r"""获取DescribeDataCustomUrl信息

        :param request: Request instance for DescribeDataCustomUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataCustomUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataCustomUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataCustomUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataCustomUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataCustomUrlV2(self, request):
        r"""获取DescribeDataCustomUrl信息

        :param request: Request instance for DescribeDataCustomUrlV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataCustomUrlV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataCustomUrlV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataCustomUrlV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataCustomUrlV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEventUrl(self, request):
        r"""获取DescribeDataEventUrl信息

        :param request: Request instance for DescribeDataEventUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataEventUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataEventUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEventUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEventUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEventUrlV2(self, request):
        r"""获取DescribeDataEventUrl信息

        :param request: Request instance for DescribeDataEventUrlV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataEventUrlV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataEventUrlV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEventUrlV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEventUrlV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataFetchProject(self, request):
        r"""获取DescribeDataFetchProject信息。已下线，请使用DescribeDataFetchUrl

        :param request: Request instance for DescribeDataFetchProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFetchProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataFetchProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataFetchUrl(self, request):
        r"""获取DescribeDataFetchUrl信息

        :param request: Request instance for DescribeDataFetchUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFetchUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataFetchUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataFetchUrlInfo(self, request):
        r"""获取DescribeDataFetchUrlInfo信息

        :param request: Request instance for DescribeDataFetchUrlInfo.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlInfoRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFetchUrlInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataFetchUrlInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataFetchUrlV2(self, request):
        r"""获取DescribeDataFetchUrl信息

        :param request: Request instance for DescribeDataFetchUrlV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFetchUrlV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataFetchUrlV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataLogUrlInfo(self, request):
        r"""获取loginfo信息

        :param request: Request instance for DescribeDataLogUrlInfo.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlInfoRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataLogUrlInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataLogUrlInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataLogUrlStatistics(self, request):
        r"""获取LogUrlStatistics信息

        :param request: Request instance for DescribeDataLogUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataLogUrlStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataLogUrlStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataLogUrlStatisticsV2(self, request):
        r"""获取LogUrlStatistics信息

        :param request: Request instance for DescribeDataLogUrlStatisticsV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlStatisticsV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlStatisticsV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataLogUrlStatisticsV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataLogUrlStatisticsV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataPerformancePage(self, request):
        r"""获取PerformancePage信息

        :param request: Request instance for DescribeDataPerformancePage.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformancePageRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformancePageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPerformancePage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataPerformancePageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataPerformancePageV2(self, request):
        r"""获取PerformancePage信息

        :param request: Request instance for DescribeDataPerformancePageV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformancePageV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformancePageV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPerformancePageV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataPerformancePageV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataPvUrlInfo(self, request):
        r"""获取PvUrlInfo信息

        :param request: Request instance for DescribeDataPvUrlInfo.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlInfoRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPvUrlInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataPvUrlInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataPvUrlStatistics(self, request):
        r"""获取DescribeDataPvUrlStatistics信息

        :param request: Request instance for DescribeDataPvUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPvUrlStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataPvUrlStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataPvUrlStatisticsV2(self, request):
        r"""获取DescribeDataPvUrlStatistics信息

        :param request: Request instance for DescribeDataPvUrlStatisticsV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlStatisticsV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlStatisticsV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPvUrlStatisticsV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataPvUrlStatisticsV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataReportCount(self, request):
        r"""获取项目上报量

        :param request: Request instance for DescribeDataReportCount.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataReportCountRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataReportCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataReportCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataReportCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataReportCountV2(self, request):
        r"""获取项目上报量

        :param request: Request instance for DescribeDataReportCountV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataReportCountV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataReportCountV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataReportCountV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataReportCountV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSetUrlStatistics(self, request):
        r"""获取DescribeDataSetUrlStatistics信息

        :param request: Request instance for DescribeDataSetUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataSetUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataSetUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSetUrlStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSetUrlStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSetUrlStatisticsV2(self, request):
        r"""获取DescribeDataSetUrlStatistics信息

        :param request: Request instance for DescribeDataSetUrlStatisticsV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataSetUrlStatisticsV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataSetUrlStatisticsV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSetUrlStatisticsV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSetUrlStatisticsV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataStaticProject(self, request):
        r"""获取DescribeDataStaticProject信息

        :param request: Request instance for DescribeDataStaticProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataStaticProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataStaticProjectV2(self, request):
        r"""获取DescribeDataStaticProject信息

        :param request: Request instance for DescribeDataStaticProjectV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticProjectV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticProjectV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticProjectV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataStaticProjectV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataStaticResource(self, request):
        r"""获取DescribeDataStaticResource信息

        :param request: Request instance for DescribeDataStaticResource.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticResourceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataStaticResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataStaticResourceV2(self, request):
        r"""获取DescribeDataStaticResource信息

        :param request: Request instance for DescribeDataStaticResourceV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticResourceV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticResourceV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticResourceV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataStaticResourceV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataStaticUrl(self, request):
        r"""获取DescribeDataStaticUrl信息

        :param request: Request instance for DescribeDataStaticUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataStaticUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataStaticUrlV2(self, request):
        r"""获取DescribeDataStaticUrl信息

        :param request: Request instance for DescribeDataStaticUrlV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticUrlV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticUrlV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticUrlV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataStaticUrlV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataWebVitalsPage(self, request):
        r"""获取DescribeDataWebVitalsPage信息，用户核心活动信息
        页面加载性能之Web Vitals。性能关键点

        :param request: Request instance for DescribeDataWebVitalsPage.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataWebVitalsPageRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataWebVitalsPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataWebVitalsPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataWebVitalsPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataWebVitalsPageV2(self, request):
        r"""获取DescribeDataWebVitalsPage信息，用户核心活动信息
        页面加载性能之Web Vitals。性能关键点

        :param request: Request instance for DescribeDataWebVitalsPageV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataWebVitalsPageV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataWebVitalsPageV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataWebVitalsPageV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataWebVitalsPageV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeError(self, request):
        r"""获取首页错误信息

        :param request: Request instance for DescribeError.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeErrorRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeErrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeError", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeErrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExceptionDetail(self, request):
        r"""获取异常问题详情数据

        :param request: Request instance for DescribeExceptionDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeExceptionDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeExceptionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExceptionDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExceptionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExceptionReportList(self, request):
        r"""获取异常个例列表

        :param request: Request instance for DescribeExceptionReportList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeExceptionReportListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeExceptionReportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExceptionReportList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExceptionReportListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFOOMMallocProblemDetail(self, request):
        r"""获取FOOM内存分配问题详情数据

        :param request: Request instance for DescribeFOOMMallocProblemDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMMallocProblemDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMMallocProblemDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFOOMMallocProblemDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFOOMMallocProblemDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFOOMMallocProblemList(self, request):
        r"""获取FOOM内存分配问题列表数据

        :param request: Request instance for DescribeFOOMMallocProblemList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMMallocProblemListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMMallocProblemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFOOMMallocProblemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFOOMMallocProblemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFOOMMallocReportList(self, request):
        r"""获取FOOM内存分配问题上报列表

        :param request: Request instance for DescribeFOOMMallocReportList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMMallocReportListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMMallocReportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFOOMMallocReportList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFOOMMallocReportListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFOOMProblemDetail(self, request):
        r"""获取FOOM问题详情数据

        :param request: Request instance for DescribeFOOMProblemDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMProblemDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMProblemDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFOOMProblemDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFOOMProblemDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFOOMProblemList(self, request):
        r"""获取FOOM问题列表数据

        :param request: Request instance for DescribeFOOMProblemList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMProblemListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMProblemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFOOMProblemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFOOMProblemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFOOMReportList(self, request):
        r"""获取FOOM问题上报列表

        :param request: Request instance for DescribeFOOMReportList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMReportListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeFOOMReportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFOOMReportList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFOOMReportListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFieldTransformRules(self, request):
        r"""获取字段配置规则

        :param request: Request instance for DescribeFieldTransformRules.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeFieldTransformRulesRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeFieldTransformRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFieldTransformRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFieldTransformRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFieldValues(self, request):
        r"""获取TDEM字段值列表

        :param request: Request instance for DescribeFieldValues.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeFieldValuesRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeFieldValuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFieldValues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFieldValuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileCertificate(self, request):
        r"""获取COS存储的临时密钥，具体到ProjectId

        :param request: Request instance for DescribeFileCertificate.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeFileCertificateRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeFileCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssueAffectedUsers(self, request):
        r"""按用户维度聚合某问题的受影响用户清单，服务端分页。AppId 与 IssueId 必填；AppVersion / StartTime / EndTime / Keyword 用于收窄范围，同时作用于清单与 Total，因此 Total 为当前条件下去重后的用户数， 条件全空时等于问题详情的影响用户数。OrderKey / OrderBy 只改变行序、不改变结果集合；排序一律由服务端执行， 并保留 uid 作为次级键以保证翻页不重不漏。接口只读。

        :param request: Request instance for DescribeIssueAffectedUsers.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssueAffectedUsersRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssueAffectedUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssueAffectedUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssueAffectedUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssueBreadcrumbs(self, request):
        r"""获取指定 Issue 当前事件或最新事件之前的 Breadcrumbs 面包屑序列

        :param request: Request instance for DescribeIssueBreadcrumbs.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssueBreadcrumbsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssueBreadcrumbsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssueBreadcrumbs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssueBreadcrumbsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssueCrashLogDownloadURL(self, request):
        r"""获取日志下载链接

        :param request: Request instance for DescribeIssueCrashLogDownloadURL.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssueCrashLogDownloadURLRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssueCrashLogDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssueCrashLogDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssueCrashLogDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssueDetail(self, request):
        r"""获取指定 Issue 的摘要信息以及默认选中的最新事件详情

        :param request: Request instance for DescribeIssueDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssueDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssueDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssueDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssueDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssueEventDetail(self, request):
        r"""获取指定 Issue 下单个事件的完整详情，包括栈信息、上下文和符号化状态等字段

        :param request: Request instance for DescribeIssueEventDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssueEventDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssueEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssueEventDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssueEventDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssueEvents(self, request):
        r"""根据条件获取指定 Issue 的错误事件列表，支持按时间范围、关键字和扩展过滤器查询，返回分页事件数据

        :param request: Request instance for DescribeIssueEvents.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssueEventsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssueEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssueEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssueEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssueTrend(self, request):
        r"""获取指定 Issue 在给定时间范围内的趋势分桶统计数据

        :param request: Request instance for DescribeIssueTrend.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssueTrendRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssueTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssueTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssueTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssues(self, request):
        r"""根据筛选条件分页查询 Issue 列表，支持环境、Issue 类型、状态、关键字、扩展过滤器和排序条件

        :param request: Request instance for DescribeIssues.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssuesRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssuesDistribution(self, request):
        r"""获取问题分布数据

        :param request: Request instance for DescribeIssuesDistribution.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssuesDistributionRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssuesDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssuesDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssuesDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssuesList(self, request):
        r"""获取问题列表数据

        :param request: Request instance for DescribeIssuesList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssuesListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssuesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssuesList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssuesListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIssuesStatisticsTrend(self, request):
        r"""获取问题趋势数据

        :param request: Request instance for DescribeIssuesStatisticsTrend.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeIssuesStatisticsTrendRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeIssuesStatisticsTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIssuesStatisticsTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIssuesStatisticsTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLagANRProblemAccountDetail(self, request):
        r"""获取卡顿ANR问题用户详情

        :param request: Request instance for DescribeLagANRProblemAccountDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeLagANRProblemAccountDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeLagANRProblemAccountDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLagANRProblemAccountDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLagANRProblemAccountDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLagANRProblemFeatureAccounts(self, request):
        r"""获取卡顿ANR问题用户列表

        :param request: Request instance for DescribeLagANRProblemFeatureAccounts.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeLagANRProblemFeatureAccountsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeLagANRProblemFeatureAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLagANRProblemFeatureAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLagANRProblemFeatureAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLagANRProblemList(self, request):
        r"""获取卡顿ANR问题列表数据

        :param request: Request instance for DescribeLagANRProblemList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeLagANRProblemListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeLagANRProblemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLagANRProblemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLagANRProblemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMiniProgramReplayPack(self, request):
        r"""按AppId+BundleHash取已编译回放包正文。成功含Pack（tmpl/css/js/manifest/hash），不返回WXML/WXSS源码。不存在返回ResourceNotFound。

        :param request: Request instance for DescribeMiniProgramReplayPack.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeMiniProgramReplayPackRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeMiniProgramReplayPackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMiniProgramReplayPack", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMiniProgramReplayPackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMiniProgramReplayPacks(self, request):
        r"""按AppId列出回放包元数据，不含Pack正文。可按Status过滤。Limit默认20、最大100。

        :param request: Request instance for DescribeMiniProgramReplayPacks.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeMiniProgramReplayPacksRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeMiniProgramReplayPacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMiniProgramReplayPacks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMiniProgramReplayPacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePerformanceMetrics(self, request):
        r"""获取TDEM性能指标数据

        :param request: Request instance for DescribePerformanceMetrics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribePerformanceMetricsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribePerformanceMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePerformanceMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePerformanceMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectLimits(self, request):
        r"""获取应用上报抽样信息

        :param request: Request instance for DescribeProjectLimits.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeProjectLimitsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeProjectLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjects(self, request):
        r"""获取项目列表（实例创建的团队下的项目列表）

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePvList(self, request):
        r"""获取项目下的PV列表

        :param request: Request instance for DescribePvList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribePvListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribePvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePvList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePvListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseFileSign(self, request):
        r"""获取上传文件存储的临时密钥

        :param request: Request instance for DescribeReleaseFileSign.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFileSignRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFileSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseFileSign", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseFileSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseFiles(self, request):
        r"""获取应用对应sourcemap文件列表

        :param request: Request instance for DescribeReleaseFiles.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFilesRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplayData(self, request):
        r"""从对象存储读取录屏帧数据

        :param request: Request instance for DescribeReplayData.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeReplayDataRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeReplayDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplayData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplayDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplayDetails(self, request):
        r"""获取回放日志

        :param request: Request instance for DescribeReplayDetails.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeReplayDetailsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeReplayDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplayDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplayDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplayMeta(self, request):
        r"""获取回放元数据

        :param request: Request instance for DescribeReplayMeta.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeReplayMetaRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeReplayMetaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplayMeta", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplayMetaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumGroupLog(self, request):
        r"""获取项目下的日志聚合信息

        :param request: Request instance for DescribeRumGroupLog.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumGroupLogRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumGroupLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumGroupLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumGroupLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumGroupLogV2(self, request):
        r"""根据label 聚合分析日志

        :param request: Request instance for DescribeRumGroupLogV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumGroupLogV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumGroupLogV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumGroupLogV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumGroupLogV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumLogDetailsV2(self, request):
        r"""查询日志明细

        :param request: Request instance for DescribeRumLogDetailsV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogDetailsV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogDetailsV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumLogDetailsV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumLogDetailsV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumLogExport(self, request):
        r"""获取项目下的日志列表（实例创建的项目下的日志列表）

        :param request: Request instance for DescribeRumLogExport.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumLogExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumLogExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumLogExportV2(self, request):
        r"""创建日志导出

        :param request: Request instance for DescribeRumLogExportV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumLogExportV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumLogExportV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumLogExports(self, request):
        r"""获取项目下的日志导出列表

        :param request: Request instance for DescribeRumLogExports.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumLogExports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumLogExportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumLogExportsV2(self, request):
        r"""获取日志导出列表

        :param request: Request instance for DescribeRumLogExportsV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportsV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportsV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumLogExportsV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumLogExportsV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumLogList(self, request):
        r"""获取项目下的日志列表（实例创建的项目下的日志列表）

        :param request: Request instance for DescribeRumLogList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumLogTotalV2(self, request):
        r"""查询原始日志总量

        :param request: Request instance for DescribeRumLogTotalV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogTotalV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogTotalV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumLogTotalV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumLogTotalV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumStatsLogList(self, request):
        r"""获取项目下的日志列表，分钟级

        :param request: Request instance for DescribeRumStatsLogList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumStatsLogListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumStatsLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumStatsLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumStatsLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumStatsLogListV2(self, request):
        r"""查询日志时间分布

        :param request: Request instance for DescribeRumStatsLogListV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumStatsLogListV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumStatsLogListV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumStatsLogListV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumStatsLogListV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSampleRate(self, request):
        r"""获取应用的采样率

        :param request: Request instance for DescribeSampleRate.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeSampleRateRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeSampleRateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSampleRate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSampleRateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScores(self, request):
        r"""获取首页分数列表

        :param request: Request instance for DescribeScores.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeScoresRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeScoresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScores", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScoresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScoresV2(self, request):
        r"""获取首页分数列表

        :param request: Request instance for DescribeScoresV2.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeScoresV2Request`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeScoresV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScoresV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScoresV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSessionList(self, request):
        r"""查询会话列表

        :param request: Request instance for DescribeSessionList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeSessionListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStruggleDistribution(self, request):
        r"""获取挣扎事件分布数据

        :param request: Request instance for DescribeStruggleDistribution.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeStruggleDistributionRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeStruggleDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStruggleDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStruggleDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSymbolArtifactUploadCredential(self, request):
        r"""获取符号制品上传临时凭证。

        :param request: Request instance for DescribeSymbolArtifactUploadCredential.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeSymbolArtifactUploadCredentialRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeSymbolArtifactUploadCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSymbolArtifactUploadCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSymbolArtifactUploadCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSymbolArtifacts(self, request):
        r"""分页查询指定类型的符号制品。

        :param request: Request instance for DescribeSymbolArtifacts.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeSymbolArtifactsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeSymbolArtifactsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSymbolArtifacts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSymbolArtifactsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMApplications(self, request):
        r"""查询应用列表，默认仅当前用户名下有权限的应用；可按业务系统 InstanceId 筛选。

        :param request: Request instance for DescribeTDEMApplications.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMApplicationsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMBusinessSystems(self, request):
        r"""查询当前用户名下业务系统列表（超管返回全部）。分页 Offset/Limit，默认 Limit=20 上限 100。

        :param request: Request instance for DescribeTDEMBusinessSystems.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMBusinessSystemsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMBusinessSystemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMBusinessSystems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMBusinessSystemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMDialDimensions(self, request):
        r"""按一个维度拆分拨测指标。Dimension 取值说明：platform、app_version、device、net_type、operator、region、country、target_ip。target_region 不是合法值。region 对应客户端省份，country 对应国家。

        :param request: Request instance for DescribeTDEMDialDimensions.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialDimensionsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialDimensionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMDialDimensions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMDialDimensionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMDialExecutionDetail(self, request):
        r"""返回一个拨测批次的探测结果和路由追踪。Probes 的 Region、Operator 是目标 IP 归属。逐跳归属同时写在 Probes.MTR.Hops 和顶层 MTR.Hops。

        :param request: Request instance for DescribeTDEMDialExecutionDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialExecutionDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialExecutionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMDialExecutionDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMDialExecutionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMDialExecutionList(self, request):
        r"""按批次返回拨测执行记录，一批次一行。TargetIps 是目标地址，TargetIpGeo 是这些地址的地区和运营商。行上的 Region 和 Operator 仍是客户端地区和运营商。

        :param request: Request instance for DescribeTDEMDialExecutionList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialExecutionListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialExecutionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMDialExecutionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMDialExecutionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMDialOverview(self, request):
        r"""按时间窗汇总拨测批次。一次多 IP 探测计为 1 个批次。

        :param request: Request instance for DescribeTDEMDialOverview.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialOverviewRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMDialOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMDialOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMDialTasks(self, request):
        r"""查询应用下未删除的拨测任务，包含启动范围。

        :param request: Request instance for DescribeTDEMDialTasks.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialTasksRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMDialTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMDialTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMDialTrend(self, request):
        r"""按小时或天返回拨测趋势。Granularity 不传时按小时。

        :param request: Request instance for DescribeTDEMDialTrend.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialTrendRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMDialTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMDialTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMDialTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMEventDetail(self, request):
        r"""按 AppId+EventId 查询事件详情，含主表字段与可选符号化结果。Date 推荐传以命中分区；或用 StartDate+EndDate（<=2 天）。越权与不存在统一 ResourceNotFound。

        :param request: Request instance for DescribeTDEMEventDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMEventDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMEventDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMEventDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMEventRank(self, request):
        r"""错误指纹或 API/资源 URL（含按访问页、状态、标签）排行。读 tdem_events，不走主分析立方 GroupBy。Kind：error/api/resource/api_page/resource_page/api_status/api_status_top/resource_status/tag。 Kind=exception_dimension返回当前普通维度或标签值的同批完整分类计数；展开不另行取数。

        :param request: Request instance for DescribeTDEMEventRank.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMEventRankRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMEventRankResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMEventRank", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMEventRankResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMEventSearch(self, request):
        r"""数据探索事件明细分页。会话分类不得调用本接口（Category 禁止 session）。时间单位 Unix 毫秒。

        :param request: Request instance for DescribeTDEMEventSearch.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMEventSearchRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMEventSearchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMEventSearch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMEventSearchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMEventSearchSummary(self, request):
        r"""同一筛选下的分类计数、访问用户、业务用户、窗口合计与分桶趋势。Category 可含 session。空窗返回 0 与空 Series。

        :param request: Request instance for DescribeTDEMEventSearchSummary.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMEventSearchSummaryRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMEventSearchSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMEventSearchSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMEventSearchSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMFieldTransformRules(self, request):
        r"""查询应用下字段值替换规则列表。替代已废弃的 DescribeFieldTransformRules；AppId 为 string。

        :param request: Request instance for DescribeTDEMFieldTransformRules.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFieldTransformRulesRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFieldTransformRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMFieldTransformRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMFieldTransformRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMFunnelDetail(self, request):
        r"""获取漏斗详情

        :param request: Request instance for DescribeTDEMFunnelDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMFunnelDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMFunnelDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMFunnelDimensions(self, request):
        r"""获取漏斗分析报告维度数据

        :param request: Request instance for DescribeTDEMFunnelDimensions.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelDimensionsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelDimensionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMFunnelDimensions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMFunnelDimensionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMFunnelList(self, request):
        r"""获取漏斗列表

        :param request: Request instance for DescribeTDEMFunnelList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMFunnelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMFunnelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMFunnelReport(self, request):
        r"""获取漏斗报告

        :param request: Request instance for DescribeTDEMFunnelReport.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelReportRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMFunnelReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMFunnelReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMFunnelStepSessionList(self, request):
        r"""获取漏斗步骤会话

        :param request: Request instance for DescribeTDEMFunnelStepSessionList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelStepSessionListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelStepSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMFunnelStepSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMFunnelStepSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMFunnelTrend(self, request):
        r"""获取漏斗趋势

        :param request: Request instance for DescribeTDEMFunnelTrend.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelTrendRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMFunnelTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMFunnelTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMFunnelTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMMetricDistribution(self, request):
        r"""按单维度 GroupBy 查询分析指标分布。读 tdem_metric_agg。

        :param request: Request instance for DescribeTDEMMetricDistribution.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMMetricDistributionRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMMetricDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMMetricDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMMetricDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMMetricSummary(self, request):
        r"""查询指定应用与时间窗内的分析指标区间合计。单查返回 Metrics；传 Queries 时返回 Results。读 tdem_metric_agg。

        :param request: Request instance for DescribeTDEMMetricSummary.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMMetricSummaryRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMMetricSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMMetricSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMMetricSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMMetricTrend(self, request):
        r"""查询分析指标时序。可传 CompareStartTime/CompareEndTime 做对比窗（仅批量）。读 tdem_metric_agg。

        :param request: Request instance for DescribeTDEMMetricTrend.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMMetricTrendRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMMetricTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMMetricTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMMetricTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMOverviewScores(self, request):
        r"""客户端总览列表批量评分。按应用列表一次返回各计分项单项分与加权总分。AppIds 1-200；不归属当前用户的应用不出现在响应中。

        :param request: Request instance for DescribeTDEMOverviewScores.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMOverviewScoresRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMOverviewScoresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMOverviewScores", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMOverviewScoresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMRelatedEvents(self, request):
        r"""会话时间线 / 页面子事件 / 错误前轨迹。Mode：timeline / page / breadcrumb。Limit 默认 200，上限 200。

        :param request: Request instance for DescribeTDEMRelatedEvents.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMRelatedEventsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMRelatedEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMRelatedEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMRelatedEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMSSEDimensions(self, request):
        r"""按一个维度返回大模型对话次数和当前指标值，按指标值降序，最多 200 行。region 由 country 与 province 拼接。

        :param request: Request instance for DescribeTDEMSSEDimensions.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSSEDimensionsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSSEDimensionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMSSEDimensions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMSSEDimensionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMSSEDistribution(self, request):
        r"""返回吞吐率、首次消息时延或流畅度的分档分布。档位左闭右开，最后一档有限区间右端闭合，超出右端的样本进入溢出档。错误率与卡死率返回 InvalidParameter。

        :param request: Request instance for DescribeTDEMSSEDistribution.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSSEDistributionRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSSEDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMSSEDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMSSEDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMSSEPercentile(self, request):
        r"""返回吞吐率、首次消息时延或流畅度在整个时间窗及各时间桶上的平均值和 P50、P75、P95、P99。错误率与卡死率返回 InvalidParameter。

        :param request: Request instance for DescribeTDEMSSEPercentile.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSSEPercentileRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSSEPercentileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMSSEPercentile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMSSEPercentileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMSSESummary(self, request):
        r"""查询指定应用与时间窗内的大模型对话汇总，包含对话次数、token 总数、吞吐率、首次消息时延、错误率、卡死率和流畅度。只读 tdem.tdem_events 中 event_type 为 sse_call 的事件。

        :param request: Request instance for DescribeTDEMSSESummary.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSSESummaryRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSSESummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMSSESummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMSSESummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMSSETrend(self, request):
        r"""按时间桶返回大模型对话趋势。overall 填充 Points，其他维度按整个窗口的指标值从高到低取 TopN 并填充 Series。

        :param request: Request instance for DescribeTDEMSSETrend.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSSETrendRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSSETrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMSSETrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMSSETrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMSampleConfig(self, request):
        r"""读取当前生效的 Web 规则化采样文档。ProjectId 必填且 > 0。无行则返回内置缺省（Event.Enabled=true、Types 空、Replay 关闭且体验率 0），不自动插库。SnapshotId 无快照为 0。query handler 做 PascalCase ↔ 存储 snake_case 映射。非 Web 应用不得走本接口，继续 DescribeSampleRate。

        :param request: Request instance for DescribeTDEMSampleConfig.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSampleConfigRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSampleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMSampleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMSampleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMSampleRate(self, request):
        r"""查询单个应用的采集采样率与会话回放采样率。替代已废弃的 DescribeSampleRate；AppId 为 string。

        :param request: Request instance for DescribeTDEMSampleRate.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSampleRateRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSampleRateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMSampleRate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMSampleRateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMSessionReplayTimeline(self, request):
        r"""获取回放时间线数据

        :param request: Request instance for DescribeTDEMSessionReplayTimeline.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSessionReplayTimelineRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMSessionReplayTimelineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMSessionReplayTimeline", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMSessionReplayTimelineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMUsageDetail(self, request):
        r"""按业务系统/应用查询用量明细（含行趋势、端类型、删除/停用标记）。Keyword 匹配业务系统名、应用名或应用 ID。

        :param request: Request instance for DescribeTDEMUsageDetail.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMUsageDetailRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMUsageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMUsageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMUsageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTDEMUsageSummary(self, request):
        r"""查询当前使用者名下（超管为全部）上报总量与趋势。时间 StartTime/EndTime 为 YYYY-MM-DD HH:00:00 小时对齐。不要求请求体带 AppId。

        :param request: Request instance for DescribeTDEMUsageSummary.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMUsageSummaryRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTDEMUsageSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTDEMUsageSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTDEMUsageSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTawAreas(self, request):
        r"""查询片区信息

        :param request: Request instance for DescribeTawAreas.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTawAreasRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTawAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTawAreas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTawAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTawInstances(self, request):
        r"""查询实例信息

        :param request: Request instance for DescribeTawInstances.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTawInstancesRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTawInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTawInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTawInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeToken(self, request):
        r"""查询令牌

        :param request: Request instance for DescribeToken.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTokenRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopIssues(self, request):
        r"""查询top问题列表

        :param request: Request instance for DescribeTopIssues.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTopIssuesRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTopIssuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopIssues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopIssuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserJourneySanKey(self, request):
        r"""获取用户旅程数据

        :param request: Request instance for DescribeUserJourneySanKey.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeUserJourneySanKeyRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeUserJourneySanKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserJourneySanKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserJourneySanKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUvList(self, request):
        r"""获取项目下的UV列表

        :param request: Request instance for DescribeUvList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeUvListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeUvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUvList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUvListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhitelists(self, request):
        r"""获取白名单列表

        :param request: Request instance for DescribeWhitelists.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeWhitelistsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeWhitelistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhitelists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhitelistsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFieldTransformRule(self, request):
        r"""修改字段配置规则

        :param request: Request instance for ModifyFieldTransformRule.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyFieldTransformRuleRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyFieldTransformRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFieldTransformRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFieldTransformRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        r"""修改 RUM 业务系统

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIssueStatus(self, request):
        r"""更新 Issue 状态，支持 resolve、ignore、reopen 等状态流转动作

        :param request: Request instance for ModifyIssueStatus.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyIssueStatusRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyIssueStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIssueStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIssueStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMiniProgramReplayPack(self, request):
        r"""更新回放包元数据，仅支持改Release，不重编译。换源码请再调UploadMiniProgramSource。

        :param request: Request instance for ModifyMiniProgramReplayPack.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyMiniProgramReplayPackRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyMiniProgramReplayPackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMiniProgramReplayPack", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMiniProgramReplayPackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        r"""修改 RUM 应用信息

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProjectLimit(self, request):
        r"""新增修改限流

        :param request: Request instance for ModifyProjectLimit.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyProjectLimitRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyProjectLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProjectLimit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySampleRate(self, request):
        r"""配置tdem采样率

        :param request: Request instance for ModifySampleRate.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifySampleRateRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifySampleRateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySampleRate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySampleRateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTDEMApplication(self, request):
        r"""修改应用，仅传需修改字段。AppId 必填。

        :param request: Request instance for ModifyTDEMApplication.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMApplicationRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTDEMApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTDEMApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTDEMBusinessSystem(self, request):
        r"""修改业务系统名称或描述。越权 UnauthorizedOperation；不存在或已删除 ResourceNotFound。

        :param request: Request instance for ModifyTDEMBusinessSystem.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMBusinessSystemRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMBusinessSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTDEMBusinessSystem", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTDEMBusinessSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTDEMDialTask(self, request):
        r"""修改拨测任务。未出现在请求中的字段保持原值。启动范围传空字符串表示清空该项。Type 和 ExecutionTime 创建后不可修改。暂停和恢复通过 Status 完成，不提供单独的状态接口。

        :param request: Request instance for ModifyTDEMDialTask.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMDialTaskRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMDialTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTDEMDialTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTDEMDialTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTDEMFieldTransformRule(self, request):
        r"""按规则 Id 修改字段值替换规则。替代已废弃的 ModifyFieldTransformRule；AppId 为 string。

        :param request: Request instance for ModifyTDEMFieldTransformRule.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMFieldTransformRuleRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMFieldTransformRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTDEMFieldTransformRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTDEMFieldTransformRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTDEMFunnel(self, request):
        r"""修改漏斗

        :param request: Request instance for ModifyTDEMFunnel.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMFunnelRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMFunnelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTDEMFunnel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTDEMFunnelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTDEMSampleConfig(self, request):
        r"""整页保存 Web 规则化采样文档：校验 → INSERT 快照 → UPSERT 当前行 → 刷新 Redis 下发缓存。不写 tdem_sample_rate。采样率 0–100、最多两位小数；规则 Conditions 不可为空；Types 含非闭集 key 返回 InvalidParameter。校验失败不写库。无 Restore/Import/Export/Diff。

        :param request: Request instance for ModifyTDEMSampleConfig.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMSampleConfigRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMSampleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTDEMSampleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTDEMSampleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTDEMSampleRate(self, request):
        r"""设置或更新应用采集采样率；ReplaySampleRate 可选。替代已废弃的 ModifySampleRate；AppId 为 string。

        :param request: Request instance for ModifyTDEMSampleRate.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMSampleRateRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyTDEMSampleRateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTDEMSampleRate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTDEMSampleRateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PreviewTDEMFunnelReport(self, request):
        r"""根据步骤配置直接生成漏斗预览报告（不保存漏斗，不需要FunnelId）

        :param request: Request instance for PreviewTDEMFunnelReport.
        :type request: :class:`tencentcloud.rum.v20210622.models.PreviewTDEMFunnelReportRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.PreviewTDEMFunnelReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PreviewTDEMFunnelReport", params, headers=headers)
            response = json.loads(body)
            model = models.PreviewTDEMFunnelReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeInstance(self, request):
        r"""恢复 RUM 业务系统，恢复后，用户可以正常使用和上报数据

        :param request: Request instance for ResumeInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.ResumeInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ResumeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeProject(self, request):
        r"""恢复应用使用与上报数据

        :param request: Request instance for ResumeProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.ResumeProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ResumeProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeProject", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeTDEMApplication(self, request):
        r"""恢复已停止的应用，Status 变为 2。

        :param request: Request instance for ResumeTDEMApplication.
        :type request: :class:`tencentcloud.rum.v20210622.models.ResumeTDEMApplicationRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ResumeTDEMApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeTDEMApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeTDEMApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopInstance(self, request):
        r"""停止实例

        :param request: Request instance for StopInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.StopInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.StopInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StopInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopProject(self, request):
        r"""停止项目使用与上报数据

        :param request: Request instance for StopProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.StopProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.StopProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopProject", params, headers=headers)
            response = json.loads(body)
            model = models.StopProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopTDEMApplication(self, request):
        r"""停止应用采集，Status 变为 6。

        :param request: Request instance for StopTDEMApplication.
        :type request: :class:`tencentcloud.rum.v20210622.models.StopTDEMApplicationRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.StopTDEMApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopTDEMApplication", params, headers=headers)
            response = json.loads(body)
            model = models.StopTDEMApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadMiniProgramSource(self, request):
        r"""上传微信小程序源码zip并同步编译回放包。控制台传FileBase64；zip需含app.json，跳过node_modules。同AppId+BundleHash且已ready则幂等。

        :param request: Request instance for UploadMiniProgramSource.
        :type request: :class:`tencentcloud.rum.v20210622.models.UploadMiniProgramSourceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.UploadMiniProgramSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadMiniProgramSource", params, headers=headers)
            response = json.loads(body)
            model = models.UploadMiniProgramSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadSymbolArtifact(self, request):
        r"""登记已上传的符号制品。请先获取上传凭证并将文件上传到 COS。

        :param request: Request instance for UploadSymbolArtifact.
        :type request: :class:`tencentcloud.rum.v20210622.models.UploadSymbolArtifactRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.UploadSymbolArtifactResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadSymbolArtifact", params, headers=headers)
            response = json.loads(body)
            model = models.UploadSymbolArtifactResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))