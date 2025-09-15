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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.fmu.v20191213 import models


class FmuClient(AbstractClient):
    _apiVersion = '2019-12-13'
    _endpoint = 'fmu.tencentcloudapi.com'
    _service = 'fmu'


    def BeautifyPic(self, request):
        r"""用户上传一张人脸图片（最多能处理一张图片中最大的五张人脸信息），精准定位五官，实现美肤、亮肤、祛痘等美颜功能。

        :param request: Request instance for BeautifyPic.
        :type request: :class:`tencentcloud.fmu.v20191213.models.BeautifyPicRequest`
        :rtype: :class:`tencentcloud.fmu.v20191213.models.BeautifyPicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BeautifyPic", params, headers=headers)
            response = json.loads(body)
            model = models.BeautifyPicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModel(self, request):
        r"""在使用LUT素材的modelid实现试唇色前，您需要先上传 LUT 格式的cube文件注册唇色ID。查看 [LUT文件的使用说明](https://cloud.tencent.com/document/product/1172/41701)。

        注：您也可以直接使用 [试唇色接口](https://cloud.tencent.com/document/product/1172/40706)，通过输入RGBA模型数值的方式指定唇色，更简单易用。

        :param request: Request instance for CreateModel.
        :type request: :class:`tencentcloud.fmu.v20191213.models.CreateModelRequest`
        :rtype: :class:`tencentcloud.fmu.v20191213.models.CreateModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModel(self, request):
        r"""删除已注册的唇色素材。

        :param request: Request instance for DeleteModel.
        :type request: :class:`tencentcloud.fmu.v20191213.models.DeleteModelRequest`
        :rtype: :class:`tencentcloud.fmu.v20191213.models.DeleteModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetModelList(self, request):
        r"""查询已注册的唇色素材。

        :param request: Request instance for GetModelList.
        :type request: :class:`tencentcloud.fmu.v20191213.models.GetModelListRequest`
        :rtype: :class:`tencentcloud.fmu.v20191213.models.GetModelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetModelList", params, headers=headers)
            response = json.loads(body)
            model = models.GetModelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StyleImage(self, request):
        r"""上传一张照片，输出滤镜处理后的图片。

        :param request: Request instance for StyleImage.
        :type request: :class:`tencentcloud.fmu.v20191213.models.StyleImageRequest`
        :rtype: :class:`tencentcloud.fmu.v20191213.models.StyleImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StyleImage", params, headers=headers)
            response = json.loads(body)
            model = models.StyleImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StyleImagePro(self, request):
        r"""上传一张照片，输出滤镜处理后的图片。

        :param request: Request instance for StyleImagePro.
        :type request: :class:`tencentcloud.fmu.v20191213.models.StyleImageProRequest`
        :rtype: :class:`tencentcloud.fmu.v20191213.models.StyleImageProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StyleImagePro", params, headers=headers)
            response = json.loads(body)
            model = models.StyleImageProResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TryLipstickPic(self, request):
        r"""对图片中的人脸嘴唇进行着色，最多支持同时对一张图中的3张人脸进行试唇色。

        您可以通过事先注册在腾讯云的唇色素材（LUT文件）改变图片中的人脸唇色，也可以输入RGBA模型数值。

        为了更好的效果，建议您使用事先注册在腾讯云的唇色素材（LUT文件）。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for TryLipstickPic.
        :type request: :class:`tencentcloud.fmu.v20191213.models.TryLipstickPicRequest`
        :rtype: :class:`tencentcloud.fmu.v20191213.models.TryLipstickPicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TryLipstickPic", params, headers=headers)
            response = json.loads(body)
            model = models.TryLipstickPicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))