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
        :param Type: 车牌类型；渣土车车牌遮挡时,该值为枚举值“异常”。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param PlateLocation: 车牌在图片中的坐标信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateLocation: list of Coord
        """
        self.Plate = None
        self.Color = None
        self.Type = None
        self.PlateLocation = None


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
        :param Confidence: 置信度，0-100
        :type Confidence: int
        :param Year: 年份，没识别出年份的时候返回0
        :type Year: int
        :param CarLocation: 车辆在图片中的坐标信息
        :type CarLocation: list of Coord
        :param PlateContent: 车牌信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PlateContent: :class:`tencentcloud.tiia.v20190529.models.CarPlateContent`
        """
        self.Serial = None
        self.Brand = None
        self.Type = None
        self.Color = None
        self.Confidence = None
        self.Year = None
        self.CarLocation = None
        self.PlateContent = None


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
        :param MaxCapacity: 该库的容量限制。
        :type MaxCapacity: int
        :param Brief: 简介。
        :type Brief: str
        :param MaxQps: 该库的访问限频 ，默认10。
        :type MaxQps: int
        :param GroupType: 图库类型， 默认为通用。
类型： 
1: 通用图库，以用户输入图提取特征。
2: 灰度图库，输入图和搜索图均转为灰度图提取特征。
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
若EntityId已存在，则对其追加图片。
        :type EntityId: str
        :param PicName: 图片名称，最多支持64个字符， 
同一个EntityId，最大支持5张图。如果图片名称已存在，则会更新库中的图片。
        :type PicName: str
        :param ImageUrl: 图片的 Url 。对应图片 base64 编码后大小不可超过2M。  
Url、Image必须提供一个，如果都提供，只使用 Url。 
图片分辨率不超过1920*1080。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type ImageUrl: str
        :param ImageBase64: 图片 base64 数据，base64 编码后大小不可超过2M。 
图片分辨率不超过1920*1080。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type ImageBase64: str
        :param CustomContent: 用户自定义的内容，最多支持4096个字符，查询时原样带回。
        :type CustomContent: str
        :param Tags: 图片自定义标签，最多不超过10个，格式为JSON。
        :type Tags: str
        """
        self.GroupId = None
        self.EntityId = None
        self.PicName = None
        self.ImageUrl = None
        self.ImageBase64 = None
        self.CustomContent = None
        self.Tags = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.EntityId = params.get("EntityId")
        self.PicName = params.get("PicName")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.CustomContent = params.get("CustomContent")
        self.Tags = params.get("Tags")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CropImageRequest(AbstractModel):
    """CropImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param Width: 需要裁剪区域的宽度，与Height共同组成所需裁剪的图片宽高比例；
输入数字请大于0、小于图片宽度的像素值；
        :type Width: int
        :param Height: 需要裁剪区域的高度，与Width共同组成所需裁剪的图片宽高比例；
输入数字请请大于0、小于图片高度的像素值；
宽高比例（Width : Height）会简化为最简分数，即如果Width输入10、Height输入20，会简化为1：2。
Width : Height建议取值在[1, 2.5]之间，超过这个范围可能会影响效果；
        :type Height: int
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


class DetectCelebrityRequest(AbstractModel):
    """DetectCelebrity请求参数结构体

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
        


class DetectCelebrityResponse(AbstractModel):
    """DetectCelebrity返回参数结构体

    """

    def __init__(self):
        r"""
        :param Faces: 公众人物识别结果数组。如果检测不到人脸，返回为空；最多可以返回10个人脸识别结果。
        :type Faces: list of Face
        :param Threshold: 本服务在不同误识率水平下（将图片中的人物识别错误的比例）的推荐阈值，可以用于控制识别结果的精度。 
FalseRate1Percent, FalseRate5Permil, FalseRate1Permil分别代表误识率在百分之一、千分之五、千分之一情况下的推荐阈值。 
因为阈值会存在变动，请勿将此处输出的固定值处理，而是每次取值与confidence对比，来判断本次的识别结果是否可信。
 例如，如果您业务中可以接受的误识率是1%，则可以将所有confidence>=FalseRate1Percent的结论认为是正确的。
注意：此字段可能返回 null，表示取不到有效值。
        :type Threshold: :class:`tencentcloud.tiia.v20190529.models.Threshold`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Faces = None
        self.Threshold = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Faces") is not None:
            self.Faces = []
            for item in params.get("Faces"):
                obj = Face()
                obj._deserialize(item)
                self.Faces.append(obj)
        if params.get("Threshold") is not None:
            self.Threshold = Threshold()
            self.Threshold._deserialize(params.get("Threshold"))
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
        


