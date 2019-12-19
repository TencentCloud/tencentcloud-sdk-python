# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.dts.v20180330 import models


class DtsClient(AbstractClient):
    _apiVersion = '2018-03-30'
    _endpoint = 'dts.tencentcloudapi.com'


    def CompleteMigrateJob(self, request):
        """本接口（CompleteMigrateJob）用于完成数据迁移任务。
        选择采用增量迁移方式的任务, 需要在迁移进度进入准备完成阶段后, 调用本接口, 停止迁移增量数据。
        通过DescribeMigrateJobs接口查询到任务的状态为准备完成（status=8）时，此时可以调用本接口完成迁移任务。

        :param request: Request instance for CompleteMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CompleteMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CompleteMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompleteMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompleteMigrateJobResponse()
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


    def CreateMigrateCheckJob(self, request):
        """创建校验迁移任务
        在开始迁移前, 必须调用本接口创建校验, 且校验成功后才能开始迁移. 校验的结果可以通过DescribeMigrateCheckJob查看.
        校验成功后,迁移任务若有修改, 则必须重新创建校验并通过后, 才能开始迁移.

        :param request: Request instance for CreateMigrateCheckJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateMigrateCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateMigrateCheckJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMigrateCheckJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMigrateCheckJobResponse()
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


    def CreateMigrateJob(self, request):
        """本接口（CreateMigrateJob）用于创建数据迁移任务。

        如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: Request instance for CreateMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMigrateJobResponse()
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


    def CreateSyncCheckJob(self, request):
        """在调用 StartSyncJob 接口启动灾备同步前, 必须调用本接口创建校验, 且校验成功后才能开始同步数据. 校验的结果可以通过 DescribeSyncCheckJob 查看.
        校验成功后才能启动同步.

        :param request: Request instance for CreateSyncCheckJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateSyncCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateSyncCheckJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSyncCheckJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSyncCheckJobResponse()
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


    def CreateSyncJob(self, request):
        """本接口(CreateSyncJob)用于创建灾备同步任务。
        创建同步任务后，可以通过 CreateSyncCheckJob 接口发起校验任务。校验成功后才可以通过 StartSyncJob 接口启动同步任务。

        :param request: Request instance for CreateSyncJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateSyncJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSyncJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSyncJobResponse()
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


    def DeleteMigrateJob(self, request):
        """本接口（DeleteMigrationJob）用于删除数据迁移任务。当通过DescribeMigrateJobs接口查询到任务的状态为：检验中（status=3）、运行中（status=7）、准备完成（status=8）、撤销中（status=11）或者完成中（status=12）时，不允许删除任务。

        :param request: Request instance for DeleteMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.DeleteMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DeleteMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMigrateJobResponse()
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


    def DeleteSyncJob(self, request):
        """删除灾备同步任务 （运行中的同步任务不能删除）。

        :param request: Request instance for DeleteSyncJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.DeleteSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DeleteSyncJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSyncJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSyncJobResponse()
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


    def DescribeMigrateCheckJob(self, request):
        """本接口用于创建校验后,获取校验的结果. 能查询到当前校验的状态和进度.
        若通过校验, 则可调用'StartMigrateJob' 开始迁移.
        若未通过校验, 则能查询到校验失败的原因. 请按照报错, 通过'ModifyMigrateJob'修改迁移配置或是调整源/目标实例的相关参数.

        :param request: Request instance for DescribeMigrateCheckJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateCheckJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrateCheckJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrateCheckJobResponse()
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


    def DescribeMigrateJobs(self, request):
        """查询数据迁移任务.
        如果是金融区链路, 请使用域名: https://dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: Request instance for DescribeMigrateJobs.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrateJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrateJobsResponse()
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


    def DescribeSyncCheckJob(self, request):
        """本接口用于在通过 CreateSyncCheckJob 接口创建灾备同步校验任务后，获取校验的结果。能查询到当前校验的状态和进度。
        若通过校验, 则可调用 StartSyncJob 启动同步任务。
        若未通过校验, 则会返回校验失败的原因。 可通过 ModifySyncJob 修改配置，然后再次发起校验。
        校验任务需要大概约30秒，当返回的 Status 不为 finished 时表示尚未校验完成，需要轮询该接口。
        如果 Status=finished 且 CheckFlag=1 时表示校验成功。
        如果 Status=finished 且 CheckFlag !=1 时表示校验失败。

        :param request: Request instance for DescribeSyncCheckJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeSyncCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeSyncCheckJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSyncCheckJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSyncCheckJobResponse()
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


    def DescribeSyncJobs(self, request):
        """查询在迁移平台发起的灾备同步任务

        :param request: Request instance for DescribeSyncJobs.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeSyncJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeSyncJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSyncJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSyncJobsResponse()
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


    def ModifyMigrateJob(self, request):
        """本接口（ModifyMigrateJob）用于修改数据迁移任务。
        当迁移任务处于下述状态时，允许调用本接口修改迁移任务：迁移创建中（status=1）、 校验成功(status=4)、校验失败(status=5)、迁移失败(status=10)。但源实例、目标实例类型和目标实例地域不允许修改。

        如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: Request instance for ModifyMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifyMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifyMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMigrateJobResponse()
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


    def ModifySyncJob(self, request):
        """修改灾备同步任务.
        当同步任务处于下述状态时, 允许调用本接口: 同步任务创建中, 创建完成, 校验成功, 校验失败.
        源实例和目标实例信息不允许修改，可以修改任务名、需要同步的库表。

        :param request: Request instance for ModifySyncJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySyncJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySyncJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySyncJobResponse()
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


    def StartMigrateJob(self, request):
        """本接口（StartMigrationJob）用于启动迁移任务。非定时迁移任务会在调用后立即开始迁移，定时任务则会开始倒计时。
        调用此接口前，请务必先使用CreateMigrateCheckJob校验数据迁移任务，并通过DescribeMigrateJobs接口查询到任务状态为校验通过（status=4）时，才能启动数据迁移任务。

        :param request: Request instance for StartMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.StartMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.StartMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMigrateJobResponse()
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


    def StartSyncJob(self, request):
        """创建的灾备同步任务在通过 CreateSyncCheckJob 和 DescribeSyncCheckJob 确定校验成功后，可以调用该接口启动同步

        :param request: Request instance for StartSyncJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.StartSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.StartSyncJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartSyncJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartSyncJobResponse()
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


    def StopMigrateJob(self, request):
        """本接口（StopMigrateJob）用于撤销数据迁移任务。
        在迁移过程中允许调用该接口撤销迁移, 撤销迁移的任务会失败。通过DescribeMigrateJobs接口查询到任务状态为运行中（status=7）或准备完成（status=8）时，才能撤销数据迁移任务。

        :param request: Request instance for StopMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.StopMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.StopMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopMigrateJobResponse()
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


    def SwitchDrToMaster(self, request):
        """将灾备升级为主实例，停止从原来所属主实例的同步，断开主备关系。

        :param request: Request instance for SwitchDrToMaster.
        :type request: :class:`tencentcloud.dts.v20180330.models.SwitchDrToMasterRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.SwitchDrToMasterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwitchDrToMaster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchDrToMasterResponse()
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