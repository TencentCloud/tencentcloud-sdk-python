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


class AssessQualityRequest(AbstractModel):
    """AssessQuality请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果。 
• 长宽比：长边：短边<5。
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过Base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要Base64编码，并且要去掉编码头部。**
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
        


class AssessQualityResponse(AbstractModel):
    """AssessQuality返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LongImage: 取值为TRUE或FALSE，TRUE为长图，FALSE为正常图，长图定义为长宽比大于等于3或小于等于1/3的图片。
        :type LongImage: bool
        :param _BlackAndWhite: 取值为TRUE或FALSE，TRUE为黑白图，FALSE为否。黑白图即灰度图，指红绿蓝三个通道都是以灰度色阶显示的图片，并非视觉上的“黑白图片”。
        :type BlackAndWhite: bool
        :param _SmallImage: 取值为TRUE或FALSE，TRUE为小图，FALSE为否, 小图定义为最长边小于179像素的图片。当一张图片被判断为小图时，不建议做推荐和展示，其他字段统一输出为0或FALSE。
        :type SmallImage: bool
        :param _BigImage: 取值为TRUE或FALSE，TRUE为大图，FALSE为否，定义为最短边大于1000像素的图片
        :type BigImage: bool
        :param _PureImage: 取值为TRUE或FALSE，TRUE为纯色图或纯文字图，即没有内容或只有简单内容的图片，FALSE为正常图片。
        :type PureImage: bool
        :param _ClarityScore: 综合评分。图像清晰度的得分，对图片的噪声、曝光、模糊、压缩等因素进行综合评估，取值为[0, 100]，值越大，越清晰。一般大于50为较清晰图片，标准可以自行把握。
        :type ClarityScore: int
        :param _AestheticScore: 综合评分。图像美观度得分， 从构图、色彩等多个艺术性维度评价图片，取值为[0, 100]，值越大，越美观。一般大于50为较美观图片，标准可以自行把握。
        :type AestheticScore: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LongImage = None
        self._BlackAndWhite = None
        self._SmallImage = None
        self._BigImage = None
        self._PureImage = None
        self._ClarityScore = None
        self._AestheticScore = None
        self._RequestId = None

    @property
    def LongImage(self):
        return self._LongImage

    @LongImage.setter
    def LongImage(self, LongImage):
        self._LongImage = LongImage

    @property
    def BlackAndWhite(self):
        return self._BlackAndWhite

    @BlackAndWhite.setter
    def BlackAndWhite(self, BlackAndWhite):
        self._BlackAndWhite = BlackAndWhite

    @property
    def SmallImage(self):
        return self._SmallImage

    @SmallImage.setter
    def SmallImage(self, SmallImage):
        self._SmallImage = SmallImage

    @property
    def BigImage(self):
        return self._BigImage

    @BigImage.setter
    def BigImage(self, BigImage):
        self._BigImage = BigImage

    @property
    def PureImage(self):
        return self._PureImage

    @PureImage.setter
    def PureImage(self, PureImage):
        self._PureImage = PureImage

    @property
    def ClarityScore(self):
        return self._ClarityScore

    @ClarityScore.setter
    def ClarityScore(self, ClarityScore):
        self._ClarityScore = ClarityScore

    @property
    def AestheticScore(self):
        return self._AestheticScore

    @AestheticScore.setter
    def AestheticScore(self, AestheticScore):
        self._AestheticScore = AestheticScore

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LongImage = params.get("LongImage")
        self._BlackAndWhite = params.get("BlackAndWhite")
        self._SmallImage = params.get("SmallImage")
        self._BigImage = params.get("BigImage")
        self._PureImage = params.get("PureImage")
        self._ClarityScore = params.get("ClarityScore")
        self._AestheticScore = params.get("AestheticScore")
        self._RequestId = params.get("RequestId")


class Attribute(AbstractModel):
    """属性

    """

    def __init__(self):
        r"""
        :param _Type: 属性
        :type Type: str
        :param _Details: 属性详情
        :type Details: str
        """
        self._Type = None
        self._Details = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Details = params.get("Details")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributesForBody(AbstractModel):
    """属性检测到的人体

    """

    def __init__(self):
        r"""
        :param _Rect: 人体框。当不开启人体检测时，内部参数默认为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rect: :class:`tencentcloud.tiia.v20190529.models.ImageRect`
        :param _DetectConfidence: 人体检测置信度。取值0-1之间，当不开启人体检测开关时默认为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectConfidence: float
        :param _Attributes: 属性信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Attributes: list of BodyAttributes
        """
        self._Rect = None
        self._DetectConfidence = None
        self._Attributes = None

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect

    @property
    def DetectConfidence(self):
        return self._DetectConfidence

    @DetectConfidence.setter
    def DetectConfidence(self, DetectConfidence):
        self._DetectConfidence = DetectConfidence

    @property
    def Attributes(self):
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes


    def _deserialize(self, params):
        if params.get("Rect") is not None:
            self._Rect = ImageRect()
            self._Rect._deserialize(params.get("Rect"))
        self._DetectConfidence = params.get("DetectConfidence")
        if params.get("Attributes") is not None:
            self._Attributes = []
            for item in params.get("Attributes"):
                obj = BodyAttributes()
                obj._deserialize(item)
                self._Attributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyAttributes(AbstractModel):
    """属性列表。

    """

    def __init__(self):
        r"""
        :param _Label: 属性值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Confidence: 置信度，取值0-1之间。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Name: 属性名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Label = None
        self._Confidence = None
        self._Name = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Confidence = params.get("Confidence")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Box(AbstractModel):
    """图像主体区域。

    """

    def __init__(self):
        r"""
        :param _Rect: 图像主体区域。
        :type Rect: :class:`tencentcloud.tiia.v20190529.models.ImageRect`
        :param _Score: 置信度。
        :type Score: float
        :param _CategoryId: 主体区域类目ID
        :type CategoryId: int
        """
        self._Rect = None
        self._Score = None
        self._CategoryId = None

    @property
    def Rect(self):
        return self._Rect

    @Rect.setter
    def Rect(self, Rect):
        self._Rect = Rect

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def CategoryId(self):
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId


    def _deserialize(self, params):
        if params.get("Rect") is not None:
            self._Rect = ImageRect()
            self._Rect._deserialize(params.get("Rect"))
        self._Score = params.get("Score")
        self._CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarPlateContent(AbstractModel):
    """车牌信息

    """

    def __init__(self):
        r"""
        :param _Plate: 车牌信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Plate: str
        :param _Color: 车牌颜色。
注意：此字段可能返回 null，表示取不到有效值。
        :type Color: str
        :param _Type: 车牌类型，包含：0普通蓝牌，1双层黄牌，2单层黄牌，3新能源车牌，4使馆车牌，5领馆车牌，6澳门车牌，7香港车牌，8警用车牌，9教练车牌，10武警车牌，11军用车牌   -2遮挡污损模糊车牌/异常   其他无牌
