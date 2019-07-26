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

from tencentcloud.common.abstract_model import AbstractModel


class Candidate(AbstractModel):
    """识别出人脸对应的候选人。

    """

    def __init__(self):
        """
        :param Name: 识别出人脸对应的候选人数组。当前返回相似度最高的候选人。
        :type Name: str
        :param Confidence: 相似度，0-100之间。
        :type Confidence: int
        """
        self.Name = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Confidence = params.get("Confidence")


class CarTagItem(AbstractModel):
    """车辆属性识别的结果

    """

    def __init__(self):
        """
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
        """
        self.Serial = None
        self.Brand = None
        self.Type = None
        self.Color = None
        self.Confidence = None
        self.Year = None


    def _deserialize(self, params):
        self.Serial = params.get("Serial")
        self.Brand = params.get("Brand")
        self.Type = params.get("Type")
        self.Color = params.get("Color")
        self.Confidence = params.get("Confidence")
        self.Year = params.get("Year")


class Coord(AbstractModel):
    """汽车坐标信息

    """

    def __init__(self):
        """
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


class DetectLabelItem(AbstractModel):
    """图像标签检测结果。

    """

    def __init__(self):
        """
        :param Name: 图片中的物体名称。
        :type Name: str
        :param Confidence: 算法对于Name的置信度，0-100之间，值越高，表示对于Name越确定。
        :type Confidence: int
        """
        self.Name = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Confidence = params.get("Confidence")


class DetectLabelRequest(AbstractModel):
    """DetectLabel请求参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片的URL地址。
        :type ImageUrl: str
        :param ImageBase64: 图片经过base64编码的内容。与ImageUrl同时存在时优先使用ImageUrl字段。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectLabelResponse(AbstractModel):
    """DetectLabel返回参数结构体

    """

    def __init__(self):
        """
        :param Labels: 标签结果数组。
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


class DetectProductRequest(AbstractModel):
    """DetectProduct请求参数结构体

    """

    def __init__(self):
        """
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
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectProductResponse(AbstractModel):
    """DetectProduct返回参数结构体

    """

    def __init__(self):
        """
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


class DisgustResult(AbstractModel):
    """恶心识别结果。

    """

    def __init__(self):
        """
        :param Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误。
        :type Code: int
        :param Msg: 错误码描述信息。
        :type Msg: str
        :param Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规
        :type Suggestion: str
        :param Confidence: 图像恶心的分数，0-100之间，分数越高恶心几率越大。
        :type Confidence: int
        """
        self.Code = None
        self.Msg = None
        self.Suggestion = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")


class FaceRect(AbstractModel):
    """识别出的人脸在图片中的位置。

    """

    def __init__(self):
        """
        :param X: 人脸区域左上角横坐标。
        :type X: int
        :param Y: 人脸区域左上角纵坐标。
        :type Y: int
        :param Width: 人脸区域宽度。
        :type Width: int
        :param Height: 人脸区域高度。
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


class FaceResult(AbstractModel):
    """人脸识别结果。

    """

    def __init__(self):
        """
        :param FaceRect: 检测出的人脸框位置。
        :type FaceRect: :class:`tencentcloud.tiia.v20190529.models.FaceRect`
        :param Candidates: 候选人列表。当前返回相似度最高的候选人。
        :type Candidates: list of Candidate
        """
        self.FaceRect = None
        self.Candidates = None


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)


