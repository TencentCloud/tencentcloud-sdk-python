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
from tencentcloud.bma.v20221115 import models


class BmaClient(AbstractClient):
    _apiVersion = '2022-11-15'
    _endpoint = 'bma.tencentcloudapi.com'
    _service = 'bma'


    def CreateBPFakeAPP(self, request):
        """仿冒应用举报

        :param request: Request instance for CreateBPFakeAPP.
        :type request: :class:`tencentcloud.bma.v20221115.models.CreateBPFakeAPPRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.CreateBPFakeAPPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPFakeAPP", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPFakeAPPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBPFakeAPPList(self, request):
        """批量仿冒应用举报

        :param request: Request instance for CreateBPFakeAPPList.
        :type request: :class:`tencentcloud.bma.v20221115.models.CreateBPFakeAPPListRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.CreateBPFakeAPPListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPFakeAPPList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPFakeAPPListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBPFakeURL(self, request):
        """仿冒网址举报

        :param request: Request instance for CreateBPFakeURL.
        :type request: :class:`tencentcloud.bma.v20221115.models.CreateBPFakeURLRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.CreateBPFakeURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPFakeURL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPFakeURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBPFakeURLs(self, request):
        """批量仿冒网址举报

        :param request: Request instance for CreateBPFakeURLs.
        :type request: :class:`tencentcloud.bma.v20221115.models.CreateBPFakeURLsRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.CreateBPFakeURLsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPFakeURLs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPFakeURLsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)