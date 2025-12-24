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