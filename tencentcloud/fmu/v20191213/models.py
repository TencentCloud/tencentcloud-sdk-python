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


class BeautifyPicRequest(AbstractModel):
    """BeautifyPic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M，单边分辨率不超过4000。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。，单边分辨率不超过4000。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :type Url: str
        :param _Whitening: 美白程度，取值范围[0,100]。0不美白，100代表最高程度。默认值30。
        :type Whitening: int
        :param _Smoothing: 磨皮程度，取值范围[0,100]。0不磨皮，100代表最高程度。默认值10。
        :type Smoothing: int
        :param _FaceLifting: 瘦脸程度，取值范围[0,100]。0不瘦脸，100代表最高程度。默认值70。
        :type FaceLifting: int
        :param _EyeEnlarging: 大眼程度，取值范围[0,100]。0不大眼，100代表最高程度。默认值70。
        :type EyeEnlarging: int
        :param _RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        """
        self._Image = None
        self._Url = None
        self._Whitening = None
        self._Smoothing = None
        self._FaceLifting = None
        self._EyeEnlarging = None
        self._RspImgType = None

    @property
    def Image(self):
        """图片 base64 数据，base64 编码后大小不可超过5M，单边分辨率不超过4000。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        """图片的 Url 。对应图片 base64 编码后大小不可超过5M。，单边分辨率不超过4000。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Whitening(self):
        """美白程度，取值范围[0,100]。0不美白，100代表最高程度。默认值30。
        :rtype: int
        """
        return self._Whitening

    @Whitening.setter
    def Whitening(self, Whitening):
        self._Whitening = Whitening

    @property
    def Smoothing(self):
        """磨皮程度，取值范围[0,100]。0不磨皮，100代表最高程度。默认值10。
        :rtype: int
        """
        return self._Smoothing

    @Smoothing.setter
    def Smoothing(self, Smoothing):
        self._Smoothing = Smoothing

    @property
    def FaceLifting(self):
        """瘦脸程度，取值范围[0,100]。0不瘦脸，100代表最高程度。默认值70。
        :rtype: int
        """
        return self._FaceLifting

    @FaceLifting.setter
    def FaceLifting(self, FaceLifting):
        self._FaceLifting = FaceLifting

    @property
    def EyeEnlarging(self):
        """大眼程度，取值范围[0,100]。0不大眼，100代表最高程度。默认值70。
        :rtype: int
        """
        return self._EyeEnlarging

    @EyeEnlarging.setter
    def EyeEnlarging(self, EyeEnlarging):
        self._EyeEnlarging = EyeEnlarging

    @property
    def RspImgType(self):
        """返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._Whitening = params.get("Whitening")
        self._Smoothing = params.get("Smoothing")
        self._FaceLifting = params.get("FaceLifting")
        self._EyeEnlarging = params.get("EyeEnlarging")
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BeautifyPicResponse(AbstractModel):
    """BeautifyPic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultImage: str
        :param _ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._ResultUrl = None
        self._RequestId = None

    @property
    def ResultImage(self):
        """RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultUrl(self):
        """RspImgType 为 url 时，返回处理后的图片 url 数据。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._ResultUrl = params.get("ResultUrl")
        self._RequestId = params.get("RequestId")


