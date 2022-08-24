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
            headers = request.headers
            body = self.call("AssessQuality", params, headers=headers)
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


    def CreateGroup(self, request):
        """用于创建一个空的图片库，如果图片库已存在则返回错误。不同类型图库对应不同的图像搜索服务，根据输入参数GroupType区分。

        | 服务类型 | GroupType参数值 |功能描述 |
        |  :------  | :----- |:-----------------  |
        | 相同图像搜索<img width=30/>    | 4 |在自建图库中搜索相同原图，可支持裁剪、翻转、调色、加水印后的图片搜索，适用于图片版权保护、原图查询等场景。|
        | 商品图像搜索<img width=30/>   | 5 |在自建图库中搜索相同或相似的商品图片，适用于商品分类、检索、推荐等电商场景。|
        | 相似图像搜索<img width=30/>   | 6 |在自建图片库中搜索与输入图片高度相似的图片，适用于相似图案、logo、纹理等图像元素的搜索。|

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.tiia.v20190529.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGroupResponse()
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


    def CreateImage(self, request):
        """创建图片，并添加对应图片的自定义信息。

        :param request: Request instance for CreateImage.
        :type request: :class:`tencentcloud.tiia.v20190529.models.CreateImageRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.CreateImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImageResponse()
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
            headers = request.headers
            body = self.call("CropImage", params, headers=headers)
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


    def DeleteImages(self, request):
        """删除图片。

        :param request: Request instance for DeleteImages.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DeleteImagesRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DeleteImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImages", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImagesResponse()
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


    def DescribeGroups(self, request):
        """查询所有的图库信息。

        :param request: Request instance for DescribeGroups.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DescribeGroupsRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DescribeGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupsResponse()
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


    def DescribeImages(self, request):
        """获取指定图片库中的图片列表。

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImages", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImagesResponse()
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
            headers = request.headers
            body = self.call("DetectDisgust", params, headers=headers)
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


    def DetectEnvelope(self, request):
        """文件封识别可检测图片中是否包含符合文件封（即文件、单据、资料等的袋状包装）特征的物品，覆盖顺丰快递文件封、文件袋、档案袋等多种文件封类型，可应用于物流行业对文件快递的包装审核等场景。

        >?
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectEnvelope.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectEnvelopeRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectEnvelopeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectEnvelope", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectEnvelopeResponse()
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
        """>!
        - **图像标签已升级服务，建议前往使用新版接口[通用图像标签](https://cloud.tencent.com/document/product/865/75196)。**
        - **与本接口相比，[通用图像标签](https://cloud.tencent.com/document/product/865/75196)新版接口提供更高精度的图像标签识别服务，覆盖更广泛的物体与场景类型，效果和通用性更优。**

        图像标签利用深度学习技术，可以对图片进行智能分类、物体识别等。

        目前支持8个大类、六十多个子类、数千个标签。涵盖各种日常场景、动植物、物品、美食、卡证等。具体分类请见[图像分析常见问题功能与限制相关](https://cloud.tencent.com/document/product/865/39164)。

        图像标签提供四个版本供选择：

        • 摄像头版：针对搜索、手机摄像头照片进行优化，涵盖大量卡证、日常物品、二维码条形码。

        • 相册版：针对手机相册、网盘进行优化，去除相册和网盘中不常见的标签，针对相册常见图片类型（人像、日常活动、日常物品等）识别效果更好。

        • 网络版：针对网络图片进行优化，涵盖标签更多，满足长尾识别需求。

        • 新闻版：针对新闻、资讯、广电等行业进行优化，增加定制识别，支持万级图像标签。

        每个产品的图像类型都有独特性，建议在接入初期，对四个版本进行对比评估后选择合适的版本使用。

        为了方便使用、减少图片传输次数，图像标签包装成多合一接口，实际上是多个服务。

        图像标签按照服务的实际使用数量进行收费。例如一张图片同时调用相册版、摄像头版两个服务，那么此次调用按照两次计费。

        >?
        - 图像标签摄像头版、相册版、网络版、新闻版分别按照各自的使用次数进行收费，例如一张图片同时使用相册版、摄像头版，则按照两次调用计费。建议测试对比后从中选择一个最合适的版本使用即可。
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectLabel.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectLabelRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectLabel", params, headers=headers)
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
            headers = request.headers
            body = self.call("DetectLabelBeta", params, headers=headers)
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


    def DetectLabelPro(self, request):
        """通用图像标签可识别数千种常见物体或场景，覆盖日常物品、场景、动物、植物、食物、饮品、交通工具等多个大类，返回主体的标签名称和所属细分类目等，广泛应用于拍照识物、场景分析、内容推荐与审核、智能相册分类等场景。

        >?
        - **通用图像标签**接口在原图像标签接口（旧版接口）的基础上进行了升级，识别精度和场景通用性更优，推荐使用。
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectLabelPro.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectLabelProRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectLabelProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectLabelPro", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectLabelProResponse()
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
            headers = request.headers
            body = self.call("DetectMisbehavior", params, headers=headers)
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
        >?
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectProduct.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectProductRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectProduct", params, headers=headers)
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
        >?
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectProductBeta.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectProductBetaRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectProductBetaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetectProductBeta", params, headers=headers)
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
        """>!
        - 图像清晰度增强接口将于2022年8月31日结束免费公测，2022年9月1日起正式转入计费。若您不需要使用本服务，请及时停止使用。价格详情在[计费概述](https://cloud.tencent.com/document/product/865/17627)中提前公示，请您参阅。

        传入一张图片，输出清晰度提升后的图片。

        可以消除图片有损压缩导致的噪声，和使用滤镜、拍摄失焦导致的模糊。让图片的边缘和细节更加清晰自然。
        >
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for EnhanceImage.
        :type request: :class:`tencentcloud.tiia.v20190529.models.EnhanceImageRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.EnhanceImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnhanceImage", params, headers=headers)
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
        """车辆识别可对图片中车辆的车型进行识别，输出车辆的品牌（如路虎）、车系（如神行者2）、类型（如中型SUV）、颜色和车辆在图中的坐标等信息，覆盖轿车、SUV、大型客车等市面常见车，支持三千多种车辆型号。如果图片中存在多辆车，会分别输出每辆车的车型和坐标。

        >?
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for RecognizeCar.
        :type request: :class:`tencentcloud.tiia.v20190529.models.RecognizeCarRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.RecognizeCarResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeCar", params, headers=headers)
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


    def RecognizeCarPro(self, request):
        """车辆识别（增强版）在车辆识别的基础上**增加了车牌识别的功能，并升级了车型识别的效果**。可对图片中车辆的车型和车牌进行同时识别，输出车辆的车牌信息，以及车辆品牌（如路虎）、车系（如神行者2）、类型（如中型SUV）、颜色和车辆在图中的坐标等信息，覆盖轿车、SUV、大型客车等市面常见车，支持三千多种车辆型号。如果图片中存在多辆车，会分别输出每辆车的车型、车牌和坐标。

        >?
        - 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for RecognizeCarPro.
        :type request: :class:`tencentcloud.tiia.v20190529.models.RecognizeCarProRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.RecognizeCarProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeCarPro", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecognizeCarProResponse()
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


    def SearchImage(self, request):
        """本接口用于对一张待识别的商品图片，在指定图片库中检索出最相似的图片列表。

        :param request: Request instance for SearchImage.
        :type request: :class:`tencentcloud.tiia.v20190529.models.SearchImageRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.SearchImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchImage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchImageResponse()
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