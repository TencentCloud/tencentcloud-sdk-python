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
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果。 
• 长宽比：长边：短边<5。
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过Base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要Base64编码，并且要去掉编码头部。**
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
        


class AssessQualityResponse(AbstractModel):
    """AssessQuality返回参数结构体

    """

    def __init__(self):
        r"""
        :param LongImage: 取值为TRUE或FALSE，TRUE为长图，FALSE为正常图，长图定义为长宽比大于等于3或小于等于1/3的图片。
        :type LongImage: bool
        :param BlackAndWhite: 取值为TRUE或FALSE，TRUE为黑白图，FALSE为否。黑白图即灰度图，指红绿蓝三个通道都是以灰度色阶显示的图片，并非视觉上的“黑白图片”。
        :type BlackAndWhite: bool
        :param SmallImage: 取值为TRUE或FALSE，TRUE为小图，FALSE为否, 小图定义为最长边小于179像素的图片。当一张图片被判断为小图时，不建议做推荐和展示，其他字段统一输出为0或FALSE。
        :type SmallImage: bool
        :param BigImage: 取值为TRUE或FALSE，TRUE为大图，FALSE为否，定义为最短边大于1000像素的图片
        :type BigImage: bool
        :param PureImage: 取值为TRUE或FALSE，TRUE为纯色图或纯文字图，即没有内容或只有简单内容的图片，FALSE为正常图片。
        :type PureImage: bool
        :param ClarityScore: 综合评分。图像清晰度的得分，对图片的噪声、曝光、模糊、压缩等因素进行综合评估，取值为[0, 100]，值越大，越清晰。一般大于50为较清晰图片，标准可以自行把握。
        :type ClarityScore: int
        :param AestheticScore: 综合评分。图像美观度得分， 从构图、色彩等多个艺术性维度评价图片，取值为[0, 100]，值越大，越美观。一般大于50为较美观图片，标准可以自行把握。
        :type AestheticScore: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LongImage = None
        self.BlackAndWhite = None
        self.SmallImage = None
        self.BigImage = None
        self.PureImage = None
        self.ClarityScore = None
        self.AestheticScore = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LongImage = params.get("LongImage")
        self.BlackAndWhite = params.get("BlackAndWhite")
        self.SmallImage = params.get("SmallImage")
        self.BigImage = params.get("BigImage")
        self.PureImage = params.get("PureImage")
        self.ClarityScore = params.get("ClarityScore")
        self.AestheticScore = params.get("AestheticScore")
        self.RequestId = params.get("RequestId")


class Attribute(AbstractModel):
    """属性

    """

    def __init__(self):
        r"""
        :param Type: 属性
        :type Type: str
        :param Details: 属性详情
        :type Details: str
        """
        self.Type = None
        self.Details = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Details = params.get("Details")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributesForBody(AbstractModel):
    """属性检测到的人体

    """

    def __init__(self):
        r"""
        :param Rect: 人体框。当不开启人体检测时，内部参数默认为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rect: :class:`tencentcloud.tiia.v20190529.models.ImageRect`
        :param DetectConfidence: 人体检测置信度。取值0-1之间，当不开启人体检测开关时默认为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectConfidence: float
        :param Attributes: 属性信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Attributes: list of BodyAttributes
        """
        self.Rect = None
        self.DetectConfidence = None
        self.Attributes = None


    def _deserialize(self, params):
        if params.get("Rect") is not None:
            self.Rect = ImageRect()
            self.Rect._deserialize(params.get("Rect"))
        self.DetectConfidence = params.get("DetectConfidence")
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = BodyAttributes()
                obj._deserialize(item)
                self.Attributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyAttributes(AbstractModel):
    """属性列表。

    """

    def __init__(self):
        r"""
        :param Label: 属性值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Confidence: 置信度，取值0-1之间。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Name: 属性名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.Label = None
        self.Confidence = None
        self.Name = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Confidence = params.get("Confidence")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Box(AbstractModel):
    """图像主体区域。

    """

    def __init__(self):
        r"""
        :param Rect: 图像主体区域。
        :type Rect: :class:`tencentcloud.tiia.v20190529.models.ImageRect`
        :param Score: 置信度。
        :type Score: float
        :param CategoryId: 主体区域类目ID
        :type CategoryId: int
        """
        self.Rect = None
        self.Score = None
        self.CategoryId = None


    def _deserialize(self, params):
        if params.get("Rect") is not None:
            self.Rect = ImageRect()
            self.Rect._deserialize(params.get("Rect"))
        self.Score = params.get("Score")
        self.CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarPlateContent(AbstractModel):
    """车牌信息

    """

    def __init__(self):
        r"""
        :param Plate: 车牌信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Plate: str
        :param Color: 车牌颜色。
注意：此字段可能返回 null，表示取不到有效值。
        :type Color: str
        :param Type: 车牌类型，包含：0普通蓝牌，1双层黄牌，2单层黄牌，3新能源车牌，4使馆车牌，5领馆车牌，6澳门车牌，7香港车牌，8警用车牌，9教练车牌，10武警车牌，11军用车牌   -2遮挡污损模糊车牌/异常   其他无牌
注意：
此字段可能返回 null，表示取不到有效值。
此字段结果遮挡污损模糊车牌/异常：包含PlateStatus参数的“遮挡污损模糊车牌”，针对车牌异常，建议参考此字段，更全面
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param PlateLocation: 车牌在图片中的坐标信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateLocation: list of Coord
        :param PlateStatus: 判断车牌是否遮挡：“遮挡污损模糊车牌”和"正常车牌"。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateStatus: str
        :param PlateStatusConfidence: 车牌遮挡的置信度，0-100。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateStatusConfidence: int
        :param PlateAngle: 车牌角度。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateAngle: float
        """
        self.Plate = None
        self.Color = None
        self.Type = None
        self.PlateLocation = None
        self.PlateStatus = None
        self.PlateStatusConfidence = None
        self.PlateAngle = None


    def _deserialize(self, params):
        self.Plate = params.get("Plate")
        self.Color = params.get("Color")
        self.Type = params.get("Type")
        if params.get("PlateLocation") is not None:
            self.PlateLocation = []
            for item in params.get("PlateLocation"):
                obj = Coord()
                obj._deserialize(item)
                self.PlateLocation.append(obj)
        self.PlateStatus = params.get("PlateStatus")
        self.PlateStatusConfidence = params.get("PlateStatusConfidence")
        self.PlateAngle = params.get("PlateAngle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarTagItem(AbstractModel):
    """车辆属性识别的结果

    """

    def __init__(self):
        r"""
        :param Serial: 车系
        :type Serial: str
        :param Brand: 车辆品牌
        :type Brand: str
        :param Type: 车辆类型
        :type Type: str
        :param Color: 车辆颜色
        :type Color: str
        :param Confidence: 车系置信度，0-100
        :type Confidence: int
        :param Year: 年份，没识别出年份的时候返回0
        :type Year: int
        :param CarLocation: 车辆在图片中的坐标信息
        :type CarLocation: list of Coord
        :param PlateContent: 车牌信息，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateContent: :class:`tencentcloud.tiia.v20190529.models.CarPlateContent`
        :param PlateConfidence: 车牌信息置信度，0-100，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateConfidence: int
        :param TypeConfidence: 车辆类型置信度，0-100，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeConfidence: int
        :param ColorConfidence: 车辆颜色置信度，0-100，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type ColorConfidence: int
        :param Orientation: 车辆朝向，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Orientation: str
        :param OrientationConfidence: 车辆朝向置信度，0-100，仅车辆识别（增强版）支持
注意：此字段可能返回 null，表示取不到有效值。
        :type OrientationConfidence: int
        """
        self.Serial = None
        self.Brand = None
        self.Type = None
        self.Color = None
        self.Confidence = None
        self.Year = None
        self.CarLocation = None
        self.PlateContent = None
        self.PlateConfidence = None
        self.TypeConfidence = None
        self.ColorConfidence = None
        self.Orientation = None
        self.OrientationConfidence = None


    def _deserialize(self, params):
        self.Serial = params.get("Serial")
        self.Brand = params.get("Brand")
        self.Type = params.get("Type")
        self.Color = params.get("Color")
        self.Confidence = params.get("Confidence")
        self.Year = params.get("Year")
        if params.get("CarLocation") is not None:
            self.CarLocation = []
            for item in params.get("CarLocation"):
                obj = Coord()
                obj._deserialize(item)
                self.CarLocation.append(obj)
        if params.get("PlateContent") is not None:
            self.PlateContent = CarPlateContent()
            self.PlateContent._deserialize(params.get("PlateContent"))
        self.PlateConfidence = params.get("PlateConfidence")
        self.TypeConfidence = params.get("TypeConfidence")
        self.ColorConfidence = params.get("ColorConfidence")
        self.Orientation = params.get("Orientation")
        self.OrientationConfidence = params.get("OrientationConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ColorInfo(AbstractModel):
    """整张图颜色信息。

    """

    def __init__(self):
        r"""
        :param Color: RGB颜色值（16进制），例如：291A18。
        :type Color: str
        :param Percentage: 当前颜色标签所占比例。
        :type Percentage: float
        :param Label: 颜色标签。蜜柚色，米驼色等。
        :type Label: str
        """
        self.Color = None
        self.Percentage = None
        self.Label = None


    def _deserialize(self, params):
        self.Color = params.get("Color")
        self.Percentage = params.get("Percentage")
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coord(AbstractModel):
    """汽车坐标信息

    """

    def __init__(self):
        r"""
        :param X: 横坐标x
        :type X: int
        :param Y: 纵坐标y
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 图库ID，不可重复，仅支持字母、数字和下划线。
        :type GroupId: str
        :param GroupName: 图库名称描述。
        :type GroupName: str
        :param MaxCapacity: 图库可容纳的最大图片数量。
        :type MaxCapacity: int
        :param Brief: 图库简介。
        :type Brief: str
        :param MaxQps: 访问限制默认为10qps，如需扩容请联系[在线客服](https://cloud.tencent.com/online-service)申请。
        :type MaxQps: int
        :param GroupType: 图库类型，对应不同的图像搜索服务类型，默认为4。1～3为历史版本，不推荐。
参数取值：
4：相同图像搜索。
5：商品图像搜索。
6：相似图像搜索。
        :type GroupType: int
        """
        self.GroupId = None
        self.GroupName = None
        self.MaxCapacity = None
        self.Brief = None
        self.MaxQps = None
        self.GroupType = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.MaxCapacity = params.get("MaxCapacity")
        self.Brief = params.get("Brief")
        self.MaxQps = params.get("MaxQps")
        self.GroupType = params.get("GroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    """CreateImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 图库ID。
        :type GroupId: str
        :param EntityId: 物品ID，最多支持64个字符。 
一个物品ID可以包含多张图片，若EntityId已存在，则对其追加图片。同一个EntityId，最大支持10张图。
        :type EntityId: str
        :param PicName: 图片名称，最多支持64个字符， 
PicName唯一确定一张图片，具有唯一性。
        :type PicName: str
        :param ImageUrl: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。  
ImageUrl和ImageBase64必须提供一个，如果都提供，只使用ImageUrl。
图片限制：
• 图片格式：支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
• 图片大小：对应图片 base64 编码后大小不可超过5M。图片分辨率不超过4096\*4096。
• 如果在商品图像搜索中开启主体识别，分辨率不超过2000\*2000，图片长宽比小于10。
建议：
• 图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的Url速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param CustomContent: 图片自定义备注内容，最多支持4096个字符，查询时原样带回。
        :type CustomContent: str
        :param ImageBase64: 图片 base64 数据，base64 编码后大小不可超过5M。 
图片限制：
• 图片格式：支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
• 图片大小：base64 编码后大小不可超过5M。图片分辨率不超过4096\*4096。
• 如果在商品图像搜索中开启主体识别，分辨率不超过2000\*2000，图片长宽比小于10。
        :type ImageBase64: str
        :param Tags: 图片自定义标签，最多不超过10个，格式为JSON。
        :type Tags: str
        :param EnableDetect: 是否需要启用主体识别，默认为**TRUE**。
• 为**TRUE**时，启用主体识别，返回主体信息。若没有指定**ImageRect**，自动提取最大面积主体创建图片并进行主体识别。主体识别结果可在**Response**中获取。
• 为**FALSE**时，不启用主体识别，不返回主体信息。若没有指定**ImageRect**，以整张图创建图片。
**<font color=#1E90FF>注意：仅服务类型为商品图像搜索时才生效。</font>**
        :type EnableDetect: bool
        :param CategoryId: 图像类目ID。
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
        :param ImageRect: 图像主体区域。
若设置主体区域，提取指定的区域创建图片。
        :type ImageRect: :class:`tencentcloud.tiia.v20190529.models.Rect`
        """
        self.GroupId = None
        self.EntityId = None
        self.PicName = None
        self.ImageUrl = None
        self.CustomContent = None
        self.ImageBase64 = None
        self.Tags = None
        self.EnableDetect = None
        self.CategoryId = None
        self.ImageRect = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.EntityId = params.get("EntityId")
        self.PicName = params.get("PicName")
        self.ImageUrl = params.get("ImageUrl")
        self.CustomContent = params.get("CustomContent")
        self.ImageBase64 = params.get("ImageBase64")
        self.Tags = params.get("Tags")
        self.EnableDetect = params.get("EnableDetect")
        self.CategoryId = params.get("CategoryId")
        if params.get("ImageRect") is not None:
            self.ImageRect = Rect()
            self.ImageRect._deserialize(params.get("ImageRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    """CreateImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Object: 输入图的主体信息。
若启用主体识别且在请求中指定了类目ID或主体区域，以指定的主体为准。若启用主体识别且没有指定，以最大面积主体为准。
**<font color=#1E90FF>注意：仅服务类型为商品图像搜索时才生效。</font>**
注意：此字段可能返回 null，表示取不到有效值。
        :type Object: :class:`tencentcloud.tiia.v20190529.models.ObjectInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Object = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Object") is not None:
            self.Object = ObjectInfo()
            self.Object._deserialize(params.get("Object"))
        self.RequestId = params.get("RequestId")


class CropImageRequest(AbstractModel):
    """CropImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param Width: 需要裁剪区域的宽度，与Height共同组成所需裁剪的图片宽高比例。
输入数字请大于0、小于图片宽度的像素值。
        :type Width: int
        :param Height: 需要裁剪区域的高度，与Width共同组成所需裁剪的图片宽高比例。
输入数字请大于0、小于图片高度的像素值。
宽高比例（Width : Height）会简化为最简分数，即如果Width输入10、Height输入20，会简化为1：2。
Width : Height建议取值在[1, 2.5]之间，超过这个范围可能会影响效果。
        :type Height: int
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果。
• 长宽比：长边：短边<5。 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过Base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
注意：图片需要Base64编码，并且要去掉编码头部。
        :type ImageBase64: str
        """
        self.Width = None
        self.Height = None
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CropImageResponse(AbstractModel):
    """CropImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param X: 裁剪区域左上角X坐标值
        :type X: int
        :param Y: 裁剪区域左上角Y坐标值
        :type Y: int
        :param Width: 裁剪区域的宽度，单位为像素
        :type Width: int
        :param Height: 裁剪区域的高度，单位为像素
        :type Height: int
        :param OriginalWidth: 原图宽度，单位为像素
        :type OriginalWidth: int
        :param OriginalHeight: 原图高度，单位为像素
        :type OriginalHeight: int
        :param CropResult: 0：抠图正常；
1：原图过长，指原图的高度是宽度的1.8倍以上；
2：原图过宽，指原图的宽度是高度的1.8倍以上；
3：抠图区域过长，指抠图的高度是主体备选框高度的1.6倍以上；
4：抠图区域过宽，指当没有检测到人脸时，抠图区域宽度是检测出的原图主体区域宽度的1.6倍以上；
5：纯色图，指裁剪区域视觉较为单一、缺乏主体部分 ；
6：宽高比异常，指Width : Height取值超出[1, 2.5]的范围；

以上是辅助决策的参考建议，可以根据业务需求选择采纳或忽视。
        :type CropResult: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.OriginalWidth = None
        self.OriginalHeight = None
        self.CropResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.OriginalWidth = params.get("OriginalWidth")
        self.OriginalHeight = params.get("OriginalHeight")
        self.CropResult = params.get("CropResult")
        self.RequestId = params.get("RequestId")


class DeleteImagesRequest(AbstractModel):
    """DeleteImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 图库名称。
        :type GroupId: str
        :param EntityId: 物品ID。
        :type EntityId: str
        :param PicName: 图片名称，如果不指定本参数，则删除EntityId下所有的图片；否则删除指定的图。
        :type PicName: str
        """
        self.GroupId = None
        self.EntityId = None
        self.PicName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.EntityId = params.get("EntityId")
        self.PicName = params.get("PicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImagesResponse(AbstractModel):
    """DeleteImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeGroupsRequest(AbstractModel):
    """DescribeGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 起始序号，默认值为0。
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为100。
        :type Limit: int
        :param GroupId: 图库ID，如果不为空，则返回指定库信息。
        :type GroupId: str
        """
        self.Offset = None
        self.Limit = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupsResponse(AbstractModel):
    """DescribeGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param Groups: 图库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of GroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 图库名称。
        :type GroupId: str
        :param EntityId: 物品ID。
        :type EntityId: str
        :param PicName: 图片名称。
        :type PicName: str
        """
        self.GroupId = None
        self.EntityId = None
        self.PicName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.EntityId = params.get("EntityId")
        self.PicName = params.get("PicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 图库名称。
        :type GroupId: str
        :param EntityId: 物品ID。
        :type EntityId: str
        :param ImageInfos: 图片信息。
        :type ImageInfos: list of ImageInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.EntityId = None
        self.ImageInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.EntityId = params.get("EntityId")
        if params.get("ImageInfos") is not None:
            self.ImageInfos = []
            for item in params.get("ImageInfos"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.ImageInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DetectChefDressRequest(AbstractModel):
    """DetectChefDress请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片的 Url 。
ImageUrl和ImageBase64必须提供一个，同时存在时优先使用ImageUrl字段。
图片限制：
• 图片格式：支持PNG、JPG、JPEG、不支持 GIF 图片。
• 图片大小：对应图片 base64 编码后大小不可超过5M。图片分辨率不超过 3840 x 2160pixel。
建议：
• 接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。与ImageUrl同时存在时优先使用ImageUrl字段。
注意：图片需要base64编码，并且要去掉编码头部。
支持的图片格式：PNG、JPG、JPEG、暂不支持GIF格式。
支持的图片大小：所下载图片经Base64编码后不超过5M。
        :type ImageBase64: str
        :param EnableDetect: 人体检测模型开关，“true”为开启，“false”为关闭
默认为开启，开启后可先对图片中的人体进行检测之后再进行属性识别
        :type EnableDetect: bool
        :param EnablePreferred: 人体优选开关，“true”为开启，“false”为关闭
开启后自动对检测质量低的人体进行优选过滤，有助于提高属性识别的准确率。
默认为开启，仅在人体检测开关开启时可配置，人体检测模型关闭时人体优选也关闭
人体优选开启时，检测到的人体分辨率不超过1920*1080 pixel
        :type EnablePreferred: bool
        """
        self.ImageUrl = None
        self.ImageBase64 = None
        self.EnableDetect = None
        self.EnablePreferred = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.EnableDetect = params.get("EnableDetect")
        self.EnablePreferred = params.get("EnablePreferred")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectChefDressResponse(AbstractModel):
    """DetectChefDress返回参数结构体

    """

    def __init__(self):
        r"""
        :param Bodies: 识别到的人体属性信息。单个人体属性信息包括人体检测置信度，属性信息，人体检测框。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bodies: list of AttributesForBody
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Bodies = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Bodies") is not None:
            self.Bodies = []
            for item in params.get("Bodies"):
                obj = AttributesForBody()
                obj._deserialize(item)
                self.Bodies.append(obj)
        self.RequestId = params.get("RequestId")


class DetectDisgustRequest(AbstractModel):
    """DetectDisgust请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
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
        


class DetectDisgustResponse(AbstractModel):
    """DetectDisgust返回参数结构体

    """

    def __init__(self):
        r"""
        :param Confidence: 对于图片中包含恶心内容的置信度，取值[0,1]，一般超过0.5则表明可能是恶心图片。
        :type Confidence: float
        :param Type: 与图像内容最相似的恶心内容的类别，包含腐烂、密集、畸形、血腥、蛇、虫子、牙齿等。
        :type Type: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Confidence = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class DetectEnvelopeRequest(AbstractModel):
    """DetectEnvelope请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片的URL地址。图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
图片大小的限制为4M，图片像素的限制为4k。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。与ImageUrl同时存在时优先使用ImageUrl字段。 
图片大小的限制为4M，图片像素的限制为4k。
**注意：图片需要base64编码，并且要去掉编码头部。
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
        


class DetectEnvelopeResponse(AbstractModel):
    """DetectEnvelope返回参数结构体

    """

    def __init__(self):
        r"""
        :param FirstTags: 一级标签结果数组。识别是否文件封。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstTags: list of ImageTag
        :param SecondTags: 二级标签结果数组。识别文件封正反面。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondTags: list of ImageTag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FirstTags = None
        self.SecondTags = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FirstTags") is not None:
            self.FirstTags = []
            for item in params.get("FirstTags"):
                obj = ImageTag()
                obj._deserialize(item)
                self.FirstTags.append(obj)
        if params.get("SecondTags") is not None:
            self.SecondTags = []
            for item in params.get("SecondTags"):
                obj = ImageTag()
                obj._deserialize(item)
                self.SecondTags.append(obj)
        self.RequestId = params.get("RequestId")


class DetectLabelBetaRequest(AbstractModel):
    """DetectLabelBeta请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
        :type ImageBase64: str
        :param Scenes: 本次调用支持的识别场景，可选值如下：
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
        self.ImageUrl = None
        self.ImageBase64 = None
        self.Scenes = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.Scenes = params.get("Scenes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectLabelBetaResponse(AbstractModel):
    """DetectLabelBeta返回参数结构体

    """

    def __init__(self):
        r"""
        :param Labels: Web网络版标签结果数组。如未选择WEB场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DetectLabelItem
        :param CameraLabels: Camera摄像头版标签结果数组。如未选择CAMERA场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CameraLabels: list of DetectLabelItem
        :param AlbumLabels: Album相册版标签结果数组。如未选择ALBUM场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumLabels: list of DetectLabelItem
        :param NewsLabels: News新闻版标签结果数组。如未选择NEWS场景，则为空。
新闻版目前为测试阶段，暂不提供每个标签的一级、二级分类信息的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type NewsLabels: list of DetectLabelItem
        :param NoneCamLabels: 非实拍标签
注意：此字段可能返回 null，表示取不到有效值。
        :type NoneCamLabels: list of DetectLabelItem
        :param LocationLabels: 识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationLabels: list of Product
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Labels = None
        self.CameraLabels = None
        self.AlbumLabels = None
        self.NewsLabels = None
        self.NoneCamLabels = None
        self.LocationLabels = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("CameraLabels") is not None:
            self.CameraLabels = []
            for item in params.get("CameraLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.CameraLabels.append(obj)
        if params.get("AlbumLabels") is not None:
            self.AlbumLabels = []
            for item in params.get("AlbumLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.AlbumLabels.append(obj)
        if params.get("NewsLabels") is not None:
            self.NewsLabels = []
            for item in params.get("NewsLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.NewsLabels.append(obj)
        if params.get("NoneCamLabels") is not None:
            self.NoneCamLabels = []
            for item in params.get("NoneCamLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.NoneCamLabels.append(obj)
        if params.get("LocationLabels") is not None:
            self.LocationLabels = []
            for item in params.get("LocationLabels"):
                obj = Product()
                obj._deserialize(item)
                self.LocationLabels.append(obj)
        self.RequestId = params.get("RequestId")


class DetectLabelItem(AbstractModel):
    """图像标签检测结果。

    """

    def __init__(self):
        r"""
        :param Name: 图片中的物体名称。
        :type Name: str
        :param Confidence: 算法对于Name的置信度，0-100之间，值越高，表示对于Name越确定。
        :type Confidence: int
        :param FirstCategory: 标签的一级分类
        :type FirstCategory: str
        :param SecondCategory: 标签的二级分类
        :type SecondCategory: str
        """
        self.Name = None
        self.Confidence = None
        self.FirstCategory = None
        self.SecondCategory = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Confidence = params.get("Confidence")
        self.FirstCategory = params.get("FirstCategory")
        self.SecondCategory = params.get("SecondCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectLabelProRequest(AbstractModel):
    """DetectLabelPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片 URL 地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG、BMP。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边:短边<5； 
• 接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片 Base64 编码数据。
与ImageUrl同时存在时优先使用ImageUrl字段。
图片限制：
• 图片格式：PNG、JPG、JPEG、BMP。 
• 图片大小：经Base64编码后不超过4M。
**<font color=#1E90FF>注意：图片需要Base64编码，并且要去掉编码头部。</font>**
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
        


class DetectLabelProResponse(AbstractModel):
    """DetectLabelPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param Labels: 返回标签数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DetectLabelItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Labels = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.RequestId = params.get("RequestId")


class DetectLabelRequest(AbstractModel):
    """DetectLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 图片 Base64 编码数据。
与ImageUrl同时存在时优先使用ImageUrl字段。
图片限制：
• 图片格式：PNG、JPG、JPEG、BMP。 
• 图片大小：经Base64编码后不超过4M。
**<font color=#1E90FF>注意：图片需要Base64编码，并且要去掉编码头部。</font>**
        :type ImageBase64: str
        :param ImageUrl: 图片 URL 地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG、BMP。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边:短边<5； 
• 接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param Scenes: 本次调用支持的识别场景，可选值如下：
• WEB，针对网络图片优化;
• CAMERA，针对手机摄像头拍摄图片优化;
• ALBUM，针对手机相册、网盘产品优化;
• NEWS，针对新闻、资讯、广电等行业优化；
如果不传此参数，则默认为WEB。

支持多场景（Scenes）一起检测。例如，使用 Scenes=["WEB", "CAMERA"]，即对一张图片使用两个模型同时检测，输出两套识别结果。
        :type Scenes: list of str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Scenes = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Scenes = params.get("Scenes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectLabelResponse(AbstractModel):
    """DetectLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param Labels: Web网络版标签结果数组。如未选择WEB场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DetectLabelItem
        :param CameraLabels: Camera摄像头版标签结果数组。如未选择CAMERA场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CameraLabels: list of DetectLabelItem
        :param AlbumLabels: Album相册版标签结果数组。如未选择ALBUM场景，则为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumLabels: list of DetectLabelItem
        :param NewsLabels: News新闻版标签结果数组。如未选择NEWS场景，则为空。
新闻版目前为测试阶段，暂不提供每个标签的一级、二级分类信息的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type NewsLabels: list of DetectLabelItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Labels = None
        self.CameraLabels = None
        self.AlbumLabels = None
        self.NewsLabels = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("CameraLabels") is not None:
            self.CameraLabels = []
            for item in params.get("CameraLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.CameraLabels.append(obj)
        if params.get("AlbumLabels") is not None:
            self.AlbumLabels = []
            for item in params.get("AlbumLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.AlbumLabels.append(obj)
        if params.get("NewsLabels") is not None:
            self.NewsLabels = []
            for item in params.get("NewsLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.NewsLabels.append(obj)
        self.RequestId = params.get("RequestId")


class DetectMisbehaviorRequest(AbstractModel):
    """DetectMisbehavior请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
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
        


class DetectMisbehaviorResponse(AbstractModel):
    """DetectMisbehavior返回参数结构体

    """

    def __init__(self):
        r"""
        :param Confidence: 对于图片中包含不良行为的置信度，取值[0,1]，一般超过0.5则表明可能包含不良行为内容；
        :type Confidence: float
        :param Type: 图像中最可能包含的不良行为类别，包括赌博、打架斗殴、吸毒等。
        :type Type: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Confidence = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class DetectPetRequest(AbstractModel):
    """DetectPet请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片的URL地址。图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
图片大小的限制为4M，图片像素的限制为4k。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。与ImageUrl同时存在时优先使用ImageUrl字段。 
图片大小的限制为4M，图片像素的限制为4k。
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
        


class DetectPetResponse(AbstractModel):
    """DetectPet返回参数结构体

    """

    def __init__(self):
        r"""
        :param Pets: 识别出图片中的宠物信息列表。
        :type Pets: list of Pet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Pets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Pets") is not None:
            self.Pets = []
            for item in params.get("Pets"):
                obj = Pet()
                obj._deserialize(item)
                self.Pets.append(obj)
        self.RequestId = params.get("RequestId")


class DetectProductBetaRequest(AbstractModel):
    """DetectProductBeta请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片限制：内测版仅支持jpg、jpeg，图片大小不超过1M，分辨率在25万到100万之间。 
建议先对图片进行压缩，以便提升处理速度。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过1M，分辨率在25万到100万之间。 
与ImageUrl同时存在时优先使用ImageUrl字段。
        :type ImageBase64: str
        :param NeedLemma: 是否需要百科信息 1：是，0: 否，默认是0
        :type NeedLemma: int
        """
        self.ImageUrl = None
        self.ImageBase64 = None
        self.NeedLemma = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.NeedLemma = params.get("NeedLemma")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectProductBetaResponse(AbstractModel):
    """DetectProductBeta返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegionDetected: 检测到的图片中的商品位置和品类预测。 
当图片中存在多个商品时，输出多组坐标，按照__显著性__排序（综合考虑面积、是否在中心、检测算法置信度）。 
最多可以输出__3组__检测结果。
        :type RegionDetected: list of RegionDetected
        :param ProductInfo: 图像识别出的商品的详细信息。 
当图像中检测到多个物品时，会对显著性最高的进行识别。
        :type ProductInfo: :class:`tencentcloud.tiia.v20190529.models.ProductInfo`
        :param ProductInfoList: 相似商品信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductInfoList: list of ProductInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionDetected = None
        self.ProductInfo = None
        self.ProductInfoList = None
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
        if params.get("ProductInfoList") is not None:
            self.ProductInfoList = []
            for item in params.get("ProductInfoList"):
                obj = ProductInfo()
                obj._deserialize(item)
                self.ProductInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DetectProductRequest(AbstractModel):
    """DetectProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
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
        


class DetectProductResponse(AbstractModel):
    """DetectProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param Products: 商品识别结果数组
        :type Products: list of Product
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = Product()
                obj._deserialize(item)
                self.Products.append(obj)
        self.RequestId = params.get("RequestId")


class DetectSecurityRequest(AbstractModel):
    """DetectSecurity请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片的 Url 。
ImageUrl和ImageBase64必须提供一个，同时存在时优先使用ImageUrl字段。
图片限制：
• 图片格式：支持PNG、JPG、JPEG、不支持 GIF 图片。
• 图片大小：对应图片 base64 编码后大小不可超过5M。图片分辨率不超过3840 x 2160 pixel。
建议：
• 接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。
最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
注意：图片需要base64编码，并且要去掉编码头部。
支持的图片格式：PNG、JPG、JPEG、暂不支持GIF格式。
支持的图片大小：所下载图片经Base64编码后不超过5M。
        :type ImageBase64: str
        :param EnableDetect: 人体检测模型开关，“true”为开启，“false”为关闭
开启后可先对图片中的人体进行检测之后再进行属性识别，默认为开启
        :type EnableDetect: bool
        :param EnablePreferred: 人体优选开关，“true”为开启，“false”为关闭
开启后自动对检测质量低的人体进行优选过滤，有助于提高属性识别的准确率。
默认为开启，仅在人体检测开关开启时可配置，人体检测模型关闭时人体优选也关闭
如开启人体优选，检测到的人体分辨率需不大于1920*1080 pixel
        :type EnablePreferred: bool
        """
        self.ImageUrl = None
        self.ImageBase64 = None
        self.EnableDetect = None
        self.EnablePreferred = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.EnableDetect = params.get("EnableDetect")
        self.EnablePreferred = params.get("EnablePreferred")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectSecurityResponse(AbstractModel):
    """DetectSecurity返回参数结构体

    """

    def __init__(self):
        r"""
        :param Bodies: 识别到的人体属性信息。单个人体属性信息包括人体检测置信度，属性信息，人体检测框。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bodies: list of AttributesForBody
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Bodies = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Bodies") is not None:
            self.Bodies = []
            for item in params.get("Bodies"):
                obj = AttributesForBody()
                obj._deserialize(item)
                self.Bodies.append(obj)
        self.RequestId = params.get("RequestId")


class EnhanceImageRequest(AbstractModel):
    """EnhanceImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，最大不超过250万像素，否则影响识别效果。 
• 长宽比：长边：短边<5。 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。图片经过Base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
注意：图片需要Base64编码，并且要去掉编码头部。
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
        


class EnhanceImageResponse(AbstractModel):
    """EnhanceImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param EnhancedImage: 增强后图片的base64编码。
        :type EnhancedImage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnhancedImage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnhancedImage = params.get("EnhancedImage")
        self.RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    """图库信息。

    """

    def __init__(self):
        r"""
        :param GroupId: 图库Id。
        :type GroupId: str
        :param GroupName: 图库名称。
        :type GroupName: str
        :param Brief: 图库简介。
        :type Brief: str
        :param MaxCapacity: 图库容量。
        :type MaxCapacity: int
        :param MaxQps: 该库的访问限频 。
        :type MaxQps: int
        :param GroupType: 图库类型，对应不同服务类型，默认为1。建议手动调整为4～6，1～3为历史版本，不推荐。
参数值：
4：在自建图库中搜索相同原图，可支持裁剪、翻转、调色、加水印后的图片搜索，适用于图片版权保护、原图查询等场景。
5：在自建图库中搜索相同或相似的商品图片，适用于商品分类、检索、推荐等电商场景。
6：在自建图片库中搜索与输入图片高度相似的图片，适用于相似图案、logo、纹理等图像元素的搜索。
        :type GroupType: int
        :param PicCount: 图库图片数量。
        :type PicCount: int
        :param CreateTime: 图库创建时间。
        :type CreateTime: str
        :param UpdateTime: 图库更新时间。
        :type UpdateTime: str
        """
        self.GroupId = None
        self.GroupName = None
        self.Brief = None
        self.MaxCapacity = None
        self.MaxQps = None
        self.GroupType = None
        self.PicCount = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Brief = params.get("Brief")
        self.MaxCapacity = params.get("MaxCapacity")
        self.MaxQps = params.get("MaxQps")
        self.GroupType = params.get("GroupType")
        self.PicCount = params.get("PicCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    """图片信息

    """

    def __init__(self):
        r"""
        :param EntityId: 图片名称。
        :type EntityId: str
        :param CustomContent: 用户自定义的内容。
        :type CustomContent: str
        :param Tags: 图片自定义标签，JSON格式。
        :type Tags: str
        :param PicName: 图片名称。
        :type PicName: str
        :param Score: 相似度。
        :type Score: int
        """
        self.EntityId = None
        self.CustomContent = None
        self.Tags = None
        self.PicName = None
        self.Score = None


    def _deserialize(self, params):
        self.EntityId = params.get("EntityId")
        self.CustomContent = params.get("CustomContent")
        self.Tags = params.get("Tags")
        self.PicName = params.get("PicName")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRect(AbstractModel):
    """图像主体区域坐标

    """

    def __init__(self):
        r"""
        :param X: 左上角横坐标。
        :type X: int
        :param Y: 左上角纵坐标。
        :type Y: int
        :param Width: 宽度。
        :type Width: int
        :param Height: 高度。
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTag(AbstractModel):
    """图片标签。

    """

    def __init__(self):
        r"""
        :param Name: 标签内容。
        :type Name: str
        :param Confidence: 置信度范围在0-100之间。值越高，表示目标为相应结果的可能性越高。
        :type Confidence: float
        """
        self.Name = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LemmaInfo(AbstractModel):
    """百科词条信息

    """

    def __init__(self):
        r"""
        :param LemmaTitle: 词条
注意：此字段可能返回 null，表示取不到有效值。
        :type LemmaTitle: str
        :param LemmaAbstract: 词条描述
注意：此字段可能返回 null，表示取不到有效值。
        :type LemmaAbstract: str
        :param Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        """
        self.LemmaTitle = None
        self.LemmaAbstract = None
        self.Tag = None


    def _deserialize(self, params):
        self.LemmaTitle = params.get("LemmaTitle")
        self.LemmaAbstract = params.get("LemmaAbstract")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class ObjectInfo(AbstractModel):
    """图像的主体信息。

    """

    def __init__(self):
        r"""
        :param Box: 图像主体区域。
        :type Box: :class:`tencentcloud.tiia.v20190529.models.Box`
        :param CategoryId: 主体类别ID。
        :type CategoryId: int
        :param Colors: 整张图颜色信息。
        :type Colors: list of ColorInfo
        :param Attributes: 属性信息。
        :type Attributes: list of Attribute
        :param AllBox: 图像的所有主体区域，置信度，以及主体区域类别ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllBox: list of Box
        """
        self.Box = None
        self.CategoryId = None
        self.Colors = None
        self.Attributes = None
        self.AllBox = None


    def _deserialize(self, params):
        if params.get("Box") is not None:
            self.Box = Box()
            self.Box._deserialize(params.get("Box"))
        self.CategoryId = params.get("CategoryId")
        if params.get("Colors") is not None:
            self.Colors = []
            for item in params.get("Colors"):
                obj = ColorInfo()
                obj._deserialize(item)
                self.Colors.append(obj)
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = Attribute()
                obj._deserialize(item)
                self.Attributes.append(obj)
        if params.get("AllBox") is not None:
            self.AllBox = []
            for item in params.get("AllBox"):
                obj = Box()
                obj._deserialize(item)
                self.AllBox.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pet(AbstractModel):
    """宠物具体信息

    """

    def __init__(self):
        r"""
        :param Name: 识别出的宠物类型（猫或者狗，暂不支持识别猫狗品种）。
        :type Name: str
        :param Score: 识别服务给识别目标打出的置信度，范围在0-100之间。值越高，表示目标为相应结果的可能性越高。
        :type Score: int
        :param Location: 识别目标在图片中的坐标。
        :type Location: :class:`tencentcloud.tiia.v20190529.models.Rect`
        """
        self.Name = None
        self.Score = None
        self.Location = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Score = params.get("Score")
        if params.get("Location") is not None:
            self.Location = Rect()
            self.Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Product(AbstractModel):
    """检测到的单个商品结构体

    """

    def __init__(self):
        r"""
        :param Name: 图片中商品的三级分类识别结果，选取所有三级分类中的置信度最大者
        :type Name: str
        :param Parents: 三级商品分类对应的一级分类和二级分类，两级之间用“-”（中划线）隔开，例如商品名称是“硬盘”，那么Parents输出为“电脑、办公-电脑配件”
        :type Parents: str
        :param Confidence: 算法对于Name的置信度，0-100之间，值越高，表示对于Name越确定
        :type Confidence: int
        :param XMin: 商品坐标X轴的最小值
        :type XMin: int
        :param YMin: 商品坐标Y轴的最小值
        :type YMin: int
        :param XMax: 商品坐标X轴的最大值
        :type XMax: int
        :param YMax: 商品坐标Y轴的最大值
        :type YMax: int
        """
        self.Name = None
        self.Parents = None
        self.Confidence = None
        self.XMin = None
        self.YMin = None
        self.XMax = None
        self.YMax = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Parents = params.get("Parents")
        self.Confidence = params.get("Confidence")
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
0表示未找到同款商品， 具体商品信息为空（参考价格、名称、品牌等），仅提供商品类目和参考图片（商品库中找到的最相似图片，供参考）。  
是否找到同款的判断依据为Score分值，分值越大则同款的可能性越大。
        :type FindSKU: int
        :param Location: 本商品在图片中的坐标，表示为矩形框的四个顶点坐标。
        :type Location: :class:`tencentcloud.tiia.v20190529.models.Location`
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
        :param Image: 搜索到的商品配图URL。
        :type Image: str
        :param LemmaInfoList: 百科词条列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LemmaInfoList: list of LemmaInfo
        """
        self.FindSKU = None
        self.Location = None
        self.Name = None
        self.Brand = None
        self.Price = None
        self.ProductCategory = None
        self.Score = None
        self.Image = None
        self.LemmaInfoList = None


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
        if params.get("LemmaInfoList") is not None:
            self.LemmaInfoList = []
            for item in params.get("LemmaInfoList"):
                obj = LemmaInfo()
                obj._deserialize(item)
                self.LemmaInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeCarProRequest(AbstractModel):
    """RecognizeCarPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
支持的图片格式：PNG、JPG、JPEG、BMP，暂不支持GIF格式。支持的图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。
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
        


class RecognizeCarProResponse(AbstractModel):
    """RecognizeCarPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param CarCoords: 汽车的四个矩形顶点坐标，如果图片中存在多辆车，则输出最大车辆的坐标。
        :type CarCoords: list of Coord
        :param CarTags: 车辆属性识别的结果数组，如果识别到多辆车，则会输出每辆车的top1结果。
注意：置信度是指车牌信息置信度。
        :type CarTags: list of CarTagItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CarCoords = None
        self.CarTags = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CarCoords") is not None:
            self.CarCoords = []
            for item in params.get("CarCoords"):
                obj = Coord()
                obj._deserialize(item)
                self.CarCoords.append(obj)
        if params.get("CarTags") is not None:
            self.CarTags = []
            for item in params.get("CarTags"):
                obj = CarTagItem()
                obj._deserialize(item)
                self.CarTags.append(obj)
        self.RequestId = params.get("RequestId")


class RecognizeCarRequest(AbstractModel):
    """RecognizeCar请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageUrl: 图片URL地址。 
图片限制： 
• 图片格式：PNG、JPG、JPEG。 
• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
建议：
• 图片像素：大于50*50像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
**注意：图片需要base64编码，并且要去掉编码头部。**
支持的图片格式：PNG、JPG、JPEG、BMP，暂不支持GIF格式。支持的图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。
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
        


class RecognizeCarResponse(AbstractModel):
    """RecognizeCar返回参数结构体

    """

    def __init__(self):
        r"""
        :param CarCoords: 汽车的四个矩形顶点坐标，如果图片中存在多辆车，则输出最大车辆的坐标。
        :type CarCoords: list of Coord
        :param CarTags: 车辆属性识别的结果数组，如果识别到多辆车，则会输出每辆车的top1结果。
        :type CarTags: list of CarTagItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CarCoords = None
        self.CarTags = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CarCoords") is not None:
            self.CarCoords = []
            for item in params.get("CarCoords"):
                obj = Coord()
                obj._deserialize(item)
                self.CarCoords.append(obj)
        if params.get("CarTags") is not None:
            self.CarTags = []
            for item in params.get("CarTags"):
                obj = CarTagItem()
                obj._deserialize(item)
                self.CarTags.append(obj)
        self.RequestId = params.get("RequestId")


class Rect(AbstractModel):
    """具体坐标，可用来判断边界

    """

    def __init__(self):
        r"""
        :param X: x轴坐标
        :type X: int
        :param Y: y轴坐标
        :type Y: int
        :param Width: (x,y)坐标距离长度
        :type Width: int
        :param Height: (x,y)坐标距离高度
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :type Location: :class:`tencentcloud.tiia.v20190529.models.Location`
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
        


class SearchImageRequest(AbstractModel):
    """SearchImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 图库名称。
        :type GroupId: str
        :param ImageUrl: 图片的 Url 。
ImageUrl和ImageBase64必须提供一个，如果都提供，只使用ImageUrl。
图片限制：
• 图片格式：支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
• 图片大小：对应图片 base64 编码后大小不可超过5M。图片分辨率不超过4096\*4096。
• 如果在商品图像搜索中开启主体识别，分辨率不超过2000\*2000，图片长宽比小于10。
建议：
• 图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的Url速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param ImageBase64: 图片 base64 数据。
ImageUrl和ImageBase64必须提供一个，如果都提供，只使用ImageUrl。
图片限制：
• 图片格式：支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
• 图片大小：base64 编码后大小不可超过5M。图片分辨率不超过4096\*4096。
• 如果在商品图像搜索中开启主体识别，分辨率不超过2000\*2000，图片长宽比小于10。
        :type ImageBase64: str
        :param Limit: 返回结果的数量，默认值为10，最大值为100。
按照相似度分数由高到低排序。
**<font color=#1E90FF>注意：服务类型为相似图像搜索时返回数量限制为1，即返回top1的结果。</font>**
        :type Limit: int
        :param Offset: 返回结果的起始序号，默认值为0。
        :type Offset: int
        :param MatchThreshold: 匹配阈值。
只有图片相似度分数超过MatchThreshold值的结果才会返回。
默认值：
• 相同图像搜索：50。
• 商品图像搜索：28。
• 相似图像搜索：56。
建议：
可以手动调整MatchThreshold值来控制输出结果的范围。如果发现无检索结果，建议调整为较低的阈值。
        :type MatchThreshold: int
        :param Filter: 标签过滤条件。
针对创建图片时提交的Tags信息进行条件过滤。支持>、>=、 <、 <=、=，!=，多个条件之间支持AND和OR进行连接。
        :type Filter: str
        :param ImageRect: 图像主体区域。
若设置主体区域，提取指定的区域进行检索。
        :type ImageRect: :class:`tencentcloud.tiia.v20190529.models.ImageRect`
        :param EnableDetect: 是否需要启用主体识别，默认为**TRUE** 。
• 为**TRUE**时，启用主体识别，返回主体信息。若没有指定**ImageRect**，自动提取最大面积主体进行检索并进行主体识别。主体识别结果可在**Response中**获取。
• 为**FALSE**时，不启用主体识别，不返回主体信息。若没有指定**ImageRect**，以整张图检索图片。
**<font color=#1E90FF>注意：仅服务类型为商品图像搜索时才生效。</font>**
        :type EnableDetect: bool
        :param CategoryId: 图像类目ID。
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
        self.GroupId = None
        self.ImageUrl = None
        self.ImageBase64 = None
        self.Limit = None
        self.Offset = None
        self.MatchThreshold = None
        self.Filter = None
        self.ImageRect = None
        self.EnableDetect = None
        self.CategoryId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.MatchThreshold = params.get("MatchThreshold")
        self.Filter = params.get("Filter")
        if params.get("ImageRect") is not None:
            self.ImageRect = ImageRect()
            self.ImageRect._deserialize(params.get("ImageRect"))
        self.EnableDetect = params.get("EnableDetect")
        self.CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchImageResponse(AbstractModel):
    """SearchImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 返回结果数量。
        :type Count: int
        :param ImageInfos: 图片信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfos: list of ImageInfo
        :param Object: 输入图的主体信息。
若启用主体识别且在请求中指定了类目ID或主体区域，以指定的主体为准。若启用主体识别且没有指定，以最大面积主体为准。
**<font color=#1E90FF>注意：仅服务类型为商品图像搜索时才生效。</font>**
注意：此字段可能返回 null，表示取不到有效值。
        :type Object: :class:`tencentcloud.tiia.v20190529.models.ObjectInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.ImageInfos = None
        self.Object = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("ImageInfos") is not None:
            self.ImageInfos = []
            for item in params.get("ImageInfos"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.ImageInfos.append(obj)
        if params.get("Object") is not None:
            self.Object = ObjectInfo()
            self.Object._deserialize(params.get("Object"))
        self.RequestId = params.get("RequestId")