class CreateModelRequest(AbstractModel):
    """CreateModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LUTFile: 图片base64数据，用于试唇色，要求必须是LUT 格式的cube文件转换成512*512的PNG图片。查看 [LUT文件的使用说明](https://cloud.tencent.com/document/product/1172/41701)。了解 [cube文件转png图片小工具](http://yyb.gtimg.com/aiplat/static/qcloud-cube-to-png.html)。
        :type LUTFile: str
        :param _Description: 文件描述信息，可用于备注。
        :type Description: str
        """
        self._LUTFile = None
        self._Description = None

    @property
    def LUTFile(self):
        """图片base64数据，用于试唇色，要求必须是LUT 格式的cube文件转换成512*512的PNG图片。查看 [LUT文件的使用说明](https://cloud.tencent.com/document/product/1172/41701)。了解 [cube文件转png图片小工具](http://yyb.gtimg.com/aiplat/static/qcloud-cube-to-png.html)。
        :rtype: str
        """
        return self._LUTFile

    @LUTFile.setter
    def LUTFile(self, LUTFile):
        self._LUTFile = LUTFile

    @property
    def Description(self):
        """文件描述信息，可用于备注。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._LUTFile = params.get("LUTFile")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModelResponse(AbstractModel):
    """CreateModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 唇色素材ID。
        :type ModelId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelId = None
        self._RequestId = None

    @property
    def ModelId(self):
        """唇色素材ID。
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._RequestId = params.get("RequestId")


class DeleteModelRequest(AbstractModel):
    """DeleteModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 素材ID。
        :type ModelId: str
        """
        self._ModelId = None

    @property
    def ModelId(self):
        """素材ID。
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelResponse(AbstractModel):
    """DeleteModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class FaceRect(AbstractModel):
    """人脸框信息

    """

    def __init__(self):
        r"""
        :param _X: 人脸框左上角横坐标。
        :type X: int
        :param _Y: 人脸框左上角纵坐标。
        :type Y: int
        :param _Width: 人脸框宽度。
        :type Width: int
        :param _Height: 人脸框高度。
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        """人脸框左上角横坐标。
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """人脸框左上角纵坐标。
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        """人脸框宽度。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """人脸框高度。
        :rtype: int
        """
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
        


class GetModelListRequest(AbstractModel):
    """GetModelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 起始序号，默认值为0。
        :type Offset: int
        :param _Limit: 返回数量，默认值为10，最大值为100。
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """起始序号，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认值为10，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetModelListResponse(AbstractModel):
    """GetModelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelIdNum: 唇色素材总数量。
        :type ModelIdNum: int
        :param _ModelInfos: 素材数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInfos: list of ModelInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelIdNum = None
        self._ModelInfos = None
        self._RequestId = None

    @property
    def ModelIdNum(self):
        """唇色素材总数量。
        :rtype: int
        """
        return self._ModelIdNum

    @ModelIdNum.setter
    def ModelIdNum(self, ModelIdNum):
        self._ModelIdNum = ModelIdNum

    @property
    def ModelInfos(self):
        """素材数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ModelInfo
        """
        return self._ModelInfos

    @ModelInfos.setter
    def ModelInfos(self, ModelInfos):
        self._ModelInfos = ModelInfos

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelIdNum = params.get("ModelIdNum")
        if params.get("ModelInfos") is not None:
            self._ModelInfos = []
            for item in params.get("ModelInfos"):
                obj = ModelInfo()
                obj._deserialize(item)
                self._ModelInfos.append(obj)
        self._RequestId = params.get("RequestId")


class LipColorInfo(AbstractModel):
    """唇色信息

    """

    def __init__(self):
        r"""
        :param _RGBA: 使用RGBA模型试唇色。
        :type RGBA: :class:`tencentcloud.fmu.v20191213.models.RGBAInfo`
        :param _ModelId: 使用已注册的 LUT 文件试唇色。  
ModelId 和 RGBA 两个参数只需提供一个，若都提供只使用 ModelId。
        :type ModelId: str
        :param _FaceRect: 人脸框位置。若不输入则选择 Image 或 Url 中面积最大的人脸。  
您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800)  接口获取人脸框位置信息。
        :type FaceRect: :class:`tencentcloud.fmu.v20191213.models.FaceRect`
        :param _ModelAlpha: 涂妆浓淡[0,100]。建议取值50。本参数仅控制ModelId对应的涂妆浓淡。
        :type ModelAlpha: int
        """
        self._RGBA = None
        self._ModelId = None
        self._FaceRect = None
        self._ModelAlpha = None

    @property
    def RGBA(self):
        """使用RGBA模型试唇色。
        :rtype: :class:`tencentcloud.fmu.v20191213.models.RGBAInfo`
        """
        return self._RGBA

    @RGBA.setter
    def RGBA(self, RGBA):
        self._RGBA = RGBA

    @property
    def ModelId(self):
        """使用已注册的 LUT 文件试唇色。  
ModelId 和 RGBA 两个参数只需提供一个，若都提供只使用 ModelId。
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def FaceRect(self):
        """人脸框位置。若不输入则选择 Image 或 Url 中面积最大的人脸。  
