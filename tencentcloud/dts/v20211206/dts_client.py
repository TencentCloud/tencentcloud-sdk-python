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
from tencentcloud.dts.v20211206 import models


class DtsClient(AbstractClient):
    _apiVersion = '2021-12-06'
    _endpoint = 'dts.tencentcloudapi.com'
    _service = 'dts'


    def CompleteMigrateJob(self, request):
        """本接口（CompleteMigrateJob）用于完成数据迁移任务。
        选择采用增量迁移方式的任务, 需要在迁移进度进入准备完成阶段后, 调用本接口, 停止迁移增量数据。
        通过DescribeMigrationJobs接口查询到任务的状态为准备完成（Status="readyComplete"）时，此时可以调用本接口完成迁移任务。

        :param request: Request instance for CompleteMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CompleteMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompleteMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompleteMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.CompleteMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ConfigureSyncJob(self, request):
        """配置一个同步任务

        :param request: Request instance for ConfigureSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ConfigureSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ConfigureSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfigureSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.ConfigureSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ContinueMigrateJob(self, request):
        """恢复一个暂停中的迁移任务。

        :param request: Request instance for ContinueMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ContinueMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ContinueMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ContinueMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.ContinueMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ContinueSyncJob(self, request):
        """恢复处于已暂停状态的数据同步任务。

        :param request: Request instance for ContinueSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ContinueSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ContinueSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ContinueSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.ContinueSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCheckSyncJob(self, request):
        """校验同步任务，检查必要参数和周边配置。

        :param request: Request instance for CreateCheckSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateCheckSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateCheckSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCheckSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCheckSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCompareTask(self, request):
        """本接口用于创建数据对比任务，创建成功后会返回数据对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9，创建成功后可通过StartCompare启动一致性校验任务

        :param request: Request instance for CreateCompareTask.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateCompareTaskRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateCompareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCompareTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCompareTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMigrateCheckJob(self, request):
        """校验迁移任务，
        在开始迁移前, 必须调用本接口创建校验迁移任务, 且校验成功后才能开始迁移. 校验的结果可以通过DescribeMigrationCheckJob查看，
        校验成功后,迁移任务若有修改, 则必须重新校验并通过后, 才能开始迁移

        :param request: Request instance for CreateMigrateCheckJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateMigrateCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateMigrateCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMigrateCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMigrateCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMigrationService(self, request):
        """购买迁移任务。购买成功后会返回随机生成的迁移任务id列表，也可以通过查询迁移任务任务列表接口`DescribeMigrationJobs`看到购买成功的实例Id。注意，一旦购买成功后源及目标数据库类型，源及目标实例地域不可修改。

        :param request: Request instance for CreateMigrationService.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateMigrationServiceRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateMigrationServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMigrationService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMigrationServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSyncJob(self, request):
        """创建一个同步任务

        :param request: Request instance for CreateSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCompareTask(self, request):
        """删除一致性校验任务。当一致性校验任务状态为success、failed、canceled 时可以执行此操作。

        :param request: Request instance for DeleteCompareTask.
        :type request: :class:`tencentcloud.dts.v20211206.models.DeleteCompareTaskRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DeleteCompareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCompareTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCompareTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCheckSyncJobResult(self, request):
        """查询同步校验任务结果，检查必要参数和周边配置

        :param request: Request instance for DescribeCheckSyncJobResult.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeCheckSyncJobResultRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeCheckSyncJobResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCheckSyncJobResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCheckSyncJobResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCompareReport(self, request):
        """查询一致性校验任务详情

        :param request: Request instance for DescribeCompareReport.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeCompareReportRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeCompareReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompareReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompareReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCompareTasks(self, request):
        """查询一致性校验任务列表，调用该接口后可通过接口`DescribeCompareTasks` 查询一致性校验任务列表来获得启动后的状态。

        :param request: Request instance for DescribeCompareTasks.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeCompareTasksRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeCompareTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompareTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompareTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMigrateDBInstances(self, request):
        """本接口用于查询支持迁移的云数据库实例

        :param request: Request instance for DescribeMigrateDBInstances.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeMigrateDBInstancesRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeMigrateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMigrationCheckJob(self, request):
        """本接口用于创建校验后,获取校验的结果. 能查询到当前校验的状态和进度.
        若通过校验, 则可调用'StartMigrateJob' 开始迁移.
        若未通过校验, 则能查询到校验失败的原因. 请按照报错, 通过'ModifyMigrationJob'修改迁移配置或是调整源/目标实例的相关参数.

        :param request: Request instance for DescribeMigrationCheckJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMigrationDetail(self, request):
        """查询某个迁移任务详情

        :param request: Request instance for DescribeMigrationDetail.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationDetailRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMigrationJobs(self, request):
        """查询数据迁移任务列表

        :param request: Request instance for DescribeMigrationJobs.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSyncJobs(self, request):
        """查询同步任务信息

        :param request: Request instance for DescribeSyncJobs.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeSyncJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeSyncJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSyncJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSyncJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyMigrateJob(self, request):
        """下线数据迁移任务。计费任务必须先调用隔离(IsolateMigrateJob)接口，且只有是**已隔离**状态下，才能调用此接口销毁任务。对于不计费任务，调用隔离(IsolateMigrateJob)接口删除任务操作。

        :param request: Request instance for DestroyMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.DestroyMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DestroyMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroySyncJob(self, request):
        """下线同步任务，任务在已隔离状态下可以通过此操作进行任务下线，即彻底删除任务。下线操作后可通过查询同步任务信息接口DescribeSyncJobs获取任务列表查看状态，此操作成功后无法看到此任务表示下线成功。

        :param request: Request instance for DestroySyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.DestroySyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DestroySyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroySyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.DestroySyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateMigrateJob(self, request):
        """隔离退还数据迁移服务。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。对于计费任务，在任务隔离后可进行解除隔离(RecoverMigrationJob)操作或直接进行下线销毁(DestroyMigrateJob)操作。对于不计费任务，调用此接口会直接销毁任务，无法进行恢复操作。

        :param request: Request instance for IsolateMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.IsolateMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.IsolateMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateSyncJob(self, request):
        """隔离同步任务，隔离后可通过查询同步任务信息接口DescribeSyncJobs获取隔离后状态。在任务隔离后可进行解除隔离(RecoverSyncJob)操作或直接进行下线操作。对于不计费任务，调用此接口后会直接删除任务，无法进行恢复操作。

        :param request: Request instance for IsolateSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.IsolateSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.IsolateSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCompareTask(self, request):
        """修改一致性校验任务，在任务创建后启动之前，可修改一致性校验参数

        :param request: Request instance for ModifyCompareTask.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyCompareTaskRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyCompareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCompareTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCompareTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCompareTaskName(self, request):
        """修改一致性校验任务名称

        :param request: Request instance for ModifyCompareTaskName.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyCompareTaskNameRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyCompareTaskNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCompareTaskName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCompareTaskNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMigrateJobSpec(self, request):
        """调整实例规格，此接口只支持按量计费任务的调整。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。

        :param request: Request instance for ModifyMigrateJobSpec.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateJobSpecRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrateJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrateJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMigrateName(self, request):
        """修改迁移任务名

        :param request: Request instance for ModifyMigrateName.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateNameRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrateName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrateNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMigrationJob(self, request):
        """配置迁移服务，配置成功后可通过`CreateMigrationCheckJob` 创建迁移校验任务接口发起校验任务，只有校验通过才能启动迁移任务。

        :param request: Request instance for ModifyMigrationJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyMigrationJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyMigrationJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrationJob", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrationJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PauseMigrateJob(self, request):
        """暂停一个迁移任务。

        :param request: Request instance for PauseMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.PauseMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.PauseMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.PauseMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PauseSyncJob(self, request):
        """暂停处于同步中的数据同步任务。

        :param request: Request instance for PauseSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.PauseSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.PauseSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.PauseSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecoverMigrateJob(self, request):
        """解除隔离数据迁移任务，用户手动发起隔离后的手动解隔离，只有任务状态为已隔离(手动操作)状态下才能触发此操作。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。

        :param request: Request instance for RecoverMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.RecoverMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.RecoverMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecoverSyncJob(self, request):
        """解除隔离同步任务，任务在已隔离状态下可调用该接口解除隔离状态任务，同时可通过查询同步任务信息接口DescribeSyncJobs，获取操作后状态。

        :param request: Request instance for RecoverSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.RecoverSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.RecoverSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResizeSyncJob(self, request):
        """调整同步任务规格，此接口只支持按量计费任务的调整，调用此接口后不会立即生效，后台调整时间大概为3~5分钟。调用此接口后可通过查询同步任务信息接口DescribeSyncJobs，获取变配后的状态。

        :param request: Request instance for ResizeSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ResizeSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ResizeSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeMigrateJob(self, request):
        """重试数据迁移任务，针对异常情况可进行重试，对于redis在失败时也可重试。注意：此操作跳过校验阶段，直接重新发起任务，相当于从StartMigrationJob开始执行。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。

        :param request: Request instance for ResumeMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ResumeMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ResumeMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeSyncJob(self, request):
        """重试同步任务，部分可恢复报错情况下，可通过该接口重试同步任务，可通过查询同步任务信息接口DescribeSyncJobs，获取操作后状态。

        :param request: Request instance for ResumeSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ResumeSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ResumeSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SkipCheckItem(self, request):
        """本接口用于校验检查项不通过后，可进行跳过此校验项操作，后端将不再校验该项。任何校验步骤都是不应该跳过的，通过校验是能正确执行的前置条件。支持跳过的产品及链路的校验项可 [参考文档](https://cloud.tencent.com/document/product/571/61639)。

        :param request: Request instance for SkipCheckItem.
        :type request: :class:`tencentcloud.dts.v20211206.models.SkipCheckItemRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.SkipCheckItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SkipCheckItem", params, headers=headers)
            response = json.loads(body)
            model = models.SkipCheckItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SkipSyncCheckItem(self, request):
        """本接口用于校验检查项不通过后，可进行跳过此校验项操作，后端将不再校验该项。任何校验步骤都是不应该跳过的，通过校验是能正确执行的前置条件。支持跳过的产品及链路的校验项可 [参考文档](https://cloud.tencent.com/document/product/571/61639)。

        :param request: Request instance for SkipSyncCheckItem.
        :type request: :class:`tencentcloud.dts.v20211206.models.SkipSyncCheckItemRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.SkipSyncCheckItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SkipSyncCheckItem", params, headers=headers)
            response = json.loads(body)
            model = models.SkipSyncCheckItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartCompare(self, request):
        """启动一致性校验任务，启动之前需要先通过接口`CreateCompareTask` 创建一致性校验任务，启动后可通过接口`DescribeCompareTasks` 查询一致性校验任务列表来获得启动后的状态

        :param request: Request instance for StartCompare.
        :type request: :class:`tencentcloud.dts.v20211206.models.StartCompareRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StartCompareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartCompare", params, headers=headers)
            response = json.loads(body)
            model = models.StartCompareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartMigrateJob(self, request):
        """本接口（StartMigrationJob）用于启动迁移任务。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。

        :param request: Request instance for StartMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.StartMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StartMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.StartMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartSyncJob(self, request):
        """启动同步任务

        :param request: Request instance for StartSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.StartSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StartSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.StartSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopCompare(self, request):
        """终止一致性校验任务

        :param request: Request instance for StopCompare.
        :type request: :class:`tencentcloud.dts.v20211206.models.StopCompareRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StopCompareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCompare", params, headers=headers)
            response = json.loads(body)
            model = models.StopCompareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopMigrateJob(self, request):
        """本接口（StopMigrateJob）用于终止数据迁移任务。
        调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。

        :param request: Request instance for StopMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.StopMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StopMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.StopMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopSyncJob(self, request):
        """结束同步任务，操作后可通过查询同步任务信息接口DescribeSyncJobs，获取操作后的状态。

        :param request: Request instance for StopSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.StopSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StopSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.StopSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)