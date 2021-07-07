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
from tencentcloud.wss.v20180426 import models


class WssClient(AbstractClient):
    _apiVersion = '2018-04-26'
    _endpoint = 'wss.tencentcloudapi.com'
    _service = 'wss'


    def DeleteCert(self, request):
        """本接口（DeleteCert）用于删除证书。

        :param request: Request instance for DeleteCert.
        :type request: :class:`tencentcloud.wss.v20180426.models.DeleteCertRequest`
        :rtype: :class:`tencentcloud.wss.v20180426.models.DeleteCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCertResponse()
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


    def DescribeCertList(self, request):
        """本接口(DescribeCertList)用于获取证书列表。

        :param request: Request instance for DescribeCertList.
        :type request: :class:`tencentcloud.wss.v20180426.models.DescribeCertListRequest`
        :rtype: :class:`tencentcloud.wss.v20180426.models.DescribeCertListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertListResponse()
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


    def UploadCert(self, request):
        """本接口（UploadCert）用于上传证书。

        :param request: Request instance for UploadCert.
        :type request: :class:`tencentcloud.wss.v20180426.models.UploadCertRequest`
        :rtype: :class:`tencentcloud.wss.v20180426.models.UploadCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadCertResponse()
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