注意：
此字段可能返回 null，表示取不到有效值。
此字段结果遮挡污损模糊车牌/异常：包含PlateStatus参数的“遮挡污损模糊车牌”，针对车牌异常，建议参考此字段，更全面
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _PlateLocation: 车牌在图片中的坐标信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateLocation: list of Coord
        :param _PlateStatus: 判断车牌是否遮挡：“遮挡污损模糊车牌”和"正常车牌"。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateStatus: str
        :param _PlateStatusConfidence: 车牌遮挡的置信度，0-100。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateStatusConfidence: int
        :param _PlateAngle: 车牌角度。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateAngle: float
        """
        self._Plate = None
        self._Color = None
        self._Type = None
        self._PlateLocation = None
        self._PlateStatus = None
        self._PlateStatusConfidence = None
        self._PlateAngle = None

    @property
    def Plate(self):
        return self._Plate

    @Plate.setter
    def Plate(self, Plate):
        self._Plate = Plate

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PlateLocation(self):
        return self._PlateLocation

    @PlateLocation.setter
    def PlateLocation(self, PlateLocation):
        self._PlateLocation = PlateLocation

    @property
    def PlateStatus(self):
        return self._PlateStatus

    @PlateStatus.setter
    def PlateStatus(self, PlateStatus):
        self._PlateStatus = PlateStatus

    @property
    def PlateStatusConfidence(self):
        return self._PlateStatusConfidence

    @PlateStatusConfidence.setter
    def PlateStatusConfidence(self, PlateStatusConfidence):
        self._PlateStatusConfidence = PlateStatusConfidence

    @property
    def PlateAngle(self):
        return self._PlateAngle

    @PlateAngle.setter
    def PlateAngle(self, PlateAngle):
        self._PlateAngle = PlateAngle


    def _deserialize(self, params):
        self._Plate = params.get("Plate")
        self._Color = params.get("Color")
        self._Type = params.get("Type")
        if params.get("PlateLocation") is not None:
            self._PlateLocation = []
            for item in params.get("PlateLocation"):
                obj = Coord()
                obj._deserialize(item)
                self._PlateLocation.append(obj)
        self._PlateStatus = params.get("PlateStatus")
        self._PlateStatusConfidence = params.get("PlateStatusConfidence")
        self._PlateAngle = params.get("PlateAngle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarTagItem(AbstractModel):
    """车辆属性识别的结果

    """

    def __init__(self):
        r"""
        :param _Serial: 车系
        :type Serial: str
        :param _Brand: 车辆品牌
        :type Brand: str
        :param _Type: 车辆类型
        :type Type: str
        :param _Color: 车辆颜色
        :type Color: str
        :param _Confidence: 车系置信度，0-100
        :type Confidence: int
        :param _Year: 年份，没识别出年份的时候返回0
        :type Year: int
        :param _CarLocation: 车辆在图片中的坐标信息
        :type CarLocation: list of Coord
        :param _PlateContent: 车牌信息，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateContent: :class:`tencentcloud.tiia.v20190529.models.CarPlateContent`
        :param _PlateConfidence: 车牌信息置信度，0-100，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateConfidence: int
        :param _TypeConfidence: 车辆类型置信度，0-100，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeConfidence: int
        :param _ColorConfidence: 车辆颜色置信度，0-100，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type ColorConfidence: int
        :param _Orientation: 车辆朝向，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Orientation: str
        :param _OrientationConfidence: 车辆朝向置信度，0-100，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type OrientationConfidence: int
        """
        self._Serial = None
        self._Brand = None
        self._Type = None
        self._Color = None
        self._Confidence = None
        self._Year = None
        self._CarLocation = None
        self._PlateContent = None
        self._PlateConfidence = None
        self._TypeConfidence = None
        self._ColorConfidence = None
        self._Orientation = None
        self._OrientationConfidence = None

    @property
    def Serial(self):
        return self._Serial

    @Serial.setter
    def Serial(self, Serial):
        self._Serial = Serial

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Year(self):
        return self._Year

    @Year.setter
    def Year(self, Year):
        self._Year = Year

    @property
    def CarLocation(self):
        return self._CarLocation

    @CarLocation.setter
    def CarLocation(self, CarLocation):
        self._CarLocation = CarLocation

    @property
    def PlateContent(self):
        return self._PlateContent

    @PlateContent.setter
    def PlateContent(self, PlateContent):
        self._PlateContent = PlateContent

    @property
    def PlateConfidence(self):
        return self._PlateConfidence

    @PlateConfidence.setter
    def PlateConfidence(self, PlateConfidence):
        self._PlateConfidence = PlateConfidence

    @property
    def TypeConfidence(self):
        return self._TypeConfidence

    @TypeConfidence.setter
    def TypeConfidence(self, TypeConfidence):
        self._TypeConfidence = TypeConfidence

    @property
    def ColorConfidence(self):
        return self._ColorConfidence

    @ColorConfidence.setter
    def ColorConfidence(self, ColorConfidence):
        self._ColorConfidence = ColorConfidence

    @property
    def Orientation(self):
        return self._Orientation

    @Orientation.setter
    def Orientation(self, Orientation):
        self._Orientation = Orientation

    @property
    def OrientationConfidence(self):
        return self._OrientationConfidence

    @OrientationConfidence.setter
    def OrientationConfidence(self, OrientationConfidence):
        self._OrientationConfidence = OrientationConfidence


    def _deserialize(self, params):
        self._Serial = params.get("Serial")
        self._Brand = params.get("Brand")
        self._Type = params.get("Type")
        self._Color = params.get("Color")
        self._Confidence = params.get("Confidence")
        self._Year = params.get("Year")
        if params.get("CarLocation") is not None:
            self._CarLocation = []
            for item in params.get("CarLocation"):
                obj = Coord()
                obj._deserialize(item)
                self._CarLocation.append(obj)
        if params.get("PlateContent") is not None:
            self._PlateContent = CarPlateContent()
            self._PlateContent._deserialize(params.get("PlateContent"))
        self._PlateConfidence = params.get("PlateConfidence")
        self._TypeConfidence = params.get("TypeConfidence")
        self._ColorConfidence = params.get("ColorConfidence")
        self._Orientation = params.get("Orientation")
        self._OrientationConfidence = params.get("OrientationConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ColorInfo(AbstractModel):
    """整张图颜色信息。

    """

    def __init__(self):
        r"""
        :param _Color: RGB颜色值（16进制），例如：291A18。
        :type Color: str
        :param _Percentage: 当前颜色标签所占比例。
        :type Percentage: float
        :param _Label: 颜色标签。蜜柚色，米驼色等。
        :type Label: str
        """
        self._Color = None
        self._Percentage = None
        self._Label = None

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def Percentage(self):
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._Color = params.get("Color")
        self._Percentage = params.get("Percentage")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coord(AbstractModel):
    """汽车坐标信息

    """

    def __init__(self):
        r"""
        :param _X: 横坐标x
        :type X: int
        :param _Y: 纵坐标y
        :type Y: int
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 图库ID，不可重复，仅支持字母、数字和下划线。图库数量单个用户上限为30。
        :type GroupId: str
        :param _GroupName: 图库名称描述。
        :type GroupName: str
        :param _MaxCapacity: 图片库可容纳的最大图片特征条数，一张图片对应一条图片特征数据，不支持修改。
