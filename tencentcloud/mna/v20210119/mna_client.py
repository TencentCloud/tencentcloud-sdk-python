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
from tencentcloud.mna.v20210119 import models


class MnaClient(AbstractClient):
    _apiVersion = '2021-01-19'
    _endpoint = 'mna.tencentcloudapi.com'
    _service = 'mna'


    def CreateQos(self, request):
        """移动网络发起Qos加速过程

        :param request: Request instance for CreateQos.
        :type request: :class:`tencentcloud.mna.v20210119.models.CreateQosRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.CreateQosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateQos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateQosResponse()
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


    def DeleteQos(self, request):
        """移动网络停止Qos加速过程

        :param request: Request instance for DeleteQos.
        :type request: :class:`tencentcloud.mna.v20210119.models.DeleteQosRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeleteQosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteQos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteQosResponse()
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


    def DescribeQos(self, request):
        """获取Qos加速状态

        :param request: Request instance for DescribeQos.
        :type request: :class:`tencentcloud.mna.v20210119.models.DescribeQosRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DescribeQosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeQos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeQosResponse()
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