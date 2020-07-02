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


class BeautifyPicRequest(AbstractModel):
    """BeautifyPic请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。 
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param Whitening: 美白程度，取值范围[0,100]。0不美白，100代表最高程度。默认值30。
        :type Whitening: int
        :param Smoothing: 磨皮程度，取值范围[0,100]。0不磨皮，100代表最高程度。默认值10。
        :type Smoothing: int
        :param FaceLifting: 瘦脸程度，取值范围[0,100]。0不瘦脸，100代表最高程度。默认值70。
        :type FaceLifting: int
        :param EyeEnlarging: 大眼程度，取值范围[0,100]。0不大眼，100代表最高程度。默认值70。
        :type EyeEnlarging: int
        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        """
        self.Image = None
        self.Url = None
        self.Whitening = None
        self.Smoothing = None
        self.FaceLifting = None
        self.EyeEnlarging = None
        self.RspImgType = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.Whitening = params.get("Whitening")
        self.Smoothing = params.get("Smoothing")
        self.FaceLifting = params.get("FaceLifting")
        self.EyeEnlarging = params.get("EyeEnlarging")
        self.RspImgType = params.get("RspImgType")


class BeautifyPicResponse(AbstractModel):
    """BeautifyPic返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
        :type ResultImage: str
        :param ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
        :type ResultUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.ResultUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultUrl = params.get("ResultUrl")
        self.RequestId = params.get("RequestId")


class CreateModelRequest(AbstractModel):
    """CreateModel请求参数结构体

    """

    def __init__(self):
        """
        :param LUTFile: 用于试唇色，要求必须是LUT 格式的cube文件转换成512*512的PNG图片。查看 [LUT文件的使用说明](https://cloud.tencent.com/document/product/1172/41701)。了解 [cube文件转png图片小工具](http://yyb.gtimg.com/aiplat/static/qcloud-cube-to-png.html)。
        :type LUTFile: str
        :param Description: 文件描述信息，可用于备注。
        :type Description: str
        """
        self.LUTFile = None
        self.Description = None


    def _deserialize(self, params):
        self.LUTFile = params.get("LUTFile")
        self.Description = params.get("Description")


class CreateModelResponse(AbstractModel):
    """CreateModel返回参数结构体

    """

    def __init__(self):
        """
        :param ModelId: 唇色素材ID。
        :type ModelId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModelId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.RequestId = params.get("RequestId")


class DeleteModelRequest(AbstractModel):
    """DeleteModel请求参数结构体

    """

    def __init__(self):
        """
        :param ModelId: 素材ID。
        :type ModelId: str
        """
        self.ModelId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")


class DeleteModelResponse(AbstractModel):
    """DeleteModel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FaceRect(AbstractModel):
    """人脸框信息

    """

    def __init__(self):
        """
        :param X: 人脸框左上角横坐标。
        :type X: int
        :param Y: 人脸框左上角纵坐标。
        :type Y: int
        :param Width: 人脸框宽度。
        :type Width: int
        :param Height: 人脸框高度。
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


class GetModelListRequest(AbstractModel):
    """GetModelList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 起始序号，默认值为0。
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为100。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetModelListResponse(AbstractModel):
    """GetModelList返回参数结构体

    """

    def __init__(self):
        """
        :param ModelIdNum: 唇色素材总数量。
        :type ModelIdNum: int
        :param ModelInfos: 素材数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInfos: list of ModelInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModelIdNum = None
        self.ModelInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelIdNum = params.get("ModelIdNum")
        if params.get("ModelInfos") is not None:
            self.ModelInfos = []
            for item in params.get("ModelInfos"):
                obj = ModelInfo()
                obj._deserialize(item)
                self.ModelInfos.append(obj)
        self.RequestId = params.get("RequestId")


class LipColorInfo(AbstractModel):
    """唇色信息

    """

    def __init__(self):
        """
        :param RGBA: 使用RGBA模型试唇色。
        :type RGBA: :class:`tencentcloud.fmu.v20191213.models.RGBAInfo`
        :param ModelId: 使用已注册的 LUT 文件试唇色。  
ModelId 和 RGBA 两个参数只需提供一个，若都提供只使用 ModelId。
        :type ModelId: str
        :param FaceRect: 人脸框位置。若不输入则选择 Image 或 Url 中面积最大的人脸。  
您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800)  接口获取人脸框位置信息。
        :type FaceRect: :class:`tencentcloud.fmu.v20191213.models.FaceRect`
        :param ModelAlpha: 涂妆浓淡[0,100]。建议取值50。本参数仅控制ModelId对应的涂妆浓淡。
        :type ModelAlpha: int
        """
        self.RGBA = None
        self.ModelId = None
        self.FaceRect = None
        self.ModelAlpha = None


    def _deserialize(self, params):
        if params.get("RGBA") is not None:
            self.RGBA = RGBAInfo()
            self.RGBA._deserialize(params.get("RGBA"))
        self.ModelId = params.get("ModelId")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        self.ModelAlpha = params.get("ModelAlpha")


class ModelInfo(AbstractModel):
    """LUT素材信息

    """

    def __init__(self):
        """
        :param ModelId: 唇色素材ID
        :type ModelId: str
        :param LUTFileUrl: 唇色素材 url 。 LUT 文件 url 5分钟有效。
        :type LUTFileUrl: str
        :param Description: 文件描述信息。
        :type Description: str
        """
        self.ModelId = None
        self.LUTFileUrl = None
        self.Description = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.LUTFileUrl = params.get("LUTFileUrl")
        self.Description = params.get("Description")


class RGBAInfo(AbstractModel):
    """RGBA通道信息

    """

    def __init__(self):
        """
        :param R: R通道数值。[0,255]。
        :type R: int
        :param G: G通道数值。[0,255]。
        :type G: int
        :param B: B通道数值。[0,255]。
        :type B: int
        :param A: A通道数值。[0,100]。建议取值50。
        :type A: int
        """
        self.R = None
        self.G = None
        self.B = None
        self.A = None


    def _deserialize(self, params):
        self.R = params.get("R")
        self.G = params.get("G")
        self.B = params.get("B")
        self.A = params.get("A")


class TryLipstickPicRequest(AbstractModel):
    """TryLipstickPic请求参数结构体

    """

    def __init__(self):
        """
        :param LipColorInfos: 唇色信息。 
您可以输入最多3个 LipColorInfo 来实现给一张图中的最多3张人脸试唇色。
        :type LipColorInfos: list of LipColorInfo
        :param Image: 图片 base64 数据，base64 编码后大小不可超过6M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url ，对应图片 base64 编码后大小不可超过6M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        """
        self.LipColorInfos = None
        self.Image = None
        self.Url = None
        self.RspImgType = None


    def _deserialize(self, params):
        if params.get("LipColorInfos") is not None:
            self.LipColorInfos = []
            for item in params.get("LipColorInfos"):
                obj = LipColorInfo()
                obj._deserialize(item)
                self.LipColorInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.RspImgType = params.get("RspImgType")


class TryLipstickPicResponse(AbstractModel):
    """TryLipstickPic返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
        :type ResultImage: str
        :param ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
        :type ResultUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.ResultUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultUrl = params.get("ResultUrl")
        self.RequestId = params.get("RequestId")