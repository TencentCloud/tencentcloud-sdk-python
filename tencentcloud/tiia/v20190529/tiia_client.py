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
from tencentcloud.tiia.v20190529 import models


class TiiaClient(AbstractClient):
    _apiVersion = '2019-05-29'
    _endpoint = 'tiia.tencentcloudapi.com'
    _service = 'tiia'


    def AssessQuality(self, request):
        """评估输入图片在视觉上的质量，从多个方面评估，并同时给出综合的、客观的清晰度评分，和主观的美观度评分。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for AssessQuality.
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


    def CropImage(self, request):
        """根据输入的裁剪比例，智能判断一张图片的最佳裁剪区域，确保原图的主体区域不受影响。

        可以自动裁剪图片，适应不同平台、设备的展示要求，避免简单拉伸带来的变形。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for CropImage.
        :type request: :class:`tencentcloud.tiia.v20190529.models.CropImageRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.CropImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CropImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CropImageResponse()
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
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectCelebrity.
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


    def DetectDisgust(self, request):
        """输入一张图片，返回AI针对一张图片是否是恶心的一系列判断值。

        通过恶心图片识别, 可以判断一张图片是否令人恶心, 同时给出它属于的潜在类别, 让您能够过滤掉使人不愉快的图片。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectDisgust.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectDisgustRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectDisgustResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectDisgust", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectDisgustResponse()
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
        """图像标签利用深度学习技术、海量训练数据，可以对图片进行智能分类、物体识别等。

        目前支持8个大类、六十多个子类、数千个标签。涵盖各种日常场景、动植物、物品、美食、卡证等。具体分类请见[图像分析常见问题功能与限制相关](https://cloud.tencent.com/document/product/865/39164)。

        图像标签提供四个版本供选择：

        • 摄像头版：针对搜索、手机摄像头照片进行优化，涵盖大量卡证、日常物品、二维码条形码。

        • 相册版：针对手机相册、网盘进行优化，去除相册和网盘中不常见的标签，针对相册常见图片类型（人像、日常活动、日常物品等）识别效果更好。

        • 网络版：针对网络图片进行优化，涵盖标签更多，满足长尾识别需求。

        • 新闻版：针对新闻、资讯、广电等行业进行优化，增加定制识别，支持万级图像标签。

        每个产品的图像类型都有独特性，建议在接入初期，对四个版本进行对比评估后选择合适的版本使用。

        为了方便使用、减少图片传输次数，图像标签包装成多合一接口，实际上是多个服务。

        图像标签按照服务的实际使用数量进行收费。例如一张图片同时调用相册版、摄像头版两个服务，那么此次调用按照两次计费。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectLabel.
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


    def DetectLabelBeta(self, request):
        """图像标签测试接口

        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectLabelBeta.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectLabelBetaRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectLabelBetaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectLabelBeta", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectLabelBetaResponse()
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


    def DetectMisbehavior(self, request):
        """可以识别输入的图片中是否包含不良行为，例如打架斗殴、赌博、抽烟等，可以应用于广告图、直播截图、短视频截图等审核，减少不良行为对平台内容质量的影响，维护健康向上的互联网环境。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectMisbehavior.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectMisbehaviorRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectMisbehaviorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectMisbehavior", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectMisbehaviorResponse()
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
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectProduct.
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


    def DetectProductBeta(self, request):
        """商品识别-微信识物版，基于人工智能技术、海量训练图片、亿级商品库，可以实现全覆盖、细粒度、高准确率的商品识别和商品推荐功能。
        本服务可以识别出图片中的主体位置、主体商品类型，覆盖亿级SKU，输出具体商品的价格、型号等详细信息。
        客户无需自建商品库，即可快速实现商品识别、拍照搜商品等功能。

        目前“商品识别-微信识物版”为内测服务，需要申请、开通后方可使用。请在[服务开通申请表](https://cloud.tencent.com/apply/p/y1q2mnf0vdl) 中填写详细信息和需求，如果通过审核，我们将会在2个工作日内与您联系，并开通服务。
        内测期间，本服务免费提供最高2QPS，收费模式和标准会在正式版上线前通过站内信、短信通知客户。如果需要提升并发，请与我们联系洽谈。

        注意：本文档为内测版本，仅适用于功能体验和测试，正式业务接入请等待正式版。正式版的输入、输出可能会与内测版存在少量差异。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectProductBeta.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectProductBetaRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectProductBetaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectProductBeta", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectProductBetaResponse()
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
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for EnhanceImage.
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


    def RecognizeCar(self, request):
        """腾讯云车辆属性识别可对汽车车身及车辆属性进行检测与识别，目前支持11种车身颜色、20多种车型、300多种品牌、4000多种车系+年款的识别，同时支持对车辆的位置进行检测。如果图片中存在多辆车，会分别输出每辆车的车型和坐标。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for RecognizeCar.
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