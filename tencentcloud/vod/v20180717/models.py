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


class AIAnalysisTemplateItem(AbstractModel):
    """AI 智能分析模板详情

    """

    def __init__(self):
        """
        :param Definition: 智能分析模板唯一标识。
        :type Definition: int
        :param Name: 智能分析模板名称。
        :type Name: str
        :param Comment: 智能分析模板描述信息。
        :type Comment: str
        :param ClassificationConfigure: 智能分类任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationConfigure: :class:`tencentcloud.vod.v20180717.models.ClassificationConfigureInfo`
        :param TagConfigure: 智能标签任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagConfigure: :class:`tencentcloud.vod.v20180717.models.TagConfigureInfo`
        :param CoverConfigure: 智能封面任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverConfigure: :class:`tencentcloud.vod.v20180717.models.CoverConfigureInfo`
        :param FrameTagConfigure: 智能按帧标签任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameTagConfigure: :class:`tencentcloud.vod.v20180717.models.FrameTagConfigureInfo`
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AdaptiveDynamicStreamingInfoItem(AbstractModel):
    """转自适应码流信息

    """

    def __init__(self):
        """
        :param Definition: 转自适应码流规格。
        :type Definition: int
        :param Package: 打包格式，可能为 hls 和 dash 两种。
        :type Package: str
        :param DrmType: 加密类型。
        :type DrmType: str
        :param Url: 播放地址。
        :type Url: str
        """
        self.Definition = None
        self.Package = None
        self.DrmType = None
        self.Url = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Package = params.get("Package")
        self.DrmType = params.get("DrmType")
        self.Url = params.get("Url")


class AdaptiveDynamicStreamingTaskInput(AbstractModel):
    """对视频转自适应码流的输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 转自适应码流模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisResult(AbstractModel):
    """智能分析结果

    """

    def __init__(self):
        """
        :param Type: 任务的类型，可以取的值有：
<li>Classification：智能分类</li>
<li>Cover：智能封面</li>
<li>Tag：智能标签</li>
<li>FrameTag：智能按帧标签</li>
        :type Type: str
        :param ClassificationTask: 视频内容分析智能分类任务的查询结果，当任务类型为 Classification 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskClassificationResult`
        :param CoverTask: 视频内容分析智能封面任务的查询结果，当任务类型为 Cover 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskCoverResult`
        :param TagTask: 视频内容分析智能标签任务的查询结果，当任务类型为 Tag 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskTagResult`
        :param FrameTagTask: 视频内容分析智能按帧标签任务的查询结果，当任务类型为 FrameTag 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameTagTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskFrameTagResult`
        """
        self.Type = None
        self.ClassificationTask = None
        self.CoverTask = None
        self.TagTask = None
        self.FrameTagTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("ClassificationTask") is not None:
            self.ClassificationTask = AiAnalysisTaskClassificationResult()
            self.ClassificationTask._deserialize(params.get("ClassificationTask"))
        if params.get("CoverTask") is not None:
            self.CoverTask = AiAnalysisTaskCoverResult()
            self.CoverTask._deserialize(params.get("CoverTask"))
        if params.get("TagTask") is not None:
            self.TagTask = AiAnalysisTaskTagResult()
            self.TagTask._deserialize(params.get("TagTask"))
        if params.get("FrameTagTask") is not None:
            self.FrameTagTask = AiAnalysisTaskFrameTagResult()
            self.FrameTagTask._deserialize(params.get("FrameTagTask"))


class AiAnalysisTaskClassificationInput(AbstractModel):
    """智能分类任务输入类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能分类模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskClassificationOutput(AbstractModel):
    """智能分类结果信息

    """

    def __init__(self):
        """
        :param ClassificationSet: 视频智能分类列表。
        :type ClassificationSet: list of MediaAiAnalysisClassificationItem
        """
        self.ClassificationSet = None


    def _deserialize(self, params):
        if params.get("ClassificationSet") is not None:
            self.ClassificationSet = []
            for item in params.get("ClassificationSet"):
                obj = MediaAiAnalysisClassificationItem()
                obj._deserialize(item)
                self.ClassificationSet.append(obj)


class AiAnalysisTaskClassificationResult(AbstractModel):
    """智能分类任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 智能分类任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskClassificationInput`
        :param Output: 智能分类任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskClassificationOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskClassificationInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskClassificationOutput()
            self.Output._deserialize(params.get("Output"))


class AiAnalysisTaskCoverInput(AbstractModel):
    """智能分类任务输入类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能封面模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskCoverOutput(AbstractModel):
    """智能封面结果信息

    """

    def __init__(self):
        """
        :param CoverSet: 智能封面列表。
        :type CoverSet: list of MediaAiAnalysisCoverItem
        """
        self.CoverSet = None


    def _deserialize(self, params):
        if params.get("CoverSet") is not None:
            self.CoverSet = []
            for item in params.get("CoverSet"):
                obj = MediaAiAnalysisCoverItem()
                obj._deserialize(item)
                self.CoverSet.append(obj)


class AiAnalysisTaskCoverResult(AbstractModel):
    """智能封面结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 智能封面任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskCoverInput`
        :param Output: 智能封面任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskCoverOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskCoverInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskCoverOutput()
            self.Output._deserialize(params.get("Output"))


class AiAnalysisTaskFrameTagInput(AbstractModel):
    """智能按帧标签任务输入类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能按帧标签模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskFrameTagOutput(AbstractModel):
    """智能按帧标签结果信息

    """

    def __init__(self):
        """
        :param SegmentSet: 视频按帧标签列表。
        :type SegmentSet: list of MediaAiAnalysisFrameTagSegmentItem
        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaAiAnalysisFrameTagSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiAnalysisTaskFrameTagResult(AbstractModel):
    """智能按帧标签结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 智能按帧标签任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskFrameTagInput`
        :param Output: 智能按帧标签任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskFrameTagOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskFrameTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskFrameTagOutput()
            self.Output._deserialize(params.get("Output"))


class AiAnalysisTaskInput(AbstractModel):
    """AI 视频智能分析输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 视频内容分析模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskTagInput(AbstractModel):
    """智能标签任务输入类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能标签模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskTagOutput(AbstractModel):
    """智能标签结果信息

    """

    def __init__(self):
        """
        :param TagSet: 视频智能标签列表。
        :type TagSet: list of MediaAiAnalysisTagItem
        """
        self.TagSet = None


    def _deserialize(self, params):
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)


class AiAnalysisTaskTagResult(AbstractModel):
    """智能标签结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 智能标签任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskTagInput`
        :param Output: 智能标签任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskTagOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskTagOutput()
            self.Output._deserialize(params.get("Output"))


class AiContentReviewResult(AbstractModel):
    """内容审核结果

    """

    def __init__(self):
        """
        :param Type: 任务的类型，可以取的值有：
<li>Porn：图片鉴黄</li>
<li>Terrorism：图片鉴恐</li>
<li>Political：图片鉴政</li>
<li>Porn.Asr：Asr 文字鉴黄</li>
<li>Porn.Ocr：Ocr 文字鉴黄</li>
<li>Political.Asr：Asr 文字鉴政</li>
<li>Political.Ocr：Ocr 文字鉴政</li>
        :type Type: str
        :param PornTask: 视频内容审核智能画面鉴黄任务的查询结果，当任务类型为 Porn 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PornTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPornResult`
        :param TerrorismTask: 视频内容审核智能画面鉴恐任务的查询结果，当任务类型为 Terrorism 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TerrorismTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskTerrorismResult`
        :param PoliticalTask: 视频内容审核智能画面鉴政任务的查询结果，当任务类型为 Political 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PoliticalTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPoliticalResult`
        :param PornAsrTask: 视频内容审核 Asr 文字鉴黄任务的查询结果，当任务类型为 Porn.Asr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PornAsrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPornAsrResult`
        :param PornOcrTask: 视频内容审核 Ocr 文字鉴黄任务的查询结果，当任务类型为 Porn.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PornOcrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPornOcrResult`
        :param PoliticalAsrTask: 视频内容审核 Asr 文字鉴政任务的查询结果，当任务类型为 Political.Asr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PoliticalAsrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPoliticalAsrResult`
        :param PoliticalOcrTask: 视频内容审核 Ocr 文字鉴政任务的查询结果，当任务类型为 Political.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PoliticalOcrTask: :class:`tencentcloud.vod.v20180717.models.AiReviewTaskPoliticalOcrResult`
        """
        self.Type = None
        self.PornTask = None
        self.TerrorismTask = None
        self.PoliticalTask = None
        self.PornAsrTask = None
        self.PornOcrTask = None
        self.PoliticalAsrTask = None
        self.PoliticalOcrTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("PornTask") is not None:
            self.PornTask = AiReviewTaskPornResult()
            self.PornTask._deserialize(params.get("PornTask"))
        if params.get("TerrorismTask") is not None:
            self.TerrorismTask = AiReviewTaskTerrorismResult()
            self.TerrorismTask._deserialize(params.get("TerrorismTask"))
        if params.get("PoliticalTask") is not None:
            self.PoliticalTask = AiReviewTaskPoliticalResult()
            self.PoliticalTask._deserialize(params.get("PoliticalTask"))
        if params.get("PornAsrTask") is not None:
            self.PornAsrTask = AiReviewTaskPornAsrResult()
            self.PornAsrTask._deserialize(params.get("PornAsrTask"))
        if params.get("PornOcrTask") is not None:
            self.PornOcrTask = AiReviewTaskPornOcrResult()
            self.PornOcrTask._deserialize(params.get("PornOcrTask"))
        if params.get("PoliticalAsrTask") is not None:
            self.PoliticalAsrTask = AiReviewTaskPoliticalAsrResult()
            self.PoliticalAsrTask._deserialize(params.get("PoliticalAsrTask"))
        if params.get("PoliticalOcrTask") is not None:
            self.PoliticalOcrTask = AiReviewTaskPoliticalOcrResult()
            self.PoliticalOcrTask._deserialize(params.get("PoliticalOcrTask"))


class AiContentReviewTaskInput(AbstractModel):
    """智能内容审核任务类型

    """

    def __init__(self):
        """
        :param Definition: 视频内容审核模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionResult(AbstractModel):
    """智能识别结果。

    """

    def __init__(self):
        """
        :param Type: 任务的类型，取值范围：
<li>FaceRecognition：人脸识别，</li>
<li>AsrFullTextRecognition：语音全文识别，</li>
<li>OcrFullTextRecognition：文本全文识别，</li>
<li>AsrWordsRecognition：用户自定义语音识别，</li>
<li>OcrWordsRecognition：用户自定义文本识别，</li>
<li>HeadTailRecognition：视频片头片尾识别，</li>
<li>ObjectRecognition：物体识别。</li>
        :type Type: str
        :param FaceRecognitionTask: 人脸识别结果，当 Type 为 
 FaceRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskFaceResult`
        :param AsrFullTextTask: 语音全文识别结果，当 Type 为
 AsrFullTextRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrFullTextTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrFullTextResult`
        :param OcrFullTextTask: 文本全文识别结果，当 Type 为
 OcrFullTextRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrFullTextTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrFullTextResult`
        :param AsrWordsTask: 用户自定义语音识别结果集，当 Type 为
 AsrWordsRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrWordsTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResult`
        :param OcrWordsTask: 用户自定义文本识别结果集，当 Type 为
 OcrWordsRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrWordsTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResult`
        :param HeadTailTask: 视频片头片尾识别结果，当 Type 为
 HeadTailRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadTailTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskHeadTailResult`
        :param ObjectTask: 物体识别结果，当 Type 为
 ObjectRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskObjectResult`
        """
        self.Type = None
        self.FaceRecognitionTask = None
        self.AsrFullTextTask = None
        self.OcrFullTextTask = None
        self.AsrWordsTask = None
        self.OcrWordsTask = None
        self.HeadTailTask = None
        self.ObjectTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("FaceRecognitionTask") is not None:
            self.FaceRecognitionTask = AiRecognitionTaskFaceResult()
            self.FaceRecognitionTask._deserialize(params.get("FaceRecognitionTask"))
        if params.get("AsrFullTextTask") is not None:
            self.AsrFullTextTask = AiRecognitionTaskAsrFullTextResult()
            self.AsrFullTextTask._deserialize(params.get("AsrFullTextTask"))
        if params.get("OcrFullTextTask") is not None:
            self.OcrFullTextTask = AiRecognitionTaskOcrFullTextResult()
            self.OcrFullTextTask._deserialize(params.get("OcrFullTextTask"))
        if params.get("AsrWordsTask") is not None:
            self.AsrWordsTask = AiRecognitionTaskAsrWordsResult()
            self.AsrWordsTask._deserialize(params.get("AsrWordsTask"))
        if params.get("OcrWordsTask") is not None:
            self.OcrWordsTask = AiRecognitionTaskOcrWordsResult()
            self.OcrWordsTask._deserialize(params.get("OcrWordsTask"))
        if params.get("HeadTailTask") is not None:
            self.HeadTailTask = AiRecognitionTaskHeadTailResult()
            self.HeadTailTask._deserialize(params.get("HeadTailTask"))
        if params.get("ObjectTask") is not None:
            self.ObjectTask = AiRecognitionTaskObjectResult()
            self.ObjectTask._deserialize(params.get("ObjectTask"))


class AiRecognitionTaskAsrFullTextResult(AbstractModel):
    """语音全文识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 语音全文识别任务输入信息。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrFullTextResultInput`
        :param Output: 语音全文识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrFullTextResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskAsrFullTextResultInput(AbstractModel):
    """语音全文识别的输入。

    """

    def __init__(self):
        """
        :param Definition: 语音全文识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskAsrFullTextResultOutput(AbstractModel):
    """语音全文识别输出。

    """

    def __init__(self):
        """
        :param SegmentSet: 语音全文识别结果集。
        :type SegmentSet: list of AiRecognitionTaskAsrFullTextSegmentItem
        :param SubtitleUrl: 字幕文件 Url。
        :type SubtitleUrl: str
        """
        self.SegmentSet = None
        self.SubtitleUrl = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        self.SubtitleUrl = params.get("SubtitleUrl")


class AiRecognitionTaskAsrFullTextSegmentItem(AbstractModel):
    """语音全文识别片段。

    """

    def __init__(self):
        """
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Text: 识别文本。
        :type Text: str
        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Text = params.get("Text")


class AiRecognitionTaskAsrWordsResult(AbstractModel):
    """用户自定义语音识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 用户自定义语音识别任务输入信息。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResultInput`
        :param Output: 用户自定义语音识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskAsrWordsResultInput(AbstractModel):
    """用户自定义语音识别输入。

    """

    def __init__(self):
        """
        :param Definition: 用户自定义语音识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskAsrWordsResultItem(AbstractModel):
    """用户自定义语音识别结果。

    """

    def __init__(self):
        """
        :param Word: 语音识别词。
        :type Word: str
        :param SegmentSet: 用户自定义语音识别结果集。
        :type SegmentSet: list of AiRecognitionTaskAsrWordsSegmentItem
        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskAsrWordsResultOutput(AbstractModel):
    """用户自定义语音识别输出。

    """

    def __init__(self):
        """
        :param ResultSet: 用户自定义语音识别结果集。
        :type ResultSet: list of AiRecognitionTaskAsrWordsResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskAsrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)


class AiRecognitionTaskAsrWordsSegmentItem(AbstractModel):
    """语音识别片段。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")


class AiRecognitionTaskFaceResult(AbstractModel):
    """人脸识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 人脸识别任务输入信息。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskFaceResultInput`
        :param Output: 人脸识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskFaceResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskFaceResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskFaceResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskFaceResultInput(AbstractModel):
    """人脸识别输入。

    """

    def __init__(self):
        """
        :param Definition: 人脸识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskFaceResultItem(AbstractModel):
    """人脸识别结果

    """

    def __init__(self):
        """
        :param Id: 人物唯一标识 ID。
        :type Id: str
        :param Type: 人物库类型，表示识别出的人物来自哪个人物库：
<li>Default：默认人物库；</li>
<li>UserDefine：用户自定义人物库。</li>
        :type Type: str
        :param Name: 人物名称。
        :type Name: str
        :param SegmentSet: 人物出现的片段结果集。
        :type SegmentSet: list of AiRecognitionTaskFaceSegmentItem
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskFaceSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskFaceResultOutput(AbstractModel):
    """智能人脸识别输出。

    """

    def __init__(self):
        """
        :param ResultSet: 智能人脸识别结果集。
        :type ResultSet: list of AiRecognitionTaskFaceResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskFaceResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)


