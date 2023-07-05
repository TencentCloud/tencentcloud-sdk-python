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


class AgeInfo(AbstractModel):
    """人脸变年龄信息

    """

    def __init__(self):
        r"""
        :param _Age: 变化到的人脸年龄 [10,80]。
        :type Age: int
        :param _FaceRect: 人脸框位置。若不输入则选择 Image 或 Url 中面积最大的人脸。  
您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800)  接口获取人脸框位置信息。
        :type FaceRect: :class:`tencentcloud.ft.v20200304.models.FaceRect`
        """
        self._Age = None
        self._FaceRect = None

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect


    def _deserialize(self, params):
        self._Age = params.get("Age")
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelFaceMorphJobRequest(AbstractModel):
    """CancelFaceMorphJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 人像渐变任务Job id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
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
        


class CancelFaceMorphJobResponse(AbstractModel):
    """CancelFaceMorphJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ChangeAgePicRequest(AbstractModel):
    """ChangeAgePic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AgeInfos: 人脸变老变年轻信息。 
您可以输入最多3个 AgeInfo 来实现给一张图中的最多3张人脸变老变年轻。
        :type AgeInfos: list of AgeInfo
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        """
        self._AgeInfos = None
        self._Image = None
        self._Url = None
        self._RspImgType = None

    @property
    def AgeInfos(self):
        return self._AgeInfos

    @AgeInfos.setter
    def AgeInfos(self, AgeInfos):
        self._AgeInfos = AgeInfos

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RspImgType(self):
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        if params.get("AgeInfos") is not None:
            self._AgeInfos = []
            for item in params.get("AgeInfos"):
                obj = AgeInfo()
                obj._deserialize(item)
                self._AgeInfos.append(obj)
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
        


class ChangeAgePicResponse(AbstractModel):
    """ChangeAgePic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
        :type ResultImage: str
        :param _ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
        :type ResultUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._ResultUrl = None
        self._RequestId = None

    @property
    def ResultImage(self):
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultUrl(self):
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._ResultUrl = params.get("ResultUrl")
        self._RequestId = params.get("RequestId")


class FaceCartoonPicRequest(AbstractModel):
    """FaceCartoonPic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        :param _DisableGlobalEffect: 关闭全图动漫化，传入true（不分大小写）即关闭全图动漫化。
        :type DisableGlobalEffect: str
        """
        self._Image = None
        self._Url = None
        self._RspImgType = None
        self._DisableGlobalEffect = None

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RspImgType(self):
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def DisableGlobalEffect(self):
        return self._DisableGlobalEffect

    @DisableGlobalEffect.setter
    def DisableGlobalEffect(self, DisableGlobalEffect):
        self._DisableGlobalEffect = DisableGlobalEffect


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._RspImgType = params.get("RspImgType")
        self._DisableGlobalEffect = params.get("DisableGlobalEffect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceCartoonPicResponse(AbstractModel):
    """FaceCartoonPic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: 结果图片Base64信息。
        :type ResultImage: str
        :param _ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。(默认为base64)
        :type ResultUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._ResultUrl = None
        self._RequestId = None

    @property
    def ResultImage(self):
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultUrl(self):
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._ResultUrl = params.get("ResultUrl")
        self._RequestId = params.get("RequestId")


