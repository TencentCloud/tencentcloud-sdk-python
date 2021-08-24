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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Location(AbstractModel):
    """检测到的主体在图片中的矩形框位置（四个顶点坐标）

    """

    def __init__(self):
        r"""
        :param XMin: 位置矩形框的左上角横坐标
        :type XMin: int
        :param YMin: 位置矩形框的左上角纵坐标
        :type YMin: int
        :param XMax: 位置矩形框的右下角横坐标
        :type XMax: int
        :param YMax: 位置矩形框的右下角纵坐标
        :type YMax: int
        """
        self.XMin = None
        self.YMin = None
        self.XMax = None
        self.YMax = None


    def _deserialize(self, params):
        self.XMin = params.get("XMin")
        self.YMin = params.get("YMin")
        self.XMax = params.get("XMax")
        self.YMax = params.get("YMax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductInfo(AbstractModel):
    """图像识别出的商品的详细信息。
    当图像中检测到多个物品时，会对显著性最高的物品进行识别。

    """

    def __init__(self):
        r"""
        :param FindSKU: 1表示找到同款商品，以下字段为同款商品信息； 
0表示未找到同款商品， 具体商品信息为空（参考价格、名称、品牌等），仅提供商品类目。  
是否找到同款的判断依据为Score分值，分值越大则同款的可能性越大。
        :type FindSKU: int
        :param Location: 本商品在图片中的坐标，表示为矩形框的四个顶点坐标。
        :type Location: :class:`tencentcloud.iir.v20200417.models.Location`
        :param Name: 商品名称
        :type Name: str
        :param Brand: 商品品牌
        :type Brand: str
        :param Price: 参考价格，综合多个信息源，仅供参考。
        :type Price: str
        :param ProductCategory: 识别结果的商品类目。 
包含：鞋、图书音像、箱包、美妆个护、服饰、家电数码、玩具乐器、食品饮料、珠宝、家居家装、药品、酒水、绿植园艺、其他商品、非商品等。 
当类别为“非商品”时，除Location、Score和本字段之外的商品信息为空。
        :type ProductCategory: str
        :param Score: 输入图片中的主体物品和输出结果的相似度。分值越大，输出结果与输入图片是同款的可能性越高。
        :type Score: float
        :param Image: 搜索到的商品配图URL
        :type Image: str
        """
        self.FindSKU = None
        self.Location = None
        self.Name = None
        self.Brand = None
        self.Price = None
        self.ProductCategory = None
        self.Score = None
        self.Image = None


    def _deserialize(self, params):
        self.FindSKU = params.get("FindSKU")
        if params.get("Location") is not None:
            self.Location = Location()
            self.Location._deserialize(params.get("Location"))
        self.Name = params.get("Name")
        self.Brand = params.get("Brand")
        self.Price = params.get("Price")
        self.ProductCategory = params.get("ProductCategory")
        self.Score = params.get("Score")
        self.Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeProductRequest(AbstractModel):
    """RecognizeProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片限制：内测版仅支持jpg、jpeg，图片大小不超过1M，分辨率在25万到100万之间。 
建议先对图片进行压缩，以便提升处理速度。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过1M，分辨率在25万到100万之间。 
与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeProductResponse(AbstractModel):
    """RecognizeProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegionDetected: 检测到的图片中的商品位置和品类预测。 
当图片中存在多个商品时，输出多组坐标，按照__显著性__排序（综合考虑面积、是否在中心、检测算法置信度）。 
最多可以输出__3组__检测结果。
        :type RegionDetected: list of RegionDetected
        :param ProductInfo: 图像识别出的商品的详细信息。 
当图像中检测到多个物品时，会对显著性最高的进行识别。
        :type ProductInfo: :class:`tencentcloud.iir.v20200417.models.ProductInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionDetected = None
        self.ProductInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionDetected") is not None:
            self.RegionDetected = []
            for item in params.get("RegionDetected"):
                obj = RegionDetected()
                obj._deserialize(item)
                self.RegionDetected.append(obj)
        if params.get("ProductInfo") is not None:
            self.ProductInfo = ProductInfo()
            self.ProductInfo._deserialize(params.get("ProductInfo"))
        self.RequestId = params.get("RequestId")


class RegionDetected(AbstractModel):
    """检测到的图片中的商品位置和品类预测。
    当图片中存在多个商品时，输出多组坐标，按照__显著性__排序（综合考虑面积、是否在中心、检测算法置信度）。
    最多可以输出__3组__检测结果。

    """

    def __init__(self):
        r"""
        :param Category: 商品的品类预测结果。 
包含：鞋、图书音像、箱包、美妆个护、服饰、家电数码、玩具乐器、食品饮料、珠宝、家居家装、药品、酒水、绿植园艺、其他商品、非商品等。
        :type Category: str
        :param CategoryScore: 商品品类预测的置信度
        :type CategoryScore: float
        :param Location: 检测到的主体在图片中的坐标，表示为矩形框的四个顶点坐标
        :type Location: :class:`tencentcloud.iir.v20200417.models.Location`
        """
        self.Category = None
        self.CategoryScore = None
        self.Location = None


    def _deserialize(self, params):
        self.Category = params.get("Category")
        self.CategoryScore = params.get("CategoryScore")
        if params.get("Location") is not None:
            self.Location = Location()
            self.Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        