class AiRecognitionTaskFaceSegmentItem(AbstractModel):
    """人脸识别结果片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")


class AiRecognitionTaskHeadTailResult(AbstractModel):
    """视频片头片尾识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 视频片头片尾识别任务输入信息。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskHeadTailResultInput`
        :param Output: 视频片头片尾识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskHeadTailResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskHeadTailResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskHeadTailResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskHeadTailResultInput(AbstractModel):
    """视频片头片尾识别的输入。

    """

    def __init__(self):
        """
        :param Definition: 视频片头片尾识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskHeadTailResultOutput(AbstractModel):
    """视频片头片尾识别输出。

    """

    def __init__(self):
        """
        :param HeadConfidence: 片头识别置信度。取值：0~100。
        :type HeadConfidence: float
        :param HeadTimeOffset: 视频片头的结束时间点，单位：秒。
        :type HeadTimeOffset: float
        :param TailConfidence: 片尾识别置信度。取值：0~100。
        :type TailConfidence: float
        :param TailTimeOffset: 视频片尾的开始时间点，单位：秒。
        :type TailTimeOffset: float
        """
        self.HeadConfidence = None
        self.HeadTimeOffset = None
        self.TailConfidence = None
        self.TailTimeOffset = None


    def _deserialize(self, params):
        self.HeadConfidence = params.get("HeadConfidence")
        self.HeadTimeOffset = params.get("HeadTimeOffset")
        self.TailConfidence = params.get("TailConfidence")
        self.TailTimeOffset = params.get("TailTimeOffset")


class AiRecognitionTaskInput(AbstractModel):
    """视频内容识别输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能识别模板 ID ，固定为 10，同时进行按帧标签识别、精彩片段识别、视频头尾识别、拆条、人脸识别、文字识别、语音识别、文字全文识别、语音全文识别，后续会推出用户自定义模板，可根据需要选择相应的识别任务。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskObjectResult(AbstractModel):
    """物体识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 物体识别任务输入信息。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskObjectResultInput`
        :param Output: 物体识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskObjectResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskObjectResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskObjectResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskObjectResultInput(AbstractModel):
    """物体识别任务输入类型。

    """

    def __init__(self):
        """
        :param Definition: 物体识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskObjectResultItem(AbstractModel):
    """单个物体识别结果。

    """

    def __init__(self):
        """
        :param Name: 识别的物体名称。
        :type Name: str
        :param SegmentSet: 物体出现的片段列表。
        :type SegmentSet: list of AiRecognitionTaskObjectSeqmentItem
        """
        self.Name = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskObjectSeqmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskObjectResultOutput(AbstractModel):
    """智能物体识别输出。

    """

    def __init__(self):
        """
        :param ResultSet: 智能物体识别结果集。
        :type ResultSet: list of AiRecognitionTaskObjectResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskObjectResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)


class AiRecognitionTaskObjectSeqmentItem(AbstractModel):
    """物体识别结果片段。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")


class AiRecognitionTaskOcrFullTextResult(AbstractModel):
    """文本全文识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 文本全文识别任务输入信息。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrFullTextResultInput`
        :param Output: 文本全文识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrFullTextResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskOcrFullTextResultInput(AbstractModel):
    """文本全文识别输入。

    """

    def __init__(self):
        """
        :param Definition: 文本全文识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskOcrFullTextResultOutput(AbstractModel):
    """文本全文识别输出。

    """

    def __init__(self):
        """
        :param SegmentSet: 文本全文识别结果集。
        :type SegmentSet: list of AiRecognitionTaskOcrFullTextSegmentItem
        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskOcrFullTextSegmentItem(AbstractModel):
    """文本全文识别片段。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param TextSet: 识别片段结果集。
        :type TextSet: list of AiRecognitionTaskOcrFullTextSegmentTextItem
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TextSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TextSet") is not None:
            self.TextSet = []
            for item in params.get("TextSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentTextItem()
                obj._deserialize(item)
                self.TextSet.append(obj)


class AiRecognitionTaskOcrFullTextSegmentTextItem(AbstractModel):
    """文本全文识别片段。

    """

    def __init__(self):
        """
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。
        :type AreaCoordSet: list of int
        :param Text: 识别文本。
        :type Text: str
        """
        self.Confidence = None
        self.AreaCoordSet = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Text = params.get("Text")


class AiRecognitionTaskOcrWordsResult(AbstractModel):
    """用户自定义文本识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 用户自定义文本识别任务输入信息。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResultInput`
        :param Output: 用户自定义文本识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskOcrWordsResultInput(AbstractModel):
    """用户自定义文本识别输入。

    """

    def __init__(self):
        """
        :param Definition: 用户自定义文本识别模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskOcrWordsResultItem(AbstractModel):
    """用户自定义文本识别结果。

    """

    def __init__(self):
        """
        :param Word: 文本识别词。
        :type Word: str
        :param SegmentSet: 文本文字识别结果集。
        :type SegmentSet: list of AiRecognitionTaskOcrWordsSegmentItem
        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskOcrWordsResultOutput(AbstractModel):
    """用户自定义文本识别输出。

    """

    def __init__(self):
        """
        :param ResultSet: 用户自定义文本识别结果集。
        :type ResultSet: list of AiRecognitionTaskOcrWordsResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskOcrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)


class AiRecognitionTaskOcrWordsSegmentItem(AbstractModel):
    """文本识别片段。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        :param Confidence: 识别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")


class AiReviewPoliticalAsrTaskInput(AbstractModel):
    """内容审核 Asr 文字鉴政、敏感任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴政模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPoliticalAsrTaskOutput(AbstractModel):
    """Asr 文字涉政信息

    """

    def __init__(self):
        """
        :param Confidence: Asr 文字涉政、敏感评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: Asr 文字涉政、敏感结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉政、敏感嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewPoliticalOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字鉴政任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴政模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPoliticalOcrTaskOutput(AbstractModel):
    """Ocr 文字涉政信息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉政、敏感评分，分值为0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉政、敏感结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉政、敏感嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewPoliticalTaskInput(AbstractModel):
    """内容审核鉴政任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴政模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPoliticalTaskOutput(AbstractModel):
    """涉政信息

    """

    def __init__(self):
        """
        :param Confidence: 视频涉政评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 涉政结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 视频鉴政结果标签，取值范围：
<li>politician：政治人物。</li>
<li>violation_photo：违规图标。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param SegmentSet: 有涉政嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of MediaContentReviewPoliticalSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewPoliticalSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewPornAsrTaskInput(AbstractModel):
    """内容审核 Asr 文字鉴黄任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴黄模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPornAsrTaskOutput(AbstractModel):
    """Asr 文字涉黄信息

    """

    def __init__(self):
        """
        :param Confidence: Asr 文字涉黄评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: Asr 文字涉黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉黄嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewPornOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字鉴黄任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴黄模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPornOcrTaskOutput(AbstractModel):
    """Ocr 文字涉黄信息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉黄评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉黄嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewPornTaskInput(AbstractModel):
    """内容审核鉴黄任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴黄模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPornTaskOutput(AbstractModel):
    """鉴黄结果信息

    """

    def __init__(self):
        """
        :param Confidence: 视频鉴黄评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 鉴黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 视频鉴黄结果标签，取值范围：
