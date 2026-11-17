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
from tencentcloud.dbs.v20211108 import models


class DbsClient(AbstractClient):
    _apiVersion = '2021-11-08'
    _endpoint = 'dbs.tencentcloudapi.com'
    _service = 'dbs'


    def ConfigureBackupPlan(self, request):
        r"""本接口（ConfigureBackupPlan）用于配置备份计划。包括配置备份源实例信息、备份对象以及备份策略等。

        :param request: Request instance for ConfigureBackupPlan.
        :type request: :class:`tencentcloud.dbs.v20211108.models.ConfigureBackupPlanRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.ConfigureBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfigureBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.ConfigureBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackupPlan(self, request):
        r"""该接口用于创建备份计划。

        :param request: Request instance for CreateBackupPlan.
        :type request: :class:`tencentcloud.dbs.v20211108.models.CreateBackupPlanRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.CreateBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConnectTestJob(self, request):
        r"""该接口用于创建连通性检测任务，请在创建备份计划前，通过该接口来检测你的源端实例是否连通性正常。

        :param request: Request instance for CreateConnectTestJob.
        :type request: :class:`tencentcloud.dbs.v20211108.models.CreateConnectTestJobRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.CreateConnectTestJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConnectTestJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConnectTestJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackupPlan(self, request):
        r"""删除备份计划。

        仅已下线的备份计划支持删除，删除后不可恢复。已隔离（isolated）的备份计划请先调用 DestroyBackupPlanByUser 完成下线，再进行删除。调用接口后，若通过 DescribeBackupPlans 接口查询不到对应的备份计划，则表示删除成功。

        :param request: Request instance for DeleteBackupPlan.
        :type request: :class:`tencentcloud.dbs.v20211108.models.DeleteBackupPlanRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.DeleteBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupCheckJob(self, request):
        r"""本接口（DescribeBackupCheckJob）用于查询备份计划预校验任务的结果。仅对于预校验通过的任务，才能启动备份计划。

        :param request: Request instance for DescribeBackupCheckJob.
        :type request: :class:`tencentcloud.dbs.v20211108.models.DescribeBackupCheckJobRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.DescribeBackupCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupPlanDetail(self, request):
        r"""查询备份计划详情。
        返回备份计划的基本信息、源库信息、备份对象、备份策略、备份进度和付费信息。

        :param request: Request instance for DescribeBackupPlanDetail.
        :type request: :class:`tencentcloud.dbs.v20211108.models.DescribeBackupPlanDetailRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.DescribeBackupPlanDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupPlanDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupPlanDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupPlans(self, request):
        r"""本接口（DescribeBackupPlans）用于查询备份计划列表。

        :param request: Request instance for DescribeBackupPlans.
        :type request: :class:`tencentcloud.dbs.v20211108.models.DescribeBackupPlansRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.DescribeBackupPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupPlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConnectTestResult(self, request):
        r"""该接口用于查询连通性检测任务的结果

        :param request: Request instance for DescribeConnectTestResult.
        :type request: :class:`tencentcloud.dbs.v20211108.models.DescribeConnectTestResultRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.DescribeConnectTestResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConnectTestResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConnectTestResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFullBackupSetDetail(self, request):
        r"""查询全量备份集详情。

        返回全量备份集的基本信息、源库信息、备份对象、备份进度和加密信息。

        :param request: Request instance for DescribeFullBackupSetDetail.
        :type request: :class:`tencentcloud.dbs.v20211108.models.DescribeFullBackupSetDetailRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.DescribeFullBackupSetDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFullBackupSetDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFullBackupSetDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIncrementBackupSetFiles(self, request):
        r"""查询增量备份集文件列表。

        文件按最后修改时间倒序返回，支持分页。

        :param request: Request instance for DescribeIncrementBackupSetFiles.
        :type request: :class:`tencentcloud.dbs.v20211108.models.DescribeIncrementBackupSetFilesRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.DescribeIncrementBackupSetFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIncrementBackupSetFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIncrementBackupSetFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIncrementBackupSets(self, request):
        r"""本接口（DescribeIncrementBackupSets）用于查询增量备份集列表。

        :param request: Request instance for DescribeIncrementBackupSets.
        :type request: :class:`tencentcloud.dbs.v20211108.models.DescribeIncrementBackupSetsRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.DescribeIncrementBackupSetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIncrementBackupSets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIncrementBackupSetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyBackupPlanByUser(self, request):
        r"""立即下线已隔离的备份计划。

        下线后备份计划不可恢复。调用接口后，若通过 DescribeBackupPlanDetail 接口查询到备份计划状态为 offlined，则表示下线成功。

        :param request: Request instance for DestroyBackupPlanByUser.
        :type request: :class:`tencentcloud.dbs.v20211108.models.DestroyBackupPlanByUserRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.DestroyBackupPlanByUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyBackupPlanByUser", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyBackupPlanByUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupPlanSourceInfo(self, request):
        r"""本接口（ModifyBackupPlanSourceInfo）用于修改备份计划的源实例信息、备份对象信息等。注意，调用该接口后，原有备份计划任务将立即停止，您可以在修改完源信息后重新启动备份任务。

        :param request: Request instance for ModifyBackupPlanSourceInfo.
        :type request: :class:`tencentcloud.dbs.v20211108.models.ModifyBackupPlanSourceInfoRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.ModifyBackupPlanSourceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupPlanSourceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupPlanSourceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeBackupPlan(self, request):
        r"""恢复已暂停的备份计划。

        仅已暂停的备份计划支持恢复。调用接口后，若通过 DescribeBackupPlanDetail 接口查询到备份计划状态为 running，则表示恢复成功。

        :param request: Request instance for ResumeBackupPlan.
        :type request: :class:`tencentcloud.dbs.v20211108.models.ResumeBackupPlanRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.ResumeBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartBackupCheckJob(self, request):
        r"""本接口（StartBackupCheckJob）用于创建备份计划预校验任务。

        :param request: Request instance for StartBackupCheckJob.
        :type request: :class:`tencentcloud.dbs.v20211108.models.StartBackupCheckJobRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.StartBackupCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartBackupCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.StartBackupCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartBackupPlan(self, request):
        r"""本接口（StartBackupPlan）用于启动备份计划。调用此接口前，请务必先使用 StartBackupCheckJob 创建备份计划预校验任务，并通过 DescribeBackupCheckJob 接口查询到任务状态为校验通过时，才能启动备份计划。

        :param request: Request instance for StartBackupPlan.
        :type request: :class:`tencentcloud.dbs.v20211108.models.StartBackupPlanRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.StartBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.StartBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopBackupPlan(self, request):
        r"""暂停备份计划。

        仅运行中的备份计划支持暂停。调用接口后，若通过 DescribeBackupPlanDetail 接口查询到备份计划状态为 paused，则表示暂停成功。

        :param request: Request instance for StopBackupPlan.
        :type request: :class:`tencentcloud.dbs.v20211108.models.StopBackupPlanRequest`
        :rtype: :class:`tencentcloud.dbs.v20211108.models.StopBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.StopBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))