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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AgeInfo(AbstractModel):
    """人脸变年龄信息

    """

    def __init__(self):
        """
        :param Age: 变化到的人脸年龄 [10,80]。
        :type Age: int
        :param FaceRect: 人脸框位置。若不输入则选择 Image 或 Url 中面积最大的人脸。  
您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800)  接口获取人脸框位置信息。
        :type FaceRect: :class:`tencentcloud.ft.v20200304.models.FaceRect`
        """
        self.Age = None
        self.FaceRect = None


    def _deserialize(self, params):
        self.Age = params.get("Age")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelFaceMorphJobRequest(AbstractModel):
    """CancelFaceMorphJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 人像渐变任务Job id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelFaceMorphJobResponse(AbstractModel):
    """CancelFaceMorphJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ChangeAgePicRequest(AbstractModel):
    """ChangeAgePic请求参数结构体

    """

    def __init__(self):
        """
        :param AgeInfos: 人脸变老变年轻信息。 
您可以输入最多3个 AgeInfo 来实现给一张图中的最多3张人脸变老变年轻。
        :type AgeInfos: list of AgeInfo
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        """
        self.AgeInfos = None
        self.Image = None
        self.Url = None
        self.RspImgType = None


    def _deserialize(self, params):
        if params.get("AgeInfos") is not None:
            self.AgeInfos = []
            for item in params.get("AgeInfos"):
                obj = AgeInfo()
                obj._deserialize(item)
                self.AgeInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ChangeAgePicResponse(AbstractModel):
    """ChangeAgePic返回参数结构体

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceCartoonPicRequest(AbstractModel):
    """FaceCartoonPic请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        :param DisableGlobalEffect: 关闭全图动漫化，传入true（不分大小写）即关闭全图动漫化。
        :type DisableGlobalEffect: str
        """
        self.Image = None
        self.Url = None
        self.RspImgType = None
        self.DisableGlobalEffect = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.RspImgType = params.get("RspImgType")
        self.DisableGlobalEffect = params.get("DisableGlobalEffect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceCartoonPicResponse(AbstractModel):
    """FaceCartoonPic返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: 结果图片Base64信息。
        :type ResultImage: str
        :param ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。(默认为base64)
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceMorphOutput(AbstractModel):
    """人像渐变返回结果

    """

    def __init__(self):
        """
        :param MorphUrl: 人像渐变输出的url
注意：此字段可能返回 null，表示取不到有效值。
        :type MorphUrl: str
        :param MorphMd5: 人像渐变输出的结果MD5，用于校验
注意：此字段可能返回 null，表示取不到有效值。
        :type MorphMd5: str
        :param CoverImage: 人像渐变输出的结果封面图base64字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverImage: str
        """
        self.MorphUrl = None
        self.MorphMd5 = None
        self.CoverImage = None


    def _deserialize(self, params):
        self.MorphUrl = params.get("MorphUrl")
        self.MorphMd5 = params.get("MorphMd5")
        self.CoverImage = params.get("CoverImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FaceRect(AbstractModel):
    """人脸框信息

    """

    def __init__(self):
        """
        :param Y: 人脸框左上角纵坐标。
        :type Y: int
        :param X: 人脸框左上角横坐标。
        :type X: int
        :param Width: 人脸框宽度。
        :type Width: int
        :param Height: 人脸框高度。
        :type Height: int
        """
        self.Y = None
        self.X = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Y = params.get("Y")
        self.X = params.get("X")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GenderInfo(AbstractModel):
    """人脸转换性别信息

    """

    def __init__(self):
        """
        :param Gender: 选择转换方向，0：男变女，1：女变男。
        :type Gender: int
        :param FaceRect: 人脸框位置。若不输入则选择 Image 或 Url 中面积最大的人脸。  
您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800)  接口获取人脸框位置信息。
        :type FaceRect: :class:`tencentcloud.ft.v20200304.models.FaceRect`
        """
        self.Gender = None
        self.FaceRect = None


    def _deserialize(self, params):
        self.Gender = params.get("Gender")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GradientInfo(AbstractModel):
    """渐变参数

    """

    def __init__(self):
        """
        :param Tempo: 图片的展示时长，即单张图片静止不变的时间。GIF默认每张图片0.7s，视频默认每张图片0.5s。最大取值1s。
        :type Tempo: float
        :param MorphTime: 人像渐变的最长时间，即单张图片使用渐变特效的时间。 GIF默认值为0.5s，视频默值认为1s。最大取值1s。
        :type MorphTime: float
        """
        self.Tempo = None
        self.MorphTime = None


    def _deserialize(self, params):
        self.Tempo = params.get("Tempo")
        self.MorphTime = params.get("MorphTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MorphFaceRequest(AbstractModel):
    """MorphFace请求参数结构体

    """

    def __init__(self):
        """
        :param Images: 图片 base64 数据，base64 编码后大小不可超过5M。 
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。 
人员人脸总数量至少2张，不可超过5张。 
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Images: list of str
        :param Urls: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。 
Url、Image必须提供一个，如果都提供，只使用 Url。图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。 
人员人脸总数量不可超过5张。 
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
        :type Urls: list of str
        :param GradientInfos: 人脸渐变参数。可调整每张图片的展示时长、人像渐变的最长时间
        :type GradientInfos: list of GradientInfo
        :param Fps: 视频帧率，取值[1,25]。默认10
        :type Fps: int
        :param OutputType: 视频类型，取值0。目前仅支持MP4格式，默认为MP4格式
        :type OutputType: int
        :param OutputWidth: 视频宽度，取值[128,1280]。默认值720
        :type OutputWidth: int
        :param OutputHeight: 视频高度，取值[128,1280]。默认值1280
        :type OutputHeight: int
        """
        self.Images = None
        self.Urls = None
        self.GradientInfos = None
        self.Fps = None
        self.OutputType = None
        self.OutputWidth = None
        self.OutputHeight = None


    def _deserialize(self, params):
        self.Images = params.get("Images")
        self.Urls = params.get("Urls")
        if params.get("GradientInfos") is not None:
            self.GradientInfos = []
            for item in params.get("GradientInfos"):
                obj = GradientInfo()
                obj._deserialize(item)
                self.GradientInfos.append(obj)
        self.Fps = params.get("Fps")
        self.OutputType = params.get("OutputType")
        self.OutputWidth = params.get("OutputWidth")
        self.OutputHeight = params.get("OutputHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MorphFaceResponse(AbstractModel):
    """MorphFace返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 人像渐变任务的Job id
        :type JobId: str
        :param EstimatedProcessTime: 预估处理时间，粒度为秒
        :type EstimatedProcessTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.EstimatedProcessTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.EstimatedProcessTime = params.get("EstimatedProcessTime")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryFaceMorphJobRequest(AbstractModel):
    """QueryFaceMorphJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 人像渐变任务Job id
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryFaceMorphJobResponse(AbstractModel):
    """QueryFaceMorphJob返回参数结构体

    """

    def __init__(self):
        """
        :param JobStatus: 当前任务状态：排队中、处理中、处理失败或者处理完成
        :type JobStatus: str
        :param FaceMorphOutput: 人像渐变输出的结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceMorphOutput: :class:`tencentcloud.ft.v20200304.models.FaceMorphOutput`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobStatus = None
        self.FaceMorphOutput = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobStatus = params.get("JobStatus")
        if params.get("FaceMorphOutput") is not None:
            self.FaceMorphOutput = FaceMorphOutput()
            self.FaceMorphOutput._deserialize(params.get("FaceMorphOutput"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SwapGenderPicRequest(AbstractModel):
    """SwapGenderPic请求参数结构体

    """

    def __init__(self):
        """
        :param GenderInfos: 人脸转化性别信息。 
您可以输入最多3个 GenderInfo 来实现给一张图中的最多3张人脸转换性别。
        :type GenderInfos: list of GenderInfo
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        """
        self.GenderInfos = None
        self.Image = None
        self.Url = None
        self.RspImgType = None


    def _deserialize(self, params):
        if params.get("GenderInfos") is not None:
            self.GenderInfos = []
            for item in params.get("GenderInfos"):
                obj = GenderInfo()
                obj._deserialize(item)
                self.GenderInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SwapGenderPicResponse(AbstractModel):
    """SwapGenderPic返回参数结构体

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        