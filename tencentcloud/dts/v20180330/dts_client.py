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
from tencentcloud.dts.v20180330 import models


class DtsClient(AbstractClient):
    _apiVersion = '2018-03-30'
    _endpoint = 'dts.tencentcloudapi.com'
    _service = 'dts'


    def ActivateSubscribe(self, request):
        r"""本接口用于配置数据订阅，只有在未配置状态的订阅实例才能调用此接口。

        :param request: Request instance for ActivateSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.ActivateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ActivateSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompleteMigrateJob(self, request):
        r"""本接口（CompleteMigrateJob）用于完成数据迁移任务。
        选择采用增量迁移方式的任务, 需要在迁移进度进入准备完成阶段后, 调用本接口, 停止迁移增量数据。
        通过DescribeMigrateJobs接口查询到任务的状态为准备完成（status=8）时，此时可以调用本接口完成迁移任务。

        :param request: Request instance for CompleteMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CompleteMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CompleteMigrateJobResponse`

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


    def CreateMigrateCheckJob(self, request):
        r"""创建校验迁移任务
        在开始迁移前, 必须调用本接口创建校验, 且校验成功后才能开始迁移. 校验的结果可以通过DescribeMigrateCheckJob查看.
        校验成功后,迁移任务若有修改, 则必须重新创建校验并通过后, 才能开始迁移.

        如果是金融区链路, 请使用域名: https://dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: Request instance for CreateMigrateCheckJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateMigrateCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateMigrateCheckJobResponse`

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


    def CreateMigrateJob(self, request):
        r"""本接口（CreateMigrateJob）用于创建数据迁移任务。

        如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: Request instance for CreateMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubscribe(self, request):
        r"""本接口(CreateSubscribe)用于创建一个数据订阅实例。

        :param request: Request instance for CreateSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateSubscribeResponse`

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


    def DeleteMigrateJob(self, request):
        r"""本接口（DeleteMigrationJob）用于删除数据迁移任务。当通过DescribeMigrateJobs接口查询到任务的状态为：检验中（status=3）、运行中（status=7）、准备完成（status=8）、撤销中（status=11）或者完成中（status=12）时，不允许删除任务。

        :param request: Request instance for DeleteMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.DeleteMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DeleteMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAsyncRequestInfo(self, request):
        r"""本接口（DescribeAsyncRequestInfo）用于查询任务执行结果

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeAsyncRequestInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsyncRequestInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAsyncRequestInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrateCheckJob(self, request):
        r"""本接口用于创建校验后,获取校验的结果. 能查询到当前校验的状态和进度.
        若通过校验, 则可调用'StartMigrateJob' 开始迁移.
        若未通过校验, 则能查询到校验失败的原因. 请按照报错, 通过'ModifyMigrateJob'修改迁移配置或是调整源/目标实例的相关参数.

        :param request: Request instance for DescribeMigrateCheckJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrateCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrateCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrateJobs(self, request):
        r"""查询数据迁移任务.
        如果是金融区链路, 请使用域名: https://dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: Request instance for DescribeMigrateJobs.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrateJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrateJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubscribeConf(self, request):
        r"""本接口（DescribeSubscribeConf）用于查询订阅实例配置

        :param request: Request instance for DescribeSubscribeConf.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribeConfRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribeConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubscribeConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubscribeConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubscribes(self, request):
        r"""本接口(DescribeSubscribes)获取数据订阅实例信息列表，默认分页，每次返回20条

        :param request: Request instance for DescribeSubscribes.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribesRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubscribes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubscribesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateSubscribe(self, request):
        r"""本接口（IsolateSubscribe）用于隔离小时计费的订阅实例。调用后，订阅实例将不能使用，同时停止计费。

        :param request: Request instance for IsolateSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.IsolateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.IsolateSubscribeResponse`

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


    def ModifyMigrateJob(self, request):
        r"""本接口（ModifyMigrateJob）用于修改数据迁移任务。
        当迁移任务处于下述状态时，允许调用本接口修改迁移任务：迁移创建中（status=1）、 校验成功(status=4)、校验失败(status=5)、迁移失败(status=10)。但源实例、目标实例类型和目标实例地域不允许修改。

        如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: Request instance for ModifyMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifyMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifyMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubscribeAutoRenewFlag(self, request):
        r"""修改订阅实例自动续费标识

        :param request: Request instance for ModifySubscribeAutoRenewFlag.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeAutoRenewFlagResponse`

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


    def ModifySubscribeConsumeTime(self, request):
        r"""本接口(ModifySubscribeConsumeTime)用于修改数据订阅通道的消费时间点

        :param request: Request instance for ModifySubscribeConsumeTime.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeConsumeTimeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeConsumeTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubscribeConsumeTime", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubscribeConsumeTimeResponse()
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
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeNameRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeNameResponse`

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
        r"""本接口(ModifySubscribeObjects)用于修改数据订阅通道的订阅规则

        :param request: Request instance for ModifySubscribeObjects.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeObjectsRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeObjectsResponse`

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


    def ModifySubscribeVipVport(self, request):
        r"""本接口(ModifySubscribeVipVport)用于修改数据订阅实例的IP和端口号

        :param request: Request instance for ModifySubscribeVipVport.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeVipVportRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeVipVportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubscribeVipVport", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubscribeVipVportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OfflineIsolatedSubscribe(self, request):
        r"""本接口（OfflineIsolatedSubscribe）用于下线已隔离的数据订阅实例

        :param request: Request instance for OfflineIsolatedSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.OfflineIsolatedSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.OfflineIsolatedSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineIsolatedSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.OfflineIsolatedSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetSubscribe(self, request):
        r"""本接口(ResetSubscribe)用于重置数据订阅实例，已经激活的数据订阅实例，重置后可以使用ActivateSubscribe接口绑定其他的数据库实例

        :param request: Request instance for ResetSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.ResetSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ResetSubscribeResponse`

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


    def StartMigrateJob(self, request):
        r"""本接口（StartMigrateJob）用于启动迁移任务。非定时迁移任务会在调用后立即开始迁移，定时任务则会开始倒计时。
        调用此接口前，请务必先使用CreateMigrateCheckJob校验数据迁移任务，并通过DescribeMigrateJobs接口查询到任务状态为校验通过（status=4）时，才能启动数据迁移任务。

        :param request: Request instance for StartMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.StartMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.StartMigrateJobResponse`

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


    def StopMigrateJob(self, request):
        r"""本接口（StopMigrateJob）用于撤销数据迁移任务。
        在迁移过程中允许调用该接口撤销迁移, 撤销迁移的任务会失败。通过DescribeMigrateJobs接口查询到任务状态为运行中（status=7）或准备完成（status=8）时，才能撤销数据迁移任务。

        :param request: Request instance for StopMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.StopMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.StopMigrateJobResponse`

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