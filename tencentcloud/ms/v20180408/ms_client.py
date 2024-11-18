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
from tencentcloud.ms.v20180408 import models


class MsClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'ms.tencentcloudapi.com'
    _service = 'ms'


    def CancelEncryptTask(self, request):
        """该接口供渠道合作应用加固使用，接口调用有白名单用户限制，取消渠道合作加固中的任务

        :param request: Request instance for CancelEncryptTask.
        :type request: :class:`tencentcloud.ms.v20180408.models.CancelEncryptTaskRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CancelEncryptTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelEncryptTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelEncryptTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBindInstance(self, request):
        """将应用和资源进行绑定。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）

        :param request: Request instance for CreateBindInstance.
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateBindInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateBindInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBindInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBindInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCosSecKeyInstance(self, request):
        """获取云COS文件存储临时密钥，密钥仅限于临时上传文件，有访问限制和时效性，请保管好临时密钥。

        :param request: Request instance for CreateCosSecKeyInstance.
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateCosSecKeyInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateCosSecKeyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosSecKeyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCosSecKeyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEncryptInstance(self, request):
        """该接口供渠道合作应用加固使用，接口调用有白名单用户限制，用于创建加固任务。

        :param request: Request instance for CreateEncryptInstance.
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateEncryptInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateEncryptInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEncryptInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEncryptInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrderInstance(self, request):
        """该接口供渠道合作应用加固使用，接口调用有白名单用户限制。
        订单类型有：免费试用、按年收费、按次收费。
        应用加固支持的平台类型有：android加固 、ios源码混淆 、sdk加固、applet小程序加固

        :param request: Request instance for CreateOrderInstance.
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateOrderInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateOrderInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrderInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrderInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourceInstances(self, request):
        """不再使用

        用户可以使用该接口自建资源，只支持白名单用户

        :param request: Request instance for CreateResourceInstances.
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateResourceInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateResourceInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourceInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateShieldInstance(self, request):
        """用户通过该接口提交应用进行应用加固，加固后需通过DescribeShieldResult接口查询加固结果。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）

        :param request: Request instance for CreateShieldInstance.
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateShieldInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateShieldInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateShieldInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateShieldInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateShieldPlanInstance(self, request):
        """对资源进行策略新增。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）

        :param request: Request instance for CreateShieldPlanInstance.
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateShieldPlanInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateShieldPlanInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateShieldPlanInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateShieldPlanInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShieldInstances(self, request):
        """删除一个或者多个app加固信息。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）

        :param request: Request instance for DeleteShieldInstances.
        :type request: :class:`tencentcloud.ms.v20180408.models.DeleteShieldInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DeleteShieldInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShieldInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShieldInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApkDetectionResult(self, request):
        """该接口采用同步模式请求腾讯APK云检测服务，即时返回检测数据，需要用户用轮询的方式调用本接口来进行样本送检并获取检测结果(每隔60s发送一次请求，传相同的参数，重试30次)，一般情况下0.5h内会出检测结果，最长时间是3h。当Result为ok并且ResultList数组非空有值时，代表检测完毕，若长时间获取不到检测结果，请联系客服。

        :param request: Request instance for DescribeApkDetectionResult.
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeApkDetectionResultRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeApkDetectionResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApkDetectionResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApkDetectionResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEncryptInstances(self, request):
        """该接口供渠道合作应用加固使用，接口调用有白名单用户限制，用于查询加固任务，入参中的条件过滤字段均为精准匹配。支持功能点: 1. 多任务分页查询  2.根据任务Id唯一值查询单记录

        :param request: Request instance for DescribeEncryptInstances.
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeEncryptInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeEncryptInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEncryptInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEncryptInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEncryptPlan(self, request):
        """该接口供渠道合作应用加固使用，接口调用有白名单用户限制。入参中的条件过滤字段均为精准匹配。

        :param request: Request instance for DescribeEncryptPlan.
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeEncryptPlanRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeEncryptPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEncryptPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEncryptPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrderInstances(self, request):
        """该接口供渠道合作应用加固使用，接口调用有白名单用户限制。 接口返回的结果为：创建订单后，订单审批状态信息，以及与订单关联的资源状态等信息，入参中的条件过滤字段均为精准匹配.
        接口功能点：
        1.支持多订单分页查询；
        2.支持唯一订单号精准匹配查询；
        3.支持唯一资源号精准匹配查询；

        :param request: Request instance for DescribeOrderInstances.
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeOrderInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeOrderInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrderInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrderInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceInstances(self, request):
        """获取某个用户的所有资源信息。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）

        :param request: Request instance for DescribeResourceInstances.
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeResourceInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeResourceInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShieldInstances(self, request):
        """本接口用于查看app列表。
        可以通过指定任务唯一标识ItemId来查询指定app的详细信息，或通过设定过滤器来查询满足过滤条件的app的详细信息。 指定偏移(Offset)和限制(Limit)来选择结果中的一部分，默认返回满足条件的前20个app信息。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）

        :param request: Request instance for DescribeShieldInstances.
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeShieldInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeShieldInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShieldInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShieldInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShieldPlanInstance(self, request):
        """查询加固策略。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）

        :param request: Request instance for DescribeShieldPlanInstance.
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeShieldPlanInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeShieldPlanInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShieldPlanInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShieldPlanInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShieldResult(self, request):
        """通过唯一标识获取加固的结果。（注意：根据国家互联网用户实名制相关要求，使用该产品前，需先完成实名认证。）

        :param request: Request instance for DescribeShieldResult.
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeShieldResultRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeShieldResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShieldResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShieldResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUrlDetectionResult(self, request):
        """移动安全-网址检测服务

        :param request: Request instance for DescribeUrlDetectionResult.
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeUrlDetectionResultRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeUrlDetectionResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUrlDetectionResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUrlDetectionResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserBaseInfoInstance(self, request):
        """获取用户基础信息

        :param request: Request instance for DescribeUserBaseInfoInstance.
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeUserBaseInfoInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeUserBaseInfoInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserBaseInfoInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserBaseInfoInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyResourceInstances(self, request):
        """渠道合作资源销毁
        安卓应用加固-按年收费资源销毁，其他类型暂不支持

        :param request: Request instance for DestroyResourceInstances.
        :type request: :class:`tencentcloud.ms.v20180408.models.DestroyResourceInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DestroyResourceInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyResourceInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyResourceInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RequestLocalTask(self, request):
        """client任务请求

        :param request: Request instance for RequestLocalTask.
        :type request: :class:`tencentcloud.ms.v20180408.models.RequestLocalTaskRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.RequestLocalTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RequestLocalTask", params, headers=headers)
            response = json.loads(body)
            model = models.RequestLocalTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateClientState(self, request):
        """更新client状态，需要白名单

        :param request: Request instance for UpdateClientState.
        :type request: :class:`tencentcloud.ms.v20180408.models.UpdateClientStateRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.UpdateClientStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateClientState", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateClientStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateLocalTaskResult(self, request):
        """更新本地任务执行结果

        :param request: Request instance for UpdateLocalTaskResult.
        :type request: :class:`tencentcloud.ms.v20180408.models.UpdateLocalTaskResultRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.UpdateLocalTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateLocalTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateLocalTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))