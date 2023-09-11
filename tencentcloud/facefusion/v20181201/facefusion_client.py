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
from tencentcloud.facefusion.v20181201 import models


class FacefusionClient(AbstractClient):
    _apiVersion = '2018-12-01'
    _endpoint = 'facefusion.tencentcloudapi.com'
    _service = 'facefusion'


    def DescribeMaterialList(self, request):
        """通常通过腾讯云人脸融合的控制台可以查看到素材相关的参数数据，可以满足使用。本接口返回活动的素材数据，包括素材状态等。用于用户通过Api查看素材相关数据，方便使用。

        :param request: Request instance for DescribeMaterialList.
        :type request: :class:`tencentcloud.facefusion.v20181201.models.DescribeMaterialListRequest`
        :rtype: :class:`tencentcloud.facefusion.v20181201.models.DescribeMaterialListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaterialList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaterialListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FaceFusion(self, request):
        """本接口用于人脸融合，用户上传人脸图片，获取与模板融合后的人脸图片。未发布的活动请求频率限制为1次/秒，已发布的活动请求频率限制50次/秒。如有需要提高活动的请求频率限制，请在控制台中申请。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for FaceFusion.
        :type request: :class:`tencentcloud.facefusion.v20181201.models.FaceFusionRequest`
        :rtype: :class:`tencentcloud.facefusion.v20181201.models.FaceFusionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FaceFusion", params, headers=headers)
            response = json.loads(body)
            model = models.FaceFusionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FaceFusionLite(self, request):
        """接口不再使用

        人脸融合活动专用版，不推荐使用。人脸融合接口建议使用[人脸融合](https://cloud.tencent.com/document/product/670/31061)或[选脸融合](https://cloud.tencent.com/document/product/670/37736)接口

        :param request: Request instance for FaceFusionLite.
        :type request: :class:`tencentcloud.facefusion.v20181201.models.FaceFusionLiteRequest`
        :rtype: :class:`tencentcloud.facefusion.v20181201.models.FaceFusionLiteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FaceFusionLite", params, headers=headers)
            response = json.loads(body)
            model = models.FaceFusionLiteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FuseFace(self, request):
        """本接口用于单脸、多脸融合，用户上传人脸图片，获取与模板融合后的人脸图片。查看 <a href="https://cloud.tencent.com/document/product/670/38247" target="_blank">选脸融合接入指引</a>。

        未发布的活动请求频率限制为1次/秒，已发布的活动请求频率限制50次/秒。如有需要提高活动的请求频率限制，请在控制台中申请。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for FuseFace.
        :type request: :class:`tencentcloud.facefusion.v20181201.models.FuseFaceRequest`
        :rtype: :class:`tencentcloud.facefusion.v20181201.models.FuseFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FuseFace", params, headers=headers)
            response = json.loads(body)
            model = models.FuseFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))