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
from tencentcloud.dts.v20211206 import models


class DtsClient(AbstractClient):
    _apiVersion = '2021-12-06'
    _endpoint = 'dts.tencentcloudapi.com'
    _service = 'dts'


    def CompleteMigrateJob(self, request):
        r"""本接口（CompleteMigrateJob）用于完成数据迁移任务。
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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfigureSubscribeJob(self, request):
        r"""本接口(ConfigureSubscribeJob)用于配置数据订阅实例。

        :param request: Request instance for ConfigureSubscribeJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ConfigureSubscribeJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ConfigureSubscribeJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfigureSubscribeJob", params, headers=headers)
            response = json.loads(body)
            model = models.ConfigureSubscribeJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfigureSyncJob(self, request):
        r"""配置一个同步任务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ContinueMigrateJob(self, request):
        r"""恢复一个暂停中的迁移任务。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ContinueSyncJob(self, request):
        r"""恢复处于已暂停状态的数据同步任务。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCheckSyncJob(self, request):
        r"""校验同步任务，检查必要参数和周边配置。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCompareTask(self, request):
        r"""本接口用于创建数据对比任务，创建成功后会返回数据对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9，创建成功后可通过StartCompare启动一致性校验任务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsumerGroup(self, request):
        r"""为订阅实例创建消费者组。
        只有状态为运行中的实例支持创建消费组。

        :param request: Request instance for CreateConsumerGroup.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateConsumerGroupRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMigrateCheckJob(self, request):
        r"""创建校验迁移任务，
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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMigrationService(self, request):
        r"""购买迁移任务。购买成功后会返回随机生成的迁移任务id列表，也可以通过查询迁移任务任务列表接口`DescribeMigrationJobs`看到购买成功的实例Id。注意，一旦购买成功后源及目标数据库类型，源及目标实例地域不可修改。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModifyCheckSyncJob(self, request):
        r"""在修改同步任务的配置后、通过该接口校验当前任务是否支持修改对象操作

        :param request: Request instance for CreateModifyCheckSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateModifyCheckSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateModifyCheckSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModifyCheckSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModifyCheckSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubscribe(self, request):
        r"""本接口(CreateSubscribe)用于创建一个数据订阅任务。

        :param request: Request instance for CreateSubscribe.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubscribeCheckJob(self, request):
        r"""本接口(CreateSubscribeCheckJob)用于创建一个订阅校验任务。任务必须已经成功调用ConfigureSubscribeJob接口配置了所有的必要信息才能启动校验。

        :param request: Request instance for CreateSubscribeCheckJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateSubscribeCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateSubscribeCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubscribeCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubscribeCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSyncJob(self, request):
        r"""创建一个同步任务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCompareTask(self, request):
        r"""删除一致性校验任务。当一致性校验任务状态为success、failed、canceled 时可以执行此操作。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConsumerGroup(self, request):
        r"""本接口(DeleteConsumerGroup)用于删除一个订阅任务的消费组。

        :param request: Request instance for DeleteConsumerGroup.
        :type request: :class:`tencentcloud.dts.v20211206.models.DeleteConsumerGroupRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DeleteConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCheckSyncJobResult(self, request):
        r"""查询同步校验任务结果，检查必要参数和周边配置

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompareReport(self, request):
        r"""查询一致性校验任务详情

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompareTasks(self, request):
        r"""查询一致性校验任务列表。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerGroups(self, request):
        r"""本接口(DescribeConsumerGroups)用于获取订阅实例配置的消费者组详情。

        :param request: Request instance for DescribeConsumerGroups.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeConsumerGroupsRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeConsumerGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrateDBInstances(self, request):
        r"""本接口用于查询支持迁移的云数据库实例

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationCheckJob(self, request):
        r"""本接口用于创建校验后,获取校验的结果. 能查询到当前校验的状态和进度.
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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationDetail(self, request):
        r"""查询某个迁移任务详情

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationJobs(self, request):
        r"""查询数据迁移任务列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModifyCheckSyncJobResult(self, request):
        r"""在创建修改对象的校验任务后、通过该接口查看校验任务的结果

        :param request: Request instance for DescribeModifyCheckSyncJobResult.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeModifyCheckSyncJobResultRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeModifyCheckSyncJobResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModifyCheckSyncJobResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModifyCheckSyncJobResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOffsetByTime(self, request):
        r"""本接口(DescribeOffsetByTime)查询KafkaTopic中指定时间前最近的offset。
        接口输出的offset是离这个时间最近的offset。
        如果输入时间比当前时间晚的多，相当于输出的就是最新的offset；
        如果输入时间比当前时间早的多，相当于输出的就是最老的offset；
        如果输入空，默认0时间，也就是查询最老的offset。

        :param request: Request instance for DescribeOffsetByTime.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeOffsetByTimeRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeOffsetByTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOffsetByTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOffsetByTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubscribeCheckJob(self, request):
        r"""本接口(DescribeSubscribeCheckJob)用于查询订阅校验任务结果。

        :param request: Request instance for DescribeSubscribeCheckJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeSubscribeCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeSubscribeCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubscribeCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubscribeCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubscribeDetail(self, request):
        r"""本接口(DescribeSubscribeDetail)获取数据订阅实例的配置信息。

        :param request: Request instance for DescribeSubscribeDetail.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeSubscribeDetailRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeSubscribeDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubscribeDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubscribeDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubscribeJobs(self, request):
        r"""本接口(DescribeSubscribes)获取数据订阅实例信息列表，默认分页，每次返回20条

        :param request: Request instance for DescribeSubscribeJobs.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeSubscribeJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeSubscribeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubscribeJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubscribeJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubscribeReturnable(self, request):
        r"""本接口(DescribeSubscribeReturnable)用于查询订阅任务是否可以销毁和退货。

        :param request: Request instance for DescribeSubscribeReturnable.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeSubscribeReturnableRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeSubscribeReturnableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubscribeReturnable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubscribeReturnableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSyncJobs(self, request):
        r"""查询同步任务信息

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyIsolatedSubscribe(self, request):
        r"""本接口（DestroyIsolatedSubscribe）用于下线已隔离的数据订阅实例

        :param request: Request instance for DestroyIsolatedSubscribe.
        :type request: :class:`tencentcloud.dts.v20211206.models.DestroyIsolatedSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DestroyIsolatedSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyIsolatedSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyIsolatedSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyMigrateJob(self, request):
        r"""下线数据迁移任务。计费任务必须先调用隔离(IsolateMigrateJob)接口，且只有是**已隔离**状态下，才能调用此接口销毁任务。对于不计费任务，调用隔离(IsolateMigrateJob)接口删除任务操作。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroySyncJob(self, request):
        r"""下线同步任务，任务在已隔离状态下可以通过此操作进行任务下线，即彻底删除任务。下线操作后可通过查询同步任务信息接口DescribeSyncJobs获取任务列表查看状态，此操作成功后无法看到此任务表示下线成功。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateMigrateJob(self, request):
        r"""隔离退还数据迁移服务。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。对于计费任务，在任务隔离后可进行解除隔离(RecoverMigrateJob)操作或直接进行下线销毁(DestroyMigrateJob)操作。对于不计费任务，调用此接口会直接销毁任务，无法进行恢复操作。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateSubscribe(self, request):
        r"""本接口（IsolateSubscribe）用于隔离订阅任务。调用后，订阅任务将不能使用。按量计费的任务会停止计费，包年包月的任务会自动退费

        :param request: Request instance for IsolateSubscribe.
        :type request: :class:`tencentcloud.dts.v20211206.models.IsolateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.IsolateSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateSyncJob(self, request):
        r"""隔离同步任务，隔离后可通过查询同步任务信息接口DescribeSyncJobs获取隔离后状态。在任务隔离后可进行解除隔离(RecoverSyncJob)操作或直接进行下线(DestroySyncJob)操作。对于不计费任务，调用此接口后会直接删除任务，无法进行恢复操作。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCompareTask(self, request):
        r"""修改一致性校验任务，在任务创建后启动之前，可修改一致性校验参数

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCompareTaskName(self, request):
        r"""修改一致性校验任务名称

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsumerGroupDescription(self, request):
        r"""本接口(ModifyConsumerGroupDescription)用于修改指定订阅消费组备注。

        :param request: Request instance for ModifyConsumerGroupDescription.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyConsumerGroupDescriptionRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyConsumerGroupDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsumerGroupDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsumerGroupDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsumerGroupPassword(self, request):
        r"""本接口(ModifyConsumerGroupPassword)用于修改指定订阅消费组密码。

        :param request: Request instance for ModifyConsumerGroupPassword.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyConsumerGroupPasswordRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyConsumerGroupPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsumerGroupPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsumerGroupPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigrateJobSpec(self, request):
        r"""调整实例规格，此接口只支持按量计费任务的调整，且仅在计费或者待计费状态下支持修改。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigrateName(self, request):
        r"""修改迁移任务名

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigrateRateLimit(self, request):
        r"""用户在发现迁移任务对用户的数据库的负载影响较大时、可通过该接口限制任务的传输速率；此操作仅在任务运行中可执行。

        :param request: Request instance for ModifyMigrateRateLimit.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateRateLimitRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrateRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrateRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigrateRuntimeAttribute(self, request):
        r"""修改任务运行时属性，此接口不同于配置类接口，不会进行状态机判断。

        :param request: Request instance for ModifyMigrateRuntimeAttribute.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateRuntimeAttributeRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateRuntimeAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrateRuntimeAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrateRuntimeAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigrationJob(self, request):
        r"""配置迁移服务，配置成功后可通过`CreateMigrateCheckJob` 创建迁移校验任务接口发起校验任务，只有校验通过才能启动迁移任务。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubscribeAutoRenewFlag(self, request):
        r"""修改订阅实例自动续费标识。只有包年包月的任务修改才有意义，按量计费任务修改后无影响。

        :param request: Request instance for ModifySubscribeAutoRenewFlag.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifySubscribeAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifySubscribeAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubscribeAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubscribeAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubscribeName(self, request):
        r"""本接口(ModifySubscribeName)用于修改数据订阅实例的名称

        :param request: Request instance for ModifySubscribeName.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifySubscribeNameRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifySubscribeNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubscribeName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubscribeNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubscribeObjects(self, request):
        r"""本接口(ModifySubscribeObjects)用于修改数据订阅对象和kafka分区规则，如果是mongo订阅，还可以修改输出聚合规则。

        :param request: Request instance for ModifySubscribeObjects.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifySubscribeObjectsRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifySubscribeObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubscribeObjects", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubscribeObjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySyncJobConfig(self, request):
        r"""该接口支持在同步任务启动后修改任务的配置
        修改同步配置的完整流程：修改同步任务配置->创建修改同步任务配置的校验任务->查询修改配置的校验任务的结果->启动修改配置任务

        :param request: Request instance for ModifySyncJobConfig.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifySyncJobConfigRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifySyncJobConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySyncJobConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySyncJobConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySyncRateLimit(self, request):
        r"""用户在发现同步任务对用户的数据库的负载影响较大时、可通过该接口限制任务的传输速率

        :param request: Request instance for ModifySyncRateLimit.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifySyncRateLimitRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifySyncRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySyncRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySyncRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseMigrateJob(self, request):
        r"""暂停一个迁移任务。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseSyncJob(self, request):
        r"""暂停处于同步中的数据同步任务。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverMigrateJob(self, request):
        r"""解除隔离数据迁移任务，用户手动发起隔离后的手动解隔离，只有任务状态为已隔离(手动操作)状态下才能触发此操作。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverSyncJob(self, request):
        r"""解除隔离同步任务，任务在已隔离状态下可调用该接口解除隔离状态任务，同时可通过查询同步任务信息接口DescribeSyncJobs，获取操作后状态。注意，此接口只支持按量计费实例。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetConsumerGroupOffset(self, request):
        r"""本接口(ResetConsumerGroupOffset)用于重置订阅消费组的offset。调用DescribeConsumerGroups接口查询消费组状态，只有消费组状态为 Dead 或 Empty 才可以执行重置该操作。否则重置不会生效，接口也不会报错。

        :param request: Request instance for ResetConsumerGroupOffset.
        :type request: :class:`tencentcloud.dts.v20211206.models.ResetConsumerGroupOffsetRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ResetConsumerGroupOffsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetConsumerGroupOffset", params, headers=headers)
            response = json.loads(body)
            model = models.ResetConsumerGroupOffsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetSubscribe(self, request):
        r"""本接口(ResetSubscribe)用于重置订阅实例，重置后，可以重新配置订阅任务。
        可以调用 [DescribeSubscribeDetail](https://cloud.tencent.com/document/product/571/102944) 查询订阅信息判断是否置成功。当SubsStatus变为notStarted时，表示重置成功。

        :param request: Request instance for ResetSubscribe.
        :type request: :class:`tencentcloud.dts.v20211206.models.ResetSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ResetSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.ResetSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetSyncJob(self, request):
        r"""重置已经结束的同步任务，重置后可以重新配置启动任务。

        :param request: Request instance for ResetSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ResetSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ResetSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.ResetSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeSyncJob(self, request):
        r"""调整同步任务规格，此接口只支持按量计费任务的调整，调用此接口后不会立即生效，后台调整时间大概为3~5分钟。调用此接口后可通过查询同步任务信息接口DescribeSyncJobs，获取变配后的状态。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeMigrateJob(self, request):
        r"""重试数据迁移任务，针对异常情况可进行重试，对于redis在失败时也可重试。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeSubscribe(self, request):
        r"""本接口(ResumeSubscribe) 用于恢复报错的订阅任务。当订阅任务的状态为error时，可通过本接口尝试对任务进行恢复。

        :param request: Request instance for ResumeSubscribe.
        :type request: :class:`tencentcloud.dts.v20211206.models.ResumeSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ResumeSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeSyncJob(self, request):
        r"""重试同步任务，部分可恢复报错情况下，可通过该接口重试同步任务，可通过查询同步任务信息接口DescribeSyncJobs，获取操作后状态。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SkipCheckItem(self, request):
        r"""本接口用于校验检查项不通过后，可进行跳过此校验项操作，后端将不再校验该项。任何校验步骤都是不应该跳过的，通过校验是能正确执行的前置条件。支持跳过的产品及链路的校验项可 [参考文档](https://cloud.tencent.com/document/product/571/61639)。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SkipSyncCheckItem(self, request):
        r"""本接口用于校验检查项不通过后，可进行跳过此校验项操作，后端将不再校验该项。任何校验步骤都是不应该跳过的，通过校验是能正确执行的前置条件。支持跳过的产品及链路的校验项可 [参考文档](https://cloud.tencent.com/document/product/571/61639)。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartCompare(self, request):
        r"""启动一致性校验任务，启动之前需要先通过接口 [CreateCompareTask](https://cloud.tencent.com/document/product/571/82093) 创建一致性校验任务，启动后可通过接口 [DescribeCompareTasks](https://cloud.tencent.com/document/product/571/82088) 查询一致性校验任务列表来获得启动后的状态

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartMigrateJob(self, request):
        r"""本接口（StartMigrateJob）用于启动迁移任务。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartModifySyncJob(self, request):
        r"""在查询修改对象的校验任务的结果中的status为success后、通过该接口开始修改配置流程

        :param request: Request instance for StartModifySyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.StartModifySyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StartModifySyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartModifySyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.StartModifySyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartSubscribe(self, request):
        r"""本接口(StartSubscribe)用于启动一个kafka版本的数据订阅实例。只有当订阅任务的状态为checkPass时，才能调用本接口。

        :param request: Request instance for StartSubscribe.
        :type request: :class:`tencentcloud.dts.v20211206.models.StartSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StartSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.StartSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartSyncJob(self, request):
        r"""启动同步任务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCompare(self, request):
        r"""终止一致性校验任务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopMigrateJob(self, request):
        r"""本接口（StopMigrateJob）用于终止数据迁移任务。当任务状态为运行中、准备运行、准备完成、错误、暂停、未知等状态时可调用此接口终止任务。
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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopSyncJob(self, request):
        r"""结束同步任务，操作后可通过查询同步任务信息接口DescribeSyncJobs，获取操作后的状态。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))