您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800)  接口获取人脸框位置信息。
        :rtype: :class:`tencentcloud.fmu.v20191213.models.FaceRect`
        """
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect

    @property
    def ModelAlpha(self):
        """涂妆浓淡[0,100]。建议取值50。本参数仅控制ModelId对应的涂妆浓淡。
        :rtype: int
        """
        return self._ModelAlpha

    @ModelAlpha.setter
    def ModelAlpha(self, ModelAlpha):
        self._ModelAlpha = ModelAlpha


    def _deserialize(self, params):
        if params.get("RGBA") is not None:
            self._RGBA = RGBAInfo()
            self._RGBA._deserialize(params.get("RGBA"))
        self._ModelId = params.get("ModelId")
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        self._ModelAlpha = params.get("ModelAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelInfo(AbstractModel):
    """LUT素材信息

    """

    def __init__(self):
        r"""
        :param _ModelId: 唇色素材ID
        :type ModelId: str
        :param _LUTFileUrl: 唇色素材 url 。 LUT 文件 url 5分钟有效。
        :type LUTFileUrl: str
        :param _Description: 文件描述信息。
        :type Description: str
        """
        self._ModelId = None
        self._LUTFileUrl = None
        self._Description = None

    @property
    def ModelId(self):
        """唇色素材ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def LUTFileUrl(self):
        """唇色素材 url 。 LUT 文件 url 5分钟有效。
        :rtype: str
        """
        return self._LUTFileUrl

    @LUTFileUrl.setter
    def LUTFileUrl(self, LUTFileUrl):
        self._LUTFileUrl = LUTFileUrl

    @property
    def Description(self):
        """文件描述信息。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._LUTFileUrl = params.get("LUTFileUrl")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RGBAInfo(AbstractModel):
    """RGBA通道信息

    """

    def __init__(self):
        r"""
        :param _R: R通道数值。[0,255]。
        :type R: int
        :param _G: G通道数值。[0,255]。
        :type G: int
        :param _B: B通道数值。[0,255]。
        :type B: int
        :param _A: A通道数值。[0,100]。建议取值50。
        :type A: int
        """
        self._R = None
        self._G = None
        self._B = None
        self._A = None

    @property
    def R(self):
        """R通道数值。[0,255]。
        :rtype: int
        """
        return self._R

    @R.setter
    def R(self, R):
        self._R = R

    @property
    def G(self):
        """G通道数值。[0,255]。
        :rtype: int
        """
        return self._G

    @G.setter
    def G(self, G):
        self._G = G

    @property
    def B(self):
        """B通道数值。[0,255]。
        :rtype: int
        """
        return self._B

    @B.setter
    def B(self, B):
        self._B = B

    @property
    def A(self):
        """A通道数值。[0,100]。建议取值50。
        :rtype: int
        """
        return self._A

    @A.setter
    def A(self, A):
        self._A = A


    def _deserialize(self, params):
        self._R = params.get("R")
        self._G = params.get("G")
        self._B = params.get("B")
        self._A = params.get("A")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StyleImageProRequest(AbstractModel):
    """StyleImagePro请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FilterType: 滤镜类型，取值如下： 
