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
        :param _XMin: 位置矩形框的左上角横坐标
        :type XMin: int
        :param _YMin: 位置矩形框的左上角纵坐标
        :type YMin: int
        :param _XMax: 位置矩形框的右下角横坐标
        :type XMax: int
        :param _YMax: 位置矩形框的右下角纵坐标
        :type YMax: int
        """
        self._XMin = None
        self._YMin = None
        self._XMax = None
        self._YMax = None

    @property
    def XMin(self):
        return self._XMin

    @XMin.setter
    def XMin(self, XMin):
        self._XMin = XMin

    @property
    def YMin(self):
        return self._YMin

    @YMin.setter
    def YMin(self, YMin):
        self._YMin = YMin

    @property
    def XMax(self):
        return self._XMax

    @XMax.setter
    def XMax(self, XMax):
        self._XMax = XMax

    @property
    def YMax(self):
        return self._YMax

    @YMax.setter
    def YMax(self, YMax):
        self._YMax = YMax


    def _deserialize(self, params):
        self._XMin = params.get("XMin")
        self._YMin = params.get("YMin")
        self._XMax = params.get("XMax")
        self._YMax = params.get("YMax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductInfo(AbstractModel):
    """图像识别出的商品的详细信息。
    当图像中检测到多个物品时，会对显著性最高的物品进行识别。

    """

    def __init__(self):
        r"""
        :param _FindSKU: 1表示找到同款商品，以下字段为同款商品信息； 
0表示未找到同款商品， 具体商品信息为空（参考价格、名称、品牌等），仅提供商品类目。  
是否找到同款的判断依据为Score分值，分值越大则同款的可能性越大。
        :type FindSKU: int
        :param _Location: 本商品在图片中的坐标，表示为矩形框的四个顶点坐标。
        :type Location: :class:`tencentcloud.iir.v20200417.models.Location`
        :param _Name: 商品名称
        :type Name: str
        :param _Brand: 商品品牌
        :type Brand: str
        :param _Price: 参考价格，综合多个信息源，仅供参考。
        :type Price: str
        :param _ProductCategory: 识别结果的商品类目。 
包含：鞋、图书音像、箱包、美妆个护、服饰、家电数码、玩具乐器、食品饮料、珠宝、家居家装、药品、酒水、绿植园艺、其他商品、非商品等。 
当类别为“非商品”时，除Location、Score和本字段之外的商品信息为空。
        :type ProductCategory: str
        :param _Score: 输入图片中的主体物品和输出结果的相似度。分值越大，输出结果与输入图片是同款的可能性越高。
        :type Score: float
        :param _Image: 搜索到的商品配图URL
        :type Image: str
        """
        self._FindSKU = None
        self._Location = None
        self._Name = None
        self._Brand = None
        self._Price = None
        self._ProductCategory = None
        self._Score = None
        self._Image = None

    @property
    def FindSKU(self):
        return self._FindSKU

    @FindSKU.setter
    def FindSKU(self, FindSKU):
        self._FindSKU = FindSKU

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def ProductCategory(self):
        return self._ProductCategory

    @ProductCategory.setter
    def ProductCategory(self, ProductCategory):
        self._ProductCategory = ProductCategory

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image


    def _deserialize(self, params):
        self._FindSKU = params.get("FindSKU")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        self._Name = params.get("Name")
        self._Brand = params.get("Brand")
        self._Price = params.get("Price")
        self._ProductCategory = params.get("ProductCategory")
        self._Score = params.get("Score")
        self._Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeProductRequest(AbstractModel):
    """RecognizeProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片限制：内测版仅支持jpg、jpeg，图片大小不超过1M，分辨率在25万到100万之间。 
建议先对图片进行压缩，以便提升处理速度。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。最大不超过1M，分辨率在25万到100万之间。 
与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        """
        self._ImageUrl = None
        self._ImageBase64 = None

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeProductResponse(AbstractModel):
    """RecognizeProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionDetected: 检测到的图片中的商品位置和品类预测。 
当图片中存在多个商品时，输出多组坐标，按照__显著性__排序（综合考虑面积、是否在中心、检测算法置信度）。 
最多可以输出__3组__检测结果。
        :type RegionDetected: list of RegionDetected
        :param _ProductInfo: 图像识别出的商品的详细信息。 
当图像中检测到多个物品时，会对显著性最高的进行识别。
        :type ProductInfo: :class:`tencentcloud.iir.v20200417.models.ProductInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionDetected = None
        self._ProductInfo = None
        self._RequestId = None

    @property
    def RegionDetected(self):
        return self._RegionDetected

    @RegionDetected.setter
    def RegionDetected(self, RegionDetected):
        self._RegionDetected = RegionDetected

    @property
    def ProductInfo(self):
        return self._ProductInfo

    @ProductInfo.setter
    def ProductInfo(self, ProductInfo):
        self._ProductInfo = ProductInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionDetected") is not None:
            self._RegionDetected = []
            for item in params.get("RegionDetected"):
                obj = RegionDetected()
                obj._deserialize(item)
                self._RegionDetected.append(obj)
        if params.get("ProductInfo") is not None:
            self._ProductInfo = ProductInfo()
            self._ProductInfo._deserialize(params.get("ProductInfo"))
        self._RequestId = params.get("RequestId")


class RegionDetected(AbstractModel):
    """检测到的图片中的商品位置和品类预测。
    当图片中存在多个商品时，输出多组坐标，按照__显著性__排序（综合考虑面积、是否在中心、检测算法置信度）。
    最多可以输出__3组__检测结果。

    """

    def __init__(self):
        r"""
        :param _Category: 商品的品类预测结果。 
包含：鞋、图书音像、箱包、美妆个护、服饰、家电数码、玩具乐器、食品饮料、珠宝、家居家装、药品、酒水、绿植园艺、其他商品、非商品等。
        :type Category: str
        :param _CategoryScore: 商品品类预测的置信度
        :type CategoryScore: float
        :param _Location: 检测到的主体在图片中的坐标，表示为矩形框的四个顶点坐标
        :type Location: :class:`tencentcloud.iir.v20200417.models.Location`
        """
        self._Category = None
        self._CategoryScore = None
        self._Location = None

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def CategoryScore(self):
        return self._CategoryScore

    @CategoryScore.setter
    def CategoryScore(self, CategoryScore):
        self._CategoryScore = CategoryScore

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._Category = params.get("Category")
        self._CategoryScore = params.get("CategoryScore")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        