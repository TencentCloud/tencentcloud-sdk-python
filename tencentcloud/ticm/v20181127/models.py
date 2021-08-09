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
        """
        :param Name: 识别出人脸对应的候选人数组。当前返回相似度最高的候选人。\n        :type Name: str\n        :param Confidence: 相似度，0-100之间。\n        :type Confidence: int\n        """
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
        


class DescribeVideoTaskRequest(AbstractModel):
    """DescribeVideoTask请求参数结构体

    """

    def __init__(self):
        """
        :param VodTaskId: 需要查询的视频审核的任务ID\n        :type VodTaskId: str\n        """
        self.VodTaskId = None


    def _deserialize(self, params):
        self.VodTaskId = params.get("VodTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoTaskResponse(AbstractModel):
    """DescribeVideoTask返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态，取值：
WAITING：等待中；
PROCESSING：处理中；
FINISH：已完成。\n        :type Status: str\n        :param BeginProcessTime: 任务开始执行的时间，采用 ISO 日期格式。\n        :type BeginProcessTime: str\n        :param FinishTime: 任务执行完毕的时间，采用 ISO 日期格式。\n        :type FinishTime: str\n        :param PornResult: 视频内容审核智能画面鉴黄任务的查询结果。\n        :type PornResult: :class:`tencentcloud.ticm.v20181127.models.VodPornReviewResult`\n        :param TerrorismResult: 视频内容审核智能画面鉴恐任务的查询结果。\n        :type TerrorismResult: :class:`tencentcloud.ticm.v20181127.models.VodTerrorismReviewResult`\n        :param PoliticalResult: 视频内容审核智能画面鉴政任务的查询结果。\n        :type PoliticalResult: :class:`tencentcloud.ticm.v20181127.models.VodPoliticalReviewResult`\n        :param PoliticalOcrResult: 视频内容审核 Ocr 文字鉴政任务的查询结果。\n        :type PoliticalOcrResult: :class:`tencentcloud.ticm.v20181127.models.VodPoliticalOcrReviewResult`\n        :param PornAsrResult: 视频内容审核 Asr 文字鉴黄任务的查询结果。\n        :type PornAsrResult: :class:`tencentcloud.ticm.v20181127.models.VodPornAsrReviewResult`\n        :param PoliticalAsrResult: 视频内容审核 Asr 文字鉴政任务的查询结果。\n        :type PoliticalAsrResult: :class:`tencentcloud.ticm.v20181127.models.VodPoliticalAsrReviewResult`\n        :param PornOcrResult: 视频内容审核 Ocr 文字鉴黄任务的查询结果。\n        :type PornOcrResult: :class:`tencentcloud.ticm.v20181127.models.VodPornOcrResult`\n        :param MetaData: 原始视频的元信息。\n        :type MetaData: :class:`tencentcloud.ticm.v20181127.models.VodMetaData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.PornResult = None
        self.TerrorismResult = None
        self.PoliticalResult = None
        self.PoliticalOcrResult = None
        self.PornAsrResult = None
        self.PoliticalAsrResult = None
        self.PornOcrResult = None
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("PornResult") is not None:
            self.PornResult = VodPornReviewResult()
            self.PornResult._deserialize(params.get("PornResult"))
        if params.get("TerrorismResult") is not None:
            self.TerrorismResult = VodTerrorismReviewResult()
            self.TerrorismResult._deserialize(params.get("TerrorismResult"))
        if params.get("PoliticalResult") is not None:
            self.PoliticalResult = VodPoliticalReviewResult()
            self.PoliticalResult._deserialize(params.get("PoliticalResult"))
        if params.get("PoliticalOcrResult") is not None:
            self.PoliticalOcrResult = VodPoliticalOcrReviewResult()
            self.PoliticalOcrResult._deserialize(params.get("PoliticalOcrResult"))
        if params.get("PornAsrResult") is not None:
            self.PornAsrResult = VodPornAsrReviewResult()
            self.PornAsrResult._deserialize(params.get("PornAsrResult"))
        if params.get("PoliticalAsrResult") is not None:
            self.PoliticalAsrResult = VodPoliticalAsrReviewResult()
            self.PoliticalAsrResult._deserialize(params.get("PoliticalAsrResult"))
        if params.get("PornOcrResult") is not None:
            self.PornOcrResult = VodPornOcrResult()
            self.PornOcrResult._deserialize(params.get("PornOcrResult"))
        if params.get("MetaData") is not None:
            self.MetaData = VodMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class DisgustResult(AbstractModel):
    """恶心识别结果。

    """

    def __init__(self):
        """
        :param Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误。\n        :type Code: int\n        :param Msg: 错误码描述信息。\n        :type Msg: str\n        :param Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规\n        :type Suggestion: str\n        :param Confidence: 图像恶心的分数，0-100之间，分数越高恶心几率越大。\n        :type Confidence: int\n        """
        self.Code = None
        self.Msg = None
        self.Suggestion = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceRect(AbstractModel):
    """识别出的人脸在图片中的位置。

    """

    def __init__(self):
        """
        :param X: 人脸区域左上角横坐标。\n        :type X: int\n        :param Y: 人脸区域左上角纵坐标。\n        :type Y: int\n        :param Width: 人脸区域宽度。\n        :type Width: int\n        :param Height: 人脸区域高度。\n        :type Height: int\n        """
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
        


class FaceResult(AbstractModel):
    """人脸识别结果。

    """

    def __init__(self):
        """
        :param FaceRect: 检测出的人脸框位置。\n        :type FaceRect: :class:`tencentcloud.ticm.v20181127.models.FaceRect`\n        :param Candidates: 候选人列表。当前返回相似度最高的候选人。\n        :type Candidates: list of Candidate\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationRequest(AbstractModel):
    """ImageModeration请求参数结构体

    """

    def __init__(self):
        """
        :param Scenes: 本次调用支持的识别场景，可选值如下：
1. PORN，即色情识别
2. TERRORISM，即暴恐识别
3. POLITICS，即政治敏感识别

支持多场景（Scenes）一起检测。例如，使用 Scenes=["PORN", "TERRORISM"]，即对一张图片同时进行色情识别和暴恐识别。\n        :type Scenes: list of str\n        :param ImageUrl: 图片URL地址。 
图片限制： 
 • 图片格式：PNG、JPG、JPEG。 
 • 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 
 • 图片像素：大于50*50像素，否则影响识别效果； 
 • 长宽比：长边：短边<5； 
接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。\n        :type ImageUrl: str\n        :param Config: 预留字段，后期用于展示更多识别信息。\n        :type Config: str\n        :param Extra: 透传字段，透传简单信息。\n        :type Extra: str\n        :param ImageBase64: 图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。\n        :type ImageBase64: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回参数结构体

    """

    def __init__(self):
        """
        :param Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规\n        :type Suggestion: str\n        :param PornResult: 色情识别结果。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PornResult: :class:`tencentcloud.ticm.v20181127.models.PornResult`\n        :param TerrorismResult: 暴恐识别结果。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TerrorismResult: :class:`tencentcloud.ticm.v20181127.models.TerrorismResult`\n        :param PoliticsResult: 政治敏感识别结果。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PoliticsResult: :class:`tencentcloud.ticm.v20181127.models.PoliticsResult`\n        :param Extra: 透传字段，透传简单信息。\n        :type Extra: str\n        :param DisgustResult: 恶心内容识别结果。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DisgustResult: :class:`tencentcloud.ticm.v20181127.models.DisgustResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
-1401表示图片不符合规范。\n        :type Code: int\n        :param Msg: 错误码描述信息。\n        :type Msg: str\n        :param Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规\n        :type Suggestion: str\n        :param Confidence: 图像涉政的分数，0-100之间，分数越高涉政几率越大。
Type为DNA时：
0到75，Suggestion建议为PASS
75到90，Suggestion建议为REVIEW
90到100，Suggestion建议为BLOCK
Type为FACE时：
0到55，Suggestion建议为PASS
55到60，Suggestion建议为REVIEW
60到100，Suggestion建议为BLOCK\n        :type Confidence: int\n        :param FaceResults: Type取值为‘FACE’时，人脸识别的结果列表。基于图片中实际检测到的人脸数，返回数组最大值不超过5个。\n        :type FaceResults: list of FaceResult\n        :param Type: 取值'DNA' 或‘FACE’。DNA表示结论和置信度来自图像指纹，FACE表示结论和置信度来自人脸识别。\n        :type Type: str\n        :param AdvancedInfo: 鉴政识别返回的详细标签后期开放。\n        :type AdvancedInfo: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornResult(AbstractModel):
    """色情识别结果。

    """

    def __init__(self):
        """
        :param Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误，
-1400表示图片解码失败。\n        :type Code: int\n        :param Msg: 错误码描述信息。\n        :type Msg: str\n        :param Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规\n        :type Suggestion: str\n        :param Confidence: 算法对于Suggestion的置信度，0-100之间，值越高，表示对于Suggestion越确定。\n        :type Confidence: int\n        :param AdvancedInfo: 预留字段，后期用于展示更多识别信息。\n        :type AdvancedInfo: str\n        :param Type: 取值'LABEL‘，LABEL表示结论和置信度来自标签分类。\n        :type Type: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismResult(AbstractModel):
    """暴恐识别结果。

    """

    def __init__(self):
        """
        :param Code: 该识别场景的错误码：
0表示成功，
-1表示系统错误，
-2表示引擎错误，
-1400表示图片解码失败。\n        :type Code: int\n        :param Msg: 错误码描述信息。\n        :type Msg: str\n        :param Suggestion: 识别场景的审核结论：
PASS：正常
REVIEW：疑似
BLOCK：违规\n        :type Suggestion: str\n        :param Confidence: 图像涉恐的分数，0-100之间，分数越高涉恐几率越大。
Type为LABEL时：
0到86，Suggestion建议为PASS
86到91，Suggestion建议为REVIEW
91到100，Suggestion建议为BLOCK
Type为FACE时：
0到55，Suggestion建议为PASS
55到60，Suggestion建议为REVIEW
60到100，Suggestion建议为BLOCK\n        :type Confidence: int\n        :param FaceResults: Type取值为‘FACE’时，人脸识别的结果列表。基于图片中实际检测到的人脸数，返回数组最大值不超过5个。\n        :type FaceResults: list of FaceResult\n        :param AdvancedInfo: 暴恐识别返回的详细标签后期开放。\n        :type AdvancedInfo: str\n        :param Type: 取值'LABEL' 或‘FACE’，LABEL表示结论和置信度来自标签分类，FACE表示结论和置信度来自人脸识别。\n        :type Type: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoModerationRequest(AbstractModel):
    """VideoModeration请求参数结构体

    """

    def __init__(self):
        """
        :param VideoUrl: 需要审核的视频的URL地址\n        :type VideoUrl: str\n        :param DeveloperId: 开发者标识\n        :type DeveloperId: str\n        :param CBUrl: 审核完成后回调地址\n        :type CBUrl: str\n        :param Extra: 透传字段，透传简单信息。\n        :type Extra: str\n        """
        self.VideoUrl = None
        self.DeveloperId = None
        self.CBUrl = None
        self.Extra = None


    def _deserialize(self, params):
        self.VideoUrl = params.get("VideoUrl")
        self.DeveloperId = params.get("DeveloperId")
        self.CBUrl = params.get("CBUrl")
        self.Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoModerationResponse(AbstractModel):
    """VideoModeration返回参数结构体

    """

    def __init__(self):
        """
        :param VodTaskId: 视频审核任务ID\n        :type VodTaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.VodTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VodTaskId = params.get("VodTaskId")
        self.RequestId = params.get("RequestId")


class VodAsrTextSegmentItem(AbstractModel):
    """内容审核 Asr 文字审核嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTimeOffset: float\n        :param Confidence: 嫌疑片段置信度。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: float\n        :param Suggestion: 嫌疑片段审核结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Suggestion: str\n        :param KeywordSet: 嫌疑关键词列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeywordSet: list of str\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodAudioStreamItem(AbstractModel):
    """文件音频流信息

    """

    def __init__(self):
        """
        :param Bitrate: 音频流的码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bitrate: int\n        :param SamplingRate: 音频流的采样率，单位：hz。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SamplingRate: int\n        :param Codec: 音频流的编码格式，例如 aac。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Codec: str\n        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodMetaData(AbstractModel):
    """媒体文件元信息。

    """

    def __init__(self):
        """
        :param Size: 上传的媒体文件大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Size: int\n        :param Container: 容器类型，例如 m4a，mp4 等。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Container: str\n        :param Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bitrate: int\n        :param Height: 视频流高度的最大值，单位：px。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Height: int\n        :param Width: 视频流宽度的最大值，单位：px。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Width: int\n        :param Duration: 视频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Duration: float\n        :param Rotate: 视频拍摄时的选择角度，单位：度。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Rotate: int\n        :param VideoStreamSet: 视频流信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VideoStreamSet: list of VodVideoStreamItem\n        :param AudioStreamSet: 音频流信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AudioStreamSet: list of VodAudioStreamItem\n        :param VideoDuration: 视频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VideoDuration: float\n        :param AudioDuration: 音频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AudioDuration: float\n        """
        self.Size = None
        self.Container = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.Rotate = None
        self.VideoStreamSet = None
        self.AudioStreamSet = None
        self.VideoDuration = None
        self.AudioDuration = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Container = params.get("Container")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        self.Rotate = params.get("Rotate")
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = VodVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = VodAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        self.VideoDuration = params.get("VideoDuration")
        self.AudioDuration = params.get("AudioDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodOcrTextSegmentItem(AbstractModel):
    """内容审核 Ocr 文字审核嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTimeOffset: float\n        :param Confidence: 嫌疑片段置信度。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: float\n        :param Suggestion: 嫌疑片段审核结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Suggestion: str\n        :param KeywordSet: 嫌疑关键词列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeywordSet: list of str\n        :param AreaCoordSet: 嫌疑文字出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AreaCoordSet: list of int\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPoliticalAsrReviewResult(AbstractModel):
    """内容审核 Asr 文字鉴政、敏感任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: int\n        :param Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Msg: str\n        :param Confidence: 嫌疑片段审核结果建议，取值范围：
pass。
review。
block。

Asr 文字涉政、敏感评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: float\n        :param Suggestion: Asr 文字涉政、敏感结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Suggestion: str\n        :param SegmentSet: Asr 文字有涉政、敏感嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SegmentSet: list of VodAsrTextSegmentItem\n        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPoliticalOcrReviewResult(AbstractModel):
    """内容审核 Ocr 文字鉴政、敏感任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: int\n        :param Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Msg: str\n        :param Confidence: Ocr 文字涉政、敏感评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: Ocr 文字涉政、敏感结果建议，取值范围：
pass。
review。
block。\n        :type Suggestion: str\n        :param SegmentSet: Ocr 文字有涉政、敏感嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SegmentSet: list of VodOcrTextSegmentItem\n        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPoliticalReviewResult(AbstractModel):
    """涉政信息

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: int\n        :param Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Msg: str\n        :param Confidence: 视频涉政评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: float\n        :param Suggestion: 涉政结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Suggestion: str\n        :param Label: 视频鉴政结果标签，取值范围：
politician：政治人物。
violation_photo：违规图标。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Label: str\n        :param SegmentSet: 有涉政嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SegmentSet: list of VodPoliticalReviewSegmentItem\n        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodPoliticalReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPoliticalReviewSegmentItem(AbstractModel):
    """内容审核鉴政任务结果类型

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTimeOffset: float\n        :param Confidence: 嫌疑片段涉政分数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: float\n        :param Suggestion: 嫌疑片段鉴政结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Suggestion: str\n        :param Name: 涉政人物、违规图标名字。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Label: 嫌疑片段鉴政结果标签。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Label: str\n        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Url: str\n        :param PicUrlExpireTimeStamp: 嫌疑图片 URL 失效时间，使用 ISO 日期格式。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PicUrlExpireTimeStamp: int\n        :param AreaCoordSet: 涉政人物、违规图标出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AreaCoordSet: list of int\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.Name = None
        self.Label = None
        self.Url = None
        self.PicUrlExpireTimeStamp = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Name = params.get("Name")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPornAsrReviewResult(AbstractModel):
    """Asr 文字涉黄信息

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: int\n        :param Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Msg: str\n        :param Confidence: Asr 文字涉黄评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: float\n        :param Suggestion: Asr 文字涉黄结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Suggestion: str\n        :param SegmentSet: Asr 文字有涉黄嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SegmentSet: list of VodAsrTextSegmentItem\n        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPornOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴黄任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: int\n        :param Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Msg: str\n        :param Confidence: Ocr 文字涉黄评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: float\n        :param Suggestion: Ocr 文字涉黄结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Suggestion: str\n        :param SegmentSet: Ocr 文字有涉黄嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SegmentSet: list of VodOcrTextSegmentItem\n        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPornReviewResult(AbstractModel):
    """内容审核鉴黄任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: int\n        :param Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Msg: str\n        :param Confidence: 视频鉴黄评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: float\n        :param Suggestion: 鉴黄结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Suggestion: str\n        :param Label: 视频鉴黄结果标签，取值范围：
porn：色情。
sexy：性感。
vulgar：低俗。
intimacy：亲密行为。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Label: str\n        :param SegmentSet: 有涉黄嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SegmentSet: list of VodPornReviewSegmentItem\n        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodPornReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodPornReviewSegmentItem(AbstractModel):
    """内容审核涉黄/暴恐嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTimeOffset: float\n        :param Confidence: 嫌疑片段涉黄分数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: float\n        :param Label: 嫌疑片段鉴黄结果标签。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Label: str\n        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Suggestion: str\n        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Url: str\n        :param PicUrlExpireTimeStamp: 嫌疑图片 URL 失效时间，使用 ISO 日期格式。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PicUrlExpireTimeStamp: int\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Label = None
        self.Suggestion = None
        self.Url = None
        self.PicUrlExpireTimeStamp = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Url = params.get("Url")
        self.PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodTerrorismReviewResult(AbstractModel):
    """暴恐信息

    """

    def __init__(self):
        """
        :param Confidence: 视频暴恐评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: float\n        :param Suggestion: 暴恐结果建议，取值范围：
pass。
review。
block。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Suggestion: str\n        :param Label: 视频暴恐结果标签，取值范围：
guns：武器枪支。
crowd：人群聚集。
police：警察部队。
bloody：血腥画面。
banners：暴恐旗帜。
militant：武装分子。
explosion：爆炸火灾。
terrorists：暴恐人物。

注意：此字段可能返回 null，表示取不到有效值。\n        :type Label: str\n        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param Code: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: int\n        :param Msg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Msg: str\n        :param SegmentSet: 有暴恐嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SegmentSet: list of VodPornReviewSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Status = None
        self.Code = None
        self.Msg = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodPornReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VodVideoStreamItem(AbstractModel):
    """文件视频流信息

    """

    def __init__(self):
        """
        :param Bitrate: 视频流的码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bitrate: int\n        :param Height: 视频流的高度，单位：px。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Height: int\n        :param Width: 视频流的宽度，单位：px。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Width: int\n        :param Codec: 视频流的编码格式，例如 h264。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Codec: str\n        :param Fps: 帧率，单位：hz。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Fps: int\n        """
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Codec = None
        self.Fps = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        