1.白茶1；2 白皙；3.初夏；4.东京；5.告白；6.暖阳；7.蔷薇；8.清澄；9.清透；10.甜薄荷；11.默认；12.心动；13.哑灰；14.樱桃布丁；15.自然；16.清逸1；17.黑白；18.水果；19.爱情；20.冬日；21.相片；22.夏日；23.香氛；24.魅惑；25.悸动；26.沙滩；27.街拍；28.甜美；29.初吻；30.午后；31.活力；32.朦胧；33.悦动；34.时尚；35.气泡；36.柠檬；37.棉花糖；38.小溪；39.丽人；40.咖啡；41.嫩芽；42.热情；43.渐暖；44.早餐；45.白茶2；46.白嫩；47.圣代；48.森林；49.冲浪；50.奶咖；51.清澈；52.微风；53.日落；54.水光；55.日系；56.星光；57.阳光；58.落叶；59.生机；60.甜心；61.清逸2；62.春意；63.罗马；64.青涩；65.清风；66.暖心；67.海水；68.神秘；69.旧调1；70.旧调2；71.雪顶；72.日光；73.浮云；74.流彩；75.胶片；76.回味；77.奶酪；78.蝴蝶。
        :type FilterType: int
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :type Image: str
        :param _Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP 等图片格式，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :type Url: str
        :param _FilterDegree: 滤镜效果，取值[0,100]，0表示无效果，100表示满滤镜效果。默认值为80。
        :type FilterDegree: int
        :param _RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。默认为base64。
        :type RspImgType: str
        """
        self._FilterType = None
        self._Image = None
        self._Url = None
        self._FilterDegree = None
        self._RspImgType = None

    @property
    def FilterType(self):
        """滤镜类型，取值如下： 
1.白茶1；2 白皙；3.初夏；4.东京；5.告白；6.暖阳；7.蔷薇；8.清澄；9.清透；10.甜薄荷；11.默认；12.心动；13.哑灰；14.樱桃布丁；15.自然；16.清逸1；17.黑白；18.水果；19.爱情；20.冬日；21.相片；22.夏日；23.香氛；24.魅惑；25.悸动；26.沙滩；27.街拍；28.甜美；29.初吻；30.午后；31.活力；32.朦胧；33.悦动；34.时尚；35.气泡；36.柠檬；37.棉花糖；38.小溪；39.丽人；40.咖啡；41.嫩芽；42.热情；43.渐暖；44.早餐；45.白茶2；46.白嫩；47.圣代；48.森林；49.冲浪；50.奶咖；51.清澈；52.微风；53.日落；54.水光；55.日系；56.星光；57.阳光；58.落叶；59.生机；60.甜心；61.清逸2；62.春意；63.罗马；64.青涩；65.清风；66.暖心；67.海水；68.神秘；69.旧调1；70.旧调2；71.雪顶；72.日光；73.浮云；74.流彩；75.胶片；76.回味；77.奶酪；78.蝴蝶。
        :rtype: int
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Image(self):
        """图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        """图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP 等图片格式，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FilterDegree(self):
        """滤镜效果，取值[0,100]，0表示无效果，100表示满滤镜效果。默认值为80。
        :rtype: int
        """
        return self._FilterDegree

    @FilterDegree.setter
    def FilterDegree(self, FilterDegree):
        self._FilterDegree = FilterDegree

    @property
    def RspImgType(self):
        """返回图像方式（base64 或 url ) ，二选一。url有效期为1天。默认为base64。
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._FilterType = params.get("FilterType")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._FilterDegree = params.get("FilterDegree")
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StyleImageProResponse(AbstractModel):
    """StyleImagePro返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultImage: str
        :param _ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._ResultUrl = None
        self._RequestId = None

    @property
    def ResultImage(self):
        """RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultUrl(self):
        """RspImgType 为 url 时，返回处理后的图片 url 数据。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._ResultUrl = params.get("ResultUrl")
        self._RequestId = params.get("RequestId")


