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


    def CreateBPBrand(self, request):
        """添加品牌

        :param request: Request instance for CreateBPBrand.
        :type request: :class:`tencentcloud.bma.v20221115.models.CreateBPBrandRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.CreateBPBrandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPBrand", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPBrandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBPWhiteList(self, request):
        """添加白名单

        :param request: Request instance for CreateBPWhiteList.
        :type request: :class:`tencentcloud.bma.v20221115.models.CreateBPWhiteListRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.CreateBPWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBPWhiteList(self, request):
        """删除白名单

        :param request: Request instance for DeleteBPWhiteList.
        :type request: :class:`tencentcloud.bma.v20221115.models.DeleteBPWhiteListRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.DeleteBPWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBPWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBPWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBPBrands(self, request):
        """查询品牌列表

        :param request: Request instance for DescribeBPBrands.
        :type request: :class:`tencentcloud.bma.v20221115.models.DescribeBPBrandsRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.DescribeBPBrandsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBPBrands", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBPBrandsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBPFakeAPPList(self, request):
        """查询仿冒应用列表

        :param request: Request instance for DescribeBPFakeAPPList.
        :type request: :class:`tencentcloud.bma.v20221115.models.DescribeBPFakeAPPListRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.DescribeBPFakeAPPListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBPFakeAPPList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBPFakeAPPListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBPFakeURLs(self, request):
        """查询仿冒网址列表

        :param request: Request instance for DescribeBPFakeURLs.
        :type request: :class:`tencentcloud.bma.v20221115.models.DescribeBPFakeURLsRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.DescribeBPFakeURLsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBPFakeURLs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBPFakeURLsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBPWhiteLists(self, request):
        """查询白名单列表

        :param request: Request instance for DescribeBPWhiteLists.
        :type request: :class:`tencentcloud.bma.v20221115.models.DescribeBPWhiteListsRequest`
        :rtype: :class:`tencentcloud.bma.v20221115.models.DescribeBPWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBPWhiteLists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBPWhiteListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))