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
from tencentcloud.iotvideo.v20211125 import models


class IotvideoClient(AbstractClient):
    _apiVersion = '2021-11-25'
    _endpoint = 'iotvideo.tencentcloudapi.com'
    _service = 'iotvideo'


    def CallDeviceActionAsync(self, request):
        """异步调用设备行为

        :param request: Request instance for CallDeviceActionAsync.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CallDeviceActionAsyncRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CallDeviceActionAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CallDeviceActionAsync", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CallDeviceActionAsyncResponse()
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


    def CallDeviceActionSync(self, request):
        """同步调用设备行为

        :param request: Request instance for CallDeviceActionSync.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CallDeviceActionSyncRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CallDeviceActionSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CallDeviceActionSync", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CallDeviceActionSyncResponse()
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


    def CreateProduct(self, request):
        """创建产品

        :param request: Request instance for CreateProduct.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.CreateProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.CreateProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProduct", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProductResponse()
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


    def DescribeDeviceDataStats(self, request):
        """查询设备数据统计

        :param request: Request instance for DescribeDeviceDataStats.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceDataStatsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeDeviceDataStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceDataStats", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceDataStatsResponse()
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


    def DescribeMessageDataStats(self, request):
        """查询设备消息数量统计

        :param request: Request instance for DescribeMessageDataStats.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.DescribeMessageDataStatsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.DescribeMessageDataStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageDataStats", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMessageDataStatsResponse()
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


    def GenSingleDeviceSignatureOfPublic(self, request):
        """获取设备的绑定签名

        :param request: Request instance for GenSingleDeviceSignatureOfPublic.
        :type request: :class:`tencentcloud.iotvideo.v20211125.models.GenSingleDeviceSignatureOfPublicRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20211125.models.GenSingleDeviceSignatureOfPublicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenSingleDeviceSignatureOfPublic", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenSingleDeviceSignatureOfPublicResponse()
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