class StyleImageRequest(AbstractModel):
    """StyleImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FilterType: 滤镜类型，取值如下： 
1.白茶；2 白皙；3.初夏；4.东京；5.告白；6.暖阳；7.蔷薇；8.清澄；9.清透；10.甜薄荷；11.默认；12.心动；13.哑灰；14.樱桃布丁；15.自然；16.清逸；17.黑白；18.水果；19.爱情；20.冬日；21.相片；22.夏日；23.香氛；24.魅惑；25.悸动；26.沙滩；27.街拍；28.甜美；29.初吻；30.午后。
        :type FilterType: int
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :type Image: str
        :param _Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP 等图片格式，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :type Url: str
        :param _FilterDegree: 滤镜效果，取值[0,100]，0表示无效果，100表示满滤镜效果。默认值为80。
        :type FilterDegree: int
        :param _RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。默认值为base64。
        :type RspImgType: str
        """
        self._FilterType = None
        self._Image = None
        self._Url = None
        self._FilterDegree = None
        self._RspImgType = None

    @property
    def FilterType(self):
        """滤镜类型，取值如下： 
1.白茶；2 白皙；3.初夏；4.东京；5.告白；6.暖阳；7.蔷薇；8.清澄；9.清透；10.甜薄荷；11.默认；12.心动；13.哑灰；14.樱桃布丁；15.自然；16.清逸；17.黑白；18.水果；19.爱情；20.冬日；21.相片；22.夏日；23.香氛；24.魅惑；25.悸动；26.沙滩；27.街拍；28.甜美；29.初吻；30.午后。
        :rtype: int
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Image(self):
        """图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        """图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP 等图片格式，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FilterDegree(self):
        """滤镜效果，取值[0,100]，0表示无效果，100表示满滤镜效果。默认值为80。
        :rtype: int
        """
        return self._FilterDegree

    @FilterDegree.setter
    def FilterDegree(self, FilterDegree):
        self._FilterDegree = FilterDegree

    @property
    def RspImgType(self):
        """返回图像方式（base64 或 url ) ，二选一。url有效期为1天。默认值为base64。
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._FilterType = params.get("FilterType")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._FilterDegree = params.get("FilterDegree")
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StyleImageResponse(AbstractModel):
    """StyleImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultImage: str
        :param _ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._ResultUrl = None
        self._RequestId = None

    @property
    def ResultImage(self):
        """RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultUrl(self):
        """RspImgType 为 url 时，返回处理后的图片 url 数据。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._ResultUrl = params.get("ResultUrl")
        self._RequestId = params.get("RequestId")


class TryLipstickPicRequest(AbstractModel):
    """TryLipstickPic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LipColorInfos: 唇色信息。 
您可以输入最多3个 LipColorInfo 来实现给一张图中的最多3张人脸试唇色。
        :type LipColorInfos: list of LipColorInfo
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过6M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :type Image: str
        :param _Url: 图片的 Url ，对应图片 base64 编码后大小不可超过6M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :type Url: str
        :param _RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        """
        self._LipColorInfos = None
        self._Image = None
        self._Url = None
        self._RspImgType = None

    @property
    def LipColorInfos(self):
        """唇色信息。 
您可以输入最多3个 LipColorInfo 来实现给一张图中的最多3张人脸试唇色。
        :rtype: list of LipColorInfo
        """
        return self._LipColorInfos

    @LipColorInfos.setter
    def LipColorInfos(self, LipColorInfos):
        self._LipColorInfos = LipColorInfos

    @property
    def Image(self):
        """图片 base64 数据，base64 编码后大小不可超过6M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        """图片的 Url ，对应图片 base64 编码后大小不可超过6M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
暂不支持带有alpha透明通道的图片。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RspImgType(self):
        """返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        if params.get("LipColorInfos") is not None:
            self._LipColorInfos = []
            for item in params.get("LipColorInfos"):
                obj = LipColorInfo()
                obj._deserialize(item)
                self._LipColorInfos.append(obj)
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TryLipstickPicResponse(AbstractModel):
    """TryLipstickPic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
        :type ResultImage: str
        :param _ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
        :type ResultUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._ResultUrl = None
        self._RequestId = None

    @property
    def ResultImage(self):
        """RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultUrl(self):
        """RspImgType 为 url 时，返回处理后的图片 url 数据。
        :rtype: str
        """
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._ResultUrl = params.get("ResultUrl")
        self._RequestId = params.get("RequestId")