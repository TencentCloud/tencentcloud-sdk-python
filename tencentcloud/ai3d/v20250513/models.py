# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class File3D(AbstractModel):
    r"""3D文件

    """

    def __init__(self):
        r"""
        :param _Type: 文件格式
        :type Type: str
        :param _Url: 文件的Url（有效期24小时）
        :type Url: str
        :param _PreviewImageUrl: 预览图片Url
        :type PreviewImageUrl: str
        """
        self._Type = None
        self._Url = None
        self._PreviewImageUrl = None

    @property
    def Type(self):
        r"""文件格式
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        r"""文件的Url（有效期24小时）
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def PreviewImageUrl(self):
        r"""预览图片Url
        :rtype: str
        """
        return self._PreviewImageUrl

    @PreviewImageUrl.setter
    def PreviewImageUrl(self, PreviewImageUrl):
        self._PreviewImageUrl = PreviewImageUrl


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        self._PreviewImageUrl = params.get("PreviewImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanTo3DProJobRequest(AbstractModel):
    r"""QueryHunyuanTo3DProJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanTo3DProJobResponse(AbstractModel):
    r"""QueryHunyuanTo3DProJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _ErrorMessage: 错误信息
        :type ErrorMessage: str
        :param _ResultFile3Ds: 生成的3D文件数组。
        :type ResultFile3Ds: list of File3D
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultFile3Ds = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""错误码
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultFile3Ds(self):
        r"""生成的3D文件数组。
        :rtype: list of File3D
        """
        return self._ResultFile3Ds

    @ResultFile3Ds.setter
    def ResultFile3Ds(self, ResultFile3Ds):
        self._ResultFile3Ds = ResultFile3Ds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        if params.get("ResultFile3Ds") is not None:
            self._ResultFile3Ds = []
            for item in params.get("ResultFile3Ds"):
                obj = File3D()
                obj._deserialize(item)
                self._ResultFile3Ds.append(obj)
        self._RequestId = params.get("RequestId")


class QueryHunyuanTo3DRapidJobRequest(AbstractModel):
    r"""QueryHunyuanTo3DRapidJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanTo3DRapidJobResponse(AbstractModel):
    r"""QueryHunyuanTo3DRapidJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _ErrorMessage: 错误信息
        :type ErrorMessage: str
        :param _ResultFile3Ds: 生成的3D文件数组。
        :type ResultFile3Ds: list of File3D
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultFile3Ds = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""错误码
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultFile3Ds(self):
        r"""生成的3D文件数组。
        :rtype: list of File3D
        """
        return self._ResultFile3Ds

    @ResultFile3Ds.setter
    def ResultFile3Ds(self, ResultFile3Ds):
        self._ResultFile3Ds = ResultFile3Ds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        if params.get("ResultFile3Ds") is not None:
            self._ResultFile3Ds = []
            for item in params.get("ResultFile3Ds"):
                obj = File3D()
                obj._deserialize(item)
                self._ResultFile3Ds.append(obj)
        self._RequestId = params.get("RequestId")


class SubmitHunyuanTo3DProJobRequest(AbstractModel):
    r"""SubmitHunyuanTo3DProJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文生3D，3D内容的描述，中文正向提示词。
最多支持1024个 utf-8 字符。
ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :type Prompt: str
        :param _ImageBase64: 输入图 Base64 数据。
大小：单边分辨率要求不小于128，不大于5000。大小不超过8m（base64编码后会大30%左右，建议实际输入图片不超过5m）
格式：jpg，png，jpeg，webp。
ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :type ImageBase64: str
        :param _ImageUrl: 输入图Url。
大小：单边分辨率要求不小于128，不大于5000。大小不超过8m（base64编码后会大30%左右，建议实际输入图片不超过5m）
格式：jpg，png，jpeg，webp。
ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :type ImageUrl: str
        :param _MultiViewImages: 多视角的模型图片，视角参考值：
left：左视图；
right：右视图；
back：后视图；

每个视角仅限制一张图片。
●图片大小限制：编码后大小不可超过8M。（base64编码后会大30%左右，建议实际输入图片不超过5m）
●图片分辨率限制：单边分辨率小于5000且大于128。
●支持图片格式：支持jpg或png
        :type MultiViewImages: list of ViewImage
        :param _EnablePBR: 是否开启 PBR材质生成，默认 false。
        :type EnablePBR: bool
        :param _FaceCount: 生成3D模型的面数，默认值为500000。
可支持生成面数范围，参考值：40000-1500000。
        :type FaceCount: int
        :param _GenerateType: 生成任务类型，默认Normal，参考值：
Normal：可生成带纹理的几何模型。
LowPoly：可生成智能减面后的模型。
Geometry：可生成不带纹理的几何模型（白模），选择此任务时，EnablePBR参数不生效。
Sketch：可输入草图或线稿图生成模型，此模式下prompt和ImageUrl/ImageBase64可一起输入。
        :type GenerateType: str
        :param _PolygonType: 该参数仅在GenerateType中选择LowPoly模式可生效。

多边形类型，表示模型的表面由几边形网格构成，默认为triangle,参考值:
triangle: 三角形面。
quadrilateral: 四边形面与三角形面混合生成。
        :type PolygonType: str
        """
        self._Prompt = None
        self._ImageBase64 = None
        self._ImageUrl = None
        self._MultiViewImages = None
        self._EnablePBR = None
        self._FaceCount = None
        self._GenerateType = None
        self._PolygonType = None

    @property
    def Prompt(self):
        r"""文生3D，3D内容的描述，中文正向提示词。
最多支持1024个 utf-8 字符。
ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def ImageBase64(self):
        r"""输入图 Base64 数据。
大小：单边分辨率要求不小于128，不大于5000。大小不超过8m（base64编码后会大30%左右，建议实际输入图片不超过5m）
格式：jpg，png，jpeg，webp。
ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""输入图Url。
大小：单边分辨率要求不小于128，不大于5000。大小不超过8m（base64编码后会大30%左右，建议实际输入图片不超过5m）
格式：jpg，png，jpeg，webp。
ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def MultiViewImages(self):
        r"""多视角的模型图片，视角参考值：
left：左视图；
right：右视图；
back：后视图；

每个视角仅限制一张图片。
●图片大小限制：编码后大小不可超过8M。（base64编码后会大30%左右，建议实际输入图片不超过5m）
●图片分辨率限制：单边分辨率小于5000且大于128。
●支持图片格式：支持jpg或png
        :rtype: list of ViewImage
        """
        return self._MultiViewImages

    @MultiViewImages.setter
    def MultiViewImages(self, MultiViewImages):
        self._MultiViewImages = MultiViewImages

    @property
    def EnablePBR(self):
        r"""是否开启 PBR材质生成，默认 false。
        :rtype: bool
        """
        return self._EnablePBR

    @EnablePBR.setter
    def EnablePBR(self, EnablePBR):
        self._EnablePBR = EnablePBR

    @property
    def FaceCount(self):
        r"""生成3D模型的面数，默认值为500000。
可支持生成面数范围，参考值：40000-1500000。
        :rtype: int
        """
        return self._FaceCount

    @FaceCount.setter
    def FaceCount(self, FaceCount):
        self._FaceCount = FaceCount

    @property
    def GenerateType(self):
        r"""生成任务类型，默认Normal，参考值：
Normal：可生成带纹理的几何模型。
LowPoly：可生成智能减面后的模型。
Geometry：可生成不带纹理的几何模型（白模），选择此任务时，EnablePBR参数不生效。
Sketch：可输入草图或线稿图生成模型，此模式下prompt和ImageUrl/ImageBase64可一起输入。
        :rtype: str
        """
        return self._GenerateType

    @GenerateType.setter
    def GenerateType(self, GenerateType):
        self._GenerateType = GenerateType

    @property
    def PolygonType(self):
        r"""该参数仅在GenerateType中选择LowPoly模式可生效。

多边形类型，表示模型的表面由几边形网格构成，默认为triangle,参考值:
triangle: 三角形面。
quadrilateral: 四边形面与三角形面混合生成。
        :rtype: str
        """
        return self._PolygonType

    @PolygonType.setter
    def PolygonType(self, PolygonType):
        self._PolygonType = PolygonType


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        if params.get("MultiViewImages") is not None:
            self._MultiViewImages = []
            for item in params.get("MultiViewImages"):
                obj = ViewImage()
                obj._deserialize(item)
                self._MultiViewImages.append(obj)
        self._EnablePBR = params.get("EnablePBR")
        self._FaceCount = params.get("FaceCount")
        self._GenerateType = params.get("GenerateType")
        self._PolygonType = params.get("PolygonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanTo3DProJobResponse(AbstractModel):
    r"""SubmitHunyuanTo3DProJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID（有效期24小时）
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID（有效期24小时）
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitHunyuanTo3DRapidJobRequest(AbstractModel):
    r"""SubmitHunyuanTo3DRapidJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文生3D，3D内容的描述，中文正向提示词。
最多支持200个 utf-8 字符。
文生3D, image、image_url和 prompt必填其一，且prompt和image/image_url不能同时存在。
        :type Prompt: str
        :param _ImageBase64: 输入图 Base64 数据。
大小：单边分辨率要求不小于128，不大于5000。大小不超过8m（base64编码后会大30%左右，建议实际输入图片不超过6m）
格式：jpg，png，jpeg，webp。
ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :type ImageBase64: str
        :param _ImageUrl: 输入图Url。
大小：单边分辨率要求不小于128，不大于5000。大小不超过8m（base64编码后会大30%左右，建议实际输入图片不超过6m）
格式：jpg，png，jpeg，webp。
ImageBase64/ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :type ImageUrl: str
        :param _ResultFormat: 生成模型的格式，仅限制生成一种格式。
生成模型文件组默认返回obj格式。
可选值：OBJ，GLB，STL，USDZ，FBX，MP4。
        :type ResultFormat: str
        :param _EnablePBR: 是否开启 PBR材质生成，默认 false。
        :type EnablePBR: bool
        """
        self._Prompt = None
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ResultFormat = None
        self._EnablePBR = None

    @property
    def Prompt(self):
        r"""文生3D，3D内容的描述，中文正向提示词。
最多支持200个 utf-8 字符。
文生3D, image、image_url和 prompt必填其一，且prompt和image/image_url不能同时存在。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def ImageBase64(self):
        r"""输入图 Base64 数据。
大小：单边分辨率要求不小于128，不大于5000。大小不超过8m（base64编码后会大30%左右，建议实际输入图片不超过6m）
格式：jpg，png，jpeg，webp。
ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        r"""输入图Url。
大小：单边分辨率要求不小于128，不大于5000。大小不超过8m（base64编码后会大30%左右，建议实际输入图片不超过6m）
格式：jpg，png，jpeg，webp。
ImageBase64/ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ResultFormat(self):
        r"""生成模型的格式，仅限制生成一种格式。
生成模型文件组默认返回obj格式。
可选值：OBJ，GLB，STL，USDZ，FBX，MP4。
        :rtype: str
        """
        return self._ResultFormat

    @ResultFormat.setter
    def ResultFormat(self, ResultFormat):
        self._ResultFormat = ResultFormat

    @property
    def EnablePBR(self):
        r"""是否开启 PBR材质生成，默认 false。
        :rtype: bool
        """
        return self._EnablePBR

    @EnablePBR.setter
    def EnablePBR(self, EnablePBR):
        self._EnablePBR = EnablePBR


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ResultFormat = params.get("ResultFormat")
        self._EnablePBR = params.get("EnablePBR")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanTo3DRapidJobResponse(AbstractModel):
    r"""SubmitHunyuanTo3DRapidJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID（有效期24小时）
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID（有效期24小时）
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class ViewImage(AbstractModel):
    r"""多视角图片

    """

    def __init__(self):
        r"""
        :param _ViewType: 视角类型。
取值：back、left、right
        :type ViewType: str
        :param _ViewImageUrl: 图片Url地址
        :type ViewImageUrl: str
        :param _ViewImageBase64: 图片base64地址
        :type ViewImageBase64: str
        """
        self._ViewType = None
        self._ViewImageUrl = None
        self._ViewImageBase64 = None

    @property
    def ViewType(self):
        r"""视角类型。
取值：back、left、right
        :rtype: str
        """
        return self._ViewType

    @ViewType.setter
    def ViewType(self, ViewType):
        self._ViewType = ViewType

    @property
    def ViewImageUrl(self):
        r"""图片Url地址
        :rtype: str
        """
        return self._ViewImageUrl

    @ViewImageUrl.setter
    def ViewImageUrl(self, ViewImageUrl):
        self._ViewImageUrl = ViewImageUrl

    @property
    def ViewImageBase64(self):
        r"""图片base64地址
        :rtype: str
        """
        return self._ViewImageBase64

    @ViewImageBase64.setter
    def ViewImageBase64(self, ViewImageBase64):
        self._ViewImageBase64 = ViewImageBase64


    def _deserialize(self, params):
        self._ViewType = params.get("ViewType")
        self._ViewImageUrl = params.get("ViewImageUrl")
        self._ViewImageBase64 = params.get("ViewImageBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        