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
from tencentcloud.fmu.v20191213 import models
from typing import Dict


class FmuClient(AbstractClient):
    _apiVersion = '2019-12-13'
    _endpoint = 'fmu.tencentcloudapi.com'
    _service = 'fmu'

    async def BeautifyPic(
            self,
            request: models.BeautifyPicRequest,
            opts: Dict = None,
    ) -> models.BeautifyPicResponse:
        """
        用户上传一张人脸图片（最多能处理一张图片中最大的五张人脸信息），精准定位五官，实现美肤、亮肤、祛痘等美颜功能。
        """
        
        kwargs = {}
        kwargs["action"] = "BeautifyPic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BeautifyPicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModel(
            self,
            request: models.CreateModelRequest,
            opts: Dict = None,
    ) -> models.CreateModelResponse:
        """
        在使用LUT素材的modelid实现试唇色前，您需要先上传 LUT 格式的cube文件注册唇色ID。查看 [LUT文件的使用说明](https://cloud.tencent.com/document/product/1172/41701)。

        注：您也可以直接使用 [试唇色接口](https://cloud.tencent.com/document/product/1172/40706)，通过输入RGBA模型数值的方式指定唇色，更简单易用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteModel(
            self,
            request: models.DeleteModelRequest,
            opts: Dict = None,
    ) -> models.DeleteModelResponse:
        """
        删除已注册的唇色素材。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetModelList(
            self,
            request: models.GetModelListRequest,
            opts: Dict = None,
    ) -> models.GetModelListResponse:
        """
        查询已注册的唇色素材。
        """
        
        kwargs = {}
        kwargs["action"] = "GetModelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetModelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StyleImage(
            self,
            request: models.StyleImageRequest,
            opts: Dict = None,
    ) -> models.StyleImageResponse:
        """
        上传一张照片，输出滤镜处理后的图片。
        """
        
        kwargs = {}
        kwargs["action"] = "StyleImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StyleImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StyleImagePro(
            self,
            request: models.StyleImageProRequest,
            opts: Dict = None,
    ) -> models.StyleImageProResponse:
        """
        上传一张照片，输出滤镜处理后的图片。
        """
        
        kwargs = {}
        kwargs["action"] = "StyleImagePro"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StyleImageProResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TryLipstickPic(
            self,
            request: models.TryLipstickPicRequest,
            opts: Dict = None,
    ) -> models.TryLipstickPicResponse:
        """
        对图片中的人脸嘴唇进行着色，最多支持同时对一张图中的3张人脸进行试唇色。

        您可以通过事先注册在腾讯云的唇色素材（LUT文件）改变图片中的人脸唇色，也可以输入RGBA模型数值。

        为了更好的效果，建议您使用事先注册在腾讯云的唇色素材（LUT文件）。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        """
        
        kwargs = {}
        kwargs["action"] = "TryLipstickPic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TryLipstickPicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)