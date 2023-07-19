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
from tencentcloud.ape.v20200513 import models


class ApeClient(AbstractClient):
    _apiVersion = '2020-05-13'
    _endpoint = 'ape.tencentcloudapi.com'
    _service = 'ape'


    def BatchDescribeOrderCertificate(self, request):
        """批量获取授权书下载地址

        :param request: Request instance for BatchDescribeOrderCertificate.
        :type request: :class:`tencentcloud.ape.v20200513.models.BatchDescribeOrderCertificateRequest`
        :rtype: :class:`tencentcloud.ape.v20200513.models.BatchDescribeOrderCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDescribeOrderCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDescribeOrderCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDescribeOrderImage(self, request):
        """批量获取图片下载地址

        :param request: Request instance for BatchDescribeOrderImage.
        :type request: :class:`tencentcloud.ape.v20200513.models.BatchDescribeOrderImageRequest`
        :rtype: :class:`tencentcloud.ape.v20200513.models.BatchDescribeOrderImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDescribeOrderImage", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDescribeOrderImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrderAndDownloads(self, request):
        """核销图片，获取原图URL地址

        :param request: Request instance for CreateOrderAndDownloads.
        :type request: :class:`tencentcloud.ape.v20200513.models.CreateOrderAndDownloadsRequest`
        :rtype: :class:`tencentcloud.ape.v20200513.models.CreateOrderAndDownloadsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrderAndDownloads", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrderAndDownloadsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrderAndPay(self, request):
        """购买一张图片并且支付

        :param request: Request instance for CreateOrderAndPay.
        :type request: :class:`tencentcloud.ape.v20200513.models.CreateOrderAndPayRequest`
        :rtype: :class:`tencentcloud.ape.v20200513.models.CreateOrderAndPayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrderAndPay", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrderAndPayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuthUsers(self, request):
        """分页查询授权人列表

        :param request: Request instance for DescribeAuthUsers.
        :type request: :class:`tencentcloud.ape.v20200513.models.DescribeAuthUsersRequest`
        :rtype: :class:`tencentcloud.ape.v20200513.models.DescribeAuthUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuthUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuthUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDownloadInfos(self, request):
        """获取用户图片下载记录

        :param request: Request instance for DescribeDownloadInfos.
        :type request: :class:`tencentcloud.ape.v20200513.models.DescribeDownloadInfosRequest`
        :rtype: :class:`tencentcloud.ape.v20200513.models.DescribeDownloadInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDownloadInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDownloadInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImage(self, request):
        """根据ID查询一张图片的详细信息

        :param request: Request instance for DescribeImage.
        :type request: :class:`tencentcloud.ape.v20200513.models.DescribeImageRequest`
        :rtype: :class:`tencentcloud.ape.v20200513.models.DescribeImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImages(self, request):
        """根据关键字搜索图片列表

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.ape.v20200513.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.ape.v20200513.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))