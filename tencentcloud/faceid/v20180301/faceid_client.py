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
from tencentcloud.faceid.v20180301 import models


class FaceidClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'faceid.tencentcloudapi.com'


    def DetectAuth(self, request):
        """实名核身鉴权。用于获取一次核身流程的BizToken。如果是微信平台，会同时返回一个URL，用作微信平台的跳转。

        :param request: 调用DetectAuth所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.DetectAuthRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.DetectAuthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectAuth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectAuthResponse()
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


    def GetDetectInfo(self, request):
        """获取实名核身结果信息

        :param request: 调用GetDetectInfo所需参数的结构体。
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDetectInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDetectInfoResponse()
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