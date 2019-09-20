# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.tiia.v20190529 import models


class TiiaClient(AbstractClient):
    _apiVersion = '2019-05-29'
    _endpoint = 'tiia.tencentcloudapi.com'


    def AssessQuality(self, request):
        """评估输入图片在视觉上的质量，从多个方面评估，并同时给出综合的、客观的清晰度评分，和主观的美观度评分。

        :param request: 调用AssessQuality所需参数的结构体。
        :type request: :class:`tencentcloud.tiia.v20190529.models.AssessQualityRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.AssessQualityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssessQuality", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssessQualityResponse()
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


    def DetectCelebrity(self, request):
        """传入一张图片，可以识别图片中包含的人物是否为公众人物，如果是，输出人物的姓名、基本信息、脸部坐标。

        支持识别一张图片中存在的多个人脸，针对每个人脸，会给出与之最相似的公众人物。

        :param request: 调用DetectCelebrity所需参数的结构体。
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectCelebrityRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectCelebrityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectCelebrity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectCelebrityResponse()
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


    def DetectLabel(self, request):
        """传入一张图片，识别出图片中存在的物体，并返回物体的名称（分类）、置信度，一张图片会给出多个可能的标签。

        :param request: 调用DetectLabel所需参数的结构体。
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectLabelRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectLabelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectLabel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectLabelResponse()
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


    def DetectProduct(self, request):
        """本接口支持识别图片中包含的商品，能够输出商品的品类名称、类别，还可以输出商品在图片中的位置。支持一张图片多个商品的识别。

        :param request: 调用DetectProduct所需参数的结构体。
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectProductRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectProductResponse()
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


    def EnhanceImage(self, request):
        """传入一张图片，输出清晰度提升后的图片。

        可以消除图片有损压缩导致的噪声，和使用滤镜、拍摄失焦导致的模糊。让图片的边缘和细节更加清晰自然。


        :param request: 调用EnhanceImage所需参数的结构体。
        :type request: :class:`tencentcloud.tiia.v20190529.models.EnhanceImageRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.EnhanceImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnhanceImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnhanceImageResponse()
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


    def ImageModeration(self, request):
        """本接口提供多种维度的图像审核能力，支持色情和性感内容识别，政治人物和涉政敏感场景识别，暴恐人物、场景、旗帜标识等违禁内容的识别，以及图片中文字内容的识别。

        :param request: 调用ImageModeration所需参数的结构体。
        :type request: :class:`tencentcloud.tiia.v20190529.models.ImageModerationRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.ImageModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageModerationResponse()
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


    def RecognizeCar(self, request):
        """腾讯云车辆属性识别可对汽车车身及车辆属性进行检测与识别，目前支持11种车身颜色、20多种车型、300多种品牌、4000多种车系+年款的识别，同时支持对车标的位置进行检测。

        :param request: 调用RecognizeCar所需参数的结构体。
        :type request: :class:`tencentcloud.tiia.v20190529.models.RecognizeCarRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.RecognizeCarResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecognizeCar", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecognizeCarResponse()
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