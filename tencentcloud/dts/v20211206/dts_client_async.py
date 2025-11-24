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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.dts.v20211206 import models
from typing import Dict


class DtsClient(AbstractClient):
    _apiVersion = '2021-12-06'
    _endpoint = 'dts.tencentcloudapi.com'
    _service = 'dts'

    async def CompleteMigrateJob(
            self,
            request: models.CompleteMigrateJobRequest,
            opts: Dict = None,
    ) -> models.CompleteMigrateJobResponse:
        """
        本接口（CompleteMigrateJob）用于完成数据迁移任务。
        选择采用增量迁移方式的任务, 需要在迁移进度进入准备完成阶段后, 调用本接口, 停止迁移增量数据。
        通过DescribeMigrationJobs接口查询到任务的状态为准备完成（Status="readyComplete"）时，此时可以调用本接口完成迁移任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfigureSubscribeJob(
            self,
            request: models.ConfigureSubscribeJobRequest,
            opts: Dict = None,
    ) -> models.ConfigureSubscribeJobResponse:
        """
        本接口(ConfigureSubscribeJob)用于配置数据订阅实例。
        """
        
        kwargs = {}
        kwargs["action"] = "ConfigureSubscribeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfigureSubscribeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfigureSyncJob(
            self,
            request: models.ConfigureSyncJobRequest,
            opts: Dict = None,
    ) -> models.ConfigureSyncJobResponse:
        """
        配置一个同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "ConfigureSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfigureSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ContinueMigrateJob(
            self,
            request: models.ContinueMigrateJobRequest,
            opts: Dict = None,
    ) -> models.ContinueMigrateJobResponse:
        """
        恢复一个暂停中的迁移任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ContinueMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ContinueMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ContinueSyncJob(
            self,
            request: models.ContinueSyncJobRequest,
            opts: Dict = None,
    ) -> models.ContinueSyncJobResponse:
        """
        恢复处于已暂停状态的数据同步任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ContinueSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ContinueSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCheckSyncJob(
            self,
            request: models.CreateCheckSyncJobRequest,
            opts: Dict = None,
    ) -> models.CreateCheckSyncJobResponse:
        """
        校验同步任务，检查必要参数和周边配置。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCheckSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCheckSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCompareTask(
            self,
            request: models.CreateCompareTaskRequest,
            opts: Dict = None,
    ) -> models.CreateCompareTaskResponse:
        """
        本接口用于创建数据对比任务，创建成功后会返回数据对比任务 ID，形如：dts-8yv4w2i1-cmp-37skmii9，创建成功后可通过StartCompare启动一致性校验任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCompareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCompareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsumerGroup(
            self,
            request: models.CreateConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.CreateConsumerGroupResponse:
        """
        为订阅实例创建消费者组。
        只有状态为运行中的实例支持创建消费组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigrateCheckJob(
            self,
            request: models.CreateMigrateCheckJobRequest,
            opts: Dict = None,
    ) -> models.CreateMigrateCheckJobResponse:
        """
        创建校验迁移任务，
        在开始迁移前, 必须调用本接口创建校验迁移任务, 且校验成功后才能开始迁移. 校验的结果可以通过DescribeMigrationCheckJob查看，
        校验成功后,迁移任务若有修改, 则必须重新校验并通过后, 才能开始迁移
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigrateCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrateCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigrationService(
            self,
            request: models.CreateMigrationServiceRequest,
            opts: Dict = None,
    ) -> models.CreateMigrationServiceResponse:
        """
        购买迁移任务。购买成功后会返回随机生成的迁移任务id列表，也可以通过查询迁移任务任务列表接口`DescribeMigrationJobs`看到购买成功的实例Id。注意，一旦购买成功后源及目标数据库类型，源及目标实例地域不可修改。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigrationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModifyCheckSyncJob(
            self,
            request: models.CreateModifyCheckSyncJobRequest,
            opts: Dict = None,
    ) -> models.CreateModifyCheckSyncJobResponse:
        """
        在修改同步任务的配置后、通过该接口校验当前任务是否支持修改对象操作
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModifyCheckSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModifyCheckSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubscribe(
            self,
            request: models.CreateSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreateSubscribeResponse:
        """
        本接口(CreateSubscribe)用于创建一个数据订阅任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubscribeCheckJob(
            self,
            request: models.CreateSubscribeCheckJobRequest,
            opts: Dict = None,
    ) -> models.CreateSubscribeCheckJobResponse:
        """
        本接口(CreateSubscribeCheckJob)用于创建一个订阅校验任务。任务必须已经成功调用ConfigureSubscribeJob接口配置了所有的必要信息才能启动校验。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubscribeCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubscribeCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSyncCompareTask(
            self,
            request: models.CreateSyncCompareTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSyncCompareTaskResponse:
        """
        本接口用于创建数据对比任务，创建成功后会返回数据对比任务 ID，形如：sync-8yv4w2i1-cmp-37skmii9，创建成功后可通过StartSyncCompare启动一致性校验任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSyncCompareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSyncCompareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSyncJob(
            self,
            request: models.CreateSyncJobRequest,
            opts: Dict = None,
    ) -> models.CreateSyncJobResponse:
        """
        创建一个同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCompareTask(
            self,
            request: models.DeleteCompareTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteCompareTaskResponse:
        """
        删除一致性校验任务。当一致性校验任务状态为success、failed、canceled 时可以执行此操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCompareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCompareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsumerGroup(
            self,
            request: models.DeleteConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteConsumerGroupResponse:
        """
        本接口(DeleteConsumerGroup)用于删除一个订阅任务的消费组。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSyncCompareTask(
            self,
            request: models.DeleteSyncCompareTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteSyncCompareTaskResponse:
        """
        删除一致性校验任务。当一致性校验任务状态为success、failed、canceled 时可以执行此操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSyncCompareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSyncCompareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckSyncJobResult(
            self,
            request: models.DescribeCheckSyncJobResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckSyncJobResultResponse:
        """
        查询同步校验任务结果，检查必要参数和周边配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckSyncJobResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckSyncJobResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompareReport(
            self,
            request: models.DescribeCompareReportRequest,
            opts: Dict = None,
    ) -> models.DescribeCompareReportResponse:
        """
        查询一致性校验任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompareReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompareReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompareTasks(
            self,
            request: models.DescribeCompareTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeCompareTasksResponse:
        """
        查询一致性校验任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompareTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompareTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerGroups(
            self,
            request: models.DescribeConsumerGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerGroupsResponse:
        """
        本接口(DescribeConsumerGroups)用于获取订阅实例配置的消费者组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrateDBInstances(
            self,
            request: models.DescribeMigrateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrateDBInstancesResponse:
        """
        本接口用于查询支持迁移的云数据库实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationCheckJob(
            self,
            request: models.DescribeMigrationCheckJobRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationCheckJobResponse:
        """
        本接口用于创建校验后,获取校验的结果. 能查询到当前校验的状态和进度.
        若通过校验, 则可调用'StartMigrateJob' 开始迁移.
        若未通过校验, 则能查询到校验失败的原因. 请按照报错, 通过'ModifyMigrationJob'修改迁移配置或是调整源/目标实例的相关参数.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationDetail(
            self,
            request: models.DescribeMigrationDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationDetailResponse:
        """
        查询某个迁移任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationJobs(
            self,
            request: models.DescribeMigrationJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationJobsResponse:
        """
        查询数据迁移任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModifyCheckSyncJobResult(
            self,
            request: models.DescribeModifyCheckSyncJobResultRequest,
            opts: Dict = None,
    ) -> models.DescribeModifyCheckSyncJobResultResponse:
        """
        在创建修改对象的校验任务后、通过该接口查看校验任务的结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModifyCheckSyncJobResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModifyCheckSyncJobResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOffsetByTime(
            self,
            request: models.DescribeOffsetByTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeOffsetByTimeResponse:
        """
        本接口(DescribeOffsetByTime)查询KafkaTopic中指定时间前最近的offset。
        接口输出的offset是离这个时间最近的offset。
        如果输入时间比当前时间晚的多，相当于输出的就是最新的offset；
        如果输入时间比当前时间早的多，相当于输出的就是最老的offset；
        如果输入空，默认0时间，也就是查询最老的offset。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOffsetByTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOffsetByTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribeCheckJob(
            self,
            request: models.DescribeSubscribeCheckJobRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribeCheckJobResponse:
        """
        本接口(DescribeSubscribeCheckJob)用于查询订阅校验任务结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribeCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribeCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribeDetail(
            self,
            request: models.DescribeSubscribeDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribeDetailResponse:
        """
        本接口(DescribeSubscribeDetail)获取数据订阅实例的配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribeDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribeDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribeJobs(
            self,
            request: models.DescribeSubscribeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribeJobsResponse:
        """
        本接口(DescribeSubscribes)获取数据订阅实例信息列表，默认分页，每次返回20条
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribeReturnable(
            self,
            request: models.DescribeSubscribeReturnableRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribeReturnableResponse:
        """
        本接口(DescribeSubscribeReturnable)用于查询订阅任务是否可以销毁和退货。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribeReturnable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribeReturnableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSyncCompareReport(
            self,
            request: models.DescribeSyncCompareReportRequest,
            opts: Dict = None,
    ) -> models.DescribeSyncCompareReportResponse:
        """
        查询一致性校验任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSyncCompareReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSyncCompareReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSyncCompareTasks(
            self,
            request: models.DescribeSyncCompareTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeSyncCompareTasksResponse:
        """
        查询一致性校验任务列表。通过该接口可查看改任务下所有一致性校验任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSyncCompareTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSyncCompareTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSyncJobs(
            self,
            request: models.DescribeSyncJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeSyncJobsResponse:
        """
        查询同步任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSyncJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSyncJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyIsolatedSubscribe(
            self,
            request: models.DestroyIsolatedSubscribeRequest,
            opts: Dict = None,
    ) -> models.DestroyIsolatedSubscribeResponse:
        """
        本接口（DestroyIsolatedSubscribe）用于下线已隔离的数据订阅实例
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyIsolatedSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyIsolatedSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyMigrateJob(
            self,
            request: models.DestroyMigrateJobRequest,
            opts: Dict = None,
    ) -> models.DestroyMigrateJobResponse:
        """
        下线数据迁移任务。计费任务必须先调用隔离(IsolateMigrateJob)接口，且只有是**已隔离**状态下，才能调用此接口销毁任务。对于不计费任务，调用隔离(IsolateMigrateJob)接口删除任务操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroySyncJob(
            self,
            request: models.DestroySyncJobRequest,
            opts: Dict = None,
    ) -> models.DestroySyncJobResponse:
        """
        下线同步任务，任务在已隔离状态下可以通过此操作进行任务下线，即彻底删除任务。下线操作后可通过查询同步任务信息接口DescribeSyncJobs获取任务列表查看状态，此操作成功后无法看到此任务表示下线成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroySyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroySyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateMigrateJob(
            self,
            request: models.IsolateMigrateJobRequest,
            opts: Dict = None,
    ) -> models.IsolateMigrateJobResponse:
        """
        隔离退还数据迁移服务。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。对于计费任务，在任务隔离后可进行解除隔离(RecoverMigrateJob)操作或直接进行下线销毁(DestroyMigrateJob)操作。对于不计费任务，调用此接口会直接销毁任务，无法进行恢复操作。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateSubscribe(
            self,
            request: models.IsolateSubscribeRequest,
            opts: Dict = None,
    ) -> models.IsolateSubscribeResponse:
        """
        本接口（IsolateSubscribe）用于隔离订阅任务。调用后，订阅任务将不能使用。按量计费的任务会停止计费，包年包月的任务会自动退费
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateSyncJob(
            self,
            request: models.IsolateSyncJobRequest,
            opts: Dict = None,
    ) -> models.IsolateSyncJobResponse:
        """
        隔离同步任务，隔离后可通过查询同步任务信息接口DescribeSyncJobs获取隔离后状态。在任务隔离后可进行解除隔离(RecoverSyncJob)操作或直接进行下线(DestroySyncJob)操作。对于不计费任务，调用此接口后会直接删除任务，无法进行恢复操作。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCompareTask(
            self,
            request: models.ModifyCompareTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyCompareTaskResponse:
        """
        修改一致性校验任务，在任务创建后启动之前，可修改一致性校验参数
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCompareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCompareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCompareTaskName(
            self,
            request: models.ModifyCompareTaskNameRequest,
            opts: Dict = None,
    ) -> models.ModifyCompareTaskNameResponse:
        """
        修改一致性校验任务名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCompareTaskName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCompareTaskNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsumerGroupDescription(
            self,
            request: models.ModifyConsumerGroupDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyConsumerGroupDescriptionResponse:
        """
        本接口(ModifyConsumerGroupDescription)用于修改指定订阅消费组备注。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsumerGroupDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsumerGroupDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsumerGroupPassword(
            self,
            request: models.ModifyConsumerGroupPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyConsumerGroupPasswordResponse:
        """
        本接口(ModifyConsumerGroupPassword)用于修改指定订阅消费组密码。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsumerGroupPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsumerGroupPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrateJobSpec(
            self,
            request: models.ModifyMigrateJobSpecRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrateJobSpecResponse:
        """
        调整实例规格，此接口只支持按量计费任务的调整，且仅在计费或者待计费状态下支持修改。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrateJobSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrateJobSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrateName(
            self,
            request: models.ModifyMigrateNameRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrateNameResponse:
        """
        修改迁移任务名
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrateName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrateNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrateRateLimit(
            self,
            request: models.ModifyMigrateRateLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrateRateLimitResponse:
        """
        用户在发现迁移任务对用户的数据库的负载影响较大时、可通过该接口限制任务的传输速率；此操作仅在任务运行中可执行。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrateRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrateRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrateRuntimeAttribute(
            self,
            request: models.ModifyMigrateRuntimeAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrateRuntimeAttributeResponse:
        """
        修改任务运行时属性，此接口不同于配置类接口，不会进行状态机判断。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrateRuntimeAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrateRuntimeAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrationJob(
            self,
            request: models.ModifyMigrationJobRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrationJobResponse:
        """
        配置迁移服务，配置成功后可通过`CreateMigrateCheckJob` 创建迁移校验任务接口发起校验任务，只有校验通过才能启动迁移任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrationJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrationJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeAutoRenewFlag(
            self,
            request: models.ModifySubscribeAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeAutoRenewFlagResponse:
        """
        修改订阅实例自动续费标识。只有包年包月的任务修改才有意义，按量计费任务修改后无影响。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeName(
            self,
            request: models.ModifySubscribeNameRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeNameResponse:
        """
        本接口(ModifySubscribeName)用于修改数据订阅实例的名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeObjects(
            self,
            request: models.ModifySubscribeObjectsRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeObjectsResponse:
        """
        本接口(ModifySubscribeObjects)用于修改数据订阅对象和kafka分区规则，如果是mongo订阅，还可以修改输出聚合规则。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySyncCompareTask(
            self,
            request: models.ModifySyncCompareTaskRequest,
            opts: Dict = None,
    ) -> models.ModifySyncCompareTaskResponse:
        """
        修改一致性校验任务，在任务创建后启动之前，可修改一致性校验参数
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySyncCompareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySyncCompareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySyncCompareTaskName(
            self,
            request: models.ModifySyncCompareTaskNameRequest,
            opts: Dict = None,
    ) -> models.ModifySyncCompareTaskNameResponse:
        """
        修改同步一致性校验任务名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySyncCompareTaskName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySyncCompareTaskNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySyncJobConfig(
            self,
            request: models.ModifySyncJobConfigRequest,
            opts: Dict = None,
    ) -> models.ModifySyncJobConfigResponse:
        """
        该接口支持在同步任务启动后修改任务的配置
        修改同步配置的完整流程：修改同步任务配置->创建修改同步任务配置的校验任务->查询修改配置的校验任务的结果->启动修改配置任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySyncJobConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySyncJobConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySyncRateLimit(
            self,
            request: models.ModifySyncRateLimitRequest,
            opts: Dict = None,
    ) -> models.ModifySyncRateLimitResponse:
        """
        用户在发现同步任务对用户的数据库的负载影响较大时、可通过该接口限制任务的传输速率
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySyncRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySyncRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseMigrateJob(
            self,
            request: models.PauseMigrateJobRequest,
            opts: Dict = None,
    ) -> models.PauseMigrateJobResponse:
        """
        暂停一个迁移任务。
        """
        
        kwargs = {}
        kwargs["action"] = "PauseMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseSyncJob(
            self,
            request: models.PauseSyncJobRequest,
            opts: Dict = None,
    ) -> models.PauseSyncJobResponse:
        """
        暂停处于同步中的数据同步任务。
        """
        
        kwargs = {}
        kwargs["action"] = "PauseSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverMigrateJob(
            self,
            request: models.RecoverMigrateJobRequest,
            opts: Dict = None,
    ) -> models.RecoverMigrateJobResponse:
        """
        解除隔离数据迁移任务，用户手动发起隔离后的手动解隔离，只有任务状态为已隔离(手动操作)状态下才能触发此操作。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverSyncJob(
            self,
            request: models.RecoverSyncJobRequest,
            opts: Dict = None,
    ) -> models.RecoverSyncJobResponse:
        """
        解除隔离同步任务，任务在已隔离状态下可调用该接口解除隔离状态任务，同时可通过查询同步任务信息接口DescribeSyncJobs，获取操作后状态。注意，此接口只支持按量计费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetConsumerGroupOffset(
            self,
            request: models.ResetConsumerGroupOffsetRequest,
            opts: Dict = None,
    ) -> models.ResetConsumerGroupOffsetResponse:
        """
        本接口(ResetConsumerGroupOffset)用于重置订阅消费组的offset。调用DescribeConsumerGroups接口查询消费组状态，只有消费组状态为 Dead 或 Empty 才可以执行重置该操作。否则重置不会生效，接口也不会报错。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetConsumerGroupOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetConsumerGroupOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetSubscribe(
            self,
            request: models.ResetSubscribeRequest,
            opts: Dict = None,
    ) -> models.ResetSubscribeResponse:
        """
        本接口(ResetSubscribe)用于重置订阅实例，重置后，可以重新配置订阅任务。
        可以调用 [DescribeSubscribeDetail](https://cloud.tencent.com/document/product/571/102944) 查询订阅信息判断是否置成功。当SubsStatus变为notStarted时，表示重置成功。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetSyncJob(
            self,
            request: models.ResetSyncJobRequest,
            opts: Dict = None,
    ) -> models.ResetSyncJobResponse:
        """
        重置已经结束的同步任务，重置后可以重新配置启动任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeSyncJob(
            self,
            request: models.ResizeSyncJobRequest,
            opts: Dict = None,
    ) -> models.ResizeSyncJobResponse:
        """
        调整同步任务规格，此接口只支持按量计费任务的调整，调用此接口后不会立即生效，后台调整时间大概为3~5分钟。调用此接口后可通过查询同步任务信息接口DescribeSyncJobs，获取变配后的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeMigrateJob(
            self,
            request: models.ResumeMigrateJobRequest,
            opts: Dict = None,
    ) -> models.ResumeMigrateJobResponse:
        """
        重试数据迁移任务，针对异常情况可进行重试，对于redis在失败时也可重试。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeSubscribe(
            self,
            request: models.ResumeSubscribeRequest,
            opts: Dict = None,
    ) -> models.ResumeSubscribeResponse:
        """
        本接口(ResumeSubscribe) 用于恢复报错的订阅任务。当订阅任务的状态为error时，可通过本接口尝试对任务进行恢复。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeSyncJob(
            self,
            request: models.ResumeSyncJobRequest,
            opts: Dict = None,
    ) -> models.ResumeSyncJobResponse:
        """
        重试同步任务，部分可恢复报错情况下，可通过该接口重试同步任务，可通过查询同步任务信息接口DescribeSyncJobs，获取操作后状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SkipCheckItem(
            self,
            request: models.SkipCheckItemRequest,
            opts: Dict = None,
    ) -> models.SkipCheckItemResponse:
        """
        本接口用于校验检查项不通过后，可进行跳过此校验项操作，后端将不再校验该项。任何校验步骤都是不应该跳过的，通过校验是能正确执行的前置条件。支持跳过的产品及链路的校验项可 [参考文档](https://cloud.tencent.com/document/product/571/61639)。
        """
        
        kwargs = {}
        kwargs["action"] = "SkipCheckItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SkipCheckItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SkipSyncCheckItem(
            self,
            request: models.SkipSyncCheckItemRequest,
            opts: Dict = None,
    ) -> models.SkipSyncCheckItemResponse:
        """
        本接口用于校验检查项不通过后，可进行跳过此校验项操作，后端将不再校验该项。任何校验步骤都是不应该跳过的，通过校验是能正确执行的前置条件。支持跳过的产品及链路的校验项可 [参考文档](https://cloud.tencent.com/document/product/571/61639)。
        """
        
        kwargs = {}
        kwargs["action"] = "SkipSyncCheckItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SkipSyncCheckItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCompare(
            self,
            request: models.StartCompareRequest,
            opts: Dict = None,
    ) -> models.StartCompareResponse:
        """
        启动一致性校验任务，启动之前需要先通过接口 [CreateCompareTask](https://cloud.tencent.com/document/product/571/82093) 创建一致性校验任务，启动后可通过接口 [DescribeCompareTasks](https://cloud.tencent.com/document/product/571/82088) 查询一致性校验任务列表来获得启动后的状态
        """
        
        kwargs = {}
        kwargs["action"] = "StartCompare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartCompareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartMigrateJob(
            self,
            request: models.StartMigrateJobRequest,
            opts: Dict = None,
    ) -> models.StartMigrateJobResponse:
        """
        本接口（StartMigrateJob）用于启动迁移任务。调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "StartMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartModifySyncJob(
            self,
            request: models.StartModifySyncJobRequest,
            opts: Dict = None,
    ) -> models.StartModifySyncJobResponse:
        """
        在查询修改对象的校验任务的结果中的status为success后、通过该接口开始修改配置流程
        """
        
        kwargs = {}
        kwargs["action"] = "StartModifySyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartModifySyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartSubscribe(
            self,
            request: models.StartSubscribeRequest,
            opts: Dict = None,
    ) -> models.StartSubscribeResponse:
        """
        本接口(StartSubscribe)用于启动一个kafka版本的数据订阅实例。只有当订阅任务的状态为checkPass时，才能调用本接口。
        """
        
        kwargs = {}
        kwargs["action"] = "StartSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartSyncCompare(
            self,
            request: models.StartSyncCompareRequest,
            opts: Dict = None,
    ) -> models.StartSyncCompareResponse:
        """
        启动一致性校验任务，启动之前需要先通过接口`CreateSyncCompareTask` 创建一致性校验任务，启动后可通过接口`DescribeSyncCompareTasks` 查询一致性校验任务列表来获得启动后的状态
        """
        
        kwargs = {}
        kwargs["action"] = "StartSyncCompare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartSyncCompareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartSyncJob(
            self,
            request: models.StartSyncJobRequest,
            opts: Dict = None,
    ) -> models.StartSyncJobResponse:
        """
        启动同步任务
        """
        
        kwargs = {}
        kwargs["action"] = "StartSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCompare(
            self,
            request: models.StopCompareRequest,
            opts: Dict = None,
    ) -> models.StopCompareResponse:
        """
        终止一致性校验任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopCompare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCompareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopMigrateJob(
            self,
            request: models.StopMigrateJobRequest,
            opts: Dict = None,
    ) -> models.StopMigrateJobResponse:
        """
        本接口（StopMigrateJob）用于终止数据迁移任务。当任务状态为运行中、准备运行、准备完成、错误、暂停、未知等状态时可调用此接口终止任务。
        调用此接口后可通过查询迁移服务列表接口`DescribeMigrationJobs`来查询当前任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "StopMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopSyncCompare(
            self,
            request: models.StopSyncCompareRequest,
            opts: Dict = None,
    ) -> models.StopSyncCompareResponse:
        """
        终止一致性校验任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopSyncCompare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopSyncCompareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopSyncJob(
            self,
            request: models.StopSyncJobRequest,
            opts: Dict = None,
    ) -> models.StopSyncJobResponse:
        """
        结束同步任务，操作后可通过查询同步任务信息接口DescribeSyncJobs，获取操作后的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "StopSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)