<li>porn：色情。</li>
<li>sexy：性感。</li>
<li>vulgar：低俗。</li>
<li>intimacy：亲密行为。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param SegmentSet: 有涉黄嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of MediaContentReviewSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewTaskPoliticalAsrResult(AbstractModel):
    """内容审核 Asr 文字鉴政、敏感任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容审核 Asr 文字鉴政任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalAsrTaskInput`
        :param Output: 内容审核 Asr 文字鉴政任务输出。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalAsrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskPoliticalOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴政、敏感任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容审核 Ocr 文字鉴政任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalOcrTaskInput`
        :param Output: 内容审核 Ocr 文字鉴政任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalOcrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskPoliticalResult(AbstractModel):
    """内容审核鉴政任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容审核鉴政任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalTaskInput`
        :param Output: 内容审核鉴政任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPoliticalTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskPornAsrResult(AbstractModel):
    """内容审核 Asr 文字鉴黄任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容审核 Asr 文字鉴黄任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPornAsrTaskInput`
        :param Output: 内容审核 Asr 文字鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPornAsrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskPornOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴黄任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容审核 Ocr 文字鉴黄任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPornOcrTaskInput`
        :param Output: 内容审核 Ocr 文字鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPornOcrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskPornResult(AbstractModel):
    """内容审核鉴黄任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容审核鉴黄任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewPornTaskInput`
        :param Output: 内容审核鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewPornTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskTerrorismResult(AbstractModel):
    """内容审核鉴恐任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容审核鉴恐任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AiReviewTerrorismTaskInput`
        :param Output: 内容审核鉴恐任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AiReviewTerrorismTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTerrorismTaskInput(AbstractModel):
    """内容审核鉴恐任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴恐模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewTerrorismTaskOutput(AbstractModel):
    """暴恐信息

    """

    def __init__(self):
        """
        :param Confidence: 视频暴恐评分，分值为0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 暴恐结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 视频暴恐结果标签，取值范围：
<li>guns：武器枪支。</li>
<li>crowd：人群聚集。</li>
<li>police：警察部队。</li>
<li>bloody：血腥画面。</li>
<li>banners：暴恐旗帜。</li>
<li>militant：武装分子。</li>
<li>explosion：爆炸火灾。</li>
<li>terrorists：暴恐人物。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param SegmentSet: 有暴恐嫌疑的视频片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentSet: list of MediaContentReviewSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AnimatedGraphicTaskInput(AbstractModel):
    """转动图任务类型

    """

    def __init__(self):
        """
        :param Definition: 视频转动图模板 ID
        :type Definition: int
        :param StartTimeOffset: 动图在视频中的开始时间，单位为秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 动图在视频中的结束时间，单位为秒。
        :type EndTimeOffset: float
        """
        self.Definition = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class ApplyUploadRequest(AbstractModel):
    """ApplyUpload请求参数结构体

    """

    def __init__(self):
        """
        :param MediaType: 媒体类型，可选值请参考[上传能力综述](https://cloud.tencent.com/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。
        :type MediaType: str
        :param MediaName: 媒体名称。
        :type MediaName: str
        :param CoverType: 封面类型，可选值请参考[上传能力综述](https://cloud.tencent.com/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。
        :type CoverType: str
        :param Procedure: 媒体后续任务操作，详见[上传指定任务流](https://cloud.tencent.com/document/product/266/9759)。
        :type Procedure: str
        :param ExpireTime: 媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type ExpireTime: str
        :param StorageRegion: 指定上传园区，仅适用于对上传地域有特殊需求的用户。
        :type StorageRegion: str
        :param ClassId: 分类ID，用于对媒体进行分类管理，可通过[创建分类](https://cloud.tencent.com/document/product/266/7812)接口，创建分类，获得分类 ID。
<li>默认值：0，表示其他分类。</li>
        :type ClassId: int
        :param SourceContext: 来源上下文，用于透传用户请求信息，上传回调接口将返回该字段值，最长 250 个字符。
        :type SourceContext: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.MediaType = None
        self.MediaName = None
        self.CoverType = None
        self.Procedure = None
        self.ExpireTime = None
        self.StorageRegion = None
        self.ClassId = None
        self.SourceContext = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.MediaType = params.get("MediaType")
        self.MediaName = params.get("MediaName")
        self.CoverType = params.get("CoverType")
        self.Procedure = params.get("Procedure")
        self.ExpireTime = params.get("ExpireTime")
        self.StorageRegion = params.get("StorageRegion")
        self.ClassId = params.get("ClassId")
        self.SourceContext = params.get("SourceContext")
        self.SubAppId = params.get("SubAppId")


class ApplyUploadResponse(AbstractModel):
    """ApplyUpload返回参数结构体

    """

    def __init__(self):
        """
        :param StorageBucket: 存储桶，用于上传接口 URL 的 bucket_name。
        :type StorageBucket: str
        :param StorageRegion: 存储园区，用于上传接口 Host 的 Region。
        :type StorageRegion: str
        :param VodSessionKey: 点播会话，用于确认上传接口的参数 VodSessionKey。
        :type VodSessionKey: str
        :param MediaStoragePath: 媒体存储路径，用于上传接口存储媒体的对象键（Key）。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaStoragePath: str
        :param CoverStoragePath: 封面存储路径，用于上传接口存储封面的对象键（Key）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverStoragePath: str
        :param TempCertificate: 临时凭证，用于上传接口的权限验证。
        :type TempCertificate: :class:`tencentcloud.vod.v20180717.models.TempCertificate`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StorageBucket = None
        self.StorageRegion = None
        self.VodSessionKey = None
        self.MediaStoragePath = None
        self.CoverStoragePath = None
        self.TempCertificate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StorageBucket = params.get("StorageBucket")
        self.StorageRegion = params.get("StorageRegion")
        self.VodSessionKey = params.get("VodSessionKey")
        self.MediaStoragePath = params.get("MediaStoragePath")
        self.CoverStoragePath = params.get("CoverStoragePath")
        if params.get("TempCertificate") is not None:
            self.TempCertificate = TempCertificate()
            self.TempCertificate._deserialize(params.get("TempCertificate"))
        self.RequestId = params.get("RequestId")


class AudioTemplateInfo(AbstractModel):
    """音频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 音频流的编码格式，可选值：
<li>libfdk_aac：更适合 mp4 和 hls；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
        :type Codec: str
        :param Bitrate: 音频流的码率，取值范围：0 和 [26, 256]，单位：kbps。
当取值为 0，表示音频码率和原始音频保持一致。
        :type Bitrate: int
        :param SampleRate: 音频流的采样率，可选值：
<li>32000</li>
<li>44100</li>
<li>48000</li>
单位：Hz。
        :type SampleRate: int
        :param AudioChannel: 音频通道方式，可选值：
<li>1：单通道</li>
<li>2：双通道</li>
<li>6：立体声</li>
默认值：2。
        :type AudioChannel: int
        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")


class AudioTemplateInfoForUpdate(AbstractModel):
    """音频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 音频流的编码格式，可选值：
<li>libfdk_aac：更适合 mp4 和 hls；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
        :type Codec: str
        :param Bitrate: 音频流的码率，取值范围：0 和 [26, 256]，单位：kbps。 当取值为 0，表示音频码率和原始音频保持一致。
        :type Bitrate: int
        :param SampleRate: 音频流的采样率，可选值：
<li>32000</li>
<li>44100</li>
<li>48000</li>
单位：Hz。
        :type SampleRate: int
        :param AudioChannel: 音频通道方式，可选值：
<li>1：单通道</li>
<li>2：双通道</li>
<li>6：立体声</li>
        :type AudioChannel: int
        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")


class ClassificationConfigureInfo(AbstractModel):
    """智能分类任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能分类任务开关，可选值：
<li>ON：开启智能分类任务；</li>
<li>OFF：关闭智能分类任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ClassificationConfigureInfoForUpdate(AbstractModel):
    """智能分类任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能分类任务开关，可选值：
<li>ON：开启智能分类任务；</li>
<li>OFF：关闭智能分类任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ClipFileInfo2017(AbstractModel):
    """视频裁剪结果文件信息（2017 版）

    """

    def __init__(self):
        """
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 输出目标文件的文件 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileUrl: 输出目标文件的文件地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUrl: str
        :param FileType: 输出目标文件的文件类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        """
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileUrl = None
        self.FileType = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")
        self.FileType = params.get("FileType")


class ClipTask2017(AbstractModel):
    """视频剪辑任务信息，该结构仅用于对 2017 版[视频剪辑](https://cloud.tencent.com/document/product/266/10156)接口发起的任务。

    """

    def __init__(self):
        """
        :param TaskId: 视频剪辑任务 ID。
        :type TaskId: str
        :param SrcFileId: 视频剪辑任务源文件 ID。
        :type SrcFileId: str
        :param FileInfo: 视频剪辑输出的文件信息。
        :type FileInfo: :class:`tencentcloud.vod.v20180717.models.ClipFileInfo2017`
        """
        self.TaskId = None
        self.SrcFileId = None
        self.FileInfo = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.SrcFileId = params.get("SrcFileId")
        if params.get("FileInfo") is not None:
            self.FileInfo = ClipFileInfo2017()
            self.FileInfo._deserialize(params.get("FileInfo"))


class CommitUploadRequest(AbstractModel):
    """CommitUpload请求参数结构体

    """

    def __init__(self):
        """
        :param VodSessionKey: 点播会话，取申请上传接口的返回值 VodSessionKey。
        :type VodSessionKey: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.VodSessionKey = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.VodSessionKey = params.get("VodSessionKey")
        self.SubAppId = params.get("SubAppId")


class CommitUploadResponse(AbstractModel):
    """CommitUpload返回参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件的唯一标识。
        :type FileId: str
        :param MediaUrl: 媒体播放地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaUrl: str
        :param CoverUrl: 媒体封面地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileId = None
        self.MediaUrl = None
        self.CoverUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.MediaUrl = params.get("MediaUrl")
        self.CoverUrl = params.get("CoverUrl")
        self.RequestId = params.get("RequestId")


class ConcatFileInfo2017(AbstractModel):
    """视频拼接源文件信息（2017 版）

    """

    def __init__(self):
        """
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 视频拼接源文件的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileUrl: 视频拼接源文件的地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUrl: str
        :param FileType: 视频拼接源文件的格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        """
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileUrl = None
        self.FileType = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")
        self.FileType = params.get("FileType")


class ConcatTask2017(AbstractModel):
    """视频拼接任务信息，该结构仅用于对 2017 版[视频拼接](https://cloud.tencent.com/document/product/266/7821)接口发起的任务。

    """

    def __init__(self):
        """
        :param TaskId: 视频拼接任务 ID。
        :type TaskId: str
        :param FileInfoSet: 视频拼接源文件信息。
        :type FileInfoSet: list of ConcatFileInfo2017
        """
        self.TaskId = None
        self.FileInfoSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = ConcatFileInfo2017()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)


class ConfirmEventsRequest(AbstractModel):
    """ConfirmEvents请求参数结构体

    """

    def __init__(self):
        """
        :param EventHandles: 事件句柄，数组长度限制：16。
        :type EventHandles: list of str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.EventHandles = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.EventHandles = params.get("EventHandles")
        self.SubAppId = params.get("SubAppId")


class ConfirmEventsResponse(AbstractModel):
    """ConfirmEvents返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CoverBySnapshotTaskInput(AbstractModel):
    """对视频截图做封面任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板 ID。
        :type Definition: int
        :param PositionType: 截图方式。包含：
<li>Time：依照时间点截图</li>
<li>Percent：依照百分比截图</li>
        :type PositionType: str
        :param PositionValue: 截图位置：
<li>对于依照时间点截图，该值表示指定视频第几秒的截图作为封面</li>
<li>对于依照百分比截图，该值表示使用视频百分之多少的截图作为封面</li>
        :type PositionValue: float
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        """
        self.Definition = None
        self.PositionType = None
        self.PositionValue = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.PositionType = params.get("PositionType")
        self.PositionValue = params.get("PositionValue")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)


class CoverBySnapshotTaskOutput(AbstractModel):
    """对视频截图做封面任务输出类型

    """

    def __init__(self):
        """
        :param CoverUrl: 封面 URL。
        :type CoverUrl: str
        """
        self.CoverUrl = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")


class CoverConfigureInfo(AbstractModel):
    """智能封面任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能封面任务开关，可选值：
<li>ON：开启智能封面任务；</li>
<li>OFF：关闭智能封面任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class CoverConfigureInfoForUpdate(AbstractModel):
    """智能封面任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能封面任务开关，可选值：
<li>ON：开启智能封面任务；</li>
<li>OFF：关闭智能封面任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class CreateAIAnalysisTemplateRequest(AbstractModel):
    """CreateAIAnalysisTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 视频内容分析模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 视频内容分析模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param ClassificationConfigure: 智能分类任务控制参数。
        :type ClassificationConfigure: :class:`tencentcloud.vod.v20180717.models.ClassificationConfigureInfo`
        :param TagConfigure: 智能标签任务控制参数。
        :type TagConfigure: :class:`tencentcloud.vod.v20180717.models.TagConfigureInfo`
        :param CoverConfigure: 智能封面任务控制参数。
        :type CoverConfigure: :class:`tencentcloud.vod.v20180717.models.CoverConfigureInfo`
        :param FrameTagConfigure: 智能按帧标签任务控制参数。
        :type FrameTagConfigure: :class:`tencentcloud.vod.v20180717.models.FrameTagConfigureInfo`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        self.SubAppId = params.get("SubAppId")


class CreateAIAnalysisTemplateResponse(AbstractModel):
    """CreateAIAnalysisTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容分析模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateClassRequest(AbstractModel):
    """CreateClass请求参数结构体

    """

    def __init__(self):
        """
        :param ParentId: 父类 ID，一级分类填写 -1。
        :type ParentId: int
        :param ClassName: 分类名称，长度限制：1-64 个字符。
        :type ClassName: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.ParentId = None
        self.ClassName = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ParentId = params.get("ParentId")
        self.ClassName = params.get("ClassName")
        self.SubAppId = params.get("SubAppId")


class CreateClassResponse(AbstractModel):
    """CreateClass返回参数结构体

    """

    def __init__(self):
        """
        :param ClassId: 分类 ID
        :type ClassId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClassId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.RequestId = params.get("RequestId")


class CreateImageSpriteTask2017(AbstractModel):
    """视频截取雪碧图任务，该结构仅用于对 2017 版[截取雪碧图](https://cloud.tencent.com/document/product/266/8101)接口发起的任务。

    """

    def __init__(self):
        """
        :param TaskId: 截图雪碧图任务 ID。
        :type TaskId: str
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 截取雪碧图文件 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param Definition: 雪碧图规格，参见[雪碧图截图模板](https://cloud.tencent.com/document/product/266/11702#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Definition: int
        :param TotalCount: 雪碧图小图总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ImageSpriteUrlSet: 截取雪碧图输出的地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSpriteUrlSet: list of str
        :param WebVttUrl: 雪碧图子图位置与时间关系 WebVtt 文件地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type WebVttUrl: str
        """
        self.TaskId = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.Definition = None
        self.TotalCount = None
        self.ImageSpriteUrlSet = None
        self.WebVttUrl = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.Definition = params.get("Definition")
        self.TotalCount = params.get("TotalCount")
        self.ImageSpriteUrlSet = params.get("ImageSpriteUrlSet")
        self.WebVttUrl = params.get("WebVttUrl")


class CreateProcedureTemplateRequest(AbstractModel):
    """CreateProcedureTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 任务流名字（支持中文，不超过20个字）。
        :type Name: str
        :param MediaProcessTask: 视频处理类型任务参数。
        :type MediaProcessTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskInput`
        :param AiContentReviewTask: AI 智能内容审核类型任务参数。
        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: AI 智能内容分析类型任务参数。
        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: AI 内容识别类型任务参数。
        :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Name = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.SubAppId = params.get("SubAppId")


class CreateProcedureTemplateResponse(AbstractModel):
    """CreateProcedureTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTranscodeTemplateRequest(AbstractModel):
    """CreateTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。
        :type Container: str
        :param Name: 转码模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
默认值：0。
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
默认值：0。
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数，当 RemoveVideo 为 0，该字段必填。
        :type VideoTemplate: :class:`tencentcloud.vod.v20180717.models.VideoTemplateInfo`
        :param AudioTemplate: 音频流配置参数，当 RemoveAudio 为 0，该字段必填。
        :type AudioTemplate: :class:`tencentcloud.vod.v20180717.models.AudioTemplateInfo`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        self.SubAppId = params.get("SubAppId")


class CreateTranscodeTemplateResponse(AbstractModel):
    """CreateTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateWatermarkTemplateRequest(AbstractModel):
    """CreateWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 水印类型，可选值：
<li>image：图片水印；</li>
<li>text：文字水印。</li>
        :type Type: str
        :param Name: 水印模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param CoordinateOrigin: 原点位置，可选值：
<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>
默认值：TopLeft。目前，当 Type 为 image，该字段仅支持 TopLeft。
        :type CoordinateOrigin: str
        :param XPos: 水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
默认值：0px。
        :type XPos: str
        :param YPos: 水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
默认值：0px。
        :type YPos: str
        :param ImageTemplate: 图片水印模板，当 Type 为 image，该字段必填。当 Type 为 text，该字段无效。
        :type ImageTemplate: :class:`tencentcloud.vod.v20180717.models.ImageWatermarkInput`
        :param TextTemplate: 文字水印模板，当 Type 为 text，该字段必填。当 Type 为 image，该字段无效。
        :type TextTemplate: :class:`tencentcloud.vod.v20180717.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG水印模板，当 Type 为 svg，该字段必填。当 Type 为 image 或 text，该字段无效。
        :type SvgTemplate: :class:`tencentcloud.vod.v20180717.models.SvgWatermarkInput`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Type = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.SubAppId = params.get("SubAppId")


class CreateWatermarkTemplateResponse(AbstractModel):
    """CreateWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        :param ImageUrl: 水印图片地址，仅当 Type 为 image，该字段有效。
        :type ImageUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class DeleteAIAnalysisTemplateRequest(AbstractModel):
    """DeleteAIAnalysisTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容分析模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteAIAnalysisTemplateResponse(AbstractModel):
    """DeleteAIAnalysisTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClassRequest(AbstractModel):
    """DeleteClass请求参数结构体

    """

    def __init__(self):
        """
        :param ClassId: 分类 ID
        :type ClassId: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.ClassId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.SubAppId = params.get("SubAppId")


class DeleteClassResponse(AbstractModel):
    """DeleteClass返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMediaRequest(AbstractModel):
    """DeleteMedia请求参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件的唯一标识。
        :type FileId: str
        :param DeleteParts: 指定本次需要删除的部分。默认值为 "[]", 表示删除媒体及其对应的全部视频处理文件。
        :type DeleteParts: list of MediaDeleteItem
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileId = None
        self.DeleteParts = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("DeleteParts") is not None:
            self.DeleteParts = []
            for item in params.get("DeleteParts"):
                obj = MediaDeleteItem()
                obj._deserialize(item)
                self.DeleteParts.append(obj)
        self.SubAppId = params.get("SubAppId")


class DeleteMediaResponse(AbstractModel):
    """DeleteMedia返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProcedureTemplateRequest(AbstractModel):
    """DeleteProcedureTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 任务流名字。
        :type Name: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Name = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SubAppId = params.get("SubAppId")


class DeleteProcedureTemplateResponse(AbstractModel):
    """DeleteProcedureTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTranscodeTemplateRequest(AbstractModel):
    """DeleteTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteTranscodeTemplateResponse(AbstractModel):
    """DeleteTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWatermarkTemplateRequest(AbstractModel):
    """DeleteWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


class DeleteWatermarkTemplateResponse(AbstractModel):
    """DeleteWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAIAnalysisTemplatesRequest(AbstractModel):
    """DescribeAIAnalysisTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 视频内容分析模板唯一标识过滤条件，数组长度限制：10。
        :type Definitions: list of int
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class DescribeAIAnalysisTemplatesResponse(AbstractModel):
    """DescribeAIAnalysisTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param AIAnalysisTemplateSet: 视频内容分析模板详情列表。
        :type AIAnalysisTemplateSet: list of AIAnalysisTemplateItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AIAnalysisTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIAnalysisTemplateSet") is not None:
            self.AIAnalysisTemplateSet = []
            for item in params.get("AIAnalysisTemplateSet"):
                obj = AIAnalysisTemplateItem()
                obj._deserialize(item)
                self.AIAnalysisTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAllClassRequest(AbstractModel):
    """DescribeAllClass请求参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.SubAppId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")


class DescribeAllClassResponse(AbstractModel):
    """DescribeAllClass返回参数结构体

    """

    def __init__(self):
        """
        :param ClassInfoSet: 分类信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassInfoSet: list of MediaClassInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClassInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClassInfoSet") is not None:
            self.ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = MediaClassInfo()
                obj._deserialize(item)
                self.ClassInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaInfosRequest(AbstractModel):
    """DescribeMediaInfos请求参数结构体

    """

    def __init__(self):
        """
        :param FileIds: 媒体文件 ID 列表，N 从 0 开始取值，最大 19。
        :type FileIds: list of str
        :param Filters: 指定所有媒体文件需要返回的信息，可同时指定多个信息，N 从 0 开始递增。如果未填写该字段，默认返回所有信息。选项有：
<li>basicInfo（视频基础信息）。</li>
<li>metaData（视频元信息）。</li>
<li>transcodeInfo（视频转码结果信息）。</li>
<li>animatedGraphicsInfo（视频转动图结果信息）。</li>
<li>imageSpriteInfo（视频雪碧图信息）。</li>
<li>snapshotByTimeOffsetInfo（视频指定时间点截图信息）。</li>
<li>sampleSnapshotInfo（采样截图信息）。</li>
<li>keyFrameDescInfo（打点信息）。</li>
        :type Filters: list of str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileIds = None
        self.Filters = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.Filters = params.get("Filters")
        self.SubAppId = params.get("SubAppId")


class DescribeMediaInfosResponse(AbstractModel):
    """DescribeMediaInfos返回参数结构体

    """

    def __init__(self):
        """
        :param MediaInfoSet: 媒体文件信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfoSet: list of MediaInfo
        :param NotExistFileIdSet: 不存在的文件 ID 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type NotExistFileIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MediaInfoSet = None
        self.NotExistFileIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MediaInfoSet") is not None:
            self.MediaInfoSet = []
            for item in params.get("MediaInfoSet"):
                obj = MediaInfo()
                obj._deserialize(item)
                self.MediaInfoSet.append(obj)
        self.NotExistFileIdSet = params.get("NotExistFileIdSet")
        self.RequestId = params.get("RequestId")


class DescribeProcedureTemplatesRequest(AbstractModel):
    """DescribeProcedureTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Names: 任务流模板名字过滤条件，数组长度限制：100。
        :type Names: list of str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Names = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class DescribeProcedureTemplatesResponse(AbstractModel):
    """DescribeProcedureTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param ProcedureTemplateSet: 任务流模板详情列表。
        :type ProcedureTemplateSet: list of ProcedureTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProcedureTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProcedureTemplateSet") is not None:
            self.ProcedureTemplateSet = []
            for item in params.get("ProcedureTemplateSet"):
                obj = ProcedureTemplate()
                obj._deserialize(item)
                self.ProcedureTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 视频处理任务的任务 ID。
        :type TaskId: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.TaskId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.SubAppId = params.get("SubAppId")


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TaskType: 任务类型，取值：
<li>Procedure：视频处理任务；</li>
<li>EditMedia：视频编辑任务；</li>
<li>WechatPublish：微信发布任务。</li>
兼容 2017 版的任务类型：
<li>Transcode：视频转码任务；</li>
<li>SnapshotByTimeOffset：视频截图任务；</li>
<li>Concat：视频拼接任务；</li>
<li>Clip：视频剪辑任务；</li>
<li>ImageSprites：截取雪碧图任务。</li>
        :type TaskType: str
        :param Status: 任务状态，取值：
<li>WAITING：等待中；</li>
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param CreateTime: 任务的创建时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param BeginProcessTime: 任务开始执行的时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type BeginProcessTime: str
        :param FinishTime: 任务执行完毕的时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type FinishTime: str
        :param ProcedureTask: 视频处理任务信息，仅当 TaskType 为 Procedure，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcedureTask: :class:`tencentcloud.vod.v20180717.models.ProcedureTask`
        :param EditMediaTask: 视频编辑任务信息，仅当 TaskType 为 EditMedia，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type EditMediaTask: :class:`tencentcloud.vod.v20180717.models.EditMediaTask`
        :param WechatPublishTask: 微信发布任务信息，仅当 TaskType 为 WechatPublish，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatPublishTask: :class:`tencentcloud.vod.v20180717.models.WechatPublishTask`
        :param TranscodeTask: 视频转码任务信息，仅当 TaskType 为 Transcode，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeTask: :class:`tencentcloud.vod.v20180717.models.TranscodeTask2017`
        :param SnapshotByTimeOffsetTask: 视频指定时间点截图任务信息，仅当 TaskType 为 SnapshotByTimeOffset，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTask: :class:`tencentcloud.vod.v20180717.models.SnapshotByTimeOffsetTask2017`
        :param ConcatTask: 视频拼接任务信息，仅当 TaskType 为 Concat，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConcatTask: :class:`tencentcloud.vod.v20180717.models.ConcatTask2017`
        :param ClipTask: 视频剪辑任务信息，仅当 TaskType 为 Clip，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClipTask: :class:`tencentcloud.vod.v20180717.models.ClipTask2017`
        :param CreateImageSpriteTask: 截取雪碧图任务信息，仅当 TaskType 为 ImageSprite，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateImageSpriteTask: :class:`tencentcloud.vod.v20180717.models.CreateImageSpriteTask2017`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskType = None
        self.Status = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.ProcedureTask = None
        self.EditMediaTask = None
        self.WechatPublishTask = None
        self.TranscodeTask = None
        self.SnapshotByTimeOffsetTask = None
        self.ConcatTask = None
        self.ClipTask = None
        self.CreateImageSpriteTask = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("ProcedureTask") is not None:
            self.ProcedureTask = ProcedureTask()
            self.ProcedureTask._deserialize(params.get("ProcedureTask"))
        if params.get("EditMediaTask") is not None:
            self.EditMediaTask = EditMediaTask()
            self.EditMediaTask._deserialize(params.get("EditMediaTask"))
        if params.get("WechatPublishTask") is not None:
            self.WechatPublishTask = WechatPublishTask()
            self.WechatPublishTask._deserialize(params.get("WechatPublishTask"))
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = TranscodeTask2017()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = SnapshotByTimeOffsetTask2017()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        if params.get("ConcatTask") is not None:
            self.ConcatTask = ConcatTask2017()
            self.ConcatTask._deserialize(params.get("ConcatTask"))
        if params.get("ClipTask") is not None:
            self.ClipTask = ClipTask2017()
            self.ClipTask._deserialize(params.get("ClipTask"))
        if params.get("CreateImageSpriteTask") is not None:
            self.CreateImageSpriteTask = CreateImageSpriteTask2017()
            self.CreateImageSpriteTask._deserialize(params.get("CreateImageSpriteTask"))
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 过滤条件：任务状态，可选值：WAITING（等待中）、PROCESSING（处理中）、FINISH（已完成）。
        :type Status: str
        :param FileId: 过滤条件：文件 ID。
        :type FileId: str
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param ScrollToken: 翻页标识，分批拉取时使用：当单次请求无法拉取所有数据，接口将会返回 ScrollToken，下一次请求携带该 Token，将会从下一条记录开始获取。
        :type ScrollToken: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Status = None
        self.FileId = None
        self.Limit = None
        self.ScrollToken = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.FileId = params.get("FileId")
        self.Limit = params.get("Limit")
        self.ScrollToken = params.get("ScrollToken")
        self.SubAppId = params.get("SubAppId")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskSet: 任务概要列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSet: list of TaskSimpleInfo
        :param ScrollToken: 翻页标识，当请求未返回所有数据，该字段表示下一条记录的 ID。当该字段为空，说明已无更多数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type ScrollToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskSet = None
        self.ScrollToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskSimpleInfo()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.ScrollToken = params.get("ScrollToken")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeTemplatesRequest(AbstractModel):
    """DescribeTranscodeTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 转码模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param ContainerType: 封装格式过滤条件，可选值：
<li>Video：视频格式，可以同时包含视频流和音频流的封装格式板；</li>
<li>PureAudio：纯音频格式，只能包含音频流的封装格式。</li>
        :type ContainerType: str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Type = None
        self.ContainerType = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.ContainerType = params.get("ContainerType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class DescribeTranscodeTemplatesResponse(AbstractModel):
    """DescribeTranscodeTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param TranscodeTemplateSet: 转码模板详情列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeTemplateSet: list of TranscodeTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TranscodeTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TranscodeTemplateSet") is not None:
            self.TranscodeTemplateSet = []
            for item in params.get("TranscodeTemplateSet"):
                obj = TranscodeTemplate()
                obj._deserialize(item)
                self.TranscodeTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWatermarkTemplatesRequest(AbstractModel):
    """DescribeWatermarkTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 水印模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int
        :param Type: 水印类型过滤条件，可选值：
<li>image：图片水印；</li>
<li>text：文字水印。</li>
        :type Type: str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数
<li>默认值：10；</li>
<li>最大值：100。</li>
        :type Limit: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Type = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class DescribeWatermarkTemplatesResponse(AbstractModel):
    """DescribeWatermarkTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param WatermarkTemplateSet: 水印模板详情列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkTemplateSet: list of WatermarkTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WatermarkTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WatermarkTemplateSet") is not None:
            self.WatermarkTemplateSet = []
            for item in params.get("WatermarkTemplateSet"):
                obj = WatermarkTemplate()
                obj._deserialize(item)
                self.WatermarkTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class EditMediaFileInfo(AbstractModel):
    """编辑点播视频文件信息

    """

    def __init__(self):
        """
        :param FileId: 视频的 ID。
        :type FileId: str
        :param StartTimeOffset: 视频剪辑的起始偏移时间偏移，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 视频剪辑的起始结束时间偏移，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        """
        self.FileId = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class EditMediaStreamInfo(AbstractModel):
    """编辑视频流信息

    """

    def __init__(self):
        """
        :param StreamId: 录制的流 ID
        :type StreamId: str
        :param StartTime: 流剪辑的起始时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 流剪辑的结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.StreamId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class EditMediaTask(AbstractModel):
    """编辑视频任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 视频编辑任务的输入。
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: :class:`tencentcloud.vod.v20180717.models.EditMediaTaskInput`
        :param Output: 视频编辑任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.EditMediaTaskOutput`
        :param ProcedureTaskId: 若发起视频编辑任务时指定了视频处理流程，则该字段为流程任务 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcedureTaskId: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None
        self.ProcedureTaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = EditMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = EditMediaTaskOutput()
            self.Output._deserialize(params.get("Output"))
        self.ProcedureTaskId = params.get("ProcedureTaskId")


class EditMediaTaskInput(AbstractModel):
    """编辑视频任务的输入。

    """

    def __init__(self):
        """
        :param InputType: 输入视频的来源类型，可以取的值为 File，Stream 两种。
        :type InputType: str
        :param FileInfoSet: 输入的视频文件信息，当 InputType 为 File 时，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileInfoSet: list of EditMediaFileInfo
        :param StreamInfoSet: 输入的流信息，当 InputType 为 Stream 时，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamInfoSet: list of EditMediaStreamInfo
        """
        self.InputType = None
        self.FileInfoSet = None
        self.StreamInfoSet = None


    def _deserialize(self, params):
        self.InputType = params.get("InputType")
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)
        if params.get("StreamInfoSet") is not None:
            self.StreamInfoSet = []
            for item in params.get("StreamInfoSet"):
                obj = EditMediaStreamInfo()
                obj._deserialize(item)
                self.StreamInfoSet.append(obj)


class EditMediaTaskOutput(AbstractModel):
    """编辑视频任务的输出

    """

    def __init__(self):
        """
        :param FileType: 文件类型，例如 mp4、flv 等。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param FileId: 媒体文件 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileUrl: 媒体文件播放地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUrl: str
        """
        self.FileType = None
        self.FileId = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.FileType = params.get("FileType")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")


class EventContent(AbstractModel):
    """事件通知内容，其中，TranscodeCompleteEvent、ConcatCompleteEvent、ClipCompleteEvent、CreateImageSpriteCompleteEvent、SnapshotByTimeOffsetCompleteEvent 为兼容 2017 版接口发起任务的事件通知。

    """

    def __init__(self):
        """
        :param EventHandle: 事件句柄，调用方必须调用 ConfirmEvents 来确认消息已经收到，确认有效时间 30 秒。失效后，事件可重新被获取。
        :type EventHandle: str
        :param EventType: <b>支持事件类型：</b>
<li>NewFileUpload：视频上传完成；</li>
<li>ProcedureStateChanged：任务流状态变更；</li>
<li>FileDeleted：视频删除完成；</li>
<li>PullComplete：视频转拉完成；</li>
<li>EditMediaComplete：视频编辑完成；</li>
<li>WechatPublishComplete：微信发布完成。</li>
<b>兼容 2017 版的事件类型：</b>
<li>TranscodeComplete：视频转码完成；</li>
<li>ConcatComplete：视频拼接完成；</li>
<li>ClipComplete：视频剪辑完成；</li>
<li>CreateImageSpriteComplete：视频截取雪碧图完成；</li>
<li>CreateSnapshotByTimeOffsetComplete：视频按时间点截图完成。</li>
        :type EventType: str
        :param FileUploadEvent: 视频上传完成事件，当事件类型为 NewFileUpload 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUploadEvent: :class:`tencentcloud.vod.v20180717.models.FileUploadTask`
        :param ProcedureStateChangeEvent: 任务流状态变更事件，当事件类型为 ProcedureStateChanged 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcedureStateChangeEvent: :class:`tencentcloud.vod.v20180717.models.ProcedureTask`
        :param FileDeleteEvent: 文件删除事件，当事件类型为 FileDeleted 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileDeleteEvent: :class:`tencentcloud.vod.v20180717.models.FileDeleteTask`
        :param PullCompleteEvent: 视频转拉完成事件，当事件类型为 PullComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PullCompleteEvent: :class:`tencentcloud.vod.v20180717.models.PullFileTask`
        :param EditMediaCompleteEvent: 视频编辑完成事件，当事件类型为 EditMediaComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type EditMediaCompleteEvent: :class:`tencentcloud.vod.v20180717.models.EditMediaTask`
        :param WechatPublishCompleteEvent: 微信发布完成事件，当事件类型为 WechatPublishComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatPublishCompleteEvent: :class:`tencentcloud.vod.v20180717.models.WechatPublishTask`
        :param TranscodeCompleteEvent: 视频转码完成事件，当事件类型为 TranscodeComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeCompleteEvent: :class:`tencentcloud.vod.v20180717.models.TranscodeTask2017`
        :param ConcatCompleteEvent: 视频拼接完成事件，当事件类型为 ConcatComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConcatCompleteEvent: :class:`tencentcloud.vod.v20180717.models.ConcatTask2017`
        :param ClipCompleteEvent: 视频剪辑完成事件，当事件类型为 ClipComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClipCompleteEvent: :class:`tencentcloud.vod.v20180717.models.ClipTask2017`
        :param CreateImageSpriteCompleteEvent: 视频截取雪碧图完成事件，当事件类型为 CreateImageSpriteComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateImageSpriteCompleteEvent: :class:`tencentcloud.vod.v20180717.models.CreateImageSpriteTask2017`
        :param SnapshotByTimeOffsetCompleteEvent: 视频按时间点截图完成事件，当事件类型为 CreateSnapshotByTimeOffsetComplete 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetCompleteEvent: :class:`tencentcloud.vod.v20180717.models.SnapshotByTimeOffsetTask2017`
        """
        self.EventHandle = None
        self.EventType = None
        self.FileUploadEvent = None
        self.ProcedureStateChangeEvent = None
        self.FileDeleteEvent = None
        self.PullCompleteEvent = None
        self.EditMediaCompleteEvent = None
        self.WechatPublishCompleteEvent = None
        self.TranscodeCompleteEvent = None
        self.ConcatCompleteEvent = None
        self.ClipCompleteEvent = None
        self.CreateImageSpriteCompleteEvent = None
        self.SnapshotByTimeOffsetCompleteEvent = None


    def _deserialize(self, params):
        self.EventHandle = params.get("EventHandle")
        self.EventType = params.get("EventType")
        if params.get("FileUploadEvent") is not None:
            self.FileUploadEvent = FileUploadTask()
            self.FileUploadEvent._deserialize(params.get("FileUploadEvent"))
        if params.get("ProcedureStateChangeEvent") is not None:
            self.ProcedureStateChangeEvent = ProcedureTask()
            self.ProcedureStateChangeEvent._deserialize(params.get("ProcedureStateChangeEvent"))
        if params.get("FileDeleteEvent") is not None:
            self.FileDeleteEvent = FileDeleteTask()
            self.FileDeleteEvent._deserialize(params.get("FileDeleteEvent"))
        if params.get("PullCompleteEvent") is not None:
            self.PullCompleteEvent = PullFileTask()
            self.PullCompleteEvent._deserialize(params.get("PullCompleteEvent"))
        if params.get("EditMediaCompleteEvent") is not None:
            self.EditMediaCompleteEvent = EditMediaTask()
            self.EditMediaCompleteEvent._deserialize(params.get("EditMediaCompleteEvent"))
        if params.get("WechatPublishCompleteEvent") is not None:
            self.WechatPublishCompleteEvent = WechatPublishTask()
            self.WechatPublishCompleteEvent._deserialize(params.get("WechatPublishCompleteEvent"))
        if params.get("TranscodeCompleteEvent") is not None:
            self.TranscodeCompleteEvent = TranscodeTask2017()
            self.TranscodeCompleteEvent._deserialize(params.get("TranscodeCompleteEvent"))
        if params.get("ConcatCompleteEvent") is not None:
            self.ConcatCompleteEvent = ConcatTask2017()
            self.ConcatCompleteEvent._deserialize(params.get("ConcatCompleteEvent"))
        if params.get("ClipCompleteEvent") is not None:
            self.ClipCompleteEvent = ClipTask2017()
            self.ClipCompleteEvent._deserialize(params.get("ClipCompleteEvent"))
        if params.get("CreateImageSpriteCompleteEvent") is not None:
            self.CreateImageSpriteCompleteEvent = CreateImageSpriteTask2017()
            self.CreateImageSpriteCompleteEvent._deserialize(params.get("CreateImageSpriteCompleteEvent"))
        if params.get("SnapshotByTimeOffsetCompleteEvent") is not None:
            self.SnapshotByTimeOffsetCompleteEvent = SnapshotByTimeOffsetTask2017()
            self.SnapshotByTimeOffsetCompleteEvent._deserialize(params.get("SnapshotByTimeOffsetCompleteEvent"))


class FileDeleteTask(AbstractModel):
    """文件删除任务

    """

    def __init__(self):
        """
        :param FileIdSet: 删除文件 ID 列表。
        :type FileIdSet: list of str
        """
        self.FileIdSet = None


    def _deserialize(self, params):
        self.FileIdSet = params.get("FileIdSet")


class FileUploadTask(AbstractModel):
    """文件上传任务信息

    """

    def __init__(self):
        """
        :param FileId: 文件唯一 ID。
        :type FileId: str
        :param MediaBasicInfo: 上传完成后生成的媒体文件基础信息。
        :type MediaBasicInfo: :class:`tencentcloud.vod.v20180717.models.MediaBasicInfo`
        :param ProcedureTaskId: 若视频上传时指定了视频处理流程，则该字段为流程任务 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcedureTaskId: str
        """
        self.FileId = None
        self.MediaBasicInfo = None
        self.ProcedureTaskId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("MediaBasicInfo") is not None:
            self.MediaBasicInfo = MediaBasicInfo()
            self.MediaBasicInfo._deserialize(params.get("MediaBasicInfo"))
        self.ProcedureTaskId = params.get("ProcedureTaskId")


class FrameTagConfigureInfo(AbstractModel):
    """智能按帧标签任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能按帧标签任务开关，可选值：
<li>ON：开启智能按帧标签任务；</li>
<li>OFF：关闭智能按帧标签任务。</li>
        :type Switch: str
        :param ScreenshotInterval: 截帧间隔，单位为秒，当不填时，默认截帧间隔为 1 秒，最小值为 0.5 秒。
        :type ScreenshotInterval: float
        """
        self.Switch = None
        self.ScreenshotInterval = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ScreenshotInterval = params.get("ScreenshotInterval")


class FrameTagConfigureInfoForUpdate(AbstractModel):
    """智能按帧标签任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能按帧标签任务开关，可选值：
<li>ON：开启智能按帧标签任务；</li>
<li>OFF：关闭智能按帧标签任务。</li>
        :type Switch: str
        :param ScreenshotInterval: 截帧间隔，单位为秒，最小值为 0.5 秒。
        :type ScreenshotInterval: float
        """
        self.Switch = None
        self.ScreenshotInterval = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ScreenshotInterval = params.get("ScreenshotInterval")


class ImageSpriteTaskInput(AbstractModel):
    """对视频截雪碧图任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class ImageWatermarkInput(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        """
        :param ImageContent: 水印图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。支持 jpeg、png 图片格式。
        :type ImageContent: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
默认值：10%。
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
默认值：0px，表示 Height 按照 Width 对视频宽度的比例缩放。
        :type Height: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class ImageWatermarkInputForUpdate(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        """
        :param ImageContent: 水印图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。支持 jpeg、png 图片格式。
        :type ImageContent: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
0px 表示 Height 按照 Width 对视频宽度的比例缩放。
        :type Height: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class ImageWatermarkTemplate(AbstractModel):
    """图片水印模板

    """

    def __init__(self):
        """
        :param ImageUrl: 水印图片地址。
        :type ImageUrl: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素；</li>
0px：表示 Height 按照 Width 对视频宽度的比例缩放。
        :type Height: str
        """
        self.ImageUrl = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class LiveRealTimeClipRequest(AbstractModel):
    """LiveRealTimeClip请求参数结构体

    """

    def __init__(self):
        """
        :param StreamId: 推流[直播码](https://cloud.tencent.com/document/product/267/5959)。
        :type StreamId: str
        :param StartTime: 流剪辑的开始时间，格式参照 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type StartTime: str
        :param EndTime: 流剪辑的结束时间，格式参照 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type EndTime: str
        :param IsPersistence: 是否固化。0 不固化，1 固化。默认不固化。
        :type IsPersistence: int
        :param ExpireTime: 剪辑固化后的视频存储过期时间。格式参照 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。填“9999-12-31T23:59:59Z”表示永不过期。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。仅 IsPersistence 为 1 时有效，默认剪辑固化的视频永不过期。
        :type ExpireTime: str
        :param Procedure: 剪辑固化后的视频点播任务流处理，详见[上传指定任务流](https://cloud.tencent.com/document/product/266/9759)。仅 IsPersistence 为 1 时有效。
        :type Procedure: str
        :param MetaDataRequired: 是否需要返回剪辑后的视频元信息。0 不需要，1 需要。默认不需要。
        :type MetaDataRequired: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.StreamId = None
        self.StartTime = None
        self.EndTime = None
        self.IsPersistence = None
        self.ExpireTime = None
        self.Procedure = None
        self.MetaDataRequired = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsPersistence = params.get("IsPersistence")
        self.ExpireTime = params.get("ExpireTime")
        self.Procedure = params.get("Procedure")
        self.MetaDataRequired = params.get("MetaDataRequired")
        self.SubAppId = params.get("SubAppId")


class LiveRealTimeClipResponse(AbstractModel):
    """LiveRealTimeClip返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 剪辑后的视频播放 URL。
        :type Url: str
        :param FileId: 剪辑固化后的视频的媒体文件的唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param VodTaskId: 剪辑固化后的视频任务流 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VodTaskId: str
        :param MetaData: 剪辑后的视频元信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.FileId = None
        self.VodTaskId = None
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileId = params.get("FileId")
        self.VodTaskId = params.get("VodTaskId")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class MediaAiAnalysisClassificationItem(AbstractModel):
    """智能分类结果

    """

    def __init__(self):
        """
        :param Classification: 智能分类的类别名称。
        :type Classification: str
        :param Confidence: 智能分类的可信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Classification = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Classification = params.get("Classification")
        self.Confidence = params.get("Confidence")


class MediaAiAnalysisCoverItem(AbstractModel):
    """智能封面信息

    """

    def __init__(self):
        """
        :param CoverUrl: 智能封面地址。
        :type CoverUrl: str
        :param Confidence: 智能封面的可信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.CoverUrl = None
        self.Confidence = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
        self.Confidence = params.get("Confidence")


class MediaAiAnalysisFrameTagItem(AbstractModel):
    """智能按帧标签结果信息

    """

    def __init__(self):
        """
        :param Tag: 按帧标签名称。
        :type Tag: str
        :param Confidence: 按帧标签的可信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")


class MediaAiAnalysisFrameTagSegmentItem(AbstractModel):
    """按帧标签片段列表

    """

    def __init__(self):
        """
        :param StartTimeOffset: 按帧标签起始的偏移时间。
        :type StartTimeOffset: float
        :param EndTimeOffset: 按帧标签结束的偏移时间。
        :type EndTimeOffset: float
        :param TagSet: 时间片段内的标签列表。
        :type TagSet: list of MediaAiAnalysisFrameTagItem
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TagSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisFrameTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)


class MediaAiAnalysisTagItem(AbstractModel):
    """智能标签结果信息

    """

    def __init__(self):
        """
        :param Tag: 标签名称。
        :type Tag: str
        :param Confidence: 标签的可信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")


class MediaAnimatedGraphicsInfo(AbstractModel):
    """点播文件视频转动图结果信息

    """

    def __init__(self):
        """
        :param AnimatedGraphicsSet: 视频转动图结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AnimatedGraphicsSet: list of MediaAnimatedGraphicsItem
        """
        self.AnimatedGraphicsSet = None


    def _deserialize(self, params):
        if params.get("AnimatedGraphicsSet") is not None:
            self.AnimatedGraphicsSet = []
            for item in params.get("AnimatedGraphicsSet"):
                obj = MediaAnimatedGraphicsItem()
                obj._deserialize(item)
                self.AnimatedGraphicsSet.append(obj)


class MediaAnimatedGraphicsItem(AbstractModel):
    """视频转动图结果信息

    """

    def __init__(self):
        """
        :param Url: 转动图的文件地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Definition: 转动图模板 ID，参见[转动图参数模板](https://cloud.tencent.com/document/product/266/11701#.E9.A2.84.E7.BD.AE.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Definition: int
        :param Container: 动图格式，如 gif。
注意：此字段可能返回 null，表示取不到有效值。
        :type Container: str
        :param Height: 动图的高度，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 动图的宽度，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Bitrate: 动图码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Size: 动图大小，单位：字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Md5: 动图的md5值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param StartTimeOffset: 动图在视频中的起始时间偏移，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 动图在视频中的结束时间偏移，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        """
        self.Url = None
        self.Definition = None
        self.Container = None
        self.Height = None
        self.Width = None
        self.Bitrate = None
        self.Size = None
        self.Md5 = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Bitrate = params.get("Bitrate")
        self.Size = params.get("Size")
        self.Md5 = params.get("Md5")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class MediaAudioStreamItem(AbstractModel):
    """点播文件音频流信息

    """

    def __init__(self):
        """
        :param Bitrate: 音频流的码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param SamplingRate: 音频流的采样率，单位：hz。
注意：此字段可能返回 null，表示取不到有效值。
        :type SamplingRate: int
        :param Codec: 音频流的编码格式，例如 aac。
注意：此字段可能返回 null，表示取不到有效值。
        :type Codec: str
        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")


class MediaBasicInfo(AbstractModel):
    """点播媒体文件基础信息

    """

    def __init__(self):
        """
        :param Name: 媒体文件名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Description: 媒体文件描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateTime: 媒体文件的创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 媒体文件的最近更新时间（如修改视频属性、发起视频处理等会触发更新媒体文件信息的操作），使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ExpireTime: 媒体文件的过期时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。“9999-12-31T23:59:59Z”表示永不过期。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param ClassId: 媒体文件的分类 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassId: int
        :param ClassName: 媒体文件的分类名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassName: str
        :param ClassPath: 媒体文件的分类路径，分类间以“-”分隔，如“新的一级分类 - 新的二级分类”。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassPath: str
        :param CoverUrl: 媒体文件的封面图片地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverUrl: str
        :param Type: 媒体文件的封装格式，例如 mp4、flv 等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param MediaUrl: 原始媒体文件的 URL 地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaUrl: str
        :param SourceInfo: 该媒体文件的来源信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceInfo: :class:`tencentcloud.vod.v20180717.models.MediaSourceData`
        :param StorageRegion: 媒体文件存储地区，如 ap-guangzhou，参见[地域列表](https://cloud.tencent.com/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageRegion: str
        :param TagSet: 媒体文件的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of str
        :param Vid: 直播录制文件的唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Vid: str
        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExpireTime = None
        self.ClassId = None
        self.ClassName = None
        self.ClassPath = None
        self.CoverUrl = None
        self.Type = None
        self.MediaUrl = None
        self.SourceInfo = None
        self.StorageRegion = None
        self.TagSet = None
        self.Vid = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ClassId = params.get("ClassId")
        self.ClassName = params.get("ClassName")
        self.ClassPath = params.get("ClassPath")
        self.CoverUrl = params.get("CoverUrl")
        self.Type = params.get("Type")
        self.MediaUrl = params.get("MediaUrl")
        if params.get("SourceInfo") is not None:
            self.SourceInfo = MediaSourceData()
            self.SourceInfo._deserialize(params.get("SourceInfo"))
        self.StorageRegion = params.get("StorageRegion")
        self.TagSet = params.get("TagSet")
        self.Vid = params.get("Vid")


class MediaClassInfo(AbstractModel):
    """分类信息描述

    """

    def __init__(self):
        """
        :param ClassId: 分类 ID
        :type ClassId: int
        :param ParentId: 父类 ID，一级分类的父类 ID 为 -1。
        :type ParentId: int
        :param ClassName: 分类名称
        :type ClassName: str
        :param Level: 分类级别，一级分类为 0，最大值为 3，即最多允许 4 级分类层次。
        :type Level: int
        :param SubClassIdSet: 当前分类的第一级子类 ID 集合
注意：此字段可能返回 null，表示取不到有效值。
        :type SubClassIdSet: list of int
        """
        self.ClassId = None
        self.ParentId = None
        self.ClassName = None
        self.Level = None
        self.SubClassIdSet = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.ParentId = params.get("ParentId")
        self.ClassName = params.get("ClassName")
        self.Level = params.get("Level")
        self.SubClassIdSet = params.get("SubClassIdSet")


class MediaContentReviewAsrTextSegmentItem(AbstractModel):
    """内容审核 Asr 文字审核嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段置信度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 嫌疑片段审核结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param KeywordSet: 嫌疑关键词列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeywordSet: list of str
        """
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


class MediaContentReviewOcrTextSegmentItem(AbstractModel):
    """内容审核 Ocr 文字审核嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段置信度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 嫌疑片段审核结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param KeywordSet: 嫌疑关键词列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeywordSet: list of str
        :param AreaCoordSet: 嫌疑文字出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
注意：此字段可能返回 null，表示取不到有效值。
        :type AreaCoordSet: list of int
        """
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


class MediaContentReviewPoliticalSegmentItem(AbstractModel):
    """内容审核涉政嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段涉政分数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 嫌疑片段鉴政结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Name: 涉政人物、违规图标名字。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Label: 嫌疑片段鉴政结果标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
 PicUrlExpireTime 时间点后图片将被删除）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param AreaCoordSet: 涉政人物、违规图标出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
注意：此字段可能返回 null，表示取不到有效值。
        :type AreaCoordSet: list of int
        :param PicUrlExpireTimeStamp: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此字段可能返回 null，表示取不到有效值。
        :type PicUrlExpireTimeStamp: int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.Name = None
        self.Label = None
        self.Url = None
        self.AreaCoordSet = None
        self.PicUrlExpireTimeStamp = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Name = params.get("Name")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")


class MediaContentReviewSegmentItem(AbstractModel):
    """内容审核涉黄/暴恐嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段涉黄分数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Label: 嫌疑片段鉴黄结果标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
 PicUrlExpireTime 时间点后图片将被删除）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param PicUrlExpireTimeStamp: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此字段可能返回 null，表示取不到有效值。
        :type PicUrlExpireTimeStamp: int
        """
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


class MediaDeleteItem(AbstractModel):
    """指定删除点播视频时的删除内容

    """

    def __init__(self):
        """
        :param Type: 所指定的删除部分。如果未填写该字段则参数无效。可选值有：
<li>TranscodeFiles（删除转码文件）。</li>
<li>WechatPublishFiles（删除微信发布文件）。</li>
        :type Type: str
        :param Definition: 删除由Type参数指定的种类下的视频模板号，模板定义参见[转码模板](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
默认值为0，表示删除参数Type指定种类下所有的视频。
        :type Definition: int
        """
        self.Type = None
        self.Definition = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Definition = params.get("Definition")


class MediaImageSpriteInfo(AbstractModel):
    """点播文件雪碧图信息

    """

    def __init__(self):
        """
        :param ImageSpriteSet: 特定规格的雪碧图信息集合，每个元素代表一套相同规格的雪碧图。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSpriteSet: list of MediaImageSpriteItem
        """
        self.ImageSpriteSet = None


    def _deserialize(self, params):
        if params.get("ImageSpriteSet") is not None:
            self.ImageSpriteSet = []
            for item in params.get("ImageSpriteSet"):
                obj = MediaImageSpriteItem()
                obj._deserialize(item)
                self.ImageSpriteSet.append(obj)


class MediaImageSpriteItem(AbstractModel):
    """雪碧图信息

    """

    def __init__(self):
        """
        :param Definition: 雪碧图规格，参见[雪碧图参数模板](https://cloud.tencent.com/document/product/266/11702#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Definition: int
        :param Height: 雪碧图小图的高度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 雪碧图小图的宽度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param TotalCount: 每一张雪碧图大图里小图的数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ImageUrlSet: 每一张雪碧图大图的地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrlSet: list of str
        :param WebVttUrl: 雪碧图子图位置与时间关系的 WebVtt 文件地址。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在在雪碧大图里的坐标位置，一般被播放器用于实现预览。
注意：此字段可能返回 null，表示取不到有效值。
        :type WebVttUrl: str
        """
        self.Definition = None
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImageUrlSet = None
        self.WebVttUrl = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImageUrlSet = params.get("ImageUrlSet")
        self.WebVttUrl = params.get("WebVttUrl")


class MediaInfo(AbstractModel):
    """点播文件信息

    """

    def __init__(self):
        """
        :param BasicInfo: 基础信息。包括视频名称、大小、时长、封面图片等。
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicInfo: :class:`tencentcloud.vod.v20180717.models.MediaBasicInfo`
        :param MetaData: 元信息。包括视频流信息、音频流信息等。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param TranscodeInfo: 转码结果信息。包括该视频转码生成的各种码率的视频的地址、规格、码率、分辨率等。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeInfo: :class:`tencentcloud.vod.v20180717.models.MediaTranscodeInfo`
        :param AnimatedGraphicsInfo: 转动图结果信息。对视频转动图（如 gif）后，动图相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AnimatedGraphicsInfo: :class:`tencentcloud.vod.v20180717.models.MediaAnimatedGraphicsInfo`
        :param SampleSnapshotInfo: 采样截图信息。对视频采样截图后，相关截图信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleSnapshotInfo: :class:`tencentcloud.vod.v20180717.models.MediaSampleSnapshotInfo`
        :param ImageSpriteInfo: 雪碧图信息。对视频截取雪碧图之后，雪碧的相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSpriteInfo: :class:`tencentcloud.vod.v20180717.models.MediaImageSpriteInfo`
        :param SnapshotByTimeOffsetInfo: 指定时间点截图信息。对视频依照指定时间点截图后，各个截图的信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetInfo: :class:`tencentcloud.vod.v20180717.models.MediaSnapshotByTimeOffsetInfo`
        :param KeyFrameDescInfo: 视频打点信息。对视频设置的各个打点信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyFrameDescInfo: :class:`tencentcloud.vod.v20180717.models.MediaKeyFrameDescInfo`
        :param FileId: 媒体文件唯一标识 ID。
        :type FileId: str
        """
        self.BasicInfo = None
        self.MetaData = None
        self.TranscodeInfo = None
        self.AnimatedGraphicsInfo = None
        self.SampleSnapshotInfo = None
        self.ImageSpriteInfo = None
        self.SnapshotByTimeOffsetInfo = None
        self.KeyFrameDescInfo = None
        self.FileId = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = MediaBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("TranscodeInfo") is not None:
            self.TranscodeInfo = MediaTranscodeInfo()
            self.TranscodeInfo._deserialize(params.get("TranscodeInfo"))
        if params.get("AnimatedGraphicsInfo") is not None:
            self.AnimatedGraphicsInfo = MediaAnimatedGraphicsInfo()
            self.AnimatedGraphicsInfo._deserialize(params.get("AnimatedGraphicsInfo"))
        if params.get("SampleSnapshotInfo") is not None:
            self.SampleSnapshotInfo = MediaSampleSnapshotInfo()
            self.SampleSnapshotInfo._deserialize(params.get("SampleSnapshotInfo"))
        if params.get("ImageSpriteInfo") is not None:
            self.ImageSpriteInfo = MediaImageSpriteInfo()
            self.ImageSpriteInfo._deserialize(params.get("ImageSpriteInfo"))
        if params.get("SnapshotByTimeOffsetInfo") is not None:
            self.SnapshotByTimeOffsetInfo = MediaSnapshotByTimeOffsetInfo()
            self.SnapshotByTimeOffsetInfo._deserialize(params.get("SnapshotByTimeOffsetInfo"))
        if params.get("KeyFrameDescInfo") is not None:
            self.KeyFrameDescInfo = MediaKeyFrameDescInfo()
            self.KeyFrameDescInfo._deserialize(params.get("KeyFrameDescInfo"))
        self.FileId = params.get("FileId")


class MediaInputInfo(AbstractModel):
    """要处理的源视频信息，视频名称、视频自定义 ID。

    """

    def __init__(self):
        """
        :param Url: 视频 URL。
        :type Url: str
        :param Name: 视频名称。
        :type Name: str
        :param Id: 视频自定义 ID。
        :type Id: str
        """
        self.Url = None
        self.Name = None
        self.Id = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Name = params.get("Name")
        self.Id = params.get("Id")


class MediaKeyFrameDescInfo(AbstractModel):
    """视频打点信息

    """

    def __init__(self):
        """
        :param KeyFrameDescSet: 视频打点信息数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyFrameDescSet: list of MediaKeyFrameDescItem
        """
        self.KeyFrameDescSet = None


    def _deserialize(self, params):
        if params.get("KeyFrameDescSet") is not None:
            self.KeyFrameDescSet = []
            for item in params.get("KeyFrameDescSet"):
                obj = MediaKeyFrameDescItem()
                obj._deserialize(item)
                self.KeyFrameDescSet.append(obj)


class MediaKeyFrameDescItem(AbstractModel):
    """视频打点信息

    """

    def __init__(self):
        """
        :param TimeOffset: 打点的视频偏移时间，单位：秒。
        :type TimeOffset: float
        :param Content: 打点的内容字符串，限制 1-128 个字符。
        :type Content: str
        """
        self.TimeOffset = None
        self.Content = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Content = params.get("Content")


class MediaMetaData(AbstractModel):
    """点播媒体文件元信息

    """

    def __init__(self):
        """
        :param Size: 上传的媒体文件大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Container: 容器类型，例如 m4a，mp4 等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Container: str
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Duration: 视频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: float
        :param Rotate: 视频拍摄时的选择角度，单位：度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: int
        :param VideoStreamSet: 视频流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoStreamSet: list of MediaVideoStreamItem
        :param AudioStreamSet: 音频流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoDuration: 视频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoDuration: float
        :param AudioDuration: 音频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioDuration: float
        """
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
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        self.VideoDuration = params.get("VideoDuration")
        self.AudioDuration = params.get("AudioDuration")


class MediaOutputInfo(AbstractModel):
    """视频处理输出文件信息参数。

    """

    def __init__(self):
        """
        :param Region: 输出文件 Bucket 所属地域，如 ap-guangzhou  。
        :type Region: str
        :param Bucket: 输出文件 Bucket 。
        :type Bucket: str
        :param Dir: 输出文件目录，目录名必须以 "/" 结尾。
        :type Dir: str
        """
        self.Region = None
        self.Bucket = None
        self.Dir = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.Dir = params.get("Dir")


class MediaProcessTaskAdaptiveDynamicStreamingResult(AbstractModel):
    """对视频转自适应码流任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频转自适应码流任务的输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AdaptiveDynamicStreamingTaskInput`
        :param Output: 对视频转自适应码流任务的输出。
        :type Output: :class:`tencentcloud.vod.v20180717.models.AdaptiveDynamicStreamingInfoItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AdaptiveDynamicStreamingTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AdaptiveDynamicStreamingInfoItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskAnimatedGraphicResult(AbstractModel):
    """转动图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 转动图任务的输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.AnimatedGraphicTaskInput`
        :param Output: 转动图任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaAnimatedGraphicsItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AnimatedGraphicTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaAnimatedGraphicsItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskCoverBySnapshotResult(AbstractModel):
    """对视频截图做封面任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 对视频截图做封面任务的输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.CoverBySnapshotTaskInput`
        :param Output: 对视频截图做封面任务的输出。
        :type Output: :class:`tencentcloud.vod.v20180717.models.CoverBySnapshotTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = CoverBySnapshotTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = CoverBySnapshotTaskOutput()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskImageSpriteResult(AbstractModel):
    """对视频截雪碧图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 对视频截雪碧图任务的输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.ImageSpriteTaskInput`
        :param Output: 对视频截雪碧图任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaImageSpriteItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = ImageSpriteTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaImageSpriteItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskInput(AbstractModel):
    """视频处理任务类型

    """

    def __init__(self):
        """
        :param TranscodeTaskSet: 视频转码任务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeTaskSet: list of TranscodeTaskInput
        :param AnimatedGraphicTaskSet: 视频转动图任务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AnimatedGraphicTaskSet: list of AnimatedGraphicTaskInput
        :param SnapshotByTimeOffsetTaskSet: 对视频按时间点截图任务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTaskSet: list of SnapshotByTimeOffsetTaskInput
        :param SampleSnapshotTaskSet: 对视频采样截图任务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleSnapshotTaskSet: list of SampleSnapshotTaskInput
        :param ImageSpriteTaskSet: 对视频截雪碧图任务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSpriteTaskSet: list of ImageSpriteTaskInput
        :param CoverBySnapshotTaskSet: 对视频截图做封面任务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverBySnapshotTaskSet: list of CoverBySnapshotTaskInput
        :param AdaptiveDynamicStreamingTaskSet: 对视频转自适应码流任务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdaptiveDynamicStreamingTaskSet: list of AdaptiveDynamicStreamingTaskInput
        """
        self.TranscodeTaskSet = None
        self.AnimatedGraphicTaskSet = None
        self.SnapshotByTimeOffsetTaskSet = None
        self.SampleSnapshotTaskSet = None
        self.ImageSpriteTaskSet = None
        self.CoverBySnapshotTaskSet = None
        self.AdaptiveDynamicStreamingTaskSet = None


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self.TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskInput()
                obj._deserialize(item)
                self.TranscodeTaskSet.append(obj)
        if params.get("AnimatedGraphicTaskSet") is not None:
            self.AnimatedGraphicTaskSet = []
            for item in params.get("AnimatedGraphicTaskSet"):
                obj = AnimatedGraphicTaskInput()
                obj._deserialize(item)
                self.AnimatedGraphicTaskSet.append(obj)
        if params.get("SnapshotByTimeOffsetTaskSet") is not None:
            self.SnapshotByTimeOffsetTaskSet = []
            for item in params.get("SnapshotByTimeOffsetTaskSet"):
                obj = SnapshotByTimeOffsetTaskInput()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTaskSet.append(obj)
        if params.get("SampleSnapshotTaskSet") is not None:
            self.SampleSnapshotTaskSet = []
            for item in params.get("SampleSnapshotTaskSet"):
                obj = SampleSnapshotTaskInput()
                obj._deserialize(item)
                self.SampleSnapshotTaskSet.append(obj)
        if params.get("ImageSpriteTaskSet") is not None:
            self.ImageSpriteTaskSet = []
            for item in params.get("ImageSpriteTaskSet"):
                obj = ImageSpriteTaskInput()
                obj._deserialize(item)
                self.ImageSpriteTaskSet.append(obj)
        if params.get("CoverBySnapshotTaskSet") is not None:
            self.CoverBySnapshotTaskSet = []
            for item in params.get("CoverBySnapshotTaskSet"):
                obj = CoverBySnapshotTaskInput()
                obj._deserialize(item)
                self.CoverBySnapshotTaskSet.append(obj)
        if params.get("AdaptiveDynamicStreamingTaskSet") is not None:
            self.AdaptiveDynamicStreamingTaskSet = []
            for item in params.get("AdaptiveDynamicStreamingTaskSet"):
                obj = AdaptiveDynamicStreamingTaskInput()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTaskSet.append(obj)


class MediaProcessTaskResult(AbstractModel):
    """任务查询结果类型

    """

    def __init__(self):
        """
        :param Type: 任务的类型，可以取的值有：
<li>Transcode：转码</li>
<li>AnimatedGraphics：转动图</li>
<li>SnapshotByTimeOffset：时间点截图</li>
<li>SampleSnapshot：采样截图</li>
<li>ImageSprites：雪碧图</li>
<li>CoverBySnapshot：截图做封面</li>
<li>AdaptiveDynamicStreaming：自适应码流</li>
        :type Type: str
        :param TranscodeTask: 视频转码任务的查询结果，当任务类型为 Transcode 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskTranscodeResult`
        :param AnimatedGraphicTask: 视频转动图任务的查询结果，当任务类型为 AnimatedGraphics 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AnimatedGraphicTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskAnimatedGraphicResult`
        :param SnapshotByTimeOffsetTask: 对视频按时间点截图任务的查询结果，当任务类型为 SnapshotByTimeOffset 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskSnapshotByTimeOffsetResult`
        :param SampleSnapshotTask: 对视频采样截图任务的查询结果，当任务类型为 SampleSnapshot 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleSnapshotTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskSampleSnapshotResult`
        :param ImageSpriteTask: 对视频截雪碧图任务的查询结果，当任务类型为 ImageSprite 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSpriteTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskImageSpriteResult`
        :param CoverBySnapshotTask: 对视频截图做封面任务的查询结果，当任务类型为 CoverBySnapshot 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverBySnapshotTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskCoverBySnapshotResult`
        :param AdaptiveDynamicStreamingTask: 对视频转自适应码流任务的查询结果，当任务类型为 AdaptiveDynamicStreaming 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdaptiveDynamicStreamingTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskAdaptiveDynamicStreamingResult`
        """
        self.Type = None
        self.TranscodeTask = None
        self.AnimatedGraphicTask = None
        self.SnapshotByTimeOffsetTask = None
        self.SampleSnapshotTask = None
        self.ImageSpriteTask = None
        self.CoverBySnapshotTask = None
        self.AdaptiveDynamicStreamingTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = MediaProcessTaskTranscodeResult()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("AnimatedGraphicTask") is not None:
            self.AnimatedGraphicTask = MediaProcessTaskAnimatedGraphicResult()
            self.AnimatedGraphicTask._deserialize(params.get("AnimatedGraphicTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = MediaProcessTaskSnapshotByTimeOffsetResult()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        if params.get("SampleSnapshotTask") is not None:
            self.SampleSnapshotTask = MediaProcessTaskSampleSnapshotResult()
            self.SampleSnapshotTask._deserialize(params.get("SampleSnapshotTask"))
        if params.get("ImageSpriteTask") is not None:
            self.ImageSpriteTask = MediaProcessTaskImageSpriteResult()
            self.ImageSpriteTask._deserialize(params.get("ImageSpriteTask"))
        if params.get("CoverBySnapshotTask") is not None:
            self.CoverBySnapshotTask = MediaProcessTaskCoverBySnapshotResult()
            self.CoverBySnapshotTask._deserialize(params.get("CoverBySnapshotTask"))
        if params.get("AdaptiveDynamicStreamingTask") is not None:
            self.AdaptiveDynamicStreamingTask = MediaProcessTaskAdaptiveDynamicStreamingResult()
            self.AdaptiveDynamicStreamingTask._deserialize(params.get("AdaptiveDynamicStreamingTask"))


class MediaProcessTaskSampleSnapshotResult(AbstractModel):
    """对视频做采样截图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 对视频做采样截图任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.SampleSnapshotTaskInput`
        :param Output: 对视频做采样截图任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaSampleSnapshotItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SampleSnapshotTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSampleSnapshotItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskSnapshotByTimeOffsetResult(AbstractModel):
    """对视频按指定时间点截图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 对视频按指定时间点截图任务输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.SnapshotByTimeOffsetTaskInput`
        :param Output: 对视频按指定时间点截图任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaSnapshotByTimeOffsetItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SnapshotByTimeOffsetTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSnapshotByTimeOffsetItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskTranscodeResult(AbstractModel):
    """转码任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0：成功，其他值：失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 转码任务的输入。
        :type Input: :class:`tencentcloud.vod.v20180717.models.TranscodeTaskInput`
        :param Output: 转码任务的输出。
        :type Output: :class:`tencentcloud.vod.v20180717.models.MediaTranscodeItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = TranscodeTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaTranscodeItem()
            self.Output._deserialize(params.get("Output"))


class MediaSampleSnapshotInfo(AbstractModel):
    """点播文件采样截图信息

    """

    def __init__(self):
        """
        :param SampleSnapshotSet: 特定规格的采样截图信息集合，每个元素代表一套相同规格的采样截图。
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleSnapshotSet: list of MediaSampleSnapshotItem
        """
        self.SampleSnapshotSet = None


    def _deserialize(self, params):
        if params.get("SampleSnapshotSet") is not None:
            self.SampleSnapshotSet = []
            for item in params.get("SampleSnapshotSet"):
                obj = MediaSampleSnapshotItem()
                obj._deserialize(item)
                self.SampleSnapshotSet.append(obj)


class MediaSampleSnapshotItem(AbstractModel):
    """采样截图信息

    """

    def __init__(self):
        """
        :param Definition: 采样截图规格 ID，参见[采样截图参数模板](https://cloud.tencent.com/document/product/266/11702#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Definition: int
        :param SampleType: 采样方式，取值范围：
<li>Percent：根据百分比间隔采样。</li>
<li>Time：根据时间间隔采样。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleType: str
        :param Interval: 采样间隔
<li>当 SampleType 为 Percent 时，该值表示多少百分比一张图。</li>
<li>当 SampleType 为 Time 时，该值表示多少时间间隔一张图，单位秒， 第一张图均为视频首帧。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Interval: int
        :param ImageUrlSet: 生成的截图 url 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrlSet: list of str
        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type WaterMarkDefinition: list of int
        """
        self.Definition = None
        self.SampleType = None
        self.Interval = None
        self.ImageUrlSet = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SampleType = params.get("SampleType")
        self.Interval = params.get("Interval")
        self.ImageUrlSet = params.get("ImageUrlSet")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")


class MediaSnapshotByTimeOffsetInfo(AbstractModel):
    """点播文件指定时间点截图信息

    """

    def __init__(self):
        """
        :param SnapshotByTimeOffsetSet: 特定规格的指定时间点截图信息集合。目前每种规格只能有一套截图。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetSet: list of MediaSnapshotByTimeOffsetItem
        """
        self.SnapshotByTimeOffsetSet = None


    def _deserialize(self, params):
        if params.get("SnapshotByTimeOffsetSet") is not None:
            self.SnapshotByTimeOffsetSet = []
            for item in params.get("SnapshotByTimeOffsetSet"):
                obj = MediaSnapshotByTimeOffsetItem()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetSet.append(obj)


class MediaSnapshotByTimeOffsetItem(AbstractModel):
    """点播文件指定时间点截图信息

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图规格，参见[指定时间点截图参数模板](https://cloud.tencent.com/document/product/266/11702#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Definition: int
        :param PicInfoSet: 同一规格的截图信息集合，每个元素代表一张截图。
注意：此字段可能返回 null，表示取不到有效值。
        :type PicInfoSet: list of MediaSnapshotByTimePicInfoItem
        """
        self.Definition = None
        self.PicInfoSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("PicInfoSet") is not None:
            self.PicInfoSet = []
            for item in params.get("PicInfoSet"):
                obj = MediaSnapshotByTimePicInfoItem()
                obj._deserialize(item)
                self.PicInfoSet.append(obj)


class MediaSnapshotByTimePicInfoItem(AbstractModel):
    """指定时间点截图信息

    """

    def __init__(self):
        """
        :param TimeOffset: 该张截图对应视频文件中的时间偏移，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeOffset: float
        :param Url: 该张截图的 URL 地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type WaterMarkDefinition: list of int
        """
        self.TimeOffset = None
        self.Url = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Url = params.get("Url")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")


class MediaSourceData(AbstractModel):
    """来源文件信息

    """

    def __init__(self):
        """
        :param SourceType: 媒体文件的来源类别：
<li>Record：来自录制。如直播录制、直播时移录制等。</li>
<li>Upload：来自上传。如拉取上传、服务端上传、客户端 UGC 上传等。</li>
<li>VideoProcessing：来自视频处理。如视频拼接、视频剪辑等。</li>
<li>Unknown：未知来源。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param SourceContext: 用户创建文件时透传的字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceContext: str
        """
        self.SourceType = None
        self.SourceContext = None


    def _deserialize(self, params):
        self.SourceType = params.get("SourceType")
        self.SourceContext = params.get("SourceContext")


class MediaTranscodeInfo(AbstractModel):
    """点播文件转码信息

    """

    def __init__(self):
        """
        :param TranscodeSet: 各规格的转码信息集合，每个元素代表一个规格的转码结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeSet: list of MediaTranscodeItem
        """
        self.TranscodeSet = None


    def _deserialize(self, params):
        if params.get("TranscodeSet") is not None:
            self.TranscodeSet = []
            for item in params.get("TranscodeSet"):
                obj = MediaTranscodeItem()
                obj._deserialize(item)
                self.TranscodeSet.append(obj)


class MediaTranscodeItem(AbstractModel):
    """转码信息

    """

    def __init__(self):
        """
        :param Url: 转码后的视频文件地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Definition: 转码规格 ID，参见[转码参数模板](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Definition: int
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和， 单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Size: 媒体文件总大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Duration: 视频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: float
        :param Container: 容器类型，例如 m4a，mp4 等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Container: str
        :param Md5: 视频的 md5 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param AudioStreamSet: 音频流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoStreamSet: 视频流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoStreamSet: list of MediaVideoStreamItem
        """
        self.Url = None
        self.Definition = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Size = None
        self.Duration = None
        self.Container = None
        self.Md5 = None
        self.AudioStreamSet = None
        self.VideoStreamSet = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Size = params.get("Size")
        self.Duration = params.get("Duration")
        self.Container = params.get("Container")
        self.Md5 = params.get("Md5")
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)


class MediaVideoStreamItem(AbstractModel):
    """点播文件视频流信息

    """

    def __init__(self):
        """
        :param Bitrate: 视频流的码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Height: 视频流的高度，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 视频流的宽度，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Codec: 视频流的编码格式，例如 h264。
注意：此字段可能返回 null，表示取不到有效值。
        :type Codec: str
        :param Fps: 帧率，单位：hz。
注意：此字段可能返回 null，表示取不到有效值。
        :type Fps: int
        """
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


class ModifyAIAnalysisTemplateRequest(AbstractModel):
    """ModifyAIAnalysisTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容分析模板唯一标识。
        :type Definition: int
        :param Name: 视频内容分析模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 视频内容分析模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param ClassificationConfigure: 智能分类任务控制参数。
        :type ClassificationConfigure: :class:`tencentcloud.vod.v20180717.models.ClassificationConfigureInfoForUpdate`
        :param TagConfigure: 智能标签任务控制参数。
        :type TagConfigure: :class:`tencentcloud.vod.v20180717.models.TagConfigureInfoForUpdate`
        :param CoverConfigure: 智能封面任务控制参数。
        :type CoverConfigure: :class:`tencentcloud.vod.v20180717.models.CoverConfigureInfoForUpdate`
        :param FrameTagConfigure: 智能按帧标签任务控制参数。
        :type FrameTagConfigure: :class:`tencentcloud.vod.v20180717.models.FrameTagConfigureInfoForUpdate`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfoForUpdate()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfoForUpdate()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfoForUpdate()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfoForUpdate()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        self.SubAppId = params.get("SubAppId")


class ModifyAIAnalysisTemplateResponse(AbstractModel):
    """ModifyAIAnalysisTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClassRequest(AbstractModel):
    """ModifyClass请求参数结构体

    """

    def __init__(self):
        """
        :param ClassId: 分类 ID
        :type ClassId: int
        :param ClassName: 分类名称。长度限制：1-64 个字符。
        :type ClassName: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.ClassId = None
        self.ClassName = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.ClassName = params.get("ClassName")
        self.SubAppId = params.get("SubAppId")


class ModifyClassResponse(AbstractModel):
    """ModifyClass返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMediaInfoRequest(AbstractModel):
    """ModifyMediaInfo请求参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件唯一标识。
        :type FileId: str
        :param Name: 媒体文件名称，最长 64 个字符。
        :type Name: str
        :param Description: 媒体文件描述，最长 128 个字符。
        :type Description: str
        :param ClassId: 媒体文件分类 ID。
        :type ClassId: int
        :param ExpireTime: 媒体文件过期时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。填“9999-12-31T23:59:59Z”表示永不过期。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。
        :type ExpireTime: str
        :param CoverData: 视频封面图片文件（如 jpeg, png 等）进行 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串，仅支持 gif、jpeg、png 三种图片格式。
        :type CoverData: str
        :param AddKeyFrameDescs: 新增的一组视频打点信息，如果某个偏移时间已存在打点，则会进行覆盖操作，单个媒体文件最多 100 个打点信息。同一个请求里，AddKeyFrameDescs 的时间偏移参数必须与 DeleteKeyFrameDescs 都不同。
        :type AddKeyFrameDescs: list of MediaKeyFrameDescItem
        :param DeleteKeyFrameDescs: 要删除的一组视频打点信息的时间偏移，单位：秒。同一个请求里，AddKeyFrameDescs 的时间偏移参数必须与 DeleteKeyFrameDescs 都不同。
        :type DeleteKeyFrameDescs: list of float
        :param ClearKeyFrameDescs: 取值 1 表示清空视频打点信息，其他值无意义。
同一个请求里，ClearKeyFrameDescs 与 AddKeyFrameDescs 不能同时出现。
        :type ClearKeyFrameDescs: int
        :param AddTags: 新增的一组标签，单个媒体文件最多 16 个标签，单个标签最多 16 个字符。同一个请求里，AddTags 参数必须与 DeleteTags 都不同。
        :type AddTags: list of str
        :param DeleteTags: 要删除的一组标签。同一个请求里，AddTags 参数必须与 DeleteTags 都不同。
        :type DeleteTags: list of str
        :param ClearTags: 取值 1 表示清空媒体文件所有标签，其他值无意义。
同一个请求里，ClearTags 与 AddTags 不能同时出现。
        :type ClearTags: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileId = None
        self.Name = None
        self.Description = None
        self.ClassId = None
        self.ExpireTime = None
        self.CoverData = None
        self.AddKeyFrameDescs = None
        self.DeleteKeyFrameDescs = None
        self.ClearKeyFrameDescs = None
        self.AddTags = None
        self.DeleteTags = None
        self.ClearTags = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")
        self.CoverData = params.get("CoverData")
        if params.get("AddKeyFrameDescs") is not None:
            self.AddKeyFrameDescs = []
            for item in params.get("AddKeyFrameDescs"):
                obj = MediaKeyFrameDescItem()
                obj._deserialize(item)
                self.AddKeyFrameDescs.append(obj)
        self.DeleteKeyFrameDescs = params.get("DeleteKeyFrameDescs")
        self.ClearKeyFrameDescs = params.get("ClearKeyFrameDescs")
        self.AddTags = params.get("AddTags")
        self.DeleteTags = params.get("DeleteTags")
        self.ClearTags = params.get("ClearTags")
        self.SubAppId = params.get("SubAppId")


class ModifyMediaInfoResponse(AbstractModel):
    """ModifyMediaInfo返回参数结构体

    """

    def __init__(self):
        """
        :param CoverUrl: 新的视频封面 URL。
* 注意：仅当请求携带 CoverData 时此返回值有效。 *
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CoverUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
        self.RequestId = params.get("RequestId")


class ModifyTranscodeTemplateRequest(AbstractModel):
    """ModifyTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。
        :type Definition: int
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。
        :type Container: str
        :param Name: 转码模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字节。
        :type Comment: str
        :param RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数。
        :type VideoTemplate: :class:`tencentcloud.vod.v20180717.models.VideoTemplateInfoForUpdate`
        :param AudioTemplate: 音频流配置参数。
        :type AudioTemplate: :class:`tencentcloud.vod.v20180717.models.AudioTemplateInfoForUpdate`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfoForUpdate()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfoForUpdate()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        self.SubAppId = params.get("SubAppId")


class ModifyTranscodeTemplateResponse(AbstractModel):
    """ModifyTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWatermarkTemplateRequest(AbstractModel):
    """ModifyWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        :param Name: 水印模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param CoordinateOrigin: 原点位置，可选值：
<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>
目前，当 Type 为 image，该字段仅支持 TopLeft。
        :type CoordinateOrigin: str
        :param XPos: 水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
        :type XPos: str
        :param YPos: 水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
        :type YPos: str
        :param ImageTemplate: 图片水印模板，该字段仅对图片水印模板有效。
        :type ImageTemplate: :class:`tencentcloud.vod.v20180717.models.ImageWatermarkInputForUpdate`
        :param TextTemplate: 文字水印模板，该字段仅对文字水印模板有效。
        :type TextTemplate: :class:`tencentcloud.vod.v20180717.models.TextWatermarkTemplateInputForUpdate`
        :param SvgTemplate: SVG水印模板，当 Type 为 svg，该字段必填。当 Type 为 image 或 text，该字段无效。
        :type SvgTemplate: :class:`tencentcloud.vod.v20180717.models.SvgWatermarkInputForUpdate`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInputForUpdate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInputForUpdate()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInputForUpdate()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.SubAppId = params.get("SubAppId")


class ModifyWatermarkTemplateResponse(AbstractModel):
    """ModifyWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片水印地址，仅当 ImageTemplate.ImageContent 非空，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class ProcedureTask(AbstractModel):
    """视频处理任务信息

    """

    def __init__(self):
        """
        :param TaskId: 视频处理任务 ID。
        :type TaskId: str
        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 媒体文件 ID
<li>若流程由 [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) 发起，该字段表示 [MediaInfo](https://cloud.tencent.com/document/product/266/31773#MediaInfo) 的 FileId；</li>
<li>若流程由 [ProcessMediaByUrl](https://cloud.tencent.com/document/product/266/33426) 发起，该字段表示 [MediaInputInfo](https://cloud.tencent.com/document/product/266/31773#MediaInputInfo) 的 Id。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileName: 媒体文件名称
<li>若流程由 [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) 发起，该字段表示 [MediaInfo](https://cloud.tencent.com/document/product/266/31773#MediaInfo) 的 BasicInfo.Name；</li>
<li>若流程由 [ProcessMediaByUrl](https://cloud.tencent.com/document/product/266/33426) 发起，该字段表示 [MediaInputInfo](https://cloud.tencent.com/document/product/266/31773#MediaInputInfo) 的 Name。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param FileUrl: 媒体文件地址
<li>若流程由 [ProcessMedia](https://cloud.tencent.com/document/product/266/33427) 发起，该字段表示 [MediaInfo](https://cloud.tencent.com/document/product/266/31773#MediaInfo) 的 BasicInfo.MediaUrl；</li>
<li>若流程由 [ProcessMediaByUrl](https://cloud.tencent.com/document/product/266/33426) 发起，该字段表示 [MediaInputInfo](https://cloud.tencent.com/document/product/266/31773#MediaInputInfo) 的 Url。</li>
        :type FileUrl: str
        :param MetaData: 原始视频的元信息。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param MediaProcessResultSet: 视频处理任务的执行状态与结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaProcessResultSet: list of MediaProcessTaskResult
        :param AiContentReviewResultSet: 视频内容审核任务的执行状态与结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiContentReviewResultSet: list of AiContentReviewResult
        :param AiAnalysisResultSet: 视频内容分析任务的执行状态与结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiAnalysisResultSet: list of AiAnalysisResult
        :param AiRecognitionResultSet: 视频内容识别任务的执行状态与结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiRecognitionResultSet: list of AiRecognitionResult
        :param TasksPriority: 任务流的优先级，取值范围为 [-10, 10]。
注意：此字段可能返回 null，表示取不到有效值。
        :type TasksPriority: int
        :param TasksNotifyMode: 任务流状态变更通知模式。
<li>Finish：只有当任务流全部执行完毕时，才发起一次事件通知；</li>
<li>Change：只要任务流中每个子任务的状态发生变化，都进行事件通知；</li>
<li>None：不接受该任务流回调。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TasksNotifyMode: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 250 个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileName = None
        self.FileUrl = None
        self.MetaData = None
        self.MediaProcessResultSet = None
        self.AiContentReviewResultSet = None
        self.AiAnalysisResultSet = None
        self.AiRecognitionResultSet = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.FileUrl = params.get("FileUrl")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("MediaProcessResultSet") is not None:
            self.MediaProcessResultSet = []
            for item in params.get("MediaProcessResultSet"):
                obj = MediaProcessTaskResult()
                obj._deserialize(item)
                self.MediaProcessResultSet.append(obj)
        if params.get("AiContentReviewResultSet") is not None:
            self.AiContentReviewResultSet = []
            for item in params.get("AiContentReviewResultSet"):
                obj = AiContentReviewResult()
                obj._deserialize(item)
                self.AiContentReviewResultSet.append(obj)
        if params.get("AiAnalysisResultSet") is not None:
            self.AiAnalysisResultSet = []
            for item in params.get("AiAnalysisResultSet"):
                obj = AiAnalysisResult()
                obj._deserialize(item)
                self.AiAnalysisResultSet.append(obj)
        if params.get("AiRecognitionResultSet") is not None:
            self.AiRecognitionResultSet = []
            for item in params.get("AiRecognitionResultSet"):
                obj = AiRecognitionResult()
                obj._deserialize(item)
                self.AiRecognitionResultSet.append(obj)
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")


class ProcedureTemplate(AbstractModel):
    """任务流模板详情

    """

    def __init__(self):
        """
        :param Name: 任务流名字。
        :type Name: str
        :param MediaProcessTask: 视频处理类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaProcessTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskInput`
        :param AiContentReviewTask: AI 智能内容审核类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: AI 智能内容分析类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: AI 内容识别类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Name = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class ProcessMediaByUrlRequest(AbstractModel):
    """ProcessMediaByUrl请求参数结构体

    """

    def __init__(self):
        """
        :param InputInfo: 输入视频信息，包括视频 URL ， 名称、视频自定义 ID。
        :type InputInfo: :class:`tencentcloud.vod.v20180717.models.MediaInputInfo`
        :param OutputInfo: 输出文件 COS 路径信息。
        :type OutputInfo: :class:`tencentcloud.vod.v20180717.models.MediaOutputInfo`
        :param AiContentReviewTask: 视频内容审核类型任务参数。
        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 视频内容分析类型任务参数。
        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param TasksPriority: 任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TasksPriority: int
        :param TasksNotifyMode: 任务流状态变更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。
        :type TasksNotifyMode: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 250 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.InputInfo = None
        self.OutputInfo = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None
        self.SubAppId = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("OutputInfo") is not None:
            self.OutputInfo = MediaOutputInfo()
            self.OutputInfo._deserialize(params.get("OutputInfo"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.SubAppId = params.get("SubAppId")


class ProcessMediaByUrlResponse(AbstractModel):
    """ProcessMediaByUrl返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProcessMediaRequest(AbstractModel):
    """ProcessMedia请求参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件 ID。
        :type FileId: str
        :param MediaProcessTask: 视频处理类型任务参数。
        :type MediaProcessTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 视频内容审核类型任务参数。
        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 视频内容分析类型任务参数。
        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param TasksPriority: 任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TasksPriority: int
        :param TasksNotifyMode: 任务流状态变更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。
        :type TasksNotifyMode: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 250 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileId = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.SubAppId = params.get("SubAppId")


class ProcessMediaResponse(AbstractModel):
    """ProcessMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PullEventsRequest(AbstractModel):
    """PullEvents请求参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.SubAppId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")


class PullEventsResponse(AbstractModel):
    """PullEvents返回参数结构体

    """

    def __init__(self):
        """
        :param EventSet: 事件列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type EventSet: list of EventContent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = EventContent()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullFileTask(AbstractModel):
    """视频转拉任务信息

    """

    def __init__(self):
        """
        :param TaskId: 转拉上传任务 ID。
        :type TaskId: str
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 转拉上传完成后生成的视频 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileUrl: 转拉上传完成后生成的播放地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUrl: str
        :param ProcedureTaskId: 若转拉上传时指定了视频处理流程，则该参数为流程任务 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcedureTaskId: str
        """
        self.TaskId = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileUrl = None
        self.ProcedureTaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")
        self.ProcedureTaskId = params.get("ProcedureTaskId")


class ResetProcedureTemplateRequest(AbstractModel):
    """ResetProcedureTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 任务流名字
        :type Name: str
        :param MediaProcessTask: 视频处理类型任务参数。
        :type MediaProcessTask: :class:`tencentcloud.vod.v20180717.models.MediaProcessTaskInput`
        :param AiContentReviewTask: AI 智能内容审核类型任务参数。
        :type AiContentReviewTask: :class:`tencentcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: AI 智能内容分析类型任务参数。
        :type AiAnalysisTask: :class:`tencentcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: AI 内容识别类型任务参数。
        :type AiRecognitionTask: :class:`tencentcloud.vod.v20180717.models.AiRecognitionTaskInput`
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Name = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.SubAppId = params.get("SubAppId")


class ResetProcedureTemplateResponse(AbstractModel):
    """ResetProcedureTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SampleSnapshotTaskInput(AbstractModel):
    """对视频做采样截图任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板 ID。
        :type Definition: int
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        """
        self.Definition = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)


class SearchMediaRequest(AbstractModel):
    """SearchMedia请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 搜索文本，模糊匹配媒体文件名称或描述信息，匹配项越多，匹配度越高，排序越优先。长度限制：64 个字符。
        :type Text: str
        :param Tags: 标签集合，匹配集合中任意元素。
<li>单个标签长度限制：8 个字符。</li>
<li>数组长度限制：10。</li>
        :type Tags: list of str
        :param ClassIds: 分类 ID 集合，匹配集合指定 ID 的分类及其所有子类。数组长度限制：10。
        :type ClassIds: list of int
        :param StartTime: 创建时间的开始时间。
<li>大于等于开始时间。</li>
<li>格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。</li>
        :type StartTime: str
        :param EndTime: 创建时间的结束时间。
<li>小于结束时间。</li>
<li>格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。</li>
        :type EndTime: str
        :param SourceType: 媒体文件来源，来源取值参见 [SourceType](https://cloud.tencent.com/document/product/266/31773#MediaSourceData)。
        :type SourceType: str
        :param StreamId: 推流[直播码](https://cloud.tencent.com/document/product/267/5959)。
        :type StreamId: str
        :param Vid: 直播录制文件的唯一标识。
        :type Vid: str
        :param Sort: 排序方式。
<li>Sort.Field 可选值：CreateTime</li>
<li>指定 Text 搜索时，将根据匹配度排序，该字段无效</li>
        :type Sort: :class:`tencentcloud.vod.v20180717.models.SortBy`
        :param Offset: 偏移量。
<li>默认值：0。</li>
<li>取值范围：Offset + Limit 不超过 5000。</li>
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10。
        :type Limit: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.Text = None
        self.Tags = None
        self.ClassIds = None
        self.StartTime = None
        self.EndTime = None
        self.SourceType = None
        self.StreamId = None
        self.Vid = None
        self.Sort = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Tags = params.get("Tags")
        self.ClassIds = params.get("ClassIds")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SourceType = params.get("SourceType")
        self.StreamId = params.get("StreamId")
        self.Vid = params.get("Vid")
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class SearchMediaResponse(AbstractModel):
    """SearchMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合搜索条件的记录总数
<li>最大值：5000，即，当命中记录数超过 5000，该字段将返回 5000，而非实际命中总数。</li>
        :type TotalCount: int
        :param MediaInfoSet: 媒体文件信息列表，只包含基础信息（BasicInfo）
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfoSet: list of MediaInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MediaInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MediaInfoSet") is not None:
            self.MediaInfoSet = []
            for item in params.get("MediaInfoSet"):
                obj = MediaInfo()
                obj._deserialize(item)
                self.MediaInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class SimpleHlsClipRequest(AbstractModel):
    """SimpleHlsClip请求参数结构体

    """

    def __init__(self):
        """
        :param Url: 需要裁剪的腾讯云点播 HLS 视频 URL。
        :type Url: str
        :param StartTimeOffset: 裁剪的开始偏移时间，单位秒。默认 0，即从视频开头开始裁剪。负数表示距离视频结束多少秒开始裁剪。比如 -10 表示从倒数第 10 秒开始裁剪。
        :type StartTimeOffset: float
        :param EndTimeOffset: 裁剪的结束偏移时间，单位秒。默认 0，即裁剪到视频尾部。负数表示距离视频结束多少秒结束裁剪。比如 -10 表示到倒数第 10 秒结束裁剪。
        :type EndTimeOffset: float
        """
        self.Url = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class SimpleHlsClipResponse(AbstractModel):
    """SimpleHlsClip返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 裁剪后的视频地址。
        :type Url: str
        :param MetaData: 裁剪后的视频元信息。目前`Size`，`Rotate`，`VideoDuration`，`AudioDuration` 几个字段暂时缺省，没有真实数据。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class SnapshotByTimeOffset2017(AbstractModel):
    """截图输出信息（2017 版）

    """

    def __init__(self):
        """
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param TimeOffset: 截图的具体时间点，单位：毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeOffset: int
        :param Url: 截图输出文件地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self.ErrCode = None
        self.TimeOffset = None
        self.Url = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.TimeOffset = params.get("TimeOffset")
        self.Url = params.get("Url")


class SnapshotByTimeOffsetTask2017(AbstractModel):
    """视频指定时间点截图任务信息，该结构仅用于 2017 版[指定时间点截图](https://cloud.tencent.com/document/product/266/8102)接口发起的任务。

    """

    def __init__(self):
        """
        :param TaskId: 截图任务 ID。
        :type TaskId: str
        :param FileId: 截图文件 ID。
        :type FileId: str
        :param Definition: 截图规格，参见[指定时间点截图参数模板](https://cloud.tencent.com/document/product/266/11702#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param SnapshotInfoSet: 截图结果信息。
        :type SnapshotInfoSet: list of SnapshotByTimeOffset2017
        """
        self.TaskId = None
        self.FileId = None
        self.Definition = None
        self.SnapshotInfoSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.FileId = params.get("FileId")
        self.Definition = params.get("Definition")
        if params.get("SnapshotInfoSet") is not None:
            self.SnapshotInfoSet = []
            for item in params.get("SnapshotInfoSet"):
                obj = SnapshotByTimeOffset2017()
                obj._deserialize(item)
                self.SnapshotInfoSet.append(obj)


class SnapshotByTimeOffsetTaskInput(AbstractModel):
    """对视频按指定时间点截图任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板 ID。
        :type Definition: int
        :param TimeOffsetSet: 截图时间点列表，单位为秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeOffsetSet: list of float
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        """
        self.Definition = None
        self.TimeOffsetSet = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.TimeOffsetSet = params.get("TimeOffsetSet")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)


class SortBy(AbstractModel):
    """排序依据

    """

    def __init__(self):
        """
        :param Field: 排序字段
        :type Field: str
        :param Order: 排序方式，可选值：Asc（升序）、Desc（降序）
        :type Order: str
        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")


class SvgWatermarkInput(AbstractModel):
    """SVG水印模板输入参数

    """

    def __init__(self):
        """
        :param Width: 水印的宽度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素；当填 0px 且
 Height 不为 0px 时，表示水印的宽度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的宽度取原始 SVG 图像的宽度；</li>
<li>当字符串以 W% 结尾，表示水印 Width 为视频宽度的百分比大小，如 10W% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Width 为视频高度的百分比大小，如 10H% 表示 Width 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Width 为视频短边的百分比大小，如 10S% 表示 Width 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Width 为视频长边的百分比大小，如 10L% 表示 Width 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 W%。</li>
默认值为 10W%。
        :type Width: str
        :param Height: 水印的高度，支持 px，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；当填 0px 且
 Width 不为 0px 时，表示水印的高度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的高度取原始 SVG 图像的高度；</li>
<li>当字符串以 W% 结尾，表示水印 Height 为视频宽度的百分比大小，如 10W% 表示 Height 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Height 为视频高度的百分比大小，如 10H% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Height 为视频短边的百分比大小，如 10S% 表示 Height 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Height 为视频长边的百分比大小，如 10L% 表示 Height 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 H%。</li>
默认值为 0px。
        :type Height: str
        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class SvgWatermarkInputForUpdate(AbstractModel):
    """SVG水印模板输入参数

    """

    def __init__(self):
        """
        :param Width: 水印的宽度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素；当填 0px 且
 Height 不为 0px 时，表示水印的宽度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的宽度取原始 SVG 图像的宽度；</li>
<li>当字符串以 W% 结尾，表示水印 Width 为视频宽度的百分比大小，如 10W% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Width 为视频高度的百分比大小，如 10H% 表示 Width 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Width 为视频短边的百分比大小，如 10S% 表示 Width 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Width 为视频长边的百分比大小，如 10L% 表示 Width 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 W%。</li>
默认值为 10W%。
        :type Width: str
        :param Height: 水印的高度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；当填 0px 且
 Width 不为 0px 时，表示水印的高度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的高度取原始 SVG 图像的高度；</li>
<li>当字符串以 W% 结尾，表示水印 Height 为视频宽度的百分比大小，如 10W% 表示 Height 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Height 为视频高度的百分比大小，如 10H% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Height 为视频短边的百分比大小，如 10S% 表示 Height 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Height 为视频长边的百分比大小，如 10L% 表示 Height 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 H%。
默认值为 0px。
        :type Height: str
        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class TagConfigureInfo(AbstractModel):
    """智能标签任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能标签任务开关，可选值：
<li>ON：开启智能标签任务；</li>
<li>OFF：关闭智能标签任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class TagConfigureInfoForUpdate(AbstractModel):
    """智能标签任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能标签任务开关，可选值：
<li>ON：开启智能标签任务；</li>
<li>OFF：关闭智能标签任务。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class TaskSimpleInfo(AbstractModel):
    """任务概要信息

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param TaskType: 任务类型，取值：
<li>Procedure：视频处理任务；</li>
<li>EditMedia：视频编辑任务</li>
<li>WechatDistribute：微信发布任务。</li>
兼容 2017 版的任务类型：
<li>Transcode：视频转码任务；</li>
<li>SnapshotByTimeOffset：视频截图任务；</li>
<li>Concat：视频拼接任务；</li>
<li>Clip：视频剪辑任务；</li>
<li>ImageSprites：截取雪碧图任务。</li>
        :type TaskType: str
        :param CreatTime: 任务创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreatTime: str
        :param BeginProcessTime: 任务开始执行时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。若任务尚未开始，该字段为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginProcessTime: str
        :param FinishTime: 任务结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。若任务尚未完成，该字段为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: str
        """
        self.TaskId = None
        self.TaskType = None
        self.CreatTime = None
        self.BeginProcessTime = None
        self.FinishTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.CreatTime = params.get("CreatTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")


class TempCertificate(AbstractModel):
    """临时凭证

    """

    def __init__(self):
        """
        :param SecretId: 临时安全证书 Id。
        :type SecretId: str
        :param SecretKey: 临时安全证书 Key。
        :type SecretKey: str
        :param Token: Token 值。
        :type Token: str
        :param ExpiredTime: 证书无效的时间，返回 Unix 时间戳，精确到秒。
        :type ExpiredTime: int
        """
        self.SecretId = None
        self.SecretKey = None
        self.Token = None
        self.ExpiredTime = None


    def _deserialize(self, params):
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Token = params.get("Token")
        self.ExpiredTime = params.get("ExpiredTime")


class TextWatermarkTemplateInput(AbstractModel):
    """文字水印模板

    """

    def __init__(self):
        """
        :param FontType: 字体类型，目前仅支持 arial.ttf。
        :type FontType: str
        :param FontSize: 字体大小，格式：Npx，N 为数值。
        :type FontSize: str
        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（黑色）。
        :type FontColor: str
        :param FontAlpha: 文字透明度，取值范围：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>
默认值：1。
        :type FontAlpha: float
        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")


class TextWatermarkTemplateInputForUpdate(AbstractModel):
    """文字水印模板

    """

    def __init__(self):
        """
        :param FontType: 字体类型，目前仅支持 arial.ttf。
        :type FontType: str
        :param FontSize: 字体大小，格式：Npx，N 为数值。
        :type FontSize: str
        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（黑色）。
        :type FontColor: str
        :param FontAlpha: 文字透明度，取值范围：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>
        :type FontAlpha: float
        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")


class TranscodePlayInfo2017(AbstractModel):
    """视频转码播放信息（2017 版）

    """

    def __init__(self):
        """
        :param Url: 播放地址。
        :type Url: str
        :param Definition: 转码规格 ID，参见[转码参数模板](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和， 单位：bps。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
        :type Width: int
        """
        self.Url = None
        self.Definition = None
        self.Bitrate = None
        self.Height = None
        self.Width = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")


class TranscodeTask2017(AbstractModel):
    """视频转码任务信息，该结构仅用于对 2017 版[视频转码](https://cloud.tencent.com/document/product/266/7822)接口发起的任务。

    """

    def __init__(self):
        """
        :param TaskId: 转码任务 ID。
        :type TaskId: str
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 被转码文件 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileName: 被转码文件名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param Duration: 视频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param CoverUrl: 封面地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverUrl: str
        :param PlayInfoSet: 视频转码后生成的播放信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayInfoSet: list of TranscodePlayInfo2017
        """
        self.TaskId = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileName = None
        self.Duration = None
        self.CoverUrl = None
        self.PlayInfoSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.Duration = params.get("Duration")
        self.CoverUrl = params.get("CoverUrl")
        if params.get("PlayInfoSet") is not None:
            self.PlayInfoSet = []
            for item in params.get("PlayInfoSet"):
                obj = TranscodePlayInfo2017()
                obj._deserialize(item)
                self.PlayInfoSet.append(obj)


class TranscodeTaskInput(AbstractModel):
    """转码任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 视频转码模板 ID。
        :type Definition: int
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        """
        self.Definition = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)


class TranscodeTemplate(AbstractModel):
    """转码模板详情

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。
        :type Definition: str
        :param Container: 封装格式，取值：mp4、flv、hls、mp3、flac、ogg。
        :type Container: str
        :param Name: 转码模板名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Comment: 模板描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param Type: 模板类型，取值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param RemoveVideo: 是否去除视频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数，仅当 RemoveVideo 为 0，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoTemplate: :class:`tencentcloud.vod.v20180717.models.VideoTemplateInfo`
        :param AudioTemplate: 音频流配置参数，仅当 RemoveAudio 为 0，该字段有效 。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioTemplate: :class:`tencentcloud.vod.v20180717.models.AudioTemplateInfo`
        :param ContainerType: 封装格式过滤条件，可选值：
<li>Video：视频格式，可以同时包含视频流和音频流的封装格式；</li>
<li>PureAudio：纯音频格式，只能包含音频流的封装格式板。</li>
        :type ContainerType: str
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.Type = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.ContainerType = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Type = params.get("Type")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        self.ContainerType = params.get("ContainerType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class VideoTemplateInfo(AbstractModel):
    """视频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码</li>
<li>libx265：H.265 编码</li>
目前 H.265 编码必须指定分辨率，并且需要在 640*480 以内。
        :type Codec: str
        :param Fps: 视频帧率，取值范围：[0, 60]，单位：Hz。
当取值为 0，表示帧率和原始视频保持一致。
        :type Fps: int
        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。
当取值为 0，表示视频码率和原始视频保持一致。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的宽度，Height 表示视频的高度；</li>
<li>close：关闭，此时，Width 代表视频的长边，Height 表示视频的短边。</li>
默认值：open。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResolutionAdaptive: str
        :param Width: 视频流宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class VideoTemplateInfoForUpdate(AbstractModel):
    """视频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码</li>
<li>libx265：H.265 编码</li>
目前 H.265 编码必须指定分辨率，并且需要在 640*480 以内。
        :type Codec: str
        :param Fps: 视频帧率，取值范围：[0, 60]，单位：Hz。
当取值为 0，表示帧率和原始视频保持一致。
        :type Fps: int
        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。
当取值为 0，表示视频码率和原始视频保持一致。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的宽度，Height 表示视频的高度；</li>
<li>close：关闭，此时，Width 代表视频的长边，Height 表示视频的短边。</li>
        :type ResolutionAdaptive: str
        :param Width: 视频流宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
        :type Width: int
        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
        :type Height: int
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class WatermarkInput(AbstractModel):
    """视频处理任务中的水印参数类型

    """

    def __init__(self):
        """
        :param Definition: 水印模板 ID。
        :type Definition: int
        :param TextContent: 文字内容，长度不超过100个字符。仅当水印类型为文字水印时填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type TextContent: str
        :param SvgContent: SVG 内容。长度不超过 2000000 个字符。仅当水印类型为 SVG 水印时填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type SvgContent: str
        """
        self.Definition = None
        self.TextContent = None
        self.SvgContent = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.TextContent = params.get("TextContent")
        self.SvgContent = params.get("SvgContent")


class WatermarkTemplate(AbstractModel):
    """水印模板详情

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        :param Type: 水印类型，取值：
<li>image：图片水印；</li>
<li>text：文字水印。</li>
        :type Type: str
        :param Name: 水印模板名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param XPos: 水印图片原点距离视频图像原点的水平位置。
<li>当字符串以 % 结尾，表示水印 Left 为视频宽度指定百分比的位置，如 10% 表示 Left 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Left 为视频宽度指定像素的位置，如 100px 表示 Left 为 100 像素。</li>
        :type XPos: str
        :param YPos: 水印图片原点距离视频图像原点的垂直位置。
<li>当字符串以 % 结尾，表示水印 Top 为视频高度指定百分比的位置，如 10% 表示 Top 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Top 为视频高度指定像素的位置，如 100px 表示 Top 为 100 像素。</li>
        :type YPos: str
        :param ImageTemplate: 图片水印模板，仅当 Type 为 image，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTemplate: :class:`tencentcloud.vod.v20180717.models.ImageWatermarkTemplate`
        :param TextTemplate: 文字水印模板，仅当 Type 为 text，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTemplate: :class:`tencentcloud.vod.v20180717.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG 水印模板，当 Type 为 svg，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SvgTemplate: :class:`tencentcloud.vod.v20180717.models.SvgWatermarkInput`
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        :param CoordinateOrigin: 原点位置，可选值：
<li>topLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>topRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>bottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>bottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下。；</li>
        :type CoordinateOrigin: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CoordinateOrigin = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkTemplate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CoordinateOrigin = params.get("CoordinateOrigin")


class WechatPublishTask(AbstractModel):
    """微信发布任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param Status: 任务状态，取值：
WAITING：等待中；
PROCESSING：处理中；
FINISH：已完成。
        :type Status: str
        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 发布视频文件 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param Definition: 微信发布模板 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type Definition: int
        :param SourceDefinition: 发布视频所对应的转码模板 ID，为 0 代表原始视频。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceDefinition: int
        :param WechatStatus: 微信发布状态，取值：
<li>FAIL：失败；</li>
<li>SUCCESS：成功；</li>
<li>AUDITNOTPASS：审核未通过；</li>
<li>NOTTRIGGERED：尚未发起微信发布。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatStatus: str
        :param WechatVid: 微信 Vid。
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatVid: str
        :param WechatUrl: 微信地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatUrl: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.Definition = None
        self.SourceDefinition = None
        self.WechatStatus = None
        self.WechatVid = None
        self.WechatUrl = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.Definition = params.get("Definition")
        self.SourceDefinition = params.get("SourceDefinition")
        self.WechatStatus = params.get("WechatStatus")
        self.WechatVid = params.get("WechatVid")
        self.WechatUrl = params.get("WechatUrl")