class DetectLabelRequest(AbstractModel):
    """DetectLabel请求参数结构体

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
• 图片像素：大于50*50像素，最大不超过250万像素，否则影响识别效果； 
• 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param ImageBase64: 支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
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


class Face(AbstractModel):
    """公众人物识别人脸信息

    """

    def __init__(self):
        r"""
        :param Name: 与图片中人脸最相似的公众人物的名字。
        :type Name: str
        :param Labels: 公众人物身份标签的数组，一个公众人物可能有多个身份标签。
        :type Labels: list of Labels
        :param BasicInfo: 对人物的简介。
        :type BasicInfo: str
        :param Confidence: 算法对于Name的置信度（图像中人脸与公众人物的相似度），0-100之间，值越高，表示对于Name越确定。
        :type Confidence: int
        :param X: 人脸区域左上角横坐标。
        :type X: int
        :param Y: 人脸区域左上角纵坐标。
        :type Y: int
        :param Width: 人脸区域宽度。
        :type Width: int
        :param Height: 人脸区域高度。
        :type Height: int
        :param ID: 公众人物的唯一编号，可以用于区分同名人物、一个人物不同称呼等情况。唯一编号为8个字符构成的字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        """
        self.Name = None
        self.Labels = None
        self.BasicInfo = None
        self.Confidence = None
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.ID = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Labels()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.BasicInfo = params.get("BasicInfo")
        self.Confidence = params.get("Confidence")
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param GroupType: 图库类型： 
1: 通用图库，以用户输入图提取特征。
2: 灰度图库，输入图和搜索图均转为灰度图提取特征。
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
        


class Labels(AbstractModel):
    """名人识别的标签

    """

    def __init__(self):
        r"""
        :param FirstLabel: 公众人物身份标签的一级分类，例如体育明星、娱乐明星、政治人物等；
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstLabel: str
        :param SecondLabel: 公众人物身份标签的二级分类，例如歌手（对应一级标签为“娱乐明星”）；
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondLabel: str
        """
        self.FirstLabel = None
        self.SecondLabel = None


    def _deserialize(self, params):
        self.FirstLabel = params.get("FirstLabel")
        self.SecondLabel = params.get("SecondLabel")
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
        :param ImageUrl: 图片的 Url 。对应图片 base64 编码后大小不可超过2M。 
图片分辨率不超过1920*1080。 
Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type ImageUrl: str
        :param ImageBase64: 图片 base64 数据，base64 编码后大小不可超过2M。 
图片分辨率不超过1920*1080。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type ImageBase64: str
        :param MatchThreshold: 出参Score中，只有超过MatchThreshold值的结果才会返回。默认为0
        :type MatchThreshold: int
        :param Offset: 起始序号，默认值为0。
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为100。
        :type Limit: int
        :param Filter: 针对入库时提交的Tags信息进行条件过滤。支持>、>=、 <、 <=、=，!=，多个条件之间支持AND和OR进行连接。
        :type Filter: str
        """
        self.GroupId = None
        self.ImageUrl = None
        self.ImageBase64 = None
        self.MatchThreshold = None
        self.Offset = None
        self.Limit = None
        self.Filter = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.MatchThreshold = params.get("MatchThreshold")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Filter = params.get("Filter")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.ImageInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("ImageInfos") is not None:
            self.ImageInfos = []
            for item in params.get("ImageInfos"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.ImageInfos.append(obj)
        self.RequestId = params.get("RequestId")


class Threshold(AbstractModel):
    """本服务在不同误识率水平下（将图片中的人物识别错误的比例）的推荐阈值，可以用于控制识别结果的精度。
    {FalseRate1Percent, FalseRate5Permil, FalseRate1Permil}分别代表误识率在百分之一、千分之五、千分之一情况下的推荐阈值。
    因为阈值会存在变动，请勿将此处输出的固定值处理，而是每次取值与confidence对比，来判断本次的识别结果是否可信。
    例如，如果您业务中可以接受的误识率是1%，则可以将所有confidence>=FalseRate1Percent的结论认为是正确的。

    """

    def __init__(self):
        r"""
        :param FalseRate1Percent: 误识率在百分之一时的推荐阈值。
        :type FalseRate1Percent: int
        :param FalseRate5Permil: 误识率在千分之五时的推荐阈值。
        :type FalseRate5Permil: int
        :param FalseRate1Permil: 误识率在千分之一时的推荐阈值。
        :type FalseRate1Permil: int
        """
        self.FalseRate1Percent = None
        self.FalseRate5Permil = None
        self.FalseRate1Permil = None


    def _deserialize(self, params):
        self.FalseRate1Percent = params.get("FalseRate1Percent")
        self.FalseRate5Permil = params.get("FalseRate5Permil")
        self.FalseRate1Permil = params.get("FalseRate1Permil")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        