单个图片库容量最大可达亿级，达到容量限制后继续创建图片将会报错。
注意，包月计费下支持绑定的最小库容量为500万。
        :type MaxCapacity: int
        :param _Brief: 图库简介。
        :type Brief: str
        :param _MaxQps: 访问限制默认为10qps，如需扩容请联系[在线客服](https://cloud.tencent.com/online-service)申请。
        :type MaxQps: int
        :param _GroupType: 图库类型，用于决定图像搜索的服务类型和算法版本，默认为4。
GroupType不支持修改，若不确定适用的服务类型，建议先对不同类型分别小规模测试后再开始正式使用。
参数取值：
4：通用图像搜索1.0版。
8：商品图像搜索3.0升级版。
7：商品图像搜索2.0版。
5：商品图像搜索1.0版。
6：图案花纹搜索1.0版。
1 - 3：通用图像搜索旧版，不推荐使用。
        :type GroupType: int
        """
        self._GroupId = None
        self._GroupName = None
        self._MaxCapacity = None
        self._Brief = None
        self._MaxQps = None
        self._GroupType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MaxCapacity(self):
        return self._MaxCapacity

    @MaxCapacity.setter
    def MaxCapacity(self, MaxCapacity):
        self._MaxCapacity = MaxCapacity

    @property
    def Brief(self):
        return self._Brief

    @Brief.setter
    def Brief(self, Brief):
        self._Brief = Brief

    @property
    def MaxQps(self):
        return self._MaxQps

    @MaxQps.setter
    def MaxQps(self, MaxQps):
        self._MaxQps = MaxQps

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._MaxCapacity = params.get("MaxCapacity")
        self._Brief = params.get("Brief")
        self._MaxQps = params.get("MaxQps")
        self._GroupType = params.get("GroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    """CreateImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 图库ID。
        :type GroupId: str
        :param _EntityId: 物品ID，最多支持64个字符。 
一个物品ID可以包含多张图片，若EntityId已存在，则对其追加图片。同一个EntityId，最大支持10张图。
        :type EntityId: str
        :param _PicName: 图片名称，最多支持64个字符， 
PicName唯一确定一张图片，具有唯一性。
        :type PicName: str
        :param _ImageUrl: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。  
ImageUrl和ImageBase64必须提供一个，如果都提供，只使用ImageUrl。
图片限制：
• 图片格式：支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
• 图片大小：对应图片 base64 编码后大小不可超过5M。图片分辨率不超过4096\*4096。
• 如果在商品图像搜索中开启主体识别，分辨率不超过2000\*2000，图片长宽比小于10。
建议：
• 图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的Url速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _CustomContent: 图片自定义备注内容，最多支持4096个字符，查询时原样带回。
        :type CustomContent: str
        :param _ImageBase64: 图片 base64 数据，base64 编码后大小不可超过5M。 
图片限制：
• 图片格式：支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
• 图片大小：base64 编码后大小不可超过5M。图片分辨率不超过4096\*4096。
• 如果在商品图像搜索中开启主体识别，分辨率不超过2000\*2000，图片长宽比小于10。
        :type ImageBase64: str
        :param _Tags: 图片自定义标签，最多不超过10个，格式为JSON。
        :type Tags: str
        :param _EnableDetect: 是否需要启用主体识别，默认为**TRUE**。
• 为**TRUE**时，启用主体识别，返回主体信息。若没有指定**ImageRect**，自动提取最大面积主体创建图片并进行主体识别。主体识别结果可在**Response**中获取。
• 为**FALSE**时，不启用主体识别，不返回主体信息。若没有指定**ImageRect**，以整张图创建图片。
**<font color=#1E90FF>注意：仅服务类型为商品图像搜索时才生效。</font>**
        :type EnableDetect: bool
        :param _CategoryId: 图像类目ID。
若设置类目ID，提取以下类目的主体创建图片。
类目取值说明：
0：上衣。
1：裙装。
2：下装。
3：包。
4：鞋。
5：配饰。
**<font color=#1E90FF>注意：仅服务类型为商品图像搜索时才生效。</font>**
        :type CategoryId: int
        :param _ImageRect: 图像主体区域。
若设置主体区域，提取指定的区域创建图片。
        :type ImageRect: :class:`tencentcloud.tiia.v20190529.models.Rect`
        """
        self._GroupId = None
        self._EntityId = None
        self._PicName = None
        self._ImageUrl = None
        self._CustomContent = None
        self._ImageBase64 = None
        self._Tags = None
        self._EnableDetect = None
        self._CategoryId = None
        self._ImageRect = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EntityId(self):
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def PicName(self):
        return self._PicName

    @PicName.setter
    def PicName(self, PicName):
        self._PicName = PicName

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def CustomContent(self):
        return self._CustomContent

    @CustomContent.setter
    def CustomContent(self, CustomContent):
        self._CustomContent = CustomContent

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnableDetect(self):
        return self._EnableDetect

    @EnableDetect.setter
    def EnableDetect(self, EnableDetect):
        self._EnableDetect = EnableDetect

    @property
    def CategoryId(self):
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def ImageRect(self):
        return self._ImageRect

    @ImageRect.setter
    def ImageRect(self, ImageRect):
        self._ImageRect = ImageRect


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._EntityId = params.get("EntityId")
        self._PicName = params.get("PicName")
        self._ImageUrl = params.get("ImageUrl")
        self._CustomContent = params.get("CustomContent")
        self._ImageBase64 = params.get("ImageBase64")
        self._Tags = params.get("Tags")
        self._EnableDetect = params.get("EnableDetect")
        self._CategoryId = params.get("CategoryId")
        if params.get("ImageRect") is not None:
            self._ImageRect = Rect()
            self._ImageRect._deserialize(params.get("ImageRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    """CreateImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Object: 输入图的主体信息。
若启用主体识别且在请求中指定了类目ID或主体区域，以指定的主体为准。若启用主体识别且没有指定，以最大面积主体为准。
**<font color=#1E90FF>注意：仅服务类型为商品图像搜索时才生效。</font>**
注意：此字段可能返回 null，表示取不到有效值。
        :type Object: :class:`tencentcloud.tiia.v20190529.models.ObjectInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Object = None
        self._RequestId = None

    @property
    def Object(self):
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Object") is not None:
            self._Object = ObjectInfo()
            self._Object._deserialize(params.get("Object"))
        self._RequestId = params.get("RequestId")


class CropImageRequest(AbstractModel):
    """CropImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Width: 需要裁剪区域的宽度，与Height共同组成所需裁剪的图片宽高比例。
输入数字请大于0、小于图片宽度的像素值。
        :type Width: int
        :param _Height: 需要裁剪区域的高度，与Width共同组成所需裁剪的图片宽高比例。
输入数字请大于0、小于图片高度的像素值。
宽高比例（Width : Height）会简化为最简分数，即如果Width输入10、Height输入20，会简化为1：2。
Width : Height建议取值在[1, 2.5]之间，超过这个范围可能会影响效果。
        :type Height: int
        :param _ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果。
• 长宽比：长边：短边<5。 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过Base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
注意：图片需要Base64编码，并且要去掉编码头部。
        :type ImageBase64: str
        """
        self._Width = None
        self._Height = None
        self._ImageUrl = None
        self._ImageBase64 = None

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

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
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CropImageResponse(AbstractModel):
    """CropImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _X: 裁剪区域左上角X坐标值
        :type X: int
        :param _Y: 裁剪区域左上角Y坐标值
        :type Y: int
        :param _Width: 裁剪区域的宽度，单位为像素
        :type Width: int
        :param _Height: 裁剪区域的高度，单位为像素
        :type Height: int
        :param _OriginalWidth: 原图宽度，单位为像素
        :type OriginalWidth: int
        :param _OriginalHeight: 原图高度，单位为像素
        :type OriginalHeight: int
        :param _CropResult: 0：抠图正常；
1：原图过长，指原图的高度是宽度的1.8倍以上；
2：原图过宽，指原图的宽度是高度的1.8倍以上；
3：抠图区域过长，指抠图的高度是主体备选框高度的1.6倍以上；
4：抠图区域过宽，指当没有检测到人脸时，抠图区域宽度是检测出的原图主体区域宽度的1.6倍以上；
5：纯色图，指裁剪区域视觉较为单一、缺乏主体部分 ；
6：宽高比异常，指Width : Height取值超出[1, 2.5]的范围；

以上是辅助决策的参考建议，可以根据业务需求选择采纳或忽视。
        :type CropResult: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None
        self._OriginalWidth = None
        self._OriginalHeight = None
        self._CropResult = None
        self._RequestId = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def OriginalWidth(self):
        return self._OriginalWidth

    @OriginalWidth.setter
    def OriginalWidth(self, OriginalWidth):
        self._OriginalWidth = OriginalWidth

    @property
    def OriginalHeight(self):
        return self._OriginalHeight

    @OriginalHeight.setter
    def OriginalHeight(self, OriginalHeight):
        self._OriginalHeight = OriginalHeight

    @property
    def CropResult(self):
        return self._CropResult

    @CropResult.setter
    def CropResult(self, CropResult):
        self._CropResult = CropResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._OriginalWidth = params.get("OriginalWidth")
        self._OriginalHeight = params.get("OriginalHeight")
        self._CropResult = params.get("CropResult")
        self._RequestId = params.get("RequestId")


class DeleteImagesRequest(AbstractModel):
    """DeleteImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 图库名称。
        :type GroupId: str
        :param _EntityId: 物品ID。
        :type EntityId: str
        :param _PicName: 图片名称，如果不指定本参数，则删除EntityId下所有的图片；否则删除指定的图。
        :type PicName: str
        """
        self._GroupId = None
        self._EntityId = None
        self._PicName = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EntityId(self):
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def PicName(self):
        return self._PicName

    @PicName.setter
    def PicName(self, PicName):
        self._PicName = PicName


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._EntityId = params.get("EntityId")
        self._PicName = params.get("PicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImagesResponse(AbstractModel):
    """DeleteImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeGroupsRequest(AbstractModel):
    """DescribeGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 起始序号，默认值为0。
        :type Offset: int
        :param _Limit: 返回数量，默认值为10，最大值为100。
        :type Limit: int
        :param _GroupId: 图库ID，如果不为空，则返回指定库信息。
        :type GroupId: str
        """
        self._Offset = None
        self._Limit = None
        self._GroupId = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupsResponse(AbstractModel):
    """DescribeGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 图库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of GroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 图库名称。
        :type GroupId: str
        :param _EntityId: 物品ID。
        :type EntityId: str
        :param _PicName: 图片名称。
        :type PicName: str
        """
        self._GroupId = None
        self._EntityId = None
        self._PicName = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EntityId(self):
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def PicName(self):
        return self._PicName

    @PicName.setter
    def PicName(self, PicName):
        self._PicName = PicName


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._EntityId = params.get("EntityId")
        self._PicName = params.get("PicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 图库名称。
        :type GroupId: str
        :param _EntityId: 物品ID。
        :type EntityId: str
        :param _ImageInfos: 图片信息。
        :type ImageInfos: list of ImageInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._EntityId = None
        self._ImageInfos = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EntityId(self):
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def ImageInfos(self):
        return self._ImageInfos

    @ImageInfos.setter
    def ImageInfos(self, ImageInfos):
        self._ImageInfos = ImageInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._EntityId = params.get("EntityId")
        if params.get("ImageInfos") is not None:
            self._ImageInfos = []
            for item in params.get("ImageInfos"):
                obj = ImageInfo()
                obj._deserialize(item)
                self._ImageInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DetectChefDressRequest(AbstractModel):
    """DetectChefDress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片的 Url 。
ImageUrl和ImageBase64必须提供一个，同时存在时优先使用ImageUrl字段。
图片限制：
• 图片格式：支持PNG、JPG、JPEG、不支持 GIF 图片。
• 图片大小：对应图片 base64 编码后大小不可超过5M。图片分辨率不超过 3840 x 2160pixel。
建议：
• 接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。与ImageUrl同时存在时优先使用ImageUrl字段。
注意：图片需要base64编码，并且要去掉编码头部。
支持的图片格式：PNG、JPG、JPEG、暂不支持GIF格式。
支持的图片大小：所下载图片经Base64编码后不超过5M。
        :type ImageBase64: str
        :param _EnableDetect: 人体检测模型开关，“true”为开启，“false”为关闭
默认为开启，开启后可先对图片中的人体进行检测之后再进行属性识别
        :type EnableDetect: bool
        :param _EnablePreferred: 人体优选开关，“true”为开启，“false”为关闭
开启后自动对检测质量低的人体进行优选过滤，有助于提高属性识别的准确率。
默认为开启，仅在人体检测开关开启时可配置，人体检测模型关闭时人体优选也关闭
人体优选开启时，检测到的人体分辨率不超过1920*1080 pixel
        :type EnablePreferred: bool
        """
        self._ImageUrl = None
        self._ImageBase64 = None
        self._EnableDetect = None
        self._EnablePreferred = None

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

    @property
    def EnableDetect(self):
        return self._EnableDetect

    @EnableDetect.setter
    def EnableDetect(self, EnableDetect):
        self._EnableDetect = EnableDetect

    @property
    def EnablePreferred(self):
        return self._EnablePreferred

    @EnablePreferred.setter
    def EnablePreferred(self, EnablePreferred):
        self._EnablePreferred = EnablePreferred


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._EnableDetect = params.get("EnableDetect")
        self._EnablePreferred = params.get("EnablePreferred")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectChefDressResponse(AbstractModel):
    """DetectChefDress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Bodies: 识别到的人体属性信息。单个人体属性信息包括人体检测置信度，属性信息，人体检测框。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bodies: list of AttributesForBody
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Bodies = None
        self._RequestId = None

    @property
    def Bodies(self):
        return self._Bodies

    @Bodies.setter
    def Bodies(self, Bodies):
        self._Bodies = Bodies

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Bodies") is not None:
            self._Bodies = []
            for item in params.get("Bodies"):
                obj = AttributesForBody()
                obj._deserialize(item)
                self._Bodies.append(obj)
        self._RequestId = params.get("RequestId")


class DetectDisgustRequest(AbstractModel):
    """DetectDisgust请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
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
        


class DetectDisgustResponse(AbstractModel):
    """DetectDisgust返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Confidence: 对于图片中包含恶心内容的置信度，取值[0,1]，一般超过0.5则表明可能是恶心图片。
        :type Confidence: float
        :param _Type: 与图像内容最相似的恶心内容的类别，包含腐烂、密集、畸形、血腥、蛇、虫子、牙齿等。
        :type Type: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Confidence = None
        self._Type = None
        self._RequestId = None

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Type = params.get("Type")
        self._RequestId = params.get("RequestId")


class DetectEnvelopeRequest(AbstractModel):
    """DetectEnvelope请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片的URL地址。图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
图片大小的限制为4M，图片像素的限制为4k。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。与ImageUrl同时存在时优先使用ImageUrl字段。 
图片大小的限制为4M，图片像素的限制为4k。
**注意：图片需要base64编码，并且要去掉编码头部。
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
        


class DetectEnvelopeResponse(AbstractModel):
    """DetectEnvelope返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FirstTags: 一级标签结果数组。识别是否文件封。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstTags: list of ImageTag
        :param _SecondTags: 二级标签结果数组。识别文件封正反面。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondTags: list of ImageTag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FirstTags = None
        self._SecondTags = None
        self._RequestId = None

    @property
    def FirstTags(self):
        return self._FirstTags

    @FirstTags.setter
    def FirstTags(self, FirstTags):
        self._FirstTags = FirstTags

    @property
    def SecondTags(self):
        return self._SecondTags

    @SecondTags.setter
    def SecondTags(self, SecondTags):
        self._SecondTags = SecondTags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FirstTags") is not None:
            self._FirstTags = []
            for item in params.get("FirstTags"):
                obj = ImageTag()
                obj._deserialize(item)
                self._FirstTags.append(obj)
        if params.get("SecondTags") is not None:
            self._SecondTags = []
            for item in params.get("SecondTags"):
                obj = ImageTag()
                obj._deserialize(item)
                self._SecondTags.append(obj)
        self._RequestId = params.get("RequestId")


class DetectLabelBetaRequest(AbstractModel):
    """DetectLabelBeta请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        :param _Scenes: 本次调用支持的识别场景，可选值如下：
WEB，针对网络图片优化;
CAMERA，针对手机摄像头拍摄图片优化;
ALBUM，针对手机相册、网盘产品优化;
NEWS，针对新闻、资讯、广电等行业优化；
NONECAM，非实拍图；
LOCATION，主体位置识别；
如果不传此参数，则默认为WEB。

支持多场景（Scenes）一起检测。例如，使用 Scenes=["WEB", "CAMERA"]，即对一张图片使用两个模型同时检测，输出两套识别结果。
        :type Scenes: list of str
        """
        self._ImageUrl = None
        self._ImageBase64 = None
        self._Scenes = None

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

    @property
    def Scenes(self):
        return self._Scenes

    @Scenes.setter
    def Scenes(self, Scenes):
        self._Scenes = Scenes


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._Scenes = params.get("Scenes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectLabelBetaResponse(AbstractModel):
    """DetectLabelBeta返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Labels: Web网络版标签结果数组。如未选择WEB场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DetectLabelItem
        :param _CameraLabels: Camera摄像头版标签结果数组。如未选择CAMERA场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CameraLabels: list of DetectLabelItem
        :param _AlbumLabels: Album相册版标签结果数组。如未选择ALBUM场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumLabels: list of DetectLabelItem
        :param _NewsLabels: News新闻版标签结果数组。如未选择NEWS场景，则为空。
新闻版目前为测试阶段，暂不提供每个标签的一级、二级分类信息的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type NewsLabels: list of DetectLabelItem
        :param _NoneCamLabels: 非实拍标签
注意：此字段可能返回 null，表示取不到有效值。
        :type NoneCamLabels: list of DetectLabelItem
        :param _LocationLabels: 识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationLabels: list of Product
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Labels = None
        self._CameraLabels = None
        self._AlbumLabels = None
        self._NewsLabels = None
        self._NoneCamLabels = None
        self._LocationLabels = None
        self._RequestId = None

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def CameraLabels(self):
        return self._CameraLabels

    @CameraLabels.setter
    def CameraLabels(self, CameraLabels):
        self._CameraLabels = CameraLabels

    @property
    def AlbumLabels(self):
        return self._AlbumLabels

    @AlbumLabels.setter
    def AlbumLabels(self, AlbumLabels):
        self._AlbumLabels = AlbumLabels

    @property
    def NewsLabels(self):
        return self._NewsLabels

    @NewsLabels.setter
    def NewsLabels(self, NewsLabels):
        self._NewsLabels = NewsLabels

    @property
    def NoneCamLabels(self):
        return self._NoneCamLabels

    @NoneCamLabels.setter
    def NoneCamLabels(self, NoneCamLabels):
        self._NoneCamLabels = NoneCamLabels

    @property
    def LocationLabels(self):
        return self._LocationLabels

    @LocationLabels.setter
    def LocationLabels(self, LocationLabels):
        self._LocationLabels = LocationLabels

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("CameraLabels") is not None:
            self._CameraLabels = []
            for item in params.get("CameraLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self._CameraLabels.append(obj)
        if params.get("AlbumLabels") is not None:
            self._AlbumLabels = []
            for item in params.get("AlbumLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self._AlbumLabels.append(obj)
        if params.get("NewsLabels") is not None:
            self._NewsLabels = []
            for item in params.get("NewsLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self._NewsLabels.append(obj)
        if params.get("NoneCamLabels") is not None:
            self._NoneCamLabels = []
            for item in params.get("NoneCamLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self._NoneCamLabels.append(obj)
        if params.get("LocationLabels") is not None:
            self._LocationLabels = []
            for item in params.get("LocationLabels"):
                obj = Product()
                obj._deserialize(item)
                self._LocationLabels.append(obj)
        self._RequestId = params.get("RequestId")


class DetectLabelItem(AbstractModel):
    """图像标签检测结果。

    """

    def __init__(self):
        r"""
        :param _Name: 图片中的物体名称。
        :type Name: str
        :param _Confidence: 算法对于Name的置信度，0-100之间，值越高，表示对于Name越确定。
        :type Confidence: int
        :param _FirstCategory: 标签的一级分类
        :type FirstCategory: str
        :param _SecondCategory: 标签的二级分类
        :type SecondCategory: str
        """
        self._Name = None
        self._Confidence = None
        self._FirstCategory = None
        self._SecondCategory = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def FirstCategory(self):
        return self._FirstCategory

    @FirstCategory.setter
    def FirstCategory(self, FirstCategory):
        self._FirstCategory = FirstCategory

    @property
    def SecondCategory(self):
        return self._SecondCategory

    @SecondCategory.setter
    def SecondCategory(self, SecondCategory):
        self._SecondCategory = SecondCategory


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Confidence = params.get("Confidence")
        self._FirstCategory = params.get("FirstCategory")
        self._SecondCategory = params.get("SecondCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectLabelProRequest(AbstractModel):
    """DetectLabelPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片 URL 地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG、BMP。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边:短边<5； 
• 接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片 Base64 编码数据。
与ImageUrl同时存在时优先使用ImageUrl字段。
图片限制：
• 图片格式：PNG、JPG、JPEG、BMP。 
• 图片大小：经Base64编码后不超过4M。
**<font color=#1E90FF>注意：图片需要Base64编码，并且要去掉编码头部。</font>**
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
        


class DetectLabelProResponse(AbstractModel):
    """DetectLabelPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Labels: 返回标签数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DetectLabelItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Labels = None
        self._RequestId = None

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._RequestId = params.get("RequestId")


class DetectLabelRequest(AbstractModel):
    """DetectLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 图片 Base64 编码数据。
与ImageUrl同时存在时优先使用ImageUrl字段。
图片限制：
• 图片格式：PNG、JPG、JPEG、BMP。 
• 图片大小：经Base64编码后不超过4M。
**<font color=#1E90FF>注意：图片需要Base64编码，并且要去掉编码头部。</font>**
        :type ImageBase64: str
        :param _ImageUrl: 图片 URL 地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG、BMP。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边:短边<5； 
• 接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _Scenes: 本次调用支持的识别场景，可选值如下：
• WEB，针对网络图片优化;
• CAMERA，针对手机摄像头拍摄图片优化;
• ALBUM，针对手机相册、网盘产品优化;
• NEWS，针对新闻、资讯、广电等行业优化；
如果不传此参数，则默认为WEB。

支持多场景（Scenes）一起检测。例如，使用 Scenes=["WEB", "CAMERA"]，即对一张图片使用两个模型同时检测，输出两套识别结果。
        :type Scenes: list of str
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Scenes = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Scenes(self):
        return self._Scenes

    @Scenes.setter
    def Scenes(self, Scenes):
        self._Scenes = Scenes


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Scenes = params.get("Scenes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectLabelResponse(AbstractModel):
    """DetectLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Labels: Web网络版标签结果数组。如未选择WEB场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DetectLabelItem
        :param _CameraLabels: Camera摄像头版标签结果数组。如未选择CAMERA场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CameraLabels: list of DetectLabelItem
        :param _AlbumLabels: Album相册版标签结果数组。如未选择ALBUM场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumLabels: list of DetectLabelItem
        :param _NewsLabels: News新闻版标签结果数组。如未选择NEWS场景，则为空。
新闻版目前为测试阶段，暂不提供每个标签的一级、二级分类信息的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type NewsLabels: list of DetectLabelItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Labels = None
        self._CameraLabels = None
        self._AlbumLabels = None
        self._NewsLabels = None
        self._RequestId = None

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def CameraLabels(self):
        return self._CameraLabels

    @CameraLabels.setter
    def CameraLabels(self, CameraLabels):
        self._CameraLabels = CameraLabels

    @property
    def AlbumLabels(self):
        return self._AlbumLabels

    @AlbumLabels.setter
    def AlbumLabels(self, AlbumLabels):
        self._AlbumLabels = AlbumLabels

    @property
    def NewsLabels(self):
        return self._NewsLabels

    @NewsLabels.setter
    def NewsLabels(self, NewsLabels):
        self._NewsLabels = NewsLabels

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("CameraLabels") is not None:
            self._CameraLabels = []
            for item in params.get("CameraLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self._CameraLabels.append(obj)
        if params.get("AlbumLabels") is not None:
            self._AlbumLabels = []
            for item in params.get("AlbumLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self._AlbumLabels.append(obj)
        if params.get("NewsLabels") is not None:
            self._NewsLabels = []
            for item in params.get("NewsLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self._NewsLabels.append(obj)
        self._RequestId = params.get("RequestId")


class DetectMisbehaviorRequest(AbstractModel):
    """DetectMisbehavior请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
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
        


class DetectMisbehaviorResponse(AbstractModel):
    """DetectMisbehavior返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Confidence: 对于图片中包含不良行为的置信度，取值[0,1]，一般超过0.5则表明可能包含不良行为内容；
        :type Confidence: float
        :param _Type: 图像中最可能包含的不良行为类别，包括赌博、打架斗殴、吸毒等。
        :type Type: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Confidence = None
        self._Type = None
        self._RequestId = None

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Type = params.get("Type")
        self._RequestId = params.get("RequestId")


class DetectPetRequest(AbstractModel):
    """DetectPet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片的URL地址。图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
图片大小的限制为4M，图片像素的限制为4k。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。与ImageUrl同时存在时优先使用ImageUrl字段。 
图片大小的限制为4M，图片像素的限制为4k。
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
        


class DetectPetResponse(AbstractModel):
    """DetectPet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Pets: 识别出图片中的宠物信息列表。
        :type Pets: list of Pet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Pets = None
        self._RequestId = None

    @property
    def Pets(self):
        return self._Pets

    @Pets.setter
    def Pets(self, Pets):
        self._Pets = Pets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Pets") is not None:
            self._Pets = []
            for item in params.get("Pets"):
                obj = Pet()
                obj._deserialize(item)
                self._Pets.append(obj)
        self._RequestId = params.get("RequestId")


class DetectProductRequest(AbstractModel):
    """DetectProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
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
        


class DetectProductResponse(AbstractModel):
    """DetectProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 商品识别结果数组
        :type Products: list of Product
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._RequestId = None

    @property
    def Products(self):
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = Product()
                obj._deserialize(item)
                self._Products.append(obj)
        self._RequestId = params.get("RequestId")


class DetectSecurityRequest(AbstractModel):
    """DetectSecurity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片的 Url 。
ImageUrl和ImageBase64必须提供一个，同时存在时优先使用ImageUrl字段。
图片限制：
• 图片格式：支持PNG、JPG、JPEG、不支持 GIF 图片。
• 图片大小：对应图片 base64 编码后大小不可超过5M。图片分辨率不超过3840 x 2160 pixel。
建议：
• 接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。
最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
注意：图片需要base64编码，并且要去掉编码头部。
支持的图片格式：PNG、JPG、JPEG、暂不支持GIF格式。
支持的图片大小：所下载图片经Base64编码后不超过5M。
        :type ImageBase64: str
        :param _EnableDetect: 人体检测模型开关，“true”为开启，“false”为关闭
开启后可先对图片中的人体进行检测之后再进行属性识别，默认为开启
        :type EnableDetect: bool
        :param _EnablePreferred: 人体优选开关，“true”为开启，“false”为关闭
开启后自动对检测质量低的人体进行优选过滤，有助于提高属性识别的准确率。
默认为开启，仅在人体检测开关开启时可配置，人体检测模型关闭时人体优选也关闭
如开启人体优选，检测到的人体分辨率需不大于1920*1080 pixel
        :type EnablePreferred: bool
        """
        self._ImageUrl = None
        self._ImageBase64 = None
        self._EnableDetect = None
        self._EnablePreferred = None

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

    @property
    def EnableDetect(self):
        return self._EnableDetect

    @EnableDetect.setter
    def EnableDetect(self, EnableDetect):
        self._EnableDetect = EnableDetect

    @property
    def EnablePreferred(self):
        return self._EnablePreferred

    @EnablePreferred.setter
    def EnablePreferred(self, EnablePreferred):
        self._EnablePreferred = EnablePreferred


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._EnableDetect = params.get("EnableDetect")
        self._EnablePreferred = params.get("EnablePreferred")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectSecurityResponse(AbstractModel):
    """DetectSecurity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Bodies: 识别到的人体属性信息。单个人体属性信息包括人体检测置信度，属性信息，人体检测框。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bodies: list of AttributesForBody
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Bodies = None
        self._RequestId = None

    @property
    def Bodies(self):
        return self._Bodies

    @Bodies.setter
    def Bodies(self, Bodies):
        self._Bodies = Bodies

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Bodies") is not None:
            self._Bodies = []
            for item in params.get("Bodies"):
                obj = AttributesForBody()
                obj._deserialize(item)
                self._Bodies.append(obj)
        self._RequestId = params.get("RequestId")


class EnhanceImageRequest(AbstractModel):
    """EnhanceImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，最大不超过250万像素，否则影响识别效果。 
• 长宽比：长边：短边<5。 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。图片经过Base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
注意：图片需要Base64编码，并且要去掉编码头部。
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
        


class EnhanceImageResponse(AbstractModel):
    """EnhanceImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnhancedImage: 增强后图片的base64编码。
        :type EnhancedImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnhancedImage = None
        self._RequestId = None

    @property
    def EnhancedImage(self):
        return self._EnhancedImage

    @EnhancedImage.setter
    def EnhancedImage(self, EnhancedImage):
        self._EnhancedImage = EnhancedImage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnhancedImage = params.get("EnhancedImage")
        self._RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    """图库信息。

    """

    def __init__(self):
        r"""
        :param _GroupId: 图库Id。
        :type GroupId: str
        :param _GroupName: 图库名称。
        :type GroupName: str
        :param _Brief: 图库简介。
        :type Brief: str
        :param _MaxCapacity: 图库容量。
        :type MaxCapacity: int
        :param _MaxQps: 该库的访问限频 。
        :type MaxQps: int
        :param _GroupType: 图库类型，对应不同服务类型，默认为1。建议手动调整为4～6，1～3为历史版本，不推荐。
参数值：
4：在自建图库中搜索相同原图，可支持裁剪、翻转、调色、加水印后的图片搜索，适用于图片版权保护、原图查询等场景。
5：在自建图库中搜索相同或相似的商品图片，适用于商品分类、检索、推荐等电商场景。
6：在自建图片库中搜索与输入图片高度相似的图片，适用于相似图案、logo、纹理等图像元素的搜索。
        :type GroupType: int
        :param _PicCount: 图库图片数量。
        :type PicCount: int
        :param _CreateTime: 图库创建时间。
        :type CreateTime: str
        :param _UpdateTime: 图库更新时间。
        :type UpdateTime: str
        """
        self._GroupId = None
        self._GroupName = None
        self._Brief = None
        self._MaxCapacity = None
        self._MaxQps = None
        self._GroupType = None
        self._PicCount = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Brief(self):
        return self._Brief

    @Brief.setter
    def Brief(self, Brief):
        self._Brief = Brief

    @property
    def MaxCapacity(self):
        return self._MaxCapacity

    @MaxCapacity.setter
    def MaxCapacity(self, MaxCapacity):
        self._MaxCapacity = MaxCapacity

    @property
    def MaxQps(self):
        return self._MaxQps

    @MaxQps.setter
    def MaxQps(self, MaxQps):
        self._MaxQps = MaxQps

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def PicCount(self):
        return self._PicCount

    @PicCount.setter
    def PicCount(self, PicCount):
        self._PicCount = PicCount

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Brief = params.get("Brief")
        self._MaxCapacity = params.get("MaxCapacity")
        self._MaxQps = params.get("MaxQps")
        self._GroupType = params.get("GroupType")
        self._PicCount = params.get("PicCount")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    """图片信息

    """

    def __init__(self):
        r"""
        :param _EntityId: 图片名称。
        :type EntityId: str
        :param _CustomContent: 用户自定义的内容。
        :type CustomContent: str
        :param _Tags: 图片自定义标签，JSON格式。
        :type Tags: str
        :param _PicName: 图片名称。
        :type PicName: str
        :param _Score: 相似度。
        :type Score: int
        """
        self._EntityId = None
        self._CustomContent = None
        self._Tags = None
        self._PicName = None
        self._Score = None

    @property
    def EntityId(self):
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def CustomContent(self):
        return self._CustomContent

    @CustomContent.setter
    def CustomContent(self, CustomContent):
        self._CustomContent = CustomContent

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PicName(self):
        return self._PicName

    @PicName.setter
    def PicName(self, PicName):
        self._PicName = PicName

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._EntityId = params.get("EntityId")
        self._CustomContent = params.get("CustomContent")
        self._Tags = params.get("Tags")
        self._PicName = params.get("PicName")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRect(AbstractModel):
    """图像主体区域坐标

    """

    def __init__(self):
        r"""
        :param _X: 左上角横坐标。
        :type X: int
        :param _Y: 左上角纵坐标。
        :type Y: int
        :param _Width: 宽度。
        :type Width: int
        :param _Height: 高度。
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTag(AbstractModel):
    """图片标签。

    """

    def __init__(self):
        r"""
        :param _Name: 标签内容。
        :type Name: str
        :param _Confidence: 置信度范围在0-100之间。值越高，表示目标为相应结果的可能性越高。
        :type Confidence: float
        """
        self._Name = None
        self._Confidence = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectInfo(AbstractModel):
    """图像的主体信息。

    """

    def __init__(self):
        r"""
        :param _Box: 图像主体区域。
        :type Box: :class:`tencentcloud.tiia.v20190529.models.Box`
        :param _CategoryId: 主体类别ID。
        :type CategoryId: int
        :param _Colors: 整张图颜色信息。
        :type Colors: list of ColorInfo
        :param _Attributes: 属性信息。
        :type Attributes: list of Attribute
        :param _AllBox: 图像的所有主体区域，置信度，以及主体区域类别ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllBox: list of Box
        """
        self._Box = None
        self._CategoryId = None
        self._Colors = None
        self._Attributes = None
        self._AllBox = None

    @property
    def Box(self):
        return self._Box

    @Box.setter
    def Box(self, Box):
        self._Box = Box

    @property
    def CategoryId(self):
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def Colors(self):
        return self._Colors

    @Colors.setter
    def Colors(self, Colors):
        self._Colors = Colors

    @property
    def Attributes(self):
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes

    @property
    def AllBox(self):
        return self._AllBox

    @AllBox.setter
    def AllBox(self, AllBox):
        self._AllBox = AllBox


    def _deserialize(self, params):
        if params.get("Box") is not None:
            self._Box = Box()
            self._Box._deserialize(params.get("Box"))
        self._CategoryId = params.get("CategoryId")
        if params.get("Colors") is not None:
            self._Colors = []
            for item in params.get("Colors"):
                obj = ColorInfo()
                obj._deserialize(item)
                self._Colors.append(obj)
        if params.get("Attributes") is not None:
            self._Attributes = []
            for item in params.get("Attributes"):
                obj = Attribute()
                obj._deserialize(item)
                self._Attributes.append(obj)
        if params.get("AllBox") is not None:
            self._AllBox = []
            for item in params.get("AllBox"):
                obj = Box()
                obj._deserialize(item)
                self._AllBox.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pet(AbstractModel):
    """宠物具体信息

    """

    def __init__(self):
        r"""
        :param _Name: 识别出的宠物类型（猫或者狗，暂不支持识别猫狗品种）。
        :type Name: str
        :param _Score: 识别服务给识别目标打出的置信度，范围在0-100之间。值越高，表示目标为相应结果的可能性越高。
        :type Score: int
        :param _Location: 识别目标在图片中的坐标。
        :type Location: :class:`tencentcloud.tiia.v20190529.models.Rect`
        """
        self._Name = None
        self._Score = None
        self._Location = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Score = params.get("Score")
        if params.get("Location") is not None:
            self._Location = Rect()
            self._Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Product(AbstractModel):
    """检测到的单个商品结构体

    """

    def __init__(self):
        r"""
        :param _Name: 图片中商品的三级分类识别结果，选取所有三级分类中的置信度最大者
        :type Name: str
        :param _Parents: 三级商品分类对应的一级分类和二级分类，两级之间用“-”（中划线）隔开，例如商品名称是“硬盘”，那么Parents输出为“电脑、办公-电脑配件”
        :type Parents: str
        :param _Confidence: 算法对于Name的置信度，0-100之间，值越高，表示对于Name越确定
        :type Confidence: int
        :param _XMin: 商品坐标X轴的最小值
        :type XMin: int
        :param _YMin: 商品坐标Y轴的最小值
        :type YMin: int
        :param _XMax: 商品坐标X轴的最大值
        :type XMax: int
        :param _YMax: 商品坐标Y轴的最大值
        :type YMax: int
        """
        self._Name = None
        self._Parents = None
        self._Confidence = None
        self._XMin = None
        self._YMin = None
        self._XMax = None
        self._YMax = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Parents(self):
        return self._Parents

    @Parents.setter
    def Parents(self, Parents):
        self._Parents = Parents

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

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
        self._Name = params.get("Name")
        self._Parents = params.get("Parents")
        self._Confidence = params.get("Confidence")
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
        


class RecognizeCarProRequest(AbstractModel):
    """RecognizeCarPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
支持的图片格式：PNG、JPG、JPEG、BMP，暂不支持GIF格式。支持的图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。
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
        


class RecognizeCarProResponse(AbstractModel):
    """RecognizeCarPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CarCoords: 汽车的四个矩形顶点坐标，如果图片中存在多辆车，则输出最大车辆的坐标。
        :type CarCoords: list of Coord
        :param _CarTags: 车辆属性识别的结果数组，如果识别到多辆车，则会输出每辆车的top1结果。
注意：置信度是指车牌信息置信度。
        :type CarTags: list of CarTagItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CarCoords = None
        self._CarTags = None
        self._RequestId = None

    @property
    def CarCoords(self):
        return self._CarCoords

    @CarCoords.setter
    def CarCoords(self, CarCoords):
        self._CarCoords = CarCoords

    @property
    def CarTags(self):
        return self._CarTags

    @CarTags.setter
    def CarTags(self, CarTags):
        self._CarTags = CarTags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CarCoords") is not None:
            self._CarCoords = []
            for item in params.get("CarCoords"):
                obj = Coord()
                obj._deserialize(item)
                self._CarCoords.append(obj)
        if params.get("CarTags") is not None:
            self._CarTags = []
            for item in params.get("CarTags"):
                obj = CarTagItem()
                obj._deserialize(item)
                self._CarTags.append(obj)
        self._RequestId = params.get("RequestId")


class RecognizeCarRequest(AbstractModel):
    """RecognizeCar请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
支持的图片格式：PNG、JPG、JPEG、BMP，暂不支持GIF格式。支持的图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。
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
        


class RecognizeCarResponse(AbstractModel):
    """RecognizeCar返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CarCoords: 汽车的四个矩形顶点坐标，如果图片中存在多辆车，则输出最大车辆的坐标。
        :type CarCoords: list of Coord
        :param _CarTags: 车辆属性识别的结果数组，如果识别到多辆车，则会输出每辆车的top1结果。
        :type CarTags: list of CarTagItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CarCoords = None
        self._CarTags = None
        self._RequestId = None

    @property
    def CarCoords(self):
        return self._CarCoords

    @CarCoords.setter
    def CarCoords(self, CarCoords):
        self._CarCoords = CarCoords

    @property
    def CarTags(self):
        return self._CarTags

    @CarTags.setter
    def CarTags(self, CarTags):
        self._CarTags = CarTags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CarCoords") is not None:
            self._CarCoords = []
            for item in params.get("CarCoords"):
                obj = Coord()
                obj._deserialize(item)
                self._CarCoords.append(obj)
        if params.get("CarTags") is not None:
            self._CarTags = []
            for item in params.get("CarTags"):
                obj = CarTagItem()
                obj._deserialize(item)
                self._CarTags.append(obj)
        self._RequestId = params.get("RequestId")


class Rect(AbstractModel):
    """具体坐标，可用来判断边界

    """

    def __init__(self):
        r"""
        :param _X: x轴坐标
        :type X: int
        :param _Y: y轴坐标
        :type Y: int
        :param _Width: (x,y)坐标距离长度
        :type Width: int
        :param _Height: (x,y)坐标距离高度
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchImageRequest(AbstractModel):
    """SearchImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 图库名称。
        :type GroupId: str
        :param _ImageUrl: 图片的 Url 。
ImageUrl和ImageBase64必须提供一个，如果都提供，只使用ImageUrl。
图片限制：
• 图片格式：支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
• 图片大小：对应图片 base64 编码后大小不可超过5M。图片分辨率不超过4096\*4096。
• 如果在商品图像搜索中开启主体识别，分辨率不超过2000\*2000，图片长宽比小于10。
建议：
• 图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的Url速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _ImageBase64: 图片 base64 数据。
ImageUrl和ImageBase64必须提供一个，如果都提供，只使用ImageUrl。
图片限制：
• 图片格式：支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
• 图片大小：base64 编码后大小不可超过5M。图片分辨率不超过4096\*4096。
• 如果在商品图像搜索中开启主体识别，分辨率不超过2000\*2000，图片长宽比小于10。
        :type ImageBase64: str
        :param _Limit: 返回结果的数量，默认值为10，最大值为100。
按照相似度分数由高到低排序。
**<font color=#1E90FF>服务类型为图案花纹搜索时Limit = 1，最多只能返回1个结果。</font>**
        :type Limit: int
        :param _Offset: 返回结果的起始序号，默认值为0。
        :type Offset: int
        :param _MatchThreshold: 匹配阈值。
只有图片相似度分数超过匹配阈值的结果才会返回。
当MatchThreshold为0（默认值）时，各服务类型将按照以下默认的匹配阈值进行结果过滤：
• 通用图像搜索1.0版：50。
• 商品图像搜索2.0升级版：45。
• 商品图像搜索1.0版：28。
• 图案花纹搜索1.0版：56。
建议：
可以手动调整MatchThreshold值来控制输出结果的范围。如果发现无检索结果，可能是因为图片相似度较低导致检索结果被匹配阈值过滤，建议调整为较低的阈值后再次尝试检索。
        :type MatchThreshold: int
        :param _Filter: 标签过滤条件。
针对创建图片时提交的Tags信息进行条件过滤。支持>、>=、 <、 <=、=，!=，多个条件之间支持AND和OR进行连接。
        :type Filter: str
        :param _ImageRect: 图像主体区域。
若设置主体区域，提取指定的区域进行检索。
        :type ImageRect: :class:`tencentcloud.tiia.v20190529.models.ImageRect`
        :param _EnableDetect: 是否需要启用主体识别，默认为**TRUE** 。
• 为**TRUE**时，启用主体识别，返回主体信息。若没有指定**ImageRect**，自动提取最大面积主体进行检索并进行主体识别。主体识别结果可在**Response中**获取。
• 为**FALSE**时，不启用主体识别，不返回主体信息。若没有指定**ImageRect**，以整张图检索图片。
**<font color=#1E90FF>注意：仅服务类型为商品图像搜索时才生效。</font>**
        :type EnableDetect: bool
        :param _CategoryId: 图像类目ID。
若设置类目ID，提取以下类目的主体进行检索。
类目取值说明：
0：上衣。
1：裙装。
2：下装。
3：包。
4：鞋。
5：配饰。
**<font color=#1E90FF>注意：仅服务类型为商品图像搜索时才生效。</font>**
        :type CategoryId: int
        """
        self._GroupId = None
        self._ImageUrl = None
        self._ImageBase64 = None
        self._Limit = None
        self._Offset = None
        self._MatchThreshold = None
        self._Filter = None
        self._ImageRect = None
        self._EnableDetect = None
        self._CategoryId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def MatchThreshold(self):
        return self._MatchThreshold

    @MatchThreshold.setter
    def MatchThreshold(self, MatchThreshold):
        self._MatchThreshold = MatchThreshold

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def ImageRect(self):
        return self._ImageRect

    @ImageRect.setter
    def ImageRect(self, ImageRect):
        self._ImageRect = ImageRect

    @property
    def EnableDetect(self):
        return self._EnableDetect

    @EnableDetect.setter
    def EnableDetect(self, EnableDetect):
        self._EnableDetect = EnableDetect

    @property
    def CategoryId(self):
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._MatchThreshold = params.get("MatchThreshold")
        self._Filter = params.get("Filter")
        if params.get("ImageRect") is not None:
            self._ImageRect = ImageRect()
            self._ImageRect._deserialize(params.get("ImageRect"))
        self._EnableDetect = params.get("EnableDetect")
        self._CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchImageResponse(AbstractModel):
    """SearchImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 返回结果数量。
        :type Count: int
        :param _ImageInfos: 图片信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfos: list of ImageInfo
        :param _Object: 输入图的主体信息。
若启用主体识别且在请求中指定了类目ID或主体区域，以指定的主体为准。若启用主体识别且没有指定，以最大面积主体为准。
**<font color=#1E90FF>注意：仅服务类型为商品图像搜索时才生效。</font>**
注意：此字段可能返回 null，表示取不到有效值。
        :type Object: :class:`tencentcloud.tiia.v20190529.models.ObjectInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._ImageInfos = None
        self._Object = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ImageInfos(self):
        return self._ImageInfos

    @ImageInfos.setter
    def ImageInfos(self, ImageInfos):
        self._ImageInfos = ImageInfos

    @property
    def Object(self):
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("ImageInfos") is not None:
            self._ImageInfos = []
            for item in params.get("ImageInfos"):
                obj = ImageInfo()
                obj._deserialize(item)
                self._ImageInfos.append(obj)
        if params.get("Object") is not None:
            self._Object = ObjectInfo()
            self._Object._deserialize(params.get("Object"))
        self._RequestId = params.get("RequestId")


class UpdateImageRequest(AbstractModel):
    """UpdateImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 图库ID。
        :type GroupId: str
        :param _EntityId: 物品ID，最多支持64个字符。
        :type EntityId: str
        :param _PicName: 图片名称，最多支持64个字符。
        :type PicName: str
        :param _Tags: 新的自定义标签，最多不超过10个，格式为JSON。
        :type Tags: str
        """
        self._GroupId = None
        self._EntityId = None
        self._PicName = None
        self._Tags = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EntityId(self):
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def PicName(self):
        return self._PicName

    @PicName.setter
    def PicName(self, PicName):
        self._PicName = PicName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._EntityId = params.get("EntityId")
        self._PicName = params.get("PicName")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateImageResponse(AbstractModel):
    """UpdateImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")