class FaceMorphOutput(AbstractModel):
    """人像渐变返回结果

    """

    def __init__(self):
        r"""
        :param _MorphUrl: 人像渐变输出的url
注意：此字段可能返回 null，表示取不到有效值。
        :type MorphUrl: str
        :param _MorphMd5: 人像渐变输出的结果MD5，用于校验
注意：此字段可能返回 null，表示取不到有效值。
        :type MorphMd5: str
        :param _CoverImage: 人像渐变输出的结果封面图base64字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverImage: str
        """
        self._MorphUrl = None
        self._MorphMd5 = None
        self._CoverImage = None

    @property
    def MorphUrl(self):
        return self._MorphUrl

    @MorphUrl.setter
    def MorphUrl(self, MorphUrl):
        self._MorphUrl = MorphUrl

    @property
    def MorphMd5(self):
        return self._MorphMd5

    @MorphMd5.setter
    def MorphMd5(self, MorphMd5):
        self._MorphMd5 = MorphMd5

    @property
    def CoverImage(self):
        return self._CoverImage

    @CoverImage.setter
    def CoverImage(self, CoverImage):
        self._CoverImage = CoverImage


    def _deserialize(self, params):
        self._MorphUrl = params.get("MorphUrl")
        self._MorphMd5 = params.get("MorphMd5")
        self._CoverImage = params.get("CoverImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceRect(AbstractModel):
    """人脸框信息

    """

    def __init__(self):
        r"""
        :param _Y: 人脸框左上角纵坐标。
        :type Y: int
        :param _X: 人脸框左上角横坐标。
        :type X: int
        :param _Width: 人脸框宽度。
        :type Width: int
        :param _Height: 人脸框高度。
        :type Height: int
        """
        self._Y = None
        self._X = None
        self._Width = None
        self._Height = None

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

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
        self._Y = params.get("Y")
        self._X = params.get("X")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenderInfo(AbstractModel):
    """人脸转换性别信息

    """

    def __init__(self):
        r"""
        :param _Gender: 选择转换方向，0：男变女，1：女变男。
        :type Gender: int
        :param _FaceRect: 人脸框位置。若不输入则选择 Image 或 Url 中面积最大的人脸。  
您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800)  接口获取人脸框位置信息。
        :type FaceRect: :class:`tencentcloud.ft.v20200304.models.FaceRect`
        """
        self._Gender = None
        self._FaceRect = None

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect


    def _deserialize(self, params):
        self._Gender = params.get("Gender")
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GradientInfo(AbstractModel):
    """渐变参数

    """

    def __init__(self):
        r"""
        :param _Tempo: 图片的展示时长，即单张图片静止不变的时间。GIF默认每张图片0.7s，视频默认每张图片0.5s。最大取值1s。
        :type Tempo: float
        :param _MorphTime: 人像渐变的最长时间，即单张图片使用渐变特效的时间。 GIF默认值为0.5s，视频默值认为1s。最大取值1s。
        :type MorphTime: float
        """
        self._Tempo = None
        self._MorphTime = None

    @property
    def Tempo(self):
        return self._Tempo

    @Tempo.setter
    def Tempo(self, Tempo):
        self._Tempo = Tempo

    @property
    def MorphTime(self):
        return self._MorphTime

    @MorphTime.setter
    def MorphTime(self, MorphTime):
        self._MorphTime = MorphTime


    def _deserialize(self, params):
        self._Tempo = params.get("Tempo")
        self._MorphTime = params.get("MorphTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MorphFaceRequest(AbstractModel):
    """MorphFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Images: 图片 base64 数据，base64 编码后大小不可超过5M。 
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。 
人员人脸总数量至少2张，不可超过5张。 
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Images: list of str
        :param _Urls: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。 
Url、Image必须提供一个，如果都提供，只使用 Url。图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。 
人员人脸总数量不可超过5张。 
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
        :type Urls: list of str
        :param _GradientInfos: 人脸渐变参数。可调整每张图片的展示时长、人像渐变的最长时间
        :type GradientInfos: list of GradientInfo
        :param _Fps: 视频帧率，取值[1,25]。默认10
        :type Fps: int
        :param _OutputType: 视频类型，取值0。目前仅支持MP4格式，默认为MP4格式
        :type OutputType: int
        :param _OutputWidth: 视频宽度，取值[128,1280]。默认值720
        :type OutputWidth: int
        :param _OutputHeight: 视频高度，取值[128,1280]。默认值1280
        :type OutputHeight: int
        """
        self._Images = None
        self._Urls = None
        self._GradientInfos = None
        self._Fps = None
        self._OutputType = None
        self._OutputWidth = None
        self._OutputHeight = None

    @property
    def Images(self):
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def GradientInfos(self):
        return self._GradientInfos

    @GradientInfos.setter
    def GradientInfos(self, GradientInfos):
        self._GradientInfos = GradientInfos

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def OutputType(self):
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType

    @property
    def OutputWidth(self):
        return self._OutputWidth

    @OutputWidth.setter
    def OutputWidth(self, OutputWidth):
        self._OutputWidth = OutputWidth

    @property
    def OutputHeight(self):
        return self._OutputHeight

    @OutputHeight.setter
    def OutputHeight(self, OutputHeight):
        self._OutputHeight = OutputHeight


    def _deserialize(self, params):
        self._Images = params.get("Images")
        self._Urls = params.get("Urls")
        if params.get("GradientInfos") is not None:
            self._GradientInfos = []
            for item in params.get("GradientInfos"):
                obj = GradientInfo()
                obj._deserialize(item)
                self._GradientInfos.append(obj)
        self._Fps = params.get("Fps")
        self._OutputType = params.get("OutputType")
        self._OutputWidth = params.get("OutputWidth")
        self._OutputHeight = params.get("OutputHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MorphFaceResponse(AbstractModel):
    """MorphFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 人像渐变任务的Job id
        :type JobId: str
        :param _EstimatedProcessTime: 预估处理时间，粒度为秒
        :type EstimatedProcessTime: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._EstimatedProcessTime = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def EstimatedProcessTime(self):
        return self._EstimatedProcessTime

    @EstimatedProcessTime.setter
    def EstimatedProcessTime(self, EstimatedProcessTime):
        self._EstimatedProcessTime = EstimatedProcessTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._EstimatedProcessTime = params.get("EstimatedProcessTime")
        self._RequestId = params.get("RequestId")


class QueryFaceMorphJobRequest(AbstractModel):
    """QueryFaceMorphJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 人像渐变任务Job id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
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
        


class QueryFaceMorphJobResponse(AbstractModel):
    """QueryFaceMorphJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatus: 当前任务状态：排队中、处理中、处理失败或者处理完成
        :type JobStatus: str
        :param _FaceMorphOutput: 人像渐变输出的结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceMorphOutput: :class:`tencentcloud.ft.v20200304.models.FaceMorphOutput`
        :param _JobStatusCode: 当前任务状态码：1：排队中、3: 处理中、5: 处理失败、7:处理完成
注意：此字段可能返回 null，表示取不到有效值。
        :type JobStatusCode: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatus = None
        self._FaceMorphOutput = None
        self._JobStatusCode = None
        self._RequestId = None

    @property
    def JobStatus(self):
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def FaceMorphOutput(self):
        return self._FaceMorphOutput

    @FaceMorphOutput.setter
    def FaceMorphOutput(self, FaceMorphOutput):
        self._FaceMorphOutput = FaceMorphOutput

    @property
    def JobStatusCode(self):
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobStatus = params.get("JobStatus")
        if params.get("FaceMorphOutput") is not None:
            self._FaceMorphOutput = FaceMorphOutput()
            self._FaceMorphOutput._deserialize(params.get("FaceMorphOutput"))
        self._JobStatusCode = params.get("JobStatusCode")
        self._RequestId = params.get("RequestId")


class SwapGenderPicRequest(AbstractModel):
    """SwapGenderPic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GenderInfos: 人脸转化性别信息。 
您可以输入最多3个 GenderInfo 来实现给一张图中的最多3张人脸转换性别。
        :type GenderInfos: list of GenderInfo
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        """
        self._GenderInfos = None
        self._Image = None
        self._Url = None
        self._RspImgType = None

    @property
    def GenderInfos(self):
        return self._GenderInfos

    @GenderInfos.setter
    def GenderInfos(self, GenderInfos):
        self._GenderInfos = GenderInfos

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RspImgType(self):
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        if params.get("GenderInfos") is not None:
            self._GenderInfos = []
            for item in params.get("GenderInfos"):
                obj = GenderInfo()
                obj._deserialize(item)
                self._GenderInfos.append(obj)
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
        


class SwapGenderPicResponse(AbstractModel):
    """SwapGenderPic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
        :type ResultImage: str
        :param _ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
        :type ResultUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._ResultUrl = None
        self._RequestId = None

    @property
    def ResultImage(self):
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultUrl(self):
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._ResultUrl = params.get("ResultUrl")
        self._RequestId = params.get("RequestId")