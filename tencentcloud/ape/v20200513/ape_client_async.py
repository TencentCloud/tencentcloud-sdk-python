# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.ape.v20200513 import models
from typing import Dict


class ApeClient(AbstractClient):
    _apiVersion = '2020-05-13'
    _endpoint = 'ape.tencentcloudapi.com'
    _service = 'ape'

    async def BatchDescribeOrderCertificate(
            self,
            request: models.BatchDescribeOrderCertificateRequest,
            opts: Dict = None,
    ) -> models.BatchDescribeOrderCertificateResponse:
        """
        批量获取授权书下载地址
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDescribeOrderCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDescribeOrderCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDescribeOrderImage(
            self,
            request: models.BatchDescribeOrderImageRequest,
            opts: Dict = None,
    ) -> models.BatchDescribeOrderImageResponse:
        """
        批量获取图片下载地址
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDescribeOrderImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDescribeOrderImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrderAndDownloads(
            self,
            request: models.CreateOrderAndDownloadsRequest,
            opts: Dict = None,
    ) -> models.CreateOrderAndDownloadsResponse:
        """
        核销图片，获取原图URL地址
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrderAndDownloads"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrderAndDownloadsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrderAndPay(
            self,
            request: models.CreateOrderAndPayRequest,
            opts: Dict = None,
    ) -> models.CreateOrderAndPayResponse:
        """
        购买一张图片并且支付
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrderAndPay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrderAndPayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuthUsers(
            self,
            request: models.DescribeAuthUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeAuthUsersResponse:
        """
        分页查询授权人列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuthUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuthUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDownloadInfos(
            self,
            request: models.DescribeDownloadInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeDownloadInfosResponse:
        """
        获取用户图片下载记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDownloadInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDownloadInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImage(
            self,
            request: models.DescribeImageRequest,
            opts: Dict = None,
    ) -> models.DescribeImageResponse:
        """
        根据ID查询一张图片的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImages(
            self,
            request: models.DescribeImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeImagesResponse:
        """
        根据关键字搜索图片列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)