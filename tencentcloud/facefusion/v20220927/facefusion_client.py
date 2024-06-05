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
from tencentcloud.facefusion.v20220927 import models


class FacefusionClient(AbstractClient):
    _apiVersion = '2022-09-27'
    _endpoint = 'facefusion.tencentcloudapi.com'
    _service = 'facefusion'


    def DescribeMaterialList(self, request):
        """通常通过腾讯云人脸融合的控制台可以查看到素材相关的参数数据，可以满足使用。本接口返回活动的素材数据，包括素材状态等。用于用户通过Api查看素材相关数据，方便使用。

        :param request: Request instance for DescribeMaterialList.
        :type request: :class:`tencentcloud.facefusion.v20220927.models.DescribeMaterialListRequest`
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.DescribeMaterialListResponse`

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


    def FuseFace(self, request):
        """本接口用于单脸、多脸、选脸融合，上传人脸图片，得到与素材模板融合后的人脸图片。支持为融合结果图添加标识。查看 <a href="https://cloud.tencent.com/document/product/670/38247" target="_blank">融合接入指引</a>。

        请求频率限制为20次/秒。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for FuseFace.
        :type request: :class:`tencentcloud.facefusion.v20220927.models.FuseFaceRequest`
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.FuseFaceResponse`

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


    def FuseFaceUltra(self, request):
        """图片人脸融合（专业版）为同步接口，支持自定义美颜、人脸增强、牙齿增强、拉脸等参数，最高支持8K分辨率，有多个模型类型供选择。查看 <a href="https://cloud.tencent.com/document/product/670/38247" target="_blank">融合接入指引</a>。
        请求频率限制为2次/秒。

        :param request: Request instance for FuseFaceUltra.
        :type request: :class:`tencentcloud.facefusion.v20220927.models.FuseFaceUltraRequest`
        :rtype: :class:`tencentcloud.facefusion.v20220927.models.FuseFaceUltraResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FuseFaceUltra", params, headers=headers)
            response = json.loads(body)
            model = models.FuseFaceUltraResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))