class ImageModerationRequest(AbstractModel):
    """ImageModeration请求参数结构体

    """

    def __init__(self):
        """
        :param Scenes: 本次调用支持的识别场景，可选值如下：
1. PORN，即色情识别
2. TERRORISM，即暴恐识别
3. POLITICS，即政治敏感识别

支持多场景（Scenes）一起检测。例如，使用 Scenes=["PORN", "TERRORISM"]，即对一张图片同时进行色情识别和暴恐识别。
        :type Scenes: list of str
        :param ImageUrl: 图片URL地址。 
图片限制： 
 • 图片格式：PNG、JPG、JPEG。 
 • 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
 • 图片像素：大于50*50像素，否则影响识别效果； 
 • 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param Config: 预留字段，后期用于展示更多识别信息。
        :type Config: str
        :param Extra: 透传字段，透传简单信息。
        :type Extra: str
        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
        :type ImageBase64: str
        """
        self.Scenes = None
        self.ImageUrl = None
        self.Config = None
        self.Extra = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.Scenes = params.get("Scenes")
        self.ImageUrl = params.get("ImageUrl")
        self.Config = params.get("Config")
        self.Extra = params.get("Extra")
        self.ImageBase64 = params.get("ImageBase64")


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回参数结构体

    """

    def __init__(self):
        """
        :param Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规
        :type Suggestion: str
        :param PornResult: 色情识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type PornResult: :class:`tencentcloud.tiia.v20190529.models.PornResult`
        :param TerrorismResult: 暴恐识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TerrorismResult: :class:`tencentcloud.tiia.v20190529.models.TerrorismResult`
        :param PoliticsResult: 政治敏感识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type PoliticsResult: :class:`tencentcloud.tiia.v20190529.models.PoliticsResult`
        :param Extra: 透传字段，透传简单信息。
        :type Extra: str
        :param DisgustResult: 恶心内容识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisgustResult: :class:`tencentcloud.tiia.v20190529.models.DisgustResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Suggestion = None
        self.PornResult = None
        self.TerrorismResult = None
        self.PoliticsResult = None
        self.Extra = None
        self.DisgustResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Suggestion = params.get("Suggestion")
        if params.get("PornResult") is not None:
            self.PornResult = PornResult()
            self.PornResult._deserialize(params.get("PornResult"))
        if params.get("TerrorismResult") is not None:
            self.TerrorismResult = TerrorismResult()
            self.TerrorismResult._deserialize(params.get("TerrorismResult"))
        if params.get("PoliticsResult") is not None:
            self.PoliticsResult = PoliticsResult()
            self.PoliticsResult._deserialize(params.get("PoliticsResult"))
        self.Extra = params.get("Extra")
        if params.get("DisgustResult") is not None:
            self.DisgustResult = DisgustResult()
            self.DisgustResult._deserialize(params.get("DisgustResult"))
        self.RequestId = params.get("RequestId")


class PoliticsResult(AbstractModel):
    """政治敏感识别结果。

    """

    def __init__(self):
        """
        :param Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误，
-1400表示图片解码失败，
-1401表示图片不符合规范。
        :type Code: int
        :param Msg: 错误码描述信息。
        :type Msg: str
        :param Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规
        :type Suggestion: str
        :param Confidence: 图像涉政的分数，0-100之间，分数越高涉政几率越大。
Type为DNA时：
0到75，Suggestion建议为PASS
75到90，Suggestion建议为REVIEW
90到100，Suggestion建议为BLOCK
Type为FACE时：
0到55，Suggestion建议为PASS
55到60，Suggestion建议为REVIEW
60到100，Suggestion建议为BLOCK
        :type Confidence: int
        :param FaceResults: Type取值为‘FACE’时，人脸识别的结果列表。基于图片中实际检测到的人脸数，返回数组最大值不超过5个。
        :type FaceResults: list of FaceResult
        :param Type: 取值'DNA' 或‘FACE’。DNA表示结论和置信度来自图像指纹，FACE表示结论和置信度来自人脸识别。
        :type Type: str
        :param AdvancedInfo: 鉴政识别返回的详细标签后期开放。
        :type AdvancedInfo: str
        """
        self.Code = None
        self.Msg = None
        self.Suggestion = None
        self.Confidence = None
        self.FaceResults = None
        self.Type = None
        self.AdvancedInfo = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")
        if params.get("FaceResults") is not None:
            self.FaceResults = []
            for item in params.get("FaceResults"):
                obj = FaceResult()
                obj._deserialize(item)
                self.FaceResults.append(obj)
        self.Type = params.get("Type")
        self.AdvancedInfo = params.get("AdvancedInfo")


class PornResult(AbstractModel):
    """色情识别结果。

    """

    def __init__(self):
        """
        :param Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误，
-1400表示图片解码失败。
        :type Code: int
        :param Msg: 错误码描述信息。
        :type Msg: str
        :param Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规
        :type Suggestion: str
        :param Confidence: 算法对于Suggestion的置信度，0-100之间，值越高，表示对于Suggestion越确定。
        :type Confidence: int
        :param AdvancedInfo: 预留字段，后期用于展示更多识别信息。
        :type AdvancedInfo: str
        :param Type: 取值'LABEL‘，LABEL表示结论和置信度来自标签分类。
        :type Type: str
        """
        self.Code = None
        self.Msg = None
        self.Suggestion = None
        self.Confidence = None
        self.AdvancedInfo = None
        self.Type = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.Type = params.get("Type")


class Product(AbstractModel):
    """检测到的单个商品结构体

    """

    def __init__(self):
        """
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


class RecognizeCarRequest(AbstractModel):
    """RecognizeCar请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 图片的BASE64值；
BASE64编码后的图片数据大小不超过3M，支持PNG、JPG、JPEG、BMP格式，暂不支持GIF格式。
        :type ImageBase64: str
        :param ImageUrl: 图片的 ImageUrl、ImageBase64必须提供一个，如果都提供，只使用ImageUrl。

图片URL地址。支持的图片格式：PNG、JPG、JPEG、BMP，暂不支持GIF格式。支持的图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class RecognizeCarResponse(AbstractModel):
    """RecognizeCar返回参数结构体

    """

    def __init__(self):
        """
        :param CarCoords: 汽车的四个矩形顶点坐标
        :type CarCoords: list of Coord
        :param CarTags: 车辆属性识别的结果数组
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


class TerrorismResult(AbstractModel):
    """暴恐识别结果。

    """

    def __init__(self):
        """
        :param Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误，
-1400表示图片解码失败。
        :type Code: int
        :param Msg: 错误码描述信息。
        :type Msg: str
        :param Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规
        :type Suggestion: str
        :param Confidence: 图像涉恐的分数，0-100之间，分数越高涉恐几率越大。
Type为LABEL时：
0到86，Suggestion建议为PASS
86到91，Suggestion建议为REVIEW
91到100，Suggestion建议为BLOCK
Type为FACE时：
0到55，Suggestion建议为PASS
55到60，Suggestion建议为REVIEW
60到100，Suggestion建议为BLOCK
        :type Confidence: int
        :param FaceResults: Type取值为‘FACE’时，人脸识别的结果列表。基于图片中实际检测到的人脸数，返回数组最大值不超过5个。
        :type FaceResults: list of FaceResult
        :param AdvancedInfo: 暴恐识别返回的详细标签后期开放。
        :type AdvancedInfo: str
        :param Type: 取值'LABEL' 或‘FACE’，LABEL表示结论和置信度来自标签分类，FACE表示结论和置信度来自人脸识别。
        :type Type: str
        """
        self.Code = None
        self.Msg = None
        self.Suggestion = None
        self.Confidence = None
        self.FaceResults = None
        self.AdvancedInfo = None
        self.Type = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")
        if params.get("FaceResults") is not None:
            self.FaceResults = []
            for item in params.get("FaceResults"):
                obj = FaceResult()
                obj._deserialize(item)
                self.FaceResults.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.Type = params.get("Type")