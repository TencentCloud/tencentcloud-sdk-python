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


class Candidate(AbstractModel):
    """识别出人脸对应的候选人。

    """

    def __init__(self):
        r"""
        :param _Name: 识别出人脸对应的候选人数组。当前返回相似度最高的候选人。
        :type Name: str
        :param _Confidence: 相似度，0-100之间。
        :type Confidence: int
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
        


class DescribeVideoTaskRequest(AbstractModel):
    """DescribeVideoTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VodTaskId: 需要查询的视频审核的任务ID
        :type VodTaskId: str
        """
        self._VodTaskId = None

    @property
    def VodTaskId(self):
        return self._VodTaskId

    @VodTaskId.setter
    def VodTaskId(self, VodTaskId):
        self._VodTaskId = VodTaskId


    def _deserialize(self, params):
        self._VodTaskId = params.get("VodTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoTaskResponse(AbstractModel):
    """DescribeVideoTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，取值：
WAITING：等待中；
PROCESSING：处理中；
FINISH：已完成。
        :type Status: str
        :param _BeginProcessTime: 任务开始执行的时间，采用 ISO 日期格式。
        :type BeginProcessTime: str
        :param _FinishTime: 任务执行完毕的时间，采用 ISO 日期格式。
        :type FinishTime: str
        :param _PornResult: 视频内容审核智能画面鉴黄任务的查询结果。
        :type PornResult: :class:`tencentcloud.ticm.v20181127.models.VodPornReviewResult`
        :param _TerrorismResult: 视频内容审核智能画面鉴恐任务的查询结果。
        :type TerrorismResult: :class:`tencentcloud.ticm.v20181127.models.VodTerrorismReviewResult`
        :param _PoliticalResult: 视频内容审核智能画面鉴政任务的查询结果。
        :type PoliticalResult: :class:`tencentcloud.ticm.v20181127.models.VodPoliticalReviewResult`
        :param _PoliticalOcrResult: 视频内容审核 Ocr 文字鉴政任务的查询结果。
        :type PoliticalOcrResult: :class:`tencentcloud.ticm.v20181127.models.VodPoliticalOcrReviewResult`
        :param _PornAsrResult: 视频内容审核 Asr 文字鉴黄任务的查询结果。
        :type PornAsrResult: :class:`tencentcloud.ticm.v20181127.models.VodPornAsrReviewResult`
        :param _PoliticalAsrResult: 视频内容审核 Asr 文字鉴政任务的查询结果。
        :type PoliticalAsrResult: :class:`tencentcloud.ticm.v20181127.models.VodPoliticalAsrReviewResult`
        :param _PornOcrResult: 视频内容审核 Ocr 文字鉴黄任务的查询结果。
        :type PornOcrResult: :class:`tencentcloud.ticm.v20181127.models.VodPornOcrResult`
        :param _MetaData: 原始视频的元信息。
        :type MetaData: :class:`tencentcloud.ticm.v20181127.models.VodMetaData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._BeginProcessTime = None
        self._FinishTime = None
        self._PornResult = None
        self._TerrorismResult = None
        self._PoliticalResult = None
        self._PoliticalOcrResult = None
        self._PornAsrResult = None
        self._PoliticalAsrResult = None
        self._PornOcrResult = None
        self._MetaData = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BeginProcessTime(self):
        return self._BeginProcessTime

    @BeginProcessTime.setter
    def BeginProcessTime(self, BeginProcessTime):
        self._BeginProcessTime = BeginProcessTime

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def PornResult(self):
        return self._PornResult

    @PornResult.setter
    def PornResult(self, PornResult):
        self._PornResult = PornResult

    @property
    def TerrorismResult(self):
        return self._TerrorismResult

    @TerrorismResult.setter
    def TerrorismResult(self, TerrorismResult):
        self._TerrorismResult = TerrorismResult

    @property
    def PoliticalResult(self):
        return self._PoliticalResult

    @PoliticalResult.setter
    def PoliticalResult(self, PoliticalResult):
        self._PoliticalResult = PoliticalResult

    @property
    def PoliticalOcrResult(self):
        return self._PoliticalOcrResult

    @PoliticalOcrResult.setter
    def PoliticalOcrResult(self, PoliticalOcrResult):
        self._PoliticalOcrResult = PoliticalOcrResult

    @property
    def PornAsrResult(self):
        return self._PornAsrResult

    @PornAsrResult.setter
    def PornAsrResult(self, PornAsrResult):
        self._PornAsrResult = PornAsrResult

    @property
    def PoliticalAsrResult(self):
        return self._PoliticalAsrResult

    @PoliticalAsrResult.setter
    def PoliticalAsrResult(self, PoliticalAsrResult):
        self._PoliticalAsrResult = PoliticalAsrResult

    @property
    def PornOcrResult(self):
        return self._PornOcrResult

    @PornOcrResult.setter
    def PornOcrResult(self, PornOcrResult):
        self._PornOcrResult = PornOcrResult

    @property
    def MetaData(self):
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._BeginProcessTime = params.get("BeginProcessTime")
        self._FinishTime = params.get("FinishTime")
        if params.get("PornResult") is not None:
            self._PornResult = VodPornReviewResult()
            self._PornResult._deserialize(params.get("PornResult"))
        if params.get("TerrorismResult") is not None:
            self._TerrorismResult = VodTerrorismReviewResult()
            self._TerrorismResult._deserialize(params.get("TerrorismResult"))
        if params.get("PoliticalResult") is not None:
            self._PoliticalResult = VodPoliticalReviewResult()
            self._PoliticalResult._deserialize(params.get("PoliticalResult"))
        if params.get("PoliticalOcrResult") is not None:
            self._PoliticalOcrResult = VodPoliticalOcrReviewResult()
            self._PoliticalOcrResult._deserialize(params.get("PoliticalOcrResult"))
        if params.get("PornAsrResult") is not None:
            self._PornAsrResult = VodPornAsrReviewResult()
            self._PornAsrResult._deserialize(params.get("PornAsrResult"))
        if params.get("PoliticalAsrResult") is not None:
            self._PoliticalAsrResult = VodPoliticalAsrReviewResult()
            self._PoliticalAsrResult._deserialize(params.get("PoliticalAsrResult"))
        if params.get("PornOcrResult") is not None:
            self._PornOcrResult = VodPornOcrResult()
            self._PornOcrResult._deserialize(params.get("PornOcrResult"))
        if params.get("MetaData") is not None:
            self._MetaData = VodMetaData()
            self._MetaData._deserialize(params.get("MetaData"))
        self._RequestId = params.get("RequestId")


class DisgustResult(AbstractModel):
    """恶心识别结果。

    """

    def __init__(self):
        r"""
        :param _Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误。
        :type Code: int
        :param _Msg: 错误码描述信息。
        :type Msg: str
        :param _Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规
        :type Suggestion: str
        :param _Confidence: 图像恶心的分数，0-100之间，分数越高恶心几率越大。
        :type Confidence: int
        """
        self._Code = None
        self._Msg = None
        self._Suggestion = None
        self._Confidence = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Suggestion = params.get("Suggestion")
        self._Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceRect(AbstractModel):
    """识别出的人脸在图片中的位置。

    """

    def __init__(self):
        r"""
        :param _X: 人脸区域左上角横坐标。
        :type X: int
        :param _Y: 人脸区域左上角纵坐标。
        :type Y: int
        :param _Width: 人脸区域宽度。
        :type Width: int
        :param _Height: 人脸区域高度。
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
        


class FaceResult(AbstractModel):
    """人脸识别结果。

    """

    def __init__(self):
        r"""
        :param _FaceRect: 检测出的人脸框位置。
        :type FaceRect: :class:`tencentcloud.ticm.v20181127.models.FaceRect`
        :param _Candidates: 候选人列表。当前返回相似度最高的候选人。
        :type Candidates: list of Candidate
        """
        self._FaceRect = None
        self._Candidates = None

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect

    @property
    def Candidates(self):
        return self._Candidates

    @Candidates.setter
    def Candidates(self, Candidates):
        self._Candidates = Candidates


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        if params.get("Candidates") is not None:
            self._Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self._Candidates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationRequest(AbstractModel):
    """ImageModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Scenes: 本次调用支持的识别场景，可选值如下：
1. PORN，即色情识别
2. TERRORISM，即暴恐识别
3. POLITICS，即政治敏感识别

支持多场景（Scenes）一起检测。例如，使用 Scenes=["PORN", "TERRORISM"]，即对一张图片同时进行色情识别和暴恐识别。
        :type Scenes: list of str
        :param _ImageUrl: 图片URL地址。 
图片限制： 
 • 图片格式：PNG、JPG、JPEG。 
 • 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
 • 图片像素：大于50*50像素，否则影响识别效果； 
 • 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。
        :type ImageUrl: str
        :param _Config: 预留字段，后期用于展示更多识别信息。
        :type Config: str
        :param _Extra: 透传字段，透传简单信息。
        :type Extra: str
        :param _ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。
        :type ImageBase64: str
        """
        self._Scenes = None
        self._ImageUrl = None
        self._Config = None
        self._Extra = None
        self._ImageBase64 = None

    @property
    def Scenes(self):
        return self._Scenes

    @Scenes.setter
    def Scenes(self, Scenes):
        self._Scenes = Scenes

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64


    def _deserialize(self, params):
        self._Scenes = params.get("Scenes")
        self._ImageUrl = params.get("ImageUrl")
        self._Config = params.get("Config")
        self._Extra = params.get("Extra")
        self._ImageBase64 = params.get("ImageBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规
        :type Suggestion: str
        :param _PornResult: 色情识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type PornResult: :class:`tencentcloud.ticm.v20181127.models.PornResult`
        :param _TerrorismResult: 暴恐识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TerrorismResult: :class:`tencentcloud.ticm.v20181127.models.TerrorismResult`
        :param _PoliticsResult: 政治敏感识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type PoliticsResult: :class:`tencentcloud.ticm.v20181127.models.PoliticsResult`
        :param _Extra: 透传字段，透传简单信息。
        :type Extra: str
        :param _DisgustResult: 恶心内容识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisgustResult: :class:`tencentcloud.ticm.v20181127.models.DisgustResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Suggestion = None
        self._PornResult = None
        self._TerrorismResult = None
        self._PoliticsResult = None
        self._Extra = None
        self._DisgustResult = None
        self._RequestId = None

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def PornResult(self):
        return self._PornResult

    @PornResult.setter
    def PornResult(self, PornResult):
        self._PornResult = PornResult

    @property
    def TerrorismResult(self):
        return self._TerrorismResult

    @TerrorismResult.setter
    def TerrorismResult(self, TerrorismResult):
        self._TerrorismResult = TerrorismResult

    @property
    def PoliticsResult(self):
        return self._PoliticsResult

    @PoliticsResult.setter
    def PoliticsResult(self, PoliticsResult):
        self._PoliticsResult = PoliticsResult

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def DisgustResult(self):
        return self._DisgustResult

    @DisgustResult.setter
    def DisgustResult(self, DisgustResult):
        self._DisgustResult = DisgustResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Suggestion = params.get("Suggestion")
        if params.get("PornResult") is not None:
            self._PornResult = PornResult()
            self._PornResult._deserialize(params.get("PornResult"))
        if params.get("TerrorismResult") is not None:
            self._TerrorismResult = TerrorismResult()
            self._TerrorismResult._deserialize(params.get("TerrorismResult"))
        if params.get("PoliticsResult") is not None:
            self._PoliticsResult = PoliticsResult()
            self._PoliticsResult._deserialize(params.get("PoliticsResult"))
        self._Extra = params.get("Extra")
        if params.get("DisgustResult") is not None:
            self._DisgustResult = DisgustResult()
            self._DisgustResult._deserialize(params.get("DisgustResult"))
        self._RequestId = params.get("RequestId")


