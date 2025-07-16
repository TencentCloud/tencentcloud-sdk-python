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
    """3D文件

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
        """文件格式
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        """文件的Url（有效期24小时）
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def PreviewImageUrl(self):
        """预览图片Url
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
        


class QueryHunyuanTo3DJobRequest(AbstractModel):
    """QueryHunyuanTo3DJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """任务ID。
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
        


class QueryHunyuanTo3DJobResponse(AbstractModel):
    """QueryHunyuanTo3DJob返回参数结构体

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
        """任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        """错误码
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultFile3Ds(self):
        """生成的3D文件数组。
        :rtype: list of File3D
        """
        return self._ResultFile3Ds

    @ResultFile3Ds.setter
    def ResultFile3Ds(self, ResultFile3Ds):
        self._ResultFile3Ds = ResultFile3Ds

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


class SubmitHunyuanTo3DJobRequest(AbstractModel):
    """SubmitHunyuanTo3DJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文生3D，3D内容的描述，中文正向提示词。
最多支持1024个 utf-8 字符。
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
        :param _MultiViewImages: 多视角的模型图片，视角参考值：
left：左视图；
right：右视图；
back：后视图；

每个视角仅限制一张图片。
●图片大小限制：编码后大小不可超过8M。
●图片分辨率限制：单边分辨率小于5000且大于128。
●支持图片格式：支持jpg或png
        :type MultiViewImages: list of ViewImage
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
        self._MultiViewImages = None
        self._ResultFormat = None
        self._EnablePBR = None

    @property
    def Prompt(self):
        """文生3D，3D内容的描述，中文正向提示词。
最多支持1024个 utf-8 字符。
文生3D, image、image_url和 prompt必填其一，且prompt和image/image_url不能同时存在。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def ImageBase64(self):
        """输入图 Base64 数据。
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
        """输入图Url。
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
    def MultiViewImages(self):
        """多视角的模型图片，视角参考值：
left：左视图；
right：右视图；
back：后视图；

每个视角仅限制一张图片。
●图片大小限制：编码后大小不可超过8M。
●图片分辨率限制：单边分辨率小于5000且大于128。
●支持图片格式：支持jpg或png
        :rtype: list of ViewImage
        """
        return self._MultiViewImages

    @MultiViewImages.setter
    def MultiViewImages(self, MultiViewImages):
        self._MultiViewImages = MultiViewImages

    @property
    def ResultFormat(self):
        """生成模型的格式，仅限制生成一种格式。
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
        """是否开启 PBR材质生成，默认 false。
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
        if params.get("MultiViewImages") is not None:
            self._MultiViewImages = []
            for item in params.get("MultiViewImages"):
                obj = ViewImage()
                obj._deserialize(item)
                self._MultiViewImages.append(obj)
        self._ResultFormat = params.get("ResultFormat")
        self._EnablePBR = params.get("EnablePBR")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanTo3DJobResponse(AbstractModel):
    """SubmitHunyuanTo3DJob返回参数结构体

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
        """任务ID（有效期24小时）
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class ViewImage(AbstractModel):
    """多视角图片

    """

    def __init__(self):
        r"""
        :param _ViewType: 视角类型。
取值：back、left、right
        :type ViewType: str
        :param _ViewImageUrl: 图片Url地址
        :type ViewImageUrl: str
        """
        self._ViewType = None
        self._ViewImageUrl = None

    @property
    def ViewType(self):
        """视角类型。
取值：back、left、right
        :rtype: str
        """
        return self._ViewType

    @ViewType.setter
    def ViewType(self, ViewType):
        self._ViewType = ViewType

    @property
    def ViewImageUrl(self):
        """图片Url地址
        :rtype: str
        """
        return self._ViewImageUrl

    @ViewImageUrl.setter
    def ViewImageUrl(self, ViewImageUrl):
        self._ViewImageUrl = ViewImageUrl


    def _deserialize(self, params):
        self._ViewType = params.get("ViewType")
        self._ViewImageUrl = params.get("ViewImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        