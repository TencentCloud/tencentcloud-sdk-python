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
from tencentcloud.tsw.v20210412 import models


class TswClient(AbstractClient):
    _apiVersion = '2021-04-12'
    _endpoint = 'tsw.tencentcloudapi.com'
    _service = 'tsw'


    def DescribeComponentAlertObject(self, request):
        """获取告警对象-组件告警

        :param request: Request instance for DescribeComponentAlertObject.
        :type request: :class:`tencentcloud.tsw.v20210412.models.DescribeComponentAlertObjectRequest`
        :rtype: :class:`tencentcloud.tsw.v20210412.models.DescribeComponentAlertObjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComponentAlertObject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComponentAlertObjectResponse()
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


    def DescribeServiceAlertObject(self, request):
        """获取告警对象-服务告警表

        :param request: Request instance for DescribeServiceAlertObject.
        :type request: :class:`tencentcloud.tsw.v20210412.models.DescribeServiceAlertObjectRequest`
        :rtype: :class:`tencentcloud.tsw.v20210412.models.DescribeServiceAlertObjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceAlertObject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceAlertObjectResponse()
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


    def DescribeToken(self, request):
        """查询token

        :param request: Request instance for DescribeToken.
        :type request: :class:`tencentcloud.tsw.v20210412.models.DescribeTokenRequest`
        :rtype: :class:`tencentcloud.tsw.v20210412.models.DescribeTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTokenResponse()
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