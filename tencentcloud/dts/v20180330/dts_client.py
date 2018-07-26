# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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
        """完成数据迁移任务.
        选择采用增量迁移方式的任务, 需要在迁移进度进入准备完成阶段后, 调用本接口, 停止迁移增量数据.
        只有当正在迁移的任务, 进入了准备完成阶段, 才能调用本接口完成迁移.

        :param request: 调用CompleteMigrateJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMigrateCheckJob(self, request):
        """创建校验迁移任务
        在开始迁移前, 必须调用本接口创建校验, 且校验成功后才能开始迁移. 校验的结果可以通过DescribeMigrateCheckJob查看.
        校验成功后,迁移任务若有修改, 则必须重新创建校验并通过后, 才能开始迁移.

        :param request: 调用CreateMigrateCheckJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMigrateJob(self, request):
        """本接口用于创建数据迁移任务。

        如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: 调用CreateMigrateJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSyncCheckJob(self, request):
        """在开始灾备同步前, 必须调用本接口创建校验, 且校验成功后才能开始同步数据. 校验的结果可以通过DescribeSyncCheckJob查看.
        校验成功或失败后均可再修改, 修改后必须重新校验并通过后, 才能开始同步.

        :param request: 调用CreateSyncCheckJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSyncJob(self, request):
        """本接口(CreateSyncJob)用于创建灾备同步任务。

        :param request: 调用CreateSyncJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMigrateJob(self, request):
        """删除数据迁移任务. 正在校验和正在迁移的任务不允许删除

        :param request: 调用DeleteMigrateJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSyncJob(self, request):
        """删除灾备同步任务 （运行中的同步任务不能删除）。

        :param request: 调用DeleteSyncJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMigrateCheckJob(self, request):
        """本接口用于创建校验后,获取校验的结果. 能查询到当前校验的状态和进度.
        若通过校验, 则可调用'StartMigrateJob' 开始迁移.
        若未通过校验, 则能查询到校验失败的原因. 请按照报错, 通过'ModifyMigrateJob'修改迁移配置或是调整源/目标实例的相关参数.

        :param request: 调用DescribeMigrateCheckJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMigrateJobs(self, request):
        """查询数据迁移任务.
        如果是金融区链路, 请使用域名: https://dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: 调用DescribeMigrateJobs所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSyncCheckJob(self, request):
        """本接口用于创建灾备同步校验任务后,获取校验的结果. 能查询到当前校验的状态和进度.
        若通过校验, 则可调用'StartSyncJob' 开始迁移.
        若未通过校验, 则会返回校验失败的原因. 可通过'ModifySyncJob'修改配置重新发起校验.

        :param request: 调用DescribeSyncCheckJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSyncJobs(self, request):
        """查询在迁移平台发起的灾备同步任务

        :param request: 调用DescribeSyncJobs所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMigrateJob(self, request):
        """修改数据迁移任务.
        当迁移任务处于下述状态时, 允许调用本接口: 迁移创建中, 创建完成, 校验成功, 校验失败, 迁移失败.
        源实例和目标实例类型不允许修改, 目标实例地域不允许修改。

        如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: 调用ModifyMigrateJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySyncJob(self, request):
        """修改灾备同步任务.
        当同步任务处于下述状态时, 允许调用本接口: 同步任务创建中, 创建完成, 校验成功, 校验失败.
        源实例和目标实例信息不允许修改，可以修改任务名、需要同步的库表。

        :param request: 调用ModifySyncJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartMigrateJob(self, request):
        """非定时任务会在调用后立即开始迁移，定时任务则会开始倒计时。
        调用此接口前，请务必先校验数据迁移任务通过。

        :param request: 调用StartMigrateJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartSyncJob(self, request):
        """创建的灾备同步任务在校验成功后，可以调用该接口开始同步

        :param request: 调用StartSyncJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopMigrateJob(self, request):
        """撤销数据迁移任务.
        在迁移过程中允许调用该接口撤销迁移, 撤销迁移的任务会失败.

        :param request: 调用StopMigrateJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SwitchDrToMaster(self, request):
        """将灾备升级为主实例，停止从原来所属主实例的同步，断开主备关系。

        :param request: 调用SwitchDrToMaster所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)