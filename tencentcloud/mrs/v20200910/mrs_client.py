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
from tencentcloud.mrs.v20200910 import models


class MrsClient(AbstractClient):
    _apiVersion = '2020-09-10'
    _endpoint = 'mrs.tencentcloudapi.com'
    _service = 'mrs'


    def ImageToClass(self, request):
        """图片分类

        :param request: Request instance for ImageToClass.
        :type request: :class:`tencentcloud.mrs.v20200910.models.ImageToClassRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.ImageToClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageToClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageToClassResponse()
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


    def ImageToObject(self, request):
        """图片转结构化对象

        :param request: Request instance for ImageToObject.
        :type request: :class:`tencentcloud.mrs.v20200910.models.ImageToObjectRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.ImageToObjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageToObject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageToObjectResponse()
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


    def TextToClass(self, request):
        """文本分类

        :param request: Request instance for TextToClass.
        :type request: :class:`tencentcloud.mrs.v20200910.models.TextToClassRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.TextToClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextToClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextToClassResponse()
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


    def TextToObject(self, request):
        """文本转结构化对象

        :param request: Request instance for TextToObject.
        :type request: :class:`tencentcloud.mrs.v20200910.models.TextToObjectRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.TextToObjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextToObject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextToObjectResponse()
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