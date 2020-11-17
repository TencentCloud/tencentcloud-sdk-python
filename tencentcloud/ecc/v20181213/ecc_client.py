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
from tencentcloud.ecc.v20181213 import models


class EccClient(AbstractClient):
    _apiVersion = '2018-12-13'
    _endpoint = 'ecc.tencentcloudapi.com'
    _service = 'ecc'


    def CorrectMultiImage(self, request):
        """https://ecc.tencentcloudapi.com/?Action=CorrectMultiImage
        多图像识别批改接口

        :param request: Request instance for CorrectMultiImage.
        :type request: :class:`tencentcloud.ecc.v20181213.models.CorrectMultiImageRequest`
        :rtype: :class:`tencentcloud.ecc.v20181213.models.CorrectMultiImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CorrectMultiImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CorrectMultiImageResponse()
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


    def DescribeTask(self, request):
        """异步任务结果查询接口

        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.ecc.v20181213.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.ecc.v20181213.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResponse()
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


    def ECC(self, request):
        """接口请求域名： ecc.tencentcloudapi.com
        纯文本英语作文批改

        :param request: Request instance for ECC.
        :type request: :class:`tencentcloud.ecc.v20181213.models.ECCRequest`
        :rtype: :class:`tencentcloud.ecc.v20181213.models.ECCResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ECC", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ECCResponse()
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


    def EHOCR(self, request):
        """https://ecc.tencentcloudapi.com/?Action=EHOCR
        图像识别批改接口

        :param request: Request instance for EHOCR.
        :type request: :class:`tencentcloud.ecc.v20181213.models.EHOCRRequest`
        :rtype: :class:`tencentcloud.ecc.v20181213.models.EHOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EHOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EHOCRResponse()
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