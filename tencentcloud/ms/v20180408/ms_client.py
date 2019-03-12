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
from tencentcloud.ms.v20180408 import models


class MsClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'ms.tencentcloudapi.com'


    def CreateBindInstance(self, request):
        """将应用和资源进行绑定

        :param request: 调用CreateBindInstance所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateBindInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateBindInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBindInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBindInstanceResponse()
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


    def CreateCosSecKeyInstance(self, request):
        """获取云COS文件存储临时密钥，密钥仅限于临时上传文件，有访问限制和时效性。

        :param request: 调用CreateCosSecKeyInstance所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateCosSecKeyInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateCosSecKeyInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCosSecKeyInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCosSecKeyInstanceResponse()
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


    def CreateResourceInstances(self, request):
        """用户可以使用该接口自建资源，只支持白名单用户

        :param request: 调用CreateResourceInstances所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateResourceInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateResourceInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateResourceInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateResourceInstancesResponse()
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


    def CreateScanInstances(self, request):
        """用户通过该接口批量提交应用进行应用扫描，扫描后需通过DescribeScanResults接口查询扫描结果

        :param request: 调用CreateScanInstances所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateScanInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateScanInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScanInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScanInstancesResponse()
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


    def CreateShieldInstance(self, request):
        """用户通过该接口提交应用进行应用加固，加固后需通过DescribeShieldResult接口查询加固结果

        :param request: 调用CreateShieldInstance所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateShieldInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateShieldInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateShieldInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateShieldInstanceResponse()
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


    def CreateShieldPlanInstance(self, request):
        """对资源进行策略新增

        :param request: 调用CreateShieldPlanInstance所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateShieldPlanInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateShieldPlanInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateShieldPlanInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateShieldPlanInstanceResponse()
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


    def DeleteScanInstances(self, request):
        """删除一个或者多个app扫描信息

        :param request: 调用DeleteScanInstances所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.DeleteScanInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DeleteScanInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScanInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScanInstancesResponse()
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


    def DeleteShieldInstances(self, request):
        """删除一个或者多个app加固信息

        :param request: 调用DeleteShieldInstances所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.DeleteShieldInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DeleteShieldInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteShieldInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteShieldInstancesResponse()
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


    def DescribeResourceInstances(self, request):
        """获取某个用户的所有资源信息

        :param request: 调用DescribeResourceInstances所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeResourceInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeResourceInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceInstancesResponse()
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


    def DescribeScanInstances(self, request):
        """本接口用于查看app列表。
        可以通过指定任务唯一标识ItemId来查询指定app的详细信息，或通过设定过滤器来查询满足过滤条件的app的详细信息。 指定偏移(Offset)和限制(Limit)来选择结果中的一部分，默认返回满足条件的前20个app信息。

        :param request: 调用DescribeScanInstances所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeScanInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeScanInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScanInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanInstancesResponse()
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


    def DescribeScanResults(self, request):
        """用户通过CreateScanInstances接口提交应用进行风险批量扫描后，用此接口批量获取风险详细信息,包含漏洞信息，广告信息，插件信息和病毒信息

        :param request: 调用DescribeScanResults所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeScanResultsRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeScanResultsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScanResults", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanResultsResponse()
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


    def DescribeShieldInstances(self, request):
        """本接口用于查看app列表。
        可以通过指定任务唯一标识ItemId来查询指定app的详细信息，或通过设定过滤器来查询满足过滤条件的app的详细信息。 指定偏移(Offset)和限制(Limit)来选择结果中的一部分，默认返回满足条件的前20个app信息。

        :param request: 调用DescribeShieldInstances所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeShieldInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeShieldInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShieldInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShieldInstancesResponse()
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


    def DescribeShieldPlanInstance(self, request):
        """查询加固策略

        :param request: 调用DescribeShieldPlanInstance所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeShieldPlanInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeShieldPlanInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShieldPlanInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShieldPlanInstanceResponse()
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


    def DescribeShieldResult(self, request):
        """通过唯一标识获取加固的结果

        :param request: 调用DescribeShieldResult所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeShieldResultRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeShieldResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShieldResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShieldResultResponse()
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


    def DescribeUserBaseInfoInstance(self, request):
        """获取用户基础信息

        :param request: 调用DescribeUserBaseInfoInstance所需参数的结构体。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeUserBaseInfoInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeUserBaseInfoInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserBaseInfoInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserBaseInfoInstanceResponse()
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