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
from tencentcloud.dts.v20180330 import models
from typing import Dict


class DtsClient(AbstractClient):
    _apiVersion = '2018-03-30'
    _endpoint = 'dts.tencentcloudapi.com'
    _service = 'dts'

    async def ActivateSubscribe(
            self,
            request: models.ActivateSubscribeRequest,
            opts: Dict = None,
    ) -> models.ActivateSubscribeResponse:
        """
        本接口用于配置数据订阅，只有在未配置状态的订阅实例才能调用此接口。
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompleteMigrateJob(
            self,
            request: models.CompleteMigrateJobRequest,
            opts: Dict = None,
    ) -> models.CompleteMigrateJobResponse:
        """
        本接口（CompleteMigrateJob）用于完成数据迁移任务。
        选择采用增量迁移方式的任务, 需要在迁移进度进入准备完成阶段后, 调用本接口, 停止迁移增量数据。
        通过DescribeMigrateJobs接口查询到任务的状态为准备完成（status=8）时，此时可以调用本接口完成迁移任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigrateCheckJob(
            self,
            request: models.CreateMigrateCheckJobRequest,
            opts: Dict = None,
    ) -> models.CreateMigrateCheckJobResponse:
        """
        创建校验迁移任务
        在开始迁移前, 必须调用本接口创建校验, 且校验成功后才能开始迁移. 校验的结果可以通过DescribeMigrateCheckJob查看.
        校验成功后,迁移任务若有修改, 则必须重新创建校验并通过后, 才能开始迁移.

        如果是金融区链路, 请使用域名: https://dts.ap-shenzhen-fsi.tencentcloudapi.com
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigrateCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrateCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigrateJob(
            self,
            request: models.CreateMigrateJobRequest,
            opts: Dict = None,
    ) -> models.CreateMigrateJobResponse:
        """
        本接口（CreateMigrateJob）用于创建数据迁移任务。

        如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubscribe(
            self,
            request: models.CreateSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreateSubscribeResponse:
        """
        本接口(CreateSubscribe)用于创建一个数据订阅实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMigrateJob(
            self,
            request: models.DeleteMigrateJobRequest,
            opts: Dict = None,
    ) -> models.DeleteMigrateJobResponse:
        """
        本接口（DeleteMigrationJob）用于删除数据迁移任务。当通过DescribeMigrateJobs接口查询到任务的状态为：检验中（status=3）、运行中（status=7）、准备完成（status=8）、撤销中（status=11）或者完成中（status=12）时，不允许删除任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsyncRequestInfo(
            self,
            request: models.DescribeAsyncRequestInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAsyncRequestInfoResponse:
        """
        本接口（DescribeAsyncRequestInfo）用于查询任务执行结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsyncRequestInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsyncRequestInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrateCheckJob(
            self,
            request: models.DescribeMigrateCheckJobRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrateCheckJobResponse:
        """
        本接口用于创建校验后,获取校验的结果. 能查询到当前校验的状态和进度.
        若通过校验, 则可调用'StartMigrateJob' 开始迁移.
        若未通过校验, 则能查询到校验失败的原因. 请按照报错, 通过'ModifyMigrateJob'修改迁移配置或是调整源/目标实例的相关参数.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrateCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrateCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrateJobs(
            self,
            request: models.DescribeMigrateJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrateJobsResponse:
        """
        查询数据迁移任务.
        如果是金融区链路, 请使用域名: https://dts.ap-shenzhen-fsi.tencentcloudapi.com
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrateJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrateJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribeConf(
            self,
            request: models.DescribeSubscribeConfRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribeConfResponse:
        """
        本接口（DescribeSubscribeConf）用于查询订阅实例配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribeConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribeConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribes(
            self,
            request: models.DescribeSubscribesRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribesResponse:
        """
        本接口(DescribeSubscribes)获取数据订阅实例信息列表，默认分页，每次返回20条
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateSubscribe(
            self,
            request: models.IsolateSubscribeRequest,
            opts: Dict = None,
    ) -> models.IsolateSubscribeResponse:
        """
        本接口（IsolateSubscribe）用于隔离小时计费的订阅实例。调用后，订阅实例将不能使用，同时停止计费。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrateJob(
            self,
            request: models.ModifyMigrateJobRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrateJobResponse:
        """
        本接口（ModifyMigrateJob）用于修改数据迁移任务。
        当迁移任务处于下述状态时，允许调用本接口修改迁移任务：迁移创建中（status=1）、 校验成功(status=4)、校验失败(status=5)、迁移失败(status=10)。但源实例、目标实例类型和目标实例地域不允许修改。

        如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeAutoRenewFlag(
            self,
            request: models.ModifySubscribeAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeAutoRenewFlagResponse:
        """
        修改订阅实例自动续费标识
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeConsumeTime(
            self,
            request: models.ModifySubscribeConsumeTimeRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeConsumeTimeResponse:
        """
        本接口(ModifySubscribeConsumeTime)用于修改数据订阅通道的消费时间点
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeConsumeTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeConsumeTimeResponse
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
        本接口(ModifySubscribeObjects)用于修改数据订阅通道的订阅规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeVipVport(
            self,
            request: models.ModifySubscribeVipVportRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeVipVportResponse:
        """
        本接口(ModifySubscribeVipVport)用于修改数据订阅实例的IP和端口号
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeVipVport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeVipVportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineIsolatedSubscribe(
            self,
            request: models.OfflineIsolatedSubscribeRequest,
            opts: Dict = None,
    ) -> models.OfflineIsolatedSubscribeResponse:
        """
        本接口（OfflineIsolatedSubscribe）用于下线已隔离的数据订阅实例
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineIsolatedSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineIsolatedSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetSubscribe(
            self,
            request: models.ResetSubscribeRequest,
            opts: Dict = None,
    ) -> models.ResetSubscribeResponse:
        """
        本接口(ResetSubscribe)用于重置数据订阅实例，已经激活的数据订阅实例，重置后可以使用ActivateSubscribe接口绑定其他的数据库实例
        """
        
        kwargs = {}
        kwargs["action"] = "ResetSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartMigrateJob(
            self,
            request: models.StartMigrateJobRequest,
            opts: Dict = None,
    ) -> models.StartMigrateJobResponse:
        """
        本接口（StartMigrateJob）用于启动迁移任务。非定时迁移任务会在调用后立即开始迁移，定时任务则会开始倒计时。
        调用此接口前，请务必先使用CreateMigrateCheckJob校验数据迁移任务，并通过DescribeMigrateJobs接口查询到任务状态为校验通过（status=4）时，才能启动数据迁移任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StartMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopMigrateJob(
            self,
            request: models.StopMigrateJobRequest,
            opts: Dict = None,
    ) -> models.StopMigrateJobResponse:
        """
        本接口（StopMigrateJob）用于撤销数据迁移任务。
        在迁移过程中允许调用该接口撤销迁移, 撤销迁移的任务会失败。通过DescribeMigrateJobs接口查询到任务状态为运行中（status=7）或准备完成（status=8）时，才能撤销数据迁移任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StopMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)