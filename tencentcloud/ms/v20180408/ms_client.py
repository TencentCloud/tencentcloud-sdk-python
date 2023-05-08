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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateResourceInstances(self, request):
        """用户可以使用该接口自建资源，只支持白名单用户

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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)