class PoliticsResult(AbstractModel):
    """政治敏感识别结果。

    """

    def __init__(self):
        r"""
        :param _Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误，
-1400表示图片解码失败，
-1401表示图片不符合规范。
        :type Code: int
        :param _Msg: 错误码描述信息。
        :type Msg: str
        :param _Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规
        :type Suggestion: str
        :param _Confidence: 图像涉政的分数，0-100之间，分数越高涉政几率越大。
Type为DNA时：
0到75，Suggestion建议为PASS
75到90，Suggestion建议为REVIEW
90到100，Suggestion建议为BLOCK
Type为FACE时：
0到55，Suggestion建议为PASS
55到60，Suggestion建议为REVIEW
60到100，Suggestion建议为BLOCK
        :type Confidence: int
        :param _FaceResults: Type取值为‘FACE’时，人脸识别的结果列表。基于图片中实际检测到的人脸数，返回数组最大值不超过5个。
        :type FaceResults: list of FaceResult
        :param _Type: 取值'DNA' 或‘FACE’。DNA表示结论和置信度来自图像指纹，FACE表示结论和置信度来自人脸识别。
        :type Type: str
        :param _AdvancedInfo: 鉴政识别返回的详细标签后期开放。
        :type AdvancedInfo: str
        """
        self._Code = None
        self._Msg = None
        self._Suggestion = None
        self._Confidence = None
        self._FaceResults = None
        self._Type = None
        self._AdvancedInfo = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def FaceResults(self):
        return self._FaceResults

    @FaceResults.setter
    def FaceResults(self, FaceResults):
        self._FaceResults = FaceResults

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Suggestion = params.get("Suggestion")
        self._Confidence = params.get("Confidence")
        if params.get("FaceResults") is not None:
            self._FaceResults = []
            for item in params.get("FaceResults"):
                obj = FaceResult()
                obj._deserialize(item)
                self._FaceResults.append(obj)
        self._Type = params.get("Type")
        self._AdvancedInfo = params.get("AdvancedInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornResult(AbstractModel):
    """色情识别结果。

    """

    def __init__(self):
        r"""
        :param _Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误，
-1400表示图片解码失败。
        :type Code: int
        :param _Msg: 错误码描述信息。
        :type Msg: str
        :param _Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规
        :type Suggestion: str
        :param _Confidence: 算法对于Suggestion的置信度，0-100之间，值越高，表示对于Suggestion越确定。
        :type Confidence: int
        :param _AdvancedInfo: 预留字段，后期用于展示更多识别信息。
        :type AdvancedInfo: str
        :param _Type: 取值'LABEL‘，LABEL表示结论和置信度来自标签分类。
        :type Type: str
        """
        self._Code = None
        self._Msg = None
        self._Suggestion = None
        self._Confidence = None
        self._AdvancedInfo = None
        self._Type = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Suggestion = params.get("Suggestion")
        self._Confidence = params.get("Confidence")
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismResult(AbstractModel):
    """暴恐识别结果。

    """

    def __init__(self):
        r"""
        :param _Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误，
-1400表示图片解码失败。
        :type Code: int
        :param _Msg: 错误码描述信息。
        :type Msg: str
        :param _Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规
        :type Suggestion: str
        :param _Confidence: 图像涉恐的分数，0-100之间，分数越高涉恐几率越大。
Type为LABEL时：
0到86，Suggestion建议为PASS
86到91，Suggestion建议为REVIEW
91到100，Suggestion建议为BLOCK
Type为FACE时：
0到55，Suggestion建议为PASS
55到60，Suggestion建议为REVIEW
60到100，Suggestion建议为BLOCK
        :type Confidence: int
        :param _FaceResults: Type取值为‘FACE’时，人脸识别的结果列表。基于图片中实际检测到的人脸数，返回数组最大值不超过5个。
        :type FaceResults: list of FaceResult
        :param _AdvancedInfo: 暴恐识别返回的详细标签后期开放。
        :type AdvancedInfo: str
        :param _Type: 取值'LABEL' 或‘FACE’，LABEL表示结论和置信度来自标签分类，FACE表示结论和置信度来自人脸识别。
        :type Type: str
        """
        self._Code = None
        self._Msg = None
        self._Suggestion = None
        self._Confidence = None
        self._FaceResults = None
        self._AdvancedInfo = None
        self._Type = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def FaceResults(self):
        return self._FaceResults

    @FaceResults.setter
    def FaceResults(self, FaceResults):
        self._FaceResults = FaceResults

    @property
    def AdvancedInfo(self):
        return self._AdvancedInfo

    @AdvancedInfo.setter
    def AdvancedInfo(self, AdvancedInfo):
        self._AdvancedInfo = AdvancedInfo

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Suggestion = params.get("Suggestion")
        self._Confidence = params.get("Confidence")
        if params.get("FaceResults") is not None:
            self._FaceResults = []
            for item in params.get("FaceResults"):
                obj = FaceResult()
                obj._deserialize(item)
                self._FaceResults.append(obj)
        self._AdvancedInfo = params.get("AdvancedInfo")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoModerationRequest(AbstractModel):
    """VideoModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoUrl: 需要审核的视频的URL地址
        :type VideoUrl: str
        :param _DeveloperId: 开发者标识
        :type DeveloperId: str
        :param _CBUrl: 审核完成后回调地址
        :type CBUrl: str
        :param _Extra: 透传字段，透传简单信息。
        :type Extra: str
        """
        self._VideoUrl = None
        self._DeveloperId = None
        self._CBUrl = None
        self._Extra = None

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def DeveloperId(self):
        return self._DeveloperId

    @DeveloperId.setter
    def DeveloperId(self, DeveloperId):
        self._DeveloperId = DeveloperId

    @property
    def CBUrl(self):
        return self._CBUrl

    @CBUrl.setter
    def CBUrl(self, CBUrl):
        self._CBUrl = CBUrl

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        self._DeveloperId = params.get("DeveloperId")
        self._CBUrl = params.get("CBUrl")
        self._Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoModerationResponse(AbstractModel):
    """VideoModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VodTaskId: 视频审核任务ID
        :type VodTaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VodTaskId = None
        self._RequestId = None

    @property
    def VodTaskId(self):
        return self._VodTaskId

    @VodTaskId.setter
    def VodTaskId(self, VodTaskId):
        self._VodTaskId = VodTaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VodTaskId = params.get("VodTaskId")
        self._RequestId = params.get("RequestId")


class VodAsrTextSegmentItem(AbstractModel):
    """内容审核 Asr 文字审核嫌疑片段

    """

    def __init__(self):
        r"""
        :param _StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param _EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param _Confidence: 嫌疑片段置信度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Suggestion: 嫌疑片段审核结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _KeywordSet: 嫌疑关键词列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeywordSet: list of str
        """
        self._StartTimeOffset = None
        self._EndTimeOffset = None
        self._Confidence = None
        self._Suggestion = None
        self._KeywordSet = None

    @property
    def StartTimeOffset(self):
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def KeywordSet(self):
        return self._KeywordSet

    @KeywordSet.setter
    def KeywordSet(self, KeywordSet):
        self._KeywordSet = KeywordSet


    def _deserialize(self, params):
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        self._KeywordSet = params.get("KeywordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodAudioStreamItem(AbstractModel):
    """文件音频流信息

    """

    def __init__(self):
        r"""
        :param _Bitrate: 音频流的码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param _SamplingRate: 音频流的采样率，单位：hz。
注意：此字段可能返回 null，表示取不到有效值。
        :type SamplingRate: int
        :param _Codec: 音频流的编码格式，例如 aac。
注意：此字段可能返回 null，表示取不到有效值。
        :type Codec: str
        """
        self._Bitrate = None
        self._SamplingRate = None
        self._Codec = None

    @property
    def Bitrate(self):
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def SamplingRate(self):
        return self._SamplingRate

    @SamplingRate.setter
    def SamplingRate(self, SamplingRate):
        self._SamplingRate = SamplingRate

    @property
    def Codec(self):
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec


    def _deserialize(self, params):
        self._Bitrate = params.get("Bitrate")
        self._SamplingRate = params.get("SamplingRate")
        self._Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodMetaData(AbstractModel):
    """媒体文件元信息。

    """

    def __init__(self):
        r"""
        :param _Size: 上传的媒体文件大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param _Container: 容器类型，例如 m4a，mp4 等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Container: str
        :param _Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param _Height: 视频流高度的最大值，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _Width: 视频流宽度的最大值，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Duration: 视频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: float
        :param _Rotate: 视频拍摄时的选择角度，单位：度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: int
        :param _VideoStreamSet: 视频流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoStreamSet: list of VodVideoStreamItem
        :param _AudioStreamSet: 音频流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioStreamSet: list of VodAudioStreamItem
        :param _VideoDuration: 视频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoDuration: float
        :param _AudioDuration: 音频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioDuration: float
        """
        self._Size = None
        self._Container = None
        self._Bitrate = None
        self._Height = None
        self._Width = None
        self._Duration = None
        self._Rotate = None
        self._VideoStreamSet = None
        self._AudioStreamSet = None
        self._VideoDuration = None
        self._AudioDuration = None

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Container(self):
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def Bitrate(self):
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Rotate(self):
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate

    @property
    def VideoStreamSet(self):
        return self._VideoStreamSet

    @VideoStreamSet.setter
    def VideoStreamSet(self, VideoStreamSet):
        self._VideoStreamSet = VideoStreamSet

    @property
    def AudioStreamSet(self):
        return self._AudioStreamSet

    @AudioStreamSet.setter
    def AudioStreamSet(self, AudioStreamSet):
        self._AudioStreamSet = AudioStreamSet

    @property
    def VideoDuration(self):
        return self._VideoDuration

    @VideoDuration.setter
    def VideoDuration(self, VideoDuration):
        self._VideoDuration = VideoDuration

    @property
    def AudioDuration(self):
        return self._AudioDuration

    @AudioDuration.setter
    def AudioDuration(self, AudioDuration):
        self._AudioDuration = AudioDuration


    def _deserialize(self, params):
        self._Size = params.get("Size")
        self._Container = params.get("Container")
        self._Bitrate = params.get("Bitrate")
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._Duration = params.get("Duration")
        self._Rotate = params.get("Rotate")
        if params.get("VideoStreamSet") is not None:
            self._VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = VodVideoStreamItem()
                obj._deserialize(item)
                self._VideoStreamSet.append(obj)
        if params.get("AudioStreamSet") is not None:
            self._AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = VodAudioStreamItem()
                obj._deserialize(item)
                self._AudioStreamSet.append(obj)
        self._VideoDuration = params.get("VideoDuration")
        self._AudioDuration = params.get("AudioDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodOcrTextSegmentItem(AbstractModel):
    """内容审核 Ocr 文字审核嫌疑片段

    """

    def __init__(self):
        r"""
        :param _StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param _EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param _Confidence: 嫌疑片段置信度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Suggestion: 嫌疑片段审核结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _KeywordSet: 嫌疑关键词列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeywordSet: list of str
        :param _AreaCoordSet: 嫌疑文字出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
注意：此字段可能返回 null，表示取不到有效值。
        :type AreaCoordSet: list of int
        """
        self._StartTimeOffset = None
        self._EndTimeOffset = None
        self._Confidence = None
        self._Suggestion = None
        self._KeywordSet = None
        self._AreaCoordSet = None

    @property
    def StartTimeOffset(self):
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def KeywordSet(self):
        return self._KeywordSet

    @KeywordSet.setter
    def KeywordSet(self, KeywordSet):
        self._KeywordSet = KeywordSet

    @property
    def AreaCoordSet(self):
        return self._AreaCoordSet

    @AreaCoordSet.setter
    def AreaCoordSet(self, AreaCoordSet):
        self._AreaCoordSet = AreaCoordSet


    def _deserialize(self, params):
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        self._KeywordSet = params.get("KeywordSet")
        self._AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPoliticalAsrReviewResult(AbstractModel):
    """内容审核 Asr 文字鉴政、敏感任务结果类型

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param _Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Confidence: 嫌疑片段审核结果建议，取值范围：
pass。
review。
block。

Asr 文字涉政、敏感评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Suggestion: Asr 文字涉政、敏感结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _SegmentSet: Asr 文字有涉政、敏感嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodAsrTextSegmentItem
        """
        self._Status = None
        self._Code = None
        self._Msg = None
        self._Confidence = None
        self._Suggestion = None
        self._SegmentSet = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def SegmentSet(self):
        return self._SegmentSet

    @SegmentSet.setter
    def SegmentSet(self, SegmentSet):
        self._SegmentSet = SegmentSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self._SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodAsrTextSegmentItem()
                obj._deserialize(item)
                self._SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPoliticalOcrReviewResult(AbstractModel):
    """内容审核 Ocr 文字鉴政、敏感任务结果类型

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param _Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Confidence: Ocr 文字涉政、敏感评分，分值为0到100。
        :type Confidence: float
        :param _Suggestion: Ocr 文字涉政、敏感结果建议，取值范围：
pass。
review。
block。
        :type Suggestion: str
        :param _SegmentSet: Ocr 文字有涉政、敏感嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodOcrTextSegmentItem
        """
        self._Status = None
        self._Code = None
        self._Msg = None
        self._Confidence = None
        self._Suggestion = None
        self._SegmentSet = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def SegmentSet(self):
        return self._SegmentSet

    @SegmentSet.setter
    def SegmentSet(self, SegmentSet):
        self._SegmentSet = SegmentSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self._SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodOcrTextSegmentItem()
                obj._deserialize(item)
                self._SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPoliticalReviewResult(AbstractModel):
    """涉政信息

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param _Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Confidence: 视频涉政评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Suggestion: 涉政结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Label: 视频鉴政结果标签，取值范围：
politician：政治人物。
violation_photo：违规图标。

注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _SegmentSet: 有涉政嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodPoliticalReviewSegmentItem
        """
        self._Status = None
        self._Code = None
        self._Msg = None
        self._Confidence = None
        self._Suggestion = None
        self._Label = None
        self._SegmentSet = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SegmentSet(self):
        return self._SegmentSet

    @SegmentSet.setter
    def SegmentSet(self, SegmentSet):
        self._SegmentSet = SegmentSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self._SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodPoliticalReviewSegmentItem()
                obj._deserialize(item)
                self._SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPoliticalReviewSegmentItem(AbstractModel):
    """内容审核鉴政任务结果类型

    """

    def __init__(self):
        r"""
        :param _StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param _EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param _Confidence: 嫌疑片段涉政分数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Suggestion: 嫌疑片段鉴政结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Name: 涉政人物、违规图标名字。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Label: 嫌疑片段鉴政结果标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _PicUrlExpireTimeStamp: 嫌疑图片 URL 失效时间，使用 ISO 日期格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type PicUrlExpireTimeStamp: int
        :param _AreaCoordSet: 涉政人物、违规图标出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
注意：此字段可能返回 null，表示取不到有效值。
        :type AreaCoordSet: list of int
        """
        self._StartTimeOffset = None
        self._EndTimeOffset = None
        self._Confidence = None
        self._Suggestion = None
        self._Name = None
        self._Label = None
        self._Url = None
        self._PicUrlExpireTimeStamp = None
        self._AreaCoordSet = None

    @property
    def StartTimeOffset(self):
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def PicUrlExpireTimeStamp(self):
        return self._PicUrlExpireTimeStamp

    @PicUrlExpireTimeStamp.setter
    def PicUrlExpireTimeStamp(self, PicUrlExpireTimeStamp):
        self._PicUrlExpireTimeStamp = PicUrlExpireTimeStamp

    @property
    def AreaCoordSet(self):
        return self._AreaCoordSet

    @AreaCoordSet.setter
    def AreaCoordSet(self, AreaCoordSet):
        self._AreaCoordSet = AreaCoordSet


    def _deserialize(self, params):
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        self._Name = params.get("Name")
        self._Label = params.get("Label")
        self._Url = params.get("Url")
        self._PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")
        self._AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPornAsrReviewResult(AbstractModel):
    """Asr 文字涉黄信息

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param _Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Confidence: Asr 文字涉黄评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Suggestion: Asr 文字涉黄结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _SegmentSet: Asr 文字有涉黄嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodAsrTextSegmentItem
        """
        self._Status = None
        self._Code = None
        self._Msg = None
        self._Confidence = None
        self._Suggestion = None
        self._SegmentSet = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def SegmentSet(self):
        return self._SegmentSet

    @SegmentSet.setter
    def SegmentSet(self, SegmentSet):
        self._SegmentSet = SegmentSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self._SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodAsrTextSegmentItem()
                obj._deserialize(item)
                self._SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPornOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴黄任务结果类型

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param _Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Confidence: Ocr 文字涉黄评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Suggestion: Ocr 文字涉黄结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _SegmentSet: Ocr 文字有涉黄嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodOcrTextSegmentItem
        """
        self._Status = None
        self._Code = None
        self._Msg = None
        self._Confidence = None
        self._Suggestion = None
        self._SegmentSet = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def SegmentSet(self):
        return self._SegmentSet

    @SegmentSet.setter
    def SegmentSet(self, SegmentSet):
        self._SegmentSet = SegmentSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self._SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodOcrTextSegmentItem()
                obj._deserialize(item)
                self._SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPornReviewResult(AbstractModel):
    """内容审核鉴黄任务结果类型

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param _Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Confidence: 视频鉴黄评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Suggestion: 鉴黄结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Label: 视频鉴黄结果标签，取值范围：
porn：色情。
sexy：性感。
vulgar：低俗。
intimacy：亲密行为。

注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _SegmentSet: 有涉黄嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodPornReviewSegmentItem
        """
        self._Status = None
        self._Code = None
        self._Msg = None
        self._Confidence = None
        self._Suggestion = None
        self._Label = None
        self._SegmentSet = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SegmentSet(self):
        return self._SegmentSet

    @SegmentSet.setter
    def SegmentSet(self, SegmentSet):
        self._SegmentSet = SegmentSet


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self._SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodPornReviewSegmentItem()
                obj._deserialize(item)
                self._SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPornReviewSegmentItem(AbstractModel):
    """内容审核涉黄/暴恐嫌疑片段

    """

    def __init__(self):
        r"""
        :param _StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param _EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param _Confidence: 嫌疑片段涉黄分数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Label: 嫌疑片段鉴黄结果标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _PicUrlExpireTimeStamp: 嫌疑图片 URL 失效时间，使用 ISO 日期格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type PicUrlExpireTimeStamp: int
        """
        self._StartTimeOffset = None
        self._EndTimeOffset = None
        self._Confidence = None
        self._Label = None
        self._Suggestion = None
        self._Url = None
        self._PicUrlExpireTimeStamp = None

    @property
    def StartTimeOffset(self):
        return self._StartTimeOffset

    @StartTimeOffset.setter
    def StartTimeOffset(self, StartTimeOffset):
        self._StartTimeOffset = StartTimeOffset

    @property
    def EndTimeOffset(self):
        return self._EndTimeOffset

    @EndTimeOffset.setter
    def EndTimeOffset(self, EndTimeOffset):
        self._EndTimeOffset = EndTimeOffset

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def PicUrlExpireTimeStamp(self):
        return self._PicUrlExpireTimeStamp

    @PicUrlExpireTimeStamp.setter
    def PicUrlExpireTimeStamp(self, PicUrlExpireTimeStamp):
        self._PicUrlExpireTimeStamp = PicUrlExpireTimeStamp


    def _deserialize(self, params):
        self._StartTimeOffset = params.get("StartTimeOffset")
        self._EndTimeOffset = params.get("EndTimeOffset")
        self._Confidence = params.get("Confidence")
        self._Label = params.get("Label")
        self._Suggestion = params.get("Suggestion")
        self._Url = params.get("Url")
        self._PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodTerrorismReviewResult(AbstractModel):
    """暴恐信息

    """

    def __init__(self):
        r"""
        :param _Confidence: 视频暴恐评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Suggestion: 暴恐结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _Label: 视频暴恐结果标签，取值范围：
guns：武器枪支。
crowd：人群聚集。
police：警察部队。
bloody：血腥画面。
banners：暴恐旗帜。
militant：武装分子。
explosion：爆炸火灾。
terrorists：暴恐人物。

注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param _Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _SegmentSet: 有暴恐嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodPornReviewSegmentItem
        """
        self._Confidence = None
        self._Suggestion = None
        self._Label = None
        self._Status = None
        self._Code = None
        self._Msg = None
        self._SegmentSet = None

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def SegmentSet(self):
        return self._SegmentSet

    @SegmentSet.setter
    def SegmentSet(self, SegmentSet):
        self._SegmentSet = SegmentSet


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._Status = params.get("Status")
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        if params.get("SegmentSet") is not None:
            self._SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodPornReviewSegmentItem()
                obj._deserialize(item)
                self._SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodVideoStreamItem(AbstractModel):
    """文件视频流信息

    """

    def __init__(self):
        r"""
        :param _Bitrate: 视频流的码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param _Height: 视频流的高度，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _Width: 视频流的宽度，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Codec: 视频流的编码格式，例如 h264。
注意：此字段可能返回 null，表示取不到有效值。
        :type Codec: str
        :param _Fps: 帧率，单位：hz。
注意：此字段可能返回 null，表示取不到有效值。
        :type Fps: int
        """
        self._Bitrate = None
        self._Height = None
        self._Width = None
        self._Codec = None
        self._Fps = None

    @property
    def Bitrate(self):
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Codec(self):
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps


    def _deserialize(self, params):
        self._Bitrate = params.get("Bitrate")
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._Codec = params.get("Codec")
        self._Fps = params.get("Fps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        